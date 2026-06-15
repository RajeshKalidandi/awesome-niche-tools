---
name: agent-reach
description: "Give your AI agent one-click internet access — Twitter, Reddit, YouTube, GitHub, Bilibili, and more. Zero API fees."
version: 1.0.0
author: Hermes Agent
license: MIT
platforms: [linux, macos]
metadata:
  hermes:
    tags: [agent, internet, web-access, research, twitter, reddit, youtube]
    related_skills: [crawl4ai, jina-reader]
---

# Agent-Reach — Internet Access for AI Agents

One-click internet access layer for AI agents. Connects to Twitter/X, Reddit, YouTube, GitHub, Bilibili, XiaoHongShu, LinkedIn, V2EX, and web search — all without API fees.

## Prerequisites

- Python 3.10+
- pip
- Optional: proxy server for server-side usage ($1/month)

## Installation

Agent-Reach is installed by telling your agent to fetch and run the install script:

```bash
# Copy this to your agent:
# Install Agent Reach: https://raw.githubusercontent.com/Panniantong/agent-reach/main/docs/install.md
```

Or manually:

```bash
pip install agent-reach
```

## Usage

### Health Check

```bash
agent-reach doctor
```

Shows what platforms work, what doesn't, and how to fix them.

### Platform Setup

Each platform has its own setup command. Agent-Reach handles authentication, proxying, and fallback routing automatically.

### In Agent Workflows

Once installed, your agent can:
- Read tweets and search Twitter/X
- Search Reddit and read threads
- Watch YouTube videos and get transcripts
- Browse GitHub repos, issues, and PRs
- Read Bilibili videos
- Search the web via Exa

## Common Pitfalls

- **Server-side usage** may need a proxy — local computers don't
- **Twitter/X** requires a cookie for search functionality
- **XiaoHongShu** requires either OpenCLI (desktop) or MCP (server) setup
- **Chinese documentation** is more complete than English — check both

## Verification

```bash
agent-reach doctor
# Should show green checkmarks for configured platforms
```

## Source

- GitHub: https://github.com/Panniantong/Agent-Reach
- Stars: 29,952+ (growing fast)
- License: MIT
