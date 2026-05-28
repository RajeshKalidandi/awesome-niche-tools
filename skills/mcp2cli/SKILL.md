---
name: mcp2cli
description: "Turn any MCP, OpenAPI, or GraphQL server into a CLI at runtime with zero codegen."
version: 1.0.0
author: Hermes Agent
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [mcp, cli, openapi, graphql, codegen, automation]
    related_skills: [headroom, codebase-memory-mcp]
---

# mcp2cli — MCP to CLI Converter

Dynamically convert MCP servers, OpenAPI specs, and GraphQL schemas into fully functional CLI tools at runtime. No code generation, no build steps.

## Prerequisites

- Python 3.9+
- pip

## Installation

```bash
pip install mcp2cli
```

## Usage

### Convert MCP Server to CLI

```bash
# Point at any MCP server (SSE or stdio)
mcp2cli --server https://my-mcp-server.com/sse --output ./my-tool

# Use the generated CLI
./my-tool --help
./my-tool subcommand --arg value
```

### Convert OpenAPI Spec

```bash
# From URL
mcp2cli --openapi https://api.example.com/openapi.json --output ./api-cli

# From file
mcp2cli --openapi ./openapi.yaml --output ./api-cli

# With authentication
mcp2cli --openapi https://api.example.com/openapi.json \
  --auth-header "Authorization: Bearer sk-..." \
  --output ./api-cli
```

### Convert GraphQL Schema

```bash
# From introspection endpoint
mcp2cli --graphql https://api.example.com/graphql --output ./gql-cli

# With custom headers
mcp2cli --graphql https://api.example.com/graphql \
  --header "X-API-Key: your-key" \
  --output ./gql-cli
```

## Integration with Hermes Agent

### Expose MCP Servers as Shell Commands

```bash
# Convert Hermes MCP servers to CLI for scripting
mcp2cli --server stdio:hermes-mcp-server --output ./hermes-tools

# Now use in shell scripts
./hermes-tools search "query" --limit 10
./hermes-tools store --key "value"
```

### Pipeline Integration

```bash
# Convert API to CLI, then pipe to other tools
mcp2cli --openapi ./petstore.json --output ./petstore
./petstore list-pets --limit 5 | jq '.[].name'
```

## Configuration

### Output Options

```bash
# Custom output directory
mcp2cli --server ... --output-dir ./bin

# Verbose logging
mcp2cli --server ... --verbose

# Skip help generation
mcp2cli --server ... --no-help
```

### Authentication

```bash
# API key
mcp2cli --openapi ... --api-key "sk-..."

# Bearer token
mcp2cli --openapi ... --auth-header "Authorization: Bearer token"

# Basic auth
mcp2cli --openapi ... --auth user:password
```

## Common Pitfalls

1. **Complex APIs may need tuning**: Very large OpenAPI specs (1000+ endpoints) may generate unwieldy CLIs. Use `--filter` to limit endpoints.
2. **Authentication timing**: Auth tokens expire. Use environment variables: `mcp2cli --openapi ... --api-key "$API_KEY"`.
3. **Binary responses**: CLI handles JSON/text well. Binary responses (images, files) need `--output-file` flag.

## Verification

```bash
# Test installation
mcp2cli --version

# Test with a public API
mcp2cli --openapi https://petstore3.swagger.io/api/v3/openapi.json --output ./petstore
./petstore --help
./petstore list-pets --limit 3
```

## Sources

- **GitHub:** [knowsuchagency/mcp2cli](https://github.com/knowsuchagency/mcp2cli)
- **Stars:** 2,183 (↑~25/day)
- **License:** MIT
- **Discovered:** 2026-05-29 via GitHub search
