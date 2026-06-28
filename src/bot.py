import importlib
import logging
import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
_wf = importlib.import_module("ml.1_words_frequency")
word_frequency = _wf.word_frequency

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
WAIT_WF_USERNAME = 1


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    targets = [
        "fm6oaorg", "Saudi_Moia", "diyanet_en",
        "h_bennajeh", "Ali_AlQaradaghi", "realDonaldTrump",
    ]
    targets_str = "\n".join(f"• @{t}" for t in targets)
    await update.message.reply_text(
        "*Twitter Datum Bot*\n\n"
        "Explorez les réseaux de réponses extraits de Twitter.\n\n"
        "*Cibles actuelles :*\n"
        f"{targets_str}\n\n"
        "/extract — exporter les données et aperçus pour un utilisateur\n"
        "/insight — aperçu de la base de données (utilisateurs, tweets, réponses)",
        parse_mode="Markdown",
    )


async def extract_start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    await update.message.reply_text("Entrez le nom d'utilisateur Twitter à extraire :")
    return WAIT_USERNAME


async def extract_run(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    username = update.message.text.strip().lstrip("@")
    conn = context.bot_data["conn"]
    cur = conn.cursor()

    cur.execute("SELECT id, fullname, followers, following FROM users WHERE username = ? COLLATE NOCASE", (username,))
    row = cur.fetchone()
    if not row:
        await update.message.reply_text(f"Utilisateur '{username}' introuvable dans la base de données.")
        return ConversationHandler.END
    user_id, fullname, followers, following = row

    await update.message.reply_text(f"Extraction de @{username} en cours…")

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
    own_dicts = [dict(zip(tweet_cols, r)) for r in own]
    reply_dicts = [dict(zip(tweet_cols, r)) for r in replies]

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

    for d in own_dicts:
        d["source"] = username
        d["target"] = ""
    for d in reply_dicts:
        d["source"] = reply_user_map.get(d["user_id"], "")
        d["target"] = username

    tweet_cols = tweet_cols + ["source", "target"]
    tweets = own_dicts + reply_dicts

    edges = [
        {"source": reply_user_map[r[1]], "target": username, "tweet_id": r[8], "reply_id": r[0], "type": "reply"}
        for r in replies if r[1] in reply_user_map
    ]

    out_dir = f"out/{username}"
    os.makedirs(out_dir, exist_ok=True)
    write_csv(f"{out_dir}/tweets.csv", tweet_cols, tweets)
    write_csv(f"{out_dir}/users.csv", ["id", "label", "followers", "following"], nodes.values())
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
        f"*Aperçu du cluster pour @{username}*\n\n"
        f"Tweets extraits : {len(own)}\n"
        f"Répondeurs uniques : {len(nodes) - 1}\n"
        f"Total des réponses : {len(replies)}\n\n"
        f"Top répondeurs :\n{top5_str}\n\n"
        f"Tweet le plus commenté :\n{most_replied_str}"
    )

    for fname in ["tweets.csv", "users.csv", "graph.gexf"]:
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
        f"*Statistiques de la base de données*\n\nUtilisateurs : {users}\nTweets : {tweets}\nRéponses : {replies}",
        parse_mode="Markdown",
    )


async def wf_start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    await update.message.reply_text("Entrez le nom d'utilisateur Twitter :")
    return WAIT_WF_USERNAME


async def wf_run(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    username = update.message.text.strip().lstrip("@")
    conn = context.bot_data["conn"]
    results = word_frequency(conn, username, top_n=20)
    if not results:
        await update.message.reply_text(f"Aucun tweet trouvé pour @{username}.")
        return ConversationHandler.END
    lines = "\n".join(f"{r:>3}. {w:<25} {c}" for r, (w, c) in enumerate(results, 1))
    await update.message.reply_text(
        f"*@{username} — mots les plus fréquents*\n\n```\n{lines}\n```",
        parse_mode="Markdown",
    )
    return ConversationHandler.END


async def post_init(app: Application) -> None:
    await app.bot.set_my_commands([
        BotCommand("start", "À propos de ce bot"),
        BotCommand("extract", "Extraire les données d'un utilisateur Twitter"),
        BotCommand("insight", "Afficher les statistiques de la base de données"),
        BotCommand("1_word_frequency", "Mots les plus fréquents pour un utilisateur"),
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
    wf_conv = ConversationHandler(
        entry_points=[CommandHandler("1_word_frequency", wf_start)],
        states={WAIT_WF_USERNAME: [MessageHandler(filters.TEXT & ~filters.COMMAND, wf_run)]},
        fallbacks=[],
    )
    app.add_handler(CommandHandler("start", start))
    app.add_handler(conv)
    app.add_handler(wf_conv)
    app.add_handler(CommandHandler("insight", insight))
    app.run_polling()


if __name__ == "__main__":
    main()
