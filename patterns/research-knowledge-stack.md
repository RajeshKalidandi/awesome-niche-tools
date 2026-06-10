# Stack: Research-Powered Knowledge Management

## Components

- last30days-skill (https://github.com/mvanhorn/last30days-skill)
- turbovec (https://github.com/RyanCodrai/turbovec)
- tolaria (https://github.com/refactoringhq/tolaria)

## What it enables

A complete knowledge management system that can:
1. Automatically research topics across multiple platforms
2. Store and index research results as vector embeddings
3. Provide a visual interface for browsing and connecting knowledge

## Why it is composable

- last30days-skill outputs structured research with citations
- turbovec provides fast similarity search over embeddings
- tolaria offers a markdown-based visual interface
- All three support Python integration
- Data flows naturally: research -> vectorize -> browse

## Execution pattern

1. Research phase: Use last30days-skill to gather information on a topic
2. Vectorization: Convert research summaries to embeddings and store in turbovec
3. Browsing: Use tolaria to visually explore and connect research findings
4. Retrieval: Use turbovec to find related research when new queries come in

## Example workflow



## Use cases

- Academic research and literature review
- Competitive intelligence gathering
- Personal knowledge management
- Team knowledge bases that update automatically
