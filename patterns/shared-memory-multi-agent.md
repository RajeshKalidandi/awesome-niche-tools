# Pattern: Shared-Memory Multi-Agent Stack

**Components:** [mnemo](https://github.com/zaydmulani09/mnemo) + [opencode](https://github.com/sst/opencode) + [claude-code](https://docs.anthropic.com/en/docs/claude-code) + [ai-rules-sync](https://github.com/PanisHandsome/ai-rules-sync) + [lowfat](https://github.com/zdk/lowfat)

**What it enables:** A multi-agent team (any mix of Codex, Claude Code, opencode, Hermes workers) running on the same repo, all sharing (a) one canonical rules file and (b) one persistent memory layer across sessions and shifts.

**Why it's composable:**

- `ai-rules-sync` is the **source-of-truth** layer. You write standards once in `AGENTS.md` and `agentsync sync` fans them out to CLAUDE.md, .cursorrules, copilot-instructions.md, etc. Every agent reads the same rules without drift.
- `mnemo serve` is the **memory layer**. A single daemon (Rust + SQLite) running on a known port. Any agent can `mnemo query "<context>"` at session start to recover prior decisions, and `mnemo add "<decision>"` at session end to persist new ones.
- `lowfat` is the **signal layer**. When an agent pipes command output back to its own context, `lowfat` strips noise (saving 90%+ of LLM tokens). The clean output is what gets persisted to Mnemo.
- The agent harnesses (opencode, claude-code, codex) are the **execution layer**. Each one can be configured to (a) read `AGENTS.md` (or its synced equivalent) and (b) call the Mnemo daemon at start/end of session.

**Execution pattern:**

```bash
# 1. Bootstrap (once per workspace)
npx @panishandsome/agentsync init        # canonical AGENTS.md
npx @panishandsome/agentsync sync        # fan out to all agents
mnemo serve --port 7654 &                 # start the memory daemon
echo $! > /tmp/mnemo.pid

# 2. In every agent's bootstrap prompt
cat AGENTS.md                             # load canonical rules
mnemo query "prior decisions on this project"   # recover context

# 3. Wrap noisy commands in lowfat
mnemo add "$(some-noisy-command | lowfat)"  # persist only the signal

# 4. At session end
mnemo add "shift 2026-06-07 decided to use Postgres for billing"
```

**Emergent value:**

- **Drift-free standards** — `agentsync` + a pre-commit hook means `AGENTS.md` is the only file anyone edits; the rest regenerate.
- **Cross-agent context** — a Claude Code shift and a Codex shift running on the same repo see the same prior decisions. No more "wait, didn't we already decide that?".
- **Token efficiency at scale** — `lowfat` keeps the memory layer from filling with command-output noise.
- **Auditability** — every decision is a row in `~/.local/share/mnemo/graph.db`. `sqlite3` + `grep` is the entire audit trail.

**Failure modes:**

- Mnemo daemon down → agents start blind. Wrap in a systemd unit or a cron-supervised process.
- `AGENTS.md` and `CLAUDE.md` drift between `sync` runs → add `agentsync diff` to CI.
- A noisy `lowfat` config strips signal you actually wanted → tune the noise threshold; the default is conservative.

**When to deploy this stack:**

- ✅ 2+ agents running on the same repo (any combination of Claude Code, Codex, opencode, custom Hermes workers)
- ✅ Team that has been bitten by agents giving different answers to the same question
- ✅ Long-running shift work where context survives across cron runs
- ❌ Single-agent, single-session workflows — overkill
- ❌ Greenfield projects with no prior decisions to remember
