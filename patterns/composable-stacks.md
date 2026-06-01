

---

## Stack: Local AI Content Factory

**Components:** [Odysseus](https://github.com/pewdiepie-archdaemon/odysseus) + [HTML Anything](https://github.com/nexu-io/html-anything) + [SubForge](https://github.com/deusjin/subforge)

**What it enables:** A complete local-first AI content production pipeline: research and writing in Odysseus, visual output via HTML Anything, video localization via SubForge.

**Why it's composable:** Odysseus provides the AI workspace (chat, agents, memory), HTML Anything adds visual content generation (social cards, decks, reports), SubForge handles video subtitle production. Each tool is independent but they share the local-first philosophy and can be orchestrated via CLI/agent tools.

**Execution pattern:**
1. Use Odysseus deep research to gather sources and synthesize content
2. Pass content to HTML Anything via Claude Code/Codex to generate visual assets
3. Use SubForge to add subtitles to any video content
4. All tools run locally with zero cloud dependencies
