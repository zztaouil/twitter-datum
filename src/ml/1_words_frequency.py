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
    # French
    "le", "la", "les", "un", "une", "des", "du", "de", "au", "aux", "et",
    "ou", "où", "mais", "donc", "or", "ni", "car", "que", "qui", "quoi",
    "dont", "quel", "quelle", "quels", "quelles", "ce", "cet", "cette",
    "ces", "cela", "ça", "ceci", "celui", "celle", "ceux", "celles",
    "je", "tu", "il", "elle", "nous", "vous", "ils", "elles", "on",
    "me", "te", "se", "lui", "leur", "leurs", "y", "en",
    "mon", "ma", "mes", "ton", "ta", "tes", "son", "sa", "ses",
    "notre", "nos", "votre", "vos",
    "être", "suis", "es", "est", "sommes", "êtes", "sont", "été", "étais",
    "était", "étions", "étiez", "étaient",
    "avoir", "ai", "as", "a", "avons", "avez", "ont", "avais", "avait",
    "avions", "aviez", "avaient", "eu",
    "faire", "fais", "fait", "faisons", "faites", "font",
    "aller", "vais", "vas", "va", "allons", "allez", "vont",
    "pas", "ne", "plus", "moins", "très", "trop", "peu", "beaucoup",
    "bien", "mal", "aussi", "encore", "déjà", "toujours", "jamais",
    "ici", "là", "alors", "ainsi", "comme", "comment", "pourquoi",
    "quand", "si", "dans", "sur", "sous", "vers", "chez", "sans",
    "avec", "pour", "par", "entre", "pendant", "depuis", "jusque",
    "jusqu", "contre", "selon", "malgré",
    "tout", "toute", "tous", "toutes", "autre", "autres", "même", "mêmes",
    "quelque", "quelques", "chaque", "certain", "certains", "certaine",
    "certaines", "aucun", "aucune", "plusieurs",
    "cependant", "pourtant", "toutefois", "néanmoins", "ainsi",
    "d", "l", "j", "n", "c", "s", "m", "t", "qu",
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


def hashtag_frequency(conn, username: str, top_n: int = 30) -> list[tuple[str, int]]:
    rows = conn.execute(
        "SELECT t.text FROM tweets t JOIN users u ON t.user_id = u.id WHERE u.username = ? COLLATE NOCASE",
        (username,),
    ).fetchall()
    if not rows:
        return []
    hashtags = [
        h.lower() for text in rows
        for h in re.findall(r'#\w+', text[0])
    ]
    return Counter(hashtags).most_common(top_n)


def main():
    if len(sys.argv) < 2:
        print("usage: python src/ml/1_words_frequency.py <username> [top_n=30]")
        sys.exit(1)

    username = sys.argv[1]
    top_n = int(sys.argv[2]) if len(sys.argv) > 2 else 30

    conn = sqlite3.connect("data.db")
    results = word_frequency(conn, username, top_n)
    hashtags = hashtag_frequency(conn, username, top_n)
    conn.close()

    if not results:
        print(f"no tweets found for @{username}")
        sys.exit(0)

    print(f"@{username} — top {top_n} words\n")
    for rank, (word, count) in enumerate(results, 1):
        print(f"  {rank:>3}. {word:<30} {count}")

    print(f"\n@{username} — top {top_n} hashtags\n")
    if hashtags:
        for rank, (tag, count) in enumerate(hashtags, 1):
            print(f"  {rank:>3}. {tag:<30} {count}")
    else:
        print("  —")


if __name__ == "__main__":
    main()
