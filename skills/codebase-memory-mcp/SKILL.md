---
name: codebase-memory-mcp
description: "High-performance code intelligence MCP server — index codebases into persistent knowledge graphs with sub-ms queries."
version: 1.0.0
author: Hermes Agent
license: MIT
platforms: [linux, macos]
metadata:
  hermes:
    tags: [code-intelligence, mcp, knowledge-graph, codebase-analysis, rag]
    related_skills: [crawl4ai, headroom]
---

# Codebase Memory MCP — Code Intelligence Server

High-performance code intelligence MCP server written in C. Indexes entire codebases into persistent knowledge graphs with 155-language support and sub-millisecond queries.

## Prerequisites

- Linux or macOS
- No runtime dependencies (single static binary)

## Installation

```bash
# Download latest release
curl -sL https://github.com/DeusData/codebase-memory-mcp/releases/latest/download/codebase-memory-mcp \
  -o /usr/local/bin/codebase-memory-mcp
chmod +x /usr/local/bin/codebase-memory-mcp

# Or build from source
git clone https://github.com/DeusData/codebase-memory-mcp.git
cd codebase-memory-mcp
make
cp codebase-memory-mcp /usr/local/bin/
```

## Usage

### Index a Codebase

```bash
# Index current directory
codebase-memory-mcp index .

# Index specific directory
codebase-memory-mcp index /path/to/repo

# Index with custom output
codebase-memory-mcp index /path/to/repo --output /tmp/codebase.db
```

### Run as MCP Server

```bash
# Default port
codebase-memory-mcp serve

# Custom port
codebase-memory-mcp serve --port 3000

# With persistent storage
codebase-memory-mcp serve --db /path/to/codebase.db
```

### Query from CLI

```bash
# Search for functions
codebase-memory-mcp query "find all authentication middleware"

# Search for types
codebase-memory-mcp query "User model definition"

# Search for patterns
codebase-memory-mcp query "error handling in API routes"
```

## Integration with Hermes Agent

### MCP Config

```json
{
  "mcpServers": {
    "codebase-memory": {
      "command": "codebase-memory-mcp",
      "args": ["serve", "--port", "3001"],
      "env": {
        "CODEBASE_PATH": "/path/to/your/repo"
      }
    }
  }
}
```

### Workflow

```bash
# 1. Index your codebase (once, or on changes)
codebase-memory-mcp index /path/to/repo

# 2. Start MCP server
codebase-memory-mcp serve --db /path/to/codebase.db &

# 3. Query from agent or CLI
codebase-memory-mcp query "How does the auth system work?"
```

## Supported Languages

C, C++, C#, Go, Java, JavaScript, TypeScript, Python, Ruby, Rust, Swift, Kotlin, PHP, Scala, Haskell, Elixir, Erlang, Clojure, F#, and 135+ more via Tree-sitter grammars.

## Common Pitfalls

1. **Initial indexing takes time**: Large codebases (1M+ LOC) may take 5-10 minutes to index. Subsequent queries are sub-millisecond.
2. **Memory usage**: Indexing uses ~2x the codebase size in RAM. Ensure sufficient memory for large repos.
3. **Incremental updates**: Re-run `index` after major code changes. The binary handles deduplication.

## Verification

```bash
# Test installation
codebase-memory-mcp --version

# Test indexing
codebase-memory-mcp index /path/to/small-repo
echo $?

# Test querying
codebase-memory-mcp query "main function"

# Test MCP server
codebase-memory-mcp serve --port 3001 &
curl http://localhost:3001/health
```

## Sources

- **GitHub:** [DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp)
- **Stars:** 2,770 (↑~30/day)
- **License:** MIT
- **Discovered:** 2026-05-29 via GitHub search
