import os
from pathlib import Path

from .settings import *  # noqa: F403

DEBUG = False
SECRET_KEY = os.environ["DJANGO_SECRET_KEY"]
ALLOWED_HOSTS = ["127.0.0.1"]
if api_host := os.environ.get("DATUM_API_HOST"):
    ALLOWED_HOSTS.append(api_host)
DATUM_WEB_ORIGIN = os.environ["ORIGIN"]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": Path(os.environ["DATUM_TWEETS_DB"]).resolve(strict=True),
    },
    "pins": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": Path(os.environ["DATUM_PINS_DB"]),
    },
}
