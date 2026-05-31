---
name: gemini-web2api
description: "Convert Google Gemini web into an OpenAI-compatible API. Zero auth, single file, drop-in replacement."
version: 1.0.0
author: Hermes Agent
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [llm, api, gemini, openai, proxy, free-tier]
    related_skills: [llama-cpp, serving-llms-vllm]
---

# gemini-web2api

Convert Google Gemini's web interface into an OpenAI-compatible API endpoint. No API keys needed — uses your Gemini web session.

## Prerequisites

- Python 3.8+
- A Google account with Gemini access
- pip

## Installation

```bash
pip install gemini-web2api
```

## Quick Start

```bash
# Start the server
gemini-web2api --port 8080

# Test with curl
curl http://localhost:8080/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{"model":"gemini","messages":[{"role":"user","content":"Hello!"}]}'
```

## Configuration

### Environment Variables

- `GEMINI_SESSION` — Gemini web session token (auto-extracted if not set)
- `PORT` — Server port (default: 8080)
- `HOST` — Bind address (default: 0.0.0.0)

### OpenAI Client Configuration

```python
import openai

client = openai.OpenAI(
    base_url="http://localhost:8080/v1",
    api_key="not-needed"  # Any string works
)

response = client.chat.completions.create(
    model="gemini",
    messages=[{"role": "user", "content": "Explain quantum computing"}]
)
```

## Usage Patterns

### As a Drop-in OpenAI Replacement

```bash
export OPENAI_API_BASE=http://localhost:8080/v1
export OPENAI_API_KEY=not-needed

# Now any OpenAI-compatible tool works
python my_script.py
```

### With Hermes Agent

Add to config.yaml:
```yaml
providers:
  - name: gemini-free
    base_url: http://localhost:8080/v1
    api_key: not-needed
    models:
      - gemini
```

### Streaming Support

```python
stream = client.chat.completions.create(
    model="gemini",
    messages=[{"role": "user", "content": "Write a story"}],
    stream=True
)
for chunk in stream:
    print(chunk.choices[0].delta.content, end="")
```

## Common Pitfalls

1. **Session expiration** — Gemini web sessions expire after ~2 hours. Restart the server or refresh the session token.
2. **Rate limits** — Gemini web has implicit rate limits. High-volume usage may trigger temporary blocks.
3. **Model naming** — Use `model: "gemini"` in requests. The server maps this to the appropriate Gemini model.
4. **Tool calling** — Supported but not all Gemini tools are exposed through the web interface.

## Verification

```bash
# Test server is running
curl -s http://localhost:8080/v1/models | python3 -m json.tool

# Test completion
curl -s http://localhost:8080/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{"model":"gemini","messages":[{"role":"user","content":"Say hello"}]}' \
  | python3 -m json.tool
```

## Source

- GitHub: https://github.com/Sophomoresty/gemini-web2api
- Stars: 870 (as of 2026-06-01)
- License: MIT
