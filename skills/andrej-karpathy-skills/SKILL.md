---
name: andrej-karpathy-skills
description: "Skills automation platform for Andrej Karpathy's code. Automatically parses code and breaks it into reusable agent skills."
tags: [python, skills, automation, agent-framework, karpathy]
related_skills: [openhands, cline, coda]
version: 1.0.0
author: "Vibe Coder"
license: MIT
platforms: [linux]

## Prerequisites

- Python 3.8+
- Git (for repository integration)
- Agent environment (OpenCode, Claude Code, pi-mono, etc.)

## Usage

### Basic Skill Generation
```python
from andrej_karpathy_skills import skill_generator

# Parse a code repository
repo_path = "/path/to/repo"
skills = skill_generator.parse_repository(repo_path)

# Use skills in your agent
agent = YourAgent()
for skill in skills:
    agent.add_skill(skill)
```

### Command Line Interface
```bash
# Install the skills platform
pip install andrej-karpathy-skills

# Parse a code repository into skills
karpathy-skills parse --repo /path/to/repo

# View generated skills
karpathy-skills list --repo /path/to/repo

# Export skills for a specific agent framework
karpathy-skills export --framework opencode --output ./skills.json
```

### Integration with Hermes Agent
```python
from andrej_karpathy_skills import HermesSkillAdapter

# Create skill adapter for Hermes
hermesh_adapter = HermesSkillAdapter()

# Load and integrate skills into Hermes
hermesh = HermesAgent()
karpathy_skills = andrej_karpathy_skills.parse("github.com/user/repo")
for skill in karpathy_skills:
    hermesh.add_skill(skill, adapter=hermesh_adapter)
```

## Common Pitfalls

### 1. Complex Code Structures
```python
# Problem: Nested functions and closures confuse the parser
# Solution: Simplify your code before skill generation
# or use --max-complexity flag
karpathy-skills parse --repo /path/to/repo --max-complexity 10
```

### 2. Non-Python Code
```python
# Problem: Skills generator optimized for Python
# Solution: Convert to Python first, or use --language python flag
karpathy-skills parse --repo /path/to/repo --language python
```

### 3. Large Codebases
```python
# Problem: Memory issues with huge repositories
# Solution: Parse in chunks or use --chunk-size option
karpathy-skills parse --repo /path/to/repo --chunk-size 1000
```

### 4. Agent Skill Loading
```python
# Problem: Hermes agent skill loading order matters
# Solution: Load core skills first, then application-specific skills
agent.add_core_skills(core_skill_list)
agent.add_application_skills(app_skill_list)
```

## Verification Steps

### 1. Basic Test
```bash
# Test installation and basic functionality
karpathy-skills --help
karpathy-skills version
```

### 2. Code Parsing Test
```bash
# Test parsing on a sample repository
cd /tmp
curl -L https://github.com/andrej-karpathy/teaching-materials/archive/refs/heads/main.tar.gz | tar -xz
cd teaching-materials-main
karpathy-skills parse .
```

### 3. Skill Generation Test
```python
# Test skill generation programmatically
from andrej_karpathy_skills import skill_generator

skills = skill_generator.parse_repository(".")
assert len(skills) > 0
assert all(skill.name for skill in skills)
assert all(skill.description for skill in skills)
print(f"Generated {len(skills)} skills successfully")
```

### 4. Integration Test
```python
# Test integration with Hermes
from andrej_karpathy_skills import HermesSkillAdapter

hermesh_adapter = HermesSkillAdapter()
karpathy_skills = andrej_karpathy_skills.parse("/path/to/repo")

for skill in karpathy_skills:
    hermesh_skill = hermesh_adapter.convert(skill)
    assert hermesh_skill.name == skill.name
    assert hermesh_skill.description == skill.description

print("Hermes integration test passed")
```

## Advanced Features

### 1. Custom Skill Templates
```python
from andrej_karpathy_skills import SkillTemplate

# Define custom skill templates for your project
template = SkillTemplate(
    name="data_processing",
    pattern=r"def process_data\(\)",
    skill_type="data",
    dependencies=["pandas", "numpy"]
)

# Apply template to matching functions
karpathy_skills.apply_template(template)
```

### 2. Batch Processing
```python
# Process multiple repositories in batch
repos = ["/path/to/repo1", "/path/to/repo2", "/path/to/repo3"]
for repo in repos:
    skills = skill_generator.parse_repository(repo)
    skill_generator.save_skills(skills, f"output/{repo.split('/')[-1]}.json")
```

### 3. CI/CD Integration
```yaml
# GitHub Actions workflow example
def parse_and_optimize():
    karpathy-skills parse --repo .
    karpathy-skills optimize --output optimized/
    karpathy-skills test --suite unit

name: Skills Automation
on: [push, pull_request]
jobs:
  generate-skills:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v2
    - name: Install dependencies
      run: pip install andrej-karpathy-skills
    - name: Generate skills
      run: parse_and_optimize()
    - name: Commit generated skills
      run: |
        git config --local user.email "action@github.com"
        git config --local user.name "GitHub Action"
        git add skills/
        git commit -m "Auto-generated skills" || exit 0
        git push
```

## Limitations

### 1. Language Support
- Primary focus on Python
- Limited support for JavaScript, TypeScript, Go
- Ongoing expansion of language support

### 2. Code Complexity
- Deep control flow analysis may miss some edge cases
- Limited support for metaprogramming
- Template matching may need refinement for complex patterns

### 3. Skill Granularity
- May generate too many fine-grained skills
- Some skills may have overlapping responsibilities
- Manual skill consolidation may be needed

### 4. Integration
- Hermes Agent integration requires specific skill formats
- May need custom adapters for other agent frameworks
- Skill compatibility testing may be required

## Troubleshooting

### Skill Generation Issues
```bash
# If skills generation fails
karpathy-skills parse --repo . --debug

# Check for syntax errors in your code
python -m py_compile your_script.py

# Verify repository structure
ls -la /path/to/repo
```

### Hermes Integration Issues
```python
# If Hermes doesn't load skills
from andrej_karpathy_skills import HermesSkillAdapter

adapter = HermesSkillAdapter()
skill = adapter.convert(your_skill)
print(f"Skill format: {skill.__dict__}")

# Check for missing fields
required_fields = ["name", "description", "parameters", "examples"]
for field in required_fields:
    if not hasattr(skill, field):
        print(f"Warning: Missing field: {field}")
```

### Performance Issues
```python
# If skill generation is slow
import time
start_time = time.time()

skills = skill_generator.parse_repository("/path/to/large/repo")
print(f"Generated {len(skills)} skills in {time.time() - start_time:.2f} seconds")

# For large repositories, use chunking
skill_generator.parse_repository("/path/to/large/repo", chunk_size=1000)
```

## Known Issues

### 1. Bug Reports
- Issues with parsing complex Python syntax
- Limited support for async functions
- Memory issues with large repositories

### 2. Feature Requests
- Better support for JavaScript/TypeScript
- Improved skill deduplication
- Advanced pattern matching

### 3. Community Contributions
- Fork the repository and submit pull requests
- Report bugs with detailed reproduction steps
- Contribute new language parsers

## Support

For support, please:
1. Check the documentation in the repository
2. Create an issue with detailed reproduction steps
3. Provide code samples that demonstrate the issue
4. Include your environment information (OS, Python version, etc.)

## Future Enhancements

### 1. Multi-Language Support
- Expand support for JavaScript, TypeScript, Go
- Add pattern-based language detection
- Improve code parsing for different syntaxes

### 2. Advanced Features
- Automated skill optimization
- Skill conflict resolution
- Multi-repository skill merging

### 3. Integration
- Native integration with more agent frameworks
- Enhanced Hermes Agent capabilities
- Improved skill validation and testing

## Changelog

### Version 1.0.0 (2026-06-17)
- Initial release
- Basic skill parsing and generation
- Hermes Agent integration
- Command line interface

### Version 0.9.0 (2026-06-15)
- Alpha testing
- Core functionality
- Limited language support

## Contributing

1. Fork the repository
2. Create a feature branch
3. Implement your changes
4. Add tests
5. Submit a pull request

## License

MIT