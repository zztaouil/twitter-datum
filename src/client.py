import json
import random
import time
from dataclasses import dataclass, field
from pathlib import Path

import httpx

BEARER = "AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA"
BASE = "https://x.com/i/api/graphql"

GQL_FEATURES = json.dumps({
    "rweb_video_screen_enabled": False,
    "rweb_cashtags_enabled": True,
    "profile_label_improvements_pcf_label_in_post_enabled": True,
    "responsive_web_profile_redirect_enabled": False,
    "rweb_tipjar_consumption_enabled": False,
    "verified_phone_label_enabled": False,
    "creator_subscriptions_tweet_preview_api_enabled": True,
    "responsive_web_graphql_timeline_navigation_enabled": True,
    "responsive_web_graphql_skip_user_profile_image_extensions_enabled": False,
    "premium_content_api_read_enabled": False,
    "communities_web_enable_tweet_community_results_fetch": True,
    "c9s_tweet_anatomy_moderator_badge_enabled": True,
    "responsive_web_grok_analyze_button_fetch_trends_enabled": False,
    "responsive_web_grok_analyze_post_followups_enabled": True,
    "articles_preview_enabled": True,
    "responsive_web_edit_tweet_api_enabled": True,
    "graphql_is_translatable_rweb_tweet_is_translatable_enabled": True,
    "view_counts_everywhere_api_enabled": True,
    "longform_notetweets_consumption_enabled": True,
    "responsive_web_twitter_article_tweet_consumption_enabled": True,
    "tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled": True,
    "longform_notetweets_rich_text_read_enabled": True,
    "longform_notetweets_inline_media_enabled": False,
    "responsive_web_enhance_cards_enabled": False,
}, separators=(",", ":"))

_COMMON_HEADERS = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "accept": "*/*",
    "accept-language": "en-US,en;q=0.9",
    "content-type": "application/json",
    "origin": "https://x.com",
    "referer": "https://x.com/",
    "x-twitter-active-user": "yes",
    "x-twitter-client-language": "en",
}


class RateLimitError(Exception):
    pass


@dataclass
class Session:
    username: str
    id: str
    auth_token: str
    ct0: str
    # ponytail: per-endpoint (remaining, reset_timestamp)
    _limits: dict[str, tuple[int, int]] = field(default_factory=dict, repr=False)

    def is_limited(self, endpoint: str) -> bool:
        if endpoint not in self._limits:
            return False
        remaining, reset = self._limits[endpoint]
        return remaining <= 10 and reset > int(time.time())

    def update_limit(self, endpoint: str, remaining: int, reset: int) -> None:
        cur = self._limits.get(endpoint)
        # match nitter's race-condition guard: don't go backwards
        if cur and cur[1] == reset and cur[0] <= remaining:
            self._limits[endpoint] = (remaining, reset)
            return
        if cur and cur[1] > reset and cur[0] < remaining:
            return
        self._limits[endpoint] = (remaining, reset)

    def headers(self) -> dict[str, str]:
        return {
            **_COMMON_HEADERS,
            "authorization": f"Bearer {BEARER}",
            "x-twitter-auth-type": "OAuth2Session",
            "x-csrf-token": self.ct0,
            "cookie": f"auth_token={self.auth_token}; ct0={self.ct0}",
        }


class TwitterClient:
    def __init__(self, auth_token: str, ct0: str, username: str = "", id: str = ""):
        self._pool = [Session(username=username, id=id, auth_token=auth_token, ct0=ct0)]
        self._http = httpx.Client(follow_redirects=True)

    @classmethod
    def from_file(cls, path: str = "sessions.jsonl") -> "TwitterClient":
        sessions: list[Session] = []
        for line in Path(path).read_text().splitlines():
            line = line.strip()
            if not line:
                continue
            data = json.loads(line)
            if data.get("kind") != "cookie":
                continue
            sessions.append(Session(
                username=data.get("username", ""),
                id=data.get("id") or "",
                auth_token=data["auth_token"],
                ct0=data["ct0"],
            ))
        if not sessions:
            raise ValueError(f"No cookie sessions in {path}")
        client = cls.__new__(cls)
        client._pool = sessions
        client._http = httpx.Client(follow_redirects=True)
        return client

    def _pick_session(self, endpoint: str) -> Session:
        available = [s for s in self._pool if not s.is_limited(endpoint)]
        if not available:
            raise RateLimitError(f"All {len(self._pool)} session(s) rate-limited for {endpoint}")
        return random.choice(available)

    def _fetch(self, endpoint: str, variables: dict, field_toggles: str = "") -> dict:
        session = self._pick_session(endpoint)
        params: dict[str, str] = {
            "variables": json.dumps(variables, separators=(",", ":")),
            "features": GQL_FEATURES,
        }
        if field_toggles:
            params["fieldToggles"] = field_toggles

        resp = self._http.get(f"{BASE}/{endpoint}", params=params, headers=session.headers())
        resp.raise_for_status()

        try:
            remaining = int(resp.headers["x-rate-limit-remaining"])
            reset = int(resp.headers["x-rate-limit-reset"])
            session.update_limit(endpoint, remaining, reset)
        except (KeyError, ValueError):
            pass

        return resp.json()
