# 🤖 AI Agents

> Infrastructure, frameworks, and tools for building and operating AI agents.

---

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
