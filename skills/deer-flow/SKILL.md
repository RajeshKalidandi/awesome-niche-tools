---
name: deer-flow
# deer-flow

> **deer-flow**: Long-horizon SuperAgent harness with sandboxes, memories, tools, and subagents

description: |
  ByteDance's enterprise-grade AI agent framework for long-horizon tasks. Features sandboxed execution environments, persistent memory management, tool integration, and multi-agent coordination with enterprise reliability and scalability.

version: "1.0.0"
author: ByteDance AI Research
license: Apache-2.0
platforms: [linux, macos, windows]
tags: [ai-agent, automation, enterprise, long-horizon, multi-agent, sandbox, memory, tools]
metadata:
  hermes:
    tags: [ai-agent, automation, enterprise, long-horizon, multi-agent, sandbox, memory, tools]
    related_skills: [openhands-cli, agent-swarm, deusdata-codebase-memory-mcp, n8n-io/n8n, open-webui]

# Prerequisites

## System Requirements
- **Operating System**: Linux, macOS, or Windows
- **Memory**: Minimum 8GB RAM, recommended 16GB+ for large-scale agent orchestration
- **Storage**: Minimum 10GB free space for agent memory and sandboxes
- **Network**: Internet connection for model access (if not using local models)

## Software Dependencies
- **Python 3.8+** or **Node.js 16+** (depending on installation method)
- **Docker** (recommended for sandbox environments)
- **Poetry** or **pip** (Python) or **npm** (Node.js)

## Model Access
- **OpenAI**: OpenAI GPT models (recommended)
- **Local models**: Ollama, LM Studio, or other local LLM providers
- **Cloud providers**: AWS Bedrock, Google Vertex AI, Azure OpenAI

# Usage Examples

## Basic Agent Setup

### Quick Start
```bash
# Initialize a new project
pip install deer-flow
deer-flow init my-agent-project --model openai/gpt-4

# Set up local model (recommended for privacy)
pip install deer-flow[local]
deer-flow init my-agent-project --model ollama/llama2
```

### Project Structure
```bash
my-agent-project/
├── .deer-flow/
│   ├── config.yaml          # Agent configuration
│   ├── memory/              # Persistent memory storage
│   └── sandboxes/           # Sandbox environments
├── tasks/                   # Task definitions
├── tools/                   # Available tools
├── workflows/               # Workflow definitions
└── logs/                    # Execution logs
```

## Long-horizon Task Execution

### Basic Task Creation
```python
import deer_flow as df

# Create an agent
agent = df.Agent(
    name="business-analyst",
    model="openai/gpt-4",
    system_prompt="You are a business analyst specializing in quarterly analysis."
)

# Define a long-horizon task
task = df.Task(
    title="Q4 Business Analysis",
    description="Analyze quarterly business trends and provide strategic recommendations for next quarter. This requires gathering data, identifying patterns, and creating actionable insights.",
    timeout_hours=24,
    requirements=[
        "Data collection from various sources",
        "Financial trend analysis",
        "Competitive landscape assessment",
        "Strategic recommendation generation"
    ]
)

# Execute the task
result = df.execute_long_horizon_task(agent, task, sandbox_mode="docker")
```

### Task with Tool Integration
```python
# Tool definition for deer-flow
tool_config = {
    "name": "web-scraper",
    "type": "external",
    "description": "Scrape web content for research",
    "parameters": {
        "url": "string",
        "selector": "string"
    }
}

# Create agent with tools
agent = df.Agent(
    name="research-analyst",
    model="openai/gpt-4",
    tools=["web-scraper", "data-analyzer", "report-generator"],
    tool_configs=[tool_config]
)
```

## Agent Configuration

### deer-flow Configuration
```yaml
# .deer-flow/config.yaml
agents:
  - name: business-analyst
    model: openai/gpt-4
    temperature: 0.3
    max_tokens: 4000
    system_prompt: |
      You are a business analyst specializing in quarterly financial analysis.
      Focus on actionable insights and strategic recommendations.
      Use tools judiciously and cite sources for data-driven insights.
    sandbox:
      mode: "docker"
      resources: "4 CPUs, 8GB RAM, 10GB SSD"
    memory:
      type: "redis"
      retention_days: 90

  - name: data-scraper
    model: openai/gpt-3.5-turbo
    tools: [web-scraper]
    sandbox:
      mode: "container"
      isolation_level: "high"
```

### Task Templates
```python
# Pre-defined task templates
task_templates = {
    "market-research": {
        "title": "Market Research Analysis",
        "description": "Conduct comprehensive market research including competitor analysis, trend identification, and opportunity assessment.",
        "estimated_duration": 4,
        "required_tools": ["web-scraper", "data-analyzer"],
        "success_criteria": ["complete market map", "3+ key insights", "actionable recommendations"]
    },
    "code-review": {
        "title": "Code Quality Review",
        "description": "Review and analyze code quality, identify bugs, and suggest improvements.",
        "estimated_duration": 2,
        "tools": ["code-analyzer", "security-scanner"],
        "output_format": "json"
    }
}
```

## Common Pitfalls

### Memory Management
**Problem:** Memory leakage in long-running agent tasks
**Solution:**
```bash
# Configure memory retention
deer-flow config set memory.retention_days 30

# Clear old memory
deer-flow memory clean --age 30
```

### Sandbox Performance
**Problem:** Sandbox resource constraints affecting agent performance
**Solution:**
```bash
# Allocate more resources to sandboxes
deer-flow config set sandbox.resources "8 CPUs, 16GB RAM"

# Use local sandboxes for faster execution (if available)
deer-flow config set sandbox.mode "local"
```

### Tool Configuration
**Problem:** Tools failing due to incorrect configuration
**Solution:**
```bash
# Validate tool configuration
deer-flow tools validate --config tools.yaml

# Test tool connectivity
deer-flow tools test web-scraper --url https://example.com
```

## Verification Steps

### Installation Verification
```bash
# Verify installation
pip install deer-flow

deer-flow --version

# Test basic functionality
python3 -c "import deer_flow; print('deer-flow imported successfully')"
```

### Agent Setup Verification
```bash
# Create a test agent
deer-flow init test-agent --model openai/gpt-3.5-turbo --dry-run

# Verify configuration
deer-flow config show test-agent
```

### Execution Verification
```python
import deer_flow as df

# Create test agent
test_agent = df.Agent(
    name="test-agent",
    model="openai/gpt-3.5-turbo",
    max_tokens=100
)

# Create simple test task
test_task = df.Task(
    title="Test Task",
    description="This is a test to verify the agent works correctly.",
    timeout_seconds=30
)

# Execute test
try:
    result = df.execute_long_horizon_task(test_agent, test_task)
    print(f"✅ Test completed successfully. Result: {result}")
except Exception as e:
    print(f"❌ Test failed: {e}")
```

### Production Readiness Check
```bash
# Full system check
deer-flow system check --comprehensive

# Memory usage check
deer-flow system monitor --resource-usage

# Sandbox health check
deer-flow system health
```

## Advanced Usage Patterns

### Multi-Agent Coordination
```python
import deer_flow as df

# Create coordinator agent
coordinator = df.Agent(
    name="coordinator",
    model="openai/gpt-4",
    system_prompt="You coordinate multiple specialized agents to accomplish complex tasks."
)

# Create specialized agents
research_agent = df.Agent(
    name="researcher",
    model="openai/gpt-4",
    tools=["web-scraper", "data-analyzer"]
)

analysis_agent = df.Agent(
    name="analyst",
    model="openai/gpt-4",
    tools=["chart-generator", "statistical-analyzer"]
)

# Orchestrate multi-agent workflow
workflow = df.Workflow(
    name="comprehensive-analysis",
    agents=[coordinator, research_agent, analysis_agent],
    tasks=[
        {"agent": "coordinator", "task": "define-research-objectives"},
        {"agent": "researcher", "task": "gather-data"},
        {"agent": "analyst", "task": "analyze-findings"},
        {"agent": "coordinator", "task": "generate-insights"}
    ]
)

# Execute workflow
results = df.execute_workflow(workflow)
```

### Integration with Hermes Skills
```python
import deer_flow as df
from hermes_skills import deusdata_codebase_memory_mcp

# Create agent with Hermes skill integration
agent = df.Agent(
    name="code-inspector",
    model="openai/gpt-4",
    tools=["deusdata-codebase-memory-mcp"],
    system_prompt="""
    You analyze codebases using semantic understanding.
    Use the deusdata-codebase-memory-mcp tool to index and search code.
    Provide insights on code quality, architecture patterns, and technical debt.
    """
)

# Example tool usage
analysis_result = agent.execute_task(
    "Analyze the architectural patterns in this codebase",
    use_tool="deusdata-codebase-memory-mcp",
    tool_params={
        "operation": "analyze",
        "path": "./my-codebase",
        "focus_areas": ["architecture", "performance", "maintainability"]
    }
)
```

### Agent Lifecycle Management
```bash
# Start agent
deer-flow agent start my-agent --config config.yaml

# Monitor agent status
deer-flow agent status my-agent

# Pause agent execution
deer-flow agent pause my-agent

# Resume agent execution
deer-flow agent resume my-agent

# Stop agent
deer-flow agent stop my-agent

# Export agent memory
deer-flow agent export my-agent --format json > agent_memory.json
```

### Workflow Templates

#### Research Workflow Template
```python
research_workflow = df.Workflow(
    name="research-and-analysis",
    agents=[
        df.Agent("web-researcher", tools=["web-scraper"]),
        df.Agent("data-analyst", tools=["statistical-analyzer"]),
        df.Agent("report-generator", tools=["document-generator"])
    ],
    tasks=[
        {"agent": "web-researcher", "task": "gather-competitor-data"},
        {"agent": "data-analyst", "task": "analyze-competitor-metrics"},
        {"agent": "report-generator", "task": "create-research-report"}
    ]
)
```

#### Code Analysis Workflow
```python
code_analysis_workflow = df.Workflow(
    name="code-inspection",
    agents=[
        df.Agent("code-inspector", tools=["deusdata-codebase-memory-mcp"]),
        df.Agent("security-auditor", tools=["security-scanner"]),
        df.Agent("performance-analyzer", tools=["performance-profiler"])
    ],
    tasks=[
        {"agent": "code-inspector", "task": "analyze-codebase"},
        {"agent": "security-auditor", "task": "scan-security-vulnerabilities"},
        {"agent": "performance-analyzer", "task": "profile-performance"}
    ]
)
```

## Troubleshooting

### Common Issues and Solutions

**Issue:** Agent memory not persisting across sessions
**Solution:**
```bash
# Configure persistent memory
deer-flow config set memory.type "redis"
deer-flow config set memory.host "localhost"
deer-flow config set memory.port 6379
```

**Issue:** Sandbox resource limits causing agent timeouts
**Solution:**
```bash
# Increase resource allocation
deer-flow config set sandbox.resources "16 CPUs, 32GB RAM, 50GB SSD"

# Use local sandbox for better performance
deer-flow config set sandbox.mode "local"
```

**Issue:** Tool authentication failures
**Solution:**
```bash
# Configure tool authentication
deer-flow config set tools.web-scraper.api_key "your-api-key"
deer-flow config set tools.web-scraper.timeout 60
```

### Debug Commands
```bash
# Debug agent execution
deer-flow debug agent run my-agent --verbose

# Check agent logs
deer-flow logs agent my-agent --tail 100

# Validate configuration
deer-flow config validate

# Test connectivity to services
deer-flow system ping --services openai redis docker
```

## FAQ

### What is the difference between deer-flow and other agent frameworks?
- **Long-horizon focus**: deer-flow is optimized for tasks that take hours or days
- **Enterprise features**: Built-in sandbox isolation, persistent memory, and tool management
- **Multi-agent coordination**: Advanced features for orchestrating multiple agents
- **Integration**: Native support for Hermes skills and external tools

### How do I get started with deer-flow?
1. **Installation**: `pip install deer-flow`
2. **Basic setup**: `deer-flow init my-project`
3. **Test with simple task**: `deer-flow task "Test agent functionality"`
4. **Configure tools**: Set up your required tools in `.deer-flow/config.yaml`
5. **Deploy**: Run production agents with `deer-flow agent start`

### Can I use deer-flow with local models?
Yes! deer-flow supports local models through:
- **Ollama**: `deer-flow init my-project --model ollama/llama2`
- **LM Studio**: `deer-flow init my-project --model lmstudio/llama-2-7b`
- **Self-hosted**: Configure OpenAI-compatible endpoints

### What sandbox options are available?
- **Docker**: Full container isolation (recommended for production)
- **Local**: Faster execution on the host system
- **Virtual**: Lightweight virtualization
- **Hybrid**: Combined approaches for specific use cases

### How do I monitor agent performance?
Use built-in monitoring:
```bash
deer-flow monitor my-agent --metrics

View real-time logs:
deer-flow logs tail my-agent

Check system resources:
deer-flow system status
```

## API Reference

### Core Classes
- `df.Agent()` - Create AI agents
- `df.Task()` - Define tasks
- `df.Workflow()` - Orchestrate multi-agent workflows
- `df.Sandbox()` - Configure execution environments
- `df.Memory()` - Manage persistent agent memory

### Main Functions
- `df.execute_long_horizon_task()` - Execute complex, multi-step tasks
- `df.execute_workflow()` - Run multi-agent workflows
- `df.monitor_agent()` - Monitor agent performance
- `df.export_agent_results()` - Export agent outputs

### Configuration
- `deer-flow config set <key> <value>` - Set configuration
- `deer-flow config get <key>` - Get configuration values
- `deer-flow config validate` - Validate configuration
- `deer-flow config show <project>` - Display project configuration

## Examples Repository

For additional examples and advanced usage patterns, visit:
https://github.com/deer-flow/examples