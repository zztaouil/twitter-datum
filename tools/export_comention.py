"""
Co-mention graph — nodes = users, edges = co-mentions (author + every @mention in the same tweet).
Pre-computes eigenvector centrality (size) and Louvain modularity (colour); layout is done in Gephi.

Usage: uv run python tools/export_comention.py ACCOUNT [ACCOUNT ...] [--depth 1] [--limit 10000] [--db data.db]
       uv run python tools/export_comention.py          # self-check only

Depth 1 reads the seed accounts' tweets. Each subsequent level reads tweets by
newly mentioned accounts, when those accounts have posts in the database.
Each author is expanded once, using up to --limit latest non-reply tweets.
Co-mention weights count contributing tweets. Accounts without posts remain leaf nodes.
Recursive exports use out/comention_<acct>_depth<N>.gexf.
Exports use GEXF 1.3 with visualization attributes for Gephi.

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
import sqlite3
import sys
sys.path.insert(0, os.getcwd())  # $(pwd) so `src` resolves when run from project root

import networkx as nx
from networkx.readwrite.gexf import GEXFWriter

MENTION = re.compile(r"(?<!\w)@([A-Za-z0-9_]{1,15})")
PALETTE = [  # one colour per big community, the rest grey
    (31, 119, 180), (255, 127, 14), (44, 160, 44), (214, 39, 40), (148, 103, 189), (140, 86, 75),
    (227, 119, 194), (23, 190, 207), (188, 189, 34), (255, 187, 120), (152, 223, 138), (174, 199, 232),
]
GREY = (190, 190, 190)


def build(rows) -> nx.Graph:
    """rows = [(author, text)] → weighted undirected co-mention graph."""
    g = nx.Graph()
    add_rows(g, rows)
    return g


def add_rows(g: nx.Graph, rows) -> None:
    """Accumulate tweets without replacing weights from previous levels."""
    for author, text in rows:
        people = {author.lower(), *(m.lower() for m in MENTION.findall(text or ""))}
        g.add_node(author.lower())
        for a, b in itertools.combinations(sorted(people), 2):
            w = g.get_edge_data(a, b, {"weight": 0})["weight"]
            g.add_edge(a, b, weight=w + 1)


def expand(conn, accounts: list[str], limit: int, depth: int) -> nx.Graph:
    """Expand each reached author once; depth counts rounds of authored tweets."""
    author_ids = {}
    for username, user_id in conn.execute("""
        SELECT DISTINCT u.username, u.id
        FROM users u JOIN tweets t ON t.user_id = u.id
        WHERE t.parent_tweet_id IS NULL
    """):
        if username:
            author_ids.setdefault(username.lower(), []).append(user_id)

    frontier = {acct.lstrip("@").lower() for acct in accounts}
    g = nx.Graph()
    g.add_nodes_from((acct, {"discovery_depth": 0}) for acct in frontier)
    expanded = set()
    for level in range(1, depth + 1):
        before = set(g)
        tweets = 0
        authors = 0
        for acct in sorted(frontier - expanded):
            expanded.add(acct)
            ids = author_ids.get(acct)
            if not ids:
                continue
            placeholders = ",".join("?" for _ in ids)
            rows = conn.execute(f"""
                SELECT u.username, t.text FROM tweets t JOIN users u ON u.id = t.user_id
                WHERE t.user_id IN ({placeholders}) AND t.parent_tweet_id IS NULL
                ORDER BY t.created_at DESC, t.id DESC LIMIT ?
            """, (*ids, limit)).fetchall()
            authors += 1
            tweets += len(rows)
            add_rows(g, rows)
        frontier = set(g) - before
        for acct in frontier:
            g.nodes[acct]["discovery_depth"] = level
        print(f"depth {level}: {g.number_of_nodes()} nodes, {g.number_of_edges()} edges "
              f"({authors} authors expanded, {tweets} tweets, {len(frontier)} new users)")
        if not frontier:
            print(f"expansion saturated at depth {level}")
            break
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


def write_gexf(g: nx.Graph, path) -> None:
    """Write GEXF 1.3, retaining node attributes, edge weights, and styling."""
    writer = GEXFWriter(g, version="1.3")
    # NetworkX 3.6.1's 1.3 entry omits 'www.' from the XML Schema namespace.
    writer.xml.set("xmlns:xsi", "http://www.w3.org/2001/XMLSchema-instance")
    with open(path, "wb") as output:
        writer.write(output)


def run(conn, accounts: list[str], limit: int, depth: int = 1) -> None:
    g = expand(conn, accounts, limit, depth)
    style(g)
    suffix = f"_depth{depth}" if depth > 1 else ""
    path = f"out/comention_{'_'.join(acct.lstrip('@') for acct in accounts)}{suffix}.gexf"
    os.makedirs("out", exist_ok=True)
    write_gexf(g, path)
    print(f"graph: {g.number_of_nodes()} nodes, {g.number_of_edges()} edges → {path}")


def selfcheck() -> None:
    g = build([("StateDept", "RT @SecRubio: met @POTUS and email a@b.com"), ("StateDept", "@secrubio again")])
    assert set(g.nodes) == {"statedept", "secrubio", "potus"}, g.nodes
    assert g["statedept"]["secrubio"]["weight"] == 2
    assert g["secrubio"]["potus"]["weight"] == 1
    # Branches, cycles, leaf accounts, and repeated co-mentions across authors.
    with sqlite3.connect(":memory:") as conn:
        conn.executescript("""
            CREATE TABLE users (id TEXT, username TEXT);
            CREATE TABLE tweets (id TEXT, user_id TEXT, text TEXT, created_at TEXT, parent_tweet_id TEXT);
            INSERT INTO users VALUES ('1', 'Seed'), ('2', 'Branch'), ('3', 'Next');
            INSERT INTO tweets VALUES
                ('1', '1', '@Branch @Leaf', '2026-01-01', NULL),
                ('2', '2', '@Seed @Next', '2026-01-01', NULL),
                ('3', '3', '@Branch @End', '2026-01-01', NULL),
                ('4', '1', '@ReplyOnly', '2026-01-02', '1');
        """)
        first = expand(conn, ["@SEED"], 10000, 1)
        assert set(first) == {"seed", "branch", "leaf"}
        third = expand(conn, ["Seed"], 10000, 3)
        assert set(third) == {"seed", "branch", "leaf", "next", "end"}
        assert third["seed"]["branch"]["weight"] == 2
        assert third["branch"]["next"]["weight"] == 2
        assert third.nodes["end"]["discovery_depth"] == 3
        saturated = expand(conn, ["Seed"], 10000, 6)
        assert dict(third.edges) == dict(saturated.edges)
    print("selfcheck ok")


if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("accounts", nargs="*")
    p.add_argument("--limit", type=int, default=10000)
    p.add_argument("--depth", type=int, default=1)
    p.add_argument("--db", default="data.db")
    args = p.parse_args()
    if args.limit < 1 or args.depth < 1:
        p.error("--limit and --depth must be positive integers")
    if args.accounts:
        from pathlib import Path
        with sqlite3.connect(Path(args.db).resolve().as_uri() + "?mode=ro", uri=True) as conn:
            run(conn, args.accounts, args.limit, args.depth)
    else:
        selfcheck()
