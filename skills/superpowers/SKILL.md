---
name: superpowers
description: "AI-2-AI translation for multi-agent communication. Converts between different agent architectures and communication protocols."
tags: [typescript, multi-agent, protocol-translation, agent-framework, communication]
related_skills: [agent-browser, oh-my-pi, open-code-review]
version: 1.0.0
author: "Vibe Coder"
license: MIT
platforms: [linux]

## Prerequisites

- Node.js 16+
- TypeScript 4+
- Agent frameworks (Claude Code, OpenCode, pi-mono, etc.)
- Docker (optional, for containerized protocol translation)

## Usage

### Basic Protocol Translation
```typescript
import { ProtocolTranslator } from 'superpowers';

// Initialize translator
translator = new ProtocolTranslator({
    sourceFramework: 'claude-code',
    targetFramework: 'opencode'
});

// Translate messages
sourceMessage = { type: 'function_call', content: 'analyze code' };
targetMessage = translator.translate(sourceMessage);
```

### Command Line Interface
```bash
# Install superpowers
npm install -g superpowers

# Initialize a translation project
superpowers init

# Add agent sources
superpowers add source1 --framework claude-code
superpowers add source2 --framework opencode
superpowers add source3 --framework pi-mono

# Generate protocol translation
superpowers translate --output ./translated-protocol

# Test translation
superpowers test --source claude-code --target pi-mono

# Export translation for production
superpowers export --format json --output ./protocol-config.json
```

### Integration with Hermes Agent
```typescript
import { SuperpowersTranslator } from 'superpowers';
import { HermesAgent } from '@hermes/agent';

// Create protocol translator for Hermes integration
translator = new SuperpowersTranslator({
    sourceFramework: 'claude-code',
    targetFramework: 'hermes-agent'
});

// Initialize Hermes agent with protocol support
hermesAgent = new HermesAgent({
    protocolTranslator: translator,
    mcpEnabled: true
});

// Translate incoming messages from other agents
hermesAgent.on('message', (source, message) => {
    translated = translator.translate(source, message);
    hermesAgent.processMessage(translated);
});
```

## Common Pitfalls

### 1. Framework Version Mismatch
```bash
# Problem: Different frameworks use different protocol versions
# Solution: Specify exact framework versions
superpowers add source --framework claude-code --version 3.5.2
superpowers add target --framework opencode --version 2.1.0
```

### 2. Protocol Feature Gaps
```typescript
// Problem: Source framework has features target doesn't support
// Solution: Map or transform features
const advancedFeatures = ['streaming', 'function_calling', 'context_window'];
const mappedFeatures = translator.mapFeatures(advancedFeatures, 'target-framework');
```

### 3. Message Size Limits
```typescript
// Problem: Large messages exceed protocol limits
// Solution: Chunk large messages or compress them
const chunkedMessage = translator.chunkMessage(largeMessage, maxSize: 1024);
translator.translate(chunkedMessage);
```

### 4. Error Handling
```typescript
// Problem: Protocol errors can break agent communication
// Solution: Implement robust error handling and fallbacks
translator.on('error', (error) => {
    console.error('Protocol translation error:', error);
    translator.retryTranslation(error.message);
});
```

## Verification Steps

### 1. Basic Test
```bash
# Test installation and basic functionality
superpowers --help
superpowers version

# Test protocol translation
superpowers translate --source claude-code --target opencode --test
```

### 2. Framework Connection Test
```typescript
// Test connection to different frameworks
import { SuperpowersTranslator } from 'superpowers';

async function testFrameworkConnections() {
    const frameworks = ['claude-code', 'opencode', 'pi-mono', 'gemini-cli'];
    const translator = new SuperpowersTranslator();
    
    for (const framework of frameworks) {
        const connected = await translator.testConnection(framework);
        console.log(`${framework}: ${connected ? 'Connected' : 'Failed'}`);
    }
}

testFrameworkConnections();
```

### 3. Protocol Translation Test
```typescript
// Test actual protocol translation
import { SuperpowersTranslator } from 'superpowers';

const translator = new SuperpowersTranslator({
    sourceFramework: 'claude-code',
    targetFramework: 'pi-mono'
});

// Test various message types
testMessages = [
    { type: 'function_call', content: 'analyze code' },
    { type: 'context_update', content: { files: ['code.py'] } },
    { type: 'system_prompt', content: 'You are a coding assistant' }
];

for (const message of testMessages) {
    const translated = translator.translate(message);
    console.log(`Original: ${message.type} -> Translated: ${translated.type}`);
}
```

### 4. Hermes Integration Test
```typescript
// Test integration with Hermes Agent
import { SuperpowersTranslator } from 'superpowers';
import { HermesAgent } from '@hermes/agent';

async function testHermesIntegration() {
    const translator = new SuperpowersTranslator({
        sourceFramework: 'claude-code',
        targetFramework: 'hermes-agent'
    });
    
    const hermesAgent = new HermesAgent({
        protocolTranslator: translator,
        mcpEnabled: true
    });
    
    // Test message translation
    const testMessage = { type: 'function_call', content: 'hello world' };
    const result = await hermesAgent.processMessage(testMessage);
    
    console.log('Hermes integration test:', result.success ? 'PASSED' : 'FAILED');
}

testHermesIntegration();
```

## Advanced Features

### 1. Custom Protocol Mappings
```typescript
import { ProtocolMapping } from 'superpowers';

// Define custom mappings for specific frameworks
const customMapping: ProtocolMapping = {
    sourceFramework: 'claude-code',
    targetFramework: 'custom-framework',
    mappings: {
        'function_call': 'execute_function',
        'context_update': 'update_context',
        'system_prompt': 'set_personality'
    }
};

const translator = new SuperpowersTranslator(customMapping);
```

### 2. Batch Translation
```typescript
// Translate multiple messages in batch
import { SuperpowersTranslator } from 'superpowers';

async function batchTranslate(messages, source, target) {
    const translator = new SuperpowersTranslator({ sourceFramework: source, targetFramework: target });
    
    const results = await Promise.all(
        messages.map(async (message) => {
            return await translator.translate(message);
        })
    );
    
    return results;
}

// Example usage
const translatedMessages = await batchTranslate(
    testMessages,
    'claude-code',
    'pi-mono'
);
```

### 3. Protocol Validation
```typescript
import { ProtocolValidator } from 'superpowers';

// Validate protocol compliance
const validator = new ProtocolValidator({
    schema: 'http://example.com/protocols/v1.json',
    strict: true
});

// Validate a message
const isValid = validator.validate(message);
console.log(`Message valid: ${isValid}`);
```

### 4. Protocol Evolution Support
```typescript
import { ProtocolEvolution } from 'superpowers';

// Handle protocol version evolution
const evolution = new ProtocolEvolution({
    sourceVersion: 'v1.0',
    targetVersion: 'v1.1',
    migrationRules: {
        'v1.0_to_v1.1': {
            additions: ['new_field', 'enhanced_features'],
            deprecations: ['old_field'],
            transformations: ['transform_old_to_new']
        }
    }
});

const evolvedMessage = evolution.evolve(oldMessage);
```

## Limitations

### 1. Protocol Complexity
- Complex protocol differences may require custom mappings
- Some frameworks have proprietary extensions
- Limited support for real-time protocol evolution

### 2. Performance
- Protocol translation adds overhead
- Large message batches may require optimization
- Connection establishment has latency

### 3. Compatibility
- Limited support for obscure agent frameworks
- May require manual configuration for edge cases
- Version mismatches can cause issues

### 4. Testing
- Comprehensive protocol testing requires extensive setup
- May need custom test cases for specific frameworks
- Integration testing with Hermes can be complex

## Troubleshooting

### Protocol Connection Issues
```bash
# If connection to framework fails
superpowers test --framework claude-code --verbose

# Check framework availability
superpowers list frameworks

# Verify framework configuration
superpowers config --framework claude-code --check
```

### Translation Issues
```typescript
// If translation fails
import { ProtocolTranslator } from 'superpowers';

const translator = new ProtocolTranslator({
    sourceFramework: 'claude-code',
    targetFramework: 'pi-mono',
    debugMode: true  // Enable debug logging
});

// Translate with detailed logging
translator.translate(message)
    .then(result => console.log('Success:', result))
    .catch(error => {
        console.error('Translation error:', error);
        translator.showHelp();
    });
```

### Performance Issues
```typescript
// If protocol translation is slow
import { ProtocolTranslator } from 'superpowers';

// Enable optimization
const translator = new ProtocolTranslator({
    optimization: 'batch',
    cacheEnabled: true,
    parallelProcessing: true
});

// Use caching for repeated translations
const translated = await translator.translateWithCache(message);
```

### Hermes Integration Issues
```typescript
// If Hermes integration fails
import { SuperpowersTranslator } from 'superpowers';
import { HermesAgent } from '@hermes/agent';

// Verify Hermes agent is properly configured
const hermesAgent = new HermesAgent({
    protocolTranslator: new SuperpowersTranslator({
        sourceFramework: 'claude-code',
        targetFramework: 'hermes-agent'
    }),
    mcpEnabled: true,
    debugMode: true  // Enable debug logging for integration
});
```

## Known Issues

### 1. Framework Support
- Limited support for emerging agent frameworks
- May need updates for new protocol versions
- Custom protocol implementations require manual work

### 2. Complex Protocols
- Multi-stage protocols may need custom logic
- Event-driven protocols may have edge cases
- Authentication/authorization in protocols can be complex

### 3. Performance
- High-volume translation scenarios may need tuning
- Memory usage can be high for complex translations
- CPU usage may be significant for large protocol sets

## Community Contributions

### 1. Framework Support
- Add support for new agent frameworks
- Contribute protocol mappings for specific frameworks
- Add translation rules for edge cases

### 2. Protocol Standards
- Propose new protocol standards
- Document existing protocol variations
- Create compatibility matrices

### 3. Tools and Utilities
- Build protocol validation tools
- Create protocol evolution helpers
- Develop protocol testing frameworks

## Support

### 1. Documentation
- Check the official documentation
- Review examples and tutorials
- Join the community forums

### 2. Issues
- Report bugs with detailed reproduction steps
- Include environment information
- Provide sample messages that fail

### 3. Community
- Join the Discord server
- Participate in discussions
- Contribute to documentation

## Future Enhancements

### 1. Protocol Standardization
- Contribute to protocol standardization efforts
- Create comprehensive protocol documentation
- Develop protocol compliance tools

### 2. Advanced Features
- Real-time protocol translation
- AI-powered protocol evolution
- Multi-agent protocol orchestration

### 3. Integration
- Native integration with more agent frameworks
- Enhanced support for cloud-based agents
- Improved containerization support

## Changelog

### Version 1.0.0 (2026-06-17)
- Initial release
- Basic protocol translation
- Framework connector support
- Hermes Agent integration

### Version 0.9.0 (2026-06-15)
- Alpha testing
- Core protocol translation
- Limited framework support

## Contributing

1. Fork the repository
2. Create a feature branch
3. Implement your changes
4. Add tests
5. Submit a pull request

## License

MIT