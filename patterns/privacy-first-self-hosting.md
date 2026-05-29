# Pattern: Privacy-First Self-Hosting

> Run AI capabilities locally. No data leaves your machine.

## Problem
Cloud AI services (Vapi, Retell, Google Photos, ChatGPT) require sending data to third-party servers. For healthcare, legal, finance, and privacy-conscious users, this is a non-starter. Self-hosting AI capabilities has traditionally required deep technical expertise and complex infrastructure.

## Solution
Package AI capabilities into self-hosted tools that run on consumer hardware:
1. **Local inference** via Ollama, llama.cpp, or similar
2. **Single-binary or Docker deployment** — minimal infrastructure
3. **BYOK (Bring Your Own Key)** for cloud LLM APIs when needed
4. **MCP integration** for agent compatibility
5. **Privacy by design** — data never leaves the host

The key insight: self-hosting doesn't mean sacrificing features. Modern tools provide the same capabilities as cloud services while keeping data local.

## When to Use
- Handling sensitive data (healthcare, legal, finance)
- Operating in regulated environments (HIPAA, GDPR, SOC2)
- Privacy-conscious personal use
- Air-gapped or restricted network environments
- Cost optimization (no per-minute/per-token fees)

## When NOT to Use
- When you need global availability and uptime SLAs
- When your team lacks infrastructure expertise
- When scaling to millions of users (cloud is more practical)
- When real-time collaboration across locations is required

## Discovered From
- **Dograh** — self-hosted voice AI (Vapi/Retell alternative)
- **A-Eye** — local photo intelligence via Ollama
- **LUKSbox** — encrypted containers with FIDO2/TPM
- **Posthorn** — self-hosted email gateway
- **Moltis** — self-hosted personal AI agent server
- **NetMap** — self-hosted network monitoring

## Variants
- **Full Self-Host**: All inference local (A-Eye with Ollama)
- **Hybrid**: Local processing + optional cloud LLM (Dograh BYOK)
- **Encrypted Self-Host**: Data encrypted at rest with hardware keys (LUKSbox)
- **Gateway Pattern**: Self-hosted proxy to cloud services (Posthorn)

## Metrics
- 6 out of 28 curated tools (21%) are self-hostable
- Self-hosted tools average higher community engagement (stars/day)
- Docker deployment is the most common packaging (4/6 tools)
- Ollama is the dominant local inference backend (3/6 tools)
