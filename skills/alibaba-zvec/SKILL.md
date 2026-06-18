---
name: alibaba-zvec
description: "In-process vector database for AI applications — embed vector search, hybrid retrieval, and full-text search directly into your application without managing a separate server."
version: 1.0.0
author: Hermes Agent
license: Apache-2.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [vector-database, semantic-search, rag, hybrid-search, full-text-search, embeddings]
    related_skills: [lmcache, milvus]
---

# Alibaba Zvec — In-Process Vector Database

An open-source, in-process vector database from Alibaba Group that embeds directly into your application as a library. Supports dense vectors, sparse vectors, full-text search, and hybrid search in a single query with durable WAL-based persistence.

## Prerequisites

- Python 3.10–3.14 (for Python SDK)
- Node.js 18+ (for Node.js SDK)
- Or Go/Rust/Dart SDKs (see [GitHub](https://github.com/alibaba/zvec))
- No external databases or servers required

## Installation

### Python (Recommended for AI/ML workflows)

```bash
pip install zvec
```

### Node.js

```bash
npm install @zvec/zvec
```

## Basic Usage

### Python — Create Collection, Insert, and Query

```python
import zvec

# Create schema and collection
schema = zvec.CollectionSchema(
    name="my_docs",
    vectors=zvec.VectorSchema("embedding", zvec.DataType.VECTOR_FP32, 384),
)
collection = zvec.create_and_open(path="./zvec_data", schema=schema)

# Insert documents
collection.insert([
    zvec.Doc(
        id="doc_1",
        vectors={"embedding": [0.1, 0.2, 0.3, 0.4]},
        fields={"title": "First Document", "content": "This is the first document."}
    ),
    zvec.Doc(
        id="doc_2",
        vectors={"embedding": [0.2, 0.3, 0.4, 0.1]},
        fields={"title": "Second Document", "content": "This is the second document."}
    ),
])

# Vector similarity search
results = collection.query(
    zvec.VectorQuery("embedding", vector=[0.4, 0.3, 0.3, 0.1]),
    topk=10
)

# Print results
for r in results:
    print(f"{r['id']}: score={r['score']}")
```

### Hybrid Search (Vector + Full-Text + Filters)

```python
# Combine vector search with full-text and scalar filters
results = collection.query(
    zvec.MultiQuery([
        zvec.VectorQuery("embedding", vector=[0.3, 0.1, 0.2, 0.4], weight=0.7),
        zvec.FtsQuery("content", query="document", weight=0.3),
    ]),
    filter={"title": {"$ne": "First Document"}},
    topk=5,
)
```

## Advanced Usage

### Sparse Vectors for Keyword Matching

```python
# Collections can have both dense and sparse vector fields
sparse_schema = zvec.CollectionSchema(
    name="hybrid_docs",
    vectors=[
        zvec.VectorSchema("dense_emb", zvec.DataType.VECTOR_FP32, 768),
        zvec.VectorSchema("sparse_emb", zvec.DataType.VECTOR_SPARSE_FP32, 0),
    ],
)
```

### Full-Text Search (FTS)

```python
# Attach an FTS index to a string field
fts_schema = zvec.CollectionSchema(
    name="text_docs",
    vectors=zvec.VectorSchema("embedding", zvec.DataType.VECTOR_FP32, 384),
    full_text_fields=["title", "content"],
)
```

### Durable Storage with WAL

```python
# WAL is enabled by default — data survives crashes
# Collections are flushed to disk on every write
collection.flush()  # Explicit flush
```

## Common Pitfalls

- **Dimension mismatch:** The vector dimension in queries must match the dimension specified in the schema. Zvec validates this and raises `ValidationError` on mismatch.
- **Path conflicts:** Two collections cannot share the same path. Use unique paths or delete an existing collection before recreating it.
- **Concurrent writes:** Writes are single-process exclusive. Multiple processes can read the same collection simultaneously, but only one process can write.
- **Memory usage:** In-memory indexes (HNSW, IVF) consume RAM proportional to dataset size. For large-scale datasets (>1B vectors), use DiskANN index which keeps the bulk of the index on disk.
- **Missing index:** Queries against unindexed vectors fall back to brute-force search, which is slow for large collections. Always build an index after inserting data.

## Verification

```python
# Verify installation
python3 -c "import zvec; print(zvec.__version__)"

# Verify collection creation
python3 -c "
import zvec
schema = zvec.CollectionSchema(
    name='test',
    vectors=zvec.VectorSchema('emb', zvec.DataType.VECTOR_FP32, 4)
)
c = zvec.create_and_open(path='/tmp/zvec_test', schema=schema)
c.insert([zvec.Doc(id='1', vectors={'emb': [0.1]*4})])
r = c.query(zvec.VectorQuery('emb', vector=[0.1]*4), topk=1)
assert len(r) == 1
print('Zvec working:', r[0]['id'])
import shutil
shutil.rmtree('/tmp/zvec_test')
"
```

## Integration with Agent Memory

Zvec can serve as a persistent, local vector store for agent memory systems:

```python
from hermes_tools import terminal

# Use zvec as an agent memory backend
memory_db = "./agent_memory"
schema = zvec.CollectionSchema(
    name="memory",
    vectors=zvec.VectorSchema("embedding", zvec.DataType.VECTOR_FP32, 1536),
)
collection = zvec.create_and_open(path=memory_db, schema=schema)
```
