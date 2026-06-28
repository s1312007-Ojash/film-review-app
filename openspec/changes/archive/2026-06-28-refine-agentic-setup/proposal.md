## Why

The repository's agentic configuration has drifted: the agent-guidance file is named `AGENTS.md` but its top-level heading still reads `# CLAUDE.md`, and there is no longer a `CLAUDE.md` for Claude Code to discover. Separately, `openspec/config.yaml` ships with its `context` and `rules` entirely commented out, so every OpenSpec proposal/design/tasks artifact is generated with zero project grounding. Fixing both now — while the project is still a skeleton — keeps future AI-assisted work consistent and grounded instead of compounding the drift.

## What Changes

- Establish a single source of truth for agent guidance in `AGENTS.md` and correct its `# CLAUDE.md` heading to `# AGENTS.md`.
- Restore Claude Code discovery by adding a thin `CLAUDE.md` that points to `AGENTS.md` (no duplicated content to drift out of sync).
- Populate `openspec/config.yaml` `context` with the project's tech stack and conventions (Django 6 / Python 3.14, `uv`, `ruff`, `pytest-django` with `@pytest.mark.django_db`, skeleton state).
- Populate `openspec/config.yaml` `rules` with concise per-artifact guardrails (e.g. proposals stay concise, tasks reference the `uv run` command surface).
- No application, `config/`, or test code changes — documentation and agent-configuration files only.

## Capabilities

### New Capabilities
- `agent-guidance`: Convention for AI agent instruction files — `AGENTS.md` as the canonical guidance document and `CLAUDE.md` as a non-duplicating pointer to it, with correct headings.
- `openspec-config`: Project-grounding content for OpenSpec — the `context` block and per-artifact `rules` in `openspec/config.yaml` that every change artifact inherits.

### Modified Capabilities
<!-- None: no existing specs in openspec/specs/. -->

## Impact

- Files: `AGENTS.md` (heading fix), new `CLAUDE.md` (pointer), `openspec/config.yaml` (context + rules).
- Tooling: improves grounding for all future `/opsx:*` runs and Claude Code sessions.
- No code, dependency, migration, or runtime impact; no breaking changes.
