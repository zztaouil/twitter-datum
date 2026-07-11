#!/usr/bin/env python3
"""
Beta extraction: date-range search sweep + replies timeline.

Strategy:
  1. Chunk the user's tweet history by month (from oldest tweet in DB to today)
     and exhaust each chunk via `from:user since:X until:Y include:nativeretweets` search.
     This bypasses the ~3200-tweet timeline cap and captures retweets.
  2. Also walk the UserWithProfileTweetsAndReplies timeline to catch recent
     replies-to-others that search may miss.
"""
import sys
import os
sys.path.insert(0, os.getcwd())

import random
import signal
import time
from datetime import date, datetime, timedelta, timezone

from src import TwitterClient, get_profile, get_tweets_and_replies, search_tweets
from src.config import TARGETS
import src.core.db as db

# chunk size in days for the search sweep
CHUNK_DAYS = 30
LOG_EVERY = 10
_WINDOW = 360

_stop = False


def _handle_sigint(sig, _):
    global _stop
    _stop = True
    print("\n[shutdown] finishing current chunk, then stopping…")


signal.signal(signal.SIGINT, _handle_sigint)


def _human_pause():
    # ponytail: probabilistic window skip + jitter; same as extraction_alpha
    if random.random() < 0.01:
        wait = _WINDOW + random.uniform(-30, 30)
        print(f"  [idle] skipping window ({wait:.0f}s)")
        deadline = time.time() + wait
        while time.time() < deadline and not _stop:
            time.sleep(1)
    else:
        time.sleep(random.uniform(0, 1.5))


def _date_chunks(start: date, end: date, days: int = CHUNK_DAYS):
    cur = start
    while cur < end:
        nxt = min(cur + timedelta(days=days), end)
        yield cur.isoformat(), nxt.isoformat()
        cur = nxt


def _load_existing(conn, user_id: str) -> set[str]:
    return {r[0] for r in conn.execute("SELECT id FROM tweets WHERE user_id = ?", (user_id,))}


def _save_new(conn, tweets, existing: set[str]) -> int:
    saved = 0
    for t in tweets:
        if t.id not in existing:
            db.save_tweet(conn, t)
            existing.add(t.id)
            saved += 1
    return saved


def _coverage(conn, user_id: str, tweets_count: int) -> str:
    n = conn.execute(
        "SELECT COUNT(*) FROM tweets WHERE user_id = ? AND parent_tweet_id IS NULL",
        (user_id,),
    ).fetchone()[0]
    pct = n / tweets_count * 100 if tweets_count else 0
    return f"{n}/{tweets_count} ({pct:.1f}%)"


def sweep_search(client, conn, username: str, user_id: str):
    """Chunk-by-month search sweep covering the full account history."""
    row = conn.execute(
        "SELECT MIN(created_at) FROM tweets WHERE user_id = ?", (user_id,)
    ).fetchone()
    if row[0]:
        start = date.fromisoformat(row[0][:10]) - timedelta(days=CHUNK_DAYS)
    else:
        # no tweets in DB yet; start from Twitter's founding
        start = date(2006, 1, 1)
    end = date.today() + timedelta(days=1)

    existing = _load_existing(conn, user_id)
    total_new = 0
    chunks = list(_date_chunks(start, end))
    print(f"  Search sweep: {len(chunks)} monthly chunks from {start} to {end}")

    for i, (since, until) in enumerate(chunks, 1):
        if _stop:
            break
        q = f"from:{username} since:{since} until:{until} include:nativeretweets"
        cursor = None
        chunk_new = 0
        while not _stop:
            tweets, cursor = search_tweets(client, q, cursor=cursor, max_count=0)
            chunk_new += _save_new(conn, tweets, existing)
            if not cursor or not tweets:
                break
            _human_pause()
        conn.commit()
        total_new += chunk_new
        if i % LOG_EVERY == 0 or i == len(chunks) or chunk_new:
            print(f"  [{i}/{len(chunks)}] {since}→{until}: +{chunk_new} new")

    print(f"  Search sweep done: +{total_new} tweets added")
    return total_new


def sweep_replies_timeline(client, conn, user_id: str):
    """Walk the tweets+replies timeline to catch recent replies-to-others."""
    existing = _load_existing(conn, user_id)
    total_new = 0
    cursor = None
    while not _stop:
        tweets, cursor = get_tweets_and_replies(client, user_id, cursor=cursor, max_count=0)
        total_new += _save_new(conn, tweets, existing)
        conn.commit()
        if not cursor or not tweets:
            break
        _human_pause()
    print(f"  Replies timeline done: +{total_new} tweets added")
    return total_new


def run_target(client, conn, target: str):
    profile = get_profile(client, target)
    db.save_user(conn, profile)
    print(f"\n=== {target} | profile tweets_count={profile.tweets_count} ===")
    print(f"  Before: {_coverage(conn, profile.id, profile.tweets_count)}")

    sweep_search(client, conn, target, profile.id)
    if not _stop:
        sweep_replies_timeline(client, conn, profile.id)

    print(f"  After:  {_coverage(conn, profile.id, profile.tweets_count)}")


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
