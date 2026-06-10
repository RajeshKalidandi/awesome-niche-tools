# Deep Dive: last30days-skill

## Overview

last30days-skill is an AI agent skill that performs cross-platform research on any topic, gathering information from Reddit, X (Twitter), YouTube, Hacker News, Polymarket, and the general web, then synthesizing a grounded summary with citations.

## Architecture

### Core Components

1. Platform Adapters: Modular connectors for each data source (Reddit API, Twitter API, YouTube Data API, HN API, Polymarket API, web scraping)
2. Citation Engine: Tracks and formats source URLs, timestamps, and credibility scores
3. Synthesis Module: Uses LLM to combine multi-source information into coherent summaries
4. Caching Layer: Stores recent queries to avoid redundant API calls

### Data Flow

User Query -> Platform Selection -> Parallel Data Collection -> Deduplication & Ranking -> LLM Synthesis -> Formatted Output

## Competitive Analysis

| Feature | last30days-skill | Perplexity | ChatGPT + Browsing |
|---------|------------------|------------|---------------------|
| Real-time data | Yes | Yes | Yes |
| Multi-platform | Yes (6+ sources) | No (web only) | No (web only) |
| Citation tracking | Yes | Yes | Yes |
| Open source | Yes | No | No |
| Self-hosted | Yes | No | No |
| Customizable | Yes | No | Limited |

## Limitations

1. API dependency: Requires valid API keys for each platform
2. Rate limits: Subject to platform-specific rate limiting
3. Cost: API calls can become expensive for high-volume usage
4. Data quality: Relies on platform moderation and source reliability

## Use Cases

### Market Research
Research AI agent market trends across Twitter, Reddit, and arxiv.

### Competitive Intelligence
Compare OpenAI vs Anthropic vs Google DeepMind across multiple sources.

### Fact Check recent breakthroughs in quantum computing via arxiv, news, and Twitter.

## Integration Patterns

### With Hermes Agent
Integrate as a research skill that queries multiple platforms and returns structured summaries.

### In RAG Pipelines
Use as a pre-processing step for knowledge retrieval, feeding results into vector databases.

## Performance Considerations

- Latency: 5-15 seconds depending on number of platforms queried
- Cost: ~/usr/bin/bash.01-0.10 per query depending on platforms and data volume
- Scalability: Horizontal scaling via async operations and caching

## Future Directions

1. Platform expansion: Adding LinkedIn, academic databases, government sources
2. Real-time streaming: Continuous monitoring and alerting
3. Multilingual support: Research in multiple languages
4. Custom source adapters: Plugin system for proprietary data sources
