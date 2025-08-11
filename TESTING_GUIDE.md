# DevContainer Testing Guide

This guide helps you test the devcontainer setup on both Mac and Windows environments to ensure everything works correctly.

## 🍎 **Mac Environment Testing**

### Prerequisites Check
```bash
# Check Docker installation
docker --version
docker ps

# Check VS Code installation
code --version

# Check if Dev Containers extension is installed
# Open VS Code → Extensions → Search "Dev Containers"
```

### Step-by-Step Testing

1. **Open Project in VS Code**
   ```bash
   cd pythonproject
   code .
   ```

2. **Install Dev Containers Extension** (if not already installed)
   - Press `Cmd+Shift+X` to open Extensions
   - Search for "Dev Containers"
   - Install "Dev Containers" by Microsoft

3. **Reopen in Container**
   - Press `Cmd+Shift+P` to open Command Palette
   - Type "Dev Containers: Reopen in Container"
   - Select the option and wait for container build

4. **Verify Container Build Success**
   - Look for "✅ uv version 0.8.7 confirmed" in build logs
   - Container should start successfully
   - Terminal should show container environment

5. **Test Python Environment**
   ```bash
   # Check Python version
   python --version
   # Expected: Python 3.10.x
   
   # Check uv version
   uv --version
   # Expected: uv 0.8.7
   
   # Check virtual environment
   which python
   # Expected: /workspaces/pythonproject/.venv/bin/python
   ```

6. **Test Dependencies**
   ```bash
   # Test package imports
   uv run python -c "import polars; print('✅ Polars imported successfully')"
   uv run python -c "import duckdb; print('✅ DuckDB imported successfully')"
   uv run python -c "import azure.identity; print('✅ Azure Identity imported successfully')"
   ```

7. **Test Development Tools**
   ```bash
   # Test linting
   uv run ruff check .
   
   # Test formatting
   uv run ruff format . --check
   
   # Test pytest
   uv run pytest --version
   ```

## 🪟 **Windows Environment Testing**

### Prerequisites Check
```cmd
# Check Docker Desktop installation
docker --version
docker ps

# Check VS Code installation
code --version

# Ensure Docker Desktop is running
# Check system tray for Docker Desktop icon
```

### Step-by-Step Testing

1. **Open Project in VS Code**
   ```cmd
   cd pythonproject
   code .
   ```

2. **Install Dev Containers Extension** (if not already installed)
   - Press `Ctrl+Shift+X` to open Extensions
   - Search for "Dev Containers"
   - Install "Dev Containers" by Microsoft

3. **Reopen in Container**
   - Press `Ctrl+Shift+P` to open Command Palette
   - Type "Dev Containers: Reopen in Container"
   - Select the option and wait for container build

4. **Verify Container Build Success**
   - Look for "✅ uv version 0.8.7 confirmed" in build logs
   - Container should start successfully
   - Terminal should show container environment

5. **Test Python Environment**
   ```bash
   # Check Python version
   python --version
   # Expected: Python 3.10.x
   
   # Check uv version
   uv --version
   # Expected: uv 0.8.7
   
   # Check virtual environment
   which python
   # Expected: /workspaces/pythonproject/.venv/bin/python
   ```

6. **Test Dependencies**
   ```bash
   # Test package imports
   uv run python -c "import polars; print('✅ Polars imported successfully')"
   uv run python -c "import duckdb; print('✅ DuckDB imported successfully')"
   uv run python -c "import azure.identity; print('✅ Azure Identity imported successfully')"
   ```

7. **Test Development Tools**
   ```bash
   # Test linting
   uv run ruff check .
   
   # Test formatting
   uv run ruff format . --check
   
   # Test pytest
   uv run pytest --version
   ```

## 🧪 **Automated Testing Script**

Use the development helper script to run comprehensive tests:

```bash
# Run all checks
uv run python scripts/dev.py all

# Individual tests
uv run python scripts/dev.py format
uv run python scripts/dev.py lint
uv run python scripts/dev.py test
uv run python scripts/dev.py test-cov
```

## 🔍 **Troubleshooting Common Issues**

### Mac-Specific Issues

1. **Docker Permission Denied**
   ```bash
   # Add user to docker group
   sudo usermod -aG docker $USER
   # Log out and back in
   ```

2. **VS Code Can't Find Docker**
   - Ensure Docker Desktop is running
   - Check Docker Desktop settings for file sharing permissions

### Windows-Specific Issues

1. **Docker Desktop Not Starting**
   - Check Windows Subsystem for Linux (WSL) is enabled
   - Ensure virtualization is enabled in BIOS
   - Check Windows Defender exclusions

2. **Path Issues in Container**
   - Ensure project is in a path accessible to Docker Desktop
   - Check Docker Desktop file sharing settings

### General Issues

1. **Container Build Fails**
   ```bash
   # Clear Docker cache
   docker system prune -a
   
   # Rebuild container
   # VS Code: "Dev Containers: Rebuild Container"
   ```

2. **Python Environment Not Detected**
   ```bash
   # Reinstall dependencies
   uv sync --dev
   
   # Check VS Code Python interpreter setting
   # Should point to .venv/bin/python
   ```

3. **Version Mismatch Errors**
   - Verify `.uv-version` contains `0.8.7`
   - Check devcontainer.json build args
   - Rebuild container after version changes

## 📋 **Success Checklist**

- [ ] Container builds successfully
- [ ] "✅ uv version 0.8.7 confirmed" appears in logs
- [ ] Python 3.10 environment is active
- [ ] Virtual environment is created at `.venv/`
- [ ] All dependencies can be imported
- [ ] Development tools (ruff, pytest) work
- [ ] VS Code Python extension detects the environment
- [ ] IntelliSense and autocomplete work

## 🚀 **Performance Verification**

After successful setup, verify performance:

```bash
# Check container startup time
time docker build -f .devcontainer/Dockerfile .

# Check dependency installation speed
time uv sync --dev

# Check Python import speed
time uv run python -c "import polars"
```

## 📝 **Reporting Issues**

If you encounter issues:

1. **Collect Environment Info**
   - OS version and architecture
   - Docker version
   - VS Code version
   - Dev Containers extension version

2. **Collect Error Logs**
   - Container build logs
   - VS Code developer console logs
   - Docker logs

3. **Document Steps to Reproduce**
   - Exact commands run
   - Expected vs actual behavior
   - Screenshots if helpful

## 🔄 **Continuous Testing**

For ongoing development:

- Test container rebuilds after dependency changes
- Verify new team members can successfully build containers
- Test on different machine configurations
- Monitor build times and optimize as needed
