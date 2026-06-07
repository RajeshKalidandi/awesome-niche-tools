---
name: ai-rules-sync
description: "Zero-dependency CLI (agentsync) to keep one source of truth for AI coding-agent rules across AGENTS.md, CLAUDE.md, .cursorrules, Copilot, Windsurf, Cline, Aider, and Gemini. Scaffold, convert, and sync."
version: 1.0.0
author: Hermes Agent
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [cli, ai-agents, codex, claude-code, cursor, copilot, dev-tools, zero-deps]
    related_skills: [opencode, codex, claude-code, hermes-agent-skill-authoring]
---

# ai-rules-sync (agentsync) — Single Source of Truth for AI Coding Rules

A zero-dependency Node CLI that fans your AI coding-agent rules out to every IDE and CLI agent that has its own conventions. Write once in `AGENTS.md`, sync everywhere.

## Prerequisites

- Node.js 18+ (or `npx` via npm 9+)
- Optional: a pre-commit hook runner (Husky, pre-commit, simple-git-hooks)

## Installation

```bash
# Use directly via npx (no install)
npx @panishandsome/agentsync init
npx @panishandsome/agentsync sync

# Or install globally
npm i -g @panishandsome/agentsync
agentsync --version
```

## Usage Examples

### Scaffold a fresh `AGENTS.md`

```bash
npx @panishandsome/agentsync init
# Interactive: asks for project name, primary agent, conventions
# Writes a canonical AGENTS.md
```

### Sync from `AGENTS.md` to every supported location

```bash
npx @panishandsome/agentsync sync
# Writes/updates:
#   .claude/CLAUDE.md        (Claude Code)
#   .cursorrules             (Cursor)
#   .github/copilot-instructions.md   (Copilot)
#   .windsurfrules           (Windsurf)
#   .clinerules              (Cline)
#   .aider.conf.yml          (Aider)
#   GEMINI.md                (Gemini)
```

### Convert a single file in one direction

```bash
npx @panishandsome/agentsync convert .cursorrules --to AGENTS.md
npx @panishandsome/agentsync convert AGENTS.md --to .windsurfrules
```

### Check drift between sources

```bash
npx @panishandsome/agentsync diff
# Reports any rules file that has diverged from AGENTS.md
```

## Wire into a Pre-Commit Hook

```bash
# .husky/pre-commit
npx @panishandsome/agentsync diff || npx @panishandsome/agentsync sync
git add AGENTS.md CLAUDE.md .cursorrules .github/copilot-instructions.md
```

## Common Pitfalls

- **No `AGENTS.md` yet**: `sync` will fail until `init` is run or you point it at an existing canonical file with `--source`.
- **Format-specific directives**: Some agents (Aider, Windsurf) have directive syntax that doesn’t translate 1:1. agentsync uses sensible defaults; review generated files for your stack.
- **Drift after manual edits**: If a teammate edits `.cursorrules` directly, `sync` will overwrite them. Run `diff` first.
- **CI drift**: Wire `agentsync diff` into CI to fail PRs that introduce drift.

## Hermes Integration

The Vibe Coder shift model benefits from a canonical rules file across all agents a shift worker spawns:

```bash
# At shift start
npx @panishandsome/agentsync sync   # ensure all agent contexts match

# In the agent's bootstrap prompt
cat AGENTS.md                          # so the agent reads the canonical rules
```

For multi-agent shifts, keep `AGENTS.md` as the single source of truth and let `agentsync` fan out to the agent-specific files each tool reads.

## Verification

```bash
# After init + sync, every supported tool should have its file:
test -f AGENTS.md && test -f .cursorrules && test -f .github/copilot-instructions.md
npx @panishandsome/agentsync diff     # should exit 0 with no output
```

## Related Skills

- **opencode** — primary agent harness; reads `.opencode/rules` or equivalent
- **codex** — Codex CLI config can be synced from `AGENTS.md`
- **claude-code** — Claude Code reads `CLAUDE.md` / `.claude/CLAUDE.md`
- **hermes-agent-skill-authoring** — for authoring skills that pair with `AGENTS.md` standards
