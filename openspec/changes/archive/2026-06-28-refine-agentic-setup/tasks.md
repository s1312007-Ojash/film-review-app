## 1. Agent guidance files

- [x] 1.1 In `AGENTS.md`, change the first-level heading from `# CLAUDE.md` to `# AGENTS.md`, leaving all other sections (project state, commands, architecture notes, conventions) unchanged.
- [x] 1.2 Create a thin `CLAUDE.md` at the repo root that points to `AGENTS.md` as the canonical guidance and contains no duplicated guidance content.

## 2. OpenSpec project grounding

- [x] 2.1 In `openspec/config.yaml`, uncomment/add a populated `context:` block summarizing the stack (Django 6 / Python 3.14), the `uv` workflow, ruff settings, `pytest-django` (`@pytest.mark.django_db`) conventions, and the skeleton state — pointing to `AGENTS.md` as the fuller source.
- [x] 2.2 In `openspec/config.yaml`, add a `rules:` block with concise per-artifact guardrails for `proposal`, `design`, and `tasks` (e.g. keep proposals concise with a non-goals framing; express tasks against the `uv run` command surface).

## 3. Verify

- [x] 3.1 Run `openspec status --change refine-agentic-setup` and confirm the CLI parses `config.yaml` without error.
- [x] 3.2 Confirm `AGENTS.md` heading reads `# AGENTS.md` and `CLAUDE.md` resolves to a pointer (manual read).
