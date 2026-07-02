import os
import sys
sys.path.insert(0, os.getcwd())  # $(pwd) so `src` resolves when run from project root

import re
import sqlite3
import sys
from collections import Counter, defaultdict
from dataclasses import dataclass

from bertopic import BERTopic
from hdbscan import HDBSCAN
from langdetect import DetectorFactory, LangDetectException, detect
from sentence_transformers import SentenceTransformer
from sklearn.feature_extraction.text import CountVectorizer
from umap import UMAP

DetectorFactory.seed = 0

STOPWORDS_EN = {
    "the", "a", "an", "is", "to", "of", "in", "and", "for", "that", "this",
    "it", "at", "on", "with", "are", "was", "be", "as", "by", "we", "you",
    "i", "he", "she", "they", "have", "has", "had", "not", "but", "from",
    "or", "so", "do", "will", "all", "can", "my", "our", "your", "their",
    "more", "also", "about", "been", "its", "than", "his", "her", "if",
}
STOPWORDS_AR = {
    "في", "من", "على", "إلى", "أن", "هذا", "هذه", "التي", "الذي", "مع",
    "كان", "قد", "لا", "ما", "هو", "هي", "أو", "عن", "كل", "بعد",
    "قبل", "حتى", "إن", "لم", "لن", "عند", "عندما", "لقد", "كما",
    "وقد", "وهو", "وهي", "وما", "ذلك", "تلك", "هناك", "بين", "خلال",
    "ثم", "يكون", "يمكن", "منذ", "وأن", "وفي", "ولا", "أي", "أيضا",
    "بل", "ال", "له", "حين", "فيه", "ومن", "عليه",
}
STOPWORDS_FR = {
    "le", "la", "les", "un", "une", "des", "de", "du", "et", "à", "en", "est",
    "que", "qui", "pour", "dans", "sur", "avec", "au", "aux", "ce", "cette",
    "ces", "il", "elle", "ils", "elles", "nous", "vous", "je", "tu", "on",
    "se", "sa", "son", "ses", "leur", "leurs", "ne", "pas", "plus", "être",
    "avoir", "fait", "faire", "sont", "été", "par", "ou", "mais", "donc",
    "or", "ni", "car", "si", "comme", "tout", "tous", "toute", "toutes",
    "aussi", "alors", "cela", "celui", "celle",
}
STOPWORDS = STOPWORDS_EN | STOPWORDS_AR | STOPWORDS_FR | {"https", "http", "t", "co", "amp", "rt"}

URL_RE = re.compile(r"https?://\S+")
MENTION_RE = re.compile(r"@\w+")
HASHTAG_RE = re.compile(r"#(\w+)")
_LANG_MAP = {"ar": "ar", "en": "en", "fr": "fr"}

_EMBEDDER = None


def _get_embedder() -> SentenceTransformer:
    global _EMBEDDER
    if _EMBEDDER is None:
        _EMBEDDER = SentenceTransformer("paraphrase-multilingual-MiniLM-L12-v2")
    return _EMBEDDER


def clean_text(text: str) -> str:
    text = URL_RE.sub("", text)
    text = MENTION_RE.sub("", text)
    text = HASHTAG_RE.sub(r"\1", text)
    return re.sub(r"\s+", " ", text).strip()


def detect_lang_bucket(cleaned: str) -> str:
    if len(cleaned) < 3:
        return "other"
    try:
        code = detect(cleaned)
    except LangDetectException:
        return "other"
    return _LANG_MAP.get(code, "other")


@dataclass
class Topic:
    id: int
    size: int
    keywords: list[str]
    examples: list[str]
    lang_breakdown: dict[str, float]


@dataclass
class TopicModelResult:
    n_docs: int
    topics: list[Topic]
    n_outliers: int
    skipped_reason: str | None = None


def topics_for_target(
    conn: sqlite3.Connection,
    username: str,
    n_topics: int | None = None,
    top_words: int = 8,
    n_examples: int = 2,
    min_docs: int = 15,
) -> TopicModelResult:
    rows = conn.execute(
        "SELECT t.text FROM tweets t JOIN users u ON t.user_id = u.id WHERE u.username = ? COLLATE NOCASE",
        (username,),
    ).fetchall()

    cleaned = [c for (raw,) in rows if (c := clean_text(raw))]
    if len(cleaned) < min_docs:
        return TopicModelResult(
            n_docs=len(cleaned), topics=[], n_outliers=0,
            skipped_reason=f"too few tweets ({len(cleaned)} < {min_docs})",
        )

    langs = [detect_lang_bucket(c) for c in cleaned]

    # ponytail: heuristic cluster-size floor, revisit if topics look too coarse/fine as corpus grows
    min_cluster_size = max(3, len(cleaned) // 25)

    vectorizer = CountVectorizer(stop_words=list(STOPWORDS), token_pattern=r"(?u)\b\w\w+\b")
    # n_neighbors must stay below the sample count or UMAP's embedding degenerates on small corpora
    n_neighbors = min(15, max(2, len(cleaned) - 1))
    umap_model = UMAP(n_neighbors=n_neighbors, n_components=5, min_dist=0.0, metric="cosine", random_state=42)
    hdbscan_model = HDBSCAN(
        min_cluster_size=min_cluster_size, metric="euclidean",
        cluster_selection_method="eom", prediction_data=True,
    )

    model = BERTopic(
        embedding_model=_get_embedder(),
        umap_model=umap_model,
        hdbscan_model=hdbscan_model,
        vectorizer_model=vectorizer,
        nr_topics=n_topics,
        calculate_probabilities=False,
        verbose=False,
    )
    topic_ids, _ = model.fit_transform(cleaned)

    lang_counts: dict[int, Counter] = defaultdict(Counter)
    for tid, lang in zip(topic_ids, langs):
        lang_counts[tid][lang] += 1

    topics = []
    n_outliers = 0
    for _, row in model.get_topic_info().iterrows():
        tid = int(row["Topic"])
        if tid == -1:
            n_outliers = int(row["Count"])
            continue
        words = [w for w, _ in model.get_topic(tid)[:top_words]]
        examples = model.get_representative_docs(tid)[:n_examples]
        total = sum(lang_counts[tid].values())
        breakdown = {l: round(c / total, 2) for l, c in lang_counts[tid].most_common()}
        topics.append(Topic(
            id=tid, size=int(row["Count"]), keywords=words,
            examples=examples, lang_breakdown=breakdown,
        ))

    return TopicModelResult(n_docs=len(cleaned), topics=topics, n_outliers=n_outliers)


def _fmt_breakdown(breakdown: dict[str, float]) -> str:
    return " / ".join(f"{pct:.0%} {lang.upper()}" for lang, pct in breakdown.items())


def main():
    if len(sys.argv) < 2:
        print("usage: python ml/2_topics_modeling.py <username> [n_topics]")
        sys.exit(1)

    username = sys.argv[1]
    n_topics = int(sys.argv[2]) if len(sys.argv) > 2 else None

    conn = sqlite3.connect("data.db")
    result = topics_for_target(conn, username, n_topics=n_topics)
    conn.close()

    if result.n_docs == 0:
        print(f"no tweets found for @{username}")
        sys.exit(0)

    if result.skipped_reason:
        print(f"@{username}: {result.skipped_reason}")
        sys.exit(0)

    print(f"@{username} — topics ({result.n_docs} tweets analyzed, {result.n_outliers} unclassified)\n")
    for topic in result.topics:
        print(f"Topic {topic.id} ({topic.size} tweets — {_fmt_breakdown(topic.lang_breakdown)}): {', '.join(topic.keywords)}")
        for ex in topic.examples:
            snippet = ex if len(ex) <= 120 else ex[:117] + "..."
            print(f'    e.g. "{snippet}"')
        print()


if __name__ == "__main__":
    main()
