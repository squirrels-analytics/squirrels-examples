FROM python:3.12-slim-trixie AS builder
COPY --from=ghcr.io/astral-sh/uv:0.8.15 /uv /uvx /bin/

WORKDIR /app

# Install only what's needed for resolving dependencies (builder only)
RUN apt-get update \
    && apt-get install -y --no-install-recommends git

COPY pyproject.toml uv.lock ./

RUN uv sync --locked

COPY . .

# Then, use a final image without uv
FROM python:3.12-slim-trixie AS runtime

WORKDIR /app

# Copy the application from the builder
COPY --from=builder /app /app

# Place executables in the environment at the front of the path
ENV PATH="/app/.venv/bin:$PATH"

EXPOSE 4465

CMD ["sqrl", "run", "--host", "0.0.0.0", "--port", "4465"]
