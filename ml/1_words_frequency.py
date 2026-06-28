import re
import sqlite3
import sys
from collections import Counter

STOPWORDS = {
    # English
    "the", "a", "an", "is", "to", "of", "in", "and", "for", "that", "this",
    "it", "at", "on", "with", "are", "was", "be", "as", "by", "we", "you",
    "i", "he", "she", "they", "have", "has", "had", "not", "but", "from",
    "or", "so", "do", "will", "all", "can", "my", "our", "your", "their",
    "more", "also", "about", "been", "its", "than", "his", "her", "if",
    # Arabic
    "في", "من", "على", "إلى", "أن", "هذا", "هذه", "التي", "الذي", "مع",
    "كان", "قد", "لا", "ما", "هو", "هي", "أو", "عن", "كل", "بعد",
    "قبل", "حتى", "إن", "لم", "لن", "عند", "عندما", "لقد", "كما",
    "وقد", "وهو", "وهي", "وما", "ذلك", "تلك", "هناك", "بين", "خلال",
    "ثم", "يكون", "يمكن", "منذ", "وأن", "وفي", "ولا", "أي", "أيضا",
    "بل", "ال", "له", "حين", "فيه", "ومن", "عليه",
    # Twitter noise
    "https", "http", "t", "co", "amp", "rt",
}


def word_frequency(conn, username: str, top_n: int = 30) -> list[tuple[str, int]]:
    rows = conn.execute(
        "SELECT t.text FROM tweets t JOIN users u ON t.user_id = u.id WHERE u.username = ? COLLATE NOCASE",
        (username,),
    ).fetchall()
    if not rows:
        return []
    words = [
        w for text in rows
        for w in re.findall(r'\b\w+\b', text[0].lower())
        if w not in STOPWORDS and not w.isdigit() and len(w) > 1
    ]
    return Counter(words).most_common(top_n)


def main():
    if len(sys.argv) < 2:
        print("usage: python ml/1_words_frequency.py <username> [top_n=30]")
        sys.exit(1)

    username = sys.argv[1]
    top_n = int(sys.argv[2]) if len(sys.argv) > 2 else 30

    conn = sqlite3.connect("data.db")
    results = word_frequency(conn, username, top_n)
    conn.close()

    if not results:
        print(f"no tweets found for @{username}")
        sys.exit(0)

    print(f"@{username} — top {top_n} words\n")
    for rank, (word, count) in enumerate(results, 1):
        print(f"  {rank:>3}. {word:<30} {count}")


if __name__ == "__main__":
    main()
