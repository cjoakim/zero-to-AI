#!/bin/bash

# Demonstration of text extraction, chunking, and vectorization.
# Chris Joakim, 3Cloud/Cognizant, 2026

echo "Activating the virtual environment ..."
source .venv/bin/activate

echo "=== Delete output tmp/ files ==="
rm tmp/*.*

echo "=== Display Document Intelligence supported filetypes ==="
python main-docintel.py supported_filetypes

echo "=== Extract text from us_constitution.pdf using Document Intelligence ==="
python main-docintel.py extract_text data/documents/US_Constitution.pdf > tmp/x.txt

echo "=== Chunk the extracted markdown file using Azure OpenAI ==="
python main-docintel.py chunk_markdown tmp/US_Constitution.pdf.md

echo "=== TODO: Persist the vectorized documents into a Vector Database ==="

echo "done"
