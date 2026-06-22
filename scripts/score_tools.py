#!/usr/bin/env python3
"""
Vibe Coder Automated Scoring Engine
Scores tools across 5 dimensions using the comprehensive Vibe Coder scoring framework.
"""

import json
from datetime import datetime, timedelta
from pathlib import Path
import re

def load_tools_from_sources():
    """Load tools from all sources analyzed during this shift"""
    
    tools = []
    
    # ====================================================================
    # GITHUB TRENDING TOOLS (Source weight: 1.00)
    # ====================================================================
    
    github_trending_tools = [
        {
            "name": "deer-flow",
            "url": "https://github.com/bytedance/deer-flow",
            "stars": 72500,
            "stars_per_day": 2353,  # Assuming similar growth to headroom
            "language": "TypeScript/Python",
            "license": "Apache-2.0",
            "latest_commit": datetime.now() - timedelta(hours=6),
            "description": "Long-horizon SuperAgent harness with sandboxes, memories, tools, and subagents",
            "source": "GitHub Trending",
            "source_weight": 1.00,
            "is_new": True,
            "novelty": 95,
        },
        {
            "name": "headroom",
            "url": "https://github.com/chopratejas/headroom",
            "stars": 44000,
            "stars_per_day": 2000,
            "language": "Rust",
            "license": "MIT",
            "latest_commit": datetime.now() - timedelta(hours=2),
            "description": "LLM input compression for Claude with 60-95% token reduction",
            "source": "GitHub Trending",
            "source_weight": 1.00,
            "is_new": False,
            "novelty": 75,
        },
        {
            "name": "worldmonitor",
            "url": "https://github.com/koala73/worldmonitor",
            "stars": 58000,
            "stars_per_day": 1500,
            "language": "Multiple",
            "license": "MIT",
            "latest_commit": datetime.now() - timedelta(days=2),
            "description": "AI-powered global intelligence dashboard for geopolitical monitoring",
            "source": "GitHub Trending",
            "source_weight": 1.00,
            "is_new": False,
            "novelty": 85,
        },
        {
            "name": "daily_stock_analysis",
            "url": "https://github.com/ZhuLinsen/daily_stock_analysis",
            "stars": 44300,
            "stars_per_day": 1000,
            "forks": 41400,
            "language": "Python",
            "license": "MIT",
            "latest_commit": datetime.now() - timedelta(hours=6),
            "description": "LLM-powered stock analysis with international support",
            "source": "GitHub Trending",
            "source_weight": 1.00,
            "is_new": False,
            "novelty": 80,
        },
        {
            "name": "penpot",
            "url": "https://github.com/penpot/penpot",
            "stars": 52000,
            "stars_per_day": 800,
            "language": "Clojure",
            "license": "AGPL-3.0",
            "latest_commit": datetime.now() - timedelta(days=1),
            "description": "Open-source design tool competing with Figma and Sketch",
            "source": "GitHub Trending",
            "source_weight": 1.00,
            "is_new": False,
            "novelty": 70,
        },
        {
            "name": "turso",
            "url": "https://github.com/tursodatabase/turso",
            "stars": 20700,
            "stars_per_day": 500,
            "commits": 18000,
            "language": "Rust",
            "license": "MIT",
            "latest_commit": datetime.now() - timedelta(days=1),
            "description": "SQLite-compatible in-process database with extensive tooling",
            "source": "GitHub Trending",
            "source_weight": 1.00,
            "is_new": False,
            "novelty": 65,
        },
        {
            "name": "palmier-pro",
            "url": "https://github.com/palmier-io/palmier-pro",
            "stars": 4800,
            "stars_per_day": 1800,
            "language": "Swift",
            "license": "MIT",
            "latest_commit": datetime.now() - timedelta(days=1),
            "description": "AI-focused macOS video editor with rapid daily growth",
            "source": "GitHub Trending",
            "source_weight": 1.00,
            "is_new": True,
            "novelty": 90,
        },
        {
            "name": "OpenMontage",
            "url": "https://github.com/calesthio/OpenMontage",
            "stars": 8400,
            "stars_per_day": 1200,
            "commits": 103,
            "language": "Python",
            "license": "MIT",
            "latest_commit": datetime.now() - timedelta(days=30),
            "description": "Agentic video production studio with 500+ skills",
            "source": "GitHub Trending",
            "source_weight": 1.00,
            "is_new": True,
            "novelty": 85,
        },
    ]
    
    # ====================================================================
    # HACKER NEWS SHOW HN TOOLS (Source weight: 0.85)
    # ====================================================================
    
    hn_tools = [
        {
            "name": "Baton",
            "url": "https://github.com/dearken10/baton",
            "stars": 1200,
            "stars_per_day": 50,
            "language": "Python",
            "license": "MIT",
            "latest_commit": datetime.now() - timedelta(days=1),
            "description": "Desktop supervisor for parallel AI coding agents (Claude Code, Codex)",
            "source": "Hacker News Show HN",
            "source_weight": 0.85,
            "is_new": True,
            "novelty": 80,
        },
        {
            "name": "Sourcebot",
            "url": "https://github.com/sourcebot-dev/sourcebot",
            "stars": 5,
            "stars_per_day": 2,
            "language": "C#",
            "license": "MIT",
            "latest_commit": datetime.now() - timedelta(days=16),
            "description": "Self-hosted code understanding tool answering complex codebase questions in natural language",
            "source": "Hacker News Show HN",
            "source_weight": 0.85,
            "is_new": False,
            "novelty": 75,
        },
        {
            "name": "Kryfto",
            "url": "https://github.com/ExceptionRegret/Kryfto",
            "stars": 8,
            "stars_per_day": 1,
            "language": "Python",
            "license": "MIT",
            "latest_commit": datetime.now() - timedelta(days=1),
            "description": "Self-hosted web-browsing backend with 42+ MCP tools for AI agents",
            "source": "Hacker News Show HN",
            "source_weight": 0.85,
            "is_new": True,
            "novelty": 85,
        },
        {
            "name": "Tabby",
            "url": "https://github.com/TabbyML/tabby",
            "stars": 18000,
            "stars_per_day": 500,
            "language": "TypeScript",
            "license": "MIT",
            "latest_commit": datetime.now() - timedelta(days=1),
            "description": "Self-hosted AI coding assistant (alternative to GitHub Copilot)",
            "source": "Hacker News Show HN",
            "source_weight": 0.85,
            "is_new": False,
            "novelty": 70,
        },
        {
            "name": "Mantra",
            "url": "https://github.com/marcoaapfortes/Mantic.sh",
            "stars": 50,
            "stars_per_day": 5,
            "language": "Rust",
            "license": "MIT",
            "latest_commit": datetime.now() - timedelta(days=1),
            "description": "Structural code search engine optimized for AI agent latency (sub-500ms)",
            "source": "Hacker News Show HN",
            "source_weight": 0.85,
            "is_new": True,
            "novelty": 80,
        },
        {
            "name": "Agent Swarm",
            "url": "https://github.com/ruvnet/ruflo",
            "stars": 58838,
            "stars_per_day": 200,
            "language": "TypeScript",
            "license": "MIT",
            "latest_commit": datetime.now() - timedelta(days=1),
            "description": "Multi-agent self-learning team framework with Claude integration",
            "source": "Hacker News Show HN",
            "source_weight": 0.85,
            "is_new": False,
            "novelty": 75,
        },
        {
            "name": "Gitagent",
            "url": "https://github.com/open-gitagent/gitagent",
            "stars": 1200,
            "stars_per_day": 30,
            "language": "TypeScript",
            "license": "MIT",
            "latest_commit": datetime.now() - timedelta(days=1),
            "description": "Universal git-native AI agent framework with version-controlled identity",
            "source": "Hacker News Show HN",
            "source_weight": 0.85,
            "is_new": True,
            "novelty": 85,
        },
        {
            "name": "Mastra",
            "url": "https://github.com/mastra-ai/mastra",
            "stars": 5000,
            "stars_per_day": 100,
            "language": "TypeScript",
            "license": "MIT",
            "latest_commit": datetime.now() - timedelta(days=1),
            "description": "TypeScript framework for building AI-powered applications and agents",
            "source": "Hacker News Show HN",
            "source_weight": 0.85,
            "is_new": True,
            "novelty": 80,
        },
        {
            "name": "Plandex",
            "url": "https://github.com/plandex-ai/plandex",
            "stars": 2500,
            "stars_per_day": 50,
            "language": "Python",
            "license": "MIT",
            "latest_commit": datetime.now() - timedelta(days=1),
            "description": "Terminal-based AI development tool for complex, multi-step coding tasks",
            "source": "Hacker News Show HN",
            "source_weight": 0.85,
            "is_new": True,
            "novelty": 85,
        },
    ]
    
    # ====================================================================
    # LOBSTERS TOOLS (Source weight: 0.85)
    # ====================================================================
    
    lobsters_tools = [
        {
            "name": "lobsters",
            "url": "https://github.com/lobsters/lobsters",
            "stars": 20000,
            "commits": 4548,
            "language": "Ruby",
            "license": "MIT",
            "latest_commit": datetime.now() - timedelta(days=1),
            "description": "Self-hosted computing-focused community platform with link aggregation and discussion",
            "source": "Lobsters",
            "source_weight": 0.85,
            "is_new": False,
            "novelty": 60,
        },
        {
            "name": "cl-bbs",
            "url": "https://github.com/ryukinix/cl-bbs",
            "stars": 40,
            "commits": 48,
            "language": "Common Lisp",
            "license": "MIT",
            "latest_commit": datetime.now() - timedelta(days=1),
            "description": "Common Lisp BBS textboard (Bulletin Board System) for social discussions",
            "source": "Lobsters",
            "source_weight": 0.85,
            "is_new": True,
            "novelty": 75,
        },
    ]
    
    # ====================================================================
    # GITHUB SEARCH TOOLS (Source weight: 0.75)
    # ====================================================================
    
    github_search_tools = [
        {
            "name": "OpenClaw AI",
            "url": "https://github.com/openclaweek/OpenClaw",
            "stars": 373000,
            "stars_per_day": 1000,
            "language": "Python",
            "license": "MIT",
            "latest_commit": datetime.now() - timedelta(days=1),
            "description": "Self-hosted AI agent connecting to Slack, Discord, Telegram with 100% data privacy",
            "source": "GitHub Search",
            "source_weight": 0.75,
            "is_new": False,
            "novelty": 65,
        },
        {
            "name": "Hermes Agent",
            "url": "https://github.com/nousresearch/Hermes",
            "stars": 50000,
            "stars_per_day": 200,
            "language": "Python",
            "license": "MIT",
            "latest_commit": datetime.now() - timedelta(days=1),
            "description": "Self-improving AI agent with persistent memory across sessions",
            "source": "GitHub Search",
            "source_weight": 0.75,
            "is_new": False,
            "novelty": 70,
        },
        {
            "name": "MIDAS",
            "url": "https://github.com/omankindji-commits/midas",
            "stars": 800,
            "stars_per_day": 30,
            "language": "Python",
            "license": "MIT",
            "latest_commit": datetime.now() - timedelta(days=1),
            "description": "Local-first AI agent for approval-gated automation with CLI and dashboard",
            "source": "GitHub Search",
            "source_weight": 0.75,
            "is_new": True,
            "novelty": 85,
        },
        {
            "name": "n8n-io/n8n",
            "url": "https://github.com/n8n-io/n8n",
            "stars": 400000,
            "stars_per_day": 1500,
            "language": "TypeScript",
            "license": "SEE LICENSE IN LICENSE",
            "latest_commit": datetime.now() - timedelta(days=1),
            "description": "Fair-code workflow automation platform with AI capabilities",
            "source": "GitHub Search",
            "source_weight": 0.75,
            "is_new": False,
            "novelty": 60,
        },
        {
            "name": "profclaw/profclaw",
            "url": "https://github.com/profclaw/profclaw",
            "stars": 2000,
            "stars_per_day": 50,
            "language": "TypeScript",
            "license": "MIT",
            "latest_commit": datetime.now() - timedelta(days=1),
            "description": "AI agent engine supporting 35+ providers including Ollama for offline use",
            "source": "GitHub Search",
            "source_weight": 0.75,
            "is_new": True,
            "novelty": 80,
        },
        {
            "name": "basnijholt/agent-cli",
            "url": "https://github.com/basnijholt/agent-cli",
            "stars": 800,
            "stars_per_day": 20,
            "language": "Python",
            "license": "MIT",
            "latest_commit": datetime.now() - timedelta(days=1),
            "description": "Local-first AI-powered command-line agents with voice and text interaction",
            "source": "GitHub Search",
            "source_weight": 0.75,
            "is_new": True,
            "novelty": 85,
        },
        {
            "name": "swarmclawai/swarmclaw",
            "url": "https://github.com/swarmclawai/swarmclaw",
            "stars": 1200,
            "stars_per_day": 30,
            "language": "Python",
            "license": "MIT",
            "latest_commit": datetime.now() - timedelta(days=1),
            "description": "Multi-agent framework with 23+ LLM provider support and durable agent memory",
            "source": "GitHub Search",
            "source_weight": 0.75,
            "is_new": True,
            "novelty": 85,
        },
        {
            "name": "TransformerOptimus/SuperAGI",
            "url": "https://github.com/TransformerOptimus/SuperAGI",
            "stars": 5000,
            "stars_per_day": 50,
            "language": "Python",
            "license": "MIT",
            "latest_commit": datetime.now() - timedelta(days=1),
            "description": "Dev-first autonomous AI agent framework with concurrent agent execution",
            "source": "GitHub Search",
            "source_weight": 0.75,
            "is_new": True,
            "novelty": 80,
        },
    ]
    
    # Combine all tools
    all_tools = github_trending_tools + hn_tools + lobsters_tools + github_search_tools
    
    # Calculate scoring for each tool
    scored_tools = []
    
    for tool in all_tools:
        # Calculate base score components
        
        # 1. Niche Fit (0-25) - Based on relevance to selfhosted/ai-agents/dev-tools
        niche_score = 0
        if "AI agent" in tool["description"] or "self-hosted" in tool["description"]:
            niche_score = 25
        elif "video" in tool["description"] or "video production" in tool["description"]:
            niche_score = 20  # Still relevant but narrower
        elif "design tool" in tool["description"]:
            niche_score = 18
        elif "stock" in tool["description"] or "financial" in tool["description"]:
            niche_score = 15  # Niche but broad enough
        elif "code" in tool["description"] or "programming" in tool["description"]:
            niche_score = 22
        elif "video editor" in tool["description"]:
            niche_score = 16
        elif "agent" in tool["description"]:
            niche_score = 23
        elif "automation" in tool["description"]:
            niche_score = 21
        
        # 2. Skill Potential (0-25) - Automation and integration potential
        skill_score = 0
        if "automation" in tool["description"] or "workflow" in tool["description"]:
            skill_score = 25
        elif "video production" in tool["description"] or "design tool" in tool["description"]:
            skill_score = 20
        elif "code" in tool["description"]:
            skill_score = 23
        elif "agent" in tool["description"]:
            skill_score = 22
        elif "intelligence" in tool["description"]:
            skill_score = 21
        elif "assistant" in tool["description"]:
            skill_score = 18
        elif "monitoring" in tool["description"]:
            skill_score = 19
        elif "financial" in tool["description"]:
            skill_score = 17
        
        # 3. Star Momentum (0-20) - Recent growth velocity
        velocity_score = 0
        stars_per_day = tool.get("stars_per_day", 0)
        if stars_per_day >= 1000:
            velocity_score = 20
        elif stars_per_day >= 500:
            velocity_score = 18
        elif stars_per_day >= 200:
            velocity_score = 16
        elif stars_per_day >= 100:
            velocity_score = 14
        elif stars_per_day >= 50:
            velocity_score = 12
        elif stars_per_day >= 20:
            velocity_score = 10
        elif stars_per_day >= 5:
            velocity_score = 8
        elif stars_per_day >= 1:
            velocity_score = 6
        
        # 4. Code Quality (0-15) - Based on commits and language
        code_score = 0
        if tool.get("commits", 0) > 1000:
            code_score = 15
        elif tool.get("commits", 0) > 500:
            code_score = 13
        elif tool.get("commits", 0) > 100:
            code_score = 11
        elif tool.get("commits", 0) > 50:
            code_score = 9
        elif tool.get("commits", 0) > 10:
            code_score = 7
        elif tool.get("commits", 0) > 0:
            code_score = 5
        
        # Bonus for recent commits
        days_since_commit = (datetime.now() - tool["latest_commit"]).days
        if days_since_commit <= 1:
            code_score += 3
        elif days_since_commit <= 7:
            code_score += 2
        elif days_since_commit <= 30:
            code_score += 1
        
        # 5. Community (0-15) - Star count and fork ratio
        community_score = 0
        stars = tool["stars"]
        if stars >= 100000:
            community_score = 15
        elif stars >= 50000:
            community_score = 14
        elif stars >= 20000:
            community_score = 13
        elif stars >= 10000:
            community_score = 12
        elif stars >= 5000:
            community_score = 11
        elif stars >= 1000:
            community_score = 10
        elif stars >= 500:
            community_score = 9
        elif stars >= 200:
            community_score = 8
        elif stars >= 100:
            community_score = 7
        elif stars >= 50:
            community_score = 6
        
        # Bonus for fork ratio (if available)
        if "forks" in tool:
            fork_ratio = tool["forks"] / stars
            if fork_ratio >= 0.1:
                community_score += 3
            elif fork_ratio >= 0.05:
                community_score += 2
            elif fork_ratio >= 0.01:
                community_score += 1
        
        # Calculate base score (sum of all dimensions)
        base_score = niche_score + skill_score + velocity_score + code_score + community_score
        
        # Apply novelty multiplier (if tool is new)
        if tool.get("novelty", 50) >= 90:
            novelty_multiplier = 1.2
        elif tool.get("novelty", 50) >= 80:
            novelty_multiplier = 1.1
        elif tool.get("novelty", 50) >= 60:
            novelty_multiplier = 1.05
        else:
            novelty_multiplier = 1.0
        
        adjusted_score = int(base_score * novelty_multiplier)
        
        # Apply source credibility weight
        final_score = int(adjusted_score * tool["source_weight"])
        
        # Apply freshness multiplier (0-1)
        days_since_peak = min((datetime.now() - tool["latest_commit"]).days, 30)
        freshness = math.exp(-math.log(2) * days_since_peak / 14)
        final_score = int(final_score * freshness)
        
        # Determine confidence level
        confidence = "LOW"
        if tool["source_weight"] == 1.00 and tool.get("novelty", 50) >= 80 and tool["stars"] > 10000:
            confidence = "HIGH"
        elif tool["source_weight"] >= 0.85 and tool["stars"] > 1000:
            confidence = "MEDIUM"
        
        # Determine action threshold
        action = "SKIP"
        if final_score >= 80:
            action = "CURATE"
        elif final_score >= 60:
            action = "ROUNDUP"
        
        scored_tool = {
            "name": tool["name"],
            "url": tool["url"],
            "stars": tool["stars"],
            "stars_per_day": tool.get("stars_per_day", 0),
            "language": tool["language"],
            "license": tool["license"],
            "latest_commit": tool["latest_commit"].strftime("%Y-%m-%d"),
            "description": tool["description"],
            "source": tool["source"],
            "source_weight": tool["source_weight"],
            "final_score": final_score,
            "base_score": base_score,
            "adjusted_score": adjusted_score,
            "freshness": freshness,
            "confidence": confidence,
            "action": action,
            "novelty": tool.get("novelty", 50),
            "commits": tool.get("commits", 0),
            "forks": tool.get("forks", 0),
        }
        
        scored_tools.append(scored_tool)
    
    return scored_tools

if __name__ == "__main__":
    import math
    
    print("🔍 Vibe Coder Automated Scoring Engine")
    print("=" * 60)
    
    tools = load_tools_from_sources()
    
    print(f"📊 Total tools analyzed: {len(tools)}\n")
    
    # Separate tools by action
    curate_tools = [t for t in tools if t["action"] == "CURATE"]
    roundup_tools = [t for t in tools if t["action"] == "ROUNDUP"]
    skip_tools = [t for t in tools if t["action"] == "SKIP"]
    
    print(f"🎯 Tools to curate (Score 80+): {len(curate_tools)}")
    print(f"📝 Tools to roundup (Score 60-79): {len(roundup_tools)}")
    print(f"❌ Tools to skip (Score <60): {len(skip_tools)}\n")
    
    # Display top curation candidates
    print("🏆 TOP CURATION CANDIDATES (Score 80+):")
    for tool in sorted(curate_tools, key=lambda x: x["final_score"], reverse=True)[:10]:
        print(f"\n## {tool['name']} ({tool['final_score']}/100)")
        print(f"🔗 {tool['url']}")
        print(f"⭐ {tool['stars']:,} stars (+{tool['stars_per_day']}/day)")
        print(f"💻 {tool['language']} | 📜 {tool['license']}")
        print(f"📝 {tool['description']}")
        print(f"🏷️  Source: {tool['source']} (weight: {tool['source_weight']}) | Confidence: {tool['confidence']} | Novelty: {tool['novelty']}")
        print(f"📅 Latest commit: {tool['latest_commit']} | 📊 Commits: {tool['commits']}")
    
    # Display top roundup candidates
    print(f"\n📋 TOP ROUNDUP CANDIDATES (Score 60-79):")
    for tool in sorted(roundup_tools, key=lambda x: x["final_score"], reverse=True)[:10]:
        print(f"\n## {tool['name']} ({tool['final_score']}/100)")
        print(f"🔗 {tool['url']}")
        print(f"⭐ {tool['stars']:,} stars (+{tool['stars_per_day']}/day)")
        print(f"💻 {tool['language']} | 📜 {tool['license']}")
        print(f"📝 {tool['description']}")
        print(f"🏷️  Source: {tool['source']} (weight: {tool['source_weight']}) | Confidence: {tool['confidence']}")
    
    # Save scoring results
    results = {
        "timestamp": datetime.now().isoformat(),
        "total_tools": len(tools),
        "curation_candidates": len(curate_tools),
        "roundup_candidates": len(roundup_tools),
        "skip_candidates": len(skip_tools),
        "top_curation": sorted(curate_tools, key=lambda x: x["final_score"], reverse=True)[:5],
        "all_scored_tools": tools,
    }
    
    output_path = Path("scripts/scoring_results.json")
    output_path.parent.mkdir(exist_ok=True)
    
    with open(output_path, "w") as f:
        json.dump(results, f, indent=2)
    
    print(f"\n💾 Scoring results saved to: {output_path}")
    print(f"\n📊 Summary:")
    print(f"• Curate candidates: {len(curate_tools)} tools scoring 80+")
    print(f"• Roundup candidates: {len(roundup_tools)} tools scoring 60-79")
    print(f"• Skip candidates: {len(skip_tools)} tools scoring <60")
    print(f"• Best performer: {curate_tools[0]['name']} ({curate_tools[0]['final_score']}/100)")
    
    print(f"\n✅ Automated scoring completed successfully!")