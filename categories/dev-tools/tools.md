# 🛠️ Dev Tools

> Tools for developers — code intelligence, LLM infrastructure, web crawling, and productivity utilities.

---

## [Headroom](https://github.com/chopratejas/headroom)

> Compress tool outputs, logs, files, and RAG chunks before they reach the LLM. 60-95% fewer tokens, same answers.

- **Stars:** 2,063 (↑~50/day) | **Language:** Python | **License:** Apache-2.0
- **Last commit:** 2026-05-28
- **Source credibility weight:** 0.90 (GitHub search)
- **Relevance score:** 91/100

### What It Does
Headroom is a token compression layer for LLM applications. It sits between your data and the LLM, intelligently compressing tool outputs, log files, RAG chunks, and any text input to reduce token usage by 60-95% while preserving the information the LLM needs to produce accurate answers. Available as a Python library, HTTP proxy, or MCP server.

### Why Now
Token costs are the #1 bottleneck for AI agent deployments. As agents chain more tool calls and accumulate context, token budgets explode. Headroom addresses this directly — and the MCP server integration means it works with any agent framework out of the box. Created May 2026, already at 2K stars with active daily commits.

### Why It Matters
If you're running AI agents that make multiple tool calls per task, Headroom can cut your LLM costs by 60-95% without degrading output quality. For a team spending $500/month on API calls, that's $300-475/month saved. The MCP server means zero integration work — just point your agent at it.

### Who Should Care
- Teams running AI agents with high token consumption
- RAG pipeline builders struggling with context window limits
- Solo devs paying out-of-pocket for API calls
- Anyone building LLM-powered tools that process large outputs

### Execution Pattern
```bash
# As MCP server (add to your agent config)
pip install headroom
headroom mcp-server --port 8080

# As Python library
from headroom import compress
compressed = compress(long_tool_output, target_ratio=0.3)

# As proxy
headroom proxy --upstream https://api.openai.com/v1/chat/completions
```

### Skill Potential
Yes — SKILL.md should cover: installation, MCP server setup, compression ratio tuning, integration with Hermes Agent config, and cost savings measurement.

- **Discovered:** 2026-05-29 via GitHub search (credibility: 0.90)

---

## [Crawl4AI](https://github.com/unclecode/crawl4ai)

> Open-source LLM-friendly web crawler & scraper — turns any website into structured data for AI.

- **Stars:** 66,896 (↑~253/day) | **Language:** Python | **License:** Apache-2.0
- **Last commit:** 2026-05-25
- **Source credibility weight:** 1.00 (GitHub Trending)
- **Relevance score:** 88/100

### What It Does
Crawl4AI is a web crawler designed specifically for LLM consumption. Unlike traditional scrapers that return raw HTML, Crawl4AI extracts clean, structured markdown from any website — handling JavaScript rendering, anti-bot measures, rate limiting, and proxy rotation. It outputs data optimized for RAG pipelines, fine-tuning, and agent context.

### Why Now
AI agents need web data, but most crawlers produce noisy HTML that wastes tokens. Crawl4AI bridges this gap with LLM-optimized extraction. At 67K stars and growing 253/day, it's become the de facto standard for agent web access. The Apache-2.0 license makes it safe for commercial use.

### Why It Matters
Every AI agent that needs to browse the web currently hacks together curl + regex or uses expensive browser automation. Crawl4AI provides a production-grade solution that handles the hard parts (JS rendering, anti-bot, proxy rotation) while outputting clean markdown. It's the missing piece for autonomous web research.

### Who Should Care
- AI agent builders who need reliable web access
- RAG pipeline engineers building knowledge bases from web content
- Data teams scraping structured data from dynamic sites
- Anyone tired of fighting anti-bot measures with headless browsers

### Execution Pattern
```bash
# Install
pip install crawl4ai

# Simple crawl
crawl4ai https://example.com --output article.md

# Crawl with JS rendering
crawl4ai https://spa-site.com --js-render --output content.md

# Python API
from crawl4ai import AsyncWebCrawler
async with AsyncWebCrawler() as crawler:
    result = await crawler.arun(url="https://example.com")
    print(result.markdown)
```

### Skill Potential
Yes — SKILL.md should cover: installation, CLI usage, Python API, JS rendering setup, proxy configuration, integration with Hermes web tools, and common crawling patterns.

- **Discovered:** 2026-05-29 via GitHub Trending (credibility: 1.00)

---

## [mcp2cli](https://github.com/knowsuchagency/mcp2cli)

> Turn any MCP, OpenAPI, or GraphQL server into a CLI — at runtime, with zero codegen.

- **Stars:** 2,183 (↑~25/day) | **Language:** Python | **License:** MIT
- **Last commit:** 2026-05-26
- **Source credibility weight:** 0.90 (GitHub search)
- **Relevance score:** 86/100

### What It Does
mcp2cli dynamically converts MCP servers, OpenAPI specs, and GraphQL schemas into fully functional CLI tools at runtime. No code generation, no build steps — point it at any API and get a CLI with auto-completion, help text, and proper argument parsing. Works with any MCP server your agent already uses.

### Why Now
The MCP ecosystem is exploding with servers, but most can only be accessed programmatically. mcp2cli bridges the gap between MCP and the command line, making every MCP server accessible from scripts, cron jobs, and terminal workflows. Zero codegen means it works immediately with any server.

### Why It Matters
This tool unlocks MCP servers for shell scripting, CI/CD pipelines, and any context where you need a CLI instead of a library. Instead of writing wrapper scripts for each MCP server, mcp2cli generates them automatically. It's the glue between the MCP ecosystem and traditional Unix workflows.

### Who Should Care
- Shell scripters who want MCP server access from bash
- CI/CD engineers building pipelines that use AI tools
- DevOps teams automating tasks with MCP servers
- Anyone who prefers CLI over library interfaces

### Execution Pattern
```bash
# Install
pip install mcp2cli

# Convert an MCP server to CLI
mcp2cli --server https://my-mcp-server.com/sse --output ./my-tool

# Use the generated CLI
./my-tool --help
./my-tool subcommand --arg value

# Convert OpenAPI spec
mcp2cli --openapi https://api.example.com/openapi.json --output ./api-cli
```

### Skill Potential
Yes — SKILL.md should cover: installation, MCP server conversion, OpenAPI/GraphQL conversion, CLI customization, integration with Hermes terminal tools, and scripting patterns.

- **Discovered:** 2026-05-29 via GitHub search (credibility: 0.90)

---

## [Codebase Memory MCP](https://github.com/DeusData/codebase-memory-mcp)

> High-performance code intelligence MCP server. Indexes codebases into a persistent knowledge graph. 155 languages, sub-ms queries.

- **Stars:** 2,770 (↑~30/day) | **Language:** C | **License:** MIT
- **Last commit:** 2026-05-28
- **Source credibility weight:** 0.90 (GitHub search)
- **Relevance score:** 85/100

### What It Does
Codebase Memory MCP is a single static binary (written in C) that indexes entire codebases into a persistent knowledge graph. It supports 155 programming languages, delivers sub-millisecond queries, and reduces token usage by 99% compared to raw code context. As an MCP server, it plugs directly into any AI coding agent.

### Why Now
AI coding agents (Claude Code, Codex, Cursor) consume massive amounts of tokens loading codebase context. Codebase Memory MCP solves this by pre-indexing code into a knowledge graph that provides precise, token-efficient context. The C implementation means it's fast enough for real-time agent workflows.

### Why It Matters
Instead of loading entire files into context (wasting tokens on irrelevant code), agents can query the knowledge graph for exactly the functions, types, and relationships they need. This means faster responses, lower costs, and better code understanding. The 155-language support makes it universally applicable.

### Who Should Care
- AI coding agent users (Claude Code, Codex, Cursor, Copilot)
- Teams with large codebases struggling with context window limits
- Anyone building code-aware AI tools
- Developers who want faster, cheaper code suggestions

### Execution Pattern
```bash
# Install (single static binary)
curl -sL https://github.com/DeusData/codebase-memory-mcp/releases/latest/download/codebase-memory-mcp -o /usr/local/bin/codebase-memory-mcp
chmod +x /usr/local/bin/codebase-memory-mcp

# Index a codebase
codebase-memory-mcp index /path/to/repo

# Run as MCP server
codebase-memory-mcp serve --port 3000

# Query from CLI
codebase-memory-mcp query "find all auth middleware"
```

### Skill Potential
Yes — SKILL.md should cover: installation, codebase indexing, MCP server setup, query patterns, integration with Hermes Agent, and performance tuning.

- **Discovered:** 2026-05-29 via GitHub search (credibility: 0.0.90)

---

## [LLMix](https://github.com/sno-ai/llmix)

> Production LLM call layer for AI agents: hot-swap models, cache, retries, circuit breakers, key rotation.

- **Stars:** 129 (↑~6/day) | **Language:** Python | **License:** Apache-2.0
- **Last commit:** 2026-05-28
- **Source credibility weight:** 0.90 (GitHub search)
- **Relevance score:** 78/100

### What It Does
LLMix is a production-grade LLM call layer that wraps OpenAI, Anthropic, AI SDK, and LiteLLM with enterprise features: hot-swap models via MDA presets, response caching, automatic retries with exponential backoff, circuit breakers, API key rotation, and singleflight deduplication. Available in Python, TypeScript, and Rust with identical APIs.

### Why Now
Created May 9, 2026 (20 days ago), LLMix is brand new but addresses a real gap: most AI agents use raw API calls without production safeguards. LLMix adds the reliability layer that production deployments need — without requiring a full LLMOps stack. The polyglot support (Python/TS/Rust) makes it accessible to any team.

### Why It Matters
AI agents fail silently when API keys run out, rate limits hit, or models go down. LLMix adds circuit breakers and key rotation that prevent cascading failures. The response cache can cut API costs by 30-50% for repeated queries. It's the missing reliability layer between "it works in dev" and "it works in production."

### Who Should Care
- Teams running AI agents in production
- Anyone hitting rate limits or burning through API keys
- Developers building multi-model applications
- DevOps engineers deploying LLM-powered services

### Execution Pattern
```bash
# Install
pip install llmix

# Python usage
from llmix import LLMClient
client = LLMClient(
    providers=["openai", "anthropic"],
    cache=True,
    retries=3,
    circuit_breaker=True
)
response = client.chat("Hello, world!")

# Hot-swap models
client.set_model("anthropic", "claude-sonnet-4-20250514")
```

### Skill Potential
Yes — SKILL.md should cover: installation, provider configuration, caching setup, circuit breaker tuning, key rotation, and integration with Hermes Agent model routing.

- **Discovered:** 2026-05-29 via GitHub search (credibility: 0.90)

---

## [ContextPlus](https://github.com/forloopcodes/contextplus)

> Semantic Intelligence for Large-Scale Engineering. RAG + Tree-sitter AST + Spectral Clustering into a searchable feature graph.

- **Stars:** 1,911 (↑~20/day) | **Language:** TypeScript | **License:** MIT
- **Last commit:** 2026-05-28
- **Source credibility weight:** 0.90 (GitHub search)
- **Relevance score:** 76/100

### What It Does
ContextPlus is an MCP server that combines RAG, Tree-sitter AST parsing, Spectral Clustering, and Obsidian-style linking to turn massive codebases into searchable, hierarchical feature graphs. It provides 99% accuracy for code understanding tasks by understanding semantic relationships, not just text matching.

### Why Now
As codebases grow, traditional search breaks down. ContextPlus uses spectral clustering to identify feature boundaries and Tree-sitter AST to understand code structure — providing search results that understand what code *does*, not just what it *says*. The MCP integration makes it agent-ready.

### Why It Matters
For teams with large monorepos or complex architectures, ContextPlus provides the code understanding that grep and basic RAG can't. It identifies feature boundaries, traces dependencies, and provides hierarchical context that helps agents navigate unfamiliar codebases accurately.

### Who Should Care
- Teams maintaining large codebases (100K+ LOC)
- AI agents that need to navigate complex architectures
- Engineers onboarding to new projects
- Anyone building code-aware search tools

### Execution Pattern
```bash
# Install
npm install -g contextplus

# Index a codebase
contextplus index /path/to/repo

# Run as MCP server
contextplus serve --port 3001

# Query
contextplus search "authentication flow"
```

### Skill Potential
Yes — SKILL.md should cover: installation, codebase indexing, MCP server setup, search patterns, and integration with Hermes Agent.

- **Discovered:** 2026-05-29 via GitHub Trending (credibility: 0.90)

---

## [stop-slop](https://github.com/hardikpandya/stop-slop)

> A skill file for removing AI tells from prose — make your writing sound human again.

- **Stars:** 6,358 (↑~755/day) | **Language:** N/A (skill file) | **License:** MIT
- **Last commit:** 2026-05-28
- **Source credibility weight:** 1.00 (GitHub Trending)
- **Relevance score:** 70/100

### What It Does
stop-slop is a skill file (for Claude Code, Codex, or similar agents) that instructs the AI to write in a natural, human voice — stripping out the characteristic "AI slop" patterns like "Let's dive in", "I'd be happy to help", "Here's the thing", and other robotic phrasings. It's a single file you drop into your agent's skills directory.

### Why Now
AI-generated content is everywhere, and readers are getting better at detecting it. stop-slop addresses the growing demand for AI-assisted writing that doesn't sound like AI. At 6.4K stars and 755/day, it's clearly resonating with developers who want their AI tools to produce natural prose.

### Why It Matters
The difference between "AI-assisted" and "AI-generated" is voice. stop-slop ensures that when you use AI to write documentation, emails, or blog posts, the output reads like a human wrote it. This is increasingly important for professional communication and content quality.

### Who Should Care
- Anyone using AI for writing (docs, emails, blog posts)
- Content teams using AI assistants
- Developers who want natural-sounding commit messages and PR descriptions
- Technical writers who use AI but want human voice

### Execution Pattern
```bash
# Download the skill file
curl -sL https://raw.githubusercontent.com/hardikpandya/stop-slop/main/stop-slop.md -o ~/.claude/skills/stop-slop.md

# Or for Codex
cp stop-slop.md ~/.codex/skills/
```

### Skill Potential
No — this is already a skill file. The value is in using it, not wrapping it.

- **Discovered:** 2026-05-29 via GitHub Trending (credibility: 1.00)

---

## [Understand-Anything](https://github.com/Lum1104/Understand-Anything)

> Graphs that teach > graphs that impress. Turn any code into an interactive knowledge graph.

- **Stars:** 42,616 (↑~3,766/day) | **Language:** TypeScript | **License:** MIT
- **Last commit:** 2026-05-28
- **Source credibility weight:** 1.00 (GitHub Trending)
- **Relevance score:** 72/100

### What It Does
Understand-Anything converts any codebase into an interactive knowledge graph that you can explore, search, and ask questions about. Unlike visualization tools that produce impressive-but-useless graphs, this focuses on *teaching* — helping you understand code architecture, dependencies, and data flow through structured exploration.

### Why Now
At 42K stars and growing 3,766/day, this is one of the fastest-growing repos on GitHub right now. It works with Claude Code, Codex, Cursor, Copilot, and Gemini CLI — making it universally compatible. The "graphs that teach" philosophy addresses the real problem: existing code visualization tools produce eye candy, not understanding.

### Why It Matters
Onboarding to a large codebase is one of the most expensive engineering activities. Understand-Anything dramatically reduces this cost by providing interactive exploration that adapts to your learning path. For AI agents, it provides structured context that's more efficient than raw file loading.

### Who Should Care
- Engineers onboarding to new codebases
- Teams documenting architecture
- AI agents that need code understanding
- Technical leads doing code reviews across large systems

### Execution Pattern
```bash
# Install
npm install -g understand-anything

# Generate knowledge graph from codebase
understand-anything generate /path/to/repo

# Interactive exploration
understand-anything explore /path/to/repo

# Ask questions
understand-anything ask "How does authentication work in this codebase?"
```

### Skill Potential
No — too high-level for automation. Best used interactively.

- **Discovered:** 2026-05-29 via GitHub Trending (credibility: 1.00)

---

## [Codegraph](https://github.com/colbymchenry/codegraph)

> Pre-indexed code knowledge graph for Claude Code, Codex, Gemini, Cursor, OpenCode — 100% local.

- **Stars:** 31,570 (↑~180/week) | **Language:** TypeScript | **License:** MIT
- **Last commit:** 2026-05-28
- **Source credibility weight:** 1.00 (GitHub Trending weekly)
- **Relevance score:** 70/100

### What It Does
Codegraph pre-indexes codebases into knowledge graphs that AI coding agents can query directly. Unlike on-the-fly analysis, Codegraph builds the graph once and reuses it — providing faster, more accurate context with fewer tokens and tool calls. Works with Claude Code, Codex, Gemini, Cursor, OpenCode, and more.

### Why Now
AI coding agents are becoming mainstream, but they all struggle with the same problem: loading enough context without wasting tokens. Codegraph solves this by pre-indexing code relationships, so agents can query exactly what they need instead of loading entire files. At 32K stars, it's proven at scale.

### Why It Matters
Pre-indexed knowledge graphs mean AI agents spend less time exploring and more time coding. The "100% local" guarantee means no code leaves your machine — critical for enterprise and security-sensitive environments. This is the infrastructure layer that makes AI coding agents practical for large codebases.

### Who Should Care
- AI coding agent users (Claude Code, Codex, Cursor)
- Enterprise teams with security requirements
- Anyone with a codebase larger than 50K LOC
- Developers who want faster, cheaper AI code suggestions

### Execution Pattern
```bash
# Install
npm install -g codegraph

# Index a codebase
codegraph index /path/to/repo

# Query the graph
codegraph query "find all API endpoints"

# Integrate with Claude Code
codegraph setup --agent claude-code
```

### Skill Potential
No — better used as a standalone tool than wrapped in a skill.

- **Discovered:** 2026-05-29 via GitHub Trending weekly (credibility: 1.00)
