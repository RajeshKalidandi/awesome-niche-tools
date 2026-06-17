---
name: deusdata-codebase-memory-mcp
version: 1.0.0
author: Vibe Coder Curator
license: MIT
tags: [mcp, code-intelligence, rust, automation, ai-agents]
related_skills: [mcp-servers, code-analysis, rust-programming]

## What It Does
DeusData/codebase-memory-mcp is a high-performance code intelligence MCP server that indexes codebases into a persistent knowledge graph. It provides semantic understanding of code structure and relationships across 158 languages with sub-ms query responses and 99% token reduction compared to traditional approaches.

## Why It Matters
This tool transforms how developers and AI agents interact with codebases:
- **For AI Agents**: Better tool usage and code understanding
- **For Development Teams**: Faster onboarding, better code reuse, more effective bug detection
- **For Code Analysis**: Semantic queries instead of string matching
- **For Documentation**: Automatic knowledge extraction from code

## Execution Pattern

### Basic Usage
```bash
# Connect to the MCP server
mcp-client connect --server deusdata-codebase-memory-mcp

# Index a repository
mcp-client analyze repository \
  --url https://github.com/user/repo \
  --branch main \
  --output-format json

# Query the knowledge graph
mcp-client query \
  --pattern "function calls" \
  --repository user/repo \
  --limit 10
```

### For AI Agent Integration
```json
{
  "mcpServers": {
    "deusdata-codebase-memory-mcp": {
      "command": "deusdata-mcp-server",
      "args": [
        "--host", "localhost",
        "--port", "3000"
      ]
    }
  }
}
```

## Prerequisites

### System Requirements
- **Operating System**: Linux/macOS (Rust development environment)
- **Architecture**: x86_64 or ARM64
- **Memory**: 4GB minimum (8GB+ recommended for large codebases)
- **Storage**: 1GB+ for indexed knowledge graph

### Dependencies
- Rust toolchain (stable channel)
- Docker (optional, for easy deployment)
- Network access to GitHub API or self-hosted Git servers

### Installation
```bash
# Clone the repository
cgit clone https://github.com/DeusData/codebase-memory-mcp.git
cd codebase-memory-mcp

# Build with cargo
cargo build --release

# For Docker users (recommended)
docker build -t deusdata-mcp .
docker run -p 3000:3000 deusdata-mcp
```

## Common Pitfalls

### Performance Issues
- **Problem**: Slow indexing for very large repositories
- **Solution**: Use incremental indexing and parallel processing
- **Tip**: Index repositories in stages, starting with core modules

### Memory Management
- **Problem**: High memory usage during indexing
- **Solution**: Configure memory limits and use efficient data structures
- **Tip**: Monitor memory usage and scale accordingly

### Authentication
- **Problem**: GitHub API rate limits
- **Solution**: Use personal access tokens and implement caching
- **Tip**: Cache repository metadata to reduce API calls

### Configuration
- **Problem**: Complex configuration for diverse codebase types
- **Solution**: Use configuration templates and defaults
- **Tip**: Start with default settings and customize as needed

## Verification Steps

### 1. Basic Connectivity Test
```bash
# Test MCP server connection
mcp-client health-check --server deusdata-codebase-memory-mcp

# Expected output: {"status": "healthy", "version": "1.0.0"}
```

### 2. Repository Indexing Test
```bash
# Index a test repository (small one for quick testing)
mcp-client analyze repository \
  --url https://github.com/torvalds/linux \
  --branch master \
  --depth 10  # Limit to 10 commits for testing

# Check indexing progress
mcp-client status --server deusdata-codebase-memory-mcp
```

### 3. Query Test
```bash
# Test basic query functionality
mcp-client query \
  --pattern "kernel" \
  --repository torvalds/linux \
  --format text

# Test advanced query
mcp-client query \
  --pattern "function.*driver" \
  --repository user/repo \
  --repository other/repo \
  --combine-results
```

### 4. Performance Test
```bash
# Measure query response time
mcp-client benchmark \
  --queries 10 \
  --repository large-repo \
  --output-format json

# Expected: Response times under 100ms for indexed repositories
```

## Advanced Usage

### Custom MCP Configurations
```bash
# Configure for specific use cases
cat > mcp-config.json << EOF
{
  "servers": {
    "deusdata-codebase-memory-mcp": {
      "command": "cargo run --release",
      "args": [
        "--host", "0.0.0.0",
        "--port", "3000",
        "--log-level", "info"
      ],
      "env": {
        "DEUSDATA_API_KEY": "${DEUSDATA_API_KEY}",
        "MAX_INDEXING_WORKERS": "4"
      }
    }
  }
}
EOF
```

### Integration with Other Tools
```json
{
  "mcpServers": {
    "deusdata-codebase-memory-mcp": {
      "command": "deusdata-mcp-server",
      "args": ["serve", "--port", "3000"],
      "env": {
        "INDEX_CACHE_DIR": "/tmp/deusdata-cache",
        "MAX_REPOSITORY_SIZE": "10GB"
      }
    }
  }
}
```

### Automated Indexing Script
```bash
#!/bin/bash
# Automated codebase indexing script

# Configuration
INDEX_DIR="~/.cache/deusdata-index"
LOG_FILE="$INDEX_DIR/index.log"
MAX_REPOS=10

# Create directories
mkdir -p "$INDEX_DIR"

# Log function
log() {
    echo "$(date '+%Y-%m-%d %H:%M:%S') - $1" >> "$LOG_FILE"
}

# Main indexing function
index_repository() {
    local repo_url=$1
    local branch=${2:-main}
    local output_dir="$INDEX_DIR/$(echo $repo_url | tr '/' '_' | sed 's://::-g')"
    
    log "Starting index for $repo_url (branch: $branch)"
    
    # Check if already indexed
    if [ -f "$output_dir/indexed.stamp" ]; then
        log "Repository $repo_url already indexed, skipping"
        return 0
    fi
    
    # Index the repository
    mcp-client analyze repository \
        --url "$repo_url" \
        --branch "$branch" \
        --output-dir "$output_dir" \
        --verbose >> "$LOG_FILE" 2>&1
    
    if [ $? -eq 0 ]; then
        touch "$output_dir/indexed.stamp"
        log "Successfully indexed $repo_url"
    else
        log "Failed to index $repo_url"
        return 1
    fi
}

# Main execution
log "Starting automated indexing process"

# Index popular repositories (example list)
popular_repos=(
    "https://github.com/torvalds/linux"
    "https://github.com/facebook/react"
    "https://github.com/microsoft/vscode"
    "https://github.com/nodejs/node"
)

for repo in ${popular_repos[@]}; do
    if [ ${#popular_repos[@]} -le $MAX_REPOS ]; then
        index_repository "$repo"
    fi
done

log "Automated indexing completed"
```

## Troubleshooting

### Common Issues and Solutions

#### Issue: MCP Server Won't Start
**Symptoms:** Connection refused, "server not found"
**Solution:**
1. Check if the server binary exists: `ls -la target/release/deusdata-mcp-server`
2. Verify dependencies: `cargo tree | grep "required-crate"`
3. Check port conflicts: `netstat -tlnp | grep :3000`

#### Issue: Slow Indexing
**Symptoms:** Takes more than 10 minutes for small repositories
**Solution:**
1. Increase indexing workers: `export MAX_INDEXING_WORKERS=8`
2. Use incremental indexing: `--incremental` flag
3. Optimize configuration: `export INDEX_BATCH_SIZE=100`

#### Issue: Query Results Incomplete
**Symptoms:** Missing functions, classes, or patterns
**Solution:**
1. Ensure repository is fully indexed: `--depth full`
2. Check query syntax: `"function.*name"` instead of just `"name"`
3. Verify language support: `--language rust cpp python`

#### Issue: Memory Exhaustion
**Symptoms:** "out of memory" errors
**Solution:**
1. Increase system memory
2. Configure memory limits: `--max-memory 4GB`
3. Use sparse indexing: `--sparse true`

### Debugging Commands
```bash
# Check server logs
journalctl -u deusdata-mcp -f

# Monitor system resources
htop
iostat 1

# Check MCP server status
mcp-client status

# Test individual components
mcp-client health-check --server deusdata-codebase-memory-mcp
```

## Verification Checklist

### Pre-deployment
- [ ] Rust toolchain installed and updated
- [ ] All dependencies resolved
- [ ] Build successful: `cargo build --release`
- [ ] Port 3000 available
- [ ] Environment variables configured

### Initial Testing
- [ ] Server starts successfully
- [ ] Health check passes
- [ ] Basic indexing works
- [ ] Simple queries return results
- [ ] Performance under load

### Production Readiness
- [ ] Monitoring and logging configured
- [ ] Error handling tested
- [ ] Backup and recovery procedures documented
- [ ] Security policies reviewed
- [ ] User documentation complete

## Next Steps

### For Developers
1. **Study the Rust implementation** to understand architecture
2. **Contribute** by adding support for new languages
3. **Write tests** for edge cases and performance
4. **Document** new features and configurations

### For Users
1. **Start small** with a single repository for testing
2. **Monitor** indexing progress and performance
3. **Customize** configuration for specific needs
4. **Integrate** with existing CI/CD pipelines

### For Researchers
1. **Analyze patterns** in indexed knowledge graphs
2. **Publish findings** on codebase analysis techniques
3. **Share configurations** for different repository types
4. **Develop benchmarks** for performance comparison

## Skills This Tool Helps You Master

- **Rust Development**: Build production-grade Rust applications
- **MCP Protocol**: Understand Model Context Protocol implementation
- **Code Analysis**: Develop semantic code understanding tools
- **Knowledge Graphs**: Work with graph databases and relationships
- **Performance Optimization**: Build high-performance systems
- **DevOps**: Containerize and deploy applications
- **API Design**: Design RESTful APIs for code intelligence

This tool provides a solid foundation for learning and building advanced code analysis and AI agent capabilities while maintaining high performance and scalability.