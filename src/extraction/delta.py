#!/usr/bin/env python3
"""
Delta extraction: two-level reply graph.

Strategy:
  For each target's already-collected root tweets (from alpha/beta/gamma),
  fetch level-1 replies, then expand only the top-engagement level-1 replies
  to level-2 (replies to replies) — exhaustively expanding every reply is
  infeasible when a single tweet has 100k+ replies.

  Meant to run unattended for a long stretch on a slow VPS: per-target,
  per-root-tweet, and per-reply-expansion errors are logged and skipped
  rather than crashing the run.
"""
import sys
import os
sys.path.insert(0, os.getcwd())

import random
import signal
import time
import traceback

import httpx

from src import TwitterClient, get_replies
from src.config import TARGETS
from src.core.client import RateLimitError
import src.core.db as db

MAX_L1_REPLIES = 200   # reply pool cap per root tweet
MAX_L1_PAGES = 8
L1_TOP_K_FOR_L2 = 15    # only top-K by engagement, per root tweet, get expanded to level 2
MAX_L2_REPLIES = 50
MAX_L2_PAGES = 3
LOG_EVERY = 10
_WINDOW = 360  # 15-min rate-limit window in seconds
PASS_PAUSE = 900  # 15min between passes

_stop = False
_dead_ends: set[str] = set()  # ponytail: in-memory only; a reply that genuinely has 0 fetchable children


def _handle_sigint(sig, _):
    global _stop
    _stop = True
    print("\n[shutdown] finishing current unit of work, then stopping…")


signal.signal(signal.SIGINT, _handle_sigint)


def _human_pause():
    # ponytail: probabilistic window skip + jitter; same as alpha/beta/gamma
    if random.random() < 0.01:
        wait = _WINDOW + random.uniform(-30, 30)
        print(f"  [idle] skipping window ({wait:.0f}s)")
        deadline = time.time() + wait
        while time.time() < deadline and not _stop:
            time.sleep(1)
    else:
        time.sleep(random.uniform(0, 1.5))


def _fetch_reply_pool(client, tweet_id: str, cap: int, max_pages: int) -> list:
    # ponytail: get_replies(max_count=N) truncates mid-page without ever
    # reaching the cursor-bottom entry, so cursor comes back "" and pagination
    # silently breaks - always call with max_count=0 and cap here instead.
    pool = []
    cursor = None
    for _ in range(max_pages):
        if _stop or len(pool) >= cap:
            break
        tweets, cursor = get_replies(client, tweet_id, cursor=cursor, max_count=0)
        pool.extend(tweets)
        if not cursor or not tweets:
            break
        _human_pause()
    return pool[:cap]


def _engagement(row) -> int:
    return row[0] + row[1] + row[2]


def _pending_roots(conn, user_id: str):
    return conn.execute(
        """SELECT id, reply_count FROM tweets
           WHERE user_id = ? AND parent_tweet_id IS NULL AND reply_count > 0
           ORDER BY (like_count + retweet_count + reply_count) DESC""",
        (user_id,),
    ).fetchall()


def _pending_l1_for_l2(conn, root_id: str):
    return conn.execute(
        """SELECT r.id, r.reply_count FROM tweets r
           WHERE r.parent_tweet_id = ?
             AND r.reply_count > 0
             AND (SELECT COUNT(*) FROM tweets c2 WHERE c2.parent_tweet_id = r.id)
                 < MIN(r.reply_count, ?)
           ORDER BY (r.like_count + r.retweet_count + r.reply_count) DESC
           LIMIT ?""",
        (root_id, MAX_L2_REPLIES, L1_TOP_K_FOR_L2),
    ).fetchall()


def _process_root(client, conn, root_id: str, reply_count: int):
    try:
        if root_id not in _dead_ends:
            l1_children = conn.execute(
                "SELECT COUNT(*) FROM tweets WHERE parent_tweet_id = ?", (root_id,)
            ).fetchone()[0]
            if l1_children < min(reply_count, MAX_L1_REPLIES):
                pool = _fetch_reply_pool(client, root_id, MAX_L1_REPLIES, MAX_L1_PAGES)
                for r in pool:
                    db.save_tweet(conn, r, parent_tweet_id=root_id)
                if not pool:
                    _dead_ends.add(root_id)
                conn.commit()
    except (httpx.HTTPError, RateLimitError) as e:
        print(f"  [error] L1 expand root {root_id}: {e}, skipping")
        return

    for reply_id, _rc in _pending_l1_for_l2(conn, root_id):
        if _stop:
            break
        if reply_id in _dead_ends:
            continue
        try:
            pool = _fetch_reply_pool(client, reply_id, MAX_L2_REPLIES, MAX_L2_PAGES)
            for r in pool:
                db.save_tweet(conn, r, parent_tweet_id=reply_id)
            if not pool:
                _dead_ends.add(reply_id)
            conn.commit()
        except (httpx.HTTPError, RateLimitError) as e:
            print(f"  [error] L2 expand reply {reply_id}: {e}, skipping")
            continue
        _human_pause()


def run_target(client, conn, target: str):
    try:
        row = conn.execute(
            "SELECT id FROM users WHERE username = ? COLLATE NOCASE", (target,)
        ).fetchone()
        if not row:
            print(f"  [skip] {target}: no cached profile, run alpha/beta/gamma first")
            return
        user_id = row[0]
        roots = _pending_roots(conn, user_id)
        print(f"\n=== {target} | {len(roots)} root tweet(s) with replies ===")
        for i, (root_id, reply_count) in enumerate(roots, 1):
            if _stop:
                break
            _process_root(client, conn, root_id, reply_count)
            if i % LOG_EVERY == 0 or i == len(roots):
                print(f"  [{i}/{len(roots)}] root {root_id}")
    except Exception:
        print(f"  [error] {target}: unhandled exception, skipping target")
        traceback.print_exc()


def _target_has_pending(conn, username: str) -> bool:
    row = conn.execute("SELECT id FROM users WHERE username = ? COLLATE NOCASE", (username,)).fetchone()
    if not row:
        return False
    user_id = row[0]
    l1 = conn.execute(
        """SELECT COUNT(*) FROM tweets t
           WHERE t.user_id = ? AND t.parent_tweet_id IS NULL AND t.reply_count > 0
             AND (SELECT COUNT(*) FROM tweets c WHERE c.parent_tweet_id = t.id) < MIN(t.reply_count, ?)""",
        (user_id, MAX_L1_REPLIES),
    ).fetchone()[0]
    if l1:
        return True
    l2 = conn.execute(
        """SELECT COUNT(*) FROM tweets r
           JOIN tweets root ON root.id = r.parent_tweet_id
           WHERE root.user_id = ? AND root.parent_tweet_id IS NULL AND r.reply_count > 0
             AND (SELECT COUNT(*) FROM tweets c2 WHERE c2.parent_tweet_id = r.id) < MIN(r.reply_count, ?)""",
        (user_id, MAX_L2_REPLIES),
    ).fetchone()[0]
    return l2 > 0


def _top_engagement(conn, username: str) -> int:
    row = conn.execute(
        """SELECT MAX(t.like_count + t.retweet_count + t.reply_count)
           FROM tweets t JOIN users u ON u.id = t.user_id
           WHERE u.username = ? COLLATE NOCASE AND t.parent_tweet_id IS NULL""",
        (username,),
    ).fetchone()
    return row[0] or 0


def main():
    client = TwitterClient.from_file("sessions.jsonl")
    conn = db.init_db()

    try:
        while not _stop:
            pending = [t for t in TARGETS if _target_has_pending(conn, t)]
            if not pending:
                print("\nAll targets fully expanded to level 2 (within caps), done.")
                break
            pending.sort(key=lambda t: -_top_engagement(conn, t))
            print(f"\n=== pass: {len(pending)} target(s) with pending L1/L2 work ===")
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
