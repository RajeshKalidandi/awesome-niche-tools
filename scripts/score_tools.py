#!/usr/bin/env python3

import json
import math
from datetime import datetime, timedelta

# Define the research findings from multiple sources
research_sources = {
    'github_trending': [
        {'name': 'DeusData/codebase-memory-mcp', 
         'url': 'https://github.com/DeusData/codebase-memory-mcp',
         'stars': 4996, 
         'stars_today': 5000,
         'language': 'Rust',
         'license': 'MIT',
         'description': 'High-performance code intelligence MCP server that indexes codebases into a persistent knowledge graph',
         'source': 'GitHub Trending',
         'category': 'AI/ML',
         'last_commit_days': 3,
         'has_corroboration': 3,
         'novelty': 85,
         'execution': 80},
        {'name': 'obra/superpowers', 
         'url': 'https://github.com/obra/superpowers', 
         'stars': 231000, 
         'stars_today': 1205,
         'language': 'TypeScript',
         'license': 'MIT',
         'description': 'Agentic skills framework & software development methodology',
         'source': 'GitHub Trending',
         'category': 'AI/ML',
         'last_commit_days': 1,
         'has_corroboration': 2,
         'novelty': 70,
         'execution': 88},
        {'name': 'continuedev/continue', 
         'url': 'https://github.com/continuedev/continue',
         'stars': 33900, 
         'stars_today': 38,
         'language': 'Python',
         'license': 'MIT',
         'description': 'Open-source coding agent',
         'source': 'GitHub Trending',
         'category': 'AI/ML', 
         'last_commit_days': 2,
         'has_corroboration': 2,
         'novelty': 65,
         'execution': 82},
        {'name': 'Panniantong/Agent-Reach', 
         'url': 'https://github.com/Panniantong/Agent-Reach',
         'stars': 33000, 
         'stars_today': 1154,
         'language': 'Python',
         'license': 'MIT',
         'description': 'Gives AI agents eyes to see entire internet - reads across platforms',
         'source': 'GitHub Trending',
         'category': 'AI/ML',
         'last_commit_days': 2,
         'has_corroboration': 2,
         'novelty': 75,
         'execution': 76},
        {'name': 'n8n-io/n8n', 
         'url': 'https://github.com/n8n-io/n8n',
         'stars': 193000, 
         'stars_today': 1205,
         'language': 'TypeScript',
         'license': 'AGPL-3.0',
         'description': 'Fair-code workflow automation platform with native AI capabilities',
         'source': 'GitHub Trending',
         'category': 'Selfhosted',
         'last_commit_days': 1,
         'has_corroboration': 3,
         'novelty': 60,
         'execution': 85},
        {'name': 'meshery/meshery', 
         'url': 'https://github.com/meshery/meshery',
         'stars': 11000, 
         'stars_today': 199,
         'language': 'Go',
         'license': 'Apache-2.0',
         'description': 'Meshery, the cloud native manager',
         'source': 'GitHub Trending',
         'category': 'Dev Tools',
         'last_commit_days': 2,
         'has_corroboration': 2,
         'novelty': 70,
         'execution': 78}
    ],
    'hacker_news': [
        {'name': 'cuTile Rust', 
         'url': 'https://github.com/nvlabs/cutile-rs',
         'stars': 508, 
         'stars_today': 508,
         'language': 'Rust',
         'license': 'MIT',
         'description': 'Safe, tile-based GPU kernel programming DSL for Rust',
         'source': 'Hacker News Show HN',
         'category': 'Dev Tools',
         'last_commit_days': 30,
         'has_corroboration': 1,
         'novelty': 90,
         'execution': 85},
        {'name': 'Relaymux', 
         'url': 'https://github.com/mupt-ai/relaymux',
         'stars': 5, 
         'stars_today': 5,
         'language': 'TypeScript',
         'license': 'MIT',
         'description': 'Lightweight tmux-backed meta-harness for coding agents',
         'source': 'Hacker News Show HN',
         'category': 'Dev Tools',
         'last_commit_days': 60,
         'has_corroboration': 1,
         'novelty': 85,
         'execution': 75},
        {'name': 'High-Res Neural Cellular Automata', 
         'url': 'https://cells2pixels.github.io/',
         'stars': None, 
         'stars_today': None,
         'language': 'JavaScript',
         'license': 'MIT',
         'description': 'Advanced AI system that generates patterns at HD resolution in real-time using neural fields',
         'source': 'Hacker News Show HN',
         'category': 'AI/ML',
         'last_commit_days': 30,
         'has_corroboration': 1,
         'novelty': 80,
         'execution': 70}
    ],
    'arxiv': [
        {'name': 'MimicFunc', 
         'url': 'https://github.com/mkt1412/FUNCTO_public',
         'stars': 10, 
         'stars_today': 10,
         'language': 'Python',
         'license': 'MIT',
         'description': 'Framework for imitating tool manipulation from single human video',
         'source': 'arXiv',
         'category': 'AI/ML',
         'last_commit_days': 7,
         'has_corroboration': 2,
         'novelty': 95,
         'execution': 85},
        {'name': 'PhysToolBench', 
         'url': 'https://github.com/zxzhawa/PhysToolBench',
         'stars': 50, 
         'stars_today': 50,
         'language': 'Python',
         'license': 'MIT',
         'description': 'Benchmark for evaluating physical tool understanding by MLLMs',
         'source': 'arXiv',
         'category': 'AI/ML',
         'last_commit_days': 14,
         'has_corroboration': 2,
         'novelty': 90,
         'execution': 80},
        {'name': 'NNTile', 
         'url': 'https://github.com/starburst-benchmarking/nntile',
         'stars': 1000, 
         'stars_today': 1000,
         'language': 'C++',
         'license': 'Apache-2.0',
         'description': 'Machine learning framework for training large GPT language models on single node',
         'source': 'arXiv',
         'category': 'AI/ML',
         'last_commit_days': 21,
         'has_corroboration': 2,
         'novelty': 85,
         'execution': 75}
    ]
}

# Scoring framework
def calculate_base_score(tool):
    # Base scoring formula from skill
    # niche_fit × 0.25 + skill_potential × 0.25 + star_momentum × 0.20 + code_quality × 0.15 + community × 0.15
    
    # Simplified scoring based on available data
    niche_fit = min(tool.get('novelty', 50) / 100, 1.0) * 100
    skill_potential = min(tool.get('execution', 50) / 100, 1.0) * 100
    
    # Calculate star momentum (stars/day)
    days_old = max(tool.get('last_commit_days', 30), 1)
    star_momentum = min((tool.get('stars_today', 0) or 0) * 100 / days_old, 100)
    
    code_quality = 80  # default good score
    # Handle None values for community score
    stars = tool.get('stars') or 0
    community = min((stars / 10000) * 100, 100)
    
    base_score = (niche_fit * 0.25 + skill_potential * 0.25 + 
                  star_momentum * 0.20 + code_quality * 0.15 + 
                  community * 0.15)
    
    return round(base_score, 1)

def calculate_confidence_score(tool):
    # Confidence scoring
    sources = tool.get('has_corroboration', 1)
    last_commit = tool.get('last_commit_days', 30)
    star_velocity = tool.get('stars_today', 0) or 0
    
    confidence = 0
    if sources >= 2:
        confidence += 30
    elif sources == 1:
        confidence += 15
    
    if last_commit <= 7:
        confidence += 25
    elif last_commit <= 30:
        confidence += 15
    
    if star_velocity > 100:
        confidence += 25
    elif star_velocity > 10:
        confidence += 15
    elif star_velocity > 0:
        confidence += 10
    
    if tool.get('stars_today') is not None:
        confidence += 10  # Has recent activity
    
    return min(confidence, 100)

def get_confidence_level(score):
    if score >= 75:
        return 'HIGH'
    elif score >= 40:
        return 'MEDIUM'
    else:
        return 'LOW'

def apply_freshness_multiplier(base_score, tool, days_since_peak=None):
    # Freshness multiplier (half-life 14 days)
    if days_since_peak is None:
        days_since_peak = tool.get('last_commit_days', 30)
    
    # If stars_today is available and growing, set days_since_peak = 0
    if tool.get('stars_today', 0) and (tool.get('stars_today', 0) or 0) > 0:
        days_since_peak = 0
    
    freshness = math.exp(-math.log(2) * days_since_peak / 14)
    return round(base_score * freshness, 1)

# Calculate all scores
all_tools = []
for source_list in research_sources.values():
    for tool in source_list:
        all_tools.append(tool)

# Deduplicate by URL (same tool in multiple sources)
seen_urls = set()
unique_tools = []
for tool in all_tools:
    url_key = tool['url']
    if url_key not in seen_urls:
        seen_urls.add(url_key)
        unique_tools.append(tool)

# Apply scoring
final_tools = []
for tool in unique_tools:
    # Get source credibility weight
    source_weights = {'GitHub Trending': 1.00, 'Hacker News Show HN': 0.85, 'arXiv': 0.80, 'GitHub Search': 0.75}
    source_weight = source_weights.get(tool['source'], 0.75)
    
    # Calculate scores
    base_score = calculate_base_score(tool)
    confidence_score = calculate_confidence_score(tool)
    confidence_level = get_confidence_level(confidence_score)
    
    # Apply source credibility weight
    weighted_score = base_score * source_weight
    
    # Apply freshness multiplier
    final_score = apply_freshness_multiplier(weighted_score, tool)
    
    final_tool = {
        **tool,
        'base_score': base_score,
        'confidence_score': confidence_score,
        'confidence_level': confidence_level,
        'source_weight': source_weight,
        'final_score': final_score
    }
    final_tools.append(final_tool)

# Sort by final score
final_tools.sort(key=lambda x: x['final_score'], reverse=True)

# Print detailed results
print('=== FINAL SCORING RESULTS ===')
print(f'Total unique tools evaluated: {len(final_tools)}')
print()

for i, tool in enumerate(final_tools, 1):
    # Handle None values for printing
    stars_display = tool['stars'] or 0
    stars_today_display = tool['stars_today'] or 0
    
    print(f"{i}. **{tool['name']}** ({tool['final_score']}/100)")
    print(f"   URL: {tool['url']}")
    print(f"   Description: {tool['description']}")
    print(f"   Stars: {stars_display:,} (↑{stars_today_display:,}/day)")
    print(f"   Language: {tool['language']} | License: {tool['license']}")
    print(f"   Source: {tool['source']} (weight: {tool['source_weight']:.2f})")
    print(f"   Base score: {tool['base_score']}/100")
    print(f"   Confidence: {tool['confidence_score']}/100 ({tool['confidence_level']})")
    print(f"   Novelty: {tool['novelty']}/100")
    print(f"   Execution: {tool['execution']}/100")
    print(f"   Last commit: {tool['last_commit_days']} days ago")
    print(f"   Categories: {tool['category']}")
    print()

# Categorize by action thresholds
print('=== ACTION CATEGORIZATION ===')
curate_tools = []
log_roundup_tools = []
skip_tools = []

for tool in final_tools:
    if tool['final_score'] >= 80:
        curate_tools.append(tool)
    elif tool['final_score'] >= 60:
        log_roundup_tools.append(tool)
    else:
        skip_tools.append(tool)

print(f"\n🟢 CURATE (score 80+): {len(curate_tools)} tools")
for tool in curate_tools:
    print(f"  • {tool['name']} ({tool['final_score']}/100)")

print(f"\n🟡 LOG for roundup (score 60-79): {len(log_roundup_tools)} tools")
for tool in log_roundup_tools:
    print(f"  • {tool['name']} ({tool['final_score']}/100)")

print(f"\n🔴 SKIP (score <60): {len(skip_tools)} tools")
for tool in skip_tools:
    print(f"  • {tool['name']} ({tool['final_score']}/100)")

print(f"\n=== TOP 3 RECOMMENDATIONS ===")
for i, tool in enumerate(curate_tools[:3], 1):
    print(f"{i}. **{tool['name']}** - {tool['description']}")
    print(f"   Final score: {tool['final_score']}/100")
    print(f"   Confidence: {tool['confidence_level']}")
    print(f"   URL: {tool['url']}\n")

# Save results to JSON file
output = {
    'summary': {
        'total_unique_tools': len(final_tools),
        'curate_count': len(curate_tools),
        'log_roundup_count': len(log_roundup_tools),
        'skip_count': len(skip_tools)
    },
    'curate_tools': curate_tools,
    'log_roundup_tools': log_roundup_tools,
    'skip_tools': skip_tools,
    'all_tools_sorted': final_tools
}

with open('/root/awesome-niche-tools/scripts/scoring_results.json', 'w') as f:
    json.dump(output, f, indent=2)

print("Scoring results saved to /root/awesome-niche-tools/scripts/scoring_results.json")