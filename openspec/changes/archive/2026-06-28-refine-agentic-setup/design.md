## Context

The agentic setup spans three configuration surfaces: `AGENTS.md` (general agent guidance), `CLAUDE.md` (Claude Code's discovery file), and `openspec/config.yaml` (grounding for OpenSpec artifact generation). Currently `AGENTS.md` holds the real guidance but carries a `# CLAUDE.md` heading, `CLAUDE.md` itself is absent, and `openspec/config.yaml` has its `context`/`rules` fully commented out. The project is a fresh Django 6 / Python 3.14 skeleton managed with `uv`, so the grounding content already exists in `AGENTS.md` and can be reused verbatim. This is a low-risk, documentation-only change.

## Goals / Non-Goals

**Goals:**
- One canonical guidance file (`AGENTS.md`) with a heading that matches its name.
- Claude Code discovery preserved via a thin, non-duplicating `CLAUDE.md` pointer.
- OpenSpec artifact generation grounded by an active `context` and `rules` block.

**Non-Goals:**
- No changes to application code, `config/`, migrations, tests, or dependencies.
- Not rewriting the substance of `AGENTS.md` (only the heading changes).
- Not authoring domain specs for films/reviews/accounts — out of scope.

## Decisions

- **`AGENTS.md` is canonical, `CLAUDE.md` is a pointer.** Both Claude Code and other agents look for their own filename; rather than maintain two copies that drift (which is how the current `# CLAUDE.md`-in-`AGENTS.md` mismatch arose), keep all substance in `AGENTS.md` and make `CLAUDE.md` a 2–3 line redirect. Alternative considered: keep full content in both — rejected because it guarantees future drift. Alternative: a symlink — rejected for poor cross-platform (Windows) ergonomics and git friction.
- **Reuse existing guidance text for `config.yaml` context.** The `context` block paraphrases the already-vetted sections of `AGENTS.md` (stack, `uv` commands, ruff/pytest conventions, skeleton state) instead of inventing new content, keeping the two in agreement.
- **Keep `rules` minimal.** A few guardrails per artifact (proposal concise + non-goals, tasks expressed against `uv run`, design only when warranted) rather than an exhaustive list, to avoid over-constraining generation.

## Risks / Trade-offs

- **Risk: `AGENTS.md` and `config.yaml` context drift apart over time** → Mitigation: context is a short summary that points to `AGENTS.md` as the fuller source, so the canonical file remains the place to update.
- **Risk: malformed YAML breaks the OpenSpec CLI** → Mitigation: validate by running `openspec status --change refine-agentic-setup` after editing `config.yaml`; the apply step will catch parse errors immediately.
- **Trade-off: a pointer `CLAUDE.md` means one extra hop for Claude Code** — accepted; the cost is trivial versus duplicated-content drift.

## Migration Plan

No runtime migration. Changes are file edits only; rollback is a `git revert` of the documentation commit. No deploy step.
