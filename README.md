# python-starter-project

A Python starter library using **uv**, **devcontainers**, and **VS Code**.

## 🚀 Getting Started

1. Install VS Code and the [Dev Containers extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers).
2. Clone this repo.
3. Open the folder in VS Code.
4. When prompted, Reopen in Container.

The container includes:
- Python (via uv)
- SQL Server ODBC Driver 18
- Azure CLI
- All project dependencies

### Python version
- Default Python version in the dev container is 3.10.
- You can override it by exporting a local env var before opening the container:
  - macOS/Linux: `export PYTHON_VERSION=3.11`
  - Windows (PowerShell): `$Env:PYTHON_VERSION = "3.11"`

The value is passed into the build and exposed as `PYTHON_VERSION` in the container. On first create, uv will create the venv using that version.

### Virtual environment location and permissions
- The project uses `.venv` inside the workspace, but it is mounted as a named Docker volume from the container side.
- This avoids permission issues when the repo is bind-mounted from the host (macOS/Windows).
- The venv is created at container start (not image build) by the devcontainer `postCreateCommand` and is owned by the non-root `vscode` user.

## 📦 Running Scripts
Inside the container:

```bash
uv run python scripts/example.py
```

A Polars example is also provided:

```bash
uv run python scripts/polars_example.py
```

## 🧪 Running Tests

```bash
uv run pytest -q
```

## 📂 Configuration

Edit `configs/config.yaml` for project-specific settings.

## 🛠️ CI

GitHub Actions workflow runs tests on Linux, macOS, and Windows across Python 3.10 and 3.11 using uv.
