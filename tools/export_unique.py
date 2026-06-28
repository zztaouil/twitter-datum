"""
Single-account export — creates out/<username>/ with nodes.csv, tweets.csv, graph.gexf.

nodes.csv  : profiles of users who replied to the target
tweets.csv : target's own tweets + all replies to them
graph.gexf : directed reply graph (replier → target)

Usage: python tools/export_csv_unique.py <username> [db_path]
"""
import os
import sys
sys.path.insert(0, os.getcwd())

import src.db as db
from src.utils import write_csv, write_gexf


def run(conn, username: str) -> None:
    cur = conn.cursor()

    cur.execute("SELECT id, fullname, followers, following FROM users WHERE username = ?", (username,))
    row = cur.fetchone()
    if not row:
        print(f"user '{username}' not found")
        return
    user_id, fullname, followers, following = row

    # target's own tweets
    cur.execute(
        "SELECT id, user_id, text, created_at, reply_count, retweet_count, like_count, view_count, parent_tweet_id "
        "FROM tweets WHERE user_id = ?",
        (user_id,)
    )
    own = cur.fetchall()
    own_ids = {r[0] for r in own}

    # replies to target's tweets
    cur.execute(
        f"SELECT id, user_id, text, created_at, reply_count, retweet_count, like_count, view_count, parent_tweet_id "
        f"FROM tweets WHERE parent_tweet_id IN ({','.join('?' * len(own_ids))}) AND user_id != ?",
        (*own_ids, user_id)
    ) if own_ids else None
    replies = cur.fetchall() if own_ids else []

    tweet_cols = ["id", "user_id", "text", "created_at", "reply_count", "retweet_count", "like_count", "view_count", "parent_tweet_id"]
    def to_tweet(r):
        return dict(zip(tweet_cols, r))

    tweets = [to_tweet(r) for r in own] + [to_tweet(r) for r in replies]

    # nodes: target + repliers
    replier_ids = {r[1] for r in replies}
    nodes: dict[str, dict] = {username: {"id": username, "label": fullname, "followers": followers, "following": following}}
    if replier_ids:
        cur.execute(
            f"SELECT username, fullname, followers, following FROM users WHERE id IN ({','.join('?' * len(replier_ids))})",
            tuple(replier_ids)
        )
        for u, fn, fo, fi in cur.fetchall():
            nodes[u] = {"id": u, "label": fn, "followers": fo, "following": fi}

    # edges: replier → target (one per reply)
    reply_user_map = {}
    if replier_ids:
        cur.execute(
            f"SELECT id, username FROM users WHERE id IN ({','.join('?' * len(replier_ids))})",
            tuple(replier_ids)
        )
        reply_user_map = {uid: uname for uid, uname in cur.fetchall()}

    edges = [
        {"source": reply_user_map[r[1]], "target": username,
         "tweet_id": r[8], "reply_id": r[0], "type": "reply"}
        for r in replies if r[1] in reply_user_map
    ]

    out_dir = f"out/{username}"
    os.makedirs(out_dir, exist_ok=True)

    write_csv(f"{out_dir}/tweets.csv", tweet_cols, tweets)
    write_csv(f"{out_dir}/users.csv", ["id", "label", "followers", "following"], nodes.values())
    write_gexf(f"{out_dir}/graph.gexf", nodes, edges)

    n_replies = sum(1 for t in tweets if t["parent_tweet_id"])
    print(f"@{username}: {len(own)} tweets, {len(replies)} replies from {len(nodes)-1} unique users")
    print(f"→ {out_dir}/tweets.csv, nodes.csv, graph.gexf")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("usage: python tools/export_csv_unique.py <username> [db_path]")
        sys.exit(1)
    username = sys.argv[1]
    path = sys.argv[2] if len(sys.argv) > 2 else "data.db"
    conn = db.init_db(path)
    run(conn, username)
