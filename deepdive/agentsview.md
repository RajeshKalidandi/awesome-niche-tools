# Deep Dive: kenn-io/agentsview

> Local-first session intelligence and analytics for coding agents — browse, search, and track costs across Claude Code, Codex, and 20+ other agents.

- **Stars:** 1623 (↑~15/day) | **Language:** Go | **License:** MIT
- **Last commit:** 2026-06-11
- **Source credibility weight:** 1.00 (GitHub Trending)
- **Relevance score:** 78/100 (after multipliers)
- **Deep Dive Date:** 2026-06-12
- **Analyst:** vibe

## What It Does

AgentsView is a local-first tool that discovers, indexes, and analyzes sessions from AI coding agents on your machine. It supports Claude Code, Codex CLI, Forge, and 20+ other agents. It provides a web UI dashboard for browsing sessions, searching conversations, and tracking API costs — all stored in a local SQLite database with no accounts or cloud dependencies.

Key capabilities:
- **Session discovery** — automatically finds sessions from all supported agents
- **Cost tracking** — tracks API costs per session, per agent, per day
- **Full-text search** — search across all agent sessions
- **Graph visualization** — see relationships between sessions
- **Docker support** — run in containers for team deployments

## Why Now

The multi-agent development workflow is becoming the norm. Developers use Claude Code for one task, Codex for another, and Forge for yet another. But there's no unified way to:
- Compare costs between agents
- Search old sessions across tools
- Audit what agents did
- Track token consumption patterns

AgentsView fills this gap with a single binary that indexes everything locally. The timing is perfect — agent usage is exploding but observability tools haven't caught up.

The "100x faster replacement for ccusage" positioning is smart — ccusage is a known tool for tracking Claude Code costs, and AgentsView extends that to all agents.

## Why It Matters

Without AgentsView, developers have no visibility into their agent usage across tools. They can't:
- Compare costs between Claude Code and Codex
- Search old sessions to find where a particular change was made
- Audit what agents did for compliance or debugging
- Track token consumption patterns to optimize usage

This tool provides the missing observability layer for the multi-agent development workflow. As AI coding agents become more capable and expensive, cost tracking and session management become critical.

## Who Should Care

- **Developers using 2+ AI coding agents daily** — the core use case
- **Teams tracking AI coding costs** — budget management across tools
- **Engineering managers** — auditing agent usage and productivity
- **DevOps teams** — deploying agent observability at scale
- **Anyone who wants to search/browse their agent session history**

## Execution Pattern

### Quick start
```bash
# Install
curl -fsSL https://agentsview.io/install.sh | bash

# Start web UI
agentsview serve

# Daily cost summary
agentsview usage daily
```

### Team deployment (Docker)
```bash
docker run --rm -p 127.0.0.1:8080:8080 \
  -v agentsview-data:/data \
  -v "$HOME/.claude/projects:/agents/claude:ro" \
  -v "$HOME/.forge:/agents/forge:ro" \
  ghcr.io/kenn-io/agentsview:latest
```

### Remote access
```bash
# SSH tunnel
ssh -L 18080:127.0.0.1:8080 user@host

# Start with public URL
agentsview serve --public-url http://127.0.0.1:18080
```

## Skill Potential

Yes — SKILL.md covers:
- Installation (multiple methods)
- Session indexing and discovery
- Cost tracking and reporting
- Web UI usage
- Docker deployment
- Remote access configuration
- Integration with agent workflows

## Composable Stack Potential

**AgentsView + SkillSpector** = Security + Analytics governance layer. AgentsView tracks what agents are doing and how much it costs, SkillSpector verifies that the skills they use are safe. Together they provide complete visibility into agent operations.

**AgentsView + Cost optimization tools** = Informed cost reduction. AgentsView provides the data (which sessions are expensive, which agents are wasteful), optimization tools (like TokenTamer) provide the action (compress context, switch models).

## Limitations & Trade-offs

- **Local-first means no cloud sync** — sessions stay on your machine, which is good for privacy but bad for team collaboration
- **SQLite backend** — works well for individual use but may not scale to enterprise-level agent usage
- **91 open issues** — indicates active development but also potential stability concerns
- **Limited to session data** — tracks what agents did, not why they did it (no reasoning/decision tracking)
- **New project** — created 2026-02-19, so long-term maintenance is uncertain

## Discovered

2026-06-12 via GitHub Trending (credibility: 1.00)
