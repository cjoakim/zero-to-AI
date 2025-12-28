#!/bin/bash

# Recreate the python virtual environment and reinstall libs on mac/linux
# using a "modern" python toolchain which includes uv and pyproject.toml
# rather than pip and requirements.in.
# Chris Joakim, 2025

echo "Prune/ensure directories..."
rm -rf venv    # legacy directory 
rm -rf .venv
rm -rf .coverage
rm -rf .pytest_cache
rm -rf htmlcov
mkdir -p out 
mkdir -p tmp 

echo "Creating a new virtual environment in .venv..."
uv venv

echo "Activating the virtual environment..."
source .venv/bin/activate

echo "Installing libraries..."
uv pip install --editable .

# echo "Creating a requirements.txt file..."
# uv pip compile pyproject.toml -o requirements.txt

# uv tree

echo "Activating the virtual environment..."
source .venv/bin/activate

echo "next: source .venv/bin/activate"
