#!/usr/bin/env python3
"""
Alpha extraction: fetch N tweets older than the oldest in DB for a given user,
with Y replies per tweet. Paginates the timeline backward until past the DB
boundary, then collects N more tweets going further back.
"""
import sys
import os
sys.path.insert(0, os.getcwd())  # $(pwd) so `src` resolves when run from project root

from datetime import datetime
from src import TwitterClient, get_profile, get_replies, get_tweets

import src.db as db

TARGETS = [
    "fm6oaorg",
    "Saudi_Moia",
    "diyanet_en",
    "h_bennajeh",
    "Ali_AlQaradaghi",
    "realDonaldTrump",
]
N = 20
Y = 10


def run_target(client, conn, target):
    row = conn.execute("SELECT id FROM users WHERE username = ?", (target,)).fetchone()
    if row:
        user_id = row[0]
    else:
        profile = get_profile(client, target)
        db.save_user(conn, profile)
        user_id = profile.id

    row = conn.execute(
        "SELECT created_at FROM tweets WHERE user_id = ? AND parent_tweet_id IS NULL"
        " ORDER BY created_at ASC LIMIT 1",
        (user_id,),
    ).fetchone()
    if not row:
        print(f"No tweets in DB for {target}. Run main.py first.")
        return

    oldest_in_db = datetime.fromisoformat(row[0])
    print(f"\n=== {target} | oldest in DB: {oldest_in_db:%Y-%m-%d %H:%M:%S UTC} ===")

    # ponytail: linear scan from newest; upgrade to search-based jump when search endpoint hash is known
    collected = []
    cursor = None
    while len(collected) < N:
        tweets, cursor = get_tweets(client, user_id, cursor=cursor, max_count=0)
        for t in tweets:
            if not t.text.startswith("RT ") and t.created_at < oldest_in_db:
                collected.append(t)
        if not cursor or not tweets:
            break

    collected = collected[:N]
    print(f"Collected {len(collected)} tweets older than {oldest_in_db:%Y-%m-%d}")

    for i, tweet in enumerate(collected, 1):
        print(f"[{i}/{len(collected)}] {tweet.id} ({tweet.created_at:%Y-%m-%d})", end="", flush=True)
        db.save_tweet(conn, tweet)
        replies, _ = get_replies(client, tweet.id, max_count=Y)
        for r in replies:
            db.save_tweet(conn, r, parent_tweet_id=tweet.id)
        print(f" → {len(replies)} replies")
        conn.commit()


def main():
    client = TwitterClient.from_file("sessions.jsonl")
    conn = db.init_db()

    for target in TARGETS:
        run_target(client, conn, target)

    client.rate_limit_summary()


if __name__ == "__main__":
    main()
