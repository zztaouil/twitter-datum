import time

from django.core.management.base import BaseCommand
from django.db import connection

QUERIES = [
    ("FTS match (common word)", "peace", None, None),
    ("FTS match (Arabic word)", "غزة", None, None),
    ("FTS match + category filter", "peace", "diplomatic-relational", None),
    ("FTS match + author filter", "peace", None, "IsraeliPM"),
    ("category filter, no query", None, "digital-influential", None),
    ("no filters (browse latest)", None, None, None),
]
RUNS = 20


def timed(fn, runs=RUNS):
    best = float("inf")
    for _ in range(runs):
        start = time.perf_counter()
        fn()
        best = min(best, time.perf_counter() - start)
    return best * 1000


class Command(BaseCommand):
    help = "Benchmark the search endpoint's underlying queries (best of N, cold cache excluded)."

    def handle(self, *args, **options):
        with connection.cursor() as cur:
            for label, q, category, author in QUERIES:
                where = ["t.category IS NOT NULL"]
                params = []
                if category:
                    where.append("(',' || COALESCE(t.category,'unclassified') || ',') LIKE %s")
                    params.append(f"%,{category},%")
                if author:
                    where.append("u.username = %s")
                    params.append(author)
                where_sql = " AND ".join(where)

                if q:
                    match = " ".join(f'"{w}"*' for w in q.split())
                    from_sql = "FROM tweets_fts f JOIN tweets t ON t.rowid = f.rowid JOIN users u ON u.id = t.user_id"
                    sql = f"SELECT t.id {from_sql} WHERE f.text MATCH %s AND {where_sql} ORDER BY bm25(tweets_fts) LIMIT 20"
                    run_params = [match, *params]
                else:
                    from_sql = "FROM tweets t JOIN users u ON u.id = t.user_id"
                    sql = f"SELECT t.id {from_sql} WHERE {where_sql} ORDER BY t.created_at DESC LIMIT 20"
                    run_params = params

                def run(sql=sql, run_params=run_params):
                    cur.execute(sql, run_params)
                    cur.fetchall()

                ms = timed(run)
                self.stdout.write(f"{label:38s} {ms:7.2f} ms  (best of {RUNS})")
