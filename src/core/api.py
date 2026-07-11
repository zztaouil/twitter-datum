import json
from datetime import datetime, timezone

from .client import TwitterClient
from .models import Tweet, User

_ENDPOINT_USER = "IGgvgiOx4QZndDHuD3x9TQ/UserByScreenName"
_ENDPOINT_TWEETS = "LE3eTyeqhBh2g-fX85O2eQ/UserWithProfileTweetsQueryV2"
_ENDPOINT_TWEETS_AND_REPLIES = "AcYHjc_YAx-9_rKWdMsKvA/UserWithProfileTweetsAndRepliesQueryV2"
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


def _parse_user_result(result: dict) -> User:
    legacy = result.get("legacy") or {}
    core = result.get("core") or {}
    privacy = result.get("privacy") or {}
    profile_bio = result.get("profile_bio") or {}
    relationship_counts = result.get("relationship_counts") or {}
    location_obj = result.get("location") or {}
    return User(
        id=result.get("rest_id") or legacy.get("id_str", ""),
        username=core.get("screen_name") or legacy.get("screen_name", ""),
        fullname=core.get("name") or legacy.get("name", ""),
        bio=profile_bio.get("description") or legacy.get("description", ""),
        location=location_obj.get("location") or legacy.get("location", ""),
        followers=int(relationship_counts.get("followers") or legacy.get("followers_count", 0)),
        following=int(relationship_counts.get("following") or legacy.get("friends_count", 0)),
        tweets_count=int(relationship_counts.get("statuses_count") or legacy.get("statuses_count", 0)),
        protected=privacy.get("protected", legacy.get("protected", False)),
    )


def _parse_tweet_result(node: dict, fallback_user: User | None = None) -> Tweet | None:
    if not node:
        return None
    legacy = node.get("legacy") or {}
    details = node.get("details") or {}
    counts = node.get("counts") or {}
    user_node = (node.get("core") or {}).get("user_results") or {}
    user_result = user_node.get("result") or {}
    user = _parse_user_result(user_result) if user_result else fallback_user
    if not user:
        return None

    text = details.get("full_text") or legacy.get("full_text", "")
    note = node.get("note_tweet", {}).get("note_tweet_results", {}).get("result", {})
    if note:
        text = note.get("text", text)

    created_at_ms = details.get("created_at_ms")
    if created_at_ms:
        created_at = datetime.fromtimestamp(created_at_ms / 1000, tz=timezone.utc)
    else:
        created_at = _parse_twitter_date(legacy.get("created_at", ""))

    return Tweet(
        id=node.get("rest_id") or legacy.get("id_str", ""),
        user=user,
        text=text,
        created_at=created_at,
        reply_count=counts.get("reply_count") or legacy.get("reply_count", 0),
        retweet_count=counts.get("retweet_count") or legacy.get("retweet_count", 0),
        like_count=counts.get("favorite_count") or legacy.get("favorite_count", 0),
        view_count=int((node.get("views") or {}).get("count") or 0),
    )


def _extract_tweet_node(entry: dict) -> dict | None:
    result = (
        entry.get("content", {})
        .get("content", {})
        .get("tweet_results", {})
        .get("result")
    )
    if result:
        return result
    for item in entry.get("content", {}).get("items", []):
        r = item.get("item", {}).get("content", {}).get("tweet_results", {}).get("result")
        if r:
            return r
    return None


def _walk_instructions(
    instructions: list,
    max_count: int = 0,
    entry_prefixes: tuple = ("tweet", "profile-conversation"),
) -> tuple[list[Tweet], str]:
    tweets: list[Tweet] = []
    cursor = ""
    for inst in instructions:
        for entry in inst.get("entries", []):
            entry_id = entry.get("entry_id", "")
            if any(entry_id.startswith(p) for p in entry_prefixes):
                node = _extract_tweet_node(entry)
                t = _parse_tweet_result(node) if node else None
                if t:
                    tweets.append(t)
                    if max_count and len(tweets) >= max_count:
                        return tweets, cursor
            elif entry_id.startswith("cursor-bottom"):
                cursor = entry.get("content", {}).get("value", "")
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
    return _parse_user_result(result)


def get_tweets(
    client: TwitterClient,
    user_id: str,
    cursor: str | None = None,
    count: int = 20,
    max_count: int = 20,
) -> tuple[list[Tweet], str]:
    variables: dict = {"rest_id": user_id, "count": count}
    if cursor:
        variables["cursor"] = cursor
    data = client._fetch(_ENDPOINT_TWEETS, variables, field_toggles=_TOGGLES_TWEETS)
    instructions = (
        data.get("data", {})
        .get("user_result", {})
        .get("result", {})
        .get("timeline_response", {})
        .get("timeline", {})
        .get("instructions", [])
    )
    return _walk_instructions(instructions, max_count=max_count)


def get_tweets_and_replies(
    client: TwitterClient,
    user_id: str,
    cursor: str | None = None,
    count: int = 20,
    max_count: int = 20,
) -> tuple[list[Tweet], str]:
    variables: dict = {"rest_id": user_id, "count": count}
    if cursor:
        variables["cursor"] = cursor
    data = client._fetch(_ENDPOINT_TWEETS_AND_REPLIES, variables, field_toggles=_TOGGLES_TWEETS)
    instructions = (
        data.get("data", {})
        .get("user_result", {})
        .get("result", {})
        .get("timeline_response", {})
        .get("timeline", {})
        .get("instructions", [])
    )
    return _walk_instructions(instructions, max_count=max_count)


def get_replies(
    client: TwitterClient,
    tweet_id: str,
    cursor: str | None = None,
    max_count: int = 0,
) -> tuple[list[Tweet], str]:
    variables = {
        "postId": tweet_id,
        "cursor": cursor or "",
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
    return _walk_instructions(
        instructions, max_count=max_count, entry_prefixes=("conversationthread",)
    )


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
            if entry.get("entry_id", "").endswith(tweet_id):
                node = _extract_tweet_node(entry)
                if node:
                    return _parse_tweet_result(node)
    return None


def search_tweets(
    client: TwitterClient, query: str, cursor: str | None = None, max_count: int = 0
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
    return _walk_instructions(instructions, max_count=max_count)
