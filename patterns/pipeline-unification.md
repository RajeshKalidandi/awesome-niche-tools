# Pipeline Unification Pattern

> When a single CLI tool replaces a fragmented chain of specialized tools into a reproducible pipeline.

## Problem

Many development workflows are chains of specialized tools glued together with scripts:
- Video subtitle production: whisper → segmentation → translation → quality check → ffmpeg
- Data processing: extract → transform → validate → load
- Content creation: research → draft → edit → format → publish

Each tool has its own interface, config format, error handling, and output format. The "glue scripts" between them are fragile, hard to reproduce, and impossible to share.

## Solution

A single CLI tool that:
1. **Owns the full pipeline** — each step is a subcommand or flag
2. **Standardizes interfaces** — consistent input/output formats between steps
3. **Manages state** — caching, intermediate files, and project memory
4. **Provides quality gates** — automatic validation between steps
5. **Supports composition** — steps can be run individually or as a full pipeline

## When to Use

- You find yourself writing the same 5-script chain for every project
- The tools in your chain all have different config formats
- You need reproducibility (same inputs → same outputs)
- You're processing batches of similar items (videos, data files, documents)
- Quality estimation or validation is part of the workflow

## When NOT to Use

- The pipeline steps are truly independent (no shared state or context)
- Each step requires fundamentally different runtime environments
- The workflow is exploratory, not production-oriented
- You only do the workflow once (not worth the abstraction)

## Discovered From

- **SubForge** (deusjin/subforge) — Unifies whisper + SaT + LLM translation + GEMBA-MQM + ffmpeg into a single Rust CLI for subtitle production
- **Crawl4AI** (unclecode/crawl4ai) — Unifies crawling, JS rendering, anti-bot bypass, and markdown extraction into one tool
- **Headroom** (chopratejas/headroom) — Unifies multiple compression algorithms (JSON, AST, prose) behind a single `compress()` interface

## Implementation Pattern

```bash
# The "before" — fragmented scripts
whisper video.mp4 --output raw.srt
python segment.py raw.srt > segmented.srt
python translate.py segmented.srt --target zh > translated.srt
python quality.py translated.srt > quality.json
ffmpeg -i video.mp4 -vf "subtitles=translated.srt" output.mp4

# The "after" — unified pipeline
subforge pipeline video.mp4 --target-lang zh --output final.mp4
```

## Key Design Principles

1. **Subcommand architecture**: `tool verb --options` instead of multiple scripts
2. **Intermediate format**: Standard format between steps (SRT, JSON, markdown)
3. **Cache-first**: Avoid re-processing unchanged inputs
4. **Quality gates**: Automatic validation between steps, with human review for low scores
5. **Project memory**: Persistent state across runs (terminology, preferences, history)

## Anti-Patterns

- ❌ **Monolithic**: Everything in one function — loses composability
- ❌ **Script glue**: Just wrapping existing tools in a shell script — no state management
- ❌ **Over-engineered**: Adding features nobody asked for — keep the pipeline focused
- ❌ **No quality gates**: Running the full pipeline without validation between steps

## Impact

Pipeline unification tools tend to:
- Reduce "time to first result" by 5-10x (no script assembly)
- Improve reproducibility (same config = same output)
- Enable batch processing (process 100 videos instead of 1)
- Create network effects (shared terminology databases, translation memory)

## Related Patterns

- [Token Economy Layer](token-economy-layer.md) — Compress before processing
- [MCP-First Integration](mcp-first-integration.md) — Standard tool protocol
- [Single Binary Distribution](single-binary-distribution.md) — No-dependency deployment
