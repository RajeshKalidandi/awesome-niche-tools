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
