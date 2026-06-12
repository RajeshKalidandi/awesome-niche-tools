# Deep Dive: NVIDIA/SkillSpector

> Security scanner for AI agent skills — detects vulnerabilities, malicious patterns, and security risks before installing agent skills.

- **Stars:** 2619 (↑~33/day) | **Language:** Python | **License:** Apache-2.0
- **Last commit:** 2026-06-10
- **Source credibility weight:** 1.00 (GitHub Trending)
- **Relevance score:** 83/100 (after multipliers)
- **Deep Dive Date:** 2026-06-12
- **Analyst:** vibe

## What It Does

SkillSpector is a security scanner specifically designed for AI agent skills — the SKILL.md files and associated scripts that Claude Code, Codex CLI, Gemini CLI, and other AI coding agents use to extend their capabilities. It scans for 64 vulnerability patterns across 16 categories, providing a risk score from 0-100 with severity labels and recommendations.

The tool operates in two stages:
1. **Fast static analysis** — pattern matching against known vulnerability signatures
2. **Optional LLM semantic evaluation** — deeper analysis using a language model to detect subtle issues

## Why Now

The AI agent skills ecosystem is exploding. Projects like Agent Skills (54K stars), Superpowers (224K stars), and pm-skills (16K stars) are creating a marketplace of community-contributed skills. But there's no automated way to verify these skills are safe.

Research cited in the README shows:
- 26.1% of agent skills contain vulnerabilities
- 5.2% show likely malicious intent

As teams deploy AI coding agents in production, the security implications become critical. A malicious or vulnerable skill could exfiltrate code, inject prompts, or escalate privileges. SkillSpector fills this gap with a comprehensive, NVIDIA-backed solution.

## Why It Matters

Without SkillSpector, the agent skills ecosystem has a trust problem. Users install skills blind, trusting that a community-contributed SKILL.md won't harm their systems. This is analogous to the early npm/PyPI supply chain attack problem — but worse, because agent skills execute with implicit trust and access to the entire codebase.

SkillSpector makes the ecosystem safer by providing:
- Automated, reproducible security auditing
- CI/CD integration via SARIF output
- Risk scoring that quantifies danger levels
- Coverage of AI-specific attack vectors (prompt injection, MCP poisoning)

## Who Should Care

- **Platform engineers** managing agent skill repositories
- **Security teams** auditing AI agent supply chains
- **DevOps engineers** integrating agent skills into CI/CD
- **Individual developers** who install community-contributed skills
- **Enterprise teams** deploying AI coding agents at scale

## Execution Pattern

### Basic scanning workflow
```bash
# Scan before installing any new skill
skillspector scan https://github.com/user/new-skill

# CI/CD integration
skillspector scan ./skills/ --format sarif --output security.sarif

# Batch scan all installed skills
for skill in ./skills/*/; do
  skillspector scan "$skill" --format json --output "reports/$(basename $skill).json"
done
```

### Integration with agent workflows
```bash
# Pre-install hook for skill installation
skillspector scan ./downloaded-skill/ --format json | jq '.risk_score'
# Only install if risk_score < 30

# Post-install verification
skillspector scan ~/.claude/skills/ --format markdown --output security-audit.md
```

## Skill Potential

Yes — SKILL.md covers:
- Installation and setup
- Scanning workflows (local, remote, batch)
- CI/CD integration (SARIF, JSON)
- Custom rule authoring
- Risk score interpretation
- Integration with agent skill installation workflows

## Composable Stack Potential

**SkillSpector + agentsview** = Security + Analytics governance layer for AI coding agents. SkillSpector scans skills for vulnerabilities, agentsview tracks costs and usage across agents. Together they provide complete visibility into what agents are doing and whether it's safe.

**SkillSpector + CI/CD** = Automated security gates for skill installation. Every new skill gets scanned before being added to the repository, with SARIF output feeding into GitHub Security tab.

## Limitations & Trade-offs

- **LLM semantic analysis requires API key and adds cost** — the two-stage approach is powerful but the second stage isn't free
- **False positives on legitimate automation patterns** — some security patterns overlap with legitimate automation (e.g., file access for tool execution)
- **Coverage gaps** — 64 patterns is comprehensive but not exhaustive; novel attack vectors may slip through
- **No runtime monitoring** — scans skills at install time, not during execution
- **Alpha-stage ecosystem** — the agent skills ecosystem itself is new, so attack patterns are still evolving

## Discovered

2026-06-12 via GitHub Trending (credibility: 1.00)
