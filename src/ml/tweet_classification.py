"""Classify all tweets from src.config.TARGETS into the tm_reference taxonomy.

Same weighted keyword scoring as tweet_classification.ipynb, applied to every
tweet from every target instead of a 50-per-target sample. Writes a CSV with
columns: tweet_id, category.
"""
import csv
import math
import os
import re
import sqlite3
import sys
import time
from collections import Counter

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
sys.path.insert(0, PROJECT_ROOT)

from langdetect import DetectorFactory, LangDetectException, detect
from nltk.stem import ISRIStemmer, SnowballStemmer

from src.config import TARGETS
from src.ml.tm_reference import TOPIC_KEYWORDS

DetectorFactory.seed = 0

CATEGORIES = list(TOPIC_KEYWORDS.keys())
STEMMERS = {"ar": ISRIStemmer(), "fr": SnowballStemmer("french"), "en": SnowballStemmer("english")}

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


def stem_tokens(cleaned: str, lang: str) -> list[str]:
    text = AR_ALEF_RE.sub("ا", AR_DIACRITICS_RE.sub("", cleaned)) if lang == "ar" else cleaned.lower()
    tokens = re.findall(r"\w+", text, re.UNICODE)
    stem = STEMMERS[lang].stem
    return [stem(t) for t in tokens]


STEMMED_KEYWORDS = {
    cat: {lang: {stem_tokens(w, lang)[0] for w in words} for lang, words in langs.items()}
    for cat, langs in TOPIC_KEYWORDS.items()
}
ALL_KEYWORD_STEMS = {
    lang: set().union(*(STEMMED_KEYWORDS[cat][lang] for cat in CATEGORIES)) for lang in STEMMERS
}


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


def classify(rows: list[dict]) -> list[dict]:
    last_report = time.monotonic()
    processed = 0
    try:
        for i, r in enumerate(rows, 1):
            r["cleaned"] = clean_text(r["text"])
            r["lang"] = detect_lang(r["cleaned"])
            processed = i
            now = time.monotonic()
            if now - last_report >= 60:
                print(f"  processed {i}/{len(rows)}")
                last_report = now
    except KeyboardInterrupt:
        print(f"interrupted after {processed}/{len(rows)}, classifying what's done so far")

    rows = [r for r in rows[:processed] if r["lang"] in STEMMERS]
    for r in rows:
        r["tokens"] = stem_tokens(r["cleaned"], r["lang"])

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
            cat: sum(counts[t] * idf[lang].get(t, 0.0) for t in STEMMED_KEYWORDS[cat][lang]) / denom
            for cat in CATEGORIES
        }
        best = max(scores, key=lambda c: scores[c])
        r["category"] = best if scores[best] > 0 else "unclassified"
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


if __name__ == "__main__":
    main()
