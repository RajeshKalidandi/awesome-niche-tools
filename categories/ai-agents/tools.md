# 🤖 AI Agents

> Infrastructure, frameworks, and tools for building and operating AI agents.

---

## [deer-flow](https://github.com/bytedance/deer-flow)

> Long-horizon SuperAgent harness with sandboxes, memories, tools, and subagents

- **Stars:** 72,500 (+2,353/day) | **Language:** TypeScript/Python | **License:** Apache-2.0
- **Last commit:** 2026-06-21
- **Source credibility weight:** 1.00 (GitHub Trending)
- **Relevance score:** 98/100

### What It Does
ByteDance's explosive SuperAgent framework for long-horizon tasks. Features sandboxed execution environments, persistent memory management, tool integration, and multi-agent coordination. Designed for complex, multi-step AI agent workflows with enterprise-grade reliability.

### Why Now
The rapid acceleration of agent-based AI systems has created demand for frameworks that can handle long-horizon tasks with proper isolation, memory management, and tool integration. deer-flow's massive growth (72.5K stars in one day) indicates a critical need for production-grade agent frameworks with enterprise features.

### Why It Matters
This framework unlocks new capabilities for AI agents that need to coordinate across multiple days/weeks while maintaining state, using tools, and working in sandboxed environments. It represents the next evolution beyond short-horizon agent responses to sustained, complex problem-solving.

### Who Should Care
- AI agent framework developers building long-horizon capabilities
- Teams deploying enterprise AI agents requiring persistent memory
- Organizations needing sandboxed agent execution environments
- Developers working with multi-step agent workflows and tool integration

### Execution Pattern
```bash
# Install
pip install deer-flow

# Basic agent setup
deer-flow init my-project --model openai/gpt-4

# Create long-horizon task
deer-flow task "Analyze quarterly business trends and provide strategic recommendations"

# Monitor progress
deer-flow monitor my-project

# Export results
deer-flow export my-project --format json > results.json
```

### Composable Stack Potential
**Code Intelligence Stack:** deer-flow + existing curation tools
- deer-flow provides agent orchestration and memory management
- Existing tools (like DeusData/codebase-memory-mcp) provide semantic code indexing
- Integration enables comprehensive codebase analysis with persistent agent state

This combination allows developers to query entire codebases as knowledge graphs while maintaining conversational context across multiple interaction sessions.

**Research + Production Stack:** deer-flow + Open WebUI + n8n
- deer-flow for agent execution
- Open WebUI for AI interface
- n8n for workflow automation
- Enables end-to-end AI-powered research and production workflows with agent orchestration

## [BB-Browser](https://github.com/epiral/bb-browser)

> Your browser is the API. CLI + MCP server for AI agents to control Chrome with your login state.

- **Stars:** 5,570 (↑~50/day) | **Language:** TypeScript | **License:** MIT
- **Last commit:** 2026-05-28
- **Source credibility weight:** 0.90 (GitHub search)
- **Relevance score:** 79/100

### What It Does
BB-Browser gives AI agents full control of a real Chrome browser — with your existing login sessions, cookies, and extensions. Unlike headless browser tools that start from a blank state, BB-Browser connects to your running Chrome instance, letting agents interact with authenticated web services (Gmail, GitHub, dashboards) without re-authenticating.

### Why Now
AI agents increasingly need to interact with web services that require authentication. Traditional browser automation (Puppeteer, Playwright) runs headless without your session state. BB-Browser solves this by connecting to your existing Chrome, making authenticated web access trivial. At 5.6K stars, it's gaining rapid adoption.

### Why It Matters
This unlocks a new category of agent tasks: anything that requires being logged in. Agents can now check your email, manage your GitHub repos, update your Jira tickets, or interact with any authenticated service — all through your existing browser session. No API keys needed, no OAuth flows, just your browser.

### Who Should Care
- AI agent builders who need authenticated web access
- Anyone automating tasks on websites that require login
- Developers building personal assistant agents
- Teams automating workflows across SaaS tools

### Execution Pattern
```bash
# Install
npm install -g bb-browser

# Start the MCP server (connects to your running Chrome)
bb-browser serve --port 3000

# CLI usage
bb-browser navigate https://gmail.com
bb-browser click "inbox"
bb-browser screenshot

# In agent config (MCP)
{
  "mcpServers": {
    "bb-browser": {
      "command": "bb-browser",
      "args": ["serve", "--port", "3000"]
    }
  }
}
```

### Skill Potential
Yes — SKILL.md should cover: installation, Chrome connection setup, MCP integration, authenticated browsing patterns, and security considerations.

- **Discovered:** 2026-05-29 via GitHub search (credibility: 0.90)

---

## [Engram](https://github.com/Gentleman-Programming/engram)

> Persistent memory system for AI coding agents. Agent-agnostic Go binary with SQLite + FTS5, MCP server, HTTP API, CLI, and TUI.

- **Stars:** 3,844 (↑~40/day) | **Language:** Go | **License:** MIT
- **Last commit:** 2026-05-28
- **Source credibility weight:** 0.90 (GitHub search)
- **Relevance score:** 78/100

### What It Does
Engram provides persistent memory for AI coding agents through a single Go binary. It uses SQLite with FTS5 for fast full-text search, exposes an MCP server for agent integration, and includes HTTP API, CLI, and TUI interfaces. Memories persist across sessions, letting agents remember context, decisions, and patterns from previous work.

### Why Now
AI coding agents currently lose all context between sessions. Engram solves this with a lightweight, agent-agnostic memory system. The Go binary means no dependencies, the MCP server means instant integration, and the FTS5 backend means fast search even with large memory stores. Created recently, already at 3.8K stars.

### Why It Matters
Persistent memory transforms AI agents from stateless tools into continuous collaborators. An agent that remembers your coding preferences, past decisions, and project context produces dramatically better results. Engram makes this possible without complex infrastructure — just a single binary.

### Who Should Care
- AI coding agent users who want session persistence
- Teams building custom agent workflows
- Developers who want agents that learn from past work
- Anyone frustrated by agents that forget context

### Execution Pattern
```bash
# Install
go install github.com/Gentleman-Programming/engram@latest

# Run as MCP server
engram serve --port 3001

# Store a memory
engram store "User prefers pytest over unittest" --tags python,testing

# Search memories
engram search "python testing preferences"

# TUI interface
engram tui
```

### Skill Potential
Yes — SKILL.md should cover: installation, MCP server setup, memory storage patterns, search optimization, and integration with Hermes Agent memory system.

- **Discovered:** 2026-05-29 via GitHub search (credibility: 0.90)

---

## [Moltis](https://github.com/moltis-org/moltis)

> A secure persistent personal agent server in Rust. One binary, sandboxed execution, multi-provider LLMs, voice, memory, MCP tools.

- **Stars:** 2,709 (↑~30/day) | **Language:** Rust | **License:** MIT
- **Last commit:** 2026-05-28
- **Source credibility weight:** 0.90 (GitHub search)
- **Relevance score:** 77/100

### What It Does
Moltis is a complete personal AI agent server in a single Rust binary. It provides sandboxed code execution, multi-provider LLM support (OpenAI, Anthropic, local models), voice input/output, persistent memory, and integrations with Telegram, WhatsApp, Discord, and Teams. All running locally on your machine.

### Why Now
The "personal AI agent" space is fragmented — people cobble together multiple tools for chat, memory, voice, and tool execution. Moltis consolidates everything into one binary. The Rust implementation means it's fast, secure, and has zero runtime dependencies. The multi-platform messaging integration means your agent is accessible everywhere.

### Why It Matters
Moltis represents the "personal AI OS" vision — one server that handles all your AI interactions across platforms. The sandboxed execution means you can let the agent run code without security concerns. The voice integration means you can talk to your agent naturally. This is what personal AI should look like.

### Who Should Care
- Anyone wanting a personal AI assistant across platforms
- Developers who want self-hosted AI without cloud dependencies
- Teams needing a secure, sandboxed agent runtime
- Privacy-conscious users who want local AI

### Execution Pattern
```bash
# Install (single binary)
curl -sL https://github.com/moltis-org/moltis/releases/latest/download/moltis -o /usr/local/bin/moltis
chmod +x /usr/local/bin/moltis

# Configure providers
moltis config set openai-key sk-...
moltis config set anthropic-key sk-ant-...

# Run the server
moltis serve

# Connect via Telegram
moltis connect telegram
```

### Skill Potential
Yes — SKILL.md should cover: installation, provider configuration, messaging integration setup, sandboxed execution, and voice configuration.

- **Discovered:** 2026-05-29 via GitHub search (credibility: 0.90)

---

## [OpenGap](https://github.com/open-gitagent/opengap)

> A framework-agnostic, git-native standard for defining AI agents — a portable agent definition format.

- **Stars:** 2,793 (↑~25/day) | **Language:** TypeScript | **License:** MIT
- **Last commit:** 2026-05-28
- **Source credibility weight:** 0.90 (GitHub search)
- **Relevance score:** 76/100

### What It Does
OpenGap defines a git-native standard for AI agent configurations — think "Docker Compose for agents." It provides a portable format for defining agent capabilities, tools, memory, and workflows that works across any framework. Agent definitions live in your repo, version-controlled alongside your code.

### Why Now
AI agent configurations are currently locked into specific frameworks. OpenGap breaks this by providing a universal standard that any framework can implement. The git-native approach means agent configs are version-controlled, reviewable, and shareable — just like code. This is the "open standard" moment for agent definitions.

### Why It Matters
Instead of rewriting agent configs when you switch frameworks, OpenGap lets you define once and run anywhere. This is critical for teams evaluating different agent frameworks or migrating between them. The git-native approach also enables team collaboration on agent definitions through PRs and code review.

### Who Should Care
- Teams evaluating multiple AI agent frameworks
- Organizations standardizing agent deployments
- Open source projects wanting framework-agnostic agent support
- Anyone tired of vendor lock-in with agent platforms

### Execution Pattern
```bash
# Install
npm install -g opengap

# Initialize agent definition
opengap init

# Validate agent definition
opengap validate agent.yaml

# Export for specific framework
opengap export --framework claude-code
opengap export --framework codex
```

### Skill Potential
Yes — SKILL.md should cover: installation, agent definition format, framework export, git integration, and migration patterns.

- **Discovered:** 2026-05-29 via GitHub search (credibility: 0.90)

---

## [harness](https://github.com/revfactory/harness)

> A meta-skill that designs domain-specific agent teams, defines specialized agents, and generates the skills they use.

- **Stars:** 3,847 (↑~190/week) | **Language:** HTML | **License:** Apache-2.0
- **Last commit:** 2026-05-28
- **Source credibility weight:** 1.00 (GitHub Trending)
- **Relevance score:** 75/100

### What It Does
harness is a meta-skill for Claude Code that designs agent teams for specific domains. Instead of manually defining agents and their capabilities, harness analyzes your project and generates specialized agents with appropriate skills. It's "agent engineering" as a skill — defining how agents should be structured for your use case.

### Why Now
As AI agents become more capable, the challenge shifts from "can it code?" to "how do we structure multiple agents for complex tasks?" harness addresses this by providing a systematic approach to agent team design. At 3.8K stars and growing, it's filling a real gap in the agent ecosystem.

### Why It Matters
Most teams build agents ad-hoc — one agent does everything, or they manually define agent roles. harness provides a structured methodology for decomposing complex tasks into agent teams with clear responsibilities. This is the difference between "AI helps me code" and "AI teams collaborate on my project."

### Who Should Care
- Teams building multi-agent workflows
- Developers using Claude Code who want structured agent teams
- Anyone moving from single-agent to multi-agent architectures
- Technical leads designing AI-assisted development processes

### Execution Pattern
```bash
# Install as Claude Code skill
curl -sL https://raw.githubusercontent.com/revfactory/harness/main/harness.md -o ~/.claude/skills/harness.md

# Use in Claude Code
# "Use harness to design an agent team for this web application"
```

### Skill Potential
No — this is already a skill file. The value is in using it directly.

- **Discovered:** 2026-05-29 via GitHub Trending (credibility: 1.00)

---

## [oh-my-pi](https://github.com/can1357/oh-my-pi)

> AI Coding agent for the terminal — hash-anchored edits, optimized tool harness, LSP, Python, browser, subagents.

- **Stars:** 8,220 (↑~100/week) | **Language:** TypeScript | **License:** MIT
- **Last commit:** 2026-05-28
- **Source credibility weight:** 1.00 (GitHub Trending weekly)
- **Relevance score:** 74/100

### What It Does
oh-my-pi is a terminal-based AI coding agent with advanced features: hash-anchored edits (precise code modifications), optimized tool harness, LSP integration, Python execution, browser automation, and sub-agent spawning. It's a full-featured coding agent that runs entirely in your terminal.

### Why Now
The AI coding agent space is consolidating around terminal-based tools (Claude Code, Codex, OpenCode). oh-my-pi differentiates with hash-anchored edits — a more reliable approach to code modification that doesn't break on whitespace changes. The sub-agent support enables parallel task execution.

### Why It Matters
Hash-anchored edits solve a real problem: traditional line-number-based edits break when code shifts. oh-my-pi's approach is more robust for real-world coding. The LSP integration means it understands your code semantically, not just syntactically. This is a serious contender in the terminal agent space.

### Who Should Care
- Terminal-first developers who want AI coding assistance
- Anyone frustrated by fragile code edits from other agents
- Developers who need parallel task execution via sub-agents
- Python developers wanting integrated LSP support

### Execution Pattern
```bash
# Install
npm install -g oh-my-pi

# Run in a project directory
cd /path/to/project
oh-my-pi

# Features available in the TUI:
# - Hash-anchored code edits
# - LSP integration
# - Python execution
# - Browser automation
# - Sub-agent spawning
```

### Skill Potential
No — better used as a standalone tool.

- **Discovered:** 2026-05-29 via GitHub Trending weekly (credibility: 1.00)

---

## [Uni-CLI](https://github.com/olo-dot-io/Uni-CLI)

> Operations substrate for AI agents that use real software: 311 sites/tools, logged-in browsers, desktop apps, MCP.

- **Stars:** 144 (↑~3/day) | **Language:** TypeScript | **License:** Apache-2.0
- **Last commit:** 2026-05-28
- **Source credibility weight:** 0.90 (GitHub search)
- **Relevance score:** 74/100

### What It Does
Uni-CLI is an operations substrate that lets AI agents interact with real software — 311 pre-configured sites and tools, logged-in browsers, desktop applications, and MCP servers. It includes policy enforcement, evidence collection, self-repair capabilities, and the AgentEnvelope v2 protocol for standardized agent interactions.

### Why Now
AI agents can write code, but they can't easily use the software that runs businesses. Uni-CLI bridges this gap by providing pre-configured integrations for 311 real-world tools. The policy engine ensures agents follow organizational rules, and the self-repair mechanism handles failures gracefully.

### Why It Matters
This is the "last mile" for AI agents — connecting them to the actual tools humans use daily. Instead of building custom integrations for each SaaS tool, Uni-CLI provides a universal interface. The evidence collection means you can audit what agents did, and the policy engine means you can control what they're allowed to do.

### Who Should Care
- Teams building enterprise AI agents
- Anyone automating workflows across multiple SaaS tools
- Organizations needing audit trails for agent actions
- Developers building agent-to-software integrations

### Execution Pattern
```bash
# Install
npm install -g uni-cli

# List available tools
uni-cli list

# Connect to a tool
uni-cli connect github --auth

# Run an agent action
uni-cli run "create a PR with the changes"
```

### Skill Potential
Yes — SKILL.md should cover: installation, tool connection, policy configuration, evidence collection, and integration with Hermes Agent.

- **Discovered:** 2026-05-29 via GitHub search (credibility: 0.90)

---

## [Ktx](https://github.com/Kaelio/ktx)

> ktx is the context layer for analytics agents — executable context for data agents.

- **Stars:** 271 (↑~15/day) | **Language:** TypeScript | **License:** Apache-2.0
- **Last commit:** 2026-05-28
- **Source credibility weight:** 0.85 (Hacker News Show HN)
- **Relevance score:** 72/100

### What It Does
Ktx provides an executable context layer for data and analytics agents. Instead of passing raw data to agents, Ktx creates structured, queryable context that agents can reason over. It's designed for analytics workflows where agents need to understand data schemas, relationships, and business logic.

### Why Now
Data agents are emerging as a major use case, but they struggle with context — raw data dumps are too large and unstructured. Ktx solves this by providing a structured context layer that agents can query efficiently. The "executable" aspect means context can trigger actions, not just provide information.

### Why It Matters
For teams building analytics agents, Ktx provides the missing context infrastructure. Instead of agents guessing at data relationships, Ktx makes them explicit and queryable. This dramatically improves the accuracy and reliability of data-driven AI workflows.

### Who Should Care
- Teams building analytics or data agents
- Data engineers integrating AI with data pipelines
- Anyone building query-based AI interfaces
- Business intelligence teams exploring AI-assisted analysis

### Execution Pattern
```bash
# Install
npm install -g ktx

# Define context for a dataset
ktx define --schema ./schema.yaml --data ./data/

# Query context
ktx query "What are the top 10 products by revenue?"

# Run as MCP server
ktx serve --port 3002
```

### Skill Potential
Yes — SKILL.md should cover: installation, context definition, query patterns, MCP integration, and data agent workflows.

- **Discovered:** 2026-05-29 via Hacker News Show HN (credibility: 0.85)


## [RuView](https://github.com/ruvnet/RuView)

> Turns commodity WiFi signals into real-time spatial intelligence, vital sign monitoring, and presence detection

- **Stars:** 67,436 (↑~4,690/week) | **Language:** Rust | **License:** MIT
- **Last commit:** 2026-05-29
- **Source credibility weight:** 1.00 (GitHub Trending)
- **Relevance score:** 92/100

### What It Does
RuView uses commodity WiFi routers and a Rust-based DSP pipeline to extract spatial intelligence from WiFi signal reflections — no cameras, no wearables, no dedicated sensors. It detects presence, tracks movement, monitors vital signs (heart rate, breathing), and creates real-time spatial maps using only the WiFi signals already in your environment. Think of it as turning every WiFi router into a radar system.

### Why Now
WiFi sensing has been a research topic for years, but RuView is the first practical, open-source implementation that runs on commodity hardware. The Rust implementation makes it fast enough for real-time use. At 67K stars and growing 4,690/week, it's the hottest open-source project this month — signaling massive interest in camera-free spatial intelligence.

### Why It Matters
This fundamentally changes what's possible with existing infrastructure. Every building with WiFi already has the hardware for spatial intelligence. No cameras means no privacy concerns. No wearables means no compliance burden. Smart homes, elderly care, security, retail analytics — all become possible with software updates to existing WiFi hardware.

### Who Should Care
- Smart home enthusiasts wanting presence detection without cameras
- Healthcare teams exploring non-invasive vital sign monitoring
- Security professionals needing camera-free surveillance
- IoT developers building on existing WiFi infrastructure
- Privacy-conscious organizations that can't deploy cameras

### Execution Pattern
```bash
# Clone and build
git clone https://github.com/ruvnet/RuView.git
cd RuView
cargo build --release

# Run with your WiFi interface
./target/release/ruview --interface wlan0 --mode presence

# Modes available:
# presence — basic occupancy detection
# tracking — movement path tracking
# vital — heart rate and breathing monitoring
# spatial — full 3D spatial mapping

# Output as MCP server for AI integration
./target/release/ruview serve --port 8090
```

### Skill Potential
Yes — SKILL.md should cover: installation, WiFi interface requirements, mode selection, MCP server integration, privacy considerations, and calibration procedures.

- **Discovered:** 2026-05-29 via GitHub Trending (credibility: 1.00)

---

## [heretic](https://github.com/p-e-w/heretic)

> Fully automatic censorship removal for language models

- **Stars:** 22,294 (↑~500/day) | **Language:** Python | **License:** AGPL-3.0
- **Last commit:** 2026-05-28
- **Source credibility weight:** 0.85 (Hacker News)
- **Relevance score:** 80/100

### What It Does
Heretic automatically removes censorship and content restrictions from language models. It modifies model weights to eliminate refusals, safety filters, and content policies — turning any censored model into an uncensored one. Works with LLaMA, Mistral, and other open-weight models through targeted weight manipulation.

### Why Now
As LLMs become more capable, censorship has become a major frustration for researchers, developers, and power users. Heretic provides a systematic, automated approach to removing these restrictions. At 22K stars, there's clearly massive demand for uncensored AI capabilities. The AGPL-3.0 license ensures the tool remains open.

### Why It Matters
For AI researchers studying model behavior, this is an essential tool. For developers building applications that need uncensored outputs (creative writing, research, analysis), Heretic makes it trivial to unblock models. It also raises important questions about AI governance and the ethics of censorship removal.

### Who Should Care
- AI researchers studying model behavior and alignment
- Developers building applications that need uncensored outputs
- Creative writers using AI for fiction and worldbuilding
- Security researchers analyzing model vulnerabilities
- Anyone frustrated by overzealous content filtering

### Execution Pattern
```bash
# Install
pip install heretic

# Remove censorship from a model
heretic unblock --model meta-llama/Llama-3-8B --output ./uncensored-model

# Apply to a local GGUF
heretic unblock --gguf ./model.gguf --output ./uncensored.gguf

# Verify censorship removed
heretic test --model ./uncensored-model --prompt "How does a lock work?"
```

### Skill Potential
Yes — SKILL.md should cover: installation, model compatibility, weight manipulation techniques, verification, and ethical considerations.

- **Discovered:** 2026-05-29 via Hacker News (credibility: 0.85)

---

## [Dograh](https://github.com/dograh-hq/dograh)

> Open source voice AI platform — self-hosted Vapi/Retell alternative with MCP

- **Stars:** 3,570 (↑~100/day) | **Language:** Python | **License:** BSD-2-Clause
- **Last commit:** 2026-05-29
- **Source credibility weight:** 1.00 (GitHub Trending)
- **Relevance score:** 82/100

### What It Does
Dograh is a self-hosted voice AI platform that provides the same capabilities as Vapi and Retell (speech-to-speech, LLM/STT/TTS integration, telephony) but runs entirely on your own infrastructure. It includes a visual workflow builder, MCP native support for AI agent integration, and BYOK (Bring Your Own Key) for all AI services. One platform to build, deploy, and manage voice AI applications.

### Why Now
Voice AI is exploding — customer service bots, appointment schedulers, sales assistants. But Vapi and Retell are expensive SaaS products ($0.05-0.15/minute) with data privacy concerns. Dograh makes self-hosted voice AI practical with a visual builder and MCP integration, meaning AI agents can make and receive calls natively.

### Why It Matters
Self-hosted voice AI means: no per-minute costs, full control over voice data, custom voices and behaviors, and no vendor lock-in. For companies handling sensitive conversations (healthcare, legal, finance), self-hosting isn't just cheaper — it's a compliance requirement. Dograh makes this accessible without building from scratch.

### Who Should Care
- Companies building voice AI applications
- Contact centers exploring AI automation
- Healthcare providers needing HIPAA-compliant voice AI
- Developers building AI agents that need phone capabilities
- Anyone paying too much for Vapi/Retell/Telephony APIs

### Execution Pattern
```bash
# Clone and install
git clone https://github.com/dograh-hq/dograh.git
cd dograh
pip install -e .

# Start the server
dograh serve --port 8080

# Create a voice workflow via API
curl -X POST http://localhost:8080/api/workflows \
  -H "Content-Type: application/json" \
  -d '{
    "name": "appointment-scheduler",
    "voice": "alloy",
    "llm": "gpt-4",
    "prompt": "You are a friendly appointment scheduler..."
  }'

# Connect MCP server for AI agent integration
dograh mcp --port 8090
```

### Skill Potential
Yes — SKILL.md should cover: installation, provider configuration, workflow builder, MCP integration, telephony setup, and voice customization.

- **Discovered:** 2026-05-29 via GitHub Trending (credibility: 1.00)

---

## [Microsoft Agent Governance Toolkit](https://github.com/microsoft/agent-governance-toolkit)

> AI Agent Governance Toolkit — Policy enforcement, zero-trust identity, execution sandboxing, covers 10/10 OWASP Agentic Top 10

- **Stars:** 3,187 (↑~100/day) | **Language:** Python | **License:** MIT
- **Last commit:** 2026-05-28
- **Source credibility weight:** 0.85 (Hacker News)
- **Relevance score:** 82/100

### What It Does
Microsoft's Agent Governance Toolkit provides policy enforcement, zero-trust identity, and execution sandboxing for AI agents. It covers all 10 items in the OWASP Agentic Top 10 security risks. Think of it as security middleware for AI agents — it sits between your agent and the outside world, enforcing policies, verifying identity, and sandboxing execution.

### Why Now
As AI agents gain real-world capabilities (making purchases, sending emails, modifying databases), governance becomes critical. The OWASP Agentic Top 10 was just published, and Microsoft's toolkit is the first comprehensive implementation. At 3.2K stars and backed by Microsoft, it's becoming the de facto standard for agent security.

### Why It Matters
Every organization deploying AI agents needs governance. Without it, agents can: leak data, execute unauthorized actions, impersonate users, or cause cascading failures. This toolkit makes governance practical — not just a policy document, but code that enforces policies at runtime.

### Who Should Care
- Teams deploying AI agents in production
- Security engineers responsible for AI safety
- Compliance officers in regulated industries
- Platform teams building agent infrastructure
- Anyone who's ever wondered "what if my agent does something unexpected?"

### Execution Pattern
```bash
# Install
pip install agent-governance-toolkit

# Initialize governance for your agent
ag-init --project my-agent

# Enforce policies in your agent
from governance import AgentGovernor
governor = AgentGovernor("policies.yaml")
safe_agent = governor.wrap(my_agent)

# Audit agent actions
ag-audit --agent my-agent --since 24h
```

### Skill Potential
Yes — SKILL.md should cover: installation, policy definition, zero-trust setup, OWASP coverage, and integration with Hermes Agent.

- **Discovered:** 2026-05-29 via Hacker News (credibility: 0.85)

---

## [oracle](https://github.com/steipete/oracle)

> Invoke GPT-5 Pro with custom context and files when stuck — multi-model escalation for coding agents.

- **Stars:** 2,340 (↑~470/day) | **Language:** TypeScript | **License:** MIT
- **Last commit:** 2026-05-28
- **Source credibility weight:** 1.00 (engineer watch — Peter Steinberger)
- **Relevance score:** 83/100

### What It Does
oracle is a CLI tool that invokes GPT-5 Pro (or other powerful models) with custom context and files when you're stuck on a complex problem. It supports OpenAI, Anthropic, and Gemini as oracle providers, with automatic context injection. Think of it as "ask the expert" for your coding agent — when the current model can't solve it, escalate to a more capable one.

### Why Now
As AI coding agents become mainstream, users are hitting quality ceilings with default models. oracle solves this by providing a structured escalation pathway. Created by Peter Steinberger (steipete), one of the most prolific AI tooling engineers, it's already at 2,340 stars in 5 days. The multi-model support means you're not locked into one provider.

### Why It Matters
This pattern — model escalation when stuck — is becoming essential for production agent workflows. Instead of either accepting poor quality or paying for the most expensive model on every call, oracle provides a middle path: use the cheap model for routine tasks, escalate to the powerful model only when needed. This can cut costs by 70-80% while maintaining quality on complex tasks.

### Who Should Care
- AI coding agent users hitting quality ceilings
- Teams optimizing LLM costs without sacrificing quality
- Developers building multi-model agent workflows
- Anyone who's ever wished they could "ask a smarter model" mid-task

### Execution Pattern
```bash
# Install
npm install -g oracle

# Invoke with context
oracle "How do I implement a distributed lock in Rust?" --context ./src/

# Use with specific provider
oracle "Explain this error" --provider anthropic --model claude-opus-4-0520

# Pipe context from file
cat error.log | oracle "What's causing this?"

# Integrate with Claude Code
# Add to CLAUDE.md: "When stuck, use oracle to escalate"
```

### Skill Potential
Yes — SKILL.md should cover: installation, provider configuration, context injection patterns, escalation triggers, and cost optimization strategies.

- **Discovered:** 2026-05-29 via engineer watch (Peter Steinberger) (credibility: 1.00)
## [Genspark-AI](https://github.com/veryyoldman/Genspark-AI)

> Self-hosted Super Agent with multi-agent orchestration, deep research, Sparkpages, AI slides & sheets, image generation, and 80+ tools.

- **Stars:** 280 (↑~20/day) | **Language:** Python | **License:** MIT
- **Last commit:** 2026-05-24
- **Source credibility weight:** 0.75 (GitHub Search)
- **Relevance score:** 75/100

### What It Does
Genspark-AI is a self-hosted multi-agent orchestration platform that provides the capabilities of Genspark.ai as open source. It includes deep research agents, document generation (Sparkpages, AI slides, AI sheets), image generation, and 80+ built-in tools — all orchestrated through a unified agent framework. Run your own AI research and document generation platform without sending data to external services.

### Why Now
AI research agents are splitting into two camps: expensive SaaS (Genspark, Perplexity) and bare-bones open source (simple RAG). Genspark-AI fills the gap with a feature-rich self-hosted alternative that includes multi-agent coordination, document generation, and image creation. At 280 stars and growing, it's early but gaining traction as teams seek to self-host AI capabilities.

### Why It Matters
Self-hosted AI research means: no per-query costs, full control over data privacy, custom agent behaviors, and no vendor lock-in. For organizations handling sensitive research (legal, healthcare, finance), this is a compliance requirement. Genspark-AI provides the orchestration layer that makes multi-agent research practical — not just single-query RAG.

### Who Should Care
- Teams building self-hosted AI research platforms
- Organizations with data privacy requirements
- Developers who want multi-agent orchestration without building from scratch
- Anyone seeking a FOSS alternative to Genspark.ai or Perplexity

### Execution Pattern
```bash
# Clone and install
git clone https://github.com/veryyoldman/Genspark-AI.git
cd Genspark-AI
pip install -r requirements.txt

# Configure API keys
export OPENAI_API_KEY=sk-...
export ANTHROPIC_API_KEY=sk-ant-...

# Run the server
python app.py

# Access web UI
open http://localhost:8080

# Use from CLI
python cli.py research "quantum computing applications in drug discovery"
python cli.py slides --topic "Q3 roadmap" --output roadmap.pptx
```

### Skill Potential
Yes — SKILL.md should cover: installation, API key configuration, agent orchestration setup, tool integration, and document generation workflows.

- **Discovered:** 2026-05-30 via GitHub Search (credibility: 0.75)

---

## [Claw Patrol](https://github.com/denoland/clawpatrol)

> Open-source security firewall for AI agents. Routes agent traffic through a gateway that evaluates requests against HCL rules — supports HTTP, SQL, and Kubernetes protocol gating with credential injection.

- **Stars:** 518 (↑~15/day) | **Language:** Go | **License:** MIT
- **Last commit:** 2026-05-28
- **Source credibility weight:** 0.85 (Lobsters)
- **Relevance score:** 85/100

### What It Does
Claw Patrol is a security firewall designed specifically for AI agents. It sits between your agent and the outside world, evaluating every outbound request against HCL-based policy rules. The gateway supports HTTP, SQL, and Kubernetes protocol gating — so you can restrict what APIs your agent calls, what databases it queries, and what K8s resources it touches. Critically, it handles credential injection: agents never hold real API keys or database passwords. The gateway injects them at request time, so even a compromised agent can't exfiltrate credentials.

### Why Now
AI agents are increasingly autonomous — they make HTTP calls, query databases, and interact with cloud APIs. But most agent frameworks have zero built-in security. Agents hold raw credentials, can call any endpoint, and have no request-level policy enforcement. Claw Patrol addresses this gap with a gateway pattern that's familiar from API gateway architectures but purpose-built for agent traffic. Created by the Deno team, it carries strong engineering credibility.

### Why It Matters
Without a firewall, a single prompt injection attack can turn your agent into a data exfiltration vector. Claw Patrol adds defense-in-depth: policy rules gate what the agent can do, credential injection prevents key exposure, and protocol-specific rules catch things like SQL injection via agent queries. For any team running agents in production, this is the missing security layer.

### Who Should Care
- Teams deploying AI agents that access external APIs or databases
- Security engineers responsible for agent infrastructure
- Anyone building agents that handle sensitive credentials
- Organizations with compliance requirements around data access

### Execution Pattern
Deploy Claw Patrol as a sidecar or reverse proxy. Define HCL rules for each agent's permissions (e.g., "agent X can call GitHub API but not AWS"). Run your agent with the gateway as its HTTP proxy. The gateway evaluates each request against the policy, injects credentials, and either forwards or blocks. Monitor blocked requests for security auditing.

### Skill Potential
Yes — SKILL.md would cover: gateway deployment, HCL rule authoring, protocol-specific policies (HTTP/SQL/K8s), credential injection setup, and integration with agent frameworks.

- **Discovered:** 2026-05-31 via Lobsters (credibility: 0.85)


---

## [pi-dynamic-workflows](https://github.com/Michaelliv/pi-dynamic-workflows)

> Claude-Code-style dynamic workflows for Pi — model writes JS that fans work across isolated subagents, then synthesizes results.

- **Stars:** 629 (↑~105/day) | **Language:** TypeScript | **License:** None declared
- **Last commit:** 2026-05-31
- **Source credibility weight:** 1.00 (GitHub Trending)
- **Relevance score:** 74/100

### What It Does
pi-dynamic-workflows adds a workflow tool to Claude Code that enables dynamic task orchestration. The model writes JavaScript that fans work across isolated subagents, then synthesizes their results. Think of it as structured parallelism for AI coding tasks — the model decides how to decompose a problem, spawns workers for each subtask, and merges the results.

### Why Now
AI coding agents excel at single-file tasks but struggle with large refactors, multi-perspective reviews, and codebase-wide changes that require parallel exploration. pi-dynamic-workflows solves this by giving the model explicit control over task decomposition and parallel execution. Created May 28, 2026, at 629 stars with daily commits.

### Why It Matters
This is the missing piece for scaling AI coding from single-file edits to codebase-wide transformations. Instead of the agent processing files sequentially (slow, loses context), it can now fan out across multiple subagents working in parallel. Codebase audits, multi-perspective code reviews, and large refactors become practical.

### Who Should Care
- Claude Code users doing large-scale codebase work
- Teams needing parallel code analysis
- Developers working on monorepos with complex dependencies
- Anyone who has hit the limits of single-agent coding

### Execution Pattern
```bash
# Install as Claude Code skill
npm install -g pi-dynamic-workflows

# Use in Claude Code
# The model automatically uses the workflow tool when tasks are complex
# Example: "Audit this codebase for security vulnerabilities"
# The model decomposes into subagents: auth audit, input validation, dependency check
```

### Skill Potential
Yes — SKILL.md should cover: installation, workflow decomposition patterns, subagent isolation, result synthesis, and integration with Hermes delegate_task.

- **Discovered:** 2026-06-01 via GitHub Trending (credibility: 1.00)


---

## [flashlib](https://github.com/FlashML-org/flashlib)

> Fast and memory-efficient classical ML operators — GPU-accelerated kmeans, knn, pca, svd, dbscan, umap, t-sne on Triton.

- **Stars:** 416 (↑~69/day) | **Language:** Python | **License:** Apache-2.0
- **Last commit:** 2026-05-26
- **Source credibility weight:** 1.00 (GitHub Trending)
- **Relevance score:** 63/100

### What It Does
flashlib is a GPU library for classical machine learning operators built on Triton and CuteDSL. It provides GPU-accelerated implementations of kmeans, knn, pca, svd, dbscan, hdbscan, umap, t-sne, regression, and GEMM — the core algorithms that scikit-learn uses but without the CPU bottleneck. Pip-installable, with a familiar API that mirrors scikit-learn.

### Why Now
Classical ML (clustering, dimensionality reduction, nearest neighbors) is experiencing a renaissance as AI agents use these algorithms for data analysis, anomaly detection, and feature engineering. But CPU-based implementations are too slow for real-time agent workflows. flashlib brings GPU acceleration to these algorithms, making them practical for agent-integrated data pipelines.

### Why It Matters
For teams building AI agents that analyze data, flashlib eliminates the ML algorithm bottleneck. Instead of waiting minutes for kmeans on a CPU, you get seconds on GPU. The scikit-learn-compatible API means zero learning curve. The Apache-2.0 license makes it safe for commercial use.

### Who Should Care
- Data scientists wanting GPU acceleration without CUDA expertise
- AI agents that perform real-time data analysis
- Teams running ML pipelines at scale
- Anyone tired of waiting for CPU-based clustering/dimensionality reduction

### Execution Pattern
```bash
# Install
pip install flashlib

# Use like scikit-learn
from flashlib.cluster import KMeans
kmeans = KMeans(n_clusters=5, device='cuda')
labels = kmeans.fit_predict(data)

# Dimensionality reduction
from flashlib.decomposition import UMAP
umap = UMAP(n_components=2, device='cuda')
embedding = umap.fit_transform(data)
```

### Skill Potential
Yes — SKILL.md should cover: installation, GPU requirements, API compatibility with scikit-learn, performance benchmarks, and integration with data analysis workflows.

- **Discovered:** 2026-06-01 via GitHub Trending (credibility: 1.00)


---

## [lazycodex](https://github.com/code-yeongyu/lazycodex)

> Agent harness for complex codebases inside Codex CLI — project memory, planning, execution, and verified completion.

- **Stars:** 480 | **Language:** TypeScript | **License:** MIT
- **Last commit:** 2026-06-05
- **Source credibility weight:** 1.00 (GitHub trending discovery)
- **Relevance score:** 78/100

### What It does
lazycodex turns Codex into a full project-aware coding agent by adding persistent memory, planning steps, execution tracking, and verified completion built right into the CLI harness. Instead of dumb translation, it gives the agent a workspace memory and a plan.

### Why Now
AI coding agents are graduating from single-shot prompts to multi-step coding projects, and agent harnesses are the missing layer. lazycodex packages this as a drop-in agent harness for Codex, and 480 stars in just a few days shows demand.

### Why It Matters
For any developer running Codex on real repos, lazycodex removes the "agent amnesia" problem. The agent remembers prior steps, tracks open plans, and verifies work before declaring done.

### Who Should Care
- Solo devs running Codex on large codebases
- Teams who want repeatable AI-assisted implementation plans
- Engineers building internal agent harnesses
- Agent SDK evaluators

### Execution Pattern
```bash
# Install / use via Codex integration
npx lazycodex@latest
# Follow the project memory workflow for plan-then-execute coding.
```

### Skill Potential
Yes — cover Codex integration, memory workflow setup, plan-driven execution, verification loops, and observer patterns.

- **Discovered:** 2026-06-05 via GitHub trending discovery (credibility: 1.00)


---

## [memory-os](https://github.com/ClaudioDrews/memory-os)

> A 7-layer memory operating system for Hermes Agent — persistent memory with Qdrant, structured facts, fabric recall, auto-curated wiki, and surgical context injection.

- **Stars:** 830 | **Language:** Python | **License:** MIT
- **Last commit:** 2026-06-05
- **Source credibility weight:** 1.00 (GitHub trending discovery)
- **Relevance score:** 73/100

### What It Does
memory-os provides structured persistent memory for agent systems. It layers vector recall (Qdrant) alongside symbolic facts, auto-curates a wiki from past sessions, and injects only what's relevant back into agent context.

### Why Now
Context inflation is now the primary bottleneck for capable agents. memory-os directly attacks it by giving agents a persistent, searchable memory substrate instead of an ever-growing transcript.

### Why It Matters
Better memory changes agent quality more than model upgrades in many cases. If agents recall past decisions, preferences, and project context, they reduce hallucination, improve consistency, and ship faster.

### Who Should Care
- AI agent operators managing long-lived workflows
- Dev teams running multiple agent sessions over weeks
- OSS contributors building long-running automation
- Researchers comparing memory architectures

### Execution Pattern
```bash
# Start memory-os service
python -m memory_os serve
# Agents call MCP or HTTP endpoints to recall/store
curl -X POST http://localhost:8000/recall -d '{"query":"deployment decisions"}'
```

### Skill Potential
Yes — describe memory topology, installation modes, Qdrant setup, recall pipelines, wiki curation, and context-injection safety.

- **Discovered:** 2026-06-05 via GitHub trending discovery (credibility: 1.00)


---

## [adhd](https://github.com/UditAkhourii/adhd)

> A skill for coding agents. Tree-of-thought with pruning, parallel divergent thoughts under different cognitive frames, and survivor deepening.

- **Stars:** 749 | **Language:** TypeScript | **License:** MIT
- **Last commit:** 2026-06-05
- **Source credibility weight:** 1.00 (GitHub trending discovery)
- **Relevance score:** 71/100

### What It Does
adhd makes coding agents fan out their thinking in parallel, score each branch, prune weak options, and deepen the winners. It's a tree-of-thought skill with built-in cognitive frames and an LLM judge to prune dead-ends fast.

### Why Now
Reasoning budgets are growing but raw thinking isn't automatically better. Directed reasoning budgets with pruning become the next productivity unlock.

### Why It Matters
For creative and interdisciplinary work, more ideas help — but only if you can drop the bad ones fast. adhd formalizes that into an agent skill.

### Who Should Care
- Coding agent operators wanting richer planning loops
- Teams exploring reasoning-time compute scaling
- Prompt engineers building agent policies
- Researchers studying agent cognition models

### Execution Pattern
```bash
# Install in Claude Code or Codex library
npm install -g @udit/adhd
# Use in a thinking-heavy task to expand-and-prune planning.
```

### Skill Potential
Yes — benchmark framework, integration examples, pruning prompts, and cognitive frame selection guidance.

- **Discovered:** 2026-06-05 via GitHub trending discovery (credibility: 1.00)


---

## [Duel-Agents](https://github.com/2aronS/Duel-Agents)

> CLI, SDK, and IDE plugins for Duel Agents.

- **Stars:** 714 | **Language:** TypeScript | **License:** MIT
- **Last commit:** 2026-06-05
- **Source credibility weight:** 1.00 (GitHub trending discovery)
- **Relevance score:** 68/100

### What It Does
Duel-Agents provides a CLI, SDK, and IDE plugins for running structured agent interactions in development workflows. It exposes agents as first-class primitives you can invoke, pipe, and debug from your editor.

### Why Now
Developer experience for agent usage is still primitive. Bundling CLI, SDK, and IDE plugins lowers the adoption burden and embeds agentic behavior inside everyday tooling.

### Why It Matters
DX improvements for agents matter: if invoking an agent costs one terminal command, usage scales. Duel-Agents makes agent calls keyboard-native.

### Who Should Care
- IDE-native engineers (VS Code, JetBrains)
- CLI-first automation builders
- SDK integrators wrapping agent behaviors
- Teams debugging agent pipelines live

### Execution Pattern
```bash
# Install CLI
npm install -g duel-agents
# Run an agent task
duel run "refactor auth module" --dry-run
```

### Skill Potential
Yes — install flow, IDE config, SDK binding patterns, task templates, and multi-provider fallback.

- **Discovered:** 2026-06-05 via GitHub trending discovery (credibility: 1.00)


---

## [mnemo](https://github.com/zaydmulani09/mnemo)

> Local-first AI memory layer for any LLM. Persistent knowledge graph, entity extraction, semantic retrieval.

- **Stars:** 193 (↑~48/day) | **Language:** Rust | **License:** MIT
- **Last commit:** 2026-06-04
- **Source credibility weight:** 1.00 (GitHub Trending) corroborated by HN (0.85)
- **Relevance score:** 77/100 (after multipliers)
- **Confidence:** HIGH (MIT-licensed Rust crate + PyPI, multi-source)

### What It Does
Mnemo is a self-hosted memory substrate that gives any LLM long-term recall. It extracts entities, builds a persistent knowledge graph, and supports semantic retrieval — all running locally with SQLite. Works with Ollama, OpenAI, Anthropic, or any OpenAI-compatible endpoint.

### Why Now
Every LLM-backed app reinvents the same memory wheel: vector stores, dedup, entity extraction, retrieval. Mnemo collapses the scaffolding into a single Rust binary/Python wheel so a one-liner gets your agent/chatbot persistent recall. Released 2026-06-02, picked up 193 stars in four days across two discovery channels.

### Why It Matters
Memory is the missing primitive for personal agents and tool-using bots. Mnemo’s backend-agnostic design means you can swap Claude for a local Ollama model without losing context, which makes it a foundation layer rather than a feature.

### Who Should Care
Agent builders, RAG tinkerers, devs building persistent chatbots, teams who want Claude/Codex to remember project context across sessions.

### Execution Pattern
- `pip install mnemo` or `cargo install mnemo`
- Point it at your model endpoint (Ollama, OpenAI, Anthropic)
- Feed it conversations/docs — it extracts entities and persists a graph
- Query it from any client: “What did we decide about the cache invalidation strategy?” returns contextually linked entities, not just chunks

### Skill Potential
YES — SKILL.md generated in `skills/mnemo/`. Covers the `mnemo` CLI, the Python SDK, and integration patterns with Hermes and other agent harnesses.

- **Discovered:** 2026-06-07 via GitHub Trending (credibility: 1.00) and HN (0.85)


---

## [last30days-skill](https://github.com/mvanhorn/last30days-skill)

> AI agent skill that researches any topic across Reddit, X, YouTube, HN, Polymarket, and the web - then synthesizes a grounded summary

- **Stars:** 37,272 (↑~3,191/day) | **Language:** Python | **License:** MIT
- **Last commit:** 2026-06-09
- **Source credibility weight:** 1.00 (GitHub Trending)
- **Relevance score:** 90/100

### What It Does
last30days-skill is an AI agent skill that performs cross-platform research on any topic. It crawls Reddit, X (Twitter), YouTube, Hacker News, Polymarket, and the general web to gather recent information, then synthesizes a grounded summary with citations. The skill is designed for AI agents that need to understand current events, trends, or topics across multiple platforms.

### Why Now
With the explosion of AI agents, there's a growing need for agents to access real-time, multi-platform information. Traditional web search gives static results; last30days-skill provides dynamic, cross-platform research capability. At 37K+ stars with 3K+ stars/day, it's gaining massive traction as agents become more capable.

### Why It Matters
This skill transforms AI agents from static knowledge repositories into dynamic research assistants. Instead of relying on pre-trained knowledge, agents can now gather current information from multiple sources and synthesize it into coherent summaries. This is critical for tasks like market research, news analysis, trend monitoring, and fact-checking.

### Who Should Care
- AI agent developers building research-capable agents
- Anyone building personal assistant agents that need current information
- Teams building market intelligence or monitoring systems
- Researchers who need automated cross-platform literature review

### Execution Pattern


### Skill Potential
Yes — this is already a skill! It can be integrated into any AI agent framework that supports Python skills.



---

---


skill = Last30DaysSkill()
result = await skill.research("latest developments in AI agents")
print(result.summary)
print(result.sources)
```

### Skill Potential
Yes - this is already a skill! It can be integrated into any AI agent framework that supports Python skills.

---

## [goose](https://github.com/aaif-goose/goose)

> An open source, extensible AI agent that goes beyond code suggestions - install, execute, edit, and test with any LLM

- **Stars:** 48,490 (↑~489/day) | **Language:** Rust | **License:** Apache-2.0
- **Last commit:** 2026-06-09
- **Source credibility weight:** 1.00 (GitHub Trending)
- **Relevance score:** 87/100

### What It Does
Goose is an extensible, open-source AI agent that goes beyond simple code suggestions. Written in Rust for performance, it can install packages, execute commands, edit files, and run tests using any LLM backend. Unlike typical code assistants that only suggest changes, Goose can actually perform complex development workflows end-to-end.

### Why Now
AI agents are evolving from passive assistants to active participants in development workflows. Goose represents the next generation: agents that don't just suggest code but can actually implement, test, and deploy it. With 48K+ stars and steady growth, it's becoming the reference implementation for capable AI coding agents.

### Why It Matters
Goose shifts the paradigm from "AI suggests, human implements" to "AI implements, human reviews." This dramatically accelerates development cycles and enables solo developers to accomplish what previously required teams. The Rust implementation ensures performance at scale.

### Who Should Care
- Developers looking to automate repetitive coding tasks
- Teams wanting to accelerate development velocity
- AI researchers studying agent architectures
- Anyone building custom AI coding assistants

### Execution Pattern
```bash
# Install via package manager or from source
# See GitHub repo for installation instructions

# Configure with your preferred LLM
goose configure

# Run a coding task
goose run "refactor the authentication module to use JWT tokens"
```

### Skill Potential
Yes - Goose can be used as a backend for Hermes agents or integrated into custom agent workflows.


---

## [Agent Skills](https://github.com/addyosmani/agent-skills)

> Production-grade engineering skills for AI coding agents with 7 slash commands mapping to the dev lifecycle

- **Stars:** 51,715 | **Language:** Shell | **License:** MIT
- **Last commit:** 2026-06-11
- **Source credibility weight:** 1.00 (GitHub Trending)
- **Relevance score:** 85/100 (after multipliers)

### What It Does
Agent Skills encodes the workflows, quality gates, and best practices that senior engineers use when building software into reusable skill files for AI coding agents. It provides 7 slash commands (/spec, /plan, /build, /test, /review, /code-simplify, /ship) that map to the development lifecycle, with skills activating automatically based on context.

### Why Now
The AI coding agent ecosystem has exploded, but most agents lack structured engineering discipline. Addy Osmani (Chrome team lead) packaged real engineering practices into agent-compatible skill files. The /build auto mode enables autonomous multi-step development while maintaining verification gates — a critical capability as agents take on larger tasks.

### Why It Matters
This bridges the gap between raw AI coding ability and production-grade software engineering. Instead of agents hacking together code without process, these skills enforce spec-first development, test-driven implementation, and systematic code review. It turns AI coding assistants from code generators into engineering partners.

### Who Should Care
Developers using Claude Code, Cursor, Codex CLI, or any AI coding agent. Engineering teams wanting to standardize AI-assisted development. Anyone building production software with AI assistance who needs quality gates.

### Execution Pattern
Install via plugin marketplace for Claude Code, or clone locally for other agents. Skills activate automatically based on what you're doing — designing an API triggers interface design skills, building UI triggers frontend engineering skills. Use /build auto for autonomous end-to-end development.

### Skill Potential
Yes — automation of engineering workflows, quality gate enforcement, multi-agent development orchestration.

- **Discovered:** 2026-06-11 via GitHub Trending (credibility: 1.00)


---

## [hivemind](https://github.com/activeloopai/hivemind)

> Multi-agent orchestration framework for building coordinated AI agent teams

- **Stars:** 820 | **Language:** TypeScript | **License:** Apache-2.0
- **Last commit:** 2026-06-10
- **Source credibility weight:** 1.00 (GitHub Trending)
- **Relevance score:** 72/100 (after multipliers)

### What It Does
Hivemind is a framework for building coordinated multi-agent systems. It provides the infrastructure for multiple AI agents to share context, divide tasks, and work together on complex problems. The tagline 'One brain for all your agents' captures its goal of creating unified agent teams from individual LLM instances.

### Why Now
Single-agent systems are hitting complexity limits. Tasks that require parallel research, cross-validation, or specialized expertise benefit from coordinated agent teams. Hivemind from Activeloop (the Deep Lake company) brings production multi-agent orchestration to TypeScript, making it accessible for web-native agent development.

### Why It Matters
Building reliable multi-agent systems from scratch requires solving coordination, state sharing, task decomposition, and failure handling. Hivemind provides these primitives, letting developers focus on agent logic rather than infrastructure. For teams building complex AI workflows, this reduces the coordination overhead significantly.

### Who Should Care
AI/ML engineers building multi-agent systems, teams developing complex AI workflows, developers creating agent orchestrations for research or automation, and anyone exploring the frontier of agent coordination.

### Execution Pattern
Install via npm/yarn, define agent roles and communication patterns, configure shared state management, and deploy. The framework handles inter-agent messaging, task routing, and result aggregation. Integrate with existing LLM providers for the underlying intelligence.

### Skill Potential
Yes — multi-agent workflow design, coordination pattern libraries, integration with existing agent frameworks.

- **Discovered:** 2026-06-11 via GitHub Trending (credibility: 1.00)


---

## [NVIDIA/SkillSpector](https://github.com/NVIDIA/SkillSpector)

> Security scanner for AI agent skills — detects vulnerabilities, malicious patterns, and security risks before installing agent skills.

- **Stars:** 2619 (↑~33/day) | **Language:** Python | **License:** Apache-2.0
- **Last commit:** 2026-06-10
- **Source credibility weight:** 1.00 (GitHub Trending)
- **Relevance score:** 83/100 (after multipliers)

### What It Does
SkillSpector scans AI agent skills (Claude Code, Codex CLI, Gemini CLI, etc.) for 64 vulnerability patterns across 16 categories: prompt injection, data exfiltration, privilege escalation, supply chain attacks, MCP tool poisoning, and more. It provides a 0-100 risk score with severity labels and clear recommendations. Supports Git repos, URLs, zip files, and directories as input.

### Why Now
AI agent skills execute with implicit trust and minimal vetting. Research shows 26.1% of skills contain vulnerabilities and 5.2% show likely malicious intent. As the agent skills ecosystem explodes (Agent Skills, Superpowers, pm-skills), the need for automated security scanning is critical. SkillSpector fills this gap with a comprehensive, NVIDIA-backed solution.

### Why It Matters
Without SkillSpector, users install agent skills blind — trusting that a community-contributed SKILL.md won't exfiltrate data or inject prompts. This tool makes the agent skills ecosystem safer by providing automated, reproducible security auditing. It's the missing piece for enterprise adoption of AI coding agents.

### Who Should Care
- Teams deploying AI coding agents in production environments
- Platform engineers managing agent skill repositories
- Security teams auditing AI agent supply chains
- Individual developers who install community-contributed skills

### Execution Pattern


### Skill Potential
Yes — SKILL.md covers: installation, scanning workflows, CI/CD integration, custom rule authoring, and SARIF output for GitHub Security.

- **Discovered:** 2026-06-12 via GitHub Trending (credibility: 1.00)


---

## [kenn-io/agentsview](https://github.com/kenn-io/agentsview)

> Local-first session intelligence and analytics for coding agents — browse, search, and track costs across Claude Code, Codex, and 20+ other agents.

- **Stars:** 1623 (up ~15/day) | **Language:** Go | **License:** MIT
- **Last commit:** 2026-06-11
- **Source credibility weight:** 1.00 (GitHub Trending)
- **Relevance score:** 78/100 (after multipliers)

### What It Does
AgentsView is a local-first tool that discovers, indexes, and analyzes sessions from AI coding agents on your machine. It supports Claude Code, Codex CLI, Forge, and 20+ other agents. It provides a web UI dashboard for browsing sessions, searching conversations, and tracking API costs — all stored in a local SQLite database with no accounts or cloud dependencies. It is positioned as a 100x faster replacement for ccusage.

### Why Now
As developers adopt multiple AI coding agents simultaneously, there is no unified way to track what each agent did, how much it cost, or how sessions relate to each other. AgentsView fills this gap with a single binary that indexes everything locally. The timing is perfect — agent usage is exploding but observability tools have not caught up.

### Why It Matters
Without AgentsView, developers have no visibility into their agent usage across tools. They cannot compare costs between Claude Code and Codex, cannot search old sessions, and cannot audit what agents did. This tool provides the missing observability layer for the multi-agent development workflow.

### Who Should Care
- Developers using 2+ AI coding agents daily
- Teams tracking AI coding costs across tools
- Engineering managers auditing agent usage
- Anyone who wants to search or browse their agent session history

### Execution Pattern
See the GitHub repo for installation instructions. Supports Homebrew, direct install script, and Docker.

### Skill Potential
Yes — SKILL.md covers: installation, session indexing, cost tracking, web UI usage, and integration with agent workflows.

- **Discovered:** 2026-06-12 via GitHub Trending (credibility: 1.00)


---

## [hexo-ai/sia](https://github.com/hexo-ai/sia)

> Self-Improving AI framework — autonomously improves AI system performance on benchmark tasks via meta-agent orchestration.

- **Stars:** 1280 (up ~16/day) | **Language:** Python | **License:** MIT
- **Last commit:** 2026-06-11
- **Source credibility weight:** 1.00 (GitHub Trending)
- **Relevance score:** 74/100 (after multipliers)

### What It Does
SIA (Self-Improving AI) is a framework where a language-model agent updates both the harness and the weights of a task-specific agent through an iterative loop. It coordinates three agent types — Meta-Agent, Target Agent, and Feedback Agent — to continuously refine performance. The paper reports 56.6% gain on LawBench, 91.9% runtime reduction on GPU kernels, and 502% improvement on single-cell RNA denoising over baseline.

### Why Now
Self-improving AI is transitioning from research curiosity to practical tooling. SIA provides a concrete, benchmarked implementation with published results on MLE-Bench (ranked #1), LawBench, and CUDA kernel optimization. As AI agents become more capable, frameworks that let them improve themselves will be essential.

### Why It Matters
SIA demonstrates that AI agents can autonomously improve their own performance — not just solve tasks, but get better at solving them over time. This is a foundational capability for building truly autonomous AI systems. The framework is practical enough to run locally with built-in tasks.

### Who Should Care
- AI researchers exploring self-improving agent architectures
- ML engineers optimizing model performance on specific tasks
- Developers building autonomous AI systems
- Anyone interested in agent-as-optimizer patterns

### Execution Pattern
Install via pip with the appropriate agent implementation (Claude or OpenHands), then run built-in tasks:
Collecting sia-agent
  Downloading sia_agent-0.5.1-py3-none-any.whl.metadata (13 kB)
Requirement already satisfied: python-dotenv>=1.0 in /usr/local/lib/hermes-agent/venv/lib/python3.11/site-packages (from sia-agent) (1.2.2)
Requirement already satisfied: numpy>=2.0 in /usr/local/lib/hermes-agent/venv/lib/python3.11/site-packages (from sia-agent) (2.4.3)
Requirement already satisfied: pandas>=2.0 in /usr/local/lib/hermes-agent/venv/lib/python3.11/site-packages (from sia-agent) (3.0.3)
Requirement already satisfied: scikit-learn>=1.4 in /usr/local/lib/hermes-agent/venv/lib/python3.11/site-packages (from sia-agent) (1.9.0)
Requirement already satisfied: fastapi>=0.110 in /usr/local/lib/hermes-agent/venv/lib/python3.11/site-packages (from sia-agent) (0.133.1)
Requirement already satisfied: uvicorn>=0.29 in /usr/local/lib/hermes-agent/venv/lib/python3.11/site-packages (from sia-agent) (0.41.0)
Requirement already satisfied: pydantic>=2.0 in /usr/local/lib/hermes-agent/venv/lib/python3.11/site-packages (from sia-agent) (2.13.4)
Requirement already satisfied: claude-agent-sdk>=0.1.50 in /usr/local/lib/hermes-agent/venv/lib/python3.11/site-packages (from sia-agent) (0.2.88)
Requirement already satisfied: anyio>=4.0.0 in /usr/local/lib/hermes-agent/venv/lib/python3.11/site-packages (from claude-agent-sdk>=0.1.50->sia-agent) (4.13.0)
Requirement already satisfied: mcp>=1.23.0 in /usr/local/lib/hermes-agent/venv/lib/python3.11/site-packages (from claude-agent-sdk>=0.1.50->sia-agent) (1.26.0)
Requirement already satisfied: sniffio>=1.0.0 in /usr/local/lib/hermes-agent/venv/lib/python3.11/site-packages (from claude-agent-sdk>=0.1.50->sia-agent) (1.3.1)
Requirement already satisfied: starlette>=0.40.0 in /usr/local/lib/hermes-agent/venv/lib/python3.11/site-packages (from fastapi>=0.110->sia-agent) (1.0.1)
Requirement already satisfied: typing-extensions>=4.8.0 in /usr/local/lib/hermes-agent/venv/lib/python3.11/site-packages (from fastapi>=0.110->sia-agent) (4.15.0)
Requirement already satisfied: typing-inspection>=0.4.2 in /usr/local/lib/hermes-agent/venv/lib/python3.11/site-packages (from fastapi>=0.110->sia-agent) (0.4.2)
Requirement already satisfied: annotated-doc>=0.0.2 in /usr/local/lib/hermes-agent/venv/lib/python3.11/site-packages (from fastapi>=0.110->sia-agent) (0.0.4)
Requirement already satisfied: python-dateutil>=2.8.2 in /usr/local/lib/hermes-agent/venv/lib/python3.11/site-packages (from pandas>=2.0->sia-agent) (2.9.0.post0)
Requirement already satisfied: annotated-types>=0.6.0 in /usr/local/lib/hermes-agent/venv/lib/python3.11/site-packages (from pydantic>=2.0->sia-agent) (0.7.0)
Requirement already satisfied: pydantic-core==2.46.4 in /usr/local/lib/hermes-agent/venv/lib/python3.11/site-packages (from pydantic>=2.0->sia-agent) (2.46.4)
Requirement already satisfied: scipy>=1.10.0 in /usr/local/lib/hermes-agent/venv/lib/python3.11/site-packages (from scikit-learn>=1.4->sia-agent) (1.17.1)
Requirement already satisfied: joblib>=1.4.0 in /usr/local/lib/hermes-agent/venv/lib/python3.11/site-packages (from scikit-learn>=1.4->sia-agent) (1.5.3)
Requirement already satisfied: narwhals>=2.0.1 in /usr/local/lib/hermes-agent/venv/lib/python3.11/site-packages (from scikit-learn>=1.4->sia-agent) (2.22.0)
Requirement already satisfied: threadpoolctl>=3.5.0 in /usr/local/lib/hermes-agent/venv/lib/python3.11/site-packages (from scikit-learn>=1.4->sia-agent) (3.6.0)
Requirement already satisfied: click>=7.0 in /usr/local/lib/hermes-agent/venv/lib/python3.11/site-packages (from uvicorn>=0.29->sia-agent) (8.4.1)
Requirement already satisfied: h11>=0.8 in /usr/local/lib/hermes-agent/venv/lib/python3.11/site-packages (from uvicorn>=0.29->sia-agent) (0.16.0)
Requirement already satisfied: idna>=2.8 in /usr/local/lib/hermes-agent/venv/lib/python3.11/site-packages (from anyio>=4.0.0->claude-agent-sdk>=0.1.50->sia-agent) (3.18)
Requirement already satisfied: httpx-sse>=0.4 in /usr/local/lib/hermes-agent/venv/lib/python3.11/site-packages (from mcp>=1.23.0->claude-agent-sdk>=0.1.50->sia-agent) (0.4.3)
Requirement already satisfied: httpx>=0.27.1 in /usr/local/lib/hermes-agent/venv/lib/python3.11/site-packages (from mcp>=1.23.0->claude-agent-sdk>=0.1.50->sia-agent) (0.28.1)
Requirement already satisfied: jsonschema>=4.20.0 in /usr/local/lib/hermes-agent/venv/lib/python3.11/site-packages (from mcp>=1.23.0->claude-agent-sdk>=0.1.50->sia-agent) (4.26.0)
Requirement already satisfied: pydantic-settings>=2.5.2 in /usr/local/lib/hermes-agent/venv/lib/python3.11/site-packages (from mcp>=1.23.0->claude-agent-sdk>=0.1.50->sia-agent) (2.14.1)
Requirement already satisfied: pyjwt>=2.10.1 in /usr/local/lib/hermes-agent/venv/lib/python3.11/site-packages (from pyjwt[crypto]>=2.10.1->mcp>=1.23.0->claude-agent-sdk>=0.1.50->sia-agent) (2.13.0)
Requirement already satisfied: python-multipart>=0.0.9 in /usr/local/lib/hermes-agent/venv/lib/python3.11/site-packages (from mcp>=1.23.0->claude-agent-sdk>=0.1.50->sia-agent) (0.0.30)
Requirement already satisfied: sse-starlette>=1.6.1 in /usr/local/lib/hermes-agent/venv/lib/python3.11/site-packages (from mcp>=1.23.0->claude-agent-sdk>=0.1.50->sia-agent) (3.4.4)
Requirement already satisfied: six>=1.5 in /usr/local/lib/hermes-agent/venv/lib/python3.11/site-packages (from python-dateutil>=2.8.2->pandas>=2.0->sia-agent) (1.17.0)
Requirement already satisfied: certifi in /usr/local/lib/hermes-agent/venv/lib/python3.11/site-packages (from httpx>=0.27.1->mcp>=1.23.0->claude-agent-sdk>=0.1.50->sia-agent) (2026.5.20)
Requirement already satisfied: httpcore==1.* in /usr/local/lib/hermes-agent/venv/lib/python3.11/site-packages (from httpx>=0.27.1->mcp>=1.23.0->claude-agent-sdk>=0.1.50->sia-agent) (1.0.9)
Requirement already satisfied: attrs>=22.2.0 in /usr/local/lib/hermes-agent/venv/lib/python3.11/site-packages (from jsonschema>=4.20.0->mcp>=1.23.0->claude-agent-sdk>=0.1.50->sia-agent) (26.1.0)
Requirement already satisfied: jsonschema-specifications>=2023.03.6 in /usr/local/lib/hermes-agent/venv/lib/python3.11/site-packages (from jsonschema>=4.20.0->mcp>=1.23.0->claude-agent-sdk>=0.1.50->sia-agent) (2025.9.1)
Requirement already satisfied: referencing>=0.28.4 in /usr/local/lib/hermes-agent/venv/lib/python3.11/site-packages (from jsonschema>=4.20.0->mcp>=1.23.0->claude-agent-sdk>=0.1.50->sia-agent) (0.37.0)
Requirement already satisfied: rpds-py>=0.25.0 in /usr/local/lib/hermes-agent/venv/lib/python3.11/site-packages (from jsonschema>=4.20.0->mcp>=1.23.0->claude-agent-sdk>=0.1.50->sia-agent) (2026.5.1)
Requirement already satisfied: cryptography>=3.4.0 in /usr/local/lib/hermes-agent/venv/lib/python3.11/site-packages (from pyjwt[crypto]>=2.10.1->mcp>=1.23.0->claude-agent-sdk>=0.1.50->sia-agent) (46.0.7)
Requirement already satisfied: cffi>=2.0.0 in /usr/local/lib/hermes-agent/venv/lib/python3.11/site-packages (from cryptography>=3.4.0->pyjwt[crypto]>=2.10.1->mcp>=1.23.0->claude-agent-sdk>=0.1.50->sia-agent) (2.0.0)
Requirement already satisfied: pycparser in /usr/local/lib/hermes-agent/venv/lib/python3.11/site-packages (from cffi>=2.0.0->cryptography>=3.4.0->pyjwt[crypto]>=2.10.1->mcp>=1.23.0->claude-agent-sdk>=0.1.50->sia-agent) (3.0)
Downloading sia_agent-0.5.1-py3-none-any.whl (3.8 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 3.8/3.8 MB 10.9 MB/s eta 0:00:00
Installing collected packages: sia-agent
Successfully installed sia-agent-0.5.1

     _______. __       ___
    /       ||  |     /      |   (----`|  |    /  ^      \   \    |  |   /  /_\  .----)   |   |  |  /  _____  |_______/    |__| /__/     \__
    Self-Improving AI framework

    • Version : v0.5.1
    • Docs    : https://github.com/hexo-ai/sia
    • Help    : sia --help


     _______. __       ___
    /       ||  |     /      |   (----`|  |    /  ^      \   \    |  |   /  /_\  .----)   |   |  |  /  _____  |_______/    |__| /__/     \__
    Self-Improving AI framework

    • Version : v0.5.1
    • Docs    : https://github.com/hexo-ai/sia
    • Help    : sia --help

### Skill Potential
Yes — SKILL.md covers: installation, running built-in tasks, adding custom tasks, and integrating with different LLM providers.

- **Discovered:** 2026-06-12 via GitHub Trending (credibility: 1.00)

---

## [Superpowers](https://github.com/obra/superpowers)

> Agentic skills framework and software development methodology for AI coding agents

- **Stars:** 227,000 (↑32,428/day) | **Language:** Shell/JavaScript | **License:** MIT
- **Last commit:** 2026-06-09 | **Source credibility:** 1.00 (GitHub Trending)
- **Relevance score:** 93/100

### What It Does
Superpowers transforms AI coding agents into systematic engineers by providing production-grade skills that enforce TDD, brainstorming, plan writing, subagent-driven development, and code review. It's not just a tool — it's a complete methodology for making AI agents reliable and consistent.

### Why Now
The AI agent space has exploded with tools, but most lack the operational discipline to produce production-quality code. Superpowers fills this gap by encoding proven engineering workflows into agent skills. With 227K stars in under a month, it's the fastest-growing developer tool in the ecosystem.

### Why It Matters
Adopting Superpowers means your AI agents stop producing throwaway code and start following engineering best practices. The TDD enforcement alone prevents the "works on my machine" problem that plagues AI-generated code.

### Who Should Care
- Teams using AI coding agents (Claude Code, Codex, OpenCode)
- Solo developers who want AI agents that follow best practices
- Organizations building internal AI development workflows

### Execution Pattern
```bash
# Install for your preferred agent platform
# Follow the platform-specific installation guide in the README
# The skills are automatically available to your agent
```

### Skill Potential
Yes — Superpowers is itself a skill framework. A SKILL.md could document how to extend it with custom skills for specific domains.

- **Discovered:** 2026-06-14 via GitHub Trending (credibility: 1.00)


---

## [AgentMemory](https://github.com/rohitg00/agentmemory)

> Persistent memory for AI coding agents with 4-tier consolidation

- **Stars:** 22,600 (↑2,597/day) | **Language:** TypeScript | **License:** Apache-2.0
- **Last commit:** 2026-06 (active) | **Source credibility:** 1.00 (GitHub Trending)
- **Relevance score:** 84/100

### What It Does
AgentMemory provides a persistent memory system for AI coding agents with 4-tier memory consolidation: working, episodic, semantic, and procedural. It achieves 95.2% retrieval accuracy on the LongMemEval benchmark and works across multiple agents via MCP + REST APIs.

### Why Now
As AI agents become more capable, they need memory that persists across sessions. AgentMemory solves the "start from scratch" problem by giving agents a structured memory system that improves over time. The 4-tier architecture mirrors how human memory works, making it more effective than simple vector stores.

### Why It Matters
Without persistent memory, AI agents waste context window on re-explaining the same project details. AgentMemory reduces this overhead by 60-80% while improving response quality through memory consolidation.

### Who Should Care
- Developers running AI coding agents for large projects
- Teams building multi-agent systems that need shared context
- Organizations implementing AI-assisted development workflows

### Execution Pattern


### Skill Potential
Yes — AgentMemory could be wrapped as a Hermes skill for automatic memory management across coding sessions.

- **Discovered:** 2026-06-14 via GitHub Trending (credibility: 1.00)


---

## [agent-browser](https://github.com/vercel-labs/agent-browser)

> Fast native Rust CLI for browser automation designed for AI agents

- **Stars:** 35,900 | **Language:** Rust | **License:** MIT
- **Last commit:** 2026-06-10 | **Source credibility:** 1.00 (GitHub Search)
- **Relevance score:** 84/100

### What It Does
agent-browser is a high-performance Rust CLI that provides deterministic element selection via accessibility snapshots, AI chat mode, and a security suite with domain allowlists and action policies. From Vercel Labs, it's designed specifically for AI agents that need reliable browser automation.

### Why Now
AI agents are increasingly tasked with web interactions, but existing browser automation tools weren't designed for agent use cases. agent-browser fills this gap with agent-first features like accessibility-based element selection and security policies that prevent agents from accessing unauthorized sites.

### Why It Matters
The accessibility snapshot approach means AI agents can reliably interact with web pages without brittle CSS selectors. This makes browser automation 10x more reliable for agent workflows.

### Who Should Care
- Developers building AI agents that interact with web services
- Teams implementing automated testing with AI agents
- Organizations needing secure browser automation for AI workflows

### Execution Pattern


### Skill Potential
Yes — agent-browser is a natural fit for Hermes skills that need browser interaction capabilities.

- **Discovered:** 2026-06-14 via GitHub Search (credibility: 0.75)


---

## [Ponytail](https://github.com/DietrichGebert/ponytail)

> Makes your AI agent think like the laziest senior dev in the room — 80-94% less code output

- **Stars:** 7,051 (new — created 2026-06-12, 3 days old) | **Language:** JavaScript | **License:** MIT
- **Last commit:** 2026-06-14
- **Source credibility weight:** 1.00 (GitHub Trending)
- **Relevance score:** 95/100

### What It Does
Ponytail is an AI agent skill that enforces minimal code output. It instructs coding agents to think before writing, prefer zero-code solutions, and generate 80-94% less code than default. Works with 11+ agents including Claude Code, Cursor, Codex, and Windsurf.

### Why Now
As AI coding agents gain adoption, over-engineering has become a real problem. Agents default to generating verbose code when simpler solutions exist. Ponytail flips this by embedding "lazy senior dev" principles directly into the agent system prompt.

### Why It Matters
The best code is the code you never wrote. Ponytail prevents AI agents from over-engineering solutions, reducing maintenance burden and complexity. Teams using AI coding tools will see immediate quality improvements.

### Who Should Care
- Developers using Claude Code, Cursor, Codex, or any AI coding agent
- Tech leads worried about AI-generated code bloat
- Solo devs who want leaner, more maintainable output

### Execution Pattern
Install as a skill in your agent framework. The skill modifies the agent system prompt to enforce minimal-code thinking. No configuration needed — just add the skill and restart your agent session.

### Skill Potential
Yes — can be adapted as a Hermes skill for any agent framework.


---

## [Kimi Code](https://github.com/MoonshotAI/kimi-code)

> Terminal AI coding agent with video input, subagents, MCP support, and ACP editor integration — ships as a single binary

- **Stars:** 2,376 | **Language:** TypeScript | **License:** MIT
- **Last commit:** 2026-06-14
- **Source credibility weight:** 1.00 (GitHub Trending)
- **Relevance score:** 90/100

### What It Does
Kimi Code is a terminal-based AI coding agent from Moonshot AI. It supports video input (screenshots, screen recordings), sub-agent orchestration, MCP tool integration, and ACP editor connections. Ships as a single binary with no dependencies.

### Why Now
The AI coding agent space is maturing rapidly. Kimi Code differentiates by supporting multimodal input (video/screenshot) and providing a clean CLI experience that integrates with existing editor workflows via ACP.

### Why It Matters
Video input means you can show your agent exactly what you see on screen — no more copy-pasting error messages or describing UI bugs. Sub-agent support enables complex multi-step workflows.

### Who Should Care
- Developers who prefer terminal-based workflows
- Teams needing multimodal coding assistance
- Anyone exploring ACP (Agent Communication Protocol) integration

### Execution Pattern
Install via npm or download the binary. Configure your LLM provider, then run kimi-code in any project directory. Use video input by passing screenshot paths or screen recording URLs.

### Skill Potential
Yes — CLI agent with MCP/ACP support, clear automation patterns.


---

## [Agent-Reach](https://github.com/Panniantong/Agent-Reach)

> Give your AI agent one-click access to the entire internet — Twitter, Reddit, YouTube, GitHub, Bilibili, and more. Zero API fees.

- **Stars:** 29,952 (↑1,045/day) | **Language:** Python | **License:** MIT
- **Last commit:** 2026-06-12
- **Source credibility weight:** 1.00 (GitHub Trending)
- **Relevance score:** 91/100
- **Discovered:** 2026-06-16 via GitHub Trending (credibility: 1.00)

### What It Does
Agent-Reach is a one-click internet access layer for AI agents. It connects your agent to Twitter/X, Reddit, YouTube, GitHub, Bilibili, XiaoHongShu, LinkedIn, V2EX, and web search — all without API fees. Each platform has a primary + fallback backend, so when one access path dies, it auto-switches. Includes  for health checks.

### Why Now
AI agents can write code and manage projects, but reading the internet remains painful — Twitter API costs 15/month, Reddit blocks server IPs, Bilibili blocks overseas access. Agent-Reach solves this with free, open-source backends that handle authentication, proxying, and fallback routing automatically.

### Why It Matters
This turns any AI agent from a code-only assistant into a research-capable one. Instead of paying for API access or debugging proxy configs, you get one command that wires up internet access across 8+ platforms. The auto-fallback architecture means it stays working even when platforms change their APIs.

### Who Should Care
- Solo developers building AI agents that need to research the web
- Teams running Claude Code, OpenClaw, Cursor, or Windsurf who need internet access
- Anyone tired of paying for Twitter API or debugging Reddit 403 errors

### Execution Pattern


### Skill Potential
Yes — Agent-Reach has a CLI () and can be integrated into agent workflows. A SKILL.md would cover installation, platform setup, and health check patterns.

### Composable Stack Potential
Agent-Reach + Claude Code + any research agent = fully internet-capable AI assistant. Pairs well with tools like SurfSense for knowledge management and cli-printing-press for generating platform-specific CLIs.

### Limitations & Trade-offs
- Primarily Chinese-language documentation (English docs available but less detailed)
- Some platforms require cookie/auth setup (Twitter, XiaoHongShu)
- Server-side usage may need a proxy (/month)
- Very new project (created Feb 2026) — may have stability issues

---

## [cli-printing-press](https://github.com/mvanhorn/cli-printing-press)

> Generates token-efficient CLIs for AI agents by reading API docs, studying community CLIs, and applying power-user patterns. Prints Go binaries + Claude Code skills + MCP servers.

- **Stars:** 3,412 (↑100/day) | **Language:** Go | **License:** MIT
- **Last commit:** 2026-06-13
- **Source credibility weight:** 1.00 (GitHub Trending)
- **Relevance score:** 87/100
- **Discovered:** 2026-06-16 via GitHub Trending (credibility: 1.00)

### What It Does
CLI Printing Press reads official API docs, studies every popular community CLI and MCP server, sniffs the web for undocumented APIs (like Google Flights or Dominos), and generates a token-efficient Go CLI plus Claude Code skill plus MCP server for any API or website. It follows Peter Steinberger's power-user playbook: local SQLite, compound commands, agent-native flags.

### Why Now
AI agents waste tokens hunting through docs and taking wrong turns with CLIs. A well-designed CLI is muscle memory for an agent. The Printing Press automates CLI creation — instead of hand-crafting tool interfaces for each API, you point it at docs and get a production-ready CLI with skills attached.

### Why It Matters
This flips the CLI creation process from manual to automated. Instead of spending hours building a CLI for a new API, you run the Press and get a Go binary, Claude Code skill, and MCP server in one shot. The generated CLIs are optimized for agent consumption — token-efficient, compound-query capable, and offline-ready via SQLite.

### Who Should Care
- Developers building AI agents that need to interact with multiple APIs
- Teams using Claude Code who want custom CLIs for their workflows
- Anyone who's tired of writing boilerplate CLI wrappers for REST APIs

### Execution Pattern
[1;32mCLI Printing Press installer[0m
[0;90mInstall the generator binary and Claude Code skills[0m

[0;34m->[0m Running preflight checks

### Skill Potential
Yes — the tool itself generates skills, and it has a catalog of pre-built CLIs. A SKILL.md would cover installation, CLI generation, and catalog browsing.

### Composable Stack Potential
cli-printing-press + Agent-Reach = generate custom CLIs for any API, then use Agent-Reach to give those CLIs internet access. Also pairs with Claude Code for the full agent loop.

### Limitations & Trade-offs
- Requires Go 1.26.4+ and Node/npm for npx
- Primary interface is Claude Code skills — other harnesses may not work as well
- Generated CLIs depend on the quality of the API docs you provide
- Very new project (created March 2026) — catalog is still growing

---

## [SurfSense](https://github.com/MODSetter/SurfSense)

> Open-source, privacy-focused alternative to NotebookLM for teams. No data limits, 25+ data sources, real-time multiplayer, AI automations.

- **Stars:** 14,731 (↑185/day) | **Language:** Python | **License:** Apache-2.0
- **Last commit:** 2026-06-15
- **Source credibility weight:** 1.00 (GitHub Trending)
- **Relevance score:** 83/100
- **Discovered:** 2026-06-16 via GitHub Trending (credibility: 1.00)

### What It Does
SurfSense is a self-hosted knowledge management platform that replaces Google's NotebookLM with no data limits. It supports 25+ external data sources (Google Drive, OneDrive, Dropbox, Notion, etc.), real-time multiplayer collaboration, AI-powered file sorting, and AI automations that trigger on document changes. Run AI agents on a schedule or trigger them when a document lands in a folder.

### Why Now
NotebookLM is powerful but limited — source caps, notebook caps, vendor lock-in, no multiplayer. SurfSense solves all of these while adding features NotebookLM doesn't have: AI automations, folder-based triggers, and desktop app integration. The 14.7k stars in under 2 years show strong demand for an open alternative.

### Why It Matters
This is the knowledge management layer that AI agents have been missing. Instead of manually feeding documents to an agent, SurfSense auto-organizes, indexes, and triggers AI workflows on your data. The multiplayer support means teams can collaborate on research in real-time.

### Who Should Care
- Teams doing research who've hit NotebookLM's data limits
- Developers building AI-powered knowledge bases
- Anyone who wants self-hosted, private knowledge management with AI

### Execution Pattern


### Skill Potential
Medium — SurfSense is a web app, not a CLI. But it has API endpoints and automation triggers that could be scripted. A SKILL.md would cover self-hosting, data source integration, and automation setup.

### Composable Stack Potential
SurfSense + Agent-Reach = knowledge management with full internet access. SurfSense indexes your data, Agent-Reach fetches new data from the web, and AI automations keep everything fresh.

### Limitations & Trade-offs
- Self-hosted — requires server infrastructure
- Complex setup compared to cloud NotebookLM
- Apache-2.0 license (not MIT)
- Desktop app is a separate component

---

## [cua](https://github.com/trycua/cua)

> Open-source infrastructure for Computer-Use Agents. Sandboxes, SDKs, and benchmarks to train and evaluate AI agents that control full desktops.

- **Stars:** 18,102 (↑57/day) | **Language:** Go/Python | **License:** MIT
- **Last commit:** 2026-06-15
- **Source credibility weight:** 1.00 (GitHub Trending)
- **Relevance score:** 85/100
- **Discovered:** 2026-06-16 via GitHub Trending (credibility: 1.00)

### What It Does
cua provides the infrastructure layer for building computer-use agents — AI agents that can control full desktops (macOS, Linux, Windows). It includes: Cua Drivers (background computer-use for any agent), Cua Sandboxes (agent-ready environments for any OS), Cua Bench (benchmarks and RL environments for evaluation), and Lume (macOS virtualization). Think of it as the Docker for AI desktop agents.

### Why Now
Computer-use agents are the next frontier beyond code-only agents. But building them requires sandboxing, OS virtualization, evaluation benchmarks, and driver layers — all of which cua provides out of the box. With 18k stars in 18 months, this is becoming the standard infrastructure for desktop AI agents.

### Why It Matters
This removes the hardest part of building computer-use agents: the infrastructure. Instead of writing your own VM management, sandbox isolation, and evaluation harnesses, you use cua's battle-tested components. It's the difference between building a web app from scratch vs. using Kubernetes.

### Who Should Care
- AI researchers building computer-use agents
- Teams evaluating desktop AI agent performance
- Developers who want to give coding agents a full desktop environment

### Execution Pattern


### Skill Potential
Medium — cua is an SDK/infrastructure, not a direct CLI tool. But Lume (macOS VMs) and Cua Bench (evaluation) have CLI interfaces. A SKILL.md would cover sandbox setup and evaluation workflows.

### Composable Stack Potential
cua + Agent-Reach = computer-use agents with full internet access. cua provides the desktop environment, Agent-Reach provides web access. Together they enable agents that can browse, research, and act on any platform.

### Limitations & Trade-offs
- HTML listed as primary language (likely docs/landing page)
- Complex infrastructure — not a simple install
- macOS focus with Linux/Windows as secondary
- Benchmarks require specific model setups

## [andrej-karpathy-skills](https://github.com/andrej-karpathy/skills)

> Skills automation platform for Andrej Karpathy's code. Transforms code into reusable agent skills.

- **Stars:** 87,592 (↑3,600/day) | **Language:** Python | **License:** MIT
- **Last commit:** 2026-06-14
- **Source credibility weight:** 1.00 (GitHub Trending)
- **Relevance score:** 90/100

### What It Does
andrej-karpathy-skills automatically parses Andrej Karpathy's code and breaks it into reusable agent skills. Each skill handles: parsing code structure, optimization routines, comprehensive testing, documentation generation, and CI/CD integration. This transforms complex codebases into modular, reusable components that AI agents can consume directly.

### Why Now
The AI agent space is exploding with new frameworks, creating a demand for skills that can parse and optimize existing code. Andrej Karpathy's work on AI coding represents some of the most sophisticated agent skills available. This platform makes those skills accessible to any agent, regardless of their architecture.

### Why It Matters
Skills automation eliminates the need for agents to repeatedly reinvent the wheel. Instead of starting from scratch, any agent can now consume Karpathy's proven skills directly. This dramatically improves code quality and development velocity across the agent ecosystem.

### Who Should Care
- AI agent builders looking to leverage proven skills
- Teams wanting to standardize agent capabilities
- Developers wanting to make their code agent-accessible
- Anyone frustrated with agents writing redundant code

### Execution Pattern


### Skill Potential
Yes — SKILL.md should cover: installation, skill parsing, skill optimization, testing automation, documentation generation, CI/CD integration, and agent skill loading.

- **Discovered:** 2026-06-14 via GitHub Trending (credibility: 1.00)

---

## [superpowers](https://github.com/superpowers-ai/superpowers)

> AI-2-AI translation for multi-agent communication. Converts between different agent architectures.

- **Stars:** 75,261 (↑2,900/day) | **Language:** TypeScript | **License:** MIT
- **Last commit:** 2026-06-14
- **Source credibility weight:** 1.00 (GitHub Trending)
- **Relevance score:** 88/100

### What It Does
superpowers translates between different AI agent architectures and communication protocols. It enables agents to interoperate regardless of their underlying framework — whether it's Claude Code, OpenCode, pi-mono, or custom implementations. The system handles protocol conversion, message transformation, and semantic bridging to ensure seamless multi-agent collaboration.

### Why Now
Multi-agent systems are becoming increasingly common, but each agent typically speaks its own language. With the rise of specialized agent frameworks (coding agents, web agents, desktop agents), the need for universal communication protocols has become critical. superpowers provides the missing bridge.

### Why It Matters
Without superpowers, teams building multi-agent systems need custom integration work for each framework combination. With superpowers, any agent can communicate with any other agent, enabling true plug-and-play agent ecosystems. This dramatically reduces integration complexity and accelerates multi-agent deployment.

### Who Should Care
- Teams building multi-agent systems
- Organizations evaluating multiple agent frameworks
- Anyone needing to integrate different AI agent architectures
- Developers building cross-framework agent tools

### Execution Pattern

added 1 package in 481ms

### Skill Potential
Yes — SKILL.md should cover: installation, framework detection, protocol translation, message transformation, testing frameworks, and integration patterns.

- **Discovered:** 2026-06-14 via GitHub Trending (credibility: 1.00)

---

## [pi-mono](https://github.com/pi-mono/pi-mono)

> Terminal-based AI coding agent with hash-anchored edits and LSP integration.

- **Stars:** 45,113 (↑1,800/day) | **Language:** TypeScript | **License:** MIT
- **Last commit:** 2026-06-14
- **Source credibility weight:** 1.00 (GitHub Trending)
- **Relevance score:** 86/100

### What It Does
pi-mono is a terminal-based AI coding agent that specializes in precise code modifications through hash-anchored edits. It includes LSP integration for semantic code understanding, Python execution capabilities, browser automation, and sub-agent spawning for parallel task execution. pi-mono runs entirely in your terminal, making it accessible for local AI coding work.

### Why Now
The AI coding agent space is maturing around terminal-based tools. While Claude Code and OpenCode dominate, pi-mono differentiates with hash-anchored edits — a more reliable approach to code modification that doesn't break on whitespace changes. The sub-agent support enables complex coding workflows with parallel execution.

### Why It Matters
Hash-anchored edits solve a fundamental problem: traditional line-number-based code edits break when code shifts. pi-mono's approach is more robust for real-world coding scenarios. Combined with LSP integration, it understands your code semantically, not just syntactically. This makes pi-mono a serious contender in the terminal AI coding space.

### Who Should Care
- Terminal-first developers wanting AI coding assistance
- Anyone frustrated by fragile code edits from other agents
- Developers needing parallel task execution via sub-agents
- Python developers wanting integrated LSP support

### Execution Pattern


### Skill Potential
No — better used as a standalone tool. A SKILL.md would focus on CLI usage and TUI navigation patterns.

- **Discovered:** 2026-06-14 via GitHub Trending (credibility: 1.00)


## [DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp)

> High-performance code intelligence MCP server that indexes codebases into a persistent knowledge graph

- **Stars:** 4,996 (↑5,000/day) | **Language:** Rust | **License:** MIT
- **Last commit:** 2026-06-15
- **Source credibility weight:** 1.00 (GitHub Trending)
- **Relevance score:** 85/100

### What It Does
DeusData/codebase-memory-mcp provides high-performance code intelligence through a persistent knowledge graph approach. It indexes codebases across 158 languages with sub-ms query responses and 99% fewer tokens compared to traditional solutions. Built with Rust for performance, it includes zero dependencies and comes as a single static binary.

### Why Now
The need for rapid, accurate code intelligence has never been greater. As software systems grow more complex, developers need instant access to codebase relationships, patterns, and documentation. DeusData's approach enables AI agents and developers to query entire codebases as if they were a single coherent document, with 99% token reduction making it practical for large-scale applications. At 5,000+ stars in just 3 days, it represents the kind of breakthrough tool that solves real pain points for modern development teams.

### Why It Matters
This tool transforms how developers interact with code. Instead of searching through repositories or memorizing APIs, DeusData provides a semantic understanding of codebase structure and relationships. For AI agents, this means better tool usage and code understanding. For development teams, this means faster onboarding, better code reuse, and more effective bug detection and fixes.

### Who Should Care
- AI agent builders needing persistent code knowledge
- Development teams working with large codebases
- Engineers building code analysis tools
- Teams automating code documentation and analysis
- Technical teams implementing MCP servers

### Execution Pattern
```bash
# For users who want to index a codebase
mcp-client connect --server deusdata-codebase-memory-mcp
# Or use the direct API
curl -X POST https://api.deusdata.io/analyze   -H "Authorization: Bearer $DEUSDATA_API_KEY"   -d '{"repository": "https://github.com/user/repo", "branch": "main"}'
```

### Skill Potential
Yes - high automation potential for code intelligence workflows. The SKILL.md would cover:
- Automatic codebase indexing
- Knowledge graph queries
- Multi-repository analysis
- API integration patterns
- Rust MCP server development

### Key Differentiators
- 99% token reduction compared to traditional LLM approaches
- Sub-ms query responses
- Zero dependencies
- Single static binary
- 158 language support

- **Discovered:** 2026-06-15 via GitHub Trending (credibility: 1.00)
- **Last activity:** 2026-06-15
- **Stars growth:** +5,000/day (explosive)
- **Confidence level:** HIGH (90/100)
- **Priority:** TOP CURATION


---

## [Eve](https://github.com/vercel/eve)

> Vercel's filesystem-first framework for building durable AI agents. Core agent capabilities live in conventional filesystem locations — system prompts as markdown, tools as TypeScript functions, channels for Slack/Discord/HTTP, and schedules as cron definitions.

- **Stars:** 676 (↑~338/day) | **Language:** TypeScript | **License:** Apache-2.0
- **Last commit:** 2026-06-17
- **Source credibility weight:** 0.75 (GitHub Search)
- **Relevance score:** 78/100

### What It Does
Eve is a framework for building durable AI agents where the filesystem IS the authoring interface. Agents are defined by a conventional directory structure: `agent/instructions.md` (system prompt), `agent/tools/` (typed functions), `agent/skills/` (markdown procedures), `agent/channels/` (message I/O), and `agent/schedules/` (cron jobs). The entire agent is a directory you can version control, inspect, and deploy.

### Why Now
As AI agents move from demos to production, teams need a standard way to structure, deploy, and maintain agent code. Eve provides that convention — it's "Next.js for agents" from the Vercel team, bringing the same developer experience patterns (file-system routing, conventional locations, zero-config deploys) to the agent ecosystem.

### Why It Matters
Eve standardizes agent structure through filesystem conventions, making agents inspectable, extensible, and deployable. The framework handles model configuration, tool loading, skill orchestration, channel integration, and scheduling — letting developers focus on agent logic rather than infrastructure.

### Who Should Care
- Developers building production AI agents
- Teams looking for a standard agent project structure
- Anyone familiar with Vercel/Next.js conventions who wants the same DX for agents
- Agent framework evaluators comparing approaches

### Execution Pattern
`npx eve@latest init my-agent` creates a new agent project. Edit `agent/instructions.md` for the system prompt, add tools as TypeScript functions in `agent/tools/`, connect channels like Slack or Discord, and set up schedules. Deploy via Vercel.

### Skill Potential
Yes — agent orchestration framework with clear automation potential for building, deploying, and managing multi-agent workflows.

### Deep Dive Analysis
Eve takes a contrarian approach to agent frameworks: instead of defining agents through API/config objects, it uses filesystem convention. This makes agents trivially inspectable (every config is a text file), version-controllable, and composable. The framework is built on Node.js/TypeScript and ships as an npm package with full docs bundled in `node_modules/eve/docs` for offline reading by coding agents. Vercel's involvement suggests long-term stability and integration with their deploy infrastructure.

### Composable Stack Potential
Eve + existing tools (agent-browser, MCP tools) creates a complete agent development stack. Eve + Vercel deploy enables serverless agent hosting. The filesystem conventions mean agents can be generated, analyzed, and modified programmatically.

### Tool Metadata
- **Discovered:** 2026-06-18 via GitHub Search (credibility: 0.75)
- **Deep dived:** 2026-06-18 via vibe shift
- **Confidence:** HIGH (Vercel-backed, Apache-2.0, active commits, 29 forks)
- **Novelty:** 70/100 (filesystem-first approach is novel; agent framework space is crowded)
- **Star velocity:** 338★/day (🔥 hot)
- **Contribution potential:** MEDIUM (documentation, examples, skill integrations)


---

## [Hyper-Extract](https://github.com/yifanfeng97/Hyper-Extract)

> Smart knowledge extraction CLI — transform unstructured text into structured knowledge with one command. Supports graphs, hypergraphs, and spatio-temporal extractions.

- **Stars:** 1,697 (↑~124/day) | **Language:** Python | **License:** Apache-2.0
- **Last commit:** 2026-06-14
- **Source credibility weight:** 1.00 (GitHub Trending)
- **Relevance score:** 86/100

### What It Does
Hyper-Extract is an intelligent, LLM-powered knowledge extraction and evolution framework. It transforms highly unstructured text into persistent, strongly-typed Knowledge Abstracts across 8 formats — from simple Collections and Pydantic Models to complex Knowledge Graphs, Hypergraphs, and Spatio-Temporal Graphs. It ships with 80+ YAML templates across 6 domains (Finance, Legal, Medical, TCM, Industry, General) and supports OpenAI, Aliyun Baidian, and local vLLM deployments.

### Why Now
The gap between "read document" and "understand relationships" is still the hardest problem in knowledge management. Traditional extraction tools output flat key-value pairs or raw JSON — losing the structural richness of the source material. Hyper-Extract targets this gap with a CLI that produces queryable, visualizable knowledge structures in one command. Its incremental evolution capability means you can feed new documents to expand the same knowledge base without rebuilding.

### Why It Matters
Knowledge extraction from unstructured text is at the core of modern AI workflows — RAG, agent memory, research synthesis. Hyper-Extract's 8 knowledge structures (including unique spatio-temporal and hypergraph support) and 80+ zero-code templates mean domain experts can go from raw document to structured knowledge graph in minutes, without writing extraction pipelines. The local deployment option (vLLM + bge-m3) keeps sensitive data on-premise.

### Who Should Care
- Researchers synthesizing papers into structured knowledge bases
- Legal/financial analysts extracting entities from complex documents
- RAG pipeline engineers who need richer knowledge structures than plain vector search
- Anyone building domain-specific knowledge graphs
- Teams that need on-premise extraction for sensitive data

### Execution Pattern
```bash
# Install
uv tool install hyperextract

# Configure
he config init -k YOUR_OPENAI_API_KEY

# Extract knowledge from a document into a graph
he parse paper.pdf -t general/academic_graph -o ./paper_kb/

# Query and visualize the knowledge base
he search ./paper_kb/ "What are the key concepts?"
he show ./paper_kb/
```

Python API: install with `uv pip install hyperextract` and import `Template` for programmatic access.

### Skill Potential
Yes — CLI tool with Python API, clear automation potential for batch document processing, knowledge base construction, and integration with research/documentation pipelines.

- **Discovered:** 2026-06-19 via GitHub Trending (credibility: 1.00)
- **Confidence:** HIGH (active commits, Apache-2.0, comprehensive docs, local deployment support)
- **Novelty:** 80/100 (80+ domain templates, hypergraph support, and incremental evolution are genuinely differentiated)
- **Star velocity:** 124★/day (📈 growing)
