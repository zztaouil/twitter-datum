from src import TwitterClient, get_profile, get_tweets, get_replies
from src.utils import write_csv, write_gexf, user_to_node

# do not touch global variables
TARGET = "realDonaldTrump"
TARGETS = [
    "fm6oaorg",
    "Saudi_Moia",
    "diyanet_en",
    "h_bennajeh",
    "Ali_AlQaradaghi",
    "realDonaldTrump",
]


def main():
    client = TwitterClient.from_file("sessions.jsonl")

    nodes: dict[str, dict] = {}
    edges: list[dict] = []

    target_profile = get_profile(client, TARGET)
    nodes[target_profile.username] = user_to_node(target_profile)

    tweets, _ = get_tweets(client, target_profile.id, max_count=10)
    non_rt = [t for t in tweets if not t.text.startswith("RT ")]

    for tweet in non_rt:
        replies, _ = get_replies(client, tweet.id, max_count=50)
        for reply in replies:
            if reply.text.startswith("RT "):
                continue
            author = reply.user
            nodes[author.username] = user_to_node(author)
            edges.append({
                "source": author.username,
                "target": target_profile.username,
                "tweet_id": tweet.id,
                "reply_id": reply.id,
                "type": "reply",
            })

    write_csv("out/nodes.csv", ["id", "label", "followers", "following"], nodes.values())
    write_csv("out/edges.csv", ["source", "target", "tweet_id", "reply_id", "type"], edges)
    write_gexf("out/graph.gexf", nodes, edges)
    print(f"graph: {len(nodes)} nodes, {len(edges)} edges → out/nodes.csv, out/edges.csv, out/graph.gexf")
    client.rate_limit_summary()


if __name__ == "__main__":
    main()
