# syntax=docker/dockerfile:1

FROM ghcr.io/astral-sh/uv:bookworm-slim

# Build arguments
ARG UV_VERSION
ARG PYTHON_VERSION

ENV DEBIAN_FRONTEND=noninteractive

# Install system dependencies for pyodbc, polars, duckdb, and ODBC Driver 18 for SQL Server
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

# Install specific uv version
RUN curl -LsSf https://astral.sh/uv/install.sh | sh -s -- --version $UV_VERSION
ENV PATH="/home/vscode/.local/bin:$PATH"

# Verify uv version matches the pinned version
RUN uv --version && \
    echo "✅ uv is working correctly" && \
    if [ -n "$UV_VERSION" ]; then \
        echo "📋 Expected uv version: $UV_VERSION"; \
        uv_version_output=$(uv --version) && \
        if echo "$uv_version_output" | grep -q "$UV_VERSION"; then \
            echo "✅ uv version $UV_VERSION confirmed"; \
        else \
            echo "❌ Expected uv version $UV_VERSION, got: $uv_version_output"; \
            exit 1; \
        fi; \
    fi

CMD [ "bash" ]


