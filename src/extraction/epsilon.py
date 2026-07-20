#!/usr/bin/env python3
"""
Epsilon extraction: backfill `media_type` for tweets already in the DB.

Historical rows were saved before media_type existed, so this re-fetches
each one individually via get_tweet() (one API call per tweet — the only
way to recover the raw entities for an already-known tweet id) and UPDATEs
just that column. Idempotent/resumable: only processes media_type IS NULL
rows, so interrupting and rerunning simply picks up where it left off.
"""
import sys
import os
sys.path.insert(0, os.getcwd())  # $(pwd) so `src` resolves when run from project root

import random
import signal
import time
import traceback

import httpx

from src import TwitterClient, get_tweet
from src.config import TARGETS
from src.core.client import RateLimitError
import src.core.db as db

LOG_EVERY = 20
_WINDOW = 360  # 15-min rate-limit window in seconds

_stop = False


def _handle_sigint(sig, _):
    global _stop
    _stop = True
    print("\n[shutdown] finishing current tweet, then stopping…")


signal.signal(signal.SIGINT, _handle_sigint)


def _human_pause():
    # ponytail: same probabilistic window-skip + jitter as alpha/beta/gamma/delta
    if random.random() < 0.01:
        wait = _WINDOW + random.uniform(-30, 30)
        print(f"  [idle] skipping window ({wait:.0f}s)")
        deadline = time.time() + wait
        while time.time() < deadline and not _stop:
            time.sleep(1)
    else:
        time.sleep(random.uniform(0, 1.5))


def _backfill_one(client, conn, tweet_id: str) -> None:
    try:
        tweet = get_tweet(client, tweet_id)
    except (httpx.HTTPError, RateLimitError) as e:
        print(f"  [error] {tweet_id}: {e}, skipping (will retry next run)")
        return
    media_type = tweet.media_type if tweet else "unknown"
    conn.execute("UPDATE tweets SET media_type = ? WHERE id = ?", (media_type, tweet_id))


def run_target(client, conn, target: str):
    try:
        pending = conn.execute(
            """SELECT t.id FROM tweets t JOIN users u ON u.id = t.user_id
               WHERE u.username = ? COLLATE NOCASE AND t.media_type IS NULL""",
            (target,),
        ).fetchall()
        print(f"\n=== {target} | {len(pending)} tweet(s) missing media_type ===")
        for i, (tweet_id,) in enumerate(pending, 1):
            if _stop:
                break
            _backfill_one(client, conn, tweet_id)
            conn.commit()
            if i % LOG_EVERY == 0 or i == len(pending):
                print(f"  [{i}/{len(pending)}] {tweet_id}")
            _human_pause()
    except Exception:
        print(f"  [error] {target}: unhandled exception, skipping target")
        traceback.print_exc()


def _run_global_catchall(client, conn):
    # sweeps in reply tweets authored by third parties, not just the TARGETS themselves
    pending = conn.execute("SELECT id FROM tweets WHERE media_type IS NULL").fetchall()
    print(f"\n=== catch-all | {len(pending)} tweet(s) missing media_type (non-target authors) ===")
    for i, (tweet_id,) in enumerate(pending, 1):
        if _stop:
            break
        _backfill_one(client, conn, tweet_id)
        conn.commit()
        if i % LOG_EVERY == 0 or i == len(pending):
            print(f"  [{i}/{len(pending)}] {tweet_id}")
        _human_pause()


def main():
    client = TwitterClient.from_file("sessions.jsonl")
    conn = db.init_db()

    try:
        for target in TARGETS:
            if _stop:
                break
            run_target(client, conn, target)
        if not _stop:
            _run_global_catchall(client, conn)
    finally:
        conn.commit()
        client.rate_limit_summary()


if __name__ == "__main__":
    main()
