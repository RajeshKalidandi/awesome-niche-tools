---
name: goose
description: "Open-source extensible AI agent for coding tasks - install, execute, edit, and test with any LLM"
version: 1.0.0
author: Hermes Agent
license: Apache-2.0
platforms: [linux, macos]
metadata:
  hermes:
    tags: [ai-agent, coding, automation, llm, rust]
    related_skills: [claude-code, codex, opencode]
---

# goose

An extensible, open-source AI agent written in Rust that goes beyond code suggestions to perform actual development workflows.

## Prerequisites

- Rust toolchain (for building from source)
- Or pre-built binary from GitHub releases
- API key for preferred LLM provider

## Installation

```bash
# From source
git clone https://github.com/aaif-goose/goose.git
cd goose
cargo build --release

# Or download pre-built binary from GitHub releases
```

## Usage

### Basic Coding Task

```bash
# Configure with your preferred LLM
goose configure

# Run a coding task
goose run "refactor the authentication module to use JWT tokens"
```

### Interactive Mode

```bash
# Start interactive session
goose chat

# Ask questions about your codebase
> How does the authentication system work?
> Can you add unit tests for the user service?
```

### Batch Processing

```bash
# Process multiple tasks
goose batch tasks.txt
```

## Common Pitfalls

1. **LLM costs**: Complex tasks may consume significant tokens. Monitor usage.
2. **Code quality**: Always review generated code. AI can introduce subtle bugs.
3. **Security**: Be cautious with tasks that modify system files or install packages.
4. **Context limits**: Very large codebases may exceed LLM context windows.

## Verification

```bash
# Test installation
goose --version

# Run a simple test task
goose run "print the current working directory"
```
