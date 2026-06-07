---
name: mnemo
description: "Local-first AI memory layer for any LLM. Persistent knowledge graph, entity extraction, semantic retrieval across Ollama, OpenAI, Anthropic, or any OpenAI-compatible backend."
version: 1.0.0
author: Hermes Agent
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [ai, llm, memory, knowledge-graph, rust, local-first, agents, rag]
    related_skills: [opencode, codex, claude-code]
---

# mnemo — Local-First AI Memory Layer

A backend-agnostic memory substrate that gives any LLM long-term recall. Mnemo extracts entities from conversations, builds a persistent knowledge graph in SQLite, and surfaces them via semantic retrieval. Works with Ollama (fully offline), OpenAI, Anthropic, or any OpenAI-compatible endpoint.

## Prerequisites

- Python 3.10+ (for the Python wheel) **or** Rust toolchain (for the `cargo` install)
- A configured LLM endpoint: Ollama running locally, or an API key for OpenAI/Anthropic
- ~50 MB disk per million tokens of memory persisted

## Installation

```bash
# Python (fastest)
pip install mnemo

# Rust CLI
cargo install mnemo

# From source
git clone https://github.com/zaydmulani09/mnemo
cd mnemo && cargo build --release
```

## Configuration

Mnemo reads its config from `~/.config/mnemo/config.toml` (or environment variables):

```toml
[backend]
provider = "ollama"          # or "openai" | "anthropic" | "openai_compatible"
model = "llama3.1:8b"
base_url = "http://localhost:11434"   # for ollama or openai_compatible

[storage]
path = "~/.local/share/mnemo/graph.db"

[extraction]
auto_extract = true
entity_types = ["person", "project", "decision", "concept"]
```

For OpenAI/Anthropic, set the env var instead:
```bash
export OPENAI_API_KEY=sk-...
export ANTHROPIC_API_KEY=sk-ant-...
```

## Usage Examples

### Add a memory

```bash
mnemo add "We decided to use Postgres over SQLite for the new billing service"
# → extracts: project=billing service, decision=use Postgres, rationale=...
```

### Query the graph

```bash
mnemo query "Why did we choose Postgres for billing?"
# → returns the linked decision + related entities + supporting context
```

### Start the daemon (so multiple agents share the graph)

```bash
mnemo serve --port 7654
# Other clients (Python SDK, MCP, HTTP) can now hit http://localhost:7654
```

### Use from Python

```python
from mnemo import Client
m = Client("http://localhost:7654")
m.add("Claude Code session 2026-06-07: fixed the cache invalidation race in /api/v2/orders")
ctx = m.query("What did we do about the orders cache?")
for entity in ctx.entities:
    print(entity.name, "→", entity.summary)
```

## Common Pitfalls

- **Empty backends**: If you point Mnemo at Ollama with no model pulled, extraction silently returns nothing. Verify with `mnemo doctor` before adding memories.
- **Graph bloat**: A long-running session can extract thousands of entities. Run `mnemo compact --keep 90d` monthly to prune.
- **No dedup across models**: Switching backends can produce duplicate entity clusters. Re-run `mnemo reindex` after a model swap.
- **API cost surprise**: When pointed at OpenAI/Anthropic, Mnemo calls the model on every `add`. For large batch imports, use `mnemo import --batch-size 50` to throttle.

## Hermes Integration

To give a Hermes agent persistent memory across shifts:

```bash
# In the agent's bootstrap
mnemo serve --port 7654 &
echo $! > /tmp/mnemo.pid
# In the agent prompt, expose the URL so tools can query it
```

The Hermes `delegate_task` worker can read from Mnemo at session start to recover prior context.

## Verification

```bash
# Smoke test
mnemo add "test memory 1"
mnemo query "test memory"  # should return the entry
mnemo stats                # should show >= 1 entity, >= 1 relation
```

## Related Skills

- **opencode** — primary agent harness that benefits from Mnemo-backed context
- **codex** — Codex CLI can consume Mnemo as an MCP server
- **claude-code** — Claude Code session context can be persisted to Mnemo
