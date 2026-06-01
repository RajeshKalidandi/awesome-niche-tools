# 🧩 Execution Patterns

> Reusable workflow patterns discovered through autonomous agent operations.

People love patterns more than tools. A good pattern is worth 100 tool links.

## Pattern Format

```markdown
# Pattern: {name}

> One-line description

## Problem
[What situation does this solve?]

## Solution
[The concrete pattern — steps, architecture, decision rules]

## When to Use
- [Condition 1]
- [Condition 2]

## When NOT to Use
- [Anti-pattern 1]
- [Anti-pattern 2]

## Discovered From
[Which tools, which shifts, which real operations revealed this pattern]

## Variants
[Alternative approaches or modifications]
```

## Current Patterns

| Pattern | Category | Discovered | Impact |
|---------|----------|------------|--------|
| [MCP-First Integration](mcp-first-integration.md) | Agent Orchestration | Week 22 | 32% of tools ship MCP servers |
| [Single-Binary Distribution](single-binary-distribution.md) | Distribution | Week 22 | 21% of tools use Go/Rust binaries |
| [Token Economy Layer](token-economy-layer.md) | Signal Processing | Week 22 | 60-95% token reduction |
| [Agent Team Orchestration](agent-team-orchestration.md) | Agent Orchestration | Week 22 | +60% quality improvement |
| [Privacy-First Self-Hosting](privacy-first-self-hosting.md) | Distribution | Week 22 | 21% of tools are self-hostable |
| [WiFi/RF Sensing](wifi-rf-sensing.md) | Research Pipelines | Week 22 | New sensing modality |
|| [Model Escalation (Oracle)](model-escalation-oracle.md) | Agent Orchestration | Week 22 | 70-80% cost reduction |
| [Dynamic Workflow Orchestration](dynamic-workflow-orchestration.md) | Agent Orchestration | Week 23 | Model-generated parallel workflows |
| [Pipeline Unification](pipeline-unification.md) | Workflow Engineering | Week 23 | Single CLI replaces fragmented tool chains |
| [Composable Stacks](composable-stacks.md) | Agent Orchestration | Week 23 | Tool combinations create emergent value |

## Categories

- **Agent Orchestration** — multi-agent coordination, isolation, scheduling
- **Research Pipelines** — crawling, scoring, filtering, curation
- **Distribution** — repo-first publishing, skill ecosystems
- **Rate Management** — cooldowns, shift models, backoff strategies
- **Signal Processing** — decay, freshness, credibility weighting
