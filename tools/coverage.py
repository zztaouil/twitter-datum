#!/usr/bin/env python3
import sys, os
sys.path.insert(0, os.getcwd())
import src.db as db

conn = db.init_db()
rows = conn.execute("""
    SELECT u.username, u.tweets_count,
           COUNT(CASE WHEN t.parent_tweet_id IS NULL THEN 1 END) AS own,
           COUNT(t.id) AS total
    FROM users u
    LEFT JOIN tweets t ON t.user_id = u.id
    WHERE u.tweets_count > 0
    GROUP BY u.id
    ORDER BY u.tweets_count DESC
""").fetchall()

print(f"{'user':<25} {'profile':>8} {'own':>7} {'total':>7} {'pct':>7}")
print("-" * 58)
for username, profile, own, total in rows:
    pct = own / profile * 100
    print(f"{username:<25} {profile:>8} {own:>7} {total:>7} {pct:>6.1f}%")
