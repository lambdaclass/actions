# lambdaclass/actions

Reusable GitHub Actions workflows for the lambdaclass organization.

## AI Code Review Workflows

Automated PR code review using various AI providers. Each workflow posts review comments directly on pull requests.

### Available Workflows

| Workflow | Provider | Model |
|----------|----------|-------|
| `ai-review-claude.yml` | [Anthropic](https://console.anthropic.com/) | claude-opus-5-5 |
| `ai-review-kimi.yml` | [Moonshot AI](https://platform.kimi.ai/) | kimi-k3.1-pro |
| `ai-review-codex.yml` | [OpenAI](https://platform.openai.com/) | gpt-6.1-sol |
| `ai-review-deepseek.yml` | [DeepSeek](https://platform.deepseek.com/) | deepseek-v4-pro |
| `ai-review-gemini.yml` | [Google](https://aistudio.google.com/apikey) | gemini-4-argon |
| `ai-review-grok.yml` | [xAI](https://console.x.ai/) | grok-4.7 |

### Quick Start

1. **Add the required secret** to your repository (Settings > Secrets and variables > Actions):
   - `KIMI_API_KEY` for Kimi
   - `OPENAI_API_KEY` for Codex
   - `DEEPSEEK_API_KEY` for DeepSeek
   - `XAI_API_KEY` for Grok
   - `GEMINI_API_KEY` for Gemini
   - `ANTHROPIC_API_KEY` for Claude

2. **Create a workflow file** in your repo at `.github/workflows/ai-review.yml`:

```yaml
name: AI Code Review

on:
  pull_request:
    types: [opened, ready_for_review]
  issue_comment:
    types: [created]

permissions:
  contents: read
  pull-requests: write

jobs:
  claude-review:
    uses: lambdaclass/actions/.github/workflows/ai-review-claude.yml@v1
    secrets:
      ANTHROPIC_API_KEY: ${{ secrets.ANTHROPIC_API_KEY }}
```

### On-Demand Reviews

Trigger reviews by commenting on a PR:
- `/review` - Trigger every reviewer the repository calls
- `/kimi` - Trigger Kimi review
- `/codex` - Trigger Codex review
- `/deepseek` - Trigger DeepSeek review
- `/gemini` - Trigger Gemini review
- `/grok` - Trigger Grok review
- `/claude` - Trigger Claude review

**Note:** Slash commands require write access to the repository.

### Custom Prompts

You can customize the review prompt in three ways (in order of priority):

1. **`prompt` input** - Pass a custom prompt directly in the workflow
2. **`.github/prompts/ai-review.md`** - Create this file in your repo with custom instructions. It is read from the PR's base branch, so a PR cannot change the prompt that reviews it; a fetch error other than a missing file fails the review rather than falling back to the default prompt
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

The diff comes from git, a blob-filtered fetch of the merge base and the PR head, not
from the pulls API, which refuses diffs over 20000 lines. `max_diff_lines` caps lines and
`max_diff_bytes` caps the payload after that, so a reviewer never receives more than its context
window holds; Codex reads the repository itself and only takes the line cap.

#### Claude (`ai-review-claude.yml`)

```yaml
jobs:
  claude-review:
    uses: lambdaclass/actions/.github/workflows/ai-review-claude.yml@v1
    secrets:
      ANTHROPIC_API_KEY: ${{ secrets.ANTHROPIC_API_KEY }}
    with:
      model: 'claude-opus-5-5'         # Model ID; 'sonnet', 'opus' and 'haiku' map to the 5.5 models
      effort: 'high'                   # 'low', 'medium', 'high', 'xhigh', 'max'; '' omits (medium)
      max_diff_lines: 10000            # Max lines of diff to review
      max_diff_bytes: 1800000          # Byte cap after the line cap; Claude's tokenizer is ~2.2 bytes/token
      max_tokens: 64000                # Max response tokens, thinking included
      timeout_minutes: 20              # Cancel the review job after this long
      prompt: ''                       # Custom prompt (overrides prompt file)
```

One Messages API call with the diff, no checkout and no tools. Opus 5.5 always
thinks; `effort` sets how much. Requests send `fallbacks: "default"`, so a
safety-classifier refusal is retried server-side on a fallback model instead of
failing the review; the footer shows the model that answered.

This replaces the earlier Claude Code agent workflow of the same name. Callers keep
their `uses:` line and `ANTHROPIC_API_KEY`; `max_turns` and `allowed_tools` are gone, and
the review is now one comment from a single API call instead of an agent run.

#### Gemini (`ai-review-gemini.yml`)

```yaml
jobs:
  gemini-review:
    uses: lambdaclass/actions/.github/workflows/ai-review-gemini.yml@v1
    secrets:
      GEMINI_API_KEY: ${{ secrets.GEMINI_API_KEY }}
    with:
      model: 'gemini-4-argon'          # Gemini model
      thinking_level: 'high'           # 'minimal', 'low', 'medium', 'high'; '' omits
      max_diff_lines: 10000            # Max lines of diff to review
      max_diff_bytes: 2400000          # Byte cap after the line cap, sized to the 1M window
      max_output_tokens: 65536         # Max response tokens, thinking included
      timeout_minutes: 20              # Cancel the review job after this long
      prompt: ''                       # Custom prompt (overrides prompt file)
```

#### Kimi (`ai-review-kimi.yml`)

```yaml
jobs:
  kimi-review:
    uses: lambdaclass/actions/.github/workflows/ai-review-kimi.yml@v1
    secrets:
      KIMI_API_KEY: ${{ secrets.KIMI_API_KEY }}
    with:
      model: 'kimi-k3.1-pro'           # Kimi model
      reasoning_effort: 'high'         # 'low', 'high', 'max', or '' to omit (K2 models)
      thinking: ''                     # '' omits it; K2 models take 'disabled' or 'enabled'
      max_diff_lines: 10000            # Max lines of diff to review
      max_diff_bytes: 2400000          # Byte cap after the line cap, sized to the 1M window
      max_tokens: 65536                # Max response tokens, reasoning included
      temperature: ''                  # '' omits it; Kimi pins temperature per model
      timeout_minutes: 20              # Cancel the review job after this long
      prompt: ''                       # Custom prompt (overrides prompt file)
```

The K3 models always reason: `thinking` stays empty and `reasoning_effort` sets
how much. Moonshot retires the K2 series at the end of December 2026; a repo still
on `kimi-k2.6` or `kimi-k2.7-code` passes `reasoning_effort: ''` and the `thinking`
value that model accepts.

#### DeepSeek (`ai-review-deepseek.yml`)

```yaml
jobs:
  deepseek-review:
    uses: lambdaclass/actions/.github/workflows/ai-review-deepseek.yml@v1
    secrets:
      DEEPSEEK_API_KEY: ${{ secrets.DEEPSEEK_API_KEY }}
    with:
      model: 'deepseek-v4-pro'         # deepseek-v4-pro or deepseek-flash
      reasoning_effort: 'high'         # 'none' disables thinking; 'low', 'high', 'max'; '' omits
      max_diff_lines: 10000            # Max lines of diff to review
      max_diff_bytes: 2400000          # Byte cap after the line cap, sized to the 1M window
      max_tokens: 65536                # Max response tokens, reasoning included
      temperature: ''                  # '' omits it; ignored in thinking mode anyway
      timeout_minutes: 20              # Cancel the review job after this long
      prompt: ''                       # Custom prompt (overrides prompt file)
```

#### Grok (`ai-review-grok.yml`)

```yaml
jobs:
  grok-review:
    uses: lambdaclass/actions/.github/workflows/ai-review-grok.yml@v1
    secrets:
      XAI_API_KEY: ${{ secrets.XAI_API_KEY }}
    with:
      model: 'grok-4.7'                # grok-4.7, grok-build-0.1 or grok-4.3
      reasoning_effort: 'medium'       # 'low', 'medium', 'high', 'xhigh'; '' omits; never off
      max_diff_lines: 10000            # Max lines of diff to review
      max_diff_bytes: 1200000          # Byte cap after the line cap, sized to the 500k window
      max_output_tokens: 16384         # Visible output only; reasoning does not count
      temperature: ''                  # '' omits it
      timeout_minutes: 20              # Cancel the review job after this long
      prompt: ''                       # Custom prompt (overrides prompt file)
```

Grok uses xAI's Responses API (`/v1/responses`), since xAI deprecated Chat
Completions. Requests are sent with `store: false` so xAI does not keep the diff
as a retrievable response.

#### Codex (`ai-review-codex.yml`)

```yaml
jobs:
  codex-review:
    uses: lambdaclass/actions/.github/workflows/ai-review-codex.yml@v1
    secrets:
      OPENAI_API_KEY: ${{ secrets.OPENAI_API_KEY }}
    with:
      model: 'gpt-6.1-sol'             # Codex model
      safety_strategy: 'drop-sudo'     # Codex safety strategy
      max_diff_lines: 10000            # Advisory: agent can regenerate the diff
      timeout_minutes: 20              # Cancel the review job after this long
      prompt: ''                       # Custom prompt (overrides prompt file)
```

> **Two caveats on the Codex failure notice.**
>
> `max_diff_lines` bounds what is written to `/tmp/pr_diff.txt`, but the agent has the
> repository checked out at `fetch-depth: 0` and can regenerate the full diff with
> `git diff`. Treat it as advisory. The kimi input of the same name *is* a hard cap,
> because there the diff is the request payload.
>
> Every workflow comments whenever its review job does not report for itself (timeout,
> cancel, failed checkout or diff), and a
> cancel is a cancel: if a consumer sets `concurrency: cancel-in-progress: true`,
> every superseded run posts a "did not complete" comment. No Actions expression
> distinguishes a timeout-cancel from a concurrency-cancel.
>
> A review that does not happen now **fails the run**, in `ai-review-codex.yml`,
> `ai-review-kimi.yml`, `ai-review-deepseek.yml`, `ai-review-grok.yml`, `ai-review-claude.yml` and
> `ai-review-gemini.yml` -- an empty model response is red, not a green run with an
> explanatory comment. The comment is still posted first. If you gate merges on these
> workflows, note that a provider outage will now block, where previously it passed.

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

permissions:
  contents: read
  pull-requests: write

jobs:
  kimi:
    uses: lambdaclass/actions/.github/workflows/ai-review-kimi.yml@v1
    secrets:
      KIMI_API_KEY: ${{ secrets.KIMI_API_KEY }}

  codex:
    uses: lambdaclass/actions/.github/workflows/ai-review-codex.yml@v1
    secrets:
      OPENAI_API_KEY: ${{ secrets.OPENAI_API_KEY }}

  deepseek:
    uses: lambdaclass/actions/.github/workflows/ai-review-deepseek.yml@v1
    secrets:
      DEEPSEEK_API_KEY: ${{ secrets.DEEPSEEK_API_KEY }}

  grok:
    uses: lambdaclass/actions/.github/workflows/ai-review-grok.yml@v1
    secrets:
      XAI_API_KEY: ${{ secrets.XAI_API_KEY }}

  claude:
    uses: lambdaclass/actions/.github/workflows/ai-review-claude.yml@v1
    secrets:
      ANTHROPIC_API_KEY: ${{ secrets.ANTHROPIC_API_KEY }}

  gemini:
    uses: lambdaclass/actions/.github/workflows/ai-review-gemini.yml@v1
    secrets:
      GEMINI_API_KEY: ${{ secrets.GEMINI_API_KEY }}
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
4. Open a PR. Claude, Kimi, Codex, DeepSeek, Gemini and Grok review it with the
   workflows at the PR's own commit (`.github/workflows/ai-review.yml` calls them
   by local path), and every PR here needs those reviews before it merges.

## License

MIT
