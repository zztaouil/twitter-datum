"""Add `category` column to tweets and fill it from tweet_classifications.csv."""
import csv
import sqlite3
from pathlib import Path

DB = Path(__file__).parent.parent / "data.db"
CSV = Path(__file__).parent.parent / "tweet_classifications.csv"


def main():
    con = sqlite3.connect(DB)
    cols = [r[1] for r in con.execute("PRAGMA table_info(tweets)")]
    if "category" not in cols:
        con.execute("ALTER TABLE tweets ADD COLUMN category TEXT")

    with open(CSV, newline="") as f:
        rows = [(r["category"], r["tweet_id"]) for r in csv.DictReader(f)]

    con.executemany("UPDATE tweets SET category = ? WHERE id = ?", rows)
    con.commit()

    updated = con.execute("SELECT COUNT(*) FROM tweets WHERE category IS NOT NULL").fetchone()[0]
    print(f"{len(rows)} rows in csv, {updated} tweets now have a category")
    con.close()


if __name__ == "__main__":
    main()
