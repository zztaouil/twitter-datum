import sqlite3

from .models import User, Tweet


def init_db(path: str = "data.db") -> sqlite3.Connection:
    conn = sqlite3.connect(path)
    conn.executescript("""
        CREATE TABLE IF NOT EXISTS users (
            id           TEXT PRIMARY KEY,
            username     TEXT,
            fullname     TEXT,
            bio          TEXT,
            location     TEXT,
            followers    INTEGER,
            following    INTEGER,
            tweets_count INTEGER,
            protected    INTEGER
        );
        CREATE TABLE IF NOT EXISTS tweets (
            id              TEXT PRIMARY KEY,
            user_id         TEXT REFERENCES users(id),
            text            TEXT,
            created_at      TEXT,
            reply_count     INTEGER,
            retweet_count   INTEGER,
            like_count      INTEGER,
            view_count      INTEGER,
            parent_tweet_id TEXT
        );
        CREATE INDEX IF NOT EXISTS idx_tweets_parent ON tweets(parent_tweet_id);
        CREATE INDEX IF NOT EXISTS idx_tweets_user ON tweets(user_id);
    """)
    conn.commit()
    return conn


def save_user(conn: sqlite3.Connection, user: User) -> None:
    conn.execute(
        "INSERT OR REPLACE INTO users VALUES (?,?,?,?,?,?,?,?,?)",
        (user.id, user.username, user.fullname, user.bio, user.location,
         user.followers, user.following, user.tweets_count, int(user.protected)),
    )


def save_tweet(conn: sqlite3.Connection, tweet: Tweet, parent_tweet_id: str | None = None) -> None:
    save_user(conn, tweet.user)
    conn.execute(
        "INSERT OR REPLACE INTO tweets VALUES (?,?,?,?,?,?,?,?,?)",
        (tweet.id, tweet.user.id, tweet.text, tweet.created_at.isoformat(),
         tweet.reply_count, tweet.retweet_count, tweet.like_count, tweet.view_count,
         parent_tweet_id),
    )
