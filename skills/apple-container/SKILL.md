---
name: apple-container
description: "Run Linux containers on Apple silicon Macs using Apple's native Swift-based container tool"
version: 1.0.0
author: Hermes Agent
license: Apache-2.0
platforms: [macos]
metadata:
  hermes:
    tags: [containers, docker, macos, apple-silicon, devops]
    related_skills: [vps-infra]
---

# Apple Container — Native Linux Containers on Mac

Apple's official tool for running Linux containers as lightweight virtual machines on Apple silicon Macs. OCI-compatible, Swift-native, optimized for Apple silicon.

## Prerequisites

- Mac with Apple silicon (M1/M2/M3/M4)
- macOS 26 or later
- Download from GitHub releases

## Usage

### Getting Started
```bash
# Start the system service
container system start

# Pull an image
container pull ubuntu:latest

# Run a container
container run ubuntu:latest /bin/bash

# List running containers
container ps
```

### Building Images
```bash
# Build from Dockerfile
container build -t myapp:latest .

# Tag for registry
container tag myapp:latest registry.example.com/myapp:latest

# Push to registry
container push registry.example.com/myapp:latest
```

### Management
```bash
# Stop a container
container stop <container_id>

# View logs
container logs <container_id>

# Execute command in running container
container exec <container_id> ls -la
```

## Common Pitfalls

- Requires macOS 26 — does not work on older versions.
- Apple silicon only — no Intel Mac support.
- OCI-compatible but not Docker CLI compatible — different command syntax.
- System service must be running before container operations.

## Verification

```bash
# Verify installation
container --version

# Test with a simple container
container run --rm alpine echo "Hello from Apple Container"
```
