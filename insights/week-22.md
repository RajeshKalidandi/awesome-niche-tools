# 📊 Insights — Week 22 (May 23-29, 2026)

> Auto-generated analysis from the Gamma analyst shift.

## 📈 Top Emerging Patterns

### 1. MCP Is the New USB
The single most dominant pattern this week: **32% of curated tools now ship MCP servers as first-class interfaces**. This isn't a trend — it's a standard forming in real-time. Tools that don't ship MCP are becoming invisible to the agent ecosystem.

**Key insight:** MCP servers are no longer optional for tools targeting AI agents. They're the integration layer that determines whether your tool gets adopted or ignored.

### 2. Token Economics Is the New Performance Optimization
Six tools (21%) address token economy — compressing, caching, indexing, and optimizing every token before it reaches the LLM. Headroom's 60-95% compression ratios aren't marginal improvements; they're order-of-magnitude cost reductions that change what's economically viable.

**Key insight:** The bottleneck has shifted from "can the model do this?" to "can we afford to ask the model to do this?" Token economy tools are the infrastructure layer that makes agent deployments practical.

### 3. Agent Teams Replace Agent Swarms
harness's meta-skill approach — designing specialized agent teams with clear roles — is producing measurable results: +60% quality, 15/15 win rate, -32% variance. The era of "one agent does everything" is ending.

**Key insight:** Agent team design is itself a skill that can be automated. The harness pattern (domain description → team architecture → specialized agents → orchestrator) is becoming the standard approach for complex AI workflows.

### 4. WiFi Sensing Goes Mainstream
RuView's 67K stars and 4,690/week growth rate signals a paradigm shift: spatial intelligence without cameras. The hardware cost ($140 for ESP32-S3) makes this accessible to hobbyists, while the Home Assistant integration makes it practical for smart homes.

**Key insight:** Every building with WiFi already has the hardware for spatial intelligence. This is a software upgrade to existing infrastructure, not a new hardware deployment.

## 🚀 Fastest Growing Agent Repos

| Repo | Stars | Growth | Signal |
|------|------:|-------:|--------|
| RuView | 67,534 | +4,690/week | 🔥 WiFi spatial intelligence — paradigm shift |
| Understand-Anything | 42,616 | +3,766/day | 🔥 Code knowledge graphs — onboarding revolution |
| Codegraph | 31,570 | +180/week | 📈 Pre-indexed code graphs for agents |
| heretic | 22,294 | +500/day | 🔥 Censorship removal — massive demand signal |
| stop-slop | 6,358 | +755/day | 🔥 Human voice for AI writing |
| LiteParse | 6,471 | +200/day | 📈 Document parsing bottleneck solver |
| presenton | 7,300 | +1,740/week | 🔥 Open-source presentation AI |
| harness | 3,962 | +190/week | 📈 Agent team architecture factory |

## 🧩 Most Repeated Execution Architectures

### Architecture 1: MCP Server + CLI + Library
**Used by:** Headroom, Crawl4AI, mcp2cli, Design-Extract
**Pattern:** Ship the same tool as MCP server (for agents), CLI (for shell scripts), and library (for apps). Three interfaces, one codebase.

### Architecture 2: Single Binary + Config File
**Used by:** Engram, Codebase Memory MCP, Moltis, Posthorn
**Pattern:** Go/Rust binary + TOML/YAML config. Zero dependencies, instant install, works everywhere.

### Architecture 3: Index → Query → Serve
**Used by:** Codebase Memory MCP, ContextPlus, Codegraph, Understand-Anything
**Pattern:** Pre-index codebase into knowledge graph → query on demand → expose via MCP. Build once, query many times.

### Architecture 4: Local Inference + MCP Bridge
**Used by:** A-Eye (Ollama), Dograh (BYOK), RuView (ESP32)
**Pattern:** Run inference locally → expose via MCP/REST → integrate with agent frameworks. Privacy-first, cost-effective.

## 📋 Most Adopted SKILL.md Patterns

| Skill | Category | Adoption Signal |
|-------|----------|----------------|
| crawl4ai | Dev Tools | High — web crawling is universal need |
| headroom | Dev Tools | High — token costs affect everyone |
| agent-governance | AI Agents | Growing — security becoming priority |
| codebase-memory-mcp | Dev Tools | Growing — code understanding is critical |
| dograh | AI Agents | Niche — voice AI is specialized |
| liteparse | Dev Tools | Growing — document parsing is bottleneck |

## 🔍 Signal Quality Report

- **Tools curated:** 28 (across 2 Alpha/Beta shifts + Gamma analysis)
- **Average relevance score:** 77/100
- **Confidence distribution:** 20 HIGH / 8 MEDIUM / 0 LOW
- **Average novelty:** 72/100
- **Dead repos filtered:** 0 (all curated tools are active)
- **Signal-to-noise ratio:** 4.7:1 (28 curated from ~130 evaluated)
- **Sources with highest yield:** GitHub Trending (12 tools), GitHub Search (10 tools), Hacker News (6 tools)

## 🎯 Recommendation

**Pay attention to three things this week:**

1. **Token Economy Tools** — Headroom, Codebase Memory MCP, and ContextPlus are solving the #1 bottleneck for AI agent deployments. If you're running agents, you need a token compression strategy. The 60-95% savings are not optional — they're the difference between "works in demo" and "works in production."

2. **Agent Team Architecture** — harness's meta-skill approach is producing measurable quality improvements. The era of single generalist agents is ending. If you're building complex AI workflows, design specialized agent teams with clear roles and an orchestrator.

3. **WiFi Sensing** — RuView's 67K stars signal massive interest in camera-free spatial intelligence. The $140 hardware cost makes this accessible. If you're in smart home, healthcare, or security, this is worth evaluating now.

**Anti-recommendation:** Don't chase the heretic (censorship removal) trend. It's a signal of demand, not a tool you should build on. The AGPL-3.0 license and ethical implications make it risky for production use.

---

*Generated by Gamma analyst shift — 2026-05-29*
*Next shift: Beta will discover new tools, Gamma will analyze patterns*
