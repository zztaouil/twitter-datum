from django.core.management.base import BaseCommand
from django.db import connection

# ponytail: FTS5 external-content table indexes tweets.text without duplicating
# it; triggers keep it in sync on future insert/update/delete.
SETUP_SQL = """
CREATE VIRTUAL TABLE IF NOT EXISTS tweets_fts USING fts5(
    text, content='tweets', content_rowid='rowid'
);

CREATE TRIGGER IF NOT EXISTS tweets_ai AFTER INSERT ON tweets BEGIN
    INSERT INTO tweets_fts(rowid, text) VALUES (new.rowid, new.text);
END;
CREATE TRIGGER IF NOT EXISTS tweets_ad AFTER DELETE ON tweets BEGIN
    INSERT INTO tweets_fts(tweets_fts, rowid, text) VALUES('delete', old.rowid, old.text);
END;
CREATE TRIGGER IF NOT EXISTS tweets_au AFTER UPDATE ON tweets BEGIN
    INSERT INTO tweets_fts(tweets_fts, rowid, text) VALUES('delete', old.rowid, old.text);
    INSERT INTO tweets_fts(rowid, text) VALUES (new.rowid, new.text);
END;

CREATE INDEX IF NOT EXISTS idx_tweets_category ON tweets(category);
CREATE INDEX IF NOT EXISTS idx_tweets_created_at ON tweets(created_at);
CREATE INDEX IF NOT EXISTS idx_users_username ON users(username);
"""


class Command(BaseCommand):
    help = "Create the FTS5 search index and filter indexes on the tweets table (idempotent)."

    def handle(self, *args, **options):
        connection.connect()
        with connection.cursor() as cur:
            cur.execute("SELECT name FROM sqlite_master WHERE name = 'tweets_fts'")
            existed = cur.fetchone() is not None

        connection.connection.executescript(SETUP_SQL)

        with connection.cursor() as cur:
            if not existed:
                cur.execute("INSERT INTO tweets_fts(tweets_fts) VALUES ('rebuild')")
            cur.execute("SELECT count(*) FROM tweets_fts_docsize")
            (indexed,) = cur.fetchone()
        self.stdout.write(f"Search index ready ({indexed} tweets indexed).")
