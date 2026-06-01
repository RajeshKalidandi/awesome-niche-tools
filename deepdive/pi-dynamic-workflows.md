# pi-dynamic-workflows: Deep Dive Analysis

## Overview
pi-dynamic-workflows is a Pi (AI agent framework) extension that implements Claude Code-style dynamic workflows. Instead of a single agent working sequentially, the language model writes and executes JavaScript scripts that spawn isolated subagents working in parallel, then synthesizes their results. This enables fan-out patterns for complex tasks like codebase analysis, research, and large-scale refactoring.

## Core Concept
The key innovation is allowing the LLM to generate workflow scripts that:
1. Define metadata (name, description, optional phases)
2. Spawn isolated subagents using the `agent()` tool
3. Execute work in parallel via `parallel()` or `pipeline()`
4. Track progress with `phase()` calls
5. Return synthesized results
6. Optionally manage token budgets and pass arguments

This mirrors Anthropic's dynamic workflows in Claude Code but adapted for the Pi framework.

## Key Features
- **Isolated Subagents**: Each subagent runs in its own sandboxed context
- **Parallel Execution**: `parallel()` and `pipeline()` utilities for concurrent work
- **Progress Tracking**: Live progress view driven by `phase()` calls
- **Token Budgeting**: Built-in budget tracking with `budget` global
- **TypeScript Support**: Editor IntelliSense via triple-slash references
- **Flexible Scripting**: Conditional logic, loops, and dynamic phase creation
- **Result Synthesis**: Automatic collection and return of subagent outputs

## Workflow Script Structure
```javascript
// Export metadata (required)
export const meta = {
  name: 'workflow_name',
  description: 'What this workflow does',
  phases: [                    // Optional documentation
    { title: 'Phase 1' },
    { title: 'Phase 2' }
  ]
}

// Mark phase boundaries for progress tracking
phase('Phase Name')

// Spawn isolated subagents
const result = await agent('Prompt for subagent', {
  label: 'Display label in progress view',
  schema: ZodSchema   // Optional validation
})

// Run multiple agents in parallel
const results = await parallel([
  () => agent('Task 1'),
  () => agent('Task 2')
])

// Pipeline pattern: process items through stages
const processed = await pipeline(items, stage1, stage2)

// Access workflow globals
const budgetRemaining = budget.remaining()
const customArgs = args
const workDir = cwd

// Log workflow-level messages
log('Important event occurred')

// Return final synthesized result
return { aggregated: data }
```

## Available Globals
| Global | Description |
|--------|-------------|
| `agent(prompt, opts)` | Spawn isolated subagent; returns text or validated object |
| `parallel(thunks)` | Run array of thunks concurrently; returns ordered results |
| `pipeline(items, ...stages)` | Process items through sequential stages with fan-out |
| `phase(title)` | Mark current phase for progress tracking |
| `log(message)` | Append workflow-level log line |
| `args` | Optional JSON input from tool invocation |
| `cwd`, `process.cwd()` | Current working directory for subagents |
| `budget` | `{ total, spent(), remaining() }` token budget tracker |

## Use Cases
1. **Codebase Audits**: Parallel analysis of different modules or aspects
2. **Multi-Perspective Review**: Get different viewpoints on the same problem
3. **Large Refactors**: Break down refactoring into parallel tasks
4. **Fan-out Research**: Research multiple sources/topics simultaneously
5. **Batch Processing**: Apply same operation to many items in parallel
6. **Pipeline Processing**: Sequential stages with parallel execution per stage
7. **Comparative Analysis**: Evaluate multiple approaches/solutions concurrently

## Technical Implementation
- **Language**: TypeScript (compiled to JavaScript)
- **Integration**: Pi extension that registers a `workflow` tool
- **Subagent Isolation**: Each `agent()` call creates a separate context
- **Progress Reporting**: Real-time updates via `phase()` calls to frontend
- **Resource Management**: Token budgeting prevents runaway costs
- **Error Handling**: Individual subagent failures don't halt entire workflow
- **Result Aggregation**: Automatic collection of parallel task outputs

## Installation
```bash
# From npm registry
pi install npm:pi-dynamic-workflows

# From local source
pi install /path/to/pi-dynamic-workflows

# Then in Pi session:
/reload
```

## Usage Example
```text
# In Pi chat:
Run a workflow to inspect this repository and summarize the main modules.
```

The model might generate:
```javascript
export const meta = {
  name: 'inspect_project',
  description: 'Inspect a repository and summarize the main modules',
  phases: [
    { title: 'Scan' },
    { title: 'Analyze' }
  ]
}

phase('Scan')
const inventory = await agent('Inspect the repository structure.', {
  label: 'repo inventory'
})

phase('Analyze')
const summary = await agent(
  'Summarize the main modules from this inventory:\\n' + inventory,
  { label: 'module summary' }
)

return { inventory, summary }
```

## Integration Potential
- **With Hermes Agent**: Similar parallel execution concepts could be adapted
- **With OpenCode**: Pi is built on OpenCode, suggesting tight integration
- **With MCP**: Subagents could leverage MCP tools for extended capabilities
- **With Skills/Memory**: Workflows could utilize persistent skills and memory
- **With Monitoring**: Could integrate with observability tools like Feloxi

## Advantages
1. **Scalability**: Utilizes multiple subagents for CPU-bound LLM tasks
2. **Fault Tolerance**: Failure in one subagent doesn't crash entire workflow
3. **Transparency**: Live progress view shows exactly what's happening
4. **Flexibility**: Arbitrary JavaScript enables complex workflow patterns
5. **Resource Control**: Token budgeting prevents excessive costs
6. **Reusability**: Workflow scripts can be saved and reused

## Limitations
1. **JavaScript Requirement**: Users must write JavaScript workflows
2. **Overhead**: Spawning many subagents has latency and resource costs
3. **Complexity**: Debugging distributed workflows can be challenging
4. **Context Limits**: Each subagent has limited context window
5. **Coordination**: Sharing state between subagents requires careful design
6. **Pi Dependency**: Requires Pi framework as foundation

## Comparison with Alternatives
- **vs. Sequential Agents**: Much faster for parallelizable tasks
- **vs. Manual Parallelization**: Automatic orchestration vs. manual management
- **vs. Other Agent Frameworks**: More structured approach to parallelism
- **vs. Simple Loops**: Built-in progress tracking and result aggregation

## Future Enhancements
- **Visual Workflow Designer**: GUI for creating workflows without coding
- **Pre-built Templates**: Library of common workflow patterns
- **Enhanced Monitoring**: Detailed metrics and profiling
- **Result Caching**: Avoid re-running expensive subagents
- **Workflow Chaining**: Output of one workflow as input to another
- **Cross-Framework Portability**: Adapt for other agent frameworks beyond Pi

## Conclusion
pi-dynamic-workflows brings sophisticated parallel agent execution to the Pi framework, enabling users to tackle complex tasks that benefit from fan-out patterns. By allowing the LLM to generate and execute workflow scripts, it provides a powerful abstraction for parallel AI agent coordination while maintaining transparency through live progress tracking. This approach is particularly valuable for code analysis, research, and any task that can benefit from dividing work among multiple specialized subagents.