"""
Gephi scenario — reads reply graph from DB, exports nodes.csv, edges.csv, graph.gexf.

Usage: python tools/gephi_scenario.py [db_path]
"""
import os
import sys
sys.path.insert(0, os.getcwd())  # $(pwd) so `src` resolves when run from project root

import src.core.db as db
from src.core.utils import write_csv, write_gexf


def run(conn) -> None:
    cur = conn.cursor()
    cur.execute("""
        SELECT ru.username, ru.fullname, ru.followers, ru.following,
               ou.username, ou.fullname, ou.followers, ou.following,
               r.parent_tweet_id, r.id
        FROM tweets r
        JOIN users ru ON ru.id = r.user_id
        JOIN tweets o  ON o.id  = r.parent_tweet_id
        JOIN users ou ON ou.id = o.user_id
        WHERE r.parent_tweet_id IS NOT NULL
          AND r.text NOT LIKE 'RT %'
    """)
    nodes: dict[str, dict] = {}
    edges: list[dict] = []
    for src_u, src_label, src_f, src_fo, tgt_u, tgt_label, tgt_f, tgt_fo, tweet_id, reply_id in cur.fetchall():
        nodes[src_u] = {"id": src_u, "label": src_label, "followers": src_f, "following": src_fo}
        nodes[tgt_u] = {"id": tgt_u, "label": tgt_label, "followers": tgt_f, "following": tgt_fo}
        edges.append({"source": src_u, "target": tgt_u, "tweet_id": tweet_id, "reply_id": reply_id, "type": "reply"})

    write_csv("out/nodes.csv", ["id", "label", "followers", "following"], nodes.values())
    write_csv("out/edges.csv", ["source", "target", "tweet_id", "reply_id", "type"], edges)
    write_gexf("out/graph.gexf", nodes, edges)
    print(f"graph: {len(nodes)} nodes, {len(edges)} edges → out/nodes.csv, out/edges.csv, out/graph.gexf")


if __name__ == "__main__":
    path = sys.argv[1] if len(sys.argv) > 1 else "data.db"
    conn = db.init_db(path)
    run(conn)
