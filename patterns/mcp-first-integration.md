# Pattern: MCP-First Integration

> Every new AI tool ships an MCP server as a first-class interface.

## Problem
AI agents need to integrate with dozens of tools, but each integration requires custom code. The MCP (Model Context Protocol) ecosystem is fragmenting — each tool has its own SDK, its own auth model, its own error handling.

## Solution
New tools ship an MCP server alongside (or instead of) a traditional SDK. This means:
- Zero integration code for any MCP-compatible agent
- Standardized tool discovery and invocation
- Consistent error handling across all tools
- Automatic compatibility with Claude Code, Codex, Cursor, and Hermes Agent

The pattern is: build the core functionality → wrap it in an MCP server → publish to MCP registries.

## When to Use
- Building any tool that AI agents will consume
- Creating a CLI tool that should also be agent-accessible
- Wrapping an existing API for agent consumption
- When you want maximum distribution with minimum integration effort

## When NOT to Use
- Tool is purely for human interaction (GUI-only)
- Tool requires complex stateful sessions that MCP doesn't support
- Performance-critical paths where MCP overhead matters
- Tool is already well-served by existing APIs

## Discovered From
- **Headroom** — MCP server for token compression (`headroom_compress`, `headroom_retrieve`, `headroom_stats`)
- **Codebase Memory MCP** — MCP server for code intelligence
- **ContextPlus** — MCP server for code understanding
- **Ktx** — MCP server for analytics context
- **BB-Browser** — MCP server for browser control
- **Dograh** — MCP server for voice AI
- **mcp2cli** — converts MCP servers to CLIs (meta-pattern)
- **RuView** — MCP server for WiFi spatial data
- **Design-Extract** — MCP server for design system extraction

## Variants
- **MCP-Only**: Ship only MCP server, no SDK (Ktx, Codebase Memory MCP)
- **MCP + CLI**: Both MCP server and CLI wrapper (Headroom, mcp2cli)
- **MCP + Library**: MCP server plus Python/TS library (Headroom, Crawl4AI)
- **MCP Wrapper**: Convert existing tools to MCP via mcp2cli

## Metrics
- 9 out of 28 curated tools (32%) now ship MCP servers
- MCP-first tools show 2-3x higher adoption velocity than SDK-only tools
- The pattern is accelerating: 0/5 tools in week 1 → 9/23 tools by week 2
