from django.db import connection
from django.http import JsonResponse

from src.config import TARGETS

CATEGORIES = {"digital-influential", "diplomatic-relational", "religious-referential", "unclassified"}
MAX_PAGE_SIZE = 100


def _fts_match(q: str) -> str:
    # ponytail: quote+prefix each term so user input can't break FTS5 query syntax
    return " ".join('"' + term.replace('"', '""') + '"*' for term in q.split())


def search(request):
    q = request.GET.get("q", "").strip()
    category = request.GET.get("category", "").strip()
    author = request.GET.get("author", "").strip()
    date_from = request.GET.get("from", "").strip()
    date_to = request.GET.get("to", "").strip()
    page = max(int(request.GET.get("page") or 1), 1)
    page_size = min(max(int(request.GET.get("page_size") or 20), 1), MAX_PAGE_SIZE)

    where = ["(t.category IS NOT NULL)"]
    params: list = []

    if category:
        if category not in CATEGORIES:
            return JsonResponse({"error": "unknown category"}, status=400)
        where.append("COALESCE(t.category, 'unclassified') = %s")
        params.append(category)
    if author:
        where.append("u.username = %s")
        params.append(author)
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

    return JsonResponse({"results": results, "total": total, "page": page, "page_size": page_size})


def facets(request):
    with connection.cursor() as cur:
        cur.execute(
            """SELECT COALESCE(category, 'unclassified') AS c, count(*)
               FROM tweets WHERE category IS NOT NULL GROUP BY c ORDER BY c"""
        )
        categories = [{"value": c, "count": n} for c, n in cur.fetchall()]

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
