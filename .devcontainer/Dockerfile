# syntax=docker/dockerfile:1

FROM debian:bookworm-slim

ENV DEBIAN_FRONTEND=noninteractive
ENV PATH="/workspaces/.venv/bin:/home/vscode/.cargo/bin:$PATH"

# Install base dependencies
RUN apt-get update && apt-get install -y \
    curl \
    build-essential \
    git \
    ca-certificates \
    gnupg \
    apt-transport-https \
    software-properties-common \
    unixodbc-dev \
    libgssapi-krb5-2 \
    && rm -rf /var/lib/apt/lists/*

# Import Microsoft GPG key
RUN curl -fsSL https://packages.microsoft.com/keys/microsoft.asc \
    | gpg --dearmor \
    | tee /usr/share/keyrings/microsoft-prod.gpg > /dev/null

# Add Microsoft repo for correct architecture
RUN arch=$(dpkg --print-architecture) && \
    echo "deb [arch=${arch} signed-by=/usr/share/keyrings/microsoft-prod.gpg] https://packages.microsoft.com/debian/12/prod bookworm main" \
    | tee /etc/apt/sources.list.d/microsoft-prod.list

# Install ODBC Driver 18 and Azure CLI
RUN apt-get update && ACCEPT_EULA=Y apt-get install -y \
    msodbcsql18 \
    azure-cli \
    && rm -rf /var/lib/apt/lists/*

# Create vscode user and workspace
RUN useradd -ms /bin/bash vscode && \
    mkdir -p /workspaces && \
    chown -R vscode:vscode /workspaces

USER vscode
WORKDIR /workspaces

# Install uv and Python 3.10 in one shot
# Install uv as root into /home/vscode/.cargo/bin
RUN export HOME=/home/vscode && \
    curl -LsSf https://astral.sh/uv/install.sh | sh && \
    /home/vscode/.cargo/bin/uv --version && \
    /home/vscode/.cargo/bin/uv python install 3.10 && \
    /home/vscode/.cargo/bin/uv venv /workspaces/.venv --python 3.10 && \
    chown -R vscode:vscode /home/vscode /workspaces
    
# Copy project files
COPY --chown=vscode:vscode . .

# Install dependencies if pyproject.toml exists
RUN if [ -f pyproject.toml ]; then /home/vscode/.cargo/bin/uv sync; fi

CMD [ "bash" ]
