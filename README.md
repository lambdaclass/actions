# Reusable GitHub Actions

This repository contains a reusable GitHub Actions workflow for AI-powered PR reviews: `pr_review_multi.yml`, an agentic multi-model security review that posts one comment with findings checked against the code.

## Multi-model PR Review

`pr_review_multi.yml` runs a security review with several models and posts **one** comment.

1. **Reviewers.** Opus 5.5 (effort xhigh), GPT 6.1 Sol, Kimi K3.1, GLM 5.3 and DeepSeek V4 Pro review the PR in parallel. Each is an agent (Claude Code or Codex) in a read-only sandbox with no network, so it reads callers, checks and types outside the diff. A soft budget asks each reviewer to finish: after 80 commands (120 for GPT and GLM), about $1.50–2.50 of estimated spend, or 30 minutes, whichever comes first; the dollar limits grow with the size of the prompt. A PR made only of `low_risk` code gets three reviewers instead of five (see below).
2. **Housekeeping.** A cheap model (DeepSeek V4 Flash) lists stale docs, missing tests, leftovers and inconsistencies, separately from the security review.
3. **Malicious-code check.** One cheap call (DeepSeek V4 Flash) looks for code aimed at whoever builds, tests or opens the repository: tests, build and install scripts, git hooks, CI workflows, editor tasks and dependency sources, plus every line a pattern scan matched in any changed file but docs (hidden Unicode, `curl | sh`, credential paths, secret environment variables, dependencies from git URLs or tarballs). Anything it reports goes at the top of the comment. On 10 planted attacks and 6 look-alike clean changes it caught all 10 and flagged none of the 6; on 10 real merged PRs it raised one item (a dependency from a personal fork). It costs well under a cent per PR.
4. **Merge and judge.** Duplicate findings are merged. A judge (GPT 6.1 Sol) checks the findings against the code, sees every reviewer's claim, and marks each one a bug, suspected, pre-existing, or likely not a problem. The comment says how many it checked; findings it did not reach (more than 60, or over the budget) are marked *unverified*.
5. **Comment.** It opens with a table of findings to check (severity, status, which models found it, where). Below that come collapsed sections: details, duplicates, pre-existing bugs, findings the judge dismissed (with its reason), and housekeeping. A last line gives what the review cost.

### Set it up in a repository

1. **Secrets.** Make `OPENROUTER_API_KEY` and `ANTHROPIC_API_KEY` available to the repository, preferably as organization secrets so that each repository needs nothing. The secrets table below says what limits to put on them.
2. **One workflow file.** Copy the example below to `.github/workflows/ai-review.yml` and pin it to a commit (see [Versioning](#versioning)). `v2.0.0` and earlier tags don't have this workflow.
3. **Nothing else is required.** Without a config, built-in rules decide which changed files each part of the review reads, with the default prompt. Add `.github/ai-review/config.toml` or `threat_model.md` only to change that (see [Repository config](#repository-config)).
4. **Try it.** Add the `ai-review` label to a PR; the label works from the PR that adds the workflow file. `/review` comments work only once the file is on the default branch, because GitHub runs comment triggers from there. The comment arrives in 15–35 minutes.

```yaml
name: AI Review

# Comment `/review` on a PR, or add a label starting with `ai-review`.
on:
  issue_comment:
    types: [created]
  pull_request:
    types: [labeled]

permissions: {}

jobs:
  review:
    # Adding a label needs triage or write access. Fork PRs are refused here and again in the workflow.
    if: >
      (
        github.event_name == 'issue_comment' &&
        github.event.issue.pull_request &&
        contains(fromJSON('["OWNER", "MEMBER", "COLLABORATOR"]'), github.event.comment.author_association) &&
        (github.event.comment.body == '/review' || startsWith(github.event.comment.body, '/review ') || startsWith(github.event.comment.body, fromJSON('"/review\n"')) || startsWith(github.event.comment.body, fromJSON('"/review\r"')))
      ) ||
      (
        github.event_name == 'pull_request' &&
        startsWith(github.event.label.name, 'ai-review') &&
        github.event.pull_request.head.repo.full_name == github.repository
      )
    uses: lambdaclass/actions/.github/workflows/pr_review_multi.yml@<tag commit SHA> # <tag>
    permissions:
      contents: read
      pull-requests: write
      actions: read
    with:
      command: /review
    secrets:
      OPENROUTER_API_KEY: ${{ secrets.OPENROUTER_API_KEY }}
      ANTHROPIC_API_KEY: ${{ secrets.ANTHROPIC_API_KEY }}
```

The comment check matches `/review` alone or followed by options, not words that merely start with it (`/reviewer`). The label branch skips fork PRs, which get no secrets on `pull_request` events; the workflow refuses them too. The label runs the PR's version of this caller file, so a change to its inputs applies to that PR's own review.

**Commands.** Options go after the command, on the first line of the comment:

| Comment | Effect |
|---|---|
| `/review` | Review the PR |
| `/review budget=80` | Use $80 for this review (at most `max_budget`) |
| `/review continue` | Finish an earlier review of the same commit that stopped at its budget or time limit; reviewers that finished are reused |

**Inputs:**

| Input | Required | Default | Description |
|-------|----------|---------|-------------|
| `command` | No | `/review` | The caller's comment command, used in the hint a partial review prints |
| `pr_budget` | No | `0` | USD limit per review. `0` = $30 |
| `max_budget` | No | `100` | Highest budget a `budget=N` comment may ask for |
| `lanes` | No | `''` | Reviewer models, comma-separated: `claude`, `gpt`, `kimi`, `glm`, `deepseek`, `gemini`, `grok`, `fable`. Empty = the first five |
| `config_dir` | No | `.github/ai-review` | Directory with the optional `config.toml` and `threat_model.md` in your repository |
| `housekeeping` | No | `true` | Run the housekeeping reviewer |
| `sandbox_check` | No | `strict` | Check the Codex reviewers' sandbox before any paid call (not Claude Code's): `strict` stops the review if it fails, `warn` only logs it, `off` skips it ([details](#sandbox-check)) |

**Secrets:**

| Secret | Required | Description |
|--------|----------|-------------|
| `OPENROUTER_API_KEY` | Yes | OpenRouter key for every model but Claude. It must belong to the account that holds the `air-*` provider presets (see below). Give it a credit limit: that limit is the hard ceiling on spend |
| `ANTHROPIC_API_KEY` | Unless `lanes` leaves out both `claude` and `fable` | Anthropic key for the Opus reviewer. Use a workspace with a monthly spend limit |

The calling job must grant `contents: read`, `pull-requests: write` and `actions: read`. Only the final job, which posts the comment, gets `pull-requests: write`; the jobs that run models get read permissions only. `actions: read` lets `continue` download the earlier review.

### Repository config

Both files are optional: a `config.toml` and a `threat_model.md` in `.github/ai-review/` in your repository. They are read from the PR's base branch, so a PR's own changes to them do not apply to its review. (Callers that also trigger on `pull_request` events run the PR's version of their own workflow file, which can change the inputs.) `threat_model` must be the name of a `.md` file in the same directory: the workflow fetches only `*.toml` and `*.md` files. Without a config only the built-in rules below apply.

Each changed file is handled by the first rule that matches:

1. `always_review` globs: reviewed as code, whatever the rules below say (binary files and whitespace-only changes excepted). For text that drives behaviour, such as model prompts.
2. `ignore` globs: not sent to the security reviewers.
3. Built in, not sent to the security reviewers: lockfiles, binary files, generated and vendored code (`vendor/`, `node_modules/`, `dist/`, `*.min.js`, `*.pb.go`, ...), whitespace-only changes (except in Python, shell, YAML and Makefiles), and docs (`.md`, `.txt`, `LICENSE`, ...).
4. Tests (built-in patterns such as `tests/`, `*_test.rs`, `*.test.ts`, plus `test_globs`): reviewers get the list of test files and the test functions they add, change or remove, not their diff, and open them as needed.
5. Everything else is code, including build and install scripts, dependency manifests, git hooks, CI workflows and editor tasks, and gets all five reviewers.

These rules decide what goes into the security reviewers' prompt as *the diff*: the PR's changes to each file. They work in a checkout of the PR and can open any other file. The other two parts read differently:

- **Housekeeping** reads the diff of code and docs. It opens the tests to look for missing ones.
- **Malicious-code check** reads the diff of every changed file except docs, lockfiles and binary files, so it also reads the tests, generated and vendored code, whitespace-only changes and `ignore` globs. From lockfiles it gets only the lines the pattern scan matches (dependency sources, install scripts, ...). It runs only when the PR changes a test, a build or install script, a dependency manifest, a git hook, a CI workflow or an editor task, or when the pattern scan matches a line in any file but docs. Otherwise the security reviewers already have everything it would read.

No part reads binary files; they are listed at the top of the comment.

A PR made only of `low_risk` code gets `low_risk_lanes` instead, unless a cheap triage call finds that it touches keys, auth, funds, cryptography or untrusted input.

| Key | Required | Default | What it does |
|-----|----------|---------|--------------|
| `threat_model` | No | `threat_model.md`, if present | What matters in this repository; goes into every reviewer prompt |
| `ignore` | No | none | Files not reviewed |
| `test_globs` | No | none | Extra test file patterns |
| `always_review` | No | none | Files reviewed as code even if they look like docs, tests, generated or vendored code |
| `low_risk` | No | none | Code that needs fewer reviewers (demo apps, local tooling) |
| `low_risk_lanes` | No | `gpt`, `kimi`, `glm` | Reviewers of a PR made only of `low_risk` code |

```toml
threat_model = "threat_model.md"
ignore = ["benches/**"]
test_globs = ["fixtures/**"]
always_review = ["prompts/**"]
low_risk = ["examples/**", "scripts/**"]
```

The keys `sensitive`, `default_sensitive`, `priority`, `nonsensitive_lanes` and `unit_depth` of earlier versions are refused with a message that says what replaces them.

Most repositories don't need a `threat_model.md`. Add one only when a reviewer can't tell from the code what is attacker-controlled or what the system must guarantee (for a prover: the verifier must reject false proofs). Keep it short and say what matters; don't list what not to report: in our tests, rules like that made the models miss real bugs. See [`.github/ai-review/`](.github/ai-review/) in this repository for an example.

### Cost and large PRs

- **Typical cost:** about $3.40 for a normal PR at API prices, about half of it Opus; about $7–12 near the size limit. The comment's last line shows the cost of each review. In CI this figure is computed from token counts and published prices. The OpenRouter bill is exact, but a key shared by several repositories can't attribute it to one review.
- **Size limit:** one review covers the whole PR, up to 20,000 *effective* lines: changed code (whitespace-only changes ignored, except in Python, shell, YAML and Makefiles; long deletions compacted) plus half the test lines; docs, lockfiles and generated files do not count. A bigger PR is not reviewed: the comment gives its effective size and asks for it to be split. The reviewers' prompt holds about 600,000 characters of diff (about 15,000 lines of whole functions); above that the largest changes come first and the rest is listed for them to read in the checkout. Changed files that no security reviewer saw (binary to git, whitespace-only changes, unusual file names) are listed at the top of the comment.
- **Budget:** $30 per review by default (`pr_budget`; `budget=N` in a comment raises it). If a review stops at its budget or time limit, the comment says so and `/review continue` finishes it, reusing the reviewers that finished.
- **Hard limits:** each reviewer is killed at its lane cap ($3–4 estimated). A watchdog stops the whole review at the PR budget, counting this review's own computed spend (other reviews may share the key). The ceilings the providers enforce are the OpenRouter key's credit limit, for every model but Opus, and the Anthropic workspace's spend limit, for Opus.
- **Time:** a review takes 15–35 minutes, up to about an hour for a PR near the size limit. The judge is skipped (findings marked unverified) if the reviewers end more than 285 minutes after the start, so the comment is posted inside the job's 330-minute limit.

### Sandbox check

Before any paid call the runner runs one command in the sandbox of the Codex reviewers (every model but Opus and Fable), with no model, and checks that it works and that it cannot read other processes' environments, where the API keys are. With `sandbox_check: strict` (the default) a failed check stops the review and the comment says why; `warn` only logs it. The check does not cover the Claude Code sandbox that Opus and Fable run in.

### Provider presets

Each OpenRouter model is called through a preset (`model@preset/air-...`, listed in [`ai-review/presets.json`](ai-review/presets.json)). The preset pins the provider, for example Anthropic's and OpenAI's own servers, or full-precision hosts for open models. The runner uses a model's preset only when OpenRouter's live endpoint list, read at the start of the review, shows a host the pin allows (for some open models, also under a price limit). If that check fails, for example because the lookup errors, that reviewer runs unpinned, on any host, for the whole review; the report in the run's artifact marks it `UNPINNED`. Presets belong to an OpenRouter account, so `OPENROUTER_API_KEY` must come from that account. Its privacy setting (no providers that train on prompts) also applies to every key in it.

### Running it locally

`ai-review/run_pilot.py` is the runner the workflow calls. It needs Python 3.11 or newer; `python3 ai-review/run_pilot.py --help` lists its options. It reads the OpenRouter key from `OPENROUTER_API_KEY` when that is set, else from the macOS Keychain. Its defaults are not CI's: CI passes `--isolate shared --claude-auth anthropic --experiment-cap 0 --sandbox-check strict --deadline-min 240` (see `pr_review_multi.yml`), while locally Opus goes through OpenRouter, spend is isolated per reviewer, a $50 cap over all local runs applies, and the sandbox check is off. `--dry-run` shows the parts, the reviewers and the estimated cost without making a paid call.

---

## Versioning

Pin callers to the commit SHA of a [release tag](https://github.com/lambdaclass/actions/tags):

```yaml
uses: lambdaclass/actions/.github/workflows/pr_review_multi.yml@<tag commit SHA> # <tag>
```

The single-model reviews (`pr_review_claude.yml`, `pr_review_codex.yml`, `pr_review_kimi.yml`, `pr_review_openrouter.yml`) were removed after `v2.0.0`. Callers pinned to `v2.0.0` or earlier keep working; their docs are in the README at that tag.

## Security

### Fork PR Protection

The workflow refuses fork PRs on every trigger before any secret is used, and posts a comment saying so. The [caller example](#set-it-up-in-a-repository) also skips them in its `if` for `pull_request` events, for defense in depth: the caller skips fork PRs, and the shared workflow enforces it as a fail-safe.
