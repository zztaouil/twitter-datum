FROM node:24.22.3-bookworm-slim
WORKDIR /app
COPY frontend/package.json frontend/package-lock.json frontend/.npmrc ./
RUN npm ci --no-audit --include=dev
COPY frontend ./
ARG PUBLIC_API_URL=http://127.0.0.1:8000
RUN find /app -path /app/node_modules -prune -o -exec chmod a+rX {} + \
    && PUBLIC_API_URL="${PUBLIC_API_URL}" \
    ORIGIN=http://127.0.0.1:3000 \
    DATABASE_URL=/tmp/build.sqlite3 \
    BETTER_AUTH_SECRET="$(node -p 'require("node:crypto").randomBytes(32).toString("hex")')" \
    npm run build \
    && rm -f /tmp/build.sqlite3
CMD ["node", "build"]
