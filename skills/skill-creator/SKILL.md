---
name: skill-creator
description: "Turn any MCP server, OpenAPI spec, or GraphQL endpoint into an AI agent skill at runtime"
version: 1.0.0
author: Hermes Agent
license: MIT
platforms: [linux, macos]
metadata:
  hermes:
    tags: [skill-generation, mcp, openapi, graphql, automation]
    related_skills: [hermes-agent]
---

# Skill Creator — Auto-Generate Agent Skills from APIs

Generate reusable AI agent skills from MCP servers, OpenAPI specs, or GraphQL endpoints. Supports 9+ agent frameworks with an auto-improvement loop.

## Prerequisites

- Node.js 18+
- Access to an MCP server, OpenAPI spec, or GraphQL endpoint

## Installation

```bash
# Install via npm
npm install -g skill-creator

# Or clone and build
git clone https://github.com/sandiiarov/skill-creator.git
cd skill-creator
npm install && npm run build
```

## Usage

### From MCP Server

```bash
# Generate skill from running MCP server
skill-creator from-mcp --server http://localhost:3000 --output ./skills/my-mcp

# Generate with custom agent framework
skill-creator from-mcp --server http://localhost:3000 --framework claude-code
```

### From OpenAPI Spec

```bash
# Generate from OpenAPI JSON/YAML
skill-creator from-openapi --spec ./api-spec.yaml --output ./skills/my-api

# Generate with authentication
skill-creator from-openapi --spec ./api-spec.yaml --auth bearer:TOKEN
```

### From GraphQL

```bash
# Generate from GraphQL endpoint
skill-creator from-graphql --endpoint https://api.example.com/graphql --output ./skills/my-graphql
```

### Auto-Improvement Loop

```bash
# Run the improvement loop
skill-creator improve --skill ./skills/my-api --iterations 5

# This will:
# 1. Test the skill against real usage
# 2. Collect gotchas and edge cases
# 3. Update the skill documentation
# 4. Repeat for specified iterations
```

## Generated Output

Each generated skill includes:
- `SKILL.md` with Hermes-compatible frontmatter
- Usage examples with error handling
- Gotcha documentation from runtime testing
- Integration instructions for target framework

## Common Pitfalls

- **Spec quality**: Garbage in, garbage out. Ensure your OpenAPI spec is well-defined.
- **Authentication**: Some endpoints require auth that can't be automated. Handle manually.
- **Rate limits**: Auto-improvement loop may hit API rate limits. Add delays between iterations.

## Verification

```bash
# Verify generated skill
cat ./skills/my-api/SKILL.md

# Test the skill works
skill-creator test --skill ./skills/my-api --dry-run
```
