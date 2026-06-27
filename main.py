from pathlib import Path

from src import TwitterClient, get_profile, get_tweets


def main():
    client = TwitterClient.from_file("sessions.jsonl")

    targets = [
        line.strip().lstrip("@")
        for line in Path("targets.txt").read_text().splitlines()
        if line.strip()
    ]

    for username in targets:
        user = get_profile(client, username)
        tweets, _ = get_tweets(client, user.id)
        print(f"@{user.username} ({user.followers} followers) — {len(tweets)} tweets fetched")
        for t in tweets[:3]:
            print(f"  [{t.id}] {t.text[:80]!r}")


if __name__ == "__main__":
    main()
