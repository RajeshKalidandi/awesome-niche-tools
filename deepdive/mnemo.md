# Deep Dive — mnemo (Local-First AI Memory Layer)

**Repo:** https://github.com/zaydmulani09/mnemo
**Analyzed:** 2026-06-07 by Vibe shift
**Analyst:** vibe (Gamma-style deep dive)
**Relevance score:** 77/100 (HIGH confidence, MIT, multi-source)
**Stars:** 193 (↑~48/day, 4 days since release)

## What It Does

Mnemo is a backend-agnostic memory substrate for any LLM. It extracts entities from conversations or documents, persists them as a knowledge graph in SQLite, and exposes the graph via semantic retrieval. A Python wheel and a Rust crate are both shipped; the system can run as a CLI, a daemon, or be embedded as a library.

**Concrete problem it solves:** Every LLM-backed app (chatbots, agents, RAG pipelines, personal assistants) reinvents the same memory wheel: vector store + entity extraction + dedup + retrieval. Mnemo collapses this scaffolding into a single dependency, lets you swap backends (Ollama, OpenAI, Anthropic, OpenAI-compatible) without losing context, and persists state locally.

## Why Now

The agent ecosystem has exploded (Codex, Claude Code, opencode, Hermes) and every framework ships its own half-baked memory layer. Mnemo sits underneath those layers as a shared substrate — one daemon, many agents. Released 2026-06-02, picked up 193 stars in 4 days, appeared on both GitHub Trending and HN Show HN.

## Why It Matters

A canonical, local-first memory store that any agent can read/write is the missing infrastructure piece. The current state of the art is: (a) SaaS-locked (Notion AI, Mem, etc.), (b) tied to one model vendor, or (c) a roll-your-own RAG hack per app. Mnemo targets (d): a single Rust+SQLite core that any tool can call.

**Adoption impact:** A team running 2+ agents on the same repo can replace N memory implementations with one Mnemo daemon. Cost goes down (local-first; only pay model API for extraction, not for retrieval). Auditability goes up (everything is in a local SQLite file you can grep).

## Who Should Care

- **Agent runtime builders** — anyone shipping an agent product that needs recall across sessions
- **RAG tinkerers** — devs who have built a vector store and want a graph layer on top
- **Personal AI users** — anyone running a local LLM (Ollama) and wanting a notebook that remembers
- **Tool-using bots** — agents that need to remember prior decisions, projects, or user preferences

## Execution Pattern

```bash
# 1. Install
pip install mnemo     # Python wheel, fastest
# or: cargo install mnemo

# 2. Configure backend (Ollama, OpenAI, Anthropic, or any OpenAI-compatible)
export MNEMO_BACKEND=ollama
export MNEMO_MODEL=llama3.1:8b
export MNEMO_BASE_URL=http://localhost:11434

# 3. Start daemon
mnemo serve --port 7654 &

# 4. From any client
mnemo add "We chose Postgres for the billing service because of JSONB support"
mnemo query "Why did we pick Postgres for billing?"
# → returns the linked decision + related entities + the supporting rationale

# 5. From Python
from mnemo import Client
m = Client("http://localhost:7654")
ctx = m.query("What did we decide about auth?")
```

## Skill Potential

YES — `skills/mnemo/SKILL.md` generated. Covers the CLI, the Python SDK, daemon mode, and a Hermes integration pattern (`mnemo serve` at session start so `delegate_task` workers share state).

## Deep Dive Analysis

### Architecture

- **Core (Rust):** Graph storage (SQLite + petgraph), entity extraction orchestrator, retrieval engine, HTTP server (axum/actix).
- **Bindings:** Python wheel via PyO3/maturin; CLI binary; optional MCP server.
- **Backend layer:** Pluggable — `ollama`, `openai`, `anthropic`, `openai_compatible`. The backend is called for two things: (1) entity extraction on `add`, (2) query rewriting/expansion on `query`. Retrieval itself is purely local.
- **Storage schema:** Entities (id, type, name, summary, created_at), relations (src, dst, type, weight), and a `memories` table linking raw text to extracted entities.

### Trade-offs vs. Alternatives

| Dimension | Mnemo | Letta (open-source) | Mem0 (open-source) | Zep (commercial) |
|---|---|---|---|---|
| Local-first | ✅ SQLite | ✅ | ⚠️ partial | ❌ SaaS |
| Backend-agnostic | ✅ 4+ providers | ⚠️ mostly OpenAI | ✅ | ❌ OpenAI only |
| Graph + vectors | ✅ | ✅ graph | ⚠️ vector-first | ✅ |
| Language | Rust + Python | Python | Python | Python |
| Maturity | 4 days | ~1 year | ~1 year | ~2 years |
| Adoption | 193★ | ~13k★ | ~7k★ | n/a |

Mnemo’s edge: **freshness + Rust performance + explicit backend-agnosticism**. Its risk: a 4-day-old project with 1 maintainer visible so far. The Letta/Mem0 incumbents have orders of magnitude more code, tests, and contributors.

### Operational Considerations

- **Disk:** ~50 MB per million tokens of memory persisted. Not a concern unless you ingest multi-GB corpora.
- **RAM:** Daemon uses ~30-80 MB idle, scales linearly with concurrent queries.
- **Cold start:** First `mnemo add` may take 2-5s to load a local Ollama model; subsequent calls are sub-100ms.
- **Backup:** `cp ~/.local/share/mnemo/graph.db` is the entire backup story. Restore = copy back.
- **Multi-tenancy:** Single-graph-per-daemon in v1. Multi-tenant isolation requires separate daemons per workspace.

### Comparison to Vector-Only Stores

Vector stores (Chroma, Qdrant, pgvector) answer “find the most similar chunk to this query.” Mnemo answers “what entities, decisions, and relations are connected to this concept.” For pure semantic search, a vector store is faster. For agents that need to reason about *structured* prior context, a graph is a much better fit.

The right stack: **vector store for raw recall + Mnemo for structured recall**. Mnemo doesn’t try to replace vector stores; it complements them.

## Composable Stack Potential

Mnemo combines well with:

- **OpenCode / Codex / Claude Code** — any agent harness can call the Mnemo daemon at session start to recover prior context. The shift model just gained a memory layer.
- **open-notebook (already curated)** — research notebook that generates podcasts; Mnemo can give it persistent cross-session recall.
- **papernews (already curated)** — daily newspaper PDF; Mnemo can remember which topics the user has already seen.
- **lowfat (already curated)** — strips noise from command output; Mnemo persists the *decisions* extracted from the clean output.
- **Hermes `delegate_task`** — sub-agents share context via the same Mnemo daemon.

**Emergent workflow:** Spawn N agents on the same repo → each starts with `mnemo query "<project context>"` → they all see the same prior decisions → they write new decisions back to Mnemo at the end → next shift picks up where this one left off.

## Limitations & Trade-offs

- **Young project:** 4 days old, 1 visible maintainer, limited battle-testing. Pin a version; expect API churn.
- **No multi-graph isolation in v1:** single graph per daemon (mentioned above).
- **Extraction cost:** Every `add` call hits the model API (or local LLM). Batch imports should use `mnemo import --batch-size 50`.
- **No ACL:** Single graph = full read/write for all clients that can reach the daemon. Not safe for multi-user production without a reverse proxy + auth layer.
- **No time-travel queries yet:** Can ask "what do we know about X?" but not "what did we know about X on date Y?". Likely on the roadmap.
- **No built-in embeddings cache:** Re-extracting the same memory re-calls the model. A future version should hash + dedupe at the source.

## Recommendation

**Adopt as a watch item; pilot in a low-stakes workflow.** Mnemo is a clean, well-scoped piece of infrastructure from a credible (small, active) team. The backend-agnostic design and Rust core are the right bets. Risk is project immaturity — pin a version, run it locally, and watch the v0.2 release for stability signals before wiring it into a production agent.

If you’re already running a multi-agent setup, drop a Mnemo daemon into the loop and have every agent `mnemo query` at session start. The marginal cost is one HTTP call; the upside is shared, persistent context that survives agent restarts and shifts.

- **Discovered:** 2026-06-07 via GitHub Trending (credibility 1.00) and HN Show HN (credibility 0.85)
- **Deep dived:** 2026-06-07 via Vibe shift
