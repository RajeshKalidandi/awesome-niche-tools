---
name: hyper-extract
description: "LLM-powered knowledge extraction CLI — transform unstructured text into structured knowledge (graphs, hypergraphs, spatio-temporal graphs) with a single command."
version: 1.0.0
author: Hermes Agent
license: Apache-2.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [knowledge-extraction, knowledge-graph, nlp, llm, document-processing, rag]
    related_skills: [alibaba-zvec, dspy, youtube-content]
---

# Hyper-Extract — Smart Knowledge Extraction CLI

Transform unstructured text into structured, queryable knowledge with a single CLI command. Supports 8 knowledge structures (lists, models, graphs, hypergraphs, temporal/spatial graphs), 80+ domain templates, and 10+ extraction engines.

## Prerequisites

- Python 3.11+
- An LLM API key (OpenAI, Aliyun, or local vLLM deployment)
- `uv` package manager (recommended) or `pip`

## Installation

```bash
# Recommended: via uv tool
uv tool install hyperextract

# Or via pip
pip install hyperextract
```

## Quick Start

### 1. Configuration

```bash
# Initialize config with your API key
he config init -k YOUR_OPENAI_API_KEY

# Or set environment variable
export HYPEREXTRACT_API_KEY=your_key
```

### 2. Extract Knowledge from a Document

```bash
# Parse a markdown file into a biography knowledge graph
he parse examples/en/tesla.md -t general/biography_graph -o ./output/ -l en

# Parse a PDF into an academic knowledge graph
he parse paper.pdf -t general/academic_graph -o ./paper_kb/
```

### 3. Query and Visualize

```bash
# Query the knowledge base
he search ./output/ "What are the major achievements?"

# Visualize as an interactive graph
he show ./output/
```

## Usage Patterns

### Python API for Programmatic Access

```python
from hyperextract import Template

# Load a template
ka = Template.create("finance/earnings_graph")

# Parse document content
with open("earnings_report.md") as f:
    result = ka.parse(f.read())

# Access structured output
print(result.entities)
print(result.relations)

# Visualize
result.show()
```

### Using Different Knowledge Structures

Hyper-Extract supports 8 knowledge types:

| Structure | Template Prefix | Use Case |
|-----------|----------------|----------|
| Collection | `general/list` | Simple lists of items |
| Model | `general/model` | Typed structured data |
| Graph | `general/academic_graph` | Entity-relationship networks |
| Hypergraph | `general/hypergraph` | Many-to-many relationships |
| Temporal Graph | `finance/temporal_graph` | Time-series entity data |
| Spatial Graph | `geography/spatial_graph` | Location-aware entities |
| Spatio-Temporal Graph | `general/st_graph` | Combined space+time |
| Knowledge Graph | `general/knowledge_graph` | Rich semantic knowledge |

### Local Deployment (On-Premise)

```python
from hyperextract import create_client

# Use local vLLM + bge-m3 for fully offline extraction
llm, emb = create_client(
    llm="vllm:Qwen3.5-9B@http://localhost:8000/v1",
    embedder="vllm:bge-m3@http://localhost:8001/v1",
    api_key="dummy",
)
```

### Incremental Knowledge Evolution

```python
# Feed new documents to grow the same knowledge base
ka = Template.create("general/knowledge_graph")

# First pass
ka.parse(first_document)

# Second pass — knowledge base expands and evolves
ka.parse(additional_document)
```

## Common Pitfalls

- **API key configuration:** The CLI requires an LLM API key. If you get authentication errors, run `he config init` first.
- **Model compatibility:** Extraction quality depends on the LLM's structured output capability. Verified models: GPT-4o, Qwen-Plus, and local Qwen3.5-9B with vLLM.
- **Template selection:** Choose templates that match your document type. A financial document extracted with `finance/earnings_graph` yields better results than a generic template.
- **Local embedding models:** If using local vLLM, ensure both the LLM and embedding model endpoints are serving before running extraction.
- **Large documents:** For very large documents (>50 pages), split them into sections and parse incrementally. Use incremental evolution to merge results.

## Verification

```bash
# Verify installation
he --version

# Verify basic extraction works
he config init -k test_key
he parse examples/en/tesla.md -t general/biography_graph -o /tmp/test_kb -l en
he search /tmp/test_kb "What is Tesla known for?"
rm -rf /tmp/test_kb

# Verify Python API
python3 -c "
from hyperextract import Template
ka = Template.create('general/biography_graph')
print(f'Template loaded: {ka.name}')
print('Hyper-Extract working correctly')
"
```

## Integration with Agent Workflows

Hyper-Extract can power knowledge-base-driven agents:

```python
# Research agent workflow: extract knowledge from papers
def process_research_paper(pdf_path: str) -> dict:
    from hyperextract import Template
    ka = Template.create("general/academic_graph")
    with open(pdf_path) as f:
        result = ka.parse(f.read())
    return {
        "entities": result.entities,
        "relations": result.relations,
        "query": result.query
    }
```
