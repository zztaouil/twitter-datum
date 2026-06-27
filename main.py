import src.db as db
from src import TwitterClient, get_profile, get_tweets, get_replies

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
    conn = db.init_db()

    for target in TARGETS:
        print(f"→ {target}")
        target_profile = get_profile(client, target)
        db.save_user(conn, target_profile)

        tweets, _ = get_tweets(client, target_profile.id, max_count=100)
        non_rt = [t for t in tweets if not t.text.startswith("RT ")]

        for tweet in non_rt:
            db.save_tweet(conn, tweet)
            replies, _ = get_replies(client, tweet.id, max_count=200)
            for reply in replies:
                db.save_tweet(conn, reply, parent_tweet_id=tweet.id)

    conn.commit()
    # run_gephi_scenario(conn)
    client.rate_limit_summary()


if __name__ == "__main__":
    main()
