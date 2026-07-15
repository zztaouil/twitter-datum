#!/usr/bin/env python3
"""
Gamma extraction: reverse-chronological (today -> oldest) search sweep.

Strategy:
  Chunk each target's history by month, newest chunk first, and exhaust
  each via `from:user since:X until:Y include:nativeretweets` search.
  Same query beta.py uses (bypasses the ~3200-tweet timeline cap, captures
  retweets), just walked backward so an interrupted/killed run banks the
  most recent history first instead of grinding through ancient chunks.

  Meant to run unattended for a long stretch on a slow VPS: per-chunk and
  per-target errors are logged and skipped rather than crashing the run.
"""
import sys
import os
sys.path.insert(0, os.getcwd())

import random
import signal
import time
import traceback
from datetime import date, timedelta

import httpx

from src import TwitterClient, get_profile, search_tweets
from src.config import TARGETS
from src.core.client import RateLimitError
import src.core.db as db

CHUNK_DAYS = 30
LOG_EVERY = 10
MAX_EMPTY_CHUNKS = 5
FOUNDING = date(2006, 1, 1)
_WINDOW = 360  # 15-min rate-limit window in seconds
TARGET_COVERAGE = 25.0
PASS_PAUSE = 900  # 15min between passes, so we don't hammer already-swept targets

_stop = False


def _handle_sigint(sig, _):
    global _stop
    _stop = True
    print("\n[shutdown] finishing current chunk, then stopping…")


signal.signal(signal.SIGINT, _handle_sigint)


def _human_pause():
    # ponytail: probabilistic window skip + jitter; same as alpha/beta
    if random.random() < 0.01:
        wait = _WINDOW + random.uniform(-30, 30)
        print(f"  [idle] skipping window ({wait:.0f}s)")
        deadline = time.time() + wait
        while time.time() < deadline and not _stop:
            time.sleep(1)
    else:
        time.sleep(random.uniform(0, 1.5))


def _date_chunks_backward(start: date, floor: date, days: int = CHUNK_DAYS):
    cur = start
    while cur > floor:
        prev = max(cur - timedelta(days=days), floor)
        yield prev.isoformat(), cur.isoformat()
        cur = prev


def _load_existing(conn, user_id: str) -> set[str]:
    return {r[0] for r in conn.execute("SELECT id FROM tweets WHERE user_id = ?", (user_id,))}


def _save_new(conn, tweets, existing: set[str]) -> int:
    # always upsert so stats (likes/retweets/replies/views) refresh even for
    # already-known tweets; `existing` only tracks genuinely new rows for logging
    saved = 0
    for t in tweets:
        db.save_tweet(conn, t)
        if t.id not in existing:
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


def sweep_search_backward(client, conn, username: str, user_id: str):
    """Chunk-by-month search sweep, newest chunk to oldest, covering full account history."""
    start = date.today() + timedelta(days=1)

    existing = _load_existing(conn, user_id)
    total_new = 0
    chunks = list(_date_chunks_backward(start, FOUNDING))
    print(f"  Search sweep: {len(chunks)} monthly chunks from {start} back to {FOUNDING}")

    empty_streak = 0
    for i, (since, until) in enumerate(chunks, 1):
        if _stop:
            break
        q = f"from:{username} since:{since} until:{until} include:nativeretweets"
        cursor = None
        chunk_new = 0
        chunk_seen = 0
        try:
            while not _stop:
                tweets, cursor = search_tweets(client, q, cursor=cursor, max_count=0)
                chunk_seen += len(tweets)
                chunk_new += _save_new(conn, tweets, existing)
                if not cursor or not tweets:
                    break
                _human_pause()
        except (httpx.HTTPError, RateLimitError) as e:
            # ponytail: chunk-level skip-on-error, can leave a gap if a chunk
            # permanently fails - rerun beta's forward sweep periodically to
            # backfill any gaps this leaves
            print(f"  [{i}/{len(chunks)}] {since}->{until}: error, skipping chunk ({e})")
            continue
        conn.commit()
        total_new += chunk_new
        empty_streak = 0 if chunk_seen else empty_streak + 1
        if i % LOG_EVERY == 0 or i == len(chunks) or chunk_new:
            print(f"  [{i}/{len(chunks)}] {since}->{until}: +{chunk_new} new")
        if empty_streak >= MAX_EMPTY_CHUNKS:
            print(f"  {MAX_EMPTY_CHUNKS} consecutive empty chunks, assuming pre-account history, stopping sweep")
            break

    print(f"  Search sweep done: +{total_new} tweets added")
    return total_new


def run_target(client, conn, target: str):
    try:
        profile = get_profile(client, target)
        db.save_user(conn, profile)
        print(f"\n=== {target} | profile tweets_count={profile.tweets_count} ===")
        print(f"  Before: {_coverage(conn, profile.id, profile.tweets_count)}")

        sweep_search_backward(client, conn, target, profile.id)

        print(f"  After:  {_coverage(conn, profile.id, profile.tweets_count)}")
    except Exception:
        print(f"  [error] {target}: unhandled exception, skipping target")
        traceback.print_exc()


def _coverage_pct(conn, username: str) -> float:
    row = conn.execute(
        """SELECT u.tweets_count, COUNT(t.id) FROM users u
           LEFT JOIN tweets t ON t.user_id = u.id AND t.parent_tweet_id IS NULL
           WHERE u.username = ? GROUP BY u.id""",
        (username,),
    ).fetchone()
    if not row or not row[0]:
        return 0.0
    return row[1] / row[0] * 100


def main():
    client = TwitterClient.from_file("sessions.jsonl")
    conn = db.init_db()

    try:
        while not _stop:
            pending = sorted(
                (t for t in TARGETS if _coverage_pct(conn, t) < TARGET_COVERAGE),
                key=lambda t: _coverage_pct(conn, t),
            )
            if not pending:
                print(f"\nAll targets >= {TARGET_COVERAGE}% coverage, done.")
                break
            print(f"\n=== pass: {len(pending)} target(s) below {TARGET_COVERAGE}% ===")
            for target in pending:
                if _stop:
                    break
                run_target(client, conn, target)
            if _stop:
                break
            print(f"[pause] {PASS_PAUSE}s before next pass…")
            deadline = time.time() + PASS_PAUSE
            while time.time() < deadline and not _stop:
                time.sleep(1)
    finally:
        conn.commit()
        client.rate_limit_summary()


if __name__ == "__main__":
    main()
