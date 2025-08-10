# python-starter-project

A Python starter library using **uv**, **devcontainers**, and **VS Code**.

## 🚀 Getting Started

1. **Install VS Code** and the [Dev Containers extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers).
2. Clone this repo.
3. Open the folder in VS Code.
4. When prompted, **Reopen in Container**.
5. The container will be built with:
   - Python 3.10 (via uv)
   - SQL Server ODBC Driver 18
   - Azure CLI
   - All project dependencies

## 📦 Running Scripts
Inside the container:
```bash
uv run python scripts/example.py
```

## 🧪 Running Tests
```bash
uv run pytest
```

## 📂 Configuration
Edit `configs/config.yaml` for project-specific settings.
