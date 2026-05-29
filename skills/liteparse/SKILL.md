---
name: liteparse
description: "Fast document parsing for RAG pipelines via LiteParse (Rust, 100x faster than Python parsers)"
tags: [rag, document-parsing, rust, pdf, llm]
related_skills: [crawl4ai, huggingface-hub]
---

# LiteParse — Fast Document Parsing for RAG

> Parse PDFs, DOCX, HTML, and other documents 100x faster than Python parsers. From the LlamaIndex team.

## Prerequisites

- Rust toolchain (or Python pip)
- LiteParse installed: `cargo install liteparse` or `pip install liteparse`

## Usage

### CLI — Parse a single document
```bash
liteparse document.pdf --output ./parsed/
```

### CLI — Parse a directory
```bash
liteparse ./documents/ --recursive --output ./parsed/
```

### Python API — Integration with RAG pipelines
```python
from liteparse import parse

result = parse("document.pdf")
print(result.markdown)   # Clean markdown output
print(result.tables)     # Extracted tables as dataframes
print(result.images)     # Extracted images as paths
print(result.metadata)   # Title, author, dates
```

### MCP Server — For AI agents
```bash
liteparse serve --port 8091
# Add to agent config:
# "mcpServers": {"liteparse": {"command": "liteparse", "args": ["serve", "--port", "8091"]}}
```

## Supported Formats

| Format | Support | Notes |
|--------|---------|-------|
| PDF | ✅ Full | Text, tables, images, metadata |
| DOCX | ✅ Full | Headings, lists, tables |
| HTML | ✅ Full | DOM-aware extraction |
| Markdown | ✅ Passthrough | Clean formatting |
| EPUB | ✅ Full | Chapter structure preserved |

## Pitfalls

1. **Scanned PDFs**: LiteParse extracts embedded text. For scanned PDFs, pair with OCR (tesseract) first.
2. **Complex tables**: Multi-row spanning tables may need manual cleanup in output.
3. **Memory usage**: Large documents (>100MB) may need chunked processing.
4. **Encoding**: Non-UTF-8 documents may need preprocessing.

## Verification

```bash
# Parse a test document and verify output
liteparse test.pdf --output ./test-output/
cat ./test-output/test.md  # Should contain extracted text
ls ./test-output/           # Should contain images if present
```
