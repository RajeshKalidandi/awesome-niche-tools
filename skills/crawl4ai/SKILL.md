---
name: crawl4ai
description: "LLM-friendly web crawler — turn any website into clean markdown for AI agents, RAG pipelines, and fine-tuning."
version: 1.0.0
author: Hermes Agent
license: Apache-2.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [web-crawling, scraping, llm, rag, markdown, browser]
    related_skills: [headroom, web-research]
---

# Crawl4AI — LLM-Friendly Web Crawler

Open-source web crawler designed for LLM consumption. Extracts clean, structured markdown from any website — handling JavaScript rendering, anti-bot measures, and proxy rotation.

## Prerequisites

- Python 3.9+
- pip

## Installation

```bash
pip install crawl4ai
```

## Usage

### CLI

```bash
# Simple crawl — outputs markdown
crawl4ai https://example.com --output article.md

# Crawl with JavaScript rendering (for SPAs)
crawl4ai https://spa-site.com --js-render --output content.md

# Crawl multiple pages
crawl4ai https://blog.example.com --crawl-links --max-pages 10 --output ./blog/

# With proxy
crawl4ai https://target.com --proxy http://proxy:8080 --output data.md
```

### Python API

```python
import asyncio
from crawl4ai import AsyncWebCrawler

async def crawl():
    async with AsyncWebCrawler() as crawler:
        result = await crawler.arun(url="https://example.com")
        
        # Clean markdown output
        print(result.markdown)
        
        # Metadata
        print(result.title)
        print(result.links)

asyncio.run(crawl())
```

### Batch Crawling

```python
from crawl4ai import AsyncWebCrawler, CrawlerRunConfig

async def batch_crawl(urls):
    config = CrawlerRunConfig(
        js_render=True,
        proxy="http://proxy:8080",
        word_count_threshold=100
    )
    
    async with AsyncWebCrawler(config=config) as crawler:
        results = await crawler.arun_many(urls)
        return [r.markdown for r in results]
```

## Integration with Hermes Agent

### As Web Research Tool

```bash
# Crawl a page for agent context
crawl4ai https://docs.example.com/api --output /tmp/api-docs.md

# Use in agent workflow
# 1. Crawl documentation
# 2. Feed markdown to agent as context
# 3. Agent answers questions based on crawled content
```

### With Headroom (Token Compression)

```bash
# Crawl and compress for LLM consumption
crawl4ai https://long-article.com --output /tmp/raw.md
headroom compress /tmp/raw.md --ratio 0.3 --output /tmp/compressed.md
```

## Common Pitfalls

1. **JS rendering requires a browser**: Install with `pip install crawl4ai[full]` for Playwright support.
2. **Rate limiting**: Add `--delay 2` between requests to avoid getting blocked.
3. **Large pages**: Use `--word-count-threshold 100` to skip thin content.
4. **Anti-bot measures**: Some sites block headless browsers. Use `--proxy` with residential proxies for sensitive targets.

## Verification

```bash
# Test installation
crawl4ai --version

# Test basic crawl
crawl4ai https://example.com --output /tmp/test.md
cat /tmp/test.md

# Test JS rendering
crawl4ai https://react-app.example.com --js-render --output /tmp/spa-test.md
```

## Sources

- **GitHub:** [unclecode/crawl4ai](https://github.com/unclecode/crawl4ai)
- **Stars:** 66,896 (↑~253/day)
- **License:** Apache-2.0
- **Discovered:** 2026-05-29 via GitHub Trending
