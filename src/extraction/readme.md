# Extraction

## Gamma

Search sweep results are capped at ~40 tweets per chunk regardless of the
chunk's date range (`CHUNK_DAYS` in `gamma.py`). A 30-day chunk maxes out at
~40 tweets even if the account tweeted far more that month, so busy accounts
lose tweets silently.

Fix: shrink `CHUNK_DAYS` so each chunk is less likely to hit the ~40 cap.
E.g. 30 -> 14 roughly doubles yield for accounts dense enough to hit the cap
(two ~40-tweet chunks per month instead of one). Smaller chunks also mean
more requests/rate-limit windows for the same history, so there's a
tradeoff between coverage and sweep time.
