---
name: ponytail
description: "AI agent skill that enforces minimal code output — 80-94% less code, prevents over-engineering"
version: 1.0.0
author: Hermes Agent
license: MIT
platforms: [linux, macos]
metadata:
  hermes:
    tags: [ai-agent, code-quality, minimal-code, skill]
    related_skills: [claude-code, opencode]
---

# Ponytail — Minimal Code Agent Skill

An AI agent skill that enforces "lazy senior dev" thinking — your agent writes 80-94% less code by preferring zero-code solutions and minimal implementations.

## Prerequisites

- Any AI coding agent (Claude Code, Cursor, Codex, Windsurf, etc.)
- Node.js 18+ (for installation)

## Installation

```bash
# Install via npm
npm install -g ponytail

# Or clone and use directly
git clone https://github.com/DietrichGebert/ponytail.git
cd ponytail
```

## Usage

### As an Agent Skill

Add to your agent's skill configuration. Ponytail modifies the system prompt to enforce minimal-code thinking.

### Key Principles

1. **Think before writing** — Is there a zero-code solution?
2. **Prefer existing tools** — Don't reinvent what's available
3. **Minimal implementation** — Only write what's strictly necessary
4. **Delete before adding** — Can you solve this by removing code?

### Example

Before Ponytail:
```python
# Agent generates a 200-line custom parser
def parse_data(input):
    # ... 200 lines of custom parsing logic
```

After Ponytail:
```python
# Agent suggests using existing library
import json
data = json.loads(input)  # 1 line instead of 200
```

## Common Pitfalls

- **Over-aggressive minimization**: Some problems genuinely need complex solutions. Ponytail works best for routine tasks, not algorithm design.
- **Missing edge cases**: Minimal code sometimes skips validation. Review agent output for correctness.

## Verification

```bash
# Test the skill loads correctly
ponytail --version

# Compare agent output with and without the skill
# Measure lines of code before/after
```
