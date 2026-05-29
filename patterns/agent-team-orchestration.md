# Pattern: Agent Team Orchestration

> Design specialized agents with clear roles, then coordinate them through an orchestrator.

## Problem
Single agents hit cognitive limits — they try to do everything and excel at nothing. As tasks grow complex (multi-file refactors, research synthesis, content production), the quality degrades. Teams of specialized agents outperform generalists, but coordinating them is hard.

## Solution
Define agent teams with:
1. **Specialized agents** — each with a focused role and expertise
2. **An orchestrator** — chains agents, manages data flow, handles errors
3. **Communication protocols** — message-based, task-based, or file-based passing
4. **Architecture patterns** — Pipeline, Fan-out/Fan-in, Expert Pool, Producer-Reviewer, Supervisor, Hierarchical

The key insight: agent team design is itself a skill that can be automated. Tools like harness generate entire team architectures from a domain description.

## When to Use
- Tasks requiring multiple expertise areas (research + writing + review)
- Workflows with clear sequential stages (Pipeline pattern)
- Parallel analysis from different angles (Fan-out/Fan-in)
- Quality-critical output requiring review (Producer-Reviewer)
- Complex problems with natural decomposition (Hierarchical)

## When NOT to Use
- Simple tasks a single agent handles well
- When inter-agent communication overhead exceeds the benefit
- When the problem domain is too fuzzy to define clear agent roles
- When latency requirements don't allow multi-agent coordination

## Discovered From
- **harness** — meta-skill generating agent team architectures (6 patterns, 3 execution modes)
- **oh-my-pi** — terminal agent with sub-agent spawning
- **OpenGap** — portable agent definition format
- **Uni-CLI** — operations substrate with policy enforcement

## Variants
- **Pipeline**: A → B → C → D (sequential, dependent)
- **Fan-out/Fan-in**: Parallel collection → merge (research, code review)
- **Expert Pool**: Router selects specialist (input-dependent)
- **Producer-Reviewer**: Generator + quality checker (content production)
- **Supervisor**: Central agent assigns tasks dynamically (variable workloads)
- **Hierarchical**: Top-down recursive decomposition (max 2 levels)

## Metrics
- harness claims +60% average quality improvement (49.5 → 79.3) with agent teams
- 15/15 task win rate in A/B testing
- -32% output variance (more consistent results)
- 5 architecture patterns cover 90% of use cases
