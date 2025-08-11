# Python Starter Project

A Python starter library using uv, devcontainers, and VS Code with optimized development environment.

## Features

- **Fast Package Management**: Uses [uv](https://github.com/astral-sh/uv) for lightning-fast Python package management
- **Dev Container Ready**: Pre-configured VS Code dev container with all dependencies
- **Modern Python Tools**: Ruff for linting/formatting, pytest for testing, coverage reporting
- **Azure Integration**: Built-in support for Azure services (Identity, Storage Blob)
- **Database Support**: Polars, DuckDB, and ODBC connectivity
- **Version Pinning**: Pinned uv version (0.8.7) for consistent builds
- **Cross-Platform**: Tested on Mac and Windows environments

## Prerequisites

- [Docker](https://www.docker.com/products/docker-desktop/)
- [VS Code](https://code.visualstudio.com/) with the [Dev Containers extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)

## Quick Start with Dev Container

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd pythonproject
   ```

2. **Open in VS Code**
   ```bash
   code .
   ```

3. **Reopen in Container**
   - Press `Ctrl+Shift+P` (or `Cmd+Shift+P` on Mac)
   - Select "Dev Containers: Reopen in Container"
   - Wait for the container to build and start

4. **The environment is ready!**
   - Python 3.10 with virtual environment
   - uv 0.8.7 (pinned version)
   - All dependencies installed via uv
   - Linting and formatting configured
   - Testing framework ready

5. **Verify Setup** (Optional but Recommended)
   ```bash
   # Run the comprehensive test suite
   uv run python scripts/test_setup.py
   
   # Or use the development helper
   uv run python scripts/dev.py all
   ```

## 🧪 **Testing Your Setup**

We provide comprehensive testing to ensure your devcontainer works correctly:

### **Quick Test**
```bash
# After container is built, run:
uv run python scripts/test_setup.py
```

### **Manual Testing**
```bash
# Check versions
python --version  # Should show Python 3.10.x
uv --version      # Should show uv 0.8.7

# Test dependencies
uv run python -c "import polars; print('✅ Polars works!')"
uv run python -c "import duckdb; print('✅ DuckDB works!')"

# Test tools
uv run ruff --version
uv run pytest --version
```

### **Cross-Platform Testing**
- **Mac**: Tested with Docker Desktop and VS Code
- **Windows**: Tested with Docker Desktop, WSL2, and VS Code
- **Linux**: Should work with Docker and VS Code

See [TESTING_GUIDE.md](TESTING_GUIDE.md) for detailed testing instructions for each platform.

## Development Workflow

### Package Management
```bash
# Add a new dependency
uv add package-name

# Add a development dependency
uv add --dev package-name

# Install all dependencies
uv sync

# Update dependencies
uv sync --upgrade
```

### Code Quality
```bash
# Format code
uv run ruff format .

# Lint code
uv run ruff check .

# Run tests
uv run pytest

# Run tests with coverage
uv run pytest --cov
```

### Virtual Environment
The dev container automatically creates and activates a virtual environment at `.venv/`. VS Code is configured to use this environment for:
- IntelliSense and autocomplete
- Running Python files
- Debugging
- Terminal sessions

## Project Structure

```
pythonproject/
├── .devcontainer/          # Dev container configuration
├── python_starter_project/ # Main package source
├── tests/                  # Test files
├── scripts/                # Utility scripts
├── configs/                # Configuration files
├── pyproject.toml         # Project configuration and dependencies
├── .uv-version            # Pinned uv version
├── TESTING_GUIDE.md       # Cross-platform testing guide
└── README.md              # This file
```

## Configuration

### Version Pinning
The project uses pinned versions for consistency:
- **Python**: 3.10 (configured in `.python-version`)
- **uv**: 0.8.7 (configured in `.uv-version` and devcontainer)

To update the uv version:
1. Update `.uv-version` with the new version
2. Update `.devcontainer/devcontainer.json` build args
3. Rebuild the container

### Tools Configuration
- **Ruff**: Linting and formatting (configured in `pyproject.toml`)
- **Pytest**: Testing framework with coverage reporting
- **uv**: Package management with virtual environment support

## Performance Optimizations

- **uv bookworm slim image**: Faster container builds and smaller image size
- **Layer caching**: Optimized Docker layers for faster rebuilds
- **Virtual environment**: Isolated dependencies for consistent development
- **Cache directories**: Configured for optimal performance
- **Version pinning**: Ensures consistent behavior across environments

## Troubleshooting

### Container Build Issues
- Ensure Docker is running
- Clear Docker cache: `docker system prune -a`
- Rebuild container: "Dev Containers: Rebuild Container"

### Python Environment Issues
- Check that `.venv/` exists in the container
- Verify Python path in VS Code settings
- Run `uv sync --dev` to reinstall dependencies

### Version Mismatch Issues
- If you see uv version errors, check that `.uv-version` matches the version in devcontainer.json
- Rebuild the container after updating versions

### Cross-Platform Issues
- **Mac**: Check Docker Desktop file sharing permissions
- **Windows**: Ensure WSL2 is enabled and Docker Desktop is configured for WSL2
- **Linux**: Check Docker group permissions

### Performance Issues
- The container uses the official uv image for optimal performance
- Virtual environment is created in the container workspace
- Dependencies are cached for faster subsequent builds

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Ensure code passes linting: `uv run ruff check .`
5. Run tests: `uv run pytest`
6. Test on both Mac and Windows (if possible)
7. Submit a pull request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
