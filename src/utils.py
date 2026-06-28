import csv
import math
import xml.etree.ElementTree as ET

from .models import User


def write_csv(path, fieldnames, rows):
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames)
        w.writeheader()
        w.writerows(rows)


def write_gexf(path, nodes: dict, edges: list):
    ET.register_namespace("", "http://gexf.net/1.3")
    ET.register_namespace("viz", "http://gexf.net/1.3/viz")

    gexf = ET.Element("gexf", {
        "xmlns": "http://gexf.net/1.3",
        "xmlns:viz": "http://gexf.net/1.3/viz",
        "version": "1.3",
    })
    graph = ET.SubElement(gexf, "graph", {"defaultedgetype": "directed"})

    node_attrs = ET.SubElement(graph, "attributes", {"class": "node"})
    ET.SubElement(node_attrs, "attribute", {"id": "followers", "title": "followers", "type": "integer"})
    ET.SubElement(node_attrs, "attribute", {"id": "following", "title": "following", "type": "integer"})

    edge_attrs = ET.SubElement(graph, "attributes", {"class": "edge"})
    ET.SubElement(edge_attrs, "attribute", {"id": "tweet_id", "title": "tweet_id", "type": "string"})
    ET.SubElement(edge_attrs, "attribute", {"id": "reply_id", "title": "reply_id", "type": "string"})

    nodes_el = ET.SubElement(graph, "nodes")
    n_nodes = len(nodes)
    for i, n in enumerate(nodes.values()):
        angle = 2 * math.pi * i / max(n_nodes, 1)
        node = ET.SubElement(nodes_el, "node", {"id": n["id"], "label": n["label"]})
        ET.SubElement(node, "viz:position", {
            "x": f"{500 * math.cos(angle):.2f}",
            "y": f"{500 * math.sin(angle):.2f}",
            "z": "0",
        })
        av = ET.SubElement(node, "attvalues")
        ET.SubElement(av, "attvalue", {"for": "followers", "value": str(n["followers"])})
        ET.SubElement(av, "attvalue", {"for": "following", "value": str(n["following"])})

    edges_el = ET.SubElement(graph, "edges")
    for i, e in enumerate(edges):
        edge = ET.SubElement(edges_el, "edge", {
            "id": str(i), "source": e["source"], "target": e["target"], "label": e["type"],
        })
        av = ET.SubElement(edge, "attvalues")
        ET.SubElement(av, "attvalue", {"for": "tweet_id", "value": e["tweet_id"]})
        ET.SubElement(av, "attvalue", {"for": "reply_id", "value": e["reply_id"]})

    ET.indent(gexf)
    ET.ElementTree(gexf).write(path, encoding="utf-8", xml_declaration=True)


def user_to_node(u: User) -> dict:
    return {
        "id": u.username,
        "label": u.fullname,
        "followers": u.followers,
        "following": u.following,
    }
