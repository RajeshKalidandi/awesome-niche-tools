---
name: aislop
description: "Static analysis linter for AI-generated code patterns — 40+ rules, 7 languages, deterministic, no LLM."
tags: [code-quality, linting, ai-code, static-analysis, ci-cd]
related_skills: [hermes-agent, requesting-code-review]
---

# AISlop — AI Code Slop Detector

AISlop catches the telltale patterns that AI coding agents leave in your code. 40+ rules across 7 languages. Pure pattern matching — no LLM calls.

## Prerequisites

- Node.js 18+
- npm

## Installation

```bash
npm install -g aislop
```

## Quick Start

```bash
# Run on a project
aislop ./src/

# Run with specific languages
aislop --lang typescript,python ./src/

# CI integration (exit code 1 on violations)
aislop --format json ./src/ | jq '.violations'

# Auto-fix fixable issues
aislop --fix ./src/
```

## Rule Categories

- **Over-commenting** — excessive JSDoc/docstrings on simple functions
- **Redundant error handling** — try/catch blocks that just re-throw
- **Generic naming** — `data`, `result`, `temp`, `value` as variable names
- **Unnecessary abstractions** — wrapper functions that add no logic
- **Verbose patterns** — loops that could be array methods

## CI Integration

```yaml
# GitHub Actions
- name: Check AI slop
  run: npx aislop --format json ./src/ > slop-report.json
  continue-on-error: true

# Fail on high-severity violations
- name: Gate AI code quality
  run: aislop --min-severity high ./src/
```

## Pitfalls

- Some rules may flag legitimate patterns in certain contexts
- Auto-fix is conservative — review changes before committing
- Rules are deterministic — same input always produces same output

## Verification

```bash
# Verify installation
aislop --version

# Run on test file
echo "function getData() { let data = []; return data; }" > test.js
aislop test.js
```
