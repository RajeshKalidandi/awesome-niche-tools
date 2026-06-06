---
name: open-notebook
description: "Self-hosted NotebookLM alternative — organize research, chat with content, generate podcasts"
version: 1.0.0
author: Hermes Agent
license: MIT
platforms: [linux, macos]
metadata:
  hermes:
    tags: [research, knowledge-management, podcast, llm, selfhosted]
    related_skills: [crawl4ai, youtube-content]
---

# Open Notebook

Open-source, privacy-focused alternative to Google NotebookLM. Supports 18+ AI providers, multi-modal content, and podcast generation.

## Prerequisites

- Docker and Docker Compose
- An AI provider API key (OpenAI, Anthropic, Ollama, etc.)
- Git

## Quick Start

```bash
git clone https://github.com/lfnovo/open-notebook
cd open-notebook
cp .env.example .env
# Edit .env to add your AI provider API key
docker compose up -d
# Open http://localhost:8000
```

## Usage Examples

### Add Content Sources
- Paste URLs (web pages, YouTube videos)
- Upload PDFs, audio files, images
- The system auto-processes and indexes content

### Chat with Your Research
- Use the web UI to ask questions about your content
- The AI uses your uploaded content as context
- Supports full-text and vector search

### Generate Podcasts
- Select notebook entries to include
- Choose 1-4 speakers with custom voice profiles
- Generates a multi-speaker podcast from your research

## Configuration

### AI Providers
Configure in `.env` or the web UI:
- OpenAI (GPT-4, etc.)
- Anthropic (Claude)
- Ollama (local models)
- LM Studio
- 15+ other providers

### Content Sources
Edit `sources.toml` to add RSS feeds or URLs for automatic ingestion.

## Common Pitfalls

- **API costs**: Podcast generation uses significant tokens. Start with short notebooks.
- **Docker resources**: The vector search needs RAM. Allocate 2GB+ to Docker.
- **First run slow**: Initial content processing takes time depending on volume.

## Verification

```bash
# Check container is running
docker compose ps

# Test the API
curl http://localhost:8000/api/health

# Check web UI
open http://localhost:8000
```

## Links

- GitHub: https://github.com/lfnovo/open-notebook
- Website: https://www.open-notebook.ai
- Discord: https://discord.gg/37XJPXfz2w
