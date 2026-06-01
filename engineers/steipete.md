# Peter Steinberger (@steipete)

> **Focus:** AI agent infrastructure, CLI tools, macOS utilities, security, observability
> **GitHub:** [@steipete](https://github.com/steipete) | **Website:** [steipete.me](https://steipete.me)
> **Status:** 🔥 **ACTIVE WATCH** — 9 new public repos in 30 days, ~30K cumulative stars
> **Last updated:** 2026-06-01

---

## Why Follow

Steinberger is the most prolific AI tooling engineer shipping in public right now. His repos consistently exhibit three patterns:

1. **Single-purpose CLI utilities** that solve one annoying problem extremely well (ghx, osc-progress, stats-store, agent-scripts, wacrawl)
2. **Agent architecture primitives** — not framework opinions, but actual building blocks (oracle, symphony, deepsec, pi-skills, oracle-skills)
3. **Developer observability** — usage meters, cost trackers, release dashboards (CodexBar, ReleaseBar, tokentally, stats-store)

If you're building AI agents or agent infrastructure, his repos are a free library of working patterns.

---

## Notable Repos (curated)

### Agent Infrastructure
- **[oracle](https://github.com/steipete/oracle)** (⭐ 2.3K) — Invoke GPT-5 Pro with custom context when stuck. The "ask a stronger model" pattern, as a tool.
- **[symphony](https://github.com/steipete/symphony)** — Isolated autonomous implementation runs (fork of OpenAI Codex). Pattern: run multiple agent implementations in parallel worktrees.
- **[deepsec](https://github.com/steipete/deepsec)** — Security harness for coding agents. Pattern: hook-based policy enforcement.
- **[oracle-skills](https://github.com/steipete/oracle-skills)** + **[pi-skills](https://github.com/steipete/pi-skills)** — Portable skill files for pi/Claude Code/Codex CLI agents.
- **[agent-scripts](https://github.com/steipete/agent-scripts)** (⭐ 4K) — Shared scripts for agents, used across his repos. Pattern: avoid reinventing the same agent glue in every project.
- **[wacrawl](https://github.com/steipete/wacrawl)** — WhatsApp chat archive crawler in Go. Pattern: declarative data extraction from closed platforms.

### CLI Utilities
- **[summarize](https://github.com/steipete/summarize)** (⭐ 6.1K) — Point at any URL/YouTube/Podcast/file. Get the gist. CLI + Chrome extension. Pattern: universal summarization, multiple input types.
- **[ghx](https://github.com/steipete/ghx)** — GitHub CLI Cache Proxy. Solves the 5,000 req/hour pain point when doing bulk operations. Pattern: cache + rate-limit relief for agent use.
- **[fluegel](https://github.com/steipete/fluegel)** — Mac app for elevated CLI permissions without sudo. Pattern: agent security boundary.
- **[osc-progress](https://github.com/steipete/osc-progress)** — Tiny lib for OSC 9;4 terminal progress. Pattern: native terminal features for long-running agent tasks.
- **[tokentally](https://github.com/steipete/tokentally)** — One tiny lib for LLM token + cost math. Pattern: cost estimation at the tool layer.
- **[homebrew-tap](https://github.com/steipete/homebrew-tap)** — Homebrew tap for his tools. Pattern: single distribution channel for personal CLI suite.

### Observability / Desktop
- **[CodexBar](https://github.com/steipete/CodexBar)** (⭐ 13.9K) — Show usage stats for OpenAI Codex and Claude Code without logging in. Swift macOS menu bar. Massive adoption.
- **[ReleaseBar](https://github.com/steipete/ReleaseBar)** — Release freshness dashboard for OSS maintainers. Pattern: keep your shipped dependencies from going stale.
- **[stats-store](https://github.com/steipete/stats-store)** — Fast, open, privacy-first analytics for Sparkle (the macOS update framework).

### Local Inference
- **[ds4](https://github.com/steipete/ds4)** — DeepSeek 4 Flash local inference (Metal/CUDA). Pattern: escape the API for cost/sensitive workloads.

---

## Recurring Patterns in His Work

| Pattern | What | Where Seen |
|---------|------|------------|
| **Single-binary CLI** | Tools that ship as one file, install via curl, no dependencies | ghx, osc-progress, tokentally, summarize |
| **Model escalation** | When stuck, ask a stronger model with full context | oracle |
| **Skill portability** | Skills that work across pi/Claude Code/Codex | pi-skills, oracle-skills, agent-scripts |
| **Privacy-first telemetry** | Local-first, no required backend | stats-store, CodexBar |
| **Hook-based policy** | Agent security as middleware, not wrapper | deepsec |
| **Cost visibility** | Always know what you're spending | tokentally, CodexBar |
| **Release freshness** | Track what's outdated in your deps | ReleaseBar |

---

## What to Curate From This Engineer

- **Track `agent-scripts`** for new shared patterns — anything added there gets reused across his other projects
- **Watch for new "oracle-*" repos** — pattern family for model escalation
- **Watch for new "*-bar" macOS apps** — observability pattern
- **Watch pi-skills / oracle-skills updates** — those become de facto standards in the Hermes skill ecosystem

---

## Recent Activity (last 30 days)

| Date | Repo | Type | Notes |
|------|------|------|-------|
| 2026-05-30 | [agent-scripts](https://github.com/steipete/agent-scripts) | updated | Active maintenance |
| 2026-05-30 | [CodexBar](https://github.com/steipete/CodexBar) | updated | v13.9K stars, active |
| 2026-05-30 | [ReleaseBar](https://github.com/steipete/ReleaseBar) | new release | v0.x, dashboard |
| 2026-05-29 | [tokentally](https://github.com/steipete/tokentally) | updated | Token math lib |
| 2026-05-29 | [osc-progress](https://github.com/steipete/osc-progress) | updated | OSC 9;4 lib |
| 2026-05-24 | [oracle](https://github.com/steipete/oracle) | new | 2.3K stars in 7 days |
| 2026-05-23 | [ds4](https://github.com/steipete/ds4) | new | Local DeepSeek |
| 2026-05-20 | [fluegel](https://github.com/steipete/fluegel) | new | Elevated CLI perms |
| 2026-05-17 | [deepsec](https://github.com/steipete/deepsec) | new | Agent security |
| 2026-05-14 | [ReleaseBar](https://github.com/steipete/ReleaseBar) | new | Release dashboard |

**Velocity:** ~9 new repos in 30 days. **Pattern density:** Very high — almost every repo introduces or refines a reusable pattern.

---

## Notes

- Steinberger is **@steipete on GitHub** (Peter Steinberger, ex-PSPDFKit founder)
- The orphan `memory/inputs/steipete_repos.json` (78KB) is the raw GitHub API snapshot used to build this profile
- Profile auto-regenerates weekly from GitHub API
