# Utility clases to chunk a Markdown file as produced by the
# Document Intelligence Service into chunks, and optionally
# iterate over the chunks and n-number of adjacent chunks.

import re

# Split after sentence-ending punctuation when followed by whitespace or end
SENTENCE_REGEX = r"(?<=[.!?;])\s+"


class TextChunk:
    def __init__(self):
        self.lines = list()

    def add_line(self, line: str, max_line_length: int = 8000):
        if line is not None:
            if len(line) < max_line_length:
                self.lines.append(line.rstrip())
            else:
                parts = line.split("\n")
                for part in parts:
                    self.lines.append(part.rstrip())

    def line_count(self) -> int:
        return len(self.lines)

    def is_empty(self) -> bool:
        return self.line_count() == 0

    def has_content(self) -> bool:
        return len(self.as_text().strip()) > 0

    def as_text(self) -> str:
        return "\n".join(self.lines).strip()


class MarkdownChunker:
    def __init__(self, opts: dict = {}):
        self.opts = opts
        self.chunks: list[TextChunk] = list()
        self.errors: list[str] = list()
        self.chunk_strategy = "page"
        self.max_chars_per_chunk = 8000
        self.sentences = list()

        try:
            if "chunk_strategy" in self.opts.keys():
                self.chunk_strategy = str(self.opts["chunk_strategy"]).strip().lower()
            if "max_chars_per_chunk" in self.opts.keys():
                self.max_chars_per_chunk = int(self.opts["max_chars_per_chunk"])
        except Exception as e:
            self.errors.append(str(e))

    def chunk_content(self, content: str) -> list[TextChunk]:
        """
        Chunk the given markdown content string.
        """
        if content is not None:
            self.content_lines = content.splitlines()
            if self.chunk_strategy == "character_count":
                self.chunk_by_character_count()
            else:
                self.chunk_by_page()
        return self.chunks

    def chunk_count(self) -> int:
        return len(self.chunks)

    def chunk_by_page(self):
        """
        Chunk by page breaks (e.g. <!-- PageBreak --> from Document Intelligence).
        If a page exceeds self.max_chars_per_chunk, it is split on line boundaries so
        embedding APIs (e.g. 8K char limit) are not exceeded.
        """
        curr_chunk = TextChunk()
        for line in self.content_lines:
            # The Markdown content may have lines that look like this:
            # <!-- PageNumber="6" -->
            # <!-- PageFooter="NATIONAL CONSTITUTION CENTER" -->
            # <!-- PageBreak -->
            if line.startswith("<!-- PageBreak -->"):
                if not curr_chunk.is_empty():
                    self.add_chunk(curr_chunk)
                curr_chunk = TextChunk()
            elif line.startswith("<!-- Page"):
                pass
            else:
                curr_chunk.add_line(line, self.max_chars_per_chunk)

        if not curr_chunk.is_empty():
            self.add_chunk(curr_chunk)

    def chunk_by_character_count(self):
        """
        Chunk by character count, splitting on sentence boundaries.
        """
        lines = list()
        for line in self.content_lines:
            if not line.startswith("<!-- Page"):
                lines.append(line)
        text = "\n".join(lines)
        self.sentences = self.split_into_sentences(text)
        print("sentences: {}".format(len(self.sentences)))
        self.chunks = self.chunks_from_sentences(self.sentences)

    def add_chunk(self, chunk: TextChunk):
        text_len = len(chunk.as_text())
        if text_len > self.max_chars_per_chunk:
            large_chunks = self.split_large_chunk(chunk, self.max_chars_per_chunk)
            for large_chunk in large_chunks:
                self.chunks.append(large_chunk)
        else:
            self.chunks.append(chunk)

    def split_large_chunk(self, chunk: TextChunk) -> list[TextChunk]:
        """
        Split a chunk that exceeds self.max_chars_per_chunk on sentence boundaries
        so no sentence is split up.
        """
        sentences = self.split_into_sentences(chunk.as_text())
        return self.chunks_from_sentences(sentences)

    def split_into_sentences(self, text: str) -> list[str]:
        """
        Split text into sentences on . ! ? followed by whitespace.
        Keeps complete sentences so chunking never breaks mid-sentence.
        """
        sentences = list()
        parts = re.split(SENTENCE_REGEX, text)
        for part in parts:
            sentences.append(str(part.strip()))
        print("sentences: {}".format(len(sentences)))
        return sentences

    def chunks_from_sentences(self, sentences: list[str]) -> list[TextChunk]:
        """
        Build chunks from sentences so we never split mid-sentence.
        When adding the next sentence would exceed max_chars, start a new chunk.
        The full sentence is always included (may slightly exceed the limit).
        """
        chunks = list()
        curr_chunk = TextChunk()
        for s in sentences:
            if isinstance(s, str):
                sum = len(s) + len(curr_chunk.as_text())
                if sum > self.max_chars_per_chunk:
                    chunks.append(curr_chunk)
                    curr_chunk = TextChunk()
                    curr_chunk.add_line(s, self.max_chars_per_chunk)
                else:
                    curr_chunk.add_line(s, self.max_chars_per_chunk)
        if curr_chunk.has_content():
            chunks.append(curr_chunk)
        return chunks
