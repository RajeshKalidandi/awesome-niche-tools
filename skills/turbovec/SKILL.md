---
name: turbovec
description: "High-performance vector index built on TurboQuant with Rust core and Python bindings"
version: 1.0.0
author: Hermes Agent
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [vector-database, similarity-search, ml, rust, python]
    related_skills: [llama-cpp, serving-llms-vllm]
---

# turbovec

A fast, lightweight vector index for similarity search, ideal for recommendation systems, semantic search, and RAG pipelines.

## Prerequisites

- Python 3.8+
- pip

## Installation

```bash
pip install turbovec
```

## Usage

### Basic Vector Operations

```python
import turbovec
import numpy as np

# Create an index with dimension 128
index = turbovec.Index(dim=128)

# Generate some random vectors
vectors = np.random.randn(1000, 128).astype(np.float32)
ids = list(range(1000))

# Add vectors to the index
index.add(vectors, ids)

# Search for similar vectors
query = np.random.randn(1, 128).astype(np.float32)
results = index.search(query, k=10)

print(f"Found {len(results[0])} similar vectors")
```

### Persistence

```python
# Save index to disk
index.save("my_index.tvec")

# Load index from disk
loaded_index = turbovec.Index.load("my_index.tvec")
```

### Integration with sentence-transformers

```python
from sentence_transformers import SentenceTransformer
import turbovec

# Encode sentences
model = SentenceTransformer('all-MiniLM-L6-v2')
sentences = ["This is a test", "Another sentence", "Third example"]
embeddings = model.encode(sentences)

# Create and populate index
index = turbovec.Index(dim=384)
index.add(embeddings, list(range(len(sentences))))

# Search
query_embedding = model.encode(["Find similar sentences"])
results = index.search(query_embedding, k=2)
```

## Common Pitfalls

1. **Memory usage**: Large indices require sufficient RAM. Consider indexing strategies.
2. **Dimension consistency**: All vectors must have the same dimension.
3. **Update limitations**: Turbovec is optimized for append-only workloads. Frequent updates may require rebuilding.
4. **Distance metrics**: Currently supports L2 distance. For cosine similarity, normalize vectors first.

## Verification

```bash
# Test installation
python -c "import turbovec; print('turbovec imported successfully')"

# Run a simple test
python -c "
import turbovec
import numpy as np

index = turbovec.Index(dim=64)
vectors = np.random.randn(100, 64).astype(np.float32)
index.add(vectors, list(range(100)))
query = np.random.randn(1, 64).astype(np.float32)
results = index.search(query, k=5)
print(f'Test passed: found {len(results[0])} results')
"
```
