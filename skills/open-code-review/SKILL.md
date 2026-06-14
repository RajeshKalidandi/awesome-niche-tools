---
name: open-code-review
description: "AI-powered code review CLI — deterministic pipelines + LLM agent, battle-tested at Alibaba scale"
version: 1.0.0
author: Hermes Agent
license: Apache-2.0
platforms: [linux, macos]
metadata:
  hermes:
    tags: [code-review, ai, cli, security, devops]
    related_skills: [github-code-review]
---

# Open Code Review — AI Code Review CLI

Production-proven AI code review tool from Alibaba. Reads Git diffs, sends changed files to a configurable LLM, and generates structured review comments with line-level precision.

## Prerequisites

- Go 1.21+ (for building from source)
- Git
- LLM API key (OpenAI, Anthropic, or compatible endpoint)

## Installation

```bash
# Clone and build
git clone https://github.com/alibaba/open-code-review.git
cd open-code-review
go build -o ocr ./cmd/ocr

# Or download pre-built binary from releases
```

## Usage

### Basic Review

```bash
# Review current branch against main
ocr review --base main --head HEAD

# Review specific commit
ocr review --commit abc123

# Review with custom LLM endpoint
ocr review --base main --endpoint https://your-llm-endpoint/v1
```

### CI/CD Integration

```bash
# GitHub Actions example
- name: AI Code Review
  run: |
    ocr review --base ${{ github.event.pull_request.base.sha }} \
               --head ${{ github.event.pull_request.head.sha }} \
               --format github
```

### Configuration

```yaml
# .ocr.yaml
llm:
  provider: openai
  model: gpt-4
  endpoint: https://api.openai.com/v1
rules:
  - npe
  - thread-safety
  - xss
  - sql-injection
  - custom-rules.yaml
```

## Common Pitfalls

- **Rate limits**: Large diffs may hit LLM token limits. Use `--max-files` to batch.
- **Cost**: Each review call consumes LLM tokens. Monitor usage for large repos.
- **False positives**: Deterministic rules are conservative; LLM reasoning may flag non-issues.

## Verification

```bash
# Run against a known-good commit
ocr review --commit HEAD --verbose

# Check output format
ocr review --base HEAD~1 --head HEAD --format json | jq .
```
