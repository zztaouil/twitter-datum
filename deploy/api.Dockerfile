FROM ghcr.io/astral-sh/uv:0.13.8 AS uv

FROM python:3.14.10-slim-trixie AS builder
COPY --from=uv /uv /usr/local/bin/uv
WORKDIR /app
COPY pyproject.toml uv.lock README.md ./
RUN uv export --locked --no-dev --no-emit-project --no-hashes > /tmp/constraints.txt \
    && uv venv /opt/venv \
    && uv pip install --python /opt/venv/bin/python --constraint /tmp/constraints.txt django gunicorn

FROM python:3.14.10-slim-trixie
ENV PATH="/opt/venv/bin:$PATH" PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1
COPY --from=builder /opt/venv /opt/venv
COPY server /app/server
COPY src/__init__.py src/config.py /app/src/
RUN chmod -R a+rX /app
WORKDIR /app/server
CMD ["gunicorn", "--bind", "127.0.0.1:8000", "--workers", "2", "--no-control-socket", "--access-logfile", "-", "core.wsgi:application"]
