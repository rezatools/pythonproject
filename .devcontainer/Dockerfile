# syntax=docker/dockerfile:1

FROM debian:bookworm-slim

# Avoid prompts from apt
ENV DEBIAN_FRONTEND=noninteractive

# Install base dependencies
RUN apt-get update && apt-get install -y \
    curl gnupg apt-transport-https software-properties-common \
    unixodbc-dev libgssapi-krb5-2 libssl3 \
    && rm -rf /var/lib/apt/lists/*

# Install SQL Server ODBC 18 Driver
RUN curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add - && \
    curl https://packages.microsoft.com/config/debian/12/prod.list \
      > /etc/apt/sources.list.d/mssql-release.list && \
    apt-get update && ACCEPT_EULA=Y apt-get install -y msodbcsql18

# Install Azure CLI
RUN curl -sL https://aka.ms/InstallAzureCLIDeb | bash

# Install uv
RUN curl -LsSf https://astral.sh/uv/install.sh | sh

# Create vscode user
RUN useradd -ms /bin/bash vscode && \
    mkdir -p /workspaces && \
    chown -R vscode:vscode /workspaces

# Switch to vscode user
USER vscode
WORKDIR /workspaces

# Install Python 3.10 via uv and set up venv
RUN ~/.cargo/bin/uv python install 3.10 && \
    ~/.cargo/bin/uv venv /workspaces/.venv

ENV PATH="/workspaces/.venv/bin:$PATH"

# Copy dependency files first (safe for missing uv.lock)
COPY --chown=vscode:vscode pyproject.toml uv.lock* ./

# Install dependencies
RUN ~/.cargo/bin/uv sync || true

# Copy project files
COPY --chown=vscode:vscode . .

# Default shell
CMD [ "bash" ]