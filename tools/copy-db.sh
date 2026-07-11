#!/bin/bash

ssh mike@178.104.119.56 "sqlite3 /home/mike/twitter-datum/data.db 'PRAGMA wal_checkpoint(TRUNCATE);'"
scp mike@178.104.119.56:/home/mike/twitter-datum/data.db ./data.db