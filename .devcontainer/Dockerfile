# syntax=docker/dockerfile:1

FROM debian:bookworm-slim

ENV DEBIAN_FRONTEND=noninteractive

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

# Install ODBC Driver 18, Azure CLI, and sudo
RUN apt-get update && ACCEPT_EULA=Y apt-get install -y \
    msodbcsql18 \
    azure-cli \
    sudo \
    && rm -rf /var/lib/apt/lists/*

# Create vscode user and workspace
RUN useradd -ms /bin/bash vscode && \
    mkdir -p /workspaces && \
    chown -R vscode:vscode /workspaces && \
    echo "vscode ALL=(ALL) NOPASSWD:ALL" > /etc/sudoers.d/90-vscode && chmod 0440 /etc/sudoers.d/90-vscode

USER vscode
WORKDIR /workspaces

# Install uv as vscode user
RUN curl -LsSf https://astral.sh/uv/install.sh | sh

# Avoid pre-creating project venv in image; it will be created in postCreateCommand into a named volume
ENV PATH="/home/vscode/.local/bin:$PATH"
RUN echo "if [ -f /workspaces/pythonproject/.venv/bin/activate ]; then source /workspaces/pythonproject/.venv/bin/activate; fi" >> /home/vscode/.bashrc
RUN uv --version

CMD [ "bash" ]
