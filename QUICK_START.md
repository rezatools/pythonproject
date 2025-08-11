# 🚀 Quick Start Guide

## **Mac & Windows Testing Summary**

### **1. Prerequisites (Both Platforms)**
- ✅ Docker Desktop installed and running
- ✅ VS Code with Dev Containers extension
- ✅ Project cloned locally

### **2. Open Project**
```bash
cd pythonproject
code .
```

### **3. Reopen in Container**
- **Mac**: `Cmd+Shift+P` → "Dev Containers: Reopen in Container"
- **Windows**: `Ctrl+Shift+P` → "Dev Containers: Reopen in Container"

### **4. Wait for Build**
- Look for: "✅ uv version 0.8.7 confirmed"
- Container should start successfully

### **5. Test Everything Works**
```bash
# Quick test
uv run python scripts/test_setup.py

# Or manual checks
python --version    # Should show Python 3.10.x
uv --version        # Should show uv 0.8.7
uv run python -c "import polars; print('✅ Polars works!')"
```

## **🔍 What to Expect**

### **Successful Build:**
- ✅ Container builds without errors
- ✅ "uv version 0.8.7 confirmed" message
- ✅ Python environment ready
- ✅ All dependencies installed

### **Common Issues:**
- **Build fails**: Check Docker is running, clear cache with `docker system prune -a`
- **Version mismatch**: Verify `.uv-version` contains `0.8.7`
- **Python not found**: Run `uv sync --dev` in container

## **📱 Platform-Specific Notes**

### **Mac:**
- Docker Desktop should be running
- Check file sharing permissions in Docker Desktop settings

### **Windows:**
- WSL2 should be enabled
- Docker Desktop should be configured for WSL2
- Check Windows Defender exclusions if needed

## **🧪 Full Testing**

For comprehensive testing, see:
- `TESTING_GUIDE.md` - Detailed platform-specific instructions
- `scripts/test_setup.py` - Automated test suite
- `scripts/dev.py` - Development helper commands

## **🚨 Need Help?**

1. Check the troubleshooting section in `README.md`
2. Verify all version files match (`.uv-version`, `devcontainer.json`)
3. Ensure Docker has enough resources allocated
4. Try rebuilding the container: "Dev Containers: Rebuild Container"
