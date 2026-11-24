from importlib import import_module

_EXPORTS = {
    "TwitterClient": ".core.client",
    "User": ".core.models",
    "Tweet": ".core.models",
    "get_profile": ".core.api",
    "get_tweets": ".core.api",
    "get_tweets_and_replies": ".core.api",
    "get_tweet": ".core.api",
    "get_replies": ".core.api",
    "search_tweets": ".core.api",
}
__all__ = list(_EXPORTS)


def __getattr__(name):
    # The web API imports src.config without needing the extraction client.
    if name not in _EXPORTS:
        raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
    value = getattr(import_module(_EXPORTS[name], __name__), name)
    globals()[name] = value
    return value
