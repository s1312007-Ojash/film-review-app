## ADDED Requirements

### Requirement: Project context for OpenSpec artifacts

`openspec/config.yaml` SHALL define a populated `context` block describing the project's tech stack and conventions so that every generated change artifact is grounded in project reality.

#### Scenario: Context is active, not commented out

- **WHEN** OpenSpec generates instructions for any artifact
- **THEN** the `context` field resolves to non-empty content covering the Django 6 / Python 3.14 stack, `uv` workflow, `ruff` settings, and `pytest-django` testing conventions

#### Scenario: Context reflects skeleton state

- **WHEN** an agent reads the resolved context
- **THEN** it learns the project is currently a skeleton with no domain apps yet, so proposals account for creating apps and wiring them in

### Requirement: Per-artifact authoring rules

`openspec/config.yaml` SHALL define a `rules` block with concise per-artifact guardrails that constrain how proposals, design, and tasks artifacts are written.

#### Scenario: Rules are applied during generation

- **WHEN** OpenSpec generates a proposal, design, or tasks artifact
- **THEN** the corresponding rules from `config.yaml` are included as constraints (e.g. keep proposals concise, express tasks against the `uv run` command surface)

#### Scenario: Rules are valid YAML the CLI accepts

- **WHEN** `openspec status` or `openspec instructions` runs against a change
- **THEN** the CLI parses `config.yaml` without error and surfaces the configured rules
