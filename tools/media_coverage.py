#!/usr/bin/env python3
import sys, os
sys.path.insert(0, os.getcwd())
import src.core.db as db

conn = db.init_db()
rows = conn.execute("""
    SELECT media_type, COUNT(*) AS n
    FROM tweets
    WHERE parent_tweet_id IS NULL
    GROUP BY media_type
""").fetchall()

totals = {}
total_tweets = 0
for media_type, n in rows:
    total_tweets += n
    for t in (media_type.split(",") if media_type else ["pending"]):
        totals[t] = totals.get(t, 0) + n

types = sorted(totals, key=lambda t: (t != "pending", t))
w = max((len(t) for t in types), default=5) + 4

print("".join(f"{t:>{w}}" for t in types) + f"{'total':>{w}}")
print("".join(f"{totals[t]:>{w}}" for t in types) + f"{total_tweets:>{w}}")
