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
