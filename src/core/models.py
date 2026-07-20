from dataclasses import dataclass
from datetime import datetime


@dataclass
class User:
    id: str
    username: str
    fullname: str
    bio: str
    location: str
    followers: int
    following: int
    tweets_count: int
    protected: bool


@dataclass
class Tweet:
    id: str
    user: User
    text: str
    created_at: datetime
    reply_count: int
    retweet_count: int
    like_count: int
    view_count: int
    media_type: str = "text"
