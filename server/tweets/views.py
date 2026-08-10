import json
from collections import Counter

from django.db import connection, connections
from django.http import HttpResponseNotAllowed, JsonResponse
from django.views.decorators.cache import cache_page

from src.config import TARGETS

# ponytail: data.db only changes when the scraper runs, not per request —
# cache the expensive analytics aggregations instead of recomputing every page load.
# in-memory (LocMemCache, Django's zero-config default), so a runserver reload clears it.
ANALYTICS_CACHE_SECONDS = 5 * 60

CATEGORIES = {"digital-influential", "diplomatic-relational", "religious-referential", "unclassified"}
MAX_PAGE_SIZE = 100


def _fts_match(q: str) -> str:
    # ponytail: quote+prefix each term so user input can't break FTS5 query syntax
    return " ".join('"' + term.replace('"', '""') + '"*' for term in q.split())


def _explode_categories(results: list[dict]) -> None:
    for r in results:
        r["categories"] = r.pop("category").split(",")


def _pinned_ids() -> set[str]:
    with connections["pins"].cursor() as cur:
        cur.execute("SELECT tweet_id FROM pinned_tweets")
        return {row[0] for row in cur.fetchall()}


def search(request):
    q = request.GET.get("q", "").strip()
    categories = [c.strip() for c in request.GET.getlist("category") if c.strip()]
    authors = [a.strip() for a in request.GET.getlist("author") if a.strip()]
    date_from = request.GET.get("from", "").strip()
    date_to = request.GET.get("to", "").strip()
    page = max(int(request.GET.get("page") or 1), 1)
    page_size = min(max(int(request.GET.get("page_size") or 20), 1), MAX_PAGE_SIZE)

    where = ["(t.category IS NOT NULL)"]
    params: list = []

    # tweets store their categories comma-separated (e.g. "religious-referential,digital-influential");
    # requiring a LIKE hit per selected category ANDs them together, so picking several
    # finds tweets that combine those aspects rather than tweets matching any one of them.
    for category in categories:
        if category not in CATEGORIES:
            return JsonResponse({"error": "unknown category"}, status=400)
        where.append("(',' || COALESCE(t.category, 'unclassified') || ',') LIKE %s")
        params.append(f"%,{category},%")
    if authors:
        placeholders = ", ".join(["%s"] * len(authors))
        where.append(f"u.username IN ({placeholders})")
        params.extend(authors)
    if date_from:
        where.append("t.created_at >= %s")
        params.append(date_from)
    if date_to:
        where.append("t.created_at <= %s")
        params.append(date_to + "T23:59:59")

    where_sql = " AND ".join(where)

    if q:
        from_sql = "FROM tweets_fts f JOIN tweets t ON t.rowid = f.rowid JOIN users u ON u.id = t.user_id"
        where_sql = "f.text MATCH %s AND " + where_sql
        params = [_fts_match(q)] + params
        order_sql = "ORDER BY bm25(tweets_fts)"
    else:
        from_sql = "FROM tweets t JOIN users u ON u.id = t.user_id"
        order_sql = "ORDER BY t.created_at DESC"

    with connection.cursor() as cur:
        cur.execute(f"SELECT count(*) {from_sql} WHERE {where_sql}", params)
        (total,) = cur.fetchone()

        cur.execute(
            f"""SELECT t.id, t.text, t.created_at, t.reply_count, t.retweet_count,
                       t.like_count, t.view_count, COALESCE(t.category, 'unclassified'),
                       u.username, u.fullname
                {from_sql} WHERE {where_sql} {order_sql} LIMIT %s OFFSET %s""",
            [*params, page_size, (page - 1) * page_size],
        )
        columns = [
            "id", "text", "created_at", "reply_count", "retweet_count",
            "like_count", "view_count", "category", "username", "fullname",
        ]
        results = [dict(zip(columns, row)) for row in cur.fetchall()]

    _explode_categories(results)
    pinned_ids = _pinned_ids()
    for r in results:
        r["pinned"] = r["id"] in pinned_ids

    return JsonResponse({"results": results, "total": total, "page": page, "page_size": page_size})


def pins(request):
    if request.method == "GET":
        with connections["pins"].cursor() as cur:
            cur.execute("SELECT tweet_id FROM pinned_tweets ORDER BY pinned_at DESC")
            pinned_ids = [row[0] for row in cur.fetchall()]

        if not pinned_ids:
            return JsonResponse({"results": []})

        placeholders = ", ".join(["%s"] * len(pinned_ids))
        with connection.cursor() as cur:
            cur.execute(
                f"""SELECT t.id, t.text, t.created_at, t.reply_count, t.retweet_count,
                           t.like_count, t.view_count, COALESCE(t.category, 'unclassified'),
                           u.username, u.fullname
                    FROM tweets t JOIN users u ON u.id = t.user_id
                    WHERE t.id IN ({placeholders})""",
                pinned_ids,
            )
            columns = [
                "id", "text", "created_at", "reply_count", "retweet_count",
                "like_count", "view_count", "category", "username", "fullname",
            ]
            by_id = {row[0]: dict(zip(columns, row)) for row in cur.fetchall()}

        _explode_categories(by_id.values())
        results = [by_id[i] for i in pinned_ids if i in by_id]
        return JsonResponse({"results": results})

    if request.method == "POST":
        tweet_id = str(json.loads(request.body or "{}").get("tweet_id", "")).strip()
        if not tweet_id:
            return JsonResponse({"error": "tweet_id required"}, status=400)
        with connections["pins"].cursor() as cur:
            cur.execute("INSERT OR IGNORE INTO pinned_tweets (tweet_id) VALUES (%s)", [tweet_id])
        return JsonResponse({"ok": True})

    if request.method == "DELETE":
        with connections["pins"].cursor() as cur:
            cur.execute("DELETE FROM pinned_tweets")
        return JsonResponse({"ok": True})

    return HttpResponseNotAllowed(["GET", "POST", "DELETE"])


def unpin(request, tweet_id):
    if request.method != "DELETE":
        return HttpResponseNotAllowed(["DELETE"])
    with connections["pins"].cursor() as cur:
        cur.execute("DELETE FROM pinned_tweets WHERE tweet_id = %s", [tweet_id])
    return JsonResponse({"ok": True})


@cache_page(ANALYTICS_CACHE_SECONDS)
def analytics(request):
    with connection.cursor() as cur:
        cur.execute(
            """SELECT u.username, COALESCE(t.category, 'unclassified')
               FROM tweets t JOIN users u ON u.id = t.user_id
               WHERE t.category IS NOT NULL"""
        )
        # a tweet with several categories counts once per category here (so the
        # per-target bars show every aspect it touches) but once in `tweet_totals`
        by_user: dict[str, Counter] = {}
        tweet_totals: Counter = Counter()
        for username, category in cur.fetchall():
            tweet_totals[username] += 1
            counts = by_user.setdefault(username, Counter())
            for c in category.split(","):
                counts[c] += 1

    ordered_categories = sorted(CATEGORIES)
    targets = [
        {
            "username": t,
            "categories": [
                {"value": c, "count": by_user.get(t, {}).get(c, 0)} for c in ordered_categories
            ],
            "total": tweet_totals.get(t, 0),
        }
        for t in TARGETS
    ]

    return JsonResponse({"targets": targets, "categories": ordered_categories})


@cache_page(ANALYTICS_CACHE_SECONDS)
def coverage(request):
    # profile tweets_count vs. tweets actually collected, per target (see tools/monitor.ipynb)
    # ponytail: scope the join to TARGETS up front instead of aggregating all 200k+ users
    # then discarding everything but TARGETS in Python (2s -> ~0.1s)
    placeholders = ", ".join(["%s"] * len(TARGETS))
    with connection.cursor() as cur:
        cur.execute(
            f"""SELECT u.username, u.tweets_count,
                       COALESCE(SUM(CASE WHEN t.parent_tweet_id IS NULL THEN 1 ELSE 0 END), 0) AS own,
                       COUNT(t.id) AS total
                FROM users u LEFT JOIN tweets t ON t.user_id = u.id
                WHERE u.username IN ({placeholders})
                GROUP BY u.id""",
            TARGETS,
        )
        by_user = {row[0]: row[1:] for row in cur.fetchall()}

    results = []
    for username in TARGETS:
        tweets_count, own, total = by_user.get(username, (0, 0, 0))
        pct = round(own / tweets_count * 100, 1) if tweets_count else 0
        results.append(
            {"username": username, "tweets_count": tweets_count, "own": own, "total": total, "pct": pct}
        )
    return JsonResponse({"results": results})


@cache_page(ANALYTICS_CACHE_SECONDS)
def media_backfill(request):
    # media_type backfill progress per target (see tools/monitor.ipynb)
    placeholders = ", ".join(["%s"] * len(TARGETS))
    with connection.cursor() as cur:
        cur.execute(
            f"""SELECT u.username,
                       COALESCE(SUM(CASE WHEN t.media_type IS NOT NULL THEN 1 ELSE 0 END), 0) AS done,
                       COUNT(t.id) AS total
                FROM users u LEFT JOIN tweets t ON t.user_id = u.id
                WHERE u.username IN ({placeholders})
                GROUP BY u.id""",
            TARGETS,
        )
        by_user = {row[0]: row[1:] for row in cur.fetchall()}

    results = []
    for username in TARGETS:
        done, total = by_user.get(username, (0, 0))
        pct = round(done / total * 100, 1) if total else 0
        results.append({"username": username, "done": done, "total": total, "pct": pct})
    return JsonResponse({"results": results})


@cache_page(ANALYTICS_CACHE_SECONDS)
def reply_depth(request):
    # level-1 vs level-2 reply coverage per target's own tweets (see tools/monitor.ipynb)
    placeholders = ", ".join(["%s"] * len(TARGETS))
    with connection.cursor() as cur:
        cur.execute(
            f"""WITH target_roots AS (
                    SELECT t.id AS root_id, u.username AS username
                    FROM tweets t JOIN users u ON u.id = t.user_id
                    WHERE t.parent_tweet_id IS NULL AND u.username IN ({placeholders})
                ),
                l1_map AS (
                    SELECT t.id AS l1_id, t.parent_tweet_id AS root_id
                    FROM tweets t WHERE t.parent_tweet_id IN (SELECT root_id FROM target_roots)
                ),
                l1 AS (
                    SELECT root_id, COUNT(*) AS n FROM l1_map GROUP BY root_id
                ),
                l2 AS (
                    SELECT lm.root_id AS root_id, COUNT(*) AS n
                    FROM tweets t2 JOIN l1_map lm ON t2.parent_tweet_id = lm.l1_id
                    GROUP BY lm.root_id
                )
                SELECT tr.username,
                       COUNT(*) AS tweets,
                       COALESCE(SUM(l1.n), 0) AS l1_replies,
                       COALESCE(SUM(l2.n), 0) AS l2_replies
                FROM target_roots tr
                LEFT JOIN l1 ON l1.root_id = tr.root_id
                LEFT JOIN l2 ON l2.root_id = tr.root_id
                GROUP BY tr.username""",
            TARGETS,
        )
        by_user = {row[0]: row[1:] for row in cur.fetchall()}

    results = []
    for username in TARGETS:
        tweets, l1_replies, l2_replies = by_user.get(username, (0, 0, 0))
        results.append(
            {
                "username": username,
                "tweets": tweets,
                "l1_replies": l1_replies,
                "l2_replies": l2_replies,
                "l1_per_tweet": round(l1_replies / tweets, 2) if tweets else 0,
                "l2_per_tweet": round(l2_replies / tweets, 2) if tweets else 0,
            }
        )
    return JsonResponse({"results": results})


def facets(request):
    with connection.cursor() as cur:
        cur.execute(
            """SELECT COALESCE(category, 'unclassified')
               FROM tweets WHERE category IS NOT NULL"""
        )
        cat_counts: Counter = Counter()
        for (c,) in cur.fetchall():
            cat_counts.update(c.split(","))
        categories = [{"value": c, "count": n} for c, n in sorted(cat_counts.items())]

        cur.execute(
            """SELECT u.username, u.fullname, count(*) n
               FROM tweets t JOIN users u ON u.id = t.user_id
               WHERE t.category IS NOT NULL
               GROUP BY u.id"""
        )
        counts = {u: (f, n) for u, f, n in cur.fetchall()}

    authors = sorted(
        (
            {"username": t, "fullname": counts.get(t, (t, 0))[0], "count": counts.get(t, (t, 0))[1]}
            for t in TARGETS
        ),
        key=lambda a: -a["count"],
    )

    return JsonResponse({"categories": categories, "authors": authors})
