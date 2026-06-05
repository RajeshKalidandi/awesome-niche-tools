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
- Intel macOS users: avoid `pip install headroom-ai[proxy]`; use Docker or Docker Native instead, or wait for a resolved install path for `x86_64-apple-darwin`

### Compatibility & Issues
- **Open issue:** Headroom 0.22.4 install currently fails on macOS Intel (`x86_64-apple-darwin`) because `ort-sys v2.0.0-rc.12` has no prebuilt binaries for that target. Reported in `chopratejas/headroom#525`.
- **Workaround:** Use the official Docker image and route clients through the proxy, e.g.:
  ```bash
  docker run --rm -it -p 8787:8787 ghcr.io/chopratejas/headroom:latest
  ```
  Set your client base URL to `http://localhost:8787` when launching tools like Claude Code. In that image, only the proxy is exposed; `headroom wrap` is not available.
- **Implication:** If you need `headroom wrap` or a native CLI on Intel Macs, wait for an upstream fix that makes the ONNX backend optional or provides a prebuilt wheel.

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


## [Ratty](https://github.com/orhun/ratty)

> GPU-rendered terminal emulator with inline 3D graphics

- **Stars:** 2,663 (↑~50/day) | **Language:** Rust | **License:** MIT
- **Last commit:** 2026-05-27
- **Source credibility weight:** 0.80 (Lobsters)
- **Relevance score:** 75/100

### What It Does
Ratty is a GPU-rendered terminal emulator that can display inline 3D graphics directly in your terminal output. Imagine running a command and seeing a rotating 3D model appear right in your terminal — no separate window, no browser, just the terminal. Built in Rust with GPU acceleration for smooth rendering.

### Why Now
Terminal emulators haven't fundamentally changed in decades. Ratty brings GPU rendering and inline 3D to the terminal, opening up new possibilities for CLI tools that need visual output — CAD previews, data visualization, game development, scientific computing. The Lobsters community (triangle-59 score) signals strong developer interest.

### Why It Matters
This blurs the line between terminal and GUI. CLI tools can now produce rich visual output without leaving the terminal. It's not just novelty — for developers who live in the terminal, having inline 3D means faster workflows and fewer context switches between terminal and browser/GUI.

### Who Should Care
- Terminal power users who want richer CLI experiences
- CLI tool developers exploring visual output
- Data scientists who want inline visualization
- Game developers prototyping in the terminal
- Anyone curious about the future of terminal interfaces

### Execution Pattern
```bash
# Install via cargo
cargo install ratty

# Run as your terminal
ratty

# In a Ratty-compatible terminal, tools can render 3D
# Example: render a 3D model inline
echo '{"type":"mesh","vertices":[...]}' | ratty-render

# Or use the library in your Rust CLI tool
# Cargo.toml: ratty = "0.1"
```

### Skill Potential
No — too niche for automation, better as a discovery entry.

- **Discovered:** 2026-05-29 via Lobsters (credibility: 0.80)

---

## [LiteParse](https://github.com/run-llama/liteparse)

> A fast, helpful, and open-source document parser — rewritten in Rust, 100x faster

- **Stars:** 6,471 (↑~200/day) | **Language:** Rust | **License:** Apache-2.0
- **Last commit:** 2026-05-29
- **Source credibility weight:** 0.85 (Hacker News)
- **Relevance score:** 88/100

### What It Does
LiteParse is a document parser rewritten in Rust that's 100x faster than existing Python-based parsers. It extracts text, tables, images, and metadata from PDFs, DOCX, HTML, and other document formats. Designed specifically for RAG pipelines and LLM context loading — output is clean, structured markdown optimized for token efficiency.

### Why Now
Document parsing is the bottleneck in every RAG pipeline. Python-based parsers (PyPDF2, pdfplumber, unstructured) are slow and produce noisy output. LiteParse's Rust implementation makes document parsing 100x faster while producing cleaner output. From the LlamaIndex team, it's designed specifically for AI/ML workflows.

### Why It Matters
If you're building a RAG pipeline, document parsing speed directly determines your pipeline throughput. Going from 100 docs/hour to 10,000 docs/hour changes what's possible. LiteParse also produces cleaner output, meaning fewer tokens wasted on noise and better retrieval quality. It's a foundational upgrade for any document-heavy AI application.

### Who Should Care
- RAG pipeline engineers parsing large document corpora
- Data teams extracting structured data from documents
- AI researchers building document understanding systems
- Anyone processing PDFs/DOCX at scale
- Developers tired of slow Python document parsers

### Execution Pattern
```bash
# Install
cargo install liteparse

# Parse a single document
liteparse document.pdf --output ./parsed/

# Parse a directory of documents
liteparse ./documents/ --recursive --output ./parsed/

# Python API
pip install liteparse
```

```python
from liteparse import parse
result = parse("document.pdf")
print(result.markdown)   # Clean markdown output
print(result.tables)     # Extracted tables as dataframes
print(result.images)     # Extracted images as paths
print(result.metadata)   # Title, author, dates
```

### Skill Potential
Yes — SKILL.md should cover: installation, CLI usage, Python API, MCP server setup, document format support, and RAG pipeline integration.

- **Discovered:** 2026-05-29 via Hacker News (credibility: 0.85)

---

## [AudioMass](https://github.com/pkalogiros/AudioMass)

> Free full-featured web-based audio & waveform editing tool

- **Stars:** 2,687 (↑steady) | **Language:** JavaScript | **License:** MIT
- **Last commit:** 2026-05-25
- **Source credibility weight:** 0.85 (Hacker News)
- **Relevance score:** 78/100

### What It Does
AudioMass is a free, open-source, web-based audio editor with multitrack support. It runs entirely in the browser — no installation, no accounts, no data upload. Full waveform editing, effects, filters, and now multitrack editing for complex audio projects. Think Audacity, but in your browser with zero setup.

### Why Now
AudioMass just launched multitrack support (the HN post got 547 points), making it a serious alternative to desktop DAWs for quick audio work. The web-based nature means it works on any device, anywhere — no software installation needed. For developers who need quick audio editing (podcast clips, sound effects, voice memos), it's the fastest path from idea to edited audio.

### Why It Matters
Audio editing has traditionally required installing desktop software. AudioMass eliminates that friction entirely. Share a URL, start editing. This is especially valuable for teams that need quick audio edits without installing software on every machine — journalists, podcasters, educators, developers.

### Who Should Care
- Podcasters needing quick audio edits without a DAW
- Developers building audio-related applications
- Educators creating audio content
- Journalists editing interview clips
- Anyone who's ever needed to trim, cut, or enhance audio quickly

### Execution Pattern
```bash
# Visit https://audiomass.co — no installation needed!

# Or self-host
git clone https://github.com/pkalogiros/AudioMass.git
cd AudioMass
npx serve .

# Open http://localhost:3000 in your browser
# Drag and drop audio files to start editing
# Multitrack: click "+" to add tracks
```

### Skill Potential
No — web-based tool, better as discovery entry than automation skill.

- **Discovered:** 2026-05-29 via Hacker News (credibility: 0.85)

## [Absurd](https://github.com/earendil-works/absurd)

> Postgres-native durable workflow system — moves durable execution into the database via stored procedures. No extra services needed.

- **Stars:** 1,950 (↑~50/day) | **Language:** Python | **License:** MIT
- **Last commit:** 2026-05-27
- **Source credibility weight:** 0.85 (Lobsters)
- **Relevance score:** 85/100

### What It Does
Absurd is a durable workflow system that stores all workflow state, execution logs, and task definitions directly in PostgreSQL using stored procedures. Unlike Temporal, Prefect, or Celery which require separate infrastructure (databases, message queues, worker fleets), Absurd runs entirely within Postgres. Define workflows as SQL, execute them via stored procedures, and get durability, retries, and observability from the database you already operate.

### Why Now
The durable execution space is fragmented — Temporal requires a full Java/Kotlin stack, Prefect needs its own server, and Celery requires Redis/RabbitMQ. Absurd eliminates this infrastructure sprawl by leveraging Postgres's existing ACID guarantees, WAL, and connection pooling. Created May 2026, already at 1.9K stars with daily commits — the community is validating the "Postgres as workflow engine" thesis.

### Why It Matters
If you already run Postgres (and most teams do), Absurd gives you durable workflows with zero additional infrastructure. No new services to deploy, monitor, or pay for. The stored-procedure approach means workflows are just SQL — version-controlled, testable, and familiar to any backend engineer. This could replace half the workflow orchestration tools in the ecosystem.

### Who Should Care
- Teams running Postgres who need workflow orchestration without new infrastructure
- Solo devs who want durable execution without deploying Temporal/Prefect
- Backend engineers who prefer SQL over YAML workflow definitions
- Anyone tired of maintaining separate message queues for task processing

### Execution Pattern
```bash
# Install
pip install absurd

# Initialize in your Postgres database
absurd init --database postgresql://localhost/myapp

# Define a workflow (SQL)
absurd workflow create order_processing << 'SQL'
INSERT INTO absurd.workflows (name, steps) VALUES
  ('process_order', ARRAY['validate_payment', 'ship_items', 'send_notification']);
SQL

# Execute
absurd run order_processing --input '{"order_id": 42}'

# Check status
absurd status <execution_id>
```

### Skill Potential
Yes — SKILL.md should cover: installation, Postgres setup, workflow definition in SQL, execution patterns, monitoring, and integration with Hermes Agent for automated task orchestration.

- **Discovered:** 2026-05-30 via Lobsters (credibility: 0.85)

---

## [AISlop](https://github.com/scanaislop/aislop)

> Catch the slop AI coding agents leave in your code. 40+ rules, 7 languages, deterministic, no LLM needed.

- **Stars:** 191 (↑~10/day) | **Language:** TypeScript | **License:** MIT
- **Last commit:** 2026-05-30
- **Source credibility weight:** 0.90 (Hacker News Show HN)
- **Relevance score:** 78/100

### What It Does
AISlop is a static analysis linter specifically designed to detect AI-generated code patterns — the "slop" that coding agents leave behind. It has 40+ rules across 7 languages that catch telltale signs: over-commented code, redundant error handling, unnecessary abstractions, generic variable names, and the distinctive "helpful but bloated" style of AI output. Runs deterministically with no LLM calls — pure pattern matching.

### Why Now
AI coding agents are now producing a significant percentage of new code. But AI-generated code has recognizable patterns that experienced developers spot immediately — over-engineering, excessive comments, and generic naming. AISlop provides a systematic way to catch these patterns before they reach production. Created May 2026, already at 191 stars with daily commits — the community recognizes the need for AI code quality gates.

### Why It Matters
As AI agents write more code, the quality gap between human-written and AI-generated code becomes a real problem. AISlop is the linting layer that catches AI-specific anti-patterns without requiring a human reviewer. It's the CI gate between "agent wrote it" and "it ships." Teams using AI agents at scale need this to maintain code quality.

### Who Should Care
- Teams using AI coding agents (Claude Code, Codex, Cursor) in production
- Code reviewers who want to catch AI-specific patterns automatically
- Engineering managers concerned about AI code quality
- Anyone running CI/CD pipelines that include AI-generated code

### Execution Pattern
```bash
# Install
npm install -g aislop

# Run on a project
aislop ./src/

# Run with specific languages
aislop --lang typescript,python ./src/

# CI integration
aislop --format json ./src/ | jq '.violations'

# Fix auto-fixable issues
aislop --fix ./src/
```

### Skill Potential
Yes — SKILL.md should cover: installation, rule configuration, CI integration, language-specific rules, and integration with Hermes Agent's code review workflow.

- **Discovered:** 2026-05-30 via Hacker News Show HN (credibility: 0.90)

---

## [Narwhal](https://github.com/Nonanti/narwhal)

> TUI database client with a built-in MCP server. Five databases, vim editing, Lua plugins.

- **Stars:** 21 (↑~5/day) | **Language:** Rust | **License:** MIT
- **Last commit:** 2026-05-28
- **Source credibility weight:** 0.75 (GitHub Search)
- **Relevance score:** 72/100

### What It Does
Narwhal is a terminal UI database client that supports PostgreSQL, MySQL, SQLite, DuckDB, and Clickhouse. It features vim-style editing, Lua plugin support, and — critically — a built-in MCP server that exposes your database connections to AI agents. Query databases from your terminal, and let your AI coding agent query them too through the same interface.

### Why Now
The MCP ecosystem is growing rapidly, but most database MCP servers are standalone services that require separate setup. Narwhal combines a practical TUI database client with MCP server functionality — one tool that serves both human and AI agent needs. The vim editing and Lua plugins make it extensible for power users. Created May 2026, growing steadily.

### Why It Matters
Most developers use separate tools for human database access (pgAdmin, DBeaver, DataGrip) and AI agent database access (custom MCP servers). Narwhal unifies these — configure your database connections once, use them interactively in the TUI, and expose the same connections to AI agents via MCP. One tool, two interfaces, zero duplication.

### Who Should Care
- Developers who work with multiple database types
- AI agent builders needing database MCP servers
- Terminal-first developers who prefer vim-style interfaces
- Teams wanting a unified database access layer for humans and agents

### Execution Pattern
```bash
# Install
cargo install narwhal

# Connect to PostgreSQL
narwhal postgresql://user:pass@localhost/mydb

# Connect to SQLite
narwhal sqlite://./data.db

# Run as MCP server (exposes all configured connections)
narwhal mcp --port 3090

# In agent config:
# { "mcpServers": { "narwhal": { "command": "narwhal", "args": ["mcp", "--port", "3090"] } } }

# Vim-style navigation in TUI
# :help for commands
# Ctrl-n/Ctrl-p for result navigation
```

### Skill Potential
Yes — SKILL.md should cover: installation, database connection setup, MCP server configuration, Lua plugin development, and integration with Hermes Agent's database tools.

- **Discovered:** 2026-05-30 via GitHub Search (credibility: 0.75)

---

## [Roto](https://github.com/NLnetLabs/roto)

> Statically-typed, compiled embedded scripting language for Rust — used by Rotonda BGP router.

- **Stars:** 492 (↑~5/day) | **Language:** Rust | **License:** BSD-3-Clause
- **Last commit:** 2026-05-28
- **Source credibility weight:** 0.85 (Lobsters)
- **Relevance score:** 68/100

### What It Does
Roto is a statically-typed, compiled scripting language designed to be embedded in Rust applications. Unlike Lua or Rhai (dynamic scripting), Roto provides compile-time type checking and AOT compilation — giving you the flexibility of a scripting language with the safety guarantees of a typed language. Used in production by the Rotonda BGP router for filter expressions and route policies.

### Why Now
Rust applications often need embedded scripting for user-defined logic (filters, plugins, rules), but existing options have tradeoffs: Lua is dynamically typed, Rhai lacks AOT compilation, and WASM is heavyweight. Roto fills this gap with static typing and compilation — scripts are validated at embed time, not runtime. The NLnet Labs backing (they maintain Routinator, the RPKI validator) signals production-grade quality.

### Why It Matters
For Rust developers building extensible systems (routers, proxies, rule engines), Roto provides a scripting layer that catches errors at compile time rather than runtime. This is critical for network infrastructure where a type error in a filter expression could cause an outage. The BGP router use case validates it for high-reliability environments.

### Who Should Care
- Rust developers building extensible applications
- Network engineers building routing/filtering tools
- Anyone needing embedded scripting without dynamic typing risks
- Plugin system designers looking for type-safe scripting

### Execution Pattern
```rust
// In your Rust application
use roto::runtime::{Runtime, TypeRegistry};

// Register types
let mut reg = TypeRegistry::new();
reg.register::<Route>();

// Compile and run scripts
let runtime = Runtime::new(reg);
let script = runtime.compile("filter where prefix.len() <= 24")?;
let result = script.run(&route)?;
```

### Skill Potential
No — too niche for a Hermes skill. Best used as a library within Rust projects.

- **Discovered:** 2026-05-30 via Lobsters (credibility: 0.85)

---

## [Compound Engineering Plugin](https://github.com/EveryInc/compound-engineering-plugin)

> Official Compound Engineering plugin for Claude Code, Codex, Cursor, and more — AI skills and agents that make each unit of engineering work easier than the last.

- **Stars:** 18,247 (↑~50/day) | **Language:** TypeScript | **License:** MIT
- **Last commit:** 2026-05-29
- **Source credibility weight:** 1.00 (GitHub Trending)
- **Relevance score:** 72/100

### What It Does
Compound Engineering is a methodology-first plugin for AI coding agents that inverts the traditional development cycle: 80% planning and review, 20% execution. It provides a suite of skills (`/ce-brainstorm`, `/ce-plan`, `/ce-work`, `/ce-code-review`, `/ce-debug`, `/ce-compound`) that enforce rigorous planning before any code is written, and codify learnings afterward so future work compounds rather than accumulates debt. Built by Every Inc., the team behind Every.to.

### Why Now
As AI coding agents generate code at unprecedented speed, the bottleneck has shifted from *writing code* to *knowing what to write and whether it's right*. Compound Engineering addresses this directly — its skills enforce the planning and review discipline that keeps agent-generated codebases maintainable. At 18K stars and trending on GitHub, it's the most popular methodology plugin for AI coding agents. The Every Inc. backing (a well-known tech publication) lends it strong credibility.

### Why It Matters
Without methodology, AI agents generate massive amounts of low-quality code that accumulates technical debt faster than humans can review. Compound Engineering provides a structured workflow that turns AI agents from "fast typists" into "disciplined engineers." For teams scaling AI-assisted development, this is the difference between a codebase that gets better with age and one that becomes unmaintainable in weeks.

### Who Should Care
- Teams using Claude Code, Codex, or Cursor at scale
- Engineering leads worried about AI-generated code quality
- Developers who want agent-assisted workflows with guardrails
- Anyone who's seen an AI agent produce 500 lines of wrong code

### Execution Pattern
```bash
# Install via npx skills
npx skills add EveryInc/compound-engineering-plugin

# Or install via npm
npm install -g @every-env/compound-plugin

# In your AI coding agent, use the skills:
# /ce-brainstorm — think through a feature before coding
# /ce-plan — turn requirements into implementation plan
# /ce-work — execute the plan with worktree tracking
# /ce-code-review — multi-agent code review before merge
# /ce-compound — document learnings for future reuse
```

### Skill Potential
Yes — SKILL.md should cover: installation via npx skills and npm, skill reference, workflow integration with OpenCode/Claude Code, and team onboarding.

- **Discovered:** 2026-05-30 via GitHub Trending (credibility: 1.00)

---

## [Taste Skill](https://github.com/Leonxlnx/taste-skill)

> The Anti-Slop Frontend Framework for AI Agents — gives your AI good taste. Stops AI from generating boring, generic slop.

- **Stars:** 28,539 (↑~300/day) | **Language:** Shell | **License:** MIT
- **Last commit:** 2026-05-26
- **Source credibility weight:** 1.00 (GitHub Trending)
- **Relevance score:** 70/100

### What It Does
Taste Skill is a portable set of agent skill files that upgrade AI-built interfaces with professional-grade design: stronger layout, typography, motion, and spacing instead of boilerplate-looking UIs. It includes code-generation skills for Claude Code, Codex, and Cursor, plus image-generation skills for reference boards, brand kits, and design research. The skills enforce design quality standards — proper visual hierarchy, responsive layouts, deliberate spacing, and tasteful motion — so AI-generated frontends look like a human designer built them.

### Why Now
The biggest criticism of AI-generated UIs is that they all look the same — generic, soulless, and clearly machine-made. Taste Skill addresses this directly by encoding design principles into agent skills. At 28K stars and growing 300/day, it's clearly filling a massive need. Created February 2026, it's become the de facto standard for quality AI frontend generation with over 2K forks and active community contributions.

### Why It Matters
For solo founders and small teams shipping fast with AI coding tools, Taste Skill is the difference between a prototype that looks like a prototype and one that looks production-ready. It eliminates the "AI smell" from generated UIs — no more excessive padding, mismatched colors, or generic layouts. It's the design system that every AI coding agent should have installed by default.

### Who Should Care
- Solo founders building frontends with AI coding agents
- Developers who want AI-generated UIs that look professionally designed
- Teams using Claude Code, Codex, or Cursor for frontend work
- Anyone tired of AI-generated UIs that look like Bootstrap from 2013

### Execution Pattern
```bash
# Install via npx skills (recommended)
npx skills add Leonxlnx/taste-skill

# This installs all skills from the skills/ directory:
# - Frontend design skills (layout, typography, motion, spacing)
# - Image generation skills (reference boards, brand kits)
# Works with: Codex, Cursor, Claude Code, Cline

# For manual install, copy skills to your agent's skills folder:
cp -r skills/* ~/.codex/skills/
```

### Skill Potential
Yes — SKILL.md should cover: installation via npx skills, skill reference cards, design quality checklist, and integration with existing frontend workflows.

- **Discovered:** 2026-05-30 via GitHub Trending (credibility: 1.00)

---

## [RMUX](https://github.com/Helvesec/rmux)

> Universal Rust multiplexer for the agentic era: detachable, scriptable, and inspectable, with a tmux-compatible CLI, daemon-backed SDK, and native Ratatui integration.

- **Stars:** 1,330 (↑~88/day) | **Language:** Rust | **License:** MIT OR Apache-2.0
- **Last commit:** 2026-05-25
- **Source credibility weight:** 0.85 (GitHub Search + HN cross-reference)
- **Relevance score:** 62/100

### What It Does
RMUX is a terminal multiplexer rebuilt from scratch in Rust. Unlike tmux, it ships with a typed SDK that lets agents, scripts, and applications programmatically create, manage, and inspect terminal sessions — all 90 tmux-compatible commands are implemented with structured snapshots, persistent sessions, and native transports on Linux, macOS, and Windows (including Named Pipes). It's designed for the "agentic era": agents can spawn sessions, run commands, detach, reconnect, and inspect output — all from code.

### Why Now
Terminal multiplexers (tmux, screen) were designed for humans, not agents. As AI coding agents increasingly run on remote servers and need persistent terminal access, the lack of a typed, programmable multiplexer becomes a bottleneck. RMUX fills this gap with SDK support in Rust and Ratatui, making it the first terminal multiplexer designed for both humans and AI agents. Created May 15, 2026, it's already at 1.3K stars with 88 stars/day velocity — the community is voting with stars.

### Why It Matters
If you run AI coding agents over SSH (and most serious agent deployments do), you need persistent terminal sessions that survive disconnection. RMUX provides this with a proper SDK, not hacky tmux wrapper scripts. The typed SDK means agents can create, monitor, and orchestrate terminal sessions programmatically — enabling multi-agent orchestration, broadcast demos, browser mirroring, and agent-driven testing workflows that were previously impractical.

### Who Should Care
- DevOps engineers running AI agents over SSH
- Developers building agent orchestration systems
- Anyone using tmux who wants a modern, SDK-enabled replacement
- Teams deploying multi-agent setups that need persistent terminal sessions
- Ratatui (Rust TUI) ecosystem developers

### Execution Pattern
```bash
# Install via cargo
cargo install rmux

# Start a session (tmux-compatible)
rmux new-session -s my-agent

# From Rust SDK
use rmux::{Rmux, SessionConfig};

let rmux = Rmux::new_daemon()?;
let session = rmux.create_session(SessionConfig::new("agent-session"))?;
session.send_command("npm run build")?;
let output = session.wait_for_output()?;

# Detach and reconnect later (sessions persist on disk)
rmux detach -s my-agent
# Later:
rmux attach -t my-agent
```

### Skill Potential
Yes — SKILL.md should cover: installation, tmux-compatible CLI reference, Rust SDK usage, daemon mode, cross-platform setup (Linux/macOS/Windows), and agent orchestration patterns.

- **Discovered:** 2026-05-30 via GitHub Search + HN (credibility: 0.85)

## [Pyrefly](https://github.com/facebook/pyrefly)

> A fast type checker and language server for Python, developed by Meta. Successor to Pyre, written in Rust for performance. Supports type server protocol (TSP).

- **Stars:** 6,564 (↑~40/day) | **Language:** Rust | **License:** MIT
- **Last commit:** 2026-05-30
- **Source credibility weight:** 0.85 (Lobsters)
- **Relevance score:** 92/100

### What It Does
Pyrefly is a fast, incremental type checker and language server for Python. Created by Meta as the successor to Pyre, it's written in Rust for performance and includes advanced features like type server protocol (TSP) support. It provides real-time type checking in IDEs, catches type errors before runtime, and integrates with popular editors via LSP. Unlike gradual type checkers that allow untyped code, Pyrefly aims for soundness while maintaining usability.

### Why Now
Python's type ecosystem has matured significantly in 2024-2025, with widespread adoption of type hints in major projects. However, existing type checkers like mypy and Pyre suffer from performance issues on large codebases. Pyrefly addresses this with a Rust implementation that offers incremental checking and faster response times. Released as v1.0 in May 2026, it signals Meta's commitment to open-source Python tooling.

### Why It Matters
For teams with large Python codebases, type checking performance directly impacts developer velocity. Pyrefly's Rust engine can check millions of lines of code in seconds rather than minutes. The TSP support enables advanced IDE integrations beyond basic LSP. As a Meta-backed project, it benefits from strong engineering resources and long-term maintenance — critical for infrastructure tools.

### Who Should Care
- Teams with large Python codebases (>100K lines) frustrated by slow type checking
- Organizations adopting type hints at scale who need performant checking
- Dev tools builders creating Python IDEs or language integrations
- Anyone using Python for performance-critical applications where type safety matters

### Execution Pattern
Install via pip (`pip install pyrefly`) or use the pre-built binaries. Run as a language server in your IDE (VS Code, Neovim, etc.) for real-time feedback. For CI, run `pyrefly check` on your codebase. Configure via pyrefly.toml to adjust strictness, enable/disable specific rules, and configure incremental caching.

### Skill Potential
Yes — SKILL.md would cover: installation, IDE integration, CI configuration, rule customization, incremental caching tuning, and integration with pre-commit hooks.

- **Discovered:** 2026-05-31 via Lobsters (credibility: 0.85)

---

## [gemini-web2api](https://github.com/Sophomoresty/gemini-web2api)

> Convert Google Gemini web into an OpenAI-compatible API. Zero auth, cross-platform, single file.

- **Stars:** 870 (↑~217/day) | **Language:** Python | **License:** MIT
- **Last commit:** 2026-05-31
- **Source credibility weight:** 1.00 (GitHub Trending)
- **Relevance score:** 82/100

### What It Does
gemini-web2api is a single-file Python server that turns Google Gemini's web interface into an OpenAI-compatible API endpoint. It intercepts Gemini's web traffic, extracts the authentication tokens, and exposes a standard `/v1/chat/completions` endpoint that any OpenAI-compatible client can use. No API keys needed — it uses your Gemini web session. Supports tool calling, streaming, and works cross-platform.

### Why Now
Google Gemini's web interface is free but has no official API for personal use. gemini-web2api bridges this gap by converting the web session into a standard API. Created May 28, 2026, it's already at 870 stars with 232 forks in 3 days — explosive growth. The OpenAI-compatible format means it's a drop-in replacement for any tool that uses OpenAI's API.

### Why It Matters
This effectively gives you a free, unlimited Gemini API for personal projects. Instead of paying $0.0025/1K tokens for Gemini API or $0.03/1K for GPT-4, you get Gemini's capabilities through the web interface at zero cost. For solo devs, researchers, and hobbyists building AI tools, this eliminates the API cost barrier entirely.

### Who Should Care
- Solo developers building AI tools on a budget
- Researchers who need large-scale LLM inference without API costs
- Anyone running local AI tools that support OpenAI-compatible endpoints
- Developers prototyping with Gemini before committing to API costs

### Execution Pattern
```bash
# Install
pip install gemini-web2api

# Run the server (uses your Gemini web session)
gemini-web2api --port 8080

# Use with any OpenAI-compatible client
curl http://localhost:8080/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{"model":"gemini","messages":[{"role":"user","content":"Hello!"}]}'

# Or configure as OpenAI base URL in your tools
export OPENAI_API_BASE=http://localhost:8080/v1
```

### Skill Potential
Yes — SKILL.md should cover: installation, web session setup, OpenAI compatibility configuration, streaming support, tool calling, and integration with Hermes Agent model routing.

- **Discovered:** 2026-06-01 via GitHub Trending (credibility: 1.00)

---

## [VTCode](https://github.com/vinhnx/VTCode)

> Open-source terminal coding agent in Rust — LLM-native code understanding, shell safety, multi-provider failover.

- **Stars:** 655 (↑~47/day) | **Language:** Rust | **License:** MIT
- **Last commit:** 2026-05-31
- **Source credibility weight:** 0.85 (Hacker News)
- **Relevance score:** 64/100

### What It Does
VTCode is a terminal-based coding agent written in Rust with LLM-native code understanding. Unlike wrapper scripts around API calls, VTCode integrates deeply with your codebase through LSP, provides shell safety mechanisms (no accidental `rm -rf`), supports multiple LLM providers with automatic failover, and includes an agent skills system. Built with Ratatui/Crossterm for a polished TUI experience.

### Why Now
The terminal coding agent space is heating up (Claude Code, Codex, OpenCode, oh-my-pi), but most are Node.js-based with limited performance. VTCode brings Rust's performance and safety to the space — faster startup, lower memory usage, and native code understanding via LSP. The multi-provider failover means you're not locked into one LLM vendor. Available on crates.io for easy installation.

### Why It Matters
VTCode addresses the "one provider goes down, your workflow stops" problem with automatic failover. The shell safety mechanisms prevent common agent mistakes (deleting files, overwriting code). The Rust implementation means it's fast enough for real-time coding assistance without the overhead of Node.js. It's a serious alternative for developers who want a lightweight, reliable terminal agent.

### Who Should Care
- Terminal-first developers wanting AI coding assistance
- Developers frustrated by Node.js-based agent performance
- Teams needing multi-provider LLM failover
- Anyone concerned about agent shell safety

### Execution Pattern
```bash
# Install via cargo
cargo install vtcode

# Run in a project directory
cd /path/to/project
vtcode

# Configure providers
vtcode config set provider openai
vtcode config set fallback-provider anthropic

# Skills system
vtcode skills list
vtcode skills add my-custom-skill
```

### Skill Potential
Yes — SKILL.md should cover: installation via cargo, provider configuration, failover setup, shell safety features, skills system, and MCP/ACP integration.

- **Discovered:** 2026-06-01 via Hacker News (credibility: 0.85)


---

## [SenPaiScanner](https://github.com/MatinSenPai/SenPaiScanner)

> Lightweight Cloudflare IP scanner written in Go — find origins behind Cloudflare in seconds.

- **Stars:** 791 (↑~263/day) | **Language:** Go | **License:** MIT
- **Last commit:** 2026-05-30
- **Source credibility weight:** 1.00 (GitHub Trending)
- **Relevance score:** 66/100

### What It Does
SenPaiScanner is a fast, lightweight Go tool that scans and identifies real IP addresses behind Cloudflare-protected domains. It uses multiple techniques (DNS history, subdomain enumeration, port scanning, SSL certificate analysis) to find origin servers that Cloudflare is proxying. Useful for security researchers, penetration testers, and sysadmins who need to verify their Cloudflare configuration is not leaking origin IPs.

### Why Now
Cloudflare is the most popular CDN/proxy service, but misconfigurations frequently leak origin server IPs. SenPaiScanner makes it trivial to audit your own infrastructure. Created May 28, 2026, it is already at 791 stars with active development. The Go implementation means it is fast and cross-platform with zero dependencies.

### Why It Matters
If you are behind Cloudflare and your origin IP is leaked, Cloudflare protection is worthless. SenPaiScanner lets you verify your configuration before someone else does. For security teams, it is an essential audit tool. For sysadmins, it is a quick sanity check after DNS changes.

### Who Should Care
- Security teams auditing Cloudflare configurations
- Penetration testers doing reconnaissance
- Sysadmins managing Cloudflare-protected infrastructure
- Anyone who wants to verify their origin IP is not exposed

### Execution Pattern
```bash
# Install
go install github.com/MatinSenPai/SenPaiScanner@latest

# Scan a domain
senpaiscanner scan example.com

# Scan with verbose output
senpaiscanner scan example.com --verbose

# Scan multiple domains
senpaiscanner scan -f domains.txt
```

### Skill Potential
Yes — SKILL.md should cover: installation, scanning modes, output interpretation, integration with security audit workflows, and batch scanning patterns.

- **Discovered:** 2026-06-01 via GitHub Trending (credibility: 1.00)


---

## [HTML Anything](https://github.com/nexu-io/html-anything)

> Agentic HTML editor — your local AI agent writes the HTML, you ship it. 75 skills x 9 surfaces.

- **Stars:** 5588 (↑rapid growth) | **Language:** HTML | **License:** MIT
- **Last commit:** 2026-05-30
- **Source credibility weight:** 1.00 (GitHub Trending)
- **Relevance score:** 82/100

### What It Does
An agentic HTML editor that lets local AI agents (Claude Code, Cursor, Codex, OpenCode, etc.) generate and edit HTML directly. Supports 75 skills across 9 output surfaces: magazine layouts, slide decks, posters, social media cards (XHS/tweet), prototypes, data reports, and Hyperframes. Sandboxed preview, 1-click publish to WeChat/X/Zhihu/HTML/PNG. Zero API keys needed — works with any local AI tool.

### Why Now
The vibecoding movement has created demand for tools that let AI agents produce visual output directly. HTML Anything bridges the gap between AI code generation and visual publishing. The multi-surface approach (social cards, decks, reports) makes it useful beyond just web pages.

### Why It Matters
This turns AI agents into visual content creators. Instead of generating code that needs manual wrapping, agents can produce ready-to-ship HTML artifacts. The zero-API-key requirement means it works entirely locally with any AI tool.

### Who Should Care
Content creators using AI for visual output, developers building AI-powered design tools, teams needing rapid prototyping, anyone wanting AI to produce polished HTML instead of raw code.

### Execution Pattern
Install as a Claude Code/Codex skill, point at your AI agent, describe what you want. The agent generates HTML using the appropriate skill (e.g., social-card for tweet images, deck for presentations). Preview in sandbox, then publish with one click.

### Skill Potential
Yes — SKILL.md would cover: skill selection for different surfaces, integration with Claude Code/Codex, preview workflow, publish pipeline.

- **Discovered:** 2026-06-01 via GitHub Trending (credibility: 1.00)


---

## [Garnix CI](https://github.com/garnix-io/garnix-ci)

> CI and hosting for nix-based, flakified GitHub repos — self-hostable Nix CI service

- **Stars:** 362 (↑growing) | **Language:** Haskell | **License:** AGPL-3.0
- **Last commit:** 2026-05-27
- **Source credibility weight:** 1.00 (GitHub Trending)
- **Relevance score:** 72/100

### What It Does
A CI service specifically designed for Nix flake-based GitHub repos. Builds Nix flakes, runs tests, and hosts build artifacts. Self-hostable via nixos-compose VMs. Includes a GitHub App integration for automated builds on push/PR. The admin interface shows build status and logs.

### Why Now
Nix adoption is accelerating, but CI for Nix flakes remains painful. GitHub Actions requires complex workarounds for Nix caching. Garnix provides native Nix CI with proper flake support, making it the missing piece for Nix-first development workflows.

### Why It Matters
For teams adopting Nix, Garnix eliminates the CI friction. Instead of fighting GitHub Actions cache configuration, you get native flake builds with proper dependency resolution. The self-hostable option means you can run it on your own infrastructure.

### Who Should Care
Nix developers and teams, DevOps engineers adopting NixOS, open source projects using Nix flakes, anyone tired of GitHub Actions Nix workarounds.

### Execution Pattern
Install the Garnix GitHub App on your repo, push a Nix flake, Garnix builds it automatically. For self-hosting, run nixos-compose to spin up VMs, configure the GitHub App, and point your repos at your Garnix instance.

### Skill Potential
No — this is a hosted/self-hosted service, not a CLI tool with automation potential.

- **Discovered:** 2026-06-01 via GitHub Trending (credibility: 1.00)


---

## [duckle](https://github.com/SouravRoy-ETL/duckle)

> Local-first ETL/ELT studio: drag-and-drop visual pipeline designer that compiles to SQL on DuckDB

- **Stars:** 165 (↑growing) | **Language:** Rust | **License:** MIT
- **Last commit:** 2026-05-27
- **Source credibility weight:** 1.00 (GitHub Trending)
- **Relevance score:** 71/100

### What It Does
A local-first ETL/ELT studio with a drag-and-drop visual pipeline designer. Design data transformation pipelines visually, then compile them to SQL and run on DuckDB. Tiny desktop app, no servers, git-friendly workspaces. Combines the visual ease of tools like dbt with the local-first philosophy of DuckDB.

### Why Now
Data teams are moving toward local-first analytics with DuckDB, but lack visual pipeline tools that work offline. Duckle fills this gap by providing a visual designer that compiles to DuckDB SQL, keeping everything local and git-friendly.

### Why It Matters
This eliminates the need for cloud ETL services (Fivetran, Airbyte) for small-to-medium datasets. The visual designer makes pipeline creation accessible to non-SQL users, while the SQL compilation ensures transparency and debuggability.

### Who Should Care
Data analysts using DuckDB, teams building local data pipelines, anyone wanting visual ETL without cloud dependencies, developers building data-intensive applications.

### Execution Pattern
Download the desktop app, connect to DuckDB databases, drag-and-drop to build transformation pipelines, compile to SQL, run locally. Export pipeline definitions as git-friendly files for version control.

### Skill Potential
No — this is a desktop GUI app, not a CLI with automation potential.

- **Discovered:** 2026-06-01 via GitHub Trending (credibility: 1.00)


---

## [vibecode-pro-max-kit](https://github.com/withkynam/vibecode-pro-max-kit)

> Spec-driven coding harness for vibecoders — self-improving context memory, 12 agents, 32 skills. Works with Claude Code and Codex.

- **Stars:** 780 | **Language:** JavaScript | **License:** MIT
- **Last commit:** 2026-06-05
- **Source credibility weight:** 1.00 (GitHub trending discovery)
- **Relevance score:** 70/100

### What It Does
vibecode-pro-max-kit reframes agent coding around specs and memory, not raw prompts. It gives a team of agents persistent project context and a reusable skill library so build quality compounds over time instead of degrading.

### Why Now
Vibe coding is shifting from vibes-only to spec-plus-memory-driven execution. This harness mirrors that shift, and 780 stars shows early adoption.

### Why It Matters
It treats agent context as infrastructure, not an accident. That makes agent-produced codebases coherent at scale.

### Who Should Care
- Product and eng leads prototyping with agents
- Claude Code/Codex users burning context on each session
- Teams who want agentizable product specs
- AI-native startups

### Execution Pattern
```bash
# Use as a harness during Claude Code or Codex sessions
npx vibecode-pro-max-kit@latest
# Load spec + agent roster, then iterate
```

### Skill Potential
Yes — spec workflow, harness lifecycle, skill extension, and quickstart for Claude Code / Codex.

- **Discovered:** 2026-06-05 via GitHub trending discovery (credibility: 1.00)
