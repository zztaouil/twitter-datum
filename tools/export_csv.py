"""
CSV export scenario — dumps users and tweets tables from DB to out/.

Usage: python tools/export_csv.py [db_path]
"""
import os
import sys
sys.path.insert(0, os.getcwd())  # $(pwd) so `src` resolves when run from project root

import src.core.db as db
from src.core.utils import write_csv


def run(conn) -> None:
    cur = conn.cursor()

    cur.execute("SELECT id, username, fullname, bio, location, followers, following, tweets_count, protected FROM users")
    users = [
        {"id": r[0], "username": r[1], "fullname": r[2], "bio": r[3], "location": r[4],
         "followers": r[5], "following": r[6], "tweets_count": r[7], "protected": bool(r[8])}
        for r in cur.fetchall()
    ]
    write_csv("out/users.csv", ["id", "username", "fullname", "bio", "location", "followers", "following", "tweets_count", "protected"], users)

    cur.execute("SELECT id, user_id, text, created_at, reply_count, retweet_count, like_count, view_count, parent_tweet_id FROM tweets")
    tweets = [
        {"id": r[0], "user_id": r[1], "text": r[2], "created_at": r[3],
         "reply_count": r[4], "retweet_count": r[5], "like_count": r[6], "view_count": r[7], "parent_tweet_id": r[8]}
        for r in cur.fetchall()
    ]
    write_csv("out/tweets.csv", ["id", "user_id", "text", "created_at", "reply_count", "retweet_count", "like_count", "view_count", "parent_tweet_id"], tweets)

    n_replies = sum(1 for t in tweets if t["parent_tweet_id"])
    print(f"exported {len(users)} users, {len(tweets) - n_replies} tweets, {n_replies} replies → out/users.csv, out/tweets.csv")


if __name__ == "__main__":
    path = sys.argv[1] if len(sys.argv) > 1 else "data.db"
    conn = db.init_db(path)
    run(conn)
