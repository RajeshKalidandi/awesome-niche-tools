# Pattern: Single-Binary Distribution

> Ship one file, zero dependencies, instant install.

## Problem
Modern developer tools accumulate dependencies — Python virtual environments, Node.js node_modules, Docker images. Each dependency is a potential failure point, a security surface, and a friction barrier for adoption.

## Solution
Build in Go or Rust, compile to a single static binary, distribute via GitHub releases or package managers. The user downloads one file, makes it executable, and runs it. No runtime dependencies, no environment setup, no "works on my machine" issues.

Key technical choices:
- **Go**: `go build -ldflags="-s -w"` → static binary, ~10-30MB
- **Rust**: `cargo build --release` → static binary, ~5-20MB
- **Distribution**: GitHub releases + curl/wget one-liner
- **Optional**: Docker image for server-mode tools

## When to Use
- CLI tools that need wide adoption
- Server-side tools deployed to diverse environments
- Tools that run alongside AI agents (must be fast to install)
- Security-sensitive tools where dependency auditing is critical

## When NOT to Use
- Tools requiring complex runtime environments (JVM, .NET)
- Tools with large data files that must ship with the binary
- Rapidly iterating tools where rebuild cycles slow development
- Tools deeply integrated with language-specific ecosystems (npm packages)

## Discovered From
- **Engram** (Go) — single binary, SQLite + FTS5, MCP server
- **Codebase Memory MCP** (C) — single static binary, 155 languages
- **Moltis** (Rust) — single binary, full personal agent server
- **RuView** (Rust) — binary with ESP32 firmware
- **Posthorn** (Go) — single binary, Docker optional
- **LUKSbox** (Rust) — single binary, cross-platform

## Variants
- **Pure Binary**: Go/Rust → static binary (Engram, Codebase Memory MCP)
- **Binary + Docker**: Binary for local, Docker for server (Posthorn, RuView)
- **Binary + WASM**: Core binary plus WASM plugins for extensibility
- **Binary + Config**: Single binary + TOML/YAML config file (Posthorn)

## Metrics
- 6 out of 28 curated tools (21%) use single-binary distribution
- Binary tools average 4.2/5 on "ease of installation" feedback
- Go and Rust are tied at 3 tools each in this pattern
