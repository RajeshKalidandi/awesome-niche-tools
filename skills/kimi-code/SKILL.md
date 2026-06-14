---
name: kimi-code
description: "Terminal AI coding agent with video input, subagents, MCP support, and ACP editor integration"
version: 1.0.0
author: Hermes Agent
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [ai-agent, coding, cli, multimodal, mcp]
    related_skills: [claude-code, opencode]
---

# Kimi Code — Terminal AI Coding Agent

A terminal-based AI coding agent from Moonshot AI with video input support, sub-agent orchestration, MCP tool integration, and ACP editor connections. Ships as a single binary.

## Prerequisites

- Node.js 18+ or standalone binary
- LLM API key (configurable provider)

## Installation

```bash
# Install via npm
npm install -g @moonshotai/kimi-code

# Or download binary from GitHub releases
# https://github.com/MoonshotAI/kimi-code/releases
```

## Usage

### Basic Coding

```bash
# Start interactive session
kimi-code

# Single-shot coding task
kimi-code "add error handling to the auth module"

# Use video input for visual context
kimi-code --video screenshot.png "fix this UI bug"
```

### MCP Integration

```bash
# Configure MCP servers
kimi-code --mcp-server filesystem --mcp-server github

# Use MCP tools in coding sessions
kimi-code "use the github tool to create a PR for these changes"
```

### Sub-agent Orchestration

```bash
# Spawn sub-agents for parallel tasks
kimi-code "refactor the database layer and write tests in parallel"
```

### ACP Editor Connection

```bash
# Connect to VS Code via ACP
kimi-code --acp-editor vscode

# Connect to Cursor via ACP
kimi-code --acp-editor cursor
```

## Common Pitfalls

- **Video input size**: Large screenshots may exceed context limits. Resize before passing.
- **MCP server availability**: Ensure MCP servers are running before starting kimi-code.
- **Sub-agent costs**: Each sub-agent consumes separate LLM tokens.

## Verification

```bash
# Verify installation
kimi-code --version

# Test basic functionality
echo "print('hello')" > test.py
kimi-code "add a docstring to this function" test.py
cat test.py
```
