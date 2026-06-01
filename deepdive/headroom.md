# Headroom: Deep Dive Analysis

## Overview
Headroom is a context compression layer for AI agents that reduces token usage by 60-95% while preserving answer quality. It operates as a Python/TypeScript library, HTTP proxy, MCP server, or one-command agent wrapper. The tool uses a multi-algorithm approach: SmartCrusher for JSON, CodeCompressor for AST-based code, and Kompress-base (a fine-tuned HuggingFace model) for prose. All compression is reversible via CCR (Compressed Content Retrieval) — originals are stored locally and the LLM can retrieve them on demand via an MCP tool.

## Key Features
- **6 compression algorithms** selected automatically by content type (JSON, AST, prose, logs, RAG chunks, conversation history)
- **CacheAligner** — stabilizes prompt prefixes so provider-side KV caches actually hit, reducing cost further
- **Reversible compression (CCR)** — originals never deleted; LLM calls `headroom_retrieve` when it needs full detail
- **Cross-agent memory** — shared compression store across Claude, Codex, Gemini agents with auto-dedup
- **`headroom learn`** — mines failed sessions, writes corrections to `CLAUDE.md` / `AGENTS.md`
- **Agent wrap** — `headroom wrap claude|codex|cursor|aider|copilot` compresses any coding agent in one command
- **MCP server** — `headroom_compress`, `headroom_retrieve`, `headroom_stats` tools for any MCP client
- **Local-first** — all compression runs locally, no data sent to external services

## Technical Architecture
- **Language**: Python 3.10+ (library) / TypeScript (npm package)
- **ContentRouter**: Detects content type (JSON, code, prose, logs) and routes to optimal compressor
- **SmartCrusher**: JSON-aware compression — removes redundant keys, collapses arrays, normalizes structures
- **CodeCompressor**: AST-based code compression — strips comments, collapses boilerplate, preserves semantics
- **Kompress-base**: Fine-tuned HuggingFace model for natural language compression (19% compression on SQuAD v2 with 97% accuracy)
- **CacheAligner**: Prefix stabilization for KV cache hit rates
- **CCR**: Compressed Content Retrieval — stores originals, provides MCP retrieval tool
- **Proxy mode**: Drop-in HTTP proxy that intercepts LLM API calls and compresses prompts/responses

## Installation & Usage
```bash
# Install
pip install "headroom-ai[all]"
npm install headroom-ai

# Wrap a coding agent (one command)
headroom wrap claude

# Run as proxy (zero code changes)
headroom proxy --port 8787

# Python library
from headroom import compress
compressed = compress(long_tool_output, target_ratio=0.3)

# MCP server (add to any MCP client config)
headroom mcp-server --port 8080

# Learn from failed sessions
headroom learn
```

## Performance Data
Real-world agent workloads:
| Workload | Before | After | Savings |
|----------|--------|-------|---------|
| Code search (100 results) | 17,765 tokens | 1,408 tokens | **92%** |
| SRE incident debugging | 65,694 tokens | 5,118 tokens | **92%** |
| GitHub issue triage | 54,174 tokens | 14,761 tokens | **73%** |
| Codebase exploration | 78,502 tokens | 41,254 tokens | **47%** |

Accuracy preservation on benchmarks:
| Benchmark | Baseline | Headroom | Delta |
|-----------|----------|----------|-------|
| GSM8K (Math) | 0.870 | 0.870 | ±0.000 |
| TruthfulQA (Factual) | 0.530 | 0.560 | +0.030 |
| SQuAD v2 (QA) | — | 97% | 19% compression |

## Use Cases
1. **Cost reduction**: Cut LLM API costs by 60-95% for agents making multiple tool calls
2. **Context window management**: Fit more information into limited context windows
3. **RAG optimization**: Compress retrieved chunks before injection into prompts
4. **Coding agent efficiency**: Compress file outputs, search results, and logs before they reach the LLM
5. **Cross-agent workflows**: Shared compression store prevents re-compressing the same content across agents
6. **Learning from failure**: `headroom learn` identifies what went wrong in failed sessions and writes corrections

## Integration Potential
- **With Hermes Agent**: Could be configured as a proxy between Hermes and its LLM provider, reducing token costs for all operations
- **With OpenCode**: `headroom wrap opencode` compresses all OpenCode interactions
- **With RAG pipelines**: Compress retrieved chunks before injection, fitting more context into the same window
- **With agent swarms**: Cross-agent memory prevents duplicate compression work across parallel agents
- **With cost tracking**: `headroom stats` provides per-session token savings data

## Advantages
1. **Multi-algorithm approach**: Different compressors for different content types = better compression ratios
2. **Reversible**: CCR means no information loss — the LLM can always retrieve full details
3. **Agent-agnostic**: Works with any coding agent via proxy or wrap mode
4. **Local-first**: No data leaves your machine
5. **Proven accuracy**: Benchmarks show maintained or improved accuracy after compression
6. **MCP integration**: Standard protocol, works with any MCP client

## Limitations
1. **Setup complexity**: Multiple installation modes (library, proxy, MCP, wrap) can be confusing
2. **Model dependency**: Kompress-base requires HuggingFace model download (~500MB)
3. **Python 3.10+ requirement**: May conflict with older project environments
4. **Compression trade-offs**: 47% savings on codebase exploration means some detail is lost (retrievable via CCR)
5. **Single-instance design**: Proxy mode may not handle high concurrent loads

## Comparison with Alternatives
- **vs. No compression**: Headroom saves 60-95% tokens with maintained accuracy
- **vs. Manual prompt engineering**: Headroom automates what would otherwise be manual context curation
- **vs. Smaller context windows**: Headroom lets you keep larger contexts at lower cost
- **vs. Prompt caching alone**: Headroom's CacheAligner improves cache hit rates beyond what providers offer natively

## Future Potential
1. **Streaming compression**: Compress tokens in real-time as they're generated
2. **Adaptive compression**: Dynamically adjust compression ratio based on task complexity
3. **Multi-model support**: Compress for different model providers simultaneously
4. **Team analytics**: Dashboard showing compression savings across team agents

## Conclusion
Headroom addresses the #1 practical bottleneck in AI agent deployment: token cost. Its multi-algorithm, reversible compression approach is technically sound, and the agent-wrap mode makes adoption trivial. For any team running coding agents at scale, Headroom's 60-95% token savings represent a direct cost reduction with no quality degradation. The MCP server integration means it works with Hermes Agent out of the box. This is a high-impact, low-effort addition to any agent stack.

---

- **Discovered:** 2026-05-29 via GitHub search (credibility: 0.90)
- **Deep dived:** 2026-06-01 via Gamma shift
- **Stars:** 3,339 (↑~50/day) | **Language:** Python | **License:** Apache-2.0
- **Last commit:** 2026-06-01
- **Relevance score:** 91/100
- **Confidence:** HIGH (multiple sources, active development, proven benchmarks)
