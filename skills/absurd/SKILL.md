---
name: absurd
description: "Postgres-native durable workflow system — run workflows as SQL stored procedures, no extra infrastructure."
tags: [durable-execution, postgres, workflows, python, orchestration]
related_skills: [hermes-agent]
---

# Absurd — Postgres-Native Durable Workflows

Absurd runs durable workflows entirely within PostgreSQL using stored procedures. No Temporal, no Prefect, no Celery — just Postgres.

## Prerequisites

- Python 3.10+
- PostgreSQL 14+ (running and accessible)

## Installation

```bash
pip install absurd
```

## Quick Start

```bash
# Initialize in your Postgres database
absurd init --database postgresql://user:***@localhost:5432/myapp

# Define a workflow
absurd workflow create process_order << 'SQL'
INSERT INTO absurd.workflows (name, steps) VALUES
  ('process_order', ARRAY['validate', 'charge', 'ship']);
SQL

# Execute
absurd run process_order --input '{"order_id": 42}'

# Check status
absurd status <execution-id>
```

## Common Patterns

### Retry with backoff
```sql
-- Workflows automatically retry failed steps
-- Configure via workflow definition
absurd workflow update process_order --max-retries 3 --backoff exponential
```

### Monitoring
```bash
# List all running workflows
absurd list --status running

# View execution history
absurd history --workflow process_order --limit 10
```

## Pitfalls

- Requires `pg_cron` extension for scheduled workflows
- Stored procedures use `SECURITY DEFINER` — ensure Postgres user has appropriate permissions
- Long-running workflows may hold connections — configure connection pooling

## Verification

```bash
# Verify installation
absurd --version

# Verify database connection
absurd status --database postgresql://localhost/myapp
```
