#!/usr/bin/env python3
"""Refresh tweets_count for TARGETS by re-fetching their profiles."""
import sys, os
sys.path.insert(0, os.getcwd())

from src.config import TARGETS
from src import TwitterClient, get_profile
import src.core.db as db

def main():
    client = TwitterClient.from_file("sessions.jsonl")
    conn = db.init_db()
    for target in TARGETS:
        profile = get_profile(client, target)
        db.save_user(conn, profile)
        print(f"{target}: tweets_count={profile.tweets_count}")
    conn.commit()

if __name__ == "__main__":
    main()
