# Automation Tools

> Workflow automation, scheduling, and orchestration.

| Tool | Stars | Language | Niche | Discovered |
|------|-------|----------|-------|------------|


---

## [SubForge](https://github.com/deusjin/subforge)

> Rust CLI for AI subtitle workflows: transcribe, segment, translate, evaluate, and burn or mux subtitles

- **Stars:** 40 (↑new, created 2026-05-28) | **Language:** Rust | **License:** MIT
- **Last commit:** 2026-05-28
- **Source credibility weight:** 1.00 (GitHub Trending)
- **Relevance score:** 70/100

### What It Does
A Rust CLI that turns video subtitle production into a reproducible AI pipeline. Transcribes audio via faster-whisper (CPU/CUDA), segments subtitles via SaT, translates using Google/Bing/OpenAI-compatible LLMs with chained or wave-based concurrent modes, evaluates quality via GEMBA-MQM, and burns or muxes subtitles via ffmpeg. Includes MAPS-style terminology extraction and project-level translation memory.

### Why Now
Subtitle production is a fragmented workflow involving multiple tools (whisper, ffmpeg, translation APIs, subtitle editors). SubForge unifies this into a single CLI pipeline. The Rust implementation makes it fast and the LLM translation backends make it adaptable to any quality tier.

### Why It Matters
For video creators, course translators, and localization teams, this eliminates the script-pile approach to subtitle production. The reproducible pipeline means consistent quality across projects. The terminology extraction and translation memory ensure consistency in domain-specific content.

### Who Should Care
Video creators doing localization, course/platform translators, content teams processing multiple videos, anyone doing batch subtitle work.

### Execution Pattern
Install via cargo, point at video files, run the pipeline: transcribe → segment → translate → evaluate → burn/mux. Configure translation backends and quality thresholds per project. Use translation memory for multi-video consistency.

### Skill Potential
Yes — SKILL.md would cover: pipeline configuration, translation backend selection, quality estimation tuning, batch processing workflows.

- **Discovered:** 2026-06-01 via GitHub Trending (credibility: 1.00)


---

## [harness-anything](https://github.com/yb2460/harness-anything)

> CLI harness for WPS Office — let AI agents control Writer, Calc & Impress via COM automation

- **Stars:** 210 (↑growing) | **Language:** Python | **License:** MIT
- **Last commit:** 2026-05-25
- **Source credibility weight:** 0.75 (GitHub Search)
- **Relevance score:** 66/100

### What It Does
A CLI toolkit that lets AI agents control WPS Office (and Microsoft Office) via COM automation on Windows. 47 CLI commands covering Writer (paragraphs, tables, images, find-replace), Calc (sheets, cells, formulas, batch fill), and Impress (slides, text boxes, shapes, export). Includes a PPT design system with 4 presets + 14 layouts + 5-dimension quality review. Also includes Zotero integration for academic research with 27 skills (literature search, paper writing, peer review, visualization).

### Why Now
AI coding agents can generate code, but controlling office software has remained manual. This tool bridges that gap by providing CLI commands that agents can invoke to manipulate documents, spreadsheets, and presentations directly. The academic Zotero integration is particularly novel.

### Why It Matters
This enables AI agents to produce real-world office documents instead of just code. An agent can now create a PowerPoint presentation, populate a spreadsheet, or format a Word document through CLI commands. The academic pipeline (literature search → paper writing → peer review) is a complete AI-assisted research workflow.

### Who Should Care
AI agent developers building office automation, academic researchers using Zotero, teams needing automated document generation, anyone wanting AI to produce polished office documents.

### Execution Pattern
Install via pip, use CLI commands to control WPS/Office: cli-anything-wps writer paragraph add "text" for Writer, cli-anything-wps calc cell set for Calc, cli-anything-wps impress slide add for Impress. For academic work, use cli-anything-zotero skills pipeline for complete research workflows.

### Skill Potential
Yes — SKILL.md would cover: COM automation setup, office command reference, academic pipeline configuration, PPT design system usage.

- **Discovered:** 2026-06-01 via GitHub Search (credibility: 0.75)
