#!/bin/bash

# Recreate the python virtual environment and reinstall libs on mac/linux
# using a "modern" python toolchain which includes uv and pyproject.toml
# rather than pip and requirements.in.
# Chris Joakim, 3Cloud/Cognizant, 2026

echo "Prune/ensure directories..."
rm -rf venv    # legacy directory 
rm -rf .venv
rm -rf .coverage
rm -rf .pytest_cache
rm -rf htmlcov
mkdir -p out 
mkdir -p tmp 

echo "Creating a new virtual environment in .venv ..."
uv venv

echo "Activating the virtual environment ..."
source .venv/bin/activate

echo "Installing libraries ..."
uv pip install --prerelease=allow --editable .

# echo "Creating a requirements.txt file for users of pip instead of uv ..."
# uv pip compile pyproject.toml -o requirements.txt

# uv-cyclonedx.json is used in the RDF Graph session
# uv export --format cyclonedx1.5 > data/uv/uv-cyclonedx.json

uv tree > data/uv/uv-tree.txt
uv tree --outdated --depth=1 > tmp/uv-tree-outdated.txt
 
echo "Listing the installed libraries ..."
uv pip list > data/uv/uv-pip-list.txt
uv pip list
