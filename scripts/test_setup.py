#!/usr/bin/env python3
"""
Quick test script to verify the devcontainer setup.
Run this after the container is built to ensure everything works.
"""

import sys
import subprocess
import importlib.util


def run_command(cmd, description):
    """Run a command and return success status."""
    print(f"Testing: {description}")
    try:
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True, check=True)
        print(f"✅ {description} - SUCCESS")
        if result.stdout.strip():
            print(f"   Output: {result.stdout.strip()}")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ {description} - FAILED")
        print(f"   Error: {e}")
        if e.stderr:
            print(f"   Stderr: {e.stderr}")
        return False


def test_import(module_name, description):
    """Test if a module can be imported."""
    print(f"Testing: {description}")
    try:
        importlib.import_module(module_name)
        print(f"✅ {description} - SUCCESS")
        return True
    except ImportError as e:
        print(f"❌ {description} - FAILED")
        print(f"   Error: {e}")
        return False


def main():
    """Run all tests."""
    print("🧪 Testing DevContainer Setup")
    print("=" * 50)
    
    tests_passed = 0
    total_tests = 0
    
    # Test Python version
    total_tests += 1
    if run_command("python --version", "Python version check"):
        tests_passed += 1
    
    # Test uv version
    total_tests += 1
    if run_command("uv --version", "uv version check"):
        tests_passed += 1
    
    # Test virtual environment
    total_tests += 1
    if run_command("which python", "Virtual environment check"):
        tests_passed += 1
    
    # Test key dependencies
    dependencies = [
        ("polars", "Polars import"),
        ("duckdb", "DuckDB import"),
        ("azure.identity", "Azure Identity import"),
        ("azure.storage.blob", "Azure Storage Blob import"),
    ]
    
    for module, description in dependencies:
        total_tests += 1
        if test_import(module, description):
            tests_passed += 1
    
    # Test development tools
    total_tests += 1
    if run_command("uv run ruff --version", "Ruff version check"):
        tests_passed += 1
    
    total_tests += 1
    if run_command("uv run pytest --version", "Pytest version check"):
        tests_passed += 1
    
    # Test uv commands
    total_tests += 1
    if run_command("uv sync --check", "Dependencies sync check"):
        tests_passed += 1
    
    print("\n" + "=" * 50)
    print(f"📊 Test Results: {tests_passed}/{total_tests} tests passed")
    
    if tests_passed == total_tests:
        print("🎉 All tests passed! Your devcontainer is working correctly.")
        return 0
    else:
        print("⚠️  Some tests failed. Check the output above for issues.")
        return 1


if __name__ == "__main__":
    sys.exit(main())
