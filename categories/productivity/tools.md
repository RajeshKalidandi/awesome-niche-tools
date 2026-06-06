# ⚡ Productivity

> Tools that make you more productive — design extraction, workflow automation, and developer utilities.

---

## [Design-Extract](https://github.com/Manavarya09/design-extract)

> Extract any website's complete design system with one command. DTCG tokens, MCP server, multi-platform emitters.

- **Stars:** 2,958 (↑~30/day) | **Language:** JavaScript | **License:** MIT
- **Last commit:** 2026-05-28
- **Source credibility weight:** 0.90 (GitHub search)
- **Relevance score:** 76/100

### What It Does
Design-Extract analyzes any website and extracts its complete design system — colors, typography, spacing, components — as DTCG (Design Token Community Group) compliant tokens. It includes an MCP server for AI integration, multi-platform emitters (CSS, Tailwind v4, Figma variables), and a CSS audit engine. One command to go from "I like this design" to "I have the tokens."

### Why Now
Design systems are critical for consistent UI development, but extracting tokens from existing websites is manual and error-prone. Design-Extract automates this completely. The DTCG compliance means tokens work with modern design tools (Figma, Style Dictionary). The MCP server means AI agents can extract and apply design systems programmatically.

### Why It Matters
Instead of spending hours manually identifying colors, fonts, and spacing from a website, Design-Extract does it in seconds. The multi-platform output means you get CSS variables, Tailwind config, and Figma tokens from the same extraction. For teams adopting or migrating design systems, this is a massive time saver.

### Who Should Care
- Frontend developers adopting existing design systems
- Design teams documenting brand guidelines
- Agencies building sites that match client branding
- Anyone who's ever inspected a website to copy its colors

### Execution Pattern
```bash
# Install
npm install -g design-extract

# Extract design system from a website
design-extract https://stripe.com --output ./stripe-tokens

# Output includes:
# - tokens.json (DTCG compliant)
# - tokens.css (CSS custom properties)
# - tokens.tailwind.js (Tailwind v4 config)
# - tokens.figmat (Figma variables)

# Run as MCP server
design-extract serve --port 3003

# AI agent usage
# "Extract the design system from https://linear.app and apply it to my project"
```

### Skill Potential
Yes — SKILL.md should cover: installation, CLI usage, MCP server setup, token format options, and integration with frontend workflows.

- **Discovered:** 2026-05-29 via GitHub search (credibility: 0.90)


## [presenton](https://github.com/presenton/presenton)

> Open-Source AI Presentation Generator and API

- **Stars:** 7,300 (↑~1,740/week) | **Language:** TypeScript | **License:** Apache-2.0
- **Last commit:** 2026-05-28
- **Source credibility weight:** 1.00 (GitHub Trending)
- **Relevance score:** 82/100

### What It Does
Presenton is an open-source alternative to Gamma and Beautiful.ai. It generates professional presentations from text prompts using AI — slides, layouts, visuals, all automated. Includes a REST API for programmatic generation, making it possible to build presentation workflows into existing tools. Self-hostable with your own LLM backend.

### Why Now
AI presentation tools have exploded in popularity, but the market is dominated by closed SaaS products (Gamma, Beautiful.ai, Tome). Presenton brings this capability open-source with an API, meaning you can integrate AI presentation generation into your own tools. The Apache-2.0 license makes it safe for commercial use.

### Why It Matters
Instead of paying $10-20/month per seat for AI presentation tools, teams can self-host Presenton and generate unlimited presentations. The API means you can build custom workflows: "Turn my meeting notes into a deck" or "Generate a weekly status report as slides." It commoditizes AI presentation generation.

### Who Should Care
- Teams spending heavily on presentation SaaS tools
- Developers building document generation pipelines
- Content creators who need rapid slide creation
- Organizations with strict data privacy requirements (self-hosted)
- Anyone who's ever stared at a blank slide wondering where to start

### Execution Pattern
```bash
# Clone and install
git clone https://github.com/presenton/presenton.git
cd presenton
npm install

# Configure your LLM backend
cp .env.example .env
# Set your LLM API key or use local Ollama

# Start the server
npm run start

# Generate a presentation via API
curl -X POST http://localhost:3000/api/generate \
  -H "Content-Type: application/json" \
  -d '{"prompt": "Quarterly sales review for Q2 2026", "style": "professional"}'

# Output: download link to .pptx file
```

### Skill Potential
Yes — SKILL.md should cover: installation, LLM backend configuration, API usage, presentation styles, and integration with meeting tools.

- **Discovered:** 2026-05-29 via GitHub Trending (credibility: 1.00)


---

## [breathe-cli](https://github.com/marekkowalczyk/breathe-cli)

> Paced resonance breathing in your terminal — vagal tone training with clinical backing

- **Stars:** 155 (↑growing) | **Language:** Python | **License:** MIT
- **Last commit:** 2026-05-25
- **Source credibility weight:** 1.00 (GitHub Trending)
- **Relevance score:** 68/100

### What It Does
A terminal app that paces resonance breathing (6 breaths per minute) for vagal tone training. Displays a visual bar that guides inhale/exhale timing. Supports custom ratios, multiple presets (calm, balanced, extended), logging, and HRV biofeedback integration for finding personal resonance frequency. Single file, no dependencies, macOS only.

### Why Now
Resonance breathing is one of the few non-pharmacological interventions shown to improve cardiac vagal tone (Bernardi et al. 1998, 2002). This tool makes the practice frictionless for terminal users — open terminal, run breathe, follow the bar. The clinical backing distinguishes it from generic breathing apps.

### Why It Matters
For developers who spend hours at terminals, this adds a health practice to the existing workflow. The HRV biofeedback integration lets users find their personal resonance frequency, making the practice more effective than one-size-fits-all apps.

### Who Should Care
Terminal-native developers, health-conscious engineers, anyone with heart failure with reduced ejection fraction (HFrEF) following clinical breathing protocols, HRV biofeedback practitioners.

### Execution Pattern
Install via pip or Homebrew, run breathe in terminal, follow the visual bar. Use --ratio to customize timing, --preset for pre-configured modes, --log for session tracking. Pair with HRV hardware for resonance frequency testing.

### Skill Potential
No — this is a simple terminal app, not a CLI with automation potential.

- **Discovered:** 2026-06-01 via Lobsters (credibility: 0.85)


---

## [tuiboard](https://github.com/NazzarenoGiannelli/tuiboard)

> Terminal dashboard for markdown task boards — kanban + Today/Tomorrow + 24h timeline + Claude Code agent view

- **Stars:** 57 (↑new, created 2026-05-27) | **Language:** TypeScript | **License:** MIT
- **Last commit:** 2026-05-27
- **Source credibility weight:** 0.75 (GitHub Search)
- **Relevance score:** 65/100

### What It Does
A terminal dashboard that unifies kanban boards, a Today/Tomorrow virtual panel, a 24-hour agenda (with Google/Microsoft 365 calendar overlay), and a live agent view for Claude Code sessions — all on top of plain markdown task files. Built with OpenTUI + SolidJS on Bun. Cross-platform. No vendor lock-in: boards are CommonMark with Obsidian Tasks-plugin emoji vocabulary.

### Why Now
The convergence of AI coding agents and terminal-native workflows has created demand for dashboards that show both human tasks and agent status. tuiboard uniquely combines kanban project management with live Claude Code session monitoring in a single TUI.

### Why It Matters
This bridges the gap between project management and AI agent monitoring. Instead of switching between a kanban app and terminal to check agent status, you get both in one view. The markdown-based storage means tasks are editable anywhere.

### Who Should Care
Claude Code users, terminal-native project managers, teams using AI coding agents who need visibility into agent progress, developers who prefer TUIs over GUIs.

### Execution Pattern
Install via bun, create markdown files with ## columns and - [ ] tasks, point tuiboard at them via config.yaml. The agent view auto-discovers Claude Code sessions from ~/.claude/. Overlay calendar events for time-blocked work.

### Skill Potential
No — this is a terminal dashboard app, not a CLI with automation potential.

- **Discovered:** 2026-06-01 via GitHub Search (credibility: 0.75)


---

## [html-video](https://github.com/nexu-io/html-video)

> HTML→Video meta-layer for coding agents.

- **Stars:** 741 | **Language:** HTML | **License:** Apache-2.0
- **Last commit:** 2026-06-05
- **Source credibility weight:** 1.00 (GitHub trending discovery)
- **Relevance score:** 69/100

### What It Does
html-video turns HTML into video outputs suitable for agent pipelines. It serves as a meta-layer coding agents can call to render prototypes, demos, or marketing clips from structured markup.

### Why Now
Agents increasingly need multimodal outputs, not just text. HTML-to-video generation bridges structured markup and motion media in agent workflows.

### Why It Matters
It narrows the gap between a structured spec and a deliverable asset. Agents can ship a video instead of only text.

### Who Should Care
- Agencies using agents for content production
- Product teams wanting auto-generated walkthroughs
- Devs building agent pipelines that need motion deliverables
- Indie makers who ship videos

### Execution Pattern
```bash
# Render HTML spec to video through agent
html-video render ./walkthrough.html ./walkthrough.mp4
# Optional templates and timing flags
```

### Skill Potential
Yes — CLI/REST integration, template styling, agent output wiring, and rendering performance tips.

- **Discovered:** 2026-06-05 via GitHub trending discovery (credibility: 1.00)


---

## [Open Notebook](https://github.com/lfnovo/open-notebook)

> Open-source, privacy-focused alternative to Google NotebookLM with 18+ AI providers

- **Stars:** 25,984 (1,152 today) | **Language:** TypeScript | **License:** MIT
- **Last commit:** 2026-06-04
- **Source credibility weight:** 1.00 (GitHub Trending)
- **Relevance score:** 85/100
- **Discovered:** 2026-06-06 via GitHub Trending

### What It Does
Open Notebook is a self-hosted alternative to Google NotebookLM that lets you organize multi-modal content (PDFs, videos, audio, web pages), chat with your research using AI, and generate multi-speaker podcasts. Supports 18+ AI providers including OpenAI, Anthropic, Ollama, and LM Studio.

### Why Now
Google NotebookLM locked users into Google's ecosystem. Open Notebook fills the demand for a privacy-respecting, provider-flexible alternative. The 1,152 stars gained today signals strong community adoption of this niche.

### Why It Matters
If you use NotebookLM for research but want to keep your data private and choose your own AI provider, this is the only mature open-source option. The podcast generation feature (1-4 speakers with custom profiles) is ahead of Google's offering.

### Who Should Care
Researchers, knowledge workers, and anyone who uses LLM-powered note-taking but wants data sovereignty and provider flexibility.

### Execution Pattern
Clone the repo, configure your preferred AI provider in the settings, add content sources (URLs, PDFs, audio), and use the web UI to chat with your research or generate podcasts. Can be deployed via Docker.

### Skill Potential
Yes — could generate a SKILL.md for automating podcast generation from web content feeds, or for batch-processing research papers into a searchable knowledge base.
