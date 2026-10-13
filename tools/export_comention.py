"""
Co-mention graph — nodes = users, edges = co-mentions (author + every @mention in the same tweet).
Pre-computes eigenvector centrality (size) and Louvain modularity (colour); layout is done in Gephi.

Usage: uv run python tools/export_comention.py ACCOUNT [ACCOUNT ...] [--limit 10000] [--db data.db]
       uv run python tools/export_comention.py          # self-check only

Gephi:
  1. Open out/comention_<acct>.gexf (undirected, merge strategy sum).
  2. Optional: Filters → Topology → Degree Range ≥ 2, then Statistics → Modularity + Eigenvector.
  3. Appearance → Partition modularity_class (colour), Ranking eigenvector 5–80 (size). Never Apply "Unique".
  4. Layout → OpenOrd (big graphs) or ForceAtlas2 LinLog + Prevent overlap (<2k nodes), then Noverlap.
  5. Preview → Edges: Rescale weight 0.1–2 (raw weights reach ~1700 px!), opacity 40, curved, colour mixed.
     Labels: font ~6, proportional size on. Export PNG/SVG.
"""
import argparse
import itertools
import os
import random
import re
import sys
sys.path.insert(0, os.getcwd())  # $(pwd) so `src` resolves when run from project root

import networkx as nx

MENTION = re.compile(r"(?<!\w)@([A-Za-z0-9_]{1,15})")
PALETTE = [  # one colour per big community, the rest grey
    (31, 119, 180), (255, 127, 14), (44, 160, 44), (214, 39, 40), (148, 103, 189), (140, 86, 75),
    (227, 119, 194), (23, 190, 207), (188, 189, 34), (255, 187, 120), (152, 223, 138), (174, 199, 232),
]
GREY = (190, 190, 190)


def build(rows) -> nx.Graph:
    """rows = [(author, text)] → weighted undirected co-mention graph."""
    g = nx.Graph()
    for author, text in rows:
        people = {author.lower(), *(m.lower() for m in MENTION.findall(text or ""))}
        g.add_node(author.lower())
        for a, b in itertools.combinations(sorted(people), 2):
            w = g.get_edge_data(a, b, {"weight": 0})["weight"]
            g.add_edge(a, b, weight=w + 1)
    return g


def style(g: nx.Graph) -> None:
    # numpy solver: power iteration stalls on star-shaped graphs. It rejects disconnected graphs,
    # so solve per component, scaled by component share so small islands stay small.
    eig = {}
    for comp in nx.connected_components(g):
        share = len(comp) / len(g)
        sub = nx.eigenvector_centrality_numpy(g.subgraph(comp), weight="weight") if len(comp) > 2 else dict.fromkeys(comp, 1)
        eig |= {n: v * share for n, v in sub.items()}
    communities = sorted(nx.community.louvain_communities(g, weight="weight", seed=42), key=len, reverse=True)
    top = max(eig.values()) or 1
    for cls, members in enumerate(communities):
        r, gr, b = PALETTE[cls] if cls < len(PALETTE) else GREY
        for n in members:
            g.nodes[n].update(
                label=n, eigenvector=eig[n], modularity_class=cls, degree=g.degree(n),
                viz={"size": 2 + 58 * eig[n] / top, "color": {"r": r, "g": gr, "b": b, "a": 1.0},
                     "position": {"x": random.uniform(-1000, 1000), "y": random.uniform(-1000, 1000), "z": 0.0}},
            )
    print(f"{len(communities)} communities (top sizes: {[len(c) for c in communities[:8]]})")
    print("top eigenvector:", ", ".join(n for n, _ in sorted(eig.items(), key=lambda kv: -kv[1])[:15]))


def run(conn, accounts: list[str], limit: int) -> None:
    rows = []
    for acct in accounts:
        cur = conn.execute("""
            SELECT u.username, t.text FROM tweets t JOIN users u ON u.id = t.user_id
            WHERE lower(u.username) = lower(?) AND t.parent_tweet_id IS NULL
            ORDER BY t.created_at DESC LIMIT ?
        """, (acct, limit))
        fetched = cur.fetchall()
        print(f"{acct}: {len(fetched)} tweets")
        rows += fetched
    g = build(rows)
    style(g)
    path = f"out/comention_{'_'.join(accounts)}.gexf"
    os.makedirs("out", exist_ok=True)
    nx.write_gexf(g, path)
    print(f"graph: {g.number_of_nodes()} nodes, {g.number_of_edges()} edges → {path}")


def selfcheck() -> None:
    g = build([("StateDept", "RT @SecRubio: met @POTUS and email a@b.com"), ("StateDept", "@secrubio again")])
    assert set(g.nodes) == {"statedept", "secrubio", "potus"}, g.nodes
    assert g["statedept"]["secrubio"]["weight"] == 2
    assert g["secrubio"]["potus"]["weight"] == 1
    print("selfcheck ok")


if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("accounts", nargs="*")
    p.add_argument("--limit", type=int, default=10000)
    p.add_argument("--db", default="data.db")
    args = p.parse_args()
    selfcheck()
    if args.accounts:
        import src.core.db as db
        run(db.init_db(args.db), args.accounts, args.limit)
