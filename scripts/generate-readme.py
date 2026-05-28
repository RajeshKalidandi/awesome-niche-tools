#!/usr/bin/env python3
"""
Auto-generate README.md for awesome-niche-tools repo.
Scans categories/ and engineers/ directories, builds index.
"""

import os
from datetime import datetime
from pathlib import Path

BASE = Path(__file__).parent.parent
CATEGORIES_DIR = BASE / "categories"
ENGINEERS_DIR = BASE / "engineers"
DIGEST_DIR = BASE / "weekly-digest"

def count_tools(category_path):
    """Count tool entries in a category's tools.md."""
    tools_file = category_path / "tools.md"
    if not tools_file.exists():
        return 0
    lines = tools_file.read_text().splitlines()
    # Count lines that start with | and have a link (tool entry)
    return sum(1 for l in lines if l.startswith("| ") and "[ " in l)

def get_latest_digest():
    """Find the most recent weekly digest."""
    if not DIGEST_DIR.exists():
        return None
    digests = sorted(DIGEST_DIR.glob("*.md"), reverse=True)
    return digests[0] if digests else None

def build_readme():
    now = datetime.now()
    
    # Scan categories
    categories = []
    total_tools = 0
    for cat_dir in sorted(CATEGORIES_DIR.iterdir()):
        if cat_dir.is_dir():
            name = cat_dir.name.replace("-", " ").title()
            count = count_tools(cat_dir)
            total_tools += count
            categories.append((name, cat_dir.name, count))
    
    # Scan engineers
    engineer_count = 0
    if ENGINEERS_DIR.exists():
        engineer_count = len([f for f in ENGINEERS_DIR.glob("*.md") if f.name != "README.md"])
    
    # Get latest digest
    latest_digest = get_latest_digest()
    
    # Build README
    readme = f"""# 🔍 Awesome Niche Tools

> Curated open source tools for niche use cases — autonomously discovered and curated by AI agents.
>
> **Last updated:** {now.strftime("%Y-%m-%d %H:%M")} UTC

## 📊 Stats

- **Tools curated:** {total_tools}
- **Categories:** {len(categories)}
- **Engineers followed:** {engineer_count}
- **Discovery method:** Autonomous AI agent shifts (OpenCode)

## 📂 Categories

"""
    
    for name, slug, count in categories:
        emoji = {
            "ai-agents": "🤖",
            "dev-tools": "🛠️",
            "productivity": "⚡",
            "automation": "🔄",
            "selfhosted": "🏠",
        }.get(slug, "📦")
        readme += f"- [{emoji} {name}](categories/{slug}/tools.md) — {count} tools\n"
    
    readme += f"""
## 👤 Engineers

Follow top AI engineers and their projects: [engineers/](engineers/)

## 📰 Latest Digest

"""
    
    if latest_digest:
        readme += f"[{latest_digest.stem}](weekly-digest/{latest_digest.name})\n"
    else:
        readme += "_No digests yet — first shift will create one._\n"
    
    readme += f"""
## 🤖 How This Works

This repo is curated by **autonomous AI agent shifts**:

1. Every 3 hours, an agent wakes up
2. Crawls GitHub Trending, Hacker News, AI engineer feeds
3. Scores tools against a relevance framework
4. Curates top finds into categories
5. Generates SKILL.md files for automatable tools
6. Commits and pushes — all hands-free

Built with [Hermes Agent](https://github.com/RajeshKalidandi) + [OpenCode](https://opencode.ai) (free tier).

## 📝 Contributing

This repo is primarily agent-curated. If you find a niche tool worth including:
- Open an issue with the tool URL
- Or submit a PR following the entry format in any `tools.md`

## 📄 License

[MIT](LICENSE)
"""
    
    # Write README
    readme_path = BASE / "README.md"
    readme_path.write_text(readme)
    print(f"README.md generated: {total_tools} tools across {len(categories)} categories")

if __name__ == "__main__":
    build_readme()
