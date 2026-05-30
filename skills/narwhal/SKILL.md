---
name: narwhal
description: "TUI database client with built-in MCP server — postgres, mysql, sqlite, duckdb, clickhouse, vim editing, Lua plugins."
tags: [database, tui, mcp, sql, cli]
related_skills: [hermes-agent, native-mcp]
---

# Narwhal — TUI Database Client with MCP

Narwhal is a terminal database client that supports 5 databases and exposes them as an MCP server for AI agents.

## Prerequisites

- Rust (for cargo install)
- Database drivers for your target databases

## Installation

```bash
cargo install narwhal
```

## Quick Start

```bash
# Connect to PostgreSQL
narwhal postgresql://user:***@localhost:5432/mydb

# Connect to SQLite
narwhal sqlite://./data.db

# Connect to DuckDB
narwhal duckdb://./analytics.duckdb

# Run as MCP server
narwhal mcp --port 3090
```

## MCP Server Mode

Expose database connections to AI agents:

```bash
# Start MCP server on port 3090
narwhal mcp --port 3090

# Agent config:
# {
#   "mcpServers": {
#     "narwhal": {
#       "command": "narwhal",
#       "args": ["mcp", "--port", "3090"]
#     }
#   }
# }
```

## Vim Keybindings

- `i` — insert mode (edit SQL)
- `Esc` — normal mode
- `:w` — execute query
- `Ctrl-n` / `Ctrl-p` — navigate results
- `:help` — show all commands

## Lua Plugins

```lua
-- ~/.config/narwhal/plugins/format.lua
local M = {}
function M.format_sql(query)
  return query:gsub("%s+", " "):gsub("^%s+", ""):gsub("%s+$", "")
end
return M
```

## Pitfalls

- MCP server mode keeps connections open — configure connection pooling for production
- Lua plugin sandboxing is limited — don't load untrusted plugins
- Vim keybindings may conflict with terminal multiplexer shortcuts

## Verification

```bash
# Verify installation
narwhal --version

# Test connection
narwhal sqlite://:memory: --eval "SELECT 1"
```
