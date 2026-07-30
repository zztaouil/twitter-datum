from django.apps import AppConfig


class TweetsConfig(AppConfig):
    name = 'tweets'

    def ready(self):
        from django.db import connection

        with connection.cursor() as cur:
            cur.execute(
                """CREATE TABLE IF NOT EXISTS pinned_tweets (
                       tweet_id  TEXT PRIMARY KEY REFERENCES tweets(id),
                       pinned_at TEXT DEFAULT CURRENT_TIMESTAMP
                   )"""
            )
