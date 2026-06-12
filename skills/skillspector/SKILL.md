---
name: skillspector
description: "Security scanner for AI agent skills — detects vulnerabilities, malicious patterns, and security risks before installing agent skills."
version: 1.0.0
author: Hermes Agent
license: MIT
platforms: [linux, macos]
metadata:
  hermes:
    tags: [security, ai-agents, skills, scanning, vulnerabilities]
    related_skills: [agent-skills, claude-code]
---

# SkillSpector — AI Agent Skill Security Scanner

Security scanner for AI agent skills. Detects vulnerabilities, malicious patterns, and security risks before installing agent skills.

## Prerequisites

- Python 3.12+
- Git (for scanning remote repos)
- Optional: LLM API key for semantic analysis stage

## Installation

```bash
git clone https://github.com/NVIDIA/SkillSpector.git
cd SkillSpector
uv venv .venv && source .venv/bin/activate
make install
```

## Usage

### Scan a local skill directory
```bash
skillspector scan ./my-skill/
```

### Scan a SKILL.md file
```bash
skillspector scan ./SKILL.md
```

### Scan a Git repository
```bash
skillspector scan https://github.com/user/my-skill
```

### Output formats
```bash
# Terminal (default)
skillspector scan ./my-skill/

# JSON for CI/CD
skillspector scan ./my-skill/ --format json --output report.json

# Markdown for documentation
skillspector scan ./my-skill/ --format markdown --output report.md

# SARIF for GitHub Security tab
skillspector scan ./my-skill/ --format sarif --output report.sarif
```

## What It Checks

64 vulnerability patterns across 16 categories:
- Prompt injection
- Data exfiltration
- Privilege escalation
- Supply chain attacks
- MCP tool poisoning
- Memory poisoning
- And 10 more categories

## Common Pitfalls

- LLM semantic analysis requires an API key and adds cost
- Some false positives on legitimate automation patterns
- SARIF output requires specific field formatting for GitHub

## Verification

```bash
# Verify installation
skillspector --version

# Test with a known-safe skill
skillspector scan https://github.com/addyosmani/agent-skills

# Test with a suspicious skill
skillspector scan ./suspicious-skill/ --format json
```
