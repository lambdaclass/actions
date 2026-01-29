# lambdaclass/actions

Reusable GitHub Actions workflows for the lambdaclass organization.

## AI Code Review Workflows

Automated PR code review using various AI providers. Each workflow posts review comments directly on pull requests.

### Available Workflows

| Workflow | Provider | Model |
|----------|----------|-------|
| `ai-review-kimi.yml` | [Moonshot AI](https://platform.moonshot.ai/) | moonshot-v1-128k |
| `ai-review-codex.yml` | [OpenAI](https://platform.openai.com/) | Codex |
| `ai-review-claude.yml` | [Anthropic](https://console.anthropic.com/) | Claude Sonnet |

### Quick Start

1. **Add the required secret** to your repository (Settings > Secrets and variables > Actions):
   - `KIMI_API_KEY` for Kimi
   - `OPENAI_API_KEY` for Codex
   - `ANTHROPIC_API_KEY` for Claude

2. **Create a workflow file** in your repo at `.github/workflows/ai-review.yml`:

```yaml
name: AI Code Review

on:
  pull_request:
    types: [opened, ready_for_review]

jobs:
  claude-review:
    uses: lambdaclass/actions/.github/workflows/ai-review-claude.yml@main
    secrets:
      ANTHROPIC_API_KEY: ${{ secrets.ANTHROPIC_API_KEY }}
```

### Customization

All workflows accept optional inputs to customize behavior:

#### Kimi (`ai-review-kimi.yml`)

```yaml
jobs:
  kimi-review:
    uses: lambdaclass/actions/.github/workflows/ai-review-kimi.yml@main
    secrets:
      KIMI_API_KEY: ${{ secrets.KIMI_API_KEY }}
    with:
      model: 'moonshot-v1-128k'      # Kimi model
      max_diff_lines: 10000           # Max lines of diff to review
      max_tokens: 4096                # Max response tokens
      temperature: 0.3                # AI temperature
      prompt: |                       # Custom system prompt
        Your custom review instructions...
```

#### Codex (`ai-review-codex.yml`)

```yaml
jobs:
  codex-review:
    uses: lambdaclass/actions/.github/workflows/ai-review-codex.yml@main
    secrets:
      OPENAI_API_KEY: ${{ secrets.OPENAI_API_KEY }}
    with:
      safety_strategy: 'drop-sudo'    # Codex safety strategy
      prompt: |                       # Custom review prompt
        Your custom review instructions...
```

#### Claude (`ai-review-claude.yml`)

```yaml
jobs:
  claude-review:
    uses: lambdaclass/actions/.github/workflows/ai-review-claude.yml@main
    secrets:
      ANTHROPIC_API_KEY: ${{ secrets.ANTHROPIC_API_KEY }}
    with:
      model: 'sonnet'                 # sonnet, opus, or haiku
      max_turns: 30                   # Max agentic turns
      allowed_tools: '...'            # Allowed Claude tools
      prompt: |                       # Custom review prompt
        Your custom review instructions...
```

### Default Review Focus

All workflows use a default prompt that focuses on:

1. **Security vulnerabilities** - Labeled by criticality (Critical/High/Medium/Low)
   - Solidity: reentrancy, access control, integer issues
   - Rust: unsafe blocks, error handling, panics
   - Web/API: SQL injection, auth bypass, input validation, CORS/CSRF

2. **Potential bugs** - Logic errors, edge cases, race conditions

3. **Performance issues** - Only significant ones (O(n²) on unbounded input, N+1 queries)

4. **Simplicity** - Prefers simple, readable code over clever abstractions

### Using Multiple Reviewers

You can run multiple AI reviewers in parallel:

```yaml
name: AI Code Review

on:
  pull_request:
    types: [opened, ready_for_review]

jobs:
  kimi:
    uses: lambdaclass/actions/.github/workflows/ai-review-kimi.yml@main
    secrets:
      KIMI_API_KEY: ${{ secrets.KIMI_API_KEY }}

  claude:
    uses: lambdaclass/actions/.github/workflows/ai-review-claude.yml@main
    secrets:
      ANTHROPIC_API_KEY: ${{ secrets.ANTHROPIC_API_KEY }}
```

### Versioning

For production use, pin to a specific tag instead of `@main`:

```yaml
uses: lambdaclass/actions/.github/workflows/ai-review-claude.yml@v1
```

## Contributing

1. Create a branch
2. Make changes
3. Test in a real repo using `@your-branch`
4. Open a PR

## License

MIT
