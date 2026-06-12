# Stack: AI Agent Governance Layer

**Components:** [NVIDIA/SkillSpector](https://github.com/NVIDIA/SkillSpector) + [kenn-io/agentsview](https://github.com/kenn-io/agentsview)

## What It Enables

A complete governance layer for AI coding agents that provides both security auditing and cost/usage observability. This stack answers the two most critical questions for teams deploying AI agents:
1. **Is it safe?** (SkillSpector)
2. **What did it do and how much did it cost?** (AgentsView)

## Why It's Composable

- **SkillSpector** scans agent skills for vulnerabilities before installation — a pre-deployment security gate
- **AgentsView** tracks agent sessions, costs, and usage patterns — a runtime observability layer
- Together they create a full lifecycle governance framework: secure the skills, monitor the execution
- Both are local-first, open-source, and can run in CI/CD pipelines
- SARIF output from SkillSpector feeds into GitHub Security tab; AgentsView data can feed into cost dashboards

## Execution Pattern

### 1. Pre-deployment: Secure skills with SkillSpector
```bash
# Scan all skills before allowing installation
for skill in ./new-skills/*/; do
  risk=$(skillspector scan "$skill" --format json | jq '.risk_score')
  if [ "$risk" -gt 30 ]; then
    echo "REJECTED: $skill (risk: $risk)"
    continue
  fi
  echo "APPROVED: $skill (risk: $risk)"
  # Install skill...
done
```

### 2. Runtime: Monitor with AgentsView
```bash
# Start observability dashboard
agentsview serve

# Daily cost review
agentsview usage daily

# Search for specific sessions
agentsview search "database migration"
```

### 3. CI/CD Integration
```bash
# GitHub Actions workflow
- name: Scan skills
  run: |
    skillspector scan ./skills/ --format sarif --output security.sarif
    
- name: Upload SARIF
  uses: github/codeql-action/upload-sarif@v3
  with:
    sarif_file: security.sarif
```

## Combined Benefits

| Capability | SkillSpector | AgentsView | Combined |
|------------|:---:|:---:|:---:|
| Security scanning | ✅ | ❌ | ✅ |
| Cost tracking | ❌ | ✅ | ✅ |
| Session search | ❌ | ✅ | ✅ |
| CI/CD integration | ✅ | Partial | ✅ |
| Local-first | ✅ | ✅ | ✅ |
| Open source | ✅ | ✅ | ✅ |

## When To Use This Stack

- Deploying AI coding agents in enterprise environments
- Managing shared skill repositories across teams
- Needing compliance/audit trails for agent operations
- Optimizing AI coding costs across multiple agents
- Building internal platforms for AI-assisted development
