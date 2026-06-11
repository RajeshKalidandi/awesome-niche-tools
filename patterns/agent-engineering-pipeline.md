# Stack: Agent Engineering Pipeline

## Stack: Agent Engineering Pipeline

**Components:** [Agent Skills](https://github.com/addyosmani/agent-skills) + [Superpowers](https://github.com/obra/superpowers) + [hivemind](https://github.com/activeloopai/hivemind)

**What it enables:** A complete autonomous software development pipeline where AI agents follow structured engineering practices, use subagent-driven development, and coordinate across multiple specialized agents.

**Why it's composable:**
- Agent Skills provides the lifecycle commands (/spec, /plan, /build, /test, /review, /ship)
- Superpowers adds the subagent-driven development methodology and autonomous execution
- hivemind provides the multi-agent coordination layer for parallel workstreams

The pieces connect through shared skill file formats and agent platform APIs. Agent Skills defines *what* to do at each stage, Superpowers defines *how* to execute autonomously, and hivemind defines *how* agents coordinate.

**Execution pattern:**
1. Install Agent Skills for structured lifecycle commands
2. Install Superpowers for autonomous execution methodology
3. Configure hivemind for multi-agent coordination
4. Use `/spec` to define requirements
5. Use `/plan` to break into atomic tasks
6. Use `/build auto` with hivemind for parallel autonomous implementation
7. Use `/test` and `/review` for quality verification
8. Use `/ship` for deployment

This stack transforms a single coding agent into a structured engineering team with clear processes, quality gates, and parallel execution capabilities.
