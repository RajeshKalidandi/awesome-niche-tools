name: pyrefly
description: "Fast type checker and language server for Python, written in Rust by Meta."
tags: [python, type-checking, lsp, dev-tools, rust, meta]
platforms: [linux]
related_skills: []
version: 1.0.0
author: Hermes Agent
license: MIT

# Pyrefly Skill

This skill provides automation for installing and configuring Pyrefly, the fast Python type checker and language server from Meta.

## Prerequisites

- Python 3.8+ installed
- pip package manager
- Optional: Rust toolchain for building from source
- Code editor with LSP support (VS Code, Neovim, etc.)

## Installation

Install via pip:

```bash
pip install pyrefly
```

Or install pre-built binaries (faster):

```bash
# Download latest release
curl -L https://github.com/facebook/pyrefly/releases/latest/download/pyrefly-x86_64-unknown-linux-gnu.tar.gz | tar xz
sudo mv pyrefly /usr/local/bin/

# Verify installation
pyrefly --version
```

Or build from source (requires Rust):

```bash
git clone https://github.com/facebook/pyrefly.git
cd pyrefly
cargo install --path .
```

## Configuration

Create a `pyrefly.toml` file in your project root:

```toml
[pyrefly]
# Enable incremental checking (recommended for large codebases)
incremental = true

# Strictness level: "off", "warn", "error" (default: "error")
strictness = "error"

# Files to exclude from checking
exclude = ["tests/", "build/", "dist/", "*.pyc"]

# Specific error codes to ignore
ignore = ["unused-import", "variable-not-used"]

# Enable experimental features
enable_experimental = false

[lsp]
# Enable language server
enabled = true

# Port for LSP TCP server (optional)
port = 0

# Trace logging for LSP (off, messages, verbose)
trace = "off"
```

## Usage

### Command-line type checking

```bash
# Check entire project
pyrefly check

# Check specific files
pyrefly check src/main.py src/utils.py

# Watch mode (re-check on file changes)
pyrefly watch

# Show help
pyrefly --help
```

### Language Server Protocol (LSP)

Pyrefly includes a language server for IDE integration:

**VS Code:**
1. Install the "Pyrefly" extension from the marketplace
2. Or manually configure: add to `.vscode/settings.json`:
   ```json
   {
     "python.analysis.typeCheckingMode": "off",
     "pyrefly.enabled": true
   }
   ```

**Neovim (with nvim-lspconfig):**
```lua
require'lspconfig'.pyrefly.setup{}
```

**Emacs (with lsp-mode):**
Pyrefly should be automatically detected if installed in PATH.

## Examples

### Basic type checking

```python
# pyrefly will catch this error
def add(x: int, y: int) -> int:
    return x + y

add("hello", "world")  # Error: Unsupported operand types for + (str, str)
```

### Complex type checking with generics

```python
from typing import List, Dict, Optional

def process_data(items: List[Dict[str, int]]) -> Optional[int]:
    total = 0
    for item in items:
        total += item.get("value", 0)
    return total if total > 0 else None

# pyrefly understands the flow and return type
result = process_data([{"value": 5}, {"value": 10}])  # Returns: int
```

### Configuration for large projects

```toml
[pyrefly]
incremental = true
strictness = "warn"
exclude = ["legacy/", "third_party/", "node_modules/"]

# Increase cache size for better performance
cache_size_mb = 512

# Use multiple threads for checking
threads = 4
```

## Environment Variables

- `PYREFLY_LOG_LEVEL`: Debug, Info, Warn, Error (default: Warn)
- `PYREFLY_CACHE_DIR`: Directory for incremental cache (default: `.pyrefly_cache`)
- `PYREFLY_MAX_THREADS`: Maximum threads for parallel checking
- `PYREFLY_DISABLE_INCREMENTAL`: Set to "1" to disable incremental checking

## Editor Integration Tips

### VS Code
- Disable Python's built-in type checker when using Pyrefly:
  ```json
  "python.analysis.typeCheckingMode": "off"
  ```
- Enable format on save with Pyrefly's formatting capabilities

### Neovim
- Use `vim.lsp.diagnostic.show_line_diagnostics` to show errors
- Configure virtual text for inline error messages

### Common Workflows
- Pre-commit hook: Add `pyrefly check` to your pre-commit configuration
- CI pipeline: Run `pyrefly check --strict` in your CI to enforce type safety
- Editor integration: Get real-time feedback as you type

## Common Pitfalls

- **Conflicting type checkers**: Disable other Python type checkers (mypy, pyright) when using Pyrefly
- **Incremental cache issues**: Delete `.pyrefly_cache` if you get strange errors after changing configuration
- **Performance**: For very large projects (>1M lines), increase cache size and thread count
- **False positives**: Use `# pyrefly: ignore=<error-code>` comments sparingly for known false positives
- **LSP initialization**: Ensure Pyrefly is in your shell PATH for editor integration to work

## Verification

Test that Pyrefly is working correctly:

1. Create a test file with intentional type errors:
   ```python
   def greet(name: str) -> str:
       return "Hello, " + name
   
   greet(123)  # Should error: Unsupported operand types for + (str, int)
   ```
2. Run `pyrefly check test.py` - should report exactly one error
3. Fix the error and run again - should report no errors
4. Test LSP integration by opening the file in your editor and seeing real-time diagnostics

## References

- GitHub Repository: https://github.com/facebook/pyrefly
- Documentation: https://pyrefly.org/
- Release Notes: https://github.com/facebook/pyrefly/releases
- Type Server Protocol (TSP): https://github.com/microsoft/pyright/blob/main/docs/type-server-protocol.md