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
