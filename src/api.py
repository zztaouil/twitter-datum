import json
from datetime import datetime, timezone

from .client import TwitterClient
from .types import Tweet, User

_ENDPOINT_USER = "IGgvgiOx4QZndDHuD3x9TQ/UserByScreenName"
_ENDPOINT_TWEETS = "LE3eTyeqhBh2g-fX85O2eQ/UserWithProfileTweetsQueryV2"
_ENDPOINT_TWEET = "OZMbEnEa96AN8Pq6HyTWdw/ConversationTimeline"
_ENDPOINT_SEARCH = "-TFXKoMnMTKdEXcCn-eahw/SearchTimeline"

_TOGGLES_USER = '{"withArticleRichContentState":true,"withArticlePlainText":false,"withGrokAnalyze":false,"withDisallowedReplyControls":false}'
_TOGGLES_TWEETS = '{"withArticleRichContentState":true,"withArticlePlainText":false}'


def _parse_twitter_date(s: str) -> datetime:
    # Twitter format: "Mon Jan 01 00:00:00 +0000 2024"
    try:
        return datetime.strptime(s, "%a %b %d %H:%M:%S %z %Y")
    except (ValueError, TypeError):
        return datetime.fromtimestamp(0, tz=timezone.utc)


def _parse_user_legacy(legacy: dict, rest_id: str = "") -> User:
    return User(
        id=rest_id or legacy.get("id_str", ""),
        username=legacy.get("screen_name", ""),
        fullname=legacy.get("name", ""),
        bio=legacy.get("description", ""),
        location=legacy.get("location", ""),
        followers=legacy.get("followers_count", 0),
        following=legacy.get("friends_count", 0),
        tweets_count=legacy.get("statuses_count", 0),
        protected=legacy.get("protected", False),
    )


def _parse_tweet_result(node: dict, fallback_user: User | None = None) -> Tweet | None:
    if not node or "legacy" not in node:
        return None
    legacy = node["legacy"]
    user_node = (node.get("core") or {}).get("user_results") or {}
    user_result = user_node.get("result") or {}
    user_legacy = user_result.get("legacy") or {}
    user = _parse_user_legacy(user_legacy, user_result.get("rest_id", "")) if user_legacy else fallback_user
    if not user:
        return None

    # note tweet has full text in note_tweet path
    text = legacy.get("full_text", "")
    note = node.get("note_tweet", {}).get("note_tweet_results", {}).get("result", {})
    if note:
        text = note.get("text", text)

    return Tweet(
        id=node.get("rest_id", legacy.get("id_str", "")),
        user=user,
        text=text,
        created_at=_parse_twitter_date(legacy.get("created_at", "")),
        reply_count=legacy.get("reply_count", 0),
        retweet_count=legacy.get("retweet_count", 0),
        like_count=legacy.get("favorite_count", 0),
        view_count=int((node.get("views") or {}).get("count") or 0),
    )


def _extract_tweet_node(entry: dict) -> dict | None:
    # try direct tweet result first, then items list
    result = (
        entry.get("content", {})
        .get("itemContent", {})
        .get("tweet_results", {})
        .get("result")
    )
    if result:
        return result
    for item in entry.get("content", {}).get("items", []):
        r = item.get("item", {}).get("itemContent", {}).get("tweet_results", {}).get("result")
        if r:
            return r
    return None


def _walk_instructions(instructions: list) -> tuple[list[Tweet], str]:
    tweets: list[Tweet] = []
    cursor = ""
    for inst in instructions:
        for entry in inst.get("entries", []):
            entry_id = entry.get("entryId", "")
            if entry_id.startswith("tweet") or entry_id.startswith("profile-grid"):
                node = _extract_tweet_node(entry)
                t = _parse_tweet_result(node) if node else None
                if t:
                    tweets.append(t)
            elif entry_id.startswith("cursor-bottom"):
                cursor = (
                    entry.get("content", {}).get("value")
                    or entry.get("content", {}).get("itemContent", {}).get("value", "")
                )
    return tweets, cursor


def get_profile(client: TwitterClient, username: str) -> User:
    data = client._fetch(
        _ENDPOINT_USER,
        {"screen_name": username, "withGrokTranslatedBio": False},
        field_toggles=_TOGGLES_USER,
    )
    result = (
        data.get("data", {})
        .get("user", {})
        .get("result", {})
    )
    legacy = result.get("legacy", {})
    return _parse_user_legacy(legacy, result.get("rest_id", ""))


def get_tweets(
    client: TwitterClient, user_id: str, cursor: str | None = None, count: int = 20
) -> tuple[list[Tweet], str]:
    variables: dict = {"rest_id": user_id, "count": count}
    if cursor:
        variables["cursor"] = cursor
    data = client._fetch(_ENDPOINT_TWEETS, variables, field_toggles=_TOGGLES_TWEETS)
    instructions = (
        data.get("data", {})
        .get("user", {})
        .get("result", {})
        .get("timeline", {})
        .get("timeline", {})
        .get("instructions", [])
    )
    return _walk_instructions(instructions)


def get_tweet(client: TwitterClient, tweet_id: str) -> Tweet | None:
    variables = {
        "postId": tweet_id,
        "cursor": "",
        "includeHasBirdwatchNotes": False,
        "includePromotedContent": False,
        "withBirdwatchNotes": True,
        "withVoice": False,
        "withV2Timeline": True,
    }
    data = client._fetch(_ENDPOINT_TWEET, variables)
    instructions = (
        data.get("data", {})
        .get("timelineResponse", data.get("data", {}).get("timeline_response", {}))
        .get("instructions", [])
    )
    for inst in instructions:
        for entry in inst.get("entries", []):
            if entry.get("entryId", "").endswith(tweet_id):
                node = _extract_tweet_node(entry)
                if node:
                    return _parse_tweet_result(node)
    return None


def search_tweets(
    client: TwitterClient, query: str, cursor: str | None = None
) -> tuple[list[Tweet], str]:
    variables: dict = {
        "rawQuery": query,
        "count": 20,
        "querySource": "typed_query",
        "product": "Latest",
        "withGrokTranslatedBio": True,
        "withQuickPromoteEligibilityTweetFields": False,
    }
    if cursor:
        variables["cursor"] = cursor
    data = client._fetch(_ENDPOINT_SEARCH, variables)
    instructions = (
        data.get("data", {})
        .get("search_by_raw_query", {})
        .get("search_timeline", {})
        .get("timeline", {})
        .get("instructions", [])
    )
    return _walk_instructions(instructions)
