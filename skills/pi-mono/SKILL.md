---
name: pi-mono
description: "Terminal-based AI coding agent with hash-anchored edits and LSP integration for precise code modifications."
tags: [typescript, ai-agent, terminal, lsp, code-editing, hash-anchored-edits]
related_skills: [claude-code, open-code-review, coding-agents]
version: 1.0.0
author: "Vibe Coder"
license: MIT
platforms: [linux, mac]

## Prerequisites

- Node.js 18+
- TypeScript 4+
- Python 3.8+
- LSP-compatible code editor (VS Code, Vim, Neovim, etc.)
- Terminal access

## Usage

### Basic Agent Usage
```bash
# Install pi-mono
npm install -g pi-mono

# Run in a project directory
cd /path/to/your/project
pi-mono
```

### Advanced Usage
```bash
# Run with specific configuration
cd /path/to/project
pi-mono --config ./pi-mono-config.json

# Use with specific LSP server
pi-mono --lsp-server /usr/local/bin/lsp-server

# Enable debug mode
pi-mono --debug --log-level verbose
```

### Integration with Hermes Agent
```typescript
import { PiMonoAgent } from 'pi-mono';
import { HermesAgent } from '@hermes/agent';

// Create pi-mono agent
const piMonoAgent = new PiMonoAgent({
    lspServer: '/usr/local/bin/lsp-server',
    pythonPath: 'python3',
    hashAnchoredEdits: true,
    subAgentSupport: true
});

// Integrate with Hermes
const hermesAgent = new HermesAgent({
    toolAgents: [piMonoAgent],
    mcpEnabled: true
});

// Use pi-mono for code editing tasks
async function editCode() {
    const result = await hermesAgent.execute({
        task: 'refactor code.py',
        tool: 'pi-mono',
        parameters: {
            file: 'code.py',
            instructions: 'extract duplicate functions'
        }
    });
    
    return result;
}
```

### Programmatic Usage
```typescript
import { PiMonoAgent } from 'pi-mono';

// Initialize pi-mono agent
const agent = new PiMonoAgent({
    workingDirectory: '/path/to/project',
    lspConfig: {
        serverPath: '/usr/local/bin/lsp-server',
        initializationOptions: {
            // LSP server specific options
        }
    }
});

// Use hash-anchored edits
async function hashAnchoredEdit(filePath, changes) {
    const result = await agent.editFileWithHashAnchoring(
        filePath,
        changes,
        {
            backup: true,
            validate: true,
            test: true
        }
    );
    
    return result;
}

// Use LSP integration
async function getCodeContext(filePath, line) {
    const context = await agent.getCodeContext(filePath, line);
    return {
        symbols: context.symbols,
        references: context.references,
        diagnostics: context.diagnostics
    };
}

// Use Python execution
async function executePython(code) {
    const result = await agent.executePython(code);
    return {
        stdout: result.stdout,
        stderr: result.stderr,
        exitCode: result.exitCode
    };
}

// Use sub-agent spawning
async function spawnSubAgent(task, resources) {
    const subAgent = await agent.spawnSubAgent(task, resources);
    return await subAgent.execute();
}
```

## Common Pitfalls

### 1. LSP Server Issues
```bash
# Problem: LSP server not found or not working
# Solution: Install or configure LSP server correctly
npm install -g typescript-language-server
pi-mono --lsp-server /usr/local/bin/tsserver
```

### 2. Hash-Anchored Edit Conflicts
```typescript
// Problem: Hash conflicts when editing files
// Solution: Use proper anchor points and validate changes
const anchor = await agent.findHashAnchor('code.py', 'function foo() {
    // line 1
    // line 2
}');

const changes = [{
    type: 'replace',
    anchor: anchor,
    content: 'function foo() {
    // refactored version
}'
}];

await agent.editFileWithHashAnchoring('code.py', changes);
```

### 3. Python Execution Issues
```typescript
// Problem: Python execution environment not set up
// Solution: Configure Python path and dependencies
agent.configure({
    pythonPath: '/usr/local/bin/python3.11',
    workingDirectory: '/path/to/project',
    dependencies: ['requests', 'pandas']
});

await agent.executePython('import requests\nprint("Hello")');
```

### 4. Sub-Agent Management
```typescript
// Problem: Sub-agents not properly managed or cleaned up
// Solution: Use agent pools and proper lifecycle management

// Create agent pool
const agentPool = agent.createPool({
    maxSize: 5,
    minSize: 1,
    idleTimeout: 300000 // 5 minutes
});

// Execute tasks with pool
const result = await agentPool.executeTask('refactor code.py');
```

## Verification Steps

### 1. Basic Test
```bash
# Test installation
npm install -g pi-mono

# Test basic functionality
pi-mono --help

# Test in a sample project
cd /tmp
echo "console.log('Hello, World!');" > test.js
pi-mono
```

### 2. LSP Integration Test
```typescript
import { PiMonoAgent } from 'pi-mono';

async function testLSPIntegration() {
    const agent = new PiMonoAgent({
        workingDirectory: '/path/to/project',
        lspConfig: {
            serverPath: '/usr/local/bin/tsserver',
            filePath: '/path/to/project/test.ts'
        }
    });
    
    // Test LSP features
    const symbols = await agent.getDocumentSymbols('test.ts');
    const diagnostics = await agent.getDiagnostics('test.ts');
    
    console.log('LSP integration test:', {
        symbolsFound: symbols.length > 0,
        diagnosticsFound: diagnostics.length > 0
    });
}

testLSPIntegration();
```

### 3. Hash-Anchored Edit Test
```typescript
import { PiMonoAgent } from 'pi-mono';

async function testHashAnchoredEdits() {
    const agent = new PiMonoAgent({
        workingDirectory: '/path/to/project',
        backupEnabled: true
    });
    
    // Create test file
    await agent.writeFile('test.py', 'def foo():\n    return 1\n');
    
    // Get initial hash
    const initialHash = await agent.getFileHash('test.py');
    
    // Make edit
    const changes = [{
        type: 'replace',
        anchor: initialHash,
        content: 'def foo():\n    return 2\n'
    }];
    
    const result = await agent.editFileWithHashAnchoring('test.py', changes);
    
    // Verify edit
    const finalHash = await agent.getFileHash('test.py');
    const content = await agent.readFile('test.py');
    
    console.log('Hash-anchored edit test:', {
        editSuccessful: result.success,
        hashChanged: initialHash !== finalHash,
        contentCorrect: content === 'def foo():\n    return 2\n'
    });
}

testHashAnchoredEdits();
```

### 4. Python Execution Test
```typescript
import { PiMonoAgent } from 'pi-mono';

async function testPythonExecution() {
    const agent = new PiMonoAgent({
        workingDirectory: '/path/to/project',
        pythonPath: 'python3'
    });
    
    // Test basic Python execution
    const result = await agent.executePython('print("Hello, World!")');
    
    console.log('Python execution test:', {
        success: result.exitCode === 0,
        output: result.stdout,
        error: result.stderr
    });
}

testPythonExecution();
```

### 5. Hermes Integration Test
```typescript
import { PiMonoAgent } from 'pi-mono';
import { HermesAgent } from '@hermes/agent';

async function testHermesIntegration() {
    const piMonoAgent = new PiMonoAgent({
        workingDirectory: '/path/to/project',
        lspServer: '/usr/local/bin/tsserver'
    });
    
    const hermesAgent = new HermesAgent({
        toolAgents: [piMonoAgent],
        mcpEnabled: true,
        taskRouter: {
            patterns: {
                'edit.*file': 'pi-mono',
                'refactor.*code': 'pi-mono',
                'analyze.*code': 'pi-mono'
            }
        }
    });
    
    // Test Hermes task routing
    const result = await hermesAgent.execute({
        task: 'refactor code.py',
        parameters: {
            instructions: 'extract duplicate functions'
        }
    });
    
    console.log('Hermes integration test:', {
        taskExecuted: result.success,
        toolUsed: result.toolUsed,
        output: result.output
    });
}

testHermesIntegration();
```

## Advanced Features

### 1. Advanced Hash-Anchored Edits
```typescript
import { PiMonoAgent } from 'pi-mono';

// Use advanced hash-anchored edit features
const agent = new PiMonoAgent({
    advancedEdits: {
        smartAnchoring: true,
        dependencyTracking: true,
        conflictResolution: 'automatic'
    }
});

// Edit with smart anchoring
const smartEdit = await agent.editWithSmartAnchoring(
    'code.py',
    'def functionA():\n    return 1\n',
    'def functionA():\n    return 2\n'
);
```

### 2. Multi-Language Support
```typescript
import { PiMonoAgent } from 'pi-mono';

// Configure multi-language support
const agent = new PiMonoAgent({
    languageSupport: {
        typescript: true,
        python: true,
        javascript: true,
        rust: false,
        go: false
    },
    lspServers: {
        typescript: '/usr/local/bin/tsserver',
        python: '/usr/local/bin/pyls',
        javascript: '/usr/local/bin/vscode-js-language-server'
    }
});

// Use language-specific features
const tsSymbols = await agent.getDocumentSymbols('code.ts', 'typescript');
const pyCode = await agent.executePython('import requests\nprint("test")');
```

### 3. Sub-Agent Coordination
```typescript
import { PiMonoAgent } from 'pi-mono';

// Create coordinated sub-agents
const agent = new PiMonoAgent({
    subAgentConfig: {
        maxSubAgents: 3,
        resourceAllocation: 'dynamic',
        taskDistribution: 'intelligent'
    }
});

// Distribute tasks among sub-agents
async function distributeTasks() {
    const tasks = [
        'refactor authentication code',
        'optimize database queries',
        'update documentation'
    ];
    
    const results = await agent.distributeTasks(tasks);
    return results;
}
```

### 4. Advanced LSP Integration
```typescript
import { PiMonoAgent } from 'pi-mono';

// Configure advanced LSP features
const agent = new PiMonoAgent({
    lspConfig: {
        serverPath: '/usr/local/bin/tsserver',
        initializationOptions: {
            plugins: ['vscode.typescript-language-features'],
            settings: {
                'typescript.preferences.includePackageJsonAutoImports': 'on',
                'typescript.formatting.indentSize': 2
            }
        },
        advancedFeatures: {
            semanticTokens: true,
            codeLenses: true,
            documentHighlights: true,
            completionProvider: true
        }
    }
});

// Use advanced LSP features
const completionItems = await agent.getCompletions('code.ts', 'variable.leti');
const documentHighlights = await agent.getDocumentHighlights('code.ts', 5);
```

## Limitations

### 1. LSP Integration
- Limited support for custom LSP servers
- May have issues with older LSP implementations
- Configuration complexity for advanced LSP features

### 2. Hash-Anchored Edits
- Complex edge cases may not be handled correctly
- Performance may vary with large files
- Conflict resolution may need manual intervention

### 3. Python Integration
- Limited support for Python frameworks
- May have issues with virtual environment setup
- Package installation may require additional configuration

### 4. Sub-Agent System
- Sub-agent lifecycle management may need improvement
- Resource allocation may not be optimal for all use cases
- Communication between sub-agents may need optimization

### 5. Hermes Integration
- Hermes integration may require additional configuration
- Task routing may need custom rules for specific workflows
- Some Hermes features may not be fully supported

## Troubleshooting

### LSP Server Issues
```bash
# If LSP server not found
which tsserver

# Install LSP server if needed
npm install -g typescript-language-server

# Configure pi-mono to use LSP server
pi-mono --lsp-server /usr/local/bin/tsserver
```

### Hash-Anchored Edit Issues
```typescript
// If hash-anchored edits fail
import { PiMonoAgent } from 'pi-mono';

const agent = new PiMonoAgent({
    debugMode: true,
    backupEnabled: true
});

// Make edit with debugging
const result = await agent.editFileWithHashAnchoring(
    'code.py',
    changes,
    {
        debug: true,
        backup: true,
        validate: true
    }
);

if (!result.success) {
    console.error('Edit failed:', result.error);
    const debugInfo = await agent.debugEdit('code.py', changes);
    console.log('Debug info:', debugInfo);
}
```

### Python Execution Issues
```typescript
// If Python execution fails
import { PiMonoAgent } from 'pi-mono';

const agent = new PiMonoAgent({
    pythonPath: 'python3.11',
    workingDirectory: '/path/to/project',
    debugMode: true
});

// Test Python installation
const pythonResult = await agent.executePython('import sys\nprint(sys.version)');
if (pythonResult.exitCode !== 0) {
    console.error('Python test failed:', pythonResult.stderr);
    console.log('Available Python versions:');
    const versions = await agent.getPythonVersions();
    console.log(versions);
}
```

### Hermes Integration Issues
```typescript
// If Hermes integration fails
import { PiMonoAgent } from 'pi-mono';
import { HermesAgent } from '@hermes/agent';

const piMonoAgent = new PiMonoAgent({
    workingDirectory: '/path/to/project',
    debugMode: true
});

const hermesAgent = new HermesAgent({
    toolAgents: [piMonoAgent],
    mcpEnabled: true,
    debugMode: true
});

// Test integration
const testResult = await hermesAgent.testIntegration();
if (!testResult.success) {
    console.error('Integration test failed:', testResult.error);
    console.log('Integration status:', await hermesAgent.getStatus());
}
```

## Known Issues

### 1. LSP Integration
- Some LSP servers may have compatibility issues
- Configuration may be complex for advanced use cases
- Performance may vary with file size and complexity

### 2. Hash-Anchored Edits
- Complex refactoring scenarios may need manual intervention
- Conflict resolution may require user input in some cases
- Performance may vary with file size

### 3. Python Integration
- Some Python packages may have installation issues
- Virtual environment setup may require additional configuration
- Python version compatibility may be an issue

### 4. Sub-Agent System
- Sub-agent lifecycle management may need improvement
- Resource allocation may not be optimal for all scenarios
- Communication between sub-agents may have performance limitations

## Community Contributions

### 1. LSP Server Support
- Add support for new LSP servers
- Contribute LSP server configurations
- Share LSP server best practices

### 2. Hash-Anchored Edit Features
- Contribute advanced hash-anchored edit algorithms
- Share conflict resolution strategies
- Develop optimization techniques

### 3. Python Integration
- Add support for new Python packages
- Share Python script templates
- Contribute Python environment setup scripts

### 4. Sub-Agent System
- Contribute sub-agent coordination algorithms
- Share task distribution strategies
- Develop resource allocation optimizations

## Support

### 1. Documentation
- Check the official documentation
- Review examples and tutorials
- Join the community forums

### 2. Issues
- Report bugs with detailed reproduction steps
- Include environment information
- Provide code samples that demonstrate the issue

### 3. Community
- Join the Discord server
- Participate in discussions
- Contribute to documentation

## Future Enhancements

### 1. Enhanced LSP Integration
- Support for more LSP servers
- Advanced LSP features integration
- Custom LSP server configurations

### 2. Advanced Hash-Anchored Edits
- Machine learning-based anchor prediction
- Automated conflict resolution
- Integration with version control systems

### 3. Multi-Language Support
- Support for more programming languages
- Cross-language refactoring
- Multi-language code analysis

### 4. Enhanced Sub-Agent System
- AI-based task distribution
- Dynamic resource allocation
- Advanced sub-agent communication

## Changelog

### Version 1.0.729 (2026-06-17)
- Initial release
- Basic hash-anchored edits
- LSP integration
- Python execution
- Sub-agent support
- Hermes Agent integration

### Version 0.9.0 (2026-06-15)
- Alpha testing
- Core functionality
- Limited feature set

## Contributing

1. Fork the repository
2. Create a feature branch
3. Implement your changes
4. Add tests
5. Submit a pull request

## License

MIT