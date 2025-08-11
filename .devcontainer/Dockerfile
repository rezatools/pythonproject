# syntax=docker/dockerfile:1

FROM debian:bookworm-slim

ENV DEBIAN_FRONTEND=noninteractive
#ENV PATH="/workspaces/.venv/bin:/home/vscode/.cargo/bin:$PATH"


# Install system dependencies for uv, pyodbc, polars, duckdb, requests, and ODBC Driver 18 for SQL Server
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    unzip \
    gnupg \
    ca-certificates \
    build-essential \
    pkg-config \
    unixodbc \
    unixodbc-dev \
    libpq-dev \
    libssl-dev \
    libcurl4-openssl-dev \
    libxml2-dev \
    && rm -rf /var/lib/apt/lists/*


# Import Microsoft GPG key
RUN curl -fsSL https://packages.microsoft.com/keys/microsoft.asc \
    | gpg --dearmor \
    | tee /usr/share/keyrings/microsoft-prod.gpg > /dev/null

# Add Microsoft repo for correct architecture
RUN arch=$(dpkg --print-architecture) && \
    echo "deb [arch=${arch} signed-by=/usr/share/keyrings/microsoft-prod.gpg] https://packages.microsoft.com/debian/12/prod bookworm main" \
    | tee /etc/apt/sources.list.d/microsoft-prod.list

# Install Azure CLI; install msodbcsql18 only if available for the architecture
RUN set -eux; \
    apt-get update; \
    ACCEPT_EULA=Y apt-get install -y azure-cli || true; \
    if apt-cache show msodbcsql18 2>/dev/null | grep -q "^Version:"; then \
        ACCEPT_EULA=Y apt-get install -y msodbcsql18; \
    else \
        echo "msodbcsql18 not available for $(dpkg --print-architecture); skipping."; \
    fi; \
    rm -rf /var/lib/apt/lists/*

# Create vscode user and workspace
RUN useradd -ms /bin/bash vscode && \
    mkdir -p /workspaces && \
    chown -R vscode:vscode /workspaces

USER vscode
WORKDIR /workspaces

# Install uv as vscode user
RUN curl -LsSf https://astral.sh/uv/install.sh | sh
# Ensure uv is available on PATH for non-interactive shells
ENV PATH="/home/vscode/.local/bin:$PATH"

# Verify uv install
RUN uv --version

CMD [ "bash" ]


