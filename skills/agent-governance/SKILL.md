---
name: agent-governance
description: "AI agent governance — policy enforcement, zero-trust identity, sandboxing (OWASP Agentic Top 10)"
tags: [ai-agents, governance, security, owasp, policy]
related_skills: [hermes-agent]
---

# Agent Governance Toolkit — AI Agent Security

> Policy enforcement, zero-trust identity, and execution sandboxing for AI agents. Covers all OWASP Agentic Top 10.

## Prerequisites

- Python 3.10+
- An existing AI agent to protect

## Installation

```bash
pip install agent-governance-toolkit
```

## Quick Start

### Initialize governance for your project
```bash
ag-init --project my-agent
# Creates: policies.yaml, audit.log, governance.config.yaml
```

### Define policies
```yaml
# policies.yaml
rules:
  - name: no-financial-actions
    match: "agent.action.type == 'financial'"
    action: deny
    reason: "Financial actions require human approval"
  
  - name: rate-limit
    match: "agent.action.count > 100"
    action: throttle
    window: "1h"
  
  - name: sandbox-external
    match: "agent.action.target == 'external'"
    action: sandbox
    timeout: 30s
```

### Wrap your agent
```python
from governance import AgentGovernor

governor = AgentGovernor("policies.yaml")
safe_agent = governor.wrap(my_agent)

# Agent now enforces all policies automatically
response = safe_agent.run("process this data")
```

### Audit agent actions
```bash
ag-audit --agent my-agent --since 24h
ag-audit --agent my-agent --action financial --result denied
```

## OWASP Agentic Top 10 Coverage

| # | Risk | Mitigation |
|---|------|------------|
| 1 | Prompt Injection | Input sanitization + context isolation |
| 2 | Tool Misuse | Policy-based tool access control |
| 3 | Privilege Escalation | Zero-trust identity verification |
| 4 | Data Exfiltration | Output filtering + audit logging |
| 5 | Unauthorized Actions | Action approval workflows |
| 6 | Cascading Failures | Execution sandboxing + timeouts |
| 7 | Memory Poisoning | Memory integrity verification |
| 8 | Hallucination Exploitation | Output validation + fact-checking |
| 9 | Over-permissioning | Least-privilege tool access |
| 10 | Supply Chain | Dependency verification |

## Pitfalls

1. **Performance overhead**: Policy checks add ~5ms per action. May be noticeable in tight loops.
2. **Policy drift**: Policies need updating as your agent evolves. Set quarterly review reminders.
3. **False positives**: Overly strict policies may block legitimate actions. Start permissive, tighten gradually.
4. **Audit storage**: Logs grow fast. Set up rotation: `ag-audit --rotate --keep 30d`
5. **Integration**: Some agent frameworks may need custom adapters for full governance support.

## Verification

```bash
# Initialize
ag-init --project test-agent

# Verify policies load
ag-validate policies.yaml

# Run a test action through governance
ag-test --action "read file /etc/passwd" --expect deny

# Check audit log
ag-audit --last 10
```
