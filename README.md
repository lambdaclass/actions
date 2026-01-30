# lambdaclass/actions

Reusable GitHub Actions workflows for the lambdaclass organization.

## AI Code Review Workflows

Automated PR code review using various AI providers. Each workflow posts review comments directly on pull requests.

### Available Workflows

| Workflow | Provider | Model |
|----------|----------|-------|
| `ai-review-kimi.yml` | [Moonshot AI](https://platform.moonshot.ai/) | kimi-k2-0711-preview |
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
  issue_comment:
    types: [created]

jobs:
  claude-review:
    uses: lambdaclass/actions/.github/workflows/ai-review-claude.yml@v1
    secrets:
      ANTHROPIC_API_KEY: ${{ secrets.ANTHROPIC_API_KEY }}
```

### On-Demand Reviews

Trigger reviews by commenting on a PR:
- `/kimi` - Trigger Kimi review
- `/codex` - Trigger Codex review
- `/claude` - Trigger Claude review

**Note:** Slash commands require write access to the repository.

### Custom Prompts

You can customize the review prompt in three ways (in order of priority):

1. **`prompt` input** - Pass a custom prompt directly in the workflow
2. **`.github/prompts/ai-review.md`** - Create this file in your repo with custom instructions
3. **Default prompt** - Generic security/bugs/performance review

When a custom prompt is used, the review footer will show "· custom prompt".

#### Example: Custom prompt file

Create `.github/prompts/ai-review.md` in your repository:

```markdown
You are a DevOps-focused code reviewer.

Review the pull request changes with special attention to:
1. **Infrastructure security** - AWS credentials, secrets exposure, IAM permissions
2. **CI/CD reliability** - Workflow syntax errors, missing error handling
3. **Terraform/IaC issues** - State management, resource naming, cost implications

Guidelines:
- Be concise and actionable
- Reference specific file names and line numbers
- Only flag real issues, not style preferences
- If no issues found, say "LGTM from DevOps perspective"
```

### Workflow Options

#### Kimi (`ai-review-kimi.yml`)

```yaml
jobs:
  kimi-review:
    uses: lambdaclass/actions/.github/workflows/ai-review-kimi.yml@v1
    secrets:
      KIMI_API_KEY: ${{ secrets.KIMI_API_KEY }}
    with:
      model: 'kimi-k2-0711-preview'   # Kimi model
      max_diff_lines: 10000            # Max lines of diff to review
      max_tokens: 4096                 # Max response tokens
      temperature: 0.3                 # AI temperature
      prompt: ''                       # Custom prompt (overrides prompt file)
```

#### Codex (`ai-review-codex.yml`)

```yaml
jobs:
  codex-review:
    uses: lambdaclass/actions/.github/workflows/ai-review-codex.yml@v1
    secrets:
      OPENAI_API_KEY: ${{ secrets.OPENAI_API_KEY }}
    with:
      safety_strategy: 'drop-sudo'    # Codex safety strategy
      prompt: ''                       # Custom prompt (overrides prompt file)
```

#### Claude (`ai-review-claude.yml`)

```yaml
jobs:
  claude-review:
    uses: lambdaclass/actions/.github/workflows/ai-review-claude.yml@v1
    secrets:
      ANTHROPIC_API_KEY: ${{ secrets.ANTHROPIC_API_KEY }}
    with:
      model: 'sonnet'                 # sonnet, opus, or haiku
      max_turns: 30                   # Max agentic turns
      allowed_tools: '...'            # Allowed Claude tools
      prompt: ''                       # Custom prompt (overrides prompt file)
```

### Default Review Focus

All workflows use a default prompt that focuses on:

1. **Security vulnerabilities** - Labeled by criticality (Critical/High/Medium/Low)
2. **Bugs** - Logic errors, edge cases, incorrect behavior
3. **Significant performance issues** - Only obvious problems like O(n²) loops

### Using Multiple Reviewers

You can run multiple AI reviewers in parallel:

```yaml
name: AI Code Review

on:
  pull_request:
    types: [opened, ready_for_review]
  issue_comment:
    types: [created]

jobs:
  kimi:
    uses: lambdaclass/actions/.github/workflows/ai-review-kimi.yml@v1
    secrets:
      KIMI_API_KEY: ${{ secrets.KIMI_API_KEY }}

  codex:
    uses: lambdaclass/actions/.github/workflows/ai-review-codex.yml@v1
    secrets:
      OPENAI_API_KEY: ${{ secrets.OPENAI_API_KEY }}

  claude:
    uses: lambdaclass/actions/.github/workflows/ai-review-claude.yml@v1
    secrets:
      ANTHROPIC_API_KEY: ${{ secrets.ANTHROPIC_API_KEY }}
```

### Security

- **Fork protection**: Reviews will not run on PRs from forks (to protect secrets)
- **Access control**: Slash commands only work for users with write access

### Versioning

Pin to a release tag (e.g., `@v1`) or a specific commit SHA:

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
