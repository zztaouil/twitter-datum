import logging
import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from dotenv import load_dotenv
load_dotenv()

import src.db as db
from src.utils import write_csv, write_gexf

from telegram import BotCommand, Update
from telegram.ext import (
    Application, CommandHandler, MessageHandler,
    ConversationHandler, filters, ContextTypes,
)

logging.basicConfig(format="%(asctime)s %(levelname)s %(message)s", level=logging.INFO)

WAIT_USERNAME = 0


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        "*Twitter Datum Bot*\n\n"
        "Explore reply networks scraped from Twitter.\n\n"
        "/extract — export data & cluster insights for a username\n"
        "/insight — database overview (users, tweets, replies)",
        parse_mode="Markdown",
    )


async def extract_start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    await update.message.reply_text("Enter the Twitter username to extract:")
    return WAIT_USERNAME


async def extract_run(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    username = update.message.text.strip().lstrip("@")
    conn = context.bot_data["conn"]
    cur = conn.cursor()

    cur.execute("SELECT id, fullname, followers, following FROM users WHERE username = ? COLLATE NOCASE", (username,))
    row = cur.fetchone()
    if not row:
        await update.message.reply_text(f"User '{username}' not found in database.")
        return ConversationHandler.END
    user_id, fullname, followers, following = row

    await update.message.reply_text(f"Extracting @{username}…")

    cur.execute(
        "SELECT id, user_id, text, created_at, reply_count, retweet_count, like_count, view_count, parent_tweet_id "
        "FROM tweets WHERE user_id = ?",
        (user_id,)
    )
    own = cur.fetchall()
    own_ids = {r[0] for r in own}

    replies = []
    if own_ids:
        cur.execute(
            f"SELECT id, user_id, text, created_at, reply_count, retweet_count, like_count, view_count, parent_tweet_id "
            f"FROM tweets WHERE parent_tweet_id IN ({','.join('?' * len(own_ids))}) AND user_id != ?",
            (*own_ids, user_id)
        )
        replies = cur.fetchall()

    tweet_cols = ["id", "user_id", "text", "created_at", "reply_count", "retweet_count", "like_count", "view_count", "parent_tweet_id"]
    tweets = [dict(zip(tweet_cols, r)) for r in own] + [dict(zip(tweet_cols, r)) for r in replies]

    replier_ids = {r[1] for r in replies}
    nodes: dict[str, dict] = {username: {"id": username, "label": fullname, "followers": followers, "following": following}}
    if replier_ids:
        cur.execute(
            f"SELECT username, fullname, followers, following FROM users WHERE id IN ({','.join('?' * len(replier_ids))})",
            tuple(replier_ids)
        )
        for u, fn, fo, fi in cur.fetchall():
            nodes[u] = {"id": u, "label": fn, "followers": fo, "following": fi}

    reply_user_map = {}
    if replier_ids:
        cur.execute(
            f"SELECT id, username FROM users WHERE id IN ({','.join('?' * len(replier_ids))})",
            tuple(replier_ids)
        )
        reply_user_map = {uid: uname for uid, uname in cur.fetchall()}

    edges = [
        {"source": reply_user_map[r[1]], "target": username, "tweet_id": r[8], "reply_id": r[0], "type": "reply"}
        for r in replies if r[1] in reply_user_map
    ]

    out_dir = f"out/{username}"
    os.makedirs(out_dir, exist_ok=True)
    write_csv(f"{out_dir}/tweets.csv", tweet_cols, tweets)
    write_csv(f"{out_dir}/nodes.csv", ["id", "label", "followers", "following"], nodes.values())
    write_gexf(f"{out_dir}/graph.gexf", nodes, edges)

    # top 5 repliers by reply count
    from collections import Counter
    reply_counts = Counter(reply_user_map.get(r[1]) for r in replies if r[1] in reply_user_map)
    top5 = reply_counts.most_common(5)
    top5_str = "\n".join(f"  {i+1}. @{u} ({c} replies)" for i, (u, c) in enumerate(top5)) or "  —"

    # most replied-to tweet
    most_replied = max(own, key=lambda r: r[4]) if own else None
    most_replied_str = (
        f"  {most_replied[4]} replies — \"{most_replied[2][:80]}\"" if most_replied else "  —"
    )

    insights = (
        f"*Cluster insights for @{username}*\n\n"
        f"Tweets scraped: {len(own)}\n"
        f"Unique repliers: {len(nodes) - 1}\n"
        f"Total replies: {len(replies)}\n\n"
        f"Top repliers:\n{top5_str}\n\n"
        f"Most replied tweet:\n{most_replied_str}"
    )

    for fname in ["tweets.csv", "nodes.csv", "graph.gexf"]:
        with open(f"{out_dir}/{fname}", "rb") as f:
            await context.bot.send_document(update.effective_chat.id, f, filename=fname)

    await update.message.reply_text(insights, parse_mode="Markdown")
    return ConversationHandler.END


async def insight(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    conn = context.bot_data["conn"]
    cur = conn.cursor()
    cur.execute(
        "SELECT (SELECT COUNT(*) FROM users), "
        "(SELECT COUNT(*) FROM tweets), "
        "(SELECT COUNT(*) FROM tweets WHERE parent_tweet_id IS NOT NULL)"
    )
    users, tweets, replies = cur.fetchone()
    await update.message.reply_text(
        f"*Database stats*\n\nUsers: {users}\nTweets: {tweets}\nReplies: {replies}",
        parse_mode="Markdown",
    )


async def post_init(app: Application) -> None:
    await app.bot.set_my_commands([
        BotCommand("start", "About this bot"),
        BotCommand("extract", "Extract data for a Twitter user"),
        BotCommand("insight", "Show database stats"),
    ])


def main() -> None:
    token = os.environ["TELEGRAM_API_KEY"]
    db_path = os.environ.get("DB_PATH", "data.db")
    conn = db.init_db(db_path)

    app = Application.builder().token(token).post_init(post_init).build()
    app.bot_data["conn"] = conn

    conv = ConversationHandler(
        entry_points=[CommandHandler("extract", extract_start)],
        states={WAIT_USERNAME: [MessageHandler(filters.TEXT & ~filters.COMMAND, extract_run)]},
        fallbacks=[],
    )
    app.add_handler(CommandHandler("start", start))
    app.add_handler(conv)
    app.add_handler(CommandHandler("insight", insight))
    app.run_polling()


if __name__ == "__main__":
    main()
