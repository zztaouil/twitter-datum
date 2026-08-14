"""Classify all tweets from src.config.TARGETS into the tm_reference taxonomy.

Same weighted keyword scoring as tweet_classification.ipynb, applied to every
tweet from every target instead of a 50-per-target sample. Writes a CSV with
columns: tweet_id, category. A tweet scoring positively on more than one
category gets all of them, comma-separated and ranked strongest first (e.g.
"religious-referential,digital-influential") — that's how tweets combining
multiple aspects of discord show up downstream.
"""
import csv
import math
import os
import re
import sqlite3
import sys
import time
from collections import Counter
from concurrent.futures import ProcessPoolExecutor

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
sys.path.insert(0, PROJECT_ROOT)

from langdetect import DetectorFactory, LangDetectException, detect
from nltk.stem import ISRIStemmer, SnowballStemmer

from src.config import TARGETS
from src.ml.tm_reference import CONFOUND_PHRASES, TOPIC_KEYWORDS

DetectorFactory.seed = 0

CATEGORIES = list(TOPIC_KEYWORDS.keys())
STEMMERS = {"ar": ISRIStemmer(), "en": SnowballStemmer("english")}

# Guard against stemmer over-collapsing: e.g. "Fasting" -> "fast" collides with the
# unrelated common word "fast" (speed). A real inflection always has the stemmer
# strip at least one character (e.g. "fasting" -> "fast", "organisé" -> "organis",
# "استقرار" -> "قرر"). So a token that already IS the stem, unchanged, only counts
# as a hit if some source keyword is itself that short — otherwise it's coincidence,
# not an inflection of the longer keyword(s) that produced this stem. This applies
# uniformly across languages (no special-casing needed for Arabic's root stemmer).
STEM_NEEDS_INFLECTION: dict[str, set[str]] = {lang: set() for lang in STEMMERS}

URL_RE = re.compile(r"https?://\S+")
MENTION_RE = re.compile(r"@\w+")
HASHTAG_RE = re.compile(r"#(\w+)")
AR_DIACRITICS_RE = re.compile(r"[ؗ-ًؚ-ْ]")
AR_ALEF_RE = re.compile(r"[إأآ]")


def clean_text(text: str) -> str:
    text = URL_RE.sub("", text)
    text = MENTION_RE.sub("", text)
    text = HASHTAG_RE.sub(r"\1", text)
    return re.sub(r"\s+", " ", text).strip()


def detect_lang(cleaned: str) -> str:
    if len(cleaned) < 3:
        return "other"
    try:
        code = detect(cleaned)
    except LangDetectException:
        return "other"
    return code if code in STEMMERS else "other"


def _normalize(text: str, lang: str) -> str:
    return AR_ALEF_RE.sub("ا", AR_DIACRITICS_RE.sub("", text)) if lang == "ar" else text.lower()


def _strip_confounds(raw_tokens: list[str], lang: str) -> list[str]:
    phrases = CONFOUND_PHRASES.get(lang)
    if not phrases:
        return raw_tokens
    max_n = max(len(p) for p in phrases)
    out = []
    i = 0
    while i < len(raw_tokens):
        for n in range(min(max_n, len(raw_tokens) - i), 0, -1):
            if tuple(raw_tokens[i : i + n]) in phrases:
                i += n
                break
        else:
            out.append(raw_tokens[i])
            i += 1
    return out


def stem_tokens(cleaned: str, lang: str) -> list[str]:
    raw_tokens = _strip_confounds(re.findall(r"\w+", _normalize(cleaned, lang), re.UNICODE), lang)
    stem = STEMMERS[lang].stem
    stems = []
    for t in raw_tokens:
        s = stem(t)
        if len(t) == len(s) and s in STEM_NEEDS_INFLECTION[lang]:
            continue
        stems.append(s)
    return stems


# Multi-word/hyphenated keywords (e.g. "Temple Mount", "المسجد الأقصى") must match as a
# phrase: every component stem present in the tweet, not just the first word's stem.
STEMMED_KEYWORDS = {
    cat: {lang: {frozenset(stem_tokens(w, lang)) for w in words} for lang, words in langs.items()}
    for cat, langs in TOPIC_KEYWORDS.items()
}
_stem_keyword_lens: dict[str, dict[str, int]] = {lang: {} for lang in STEMMERS}
for _langs in TOPIC_KEYWORDS.values():
    for _lang, _words in _langs.items():
        for _w in _words:
            for _t in re.findall(r"\w+", _normalize(_w, _lang), re.UNICODE):
                _s = STEMMERS[_lang].stem(_t)
                _lens = _stem_keyword_lens[_lang]
                _lens[_s] = min(_lens.get(_s, len(_t)), len(_t))
for _lang, _lens in _stem_keyword_lens.items():
    for _s, _shortest_keyword_len in _lens.items():
        if _shortest_keyword_len > len(_s):
            STEM_NEEDS_INFLECTION[_lang].add(_s)

ALL_KEYWORD_STEMS = {
    lang: {s for cat in CATEGORIES for phrase in STEMMED_KEYWORDS[cat][lang] for s in phrase}
    for lang in STEMMERS
}


def phrase_weight(phrase: frozenset[str], counts: Counter, idf_lang: dict[str, float]) -> float:
    if not all(t in counts for t in phrase):
        return 0.0
    return min(counts[t] for t in phrase) * sum(idf_lang.get(t, 0.0) for t in phrase)


def pick_categories(scores: dict[str, float]) -> str:
    hits = sorted((c for c in scores if scores[c] > 0), key=lambda c: -scores[c])
    return ",".join(hits) if hits else "unclassified"


def load_tweets(conn: sqlite3.Connection) -> list[dict]:
    rows = []
    for target in TARGETS:
        for tweet_id, text in conn.execute(
            "SELECT t.id, t.text FROM tweets t JOIN users u ON t.user_id = u.id "
            "WHERE u.username = ? COLLATE NOCASE",
            (target,),
        ).fetchall():
            rows.append({"tweet_id": tweet_id, "text": text})
    return rows


def _prep_row(r: dict) -> dict:
    r["cleaned"] = clean_text(r["text"])
    r["lang"] = detect_lang(r["cleaned"])
    if r["lang"] in STEMMERS:
        r["tokens"] = stem_tokens(r["cleaned"], r["lang"])
    return r


def classify(rows: list[dict]) -> list[dict]:
    last_report = time.monotonic()
    prepped = []
    try:
        with ProcessPoolExecutor() as pool:
            for i, r in enumerate(pool.map(_prep_row, rows, chunksize=200), 1):
                prepped.append(r)
                now = time.monotonic()
                if now - last_report >= 60:
                    print(f"  processed {i}/{len(rows)}")
                    last_report = now
    except KeyboardInterrupt:
        print(f"interrupted after {len(prepped)}/{len(rows)}, classifying what's done so far")

    rows = [r for r in prepped if r["lang"] in STEMMERS]

    n_lang = Counter(r["lang"] for r in rows)
    df_counts = {lang: Counter() for lang in STEMMERS}
    for r in rows:
        for t in set(r["tokens"]) & ALL_KEYWORD_STEMS[r["lang"]]:
            df_counts[r["lang"]][t] += 1
    idf = {
        lang: {t: math.log((1 + n_lang[lang]) / (1 + c)) + 1 for t, c in df_counts[lang].items()}
        for lang in STEMMERS
    }

    for r in rows:
        lang, tokens = r["lang"], r["tokens"]
        if not tokens:
            r["category"] = "unclassified"
            continue
        counts = Counter(tokens)
        denom = math.log(2 + len(tokens))
        scores = {
            cat: sum(phrase_weight(p, counts, idf[lang]) for p in STEMMED_KEYWORDS[cat][lang]) / denom
            for cat in CATEGORIES
        }
        r["category"] = pick_categories(scores)
    return rows


def main():
    out_path = sys.argv[1] if len(sys.argv) > 1 else os.path.join(PROJECT_ROOT, "tweet_classifications.csv")

    conn = sqlite3.connect(os.path.join(PROJECT_ROOT, "data.db"))
    rows = load_tweets(conn)
    conn.close()
    print(f"loaded {len(rows)} tweets across {len(TARGETS)} targets")

    rows = classify(rows)
    print(Counter(r["category"] for r in rows))

    with open(out_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["tweet_id", "category"])
        writer.writeheader()
        for r in rows:
            writer.writerow({"tweet_id": r["tweet_id"], "category": r["category"]})
    print(f"wrote {out_path}")


def _selfcheck():
    assert "fast" not in stem_tokens("he would go down fast and hard", "en")
    assert stem_tokens("fasting", "en") == stem_tokens("fasted", "en") == ["fast"]
    # legitimate root-shared Arabic match must survive the guard (not a collision)
    assert "قرر" in stem_tokens("قرار", "ar")
    assert pick_categories({"a": 0.0, "b": 0.0}) == "unclassified"
    assert pick_categories({"a": 2.0, "b": 1.0, "c": 0.0}) == "a,b"
    # multi-word keyword ("Temple Mount") must require every component stem, not just the first
    phrase = frozenset(stem_tokens("Temple Mount", "en"))
    assert len(phrase) == 2
    idf_lang = {t: 1.0 for t in phrase}
    assert phrase_weight(phrase, Counter(["templ", "mount"]), idf_lang) == 2.0
    assert phrase_weight(phrase, Counter(["templ"]), idf_lang) == 0.0
    # confound phrases (proper nouns colliding with a keyword's stem) must not count
    assert "unit" not in stem_tokens("the united states and united nations", "en")
    assert "unit" in stem_tokens("we stand united in this", "en")
    assert "قطع" not in stem_tokens("جنوب قطاع غزة", "ar")


if __name__ == "__main__":
    _selfcheck()
    main()
