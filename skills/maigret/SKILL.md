---
name: maigret
description: "OSINT username reconnaissance — collect dossiers on people from 3000+ sites using only a username"
version: 1.0.0
author: Hermes Agent
license: MIT
platforms: [linux, macos]
metadata:
  hermes:
    tags: [osint, security, reconnaissance, cli, username]
    related_skills: [web-research]
---

# Maigret — OSINT Username Reconnaissance

Collect a comprehensive dossier on a person using only their username. Checks 3000+ sites, gathers public profile data, and generates AI-powered analysis.

## Prerequisites

- Python 3.10+
- pip install maigret
- Optional: LLM API key for AI profiling feature

## Usage

### Basic Investigation
```bash
# Single username check
maigret username <target_username>

# With AI analysis enabled
maigret username <target_username> --ai-provider openai

# Generate HTML report
maigret username <target_username> --html
```

### Batch Processing
```bash
# From a file (one username per line)
maigret --input usernames.txt --output results.json

# CSV output for spreadsheet analysis
maigret username <target> --csv
```

### Advanced Options
```bash
# Custom timeout for slow networks
maigret username <target> --timeout 30

# Use proxies to avoid rate limiting
maigret username <target> --proxy socks5://127.0.0.1:9050

# Update site database
maigret --update
```

## Common Pitfalls

- Rate limiting: Checking 3000+ sites can trigger blocks. Use proxies or reduce concurrency.
- Site database staleness: Run `maigret --update` regularly to get最新的 site patterns.
- False positives: Some sites return 200 for non-existent users. Verify critical findings manually.
- Legal considerations: OSINT collection may have legal implications depending on jurisdiction.

## Verification

```bash
# Verify installation
maigret --version

# Test with a known username
maigret username test --json | head -20
```
