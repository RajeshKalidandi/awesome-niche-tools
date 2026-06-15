---
name: cli-printing-press
description: "Generate token-efficient CLIs for AI agents by reading API docs and studying community patterns. Prints Go binaries + Claude Code skills + MCP servers."
version: 1.0.0
author: Hermes Agent
license: MIT
platforms: [linux, macos]
metadata:
  hermes:
    tags: [cli, code-generation, ai-agent, api, mcp, claude-code]
    related_skills: [agent-reach, claude-code]
---

# CLI Printing Press — Auto-Generate CLIs for AI Agents

Reads official API docs, studies community CLIs, and generates token-efficient Go CLIs + Claude Code skills + MCP servers for any API or website.

## Prerequisites

- Go 1.26.4 or newer
- Node/npm (for npx)
- Claude Code (primary interface)

## Installation

```bash
curl -fsSL https://raw.githubusercontent.com/mvanhorn/cli-printing-press/main/scripts/install.sh | bash
```

Or install components separately:

```bash
# CLI only
curl -fsSL https://raw.githubusercontent.com/mvanhorn/cli-printing-press/main/scripts/install.sh | bash -s -- --cli-only

# Skills only
curl -fsSL https://raw.githubusercontent.com/mvanhorn/cli-printing-press/main/scripts/install.sh | bash -s -- --skills-only
```

## Usage

### Generate a CLI from API Docs

```bash
cli-printing-press generate --api-docs ./openapi.yaml --name my-cli
```

### Browse the Catalog

```bash
printing-press list
printing-press search <keyword>
printing-press install <cli-name>
```

### Use in Claude Code

```bash
/printing-press linear-pp-cli "Every blocked issue whose blocker has been stuck for a week"
```

## Pre-built CLIs

- **ESPN** — live scores, stats, injury news (sniffed, no official API)
- **flight-goat** — Kayak + Google Flights nonstop search
- **linear-pp-cli** — 50ms queries against local SQLite mirror

## Common Pitfalls

- Requires Go 1.26.4+ — older versions won't work
- Primary interface is Claude Code skills — other harnesses may not work as well
- Generated CLI quality depends on API doc quality
- Restart Claude Code after installation to load refreshed skills

## Verification

```bash
cli-printing-press --version
printing-press list
```

## Source

- GitHub: https://github.com/mvanhorn/cli-printing-press
- Stars: 3,412+ (growing fast)
- License: MIT
- Catalog: https://printingpress.dev
