# Pattern: Dynamic Workflow Orchestration

> Enable language models to generate and execute parallel workflow scripts that spawn isolated subagents for fan-out patterns.

## Problem
Complex tasks like codebase analysis, research synthesis, and large refactoring benefit from parallel execution, but manually orchestrating multiple agents is error-prone and difficult to scale. Single agents hit cognitive limits when trying to handle multifaceted problems requiring different expertise or perspectives.

## Solution
Create a framework where:
1. The language model generates workflow scripts in a sandboxed language (JavaScript/TypeScript)
2. Workflow scripts define metadata, spawn isolated subagents via `agent()` tool
3. Execute work in parallel using `parallel()` or `pipeline()` utilities
4. Track progress with `phase()` calls for live feedback
5. Automatically synthesize results from parallel subagents
6. Manage token budgets to prevent runaway costs
7. Handle individual subagent failures without halting entire workflow

The key insight is inverting control: instead of the orchestrator defining the workflow structure, the LLM generates the workflow script itself based on the task description.

## When to Use
- Tasks requiring analysis from multiple angles (codebase audits, comparative studies)
- Research synthesis needing parallel source exploration
- Large refactors decomposable into independent module changes
- Batch processing where each item can be processed independently
- Fan-out scenarios: one input → many parallel processes → synthesized output
- When task complexity exceeds single-agent cognitive capacity
- Need for transparent progress tracking during long-running operations

## When NOT to Use
- Simple sequential tasks with clear step-by-step dependencies
- Ultra-low latency requirements where parallelization overhead hurts performance
- Tasks requiring tight shared state between parallel workers
- When subagent isolation prevents necessary collaboration
- Debugging-heavy work where distributed tracing is essential
- Resource-constrained environments where spawning many agents is prohibitive

## Discovered From
- **pi-dynamic-workflows** — Pi framework extension implementing Claude Code-style dynamic workflows
- **VTCode** — Terminal coding agent showing interest in LLM-native workflow orchestration
- **gemini-web2api** — Enables Gemini's advanced features (thinking depth, tool calling) that could power such workflows

## Variants
- **Thinking-Enhanced**: Use models with adjustable thinking depth (`@think=N`) for reasoning-heavy subagents
- **Tool-Augmented**: Subagents equipped with specific tools (web search, file operations, code analysis)
- **Hierarchical**: Workflows that spawn sub-workflows for recursive decomposition
- **Monitored**: Integration with observability tools for detailed metrics and profiling
- **Cached**: Result caching to avoid re-running expensive subagent computations

## Execution Pattern
```javascript
// 1. Define workflow metadata
export const meta = {
  name: 'workflow_name',
  description: 'What this workflow accomplishes',
  phases: [  // Optional progress tracking documentation
    { title: 'Phase 1' },
    { title: 'Phase 2' }
  ]
}

// 2. Mark phase boundaries
phase('Initial Analysis')

// 3. Spawn isolated subagents for parallel work
const results = await parallel([
  () => agent('Analyze frontend components', { label: 'frontend analysis' }),
  () => agent('Analyze backend services', { label: 'backend analysis' }),
  () => agent('Analyze database schema', { label: 'database analysis' })
])

// 4. Synthesize results
const synthesis = await agent(
  'Synthesize findings from:\\n' + JSON.stringify(results),
  { label: 'result synthesis' }
)

// 5. Return final output
return { analysis: results, synthesis }
```

## Metrics & Benefits
- **Scalability**: Utilizes multiple subagents for CPU-bound LLM tasks
- **Fault Tolerance**: Failure in one subagent doesn't crash entire workflow  
- **Transparency**: Live progress view shows exactly what's happening via `phase()` calls
- **Flexibility**: Arbitrary JavaScript enables complex workflow patterns (conditionals, loops)
- **Resource Control**: Token budgeting prevents excessive costs from runaway agents
- **Reusability**: Workflow scripts can be saved, versioned, and reused across similar tasks

## Integration Potential
- **With Hermes Agent**: Similar parallel execution concepts could be adapted for agent swarms
- **With OpenCode**: Pi is built on OpenCode, suggesting tight integration possibilities
- **With MCP**: Subagents could leverage MCP tools for extended capabilities (file, web, shell)
- **With Skills/Memory**: Workflows could utilize persistent skills and memory for context
- **With Monitoring**: Integration with observability tools like Feloxi for detailed metrics