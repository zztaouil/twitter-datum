import src.core.db as db
from src import TwitterClient, get_profile, get_tweets, get_replies

# do not touch global variables
TARGET = "realDonaldTrump"
TARGETS = [
    "fm6oaorg",
    "MmedHamdaoui",
    "osekguub6096Gwf",
    "habousmaroc",
    "MarocDiplo_AR",
    "nosraorg",
    "USAbilAraby",
    "AIPACofficial",
    "TuckerCarlson",
    "SecRubio",
    "WhiteHouse",
    "CUFI",
    "TheIRD",
    "StateDept",
    "USIPorg",
    "Franklin_Graham",
    "SpeakerJohnson",
    "GovMikeHuckabee",
    "RTErdogan",
    "DiyanetDijital",
    "Tika_Turkiye",
    "mfa_russia",
    "KremlinRussia_E",
    "patriarchia_ru",
    "mospat_ru",
    "ar_khamenei",
    "IRIMFA_EN",
    "netanyahu",
    "IsraelMFA",
    "IsraelinUSA",
    "EdyCohen",
    "IsraeliPM",
    "IDF",
    "itamarbengvir",
    "bezalelsm",
    "Pontifex_ar",
    "vaticannews_fr",
    "AlAzhar",
    "alimamaltayeb",
]


def main():
    client = TwitterClient.from_file("sessions.jsonl")
    conn = db.init_db()

    for target in TARGETS:
        print(f"→ {target}")
        target_profile = get_profile(client, target)
        db.save_user(conn, target_profile)

        tweets, _ = get_tweets(client, target_profile.id, max_count=100)

        for tweet in tweets:
            db.save_tweet(conn, tweet)
            replies, _ = get_replies(client, tweet.id, max_count=200)
            for reply in replies:
                db.save_tweet(conn, reply, parent_tweet_id=tweet.id)

    conn.commit()
    client.rate_limit_summary()


if __name__ == "__main__":
    main()
