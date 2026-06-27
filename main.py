import json
from dataclasses import asdict
from src import TwitterClient, get_profile, get_tweets, get_replies

TARGET = "realDonaldTrump"

def main():
    client = TwitterClient.from_file("sessions.jsonl")

    user = get_profile(client, TARGET)
    tweets, _ = get_tweets(client, user.id, max_count=20)
    tweet = next(t for t in tweets if not t.text.startswith("RT "))

    replies, _ = get_replies(client, tweet.id, max_count=10)

    result = {
        "tweet": asdict(tweet),
        "replies": [asdict(r) for r in replies],
    }

    with open("out.json", "w") as f:
        json.dump(result, f, indent=2, default=str)
    print(f"saved tweet {tweet.id} + {len(replies)} replies to out.json")


if __name__ == "__main__":
    main()
