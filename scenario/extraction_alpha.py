#!/usr/bin/env python3
"""
Alpha extraction: fetch N tweets older than the oldest in DB for a given user,
with Y replies per tweet. Paginates the timeline backward until past the DB
boundary, then collects N more tweets going further back.
"""
import sys
import os
sys.path.insert(0, os.getcwd())  # $(pwd) so `src` resolves when run from project root

import random
import signal
import time
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
Y = 20
LOG_EVERY = 20
_WINDOW = 900  # 15-min rate-limit window in seconds

_stop = False


def _handle_sigint(sig, _):
    global _stop
    _stop = True
    print("\n[shutdown] finishing current tweet, then stopping…")


signal.signal(signal.SIGINT, _handle_sigint)


def _human_pause():
    # ponytail: probabilistic window skip + jitter; upgrade to token-budget pacing if fingerprinting becomes an issue
    if random.random() < 0.10:
        wait = _WINDOW + random.uniform(-60, 60)
        print(f"  [idle] skipping window ({wait:.0f}s)")
        time.sleep(wait)
    else:
        time.sleep(random.uniform(2, 18))


def run_target(client, conn, target):
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
    while len(collected) < N and not _stop:
        tweets, cursor = get_tweets(client, user_id, cursor=cursor, max_count=0)
        for t in tweets:
            if not t.text.startswith("RT ") and t.created_at < oldest_in_db:
                collected.append(t)
        if not cursor or not tweets:
            break

    collected = collected[:N]
    print(f"Collected {len(collected)} tweets older than {oldest_in_db:%Y-%m-%d}")

    total_replies = 0
    for i, tweet in enumerate(collected, 1):
        if _stop:
            break
        db.save_tweet(conn, tweet)
        replies, _ = get_replies(client, tweet.id, max_count=Y)
        for r in replies:
            db.save_tweet(conn, r, parent_tweet_id=tweet.id)
        total_replies += len(replies)
        conn.commit()

        if i % LOG_EVERY == 0 or i == len(collected):
            print(f"  [{i}/{len(collected)}] up to {tweet.created_at:%Y-%m-%d} | +{len(replies)} replies | total: {total_replies}")

        _human_pause()


def main():
    client = TwitterClient.from_file("sessions.jsonl")
    conn = db.init_db()

    try:
        for target in TARGETS:
            if _stop:
                break
            run_target(client, conn, target)
    finally:
        conn.commit()
        client.rate_limit_summary()


if __name__ == "__main__":
    main()
