---
name: agent-skills
description: "Production-grade engineering skills for AI coding agents — slash commands mapping to the full dev lifecycle"
version: 1.0.0
author: Hermes Agent
license: MIT
platforms: [linux, macos]
metadata:
  hermes:
    tags: [ai-agents, coding, engineering, skills, claude-code]
    related_skills: [hermes-agent]
---

# Agent Skills — Structured Engineering for AI Coding Agents

Production-grade engineering skills by Addy Osmani that encode senior engineering practices into reusable skill files for AI coding agents. Works across Claude Code, Cursor, Codex CLI, and more.

## Prerequisites

- An AI coding agent (Claude Code, Cursor, Codex CLI, etc.)
- Agent must support skill/plugin loading

## Usage

### Installation (Claude Code)
```bash
# Via marketplace
/plugin marketplace add addyosmani/agent-skills
/plugin install agent-skills@addy-agent-skills

# Or clone locally
git clone https://github.com/addyosmani/agent-skills.git
claude --plugin-dir /path/to/agent-skills
```

### Slash Commands
| Command | Purpose |
|---------|---------|
| `/spec` | Define what to build |
| `/plan` | Plan implementation tasks |
| `/build` | Build incrementally |
| `/build auto` | Autonomous full build |
| `/test` | Run and verify tests |
| `/review` | Code review |
| `/code-simplify` | Simplify code |
| `/ship` | Deploy to production |

### Autonomous Development
```bash
# In Claude Code, after defining a spec:
/build auto

# This generates a plan and implements all tasks autonomously
# Each task is test-driven and committed individually
# Pauses on failures or risky steps
```

## Common Pitfalls

- `/build auto` requires a well-defined spec — vague specs lead to autonomous runs that deviate.
- Skills are prompts, not code — the agent can choose to ignore them in ambiguous contexts.
- Team customization requires editing skill files and maintaining a fork.

## Verification

```bash
# Verify skills are loaded (in Claude Code)
/plugin list

# Test with a simple task
/spec build a hello world CLI tool
/plan
/build
/test
```
