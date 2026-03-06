import pytest

from src.util.markdown import Chunk, MarkdownChunker

# pytest -v tests/test_markdown.py


@pytest.mark.skip(reason="currently disabled")
def test_text_chunk():
    chunk = Chunk()
    chunk.add_line("This is a test.")
    chunk.add_line("This is only a test.")
    assert chunk.line_count() == 2
    assert not chunk.is_empty()
    assert chunk.as_text() == "This is a test.\nThis is only a test."


@pytest.mark.skip(reason="currently disabled")
def test_empty_text_chunk():
    chunk = Chunk()
    assert chunk.line_count() == 0
    assert chunk.is_empty()
    assert chunk.as_text() == ""


@pytest.mark.skip(reason="currently disabled")
def test_chunking():
    opts = dict()
    mc = MarkdownChunker(filename="tests/test_data/sample.md", opts=opts)
    chunks = mc.chunk_document()
    assert len(mc.errors) == 0
    # May be 7 (one per page) or more if a page exceeded max chars and was split on sentence boundaries
    assert len(chunks) >= 7
    for chunk in chunks:
        assert isinstance(chunk, Chunk)

    for idx, chunk in enumerate(chunks):
        txt = chunk.as_text().replace("\n", " ")
        print("---\nChunk {}: {} {}".format(idx, chunk.line_count(), txt))

    # Gettysburg Address may be in one chunk or split across chunks (sentence-boundary splitting)
    all_text = " ".join(c.as_text() for c in chunks)
    assert "## The Gettysburg Address" in all_text
    assert "shall not perish from the earth." in all_text
