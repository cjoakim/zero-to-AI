"""
Unit tests for the markdown chunker (sentence-boundary chunking).
No blob storage or database connections; uses local fixture files only.
"""

import os

import pytest

from src.util.markdown import MarkdownChunker, _split_into_sentences

# pytest -v tests/test_markdown_chunker.py

FIXTURE_PATH = os.path.join(os.path.dirname(__file__), "test_data", "markdown_chunker_fixture.txt")
MAX_CHARS = 2000


def _load_fixture() -> str:
    with open(FIXTURE_PATH, encoding="utf-8") as f:
        return f.read()


@pytest.mark.skip(reason="currently disabled")
def test_chunker_uses_fixture_file():
    """Fixture file exists and has content."""
    assert os.path.isfile(FIXTURE_PATH), f"Fixture not found: {FIXTURE_PATH}"
    text = _load_fixture()
    assert len(text) > MAX_CHARS, "Fixture must be larger than MAX_CHARS to test multiple chunks"


@pytest.mark.skip(reason="currently disabled")
def test_chunker_produces_expected_number_of_chunks():
    """Chunker splits large text into an expected number of chunks (no page breaks)."""
    text = _load_fixture()
    mc = MarkdownChunker(filename=None, opts={})
    mc.file_lines = text.splitlines()
    mc.chunk_by_character_count(max_chars=MAX_CHARS)
    chunks = mc.chunks
    assert len(chunks) >= 2, "Fixture is > 2000 chars so we expect at least 2 chunks"
    # With ~7K char fixture at max 2000 we get ~4 chunks; upper bound allows fixture to grow
    assert 2 <= len(chunks) <= 25, "Chunk count should be reasonable for fixture size"


@pytest.mark.skip(reason="currently disabled")
def test_no_chunk_exceeds_max_characters():
    """No chunk contains more than MAX_CHARS (2000) characters."""
    text = _load_fixture()
    mc = MarkdownChunker(filename=None, opts={})
    mc.file_lines = text.splitlines()
    mc.chunk_by_character_count(max_chars=MAX_CHARS)
    for i, chunk in enumerate(mc.chunks):
        chunk_text = chunk.as_text()
        assert len(chunk_text) <= MAX_CHARS, (
            f"Chunk {i + 1} has {len(chunk_text)} chars (max {MAX_CHARS}): "
            f"{chunk_text[:80]}..."
        )


@pytest.mark.skip(reason="currently disabled")
def test_no_chunk_contains_partial_sentences():
    """Every chunk contains only complete sentences (none cut mid-sentence)."""
    text = _load_fixture()
    mc = MarkdownChunker(filename=None, opts={})
    mc.file_lines = text.splitlines()
    mc.chunk_by_character_count(max_chars=MAX_CHARS)
    for i, chunk in enumerate(mc.chunks):
        chunk_text = chunk.as_text()
        sentences = _split_into_sentences(chunk_text)
        for j, sent in enumerate(sentences):
            s = sent.strip()
            if not s:
                continue
            assert s[-1] in ".!?", (
                f"Chunk {i + 1} has partial sentence (segment does not end with .!?): "
                f"'{s[:60]}...'"
            )


@pytest.mark.skip(reason="currently disabled")
def test_chunker_reassembles_to_original_content():
    """Reassembled chunks contain the same sentences as the original (no loss or duplication)."""
    text = _load_fixture()
    mc = MarkdownChunker(filename=None, opts={})
    mc.file_lines = text.splitlines()
    mc.chunk_by_character_count(max_chars=MAX_CHARS)
    reassembled = "\n".join(c.as_text() for c in mc.chunks)
    orig_sentences = _split_into_sentences(text)
    reass_sentences = _split_into_sentences(reassembled)
    assert orig_sentences == reass_sentences, (
        "Reassembled chunks should yield the same sentences as original"
    )
