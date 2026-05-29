# Pattern: Model Escalation (Oracle Pattern)

> When the current model is stuck, invoke a more powerful model with focused context.

## Problem
AI agents hit quality ceilings with their current model. Simple tasks work fine, but complex reasoning, nuanced analysis, or edge cases require more capable models. Calling the most powerful model for everything is expensive; never escalating means missing quality improvements.

## Solution
Implement a tiered model strategy:
1. **Default model** handles 80% of tasks (fast, cheap)
2. **Escalation trigger** detects when the model is stuck (repeated failures, low confidence, complex reasoning)
3. **Oracle invocation** sends focused context to a more powerful model
4. **Result integration** feeds the oracle's response back into the workflow

The key insight: escalation isn't failure — it's a designed pathway for quality improvement. The oracle gets focused context (not the full conversation), making it efficient.

## When to Use
- Agent workflows with mixed complexity tasks
- When cost optimization matters (don't use GPT-5 for simple tasks)
- When quality matters (don't use small models for complex reasoning)
- When you need graceful degradation under load

## When NOT to Use
- When latency is critical (escalation adds round-trip time)
- When the task is well-defined and the default model handles it
- When oracle costs exceed the value of the improvement
- When you can't define clear escalation triggers

## Discovered From
- **oracle** (steipete/oracle) — GPT-5 Pro invoker with multi-model support (2,340 stars, created May 24, 2026)
  - Supports OpenAI, Anthropic, Gemini as oracle providers
  - Custom context and file injection
  - CLI-first design for integration with coding agents

## Variants
- **CLI Escalation**: `oracle "complex question" --context ./file.md` (oracle pattern)
- **MCP Escalation**: Agent calls oracle MCP tool when confidence drops
- **Proxy Escalation**: Headroom-style proxy that routes to stronger models for complex queries
- **Batch Escalation**: Collect uncertain items, escalate in batch to amortize cost

## Metrics
- oracle: 2,340 stars in 5 days (strong signal)
- Multi-model support reduces vendor lock-in
- Custom context injection improves oracle accuracy
