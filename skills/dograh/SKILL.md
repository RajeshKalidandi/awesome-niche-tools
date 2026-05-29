---
name: dograh
description: "Self-hosted voice AI platform — Vapi/Retell alternative with MCP and visual workflow builder"
tags: [voice-ai, telephony, selfhosted, mcp, stt, tts]
related_skills: [hermes-agent]
---

# Dograh — Self-Hosted Voice AI Platform

> Build, deploy, and manage voice AI applications on your own infrastructure. MCP native.

## Prerequisites

- Python 3.10+
- API keys for STT/TTS providers (Deepgram, ElevenLabs, OpenAI, etc.)
- Telephony provider (Twilio, Vonage) for inbound/outbound calls

## Installation

```bash
git clone https://github.com/dograh-hq/dograh.git
cd dograh
pip install -e .
```

## Configuration

```bash
# Set provider keys
export OPENAI_API_KEY=*** DEEPGRAM_API_KEY=*** ELEVENLABS_API_KEY=***
# Or use .env file
cp .env.example .env
```

## Usage

### Start the server
```bash
dograh serve --port 8080
```

### Create a voice workflow
```bash
curl -X POST http://localhost:8080/api/workflows \
  -H "Content-Type: application/json" \
  -d '{
    "name": "appointment-scheduler",
    "voice": "alloy",
    "llm": "gpt-4",
    "prompt": "You are a friendly appointment scheduler. Help callers book appointments.",
    "max_duration_seconds": 300
  }'
```

### MCP Server (for AI agent integration)
```bash
dograh mcp --port 8090
# Add to agent config:
# "mcpServers": {"dograh": {"command": "dograh", "args": ["mcp", "--port", "8090"]}}
```

## Common Pitfalls

1. **Latency**: First response may be slow (LLM cold start). Use streaming for real-time feel.
2. **Telephony costs**: Self-hosting eliminates platform fees, but you still pay Twilio/Vonage per minute.
3. **Voice quality**: Test with your target TTS provider — some voices sound robotic at speed.
4. **Concurrent calls**: Default config handles ~10 concurrent calls. Scale workers for more.
5. **MCP auth**: When exposing MCP server, add authentication for production use.

## Verification

```bash
# Start server
dograh serve --port 8080 &

# Health check
curl http://localhost:8080/health

# Create test workflow
curl -X POST http://localhost:8080/api/workflows \
  -H "Content-Type: application/json" \
  -d '{"name": "test", "voice": "alloy", "llm": "gpt-4", "prompt": "Say hello"}'

# List workflows
curl http://localhost:8080/api/workflows
```
