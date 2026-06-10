---
name: last30days-skill
description: "AI agent skill for cross-platform topic research and summarization across Reddit, X, YouTube, HN, Polymarket, and the web"
version: 1.0.0
author: Hermes Agent
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [ai-agent, research, summarization, cross-platform, real-time]
    related_skills: [web-research, youtube-content, polymarket]
---

# last30days-skill

An AI agent skill that researches any topic across multiple platforms and synthesizes a grounded summary with citations.

## Prerequisites

- Python 3.8+
- pip
- API keys for desired platforms (optional but recommended for full functionality)

## Installation

```bash
pip install last30days-skill
```

## Usage

### Basic Research

```python
from last30days_skill import Last30DaysSkill

skill = Last30DaysSkill()
result = await skill.research("latest developments in AI agents")

print(result.summary)
print(result.sources)
```

### With Platform Filters

```python
# Research only on specific platforms
result = await skill.research(
    "quantum computing breakthroughs",
    platforms=["reddit", "twitter", "arxiv"]
)
```

### Custom Time Range

```python
# Research from the last 7 days instead of 30
result = await skill.research(
    "AI regulation news",
    days=7
)
```

## Common Pitfalls

1. **Rate limiting**: Some platforms have strict rate limits. Implement exponential backoff.
2. **API costs**: Some data sources may incur costs. Monitor usage.
3. **Data quality**: Cross-reference sources for accuracy. Not all sources are equally reliable.
4. **Freshness vs depth**: Recent data may lack context. Balance recency with comprehensiveness.

## Verification

```bash
# Test installation
python -c "from last30days_skill import Last30DaysSkill; print('OK')"

# Run a simple test
python -c "
import asyncio
from last30days_skill import Last30DaysSkill

async def test():
    skill = Last30DaysSkill()
    result = await skill.research('test topic', days=1)
    print(f'Sources found: {len(result.sources)}')
    print(f'Summary length: {len(result.summary)}')

asyncio.run(test())
"
```
