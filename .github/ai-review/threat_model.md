# lambdaclass/actions

Reusable GitHub Actions workflows that other repositories call to get AI reviews of their pull
requests (`.github/workflows/pr_review_*.yml`), the README that documents how to call them, and the
multi-model review runner (`ai-review/`: a Python orchestrator that runs Codex and Claude Code agents
on the PR in read-only sandboxes, merges their findings and has a judge model check them).

The reviewer models read attacker-influenced text (the diff, PR title and description, repository
content), so treat them as untrusted. Priorities:
- Secrets and tokens: anything that lets a model read or echo an API key or a GitHub token
  (environment variables passed to model processes or their commands, files on disk, process
  environments under /proc, credentials persisted by checkout or git), or posts model output with a
  token that can do more than comment.
- Script injection: workflow expressions interpolated into `run:` scripts or `github-script` code
  when the value comes from PR titles, branch names, comments, API responses or model output.
- Permissions and triggers: least privilege per job; fork PRs blocked before any secret is used;
  comment triggers restricted by author association; no `pull_request_target` or `workflow_run`
  running PR code with secrets; the write token kept away from jobs that run models.
- Supply chain: external actions pinned to full commit SHAs, CLIs installed at pinned versions,
  downloaded artifacts and API responses treated as untrusted input.
- Sandbox and budget enforcement in the runner: read-deny lists, the soft-budget gates (zsh startup
  file for Codex, PreToolUse hook for Claude Code), lane caps, the run cap watchdog, the PR budget.
  A bypass is a bug.
- Caller compatibility: removed or renamed inputs and secrets, changed defaults, new permissions a
  caller must grant, README examples that no longer match the workflows.
- Correctness: shell quoting, failures that pass silently, multiline values in `$GITHUB_OUTPUT`,
  PR numbers for both `pull_request` and `issue_comment` events.
