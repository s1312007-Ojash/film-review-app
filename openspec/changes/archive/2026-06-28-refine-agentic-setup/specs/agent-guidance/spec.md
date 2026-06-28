## ADDED Requirements

### Requirement: Canonical agent-guidance document

The repository SHALL maintain `AGENTS.md` at the repository root as the single canonical source of agent guidance, and its top-level heading SHALL match its filename.

#### Scenario: Heading matches filename

- **WHEN** a reader or tool opens `AGENTS.md`
- **THEN** its first-level heading reads `# AGENTS.md` (not `# CLAUDE.md` or any other filename)

#### Scenario: Guidance content is preserved

- **WHEN** the heading is corrected
- **THEN** the existing project-state, commands, architecture-notes, and conventions sections remain intact and unchanged in meaning

### Requirement: Claude Code discovery pointer

The repository SHALL provide a `CLAUDE.md` at the repository root so Claude Code discovers project guidance, and that file SHALL point to `AGENTS.md` rather than duplicating its content.

#### Scenario: Claude Code finds guidance

- **WHEN** Claude Code starts a session and looks for `CLAUDE.md`
- **THEN** it finds the file and the file directs the reader to `AGENTS.md` as the source of truth

#### Scenario: No content duplication

- **WHEN** guidance content changes
- **THEN** only `AGENTS.md` needs editing, because `CLAUDE.md` carries a pointer and no copied guidance that could drift
