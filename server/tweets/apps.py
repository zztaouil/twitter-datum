from django.apps import AppConfig


class TweetsConfig(AppConfig):
    name = 'tweets'

    def ready(self):
        from django.db import connections

        # lives in the 'pins' db (server/db.sqlite3), not data.db — no cross-db FK possible
        with connections['pins'].cursor() as cur:
            cur.execute(
                """CREATE TABLE IF NOT EXISTS pinned_tweets (
                       tweet_id  TEXT PRIMARY KEY,
                       pinned_at TEXT DEFAULT CURRENT_TIMESTAMP
                   )"""
            )
