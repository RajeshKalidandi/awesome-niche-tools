---
name: headroom
description: "Token compression for LLM applications — compress tool outputs, logs, and RAG chunks by 60-95% before they reach the LLM."
version: 1.0.0
author: Hermes Agent
license: Apache-2.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [llm, tokens, compression, cost-optimization, mcp, rag]
    related_skills: [crawl4ai, codebase-memory-mcp]
---

# Headroom — Token Compression for LLM Applications

Compress tool outputs, logs, files, and RAG chunks before they reach the LLM. 60-95% fewer tokens, same answers.

## Prerequisites

- Python 3.9+
- pip

## Installation

```bash
pip install headroom
```

## Usage

### As MCP Server (Recommended)

Add to your Hermes Agent config or any MCP-compatible agent:

```bash
headroom mcp-server --port 8080
```

MCP config:
```json
{
  "mcpServers": {
    "headroom": {
      "command": "headroom",
      "args": ["mcp-server", "--port", "8080"]
    }
  }
}
```

### As Python Library

```python
from headroom import compress

# Compress text to 30% of original size
long_output = "..."  # Your tool output, log, or RAG chunk
compressed = compress(long_output, target_ratio=0.3)

# Use compressed output with your LLM
response = llm.chat(compressed)
```

### As HTTP Proxy

```bash
# Proxy OpenAI API calls through Headroom
headroom proxy --upstream https://api.openai.com/v1/chat/completions

# Your app sends requests to http://localhost:8080 instead
# Headroom compresses inputs and decompresses outputs transparently
```

## Configuration

### Compression Ratios

| Ratio | Use Case | Token Savings |
|-------|----------|---------------|
| 0.1 | Maximum compression (logs, verbose output) | ~90% |
| 0.3 | Balanced (tool outputs, RAG chunks) | ~70% |
| 0.5 | Conservative (code, structured data) | ~50% |
| 0.7 | Minimal (already concise text) | ~30% |

### Environment Variables

```bash
HEADROOM_DEFAULT_RATIO=0.3    # Default compression ratio
HEADROOM_CACHE_SIZE=1000       # LRU cache size
HEADROOM_LOG_LEVEL=info        # Logging verbosity
```

## Common Pitfalls

1. **Over-compression on code**: Code loses meaning below 0.5 ratio. Use 0.5-0.7 for code blocks.
2. **Missing context**: Very short texts (<100 tokens) don't benefit from compression. Skip them.
3. **Streaming responses**: The proxy mode doesn't support streaming yet. Use library mode for streaming.

## Verification

```bash
# Test installation
headroom --version

# Test compression
echo "This is a test output that should be compressed significantly by the Headroom library for LLM consumption" | headroom compress --ratio 0.3

# Test MCP server
headroom mcp-server --port 8080 &
curl http://localhost:8080/health
```

## Sources

- **GitHub:** [chopratejas/headroom](https://github.com/chopratejas/headroom)
- **Stars:** 2,063 (↑~50/day)
- **License:** Apache-2.0
- **Discovered:** 2026-05-29 via GitHub search
