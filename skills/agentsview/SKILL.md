---
name: agentsview
description: "Local-first session intelligence and analytics for coding agents — browse, search, and track costs across Claude Code, Codex, and 20+ other agents."
version: 1.0.0
author: Hermes Agent
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [ai-agents, analytics, cost-tracking, session-management, observability]
    related_skills: [claude-code, codex]
---

# AgentsView — Coding Agent Session Intelligence

Local-first session intelligence and analytics for coding agents. Browse, search, and track costs across Claude Code, Codex, and 20+ other agents.

## Prerequisites

- Go 1.21+ (for building from source)
- Or: Homebrew (macOS), Docker, or direct install script
- Supported agents: Claude Code, Codex CLI, Forge, and 20+ others

## Installation

### macOS / Linux (recommended)
```bash
curl -fsSL https://agentsview.io/install.sh | bash
```

### Homebrew (macOS)
```bash
brew install --cask agentsview
```

### Docker
```bash
docker run --rm -p 127.0.0.1:8080:8080 \
  -v agentsview-data:/data \
  -v "$HOME/.claude/projects:/agents/claude:ro" \
  ghcr.io/kenn-io/agentsview:latest
```

### Build from source
```bash
git clone https://github.com/kenn-io/agentsview.git
cd agentsview
go build -o agentsview ./cmd/agentsview
```

## Usage

### Start the web UI
```bash
agentsview serve
# Opens at http://127.0.0.1:8080
```

### Daily cost summary
```bash
agentsview usage daily
```

### Search sessions
```bash
agentsview search "docker networking"
```

### Remote access (SSH tunnel)
```bash
# Terminal 1: SSH tunnel
ssh -L 18080:127.0.0.1:8080 user@host

# Terminal 2: Start with public URL
agentsview serve --public-url http://127.0.0.1:18080
```

## What It Tracks

- Session history across all supported agents
- API costs per session, per agent, per day
- File changes and tool usage
- Token consumption patterns
- Cross-agent session correlations

## Common Pitfalls

- First run syncs all existing sessions — may take time for large histories
- Remote access requires `--public-url` flag for correct Host header validation
- Docker volume mounts must match your agent's session directory structure

## Verification

```bash
# Verify installation
agentsview --version

# Check session count
agentsview sessions list | wc -l

# Verify web UI
curl -s http://127.0.0.1:8080/api/v1/health
```
