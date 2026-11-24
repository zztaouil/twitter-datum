# Deploy Twitter Datum with Docker Compose

Target `mike@100.95.179.78` runs Debian 13 on x86-64. Compose runs Gunicorn and SvelteKit on the Linux host network. Both origins bind to `127.0.0.1`. Cloudflare terminates browser TLS at its edge and sends requests through the tunnel to cloudflared, which proxies over loopback HTTP.

## Stage the release

Install Docker Engine, Buildx, and the Compose plugin on the host. On Debian 13, the Compose package is `docker-compose`. Verify with `docker compose version`.

Extract the source bundle into `~/twitter-datum/compose-tunnel`. The sibling `~/twitter-datum/state` directory holds the tweet snapshot, pins, and auth SQLite DBs. Compose runs both processes as UID/GID `1000:1000` on this host. On a host with different IDs, export `DATUM_UID` and `DATUM_GID` before running Compose.

Reuse `~/.config/twitter-datum/api.env` and `web.env` from the staged release. For a fresh host, create them once as the deployment user.

```bash
umask 077
config="$HOME/.config/twitter-datum"
install -d -m 700 "$config" "$HOME/twitter-datum/state"

if [[ ! -e "$config/api.env" ]]; then
  cat > "$config/api.env" <<ENV
DJANGO_SECRET_KEY=$(openssl rand -hex 48)
ORIGIN=https://twitter-datum.17082711.xyz
ENV
fi

if [[ ! -e "$config/web.env" ]]; then
  cat > "$config/web.env" <<ENV
BETTER_AUTH_SECRET=$(openssl rand -hex 32)
ORIGIN=https://twitter-datum.17082711.xyz
ENV
fi

cd "$HOME/twitter-datum/compose-tunnel"
docker compose build
```

For an existing deployment, update `ORIGIN` in both env files to `https://twitter-datum.17082711.xyz` and keep the existing secrets. Compose bakes `PUBLIC_API_URL` into the browser bundle. SvelteKit uses `INTERNAL_API_URL` for server-side requests.

## Stage the tweet snapshot

On the source machine, take a consistent SQLite backup from the workspace root. SQLite includes committed WAL changes in the backup. This command initializes a fresh dataset path on the host.

```sh
snapshot_dir=$(mktemp -d)
sqlite3 -readonly data.db ".backup $snapshot_dir/tweets.sqlite3"
ssh mike@100.95.179.78 'install -d -m 700 "$HOME/twitter-datum/state"'
scp "$snapshot_dir/tweets.sqlite3" mike@100.95.179.78:twitter-datum/state/tweets.sqlite3.incoming
ssh mike@100.95.179.78 'ln "$HOME/twitter-datum/state/tweets.sqlite3.incoming" "$HOME/twitter-datum/state/tweets.sqlite3" && rm "$HOME/twitter-datum/state/tweets.sqlite3.incoming"'
```

On the host, build the full-text index before serving traffic. Use `db:push` for initial schema setup and review any changes before approving the prompt. A fresh auth DB should contain `account`, `session`, `task`, `user`, and `verification`.

```bash
cd "$HOME/twitter-datum/compose-tunnel"
docker compose run --rm --no-deps api python manage.py check
docker compose run --rm --no-deps api python manage.py build_search_index
docker compose run --rm --no-deps web npm run db:push
```

## Start and verify

```bash
docker compose up -d --wait
curl -fsS -o /dev/null http://127.0.0.1:8000/api/facets
curl -fsS -o /dev/null http://127.0.0.1:3000/
```

Configure a remotely managed Cloudflare Tunnel named `twitter-datum` with these ingress rules, in order.

| Hostname | Origin |
| --- | --- |
| `twitter-datum.17082711.xyz` | `http://127.0.0.1:3000` |
| `api-twitter-datum.17082711.xyz` | `http://127.0.0.1:8000` |
| Catch-all | `http_status:404` |

Save `TUNNEL_TOKEN=<connector token>` in `~/.config/twitter-datum/tunnel.env` with permissions `0600`. Start cloudflared, verify it connects, then point both hostnames at `<tunnel-id>.cfargotunnel.com` using proxied CNAME records.

```bash
docker compose --profile tunnel up -d --wait
docker compose --profile tunnel logs --tail=30 cloudflared
curl -fsS -o /dev/null https://twitter-datum.17082711.xyz/
curl -fsS -o /dev/null https://api-twitter-datum.17082711.xyz/api/facets
```

Check search, analytics, pin/unpin, and the pinned page. Use `docker compose --profile tunnel logs -f` for logs and `docker compose --profile tunnel down` to stop the stack. SQLite state persists in `~/twitter-datum/state`.
