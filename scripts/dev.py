#!/usr/bin/env python3
"""
Development helper script for common tasks.
Run with: uv run python scripts/dev.py
"""

import argparse
import subprocess
import sys
from pathlib import Path


def run_command(cmd, check=True):
    """Run a command and return the result."""
    print(f"Running: {cmd}")
    result = subprocess.run(cmd, shell=True, check=check, capture_output=True, text=True)
    if result.stdout:
        print(result.stdout)
    if result.stderr:
        print(result.stderr, file=sys.stderr)
    return result


def format_code():
    """Format code using ruff."""
    print("Formatting code...")
    run_command("uv run ruff format .")


def lint_code():
    """Lint code using ruff."""
    print("Linting code...")
    result = run_command("uv run ruff check .", check=False)
    if result.returncode != 0:
        print("Linting found issues. Fix them and try again.")
        sys.exit(1)
    print("✅ Code passed linting!")


def run_tests(verbose=False):
    """Run tests using pytest."""
    print("Running tests...")
    cmd = "uv run pytest"
    if verbose:
        cmd += " -v"
    result = run_command(cmd, check=False)
    if result.returncode != 0:
        print("❌ Tests failed!")
        sys.exit(1)
    print("✅ All tests passed!")


def run_tests_with_coverage():
    """Run tests with coverage reporting."""
    print("Running tests with coverage...")
    result = run_command("uv run pytest --cov", check=False)
    if result.returncode != 0:
        print("❌ Tests failed!")
        sys.exit(1)
    print("✅ Coverage report generated!")


def sync_dependencies():
    """Sync project dependencies."""
    print("Syncing dependencies...")
    run_command("uv sync --dev")
    print("✅ Dependencies synced!")


def main():
    parser = argparse.ArgumentParser(description="Development helper script")
    parser.add_argument("command", choices=[
        "format", "lint", "test", "test-cov", "sync", "all"
    ], help="Command to run")
    parser.add_argument("--verbose", "-v", action="store_true", help="Verbose output")

    args = parser.parse_args()

    if args.command == "format":
        format_code()
    elif args.command == "lint":
        lint_code()
    elif args.command == "test":
        run_tests(args.verbose)
    elif args.command == "test-cov":
        run_tests_with_coverage()
    elif args.command == "sync":
        sync_dependencies()
    elif args.command == "all":
        print("Running all checks...")
        format_code()
        lint_code()
        run_tests(args.verbose)
        print("✅ All checks completed!")


if __name__ == "__main__":
    main()
