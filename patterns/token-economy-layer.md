# Pattern: Token Economy Layer

> Compress, cache, and optimize every token before it reaches the LLM.

## Problem
AI agents consume tokens at an accelerating rate — tool outputs, code context, RAG chunks, conversation history. Token costs scale linearly with usage, and context windows are finite. The #1 bottleneck for agent deployments is token budget.

## Solution
Insert a compression/optimization layer between data sources and the LLM. This layer:
1. **Compresses** tool outputs (60-95% reduction)
2. **Caches** repeated queries (30-50% cost reduction)
3. **Indexes** codebases into knowledge graphs (99% token reduction)
4. **Selects** only relevant context (intelligent filtering)

The key insight: the same information can be represented in far fewer tokens without losing meaning. The compression happens at the infrastructure level, not the application level.

## When to Use
- Running AI agents with multiple tool calls per task
- Processing large codebases (>50K LOC)
- Building RAG pipelines with large document corpora
- Paying per-token for API calls
- Hitting context window limits regularly

## When NOT to Use
- Simple single-turn Q&A (no compression needed)
- When latency budget is extremely tight (compression adds ms)
- When output quality is mission-critical and any loss is unacceptable
- When you control the model and can extend context windows directly

## Discovered From
- **Headroom** — 6 compression engines, 60-95% token reduction, MCP server
- **Codebase Memory MCP** — knowledge graph indexing, 99% token reduction
- **ContextPlus** — RAG + AST + clustering, 99% accuracy
- **Ktx** — executable context for analytics agents
- **Codegraph** — pre-indexed code knowledge graphs
- **Understand-Anything** — interactive code exploration

## Variants
- **Lossy Compression**: Remove redundancy, keep meaning (Headroom SmartCrusher)
- **AST-Aware**: Parse code structure, compress semantically (Headroom CodeCompressor)
- **Knowledge Graph**: Index relationships, query on demand (Codebase Memory MCP)
- **Pre-computed Context**: Build once, query many times (Codegraph)
- **Reversible Compression**: Store originals, retrieve on demand (Headroom CCR)

## Metrics
- 6 out of 28 curated tools (21%) address token economy
- Headroom claims 60B+ tokens saved across users
- Average compression ratio: 73% (range: 47-95%)
- Knowledge graph approaches achieve 99% reduction for code context
