# Sprint 05 — Lifecycle Templates and Stage Gates

- Status: Completed
- Version: v0.1
- Owner: APES Maintainers
- Last Updated: 2026-08-19
- Purpose: Deliver one reusable document template per lifecycle stage and one evidence-based checklist per circular stage gate.

## Table of Contents

- [Goal](#goal)
- [Approval and Inputs](#approval-and-inputs)
- [Scope](#scope)
- [Out of Scope](#out-of-scope)
- [Deliverables](#deliverables)
- [Acceptance Criteria](#acceptance-criteria)
- [Verification](#verification)
- [Rollback](#rollback)
- [Status](#status)

## Goal

Complete the v0.2 roadmap work for lifecycle document templates and quality / stage-gate checklists while preserving the documentation-first, vendor-neutral, evidence-anchored repository boundary.

## Approval and Inputs

- Maintainer approval: direct instruction in the 2026-08-19 session to implement Sprint 05.
- [`../docs/lifecycle.md`](../docs/lifecycle.md) — nine-stage lifecycle and circular feedback model.
- [`../docs/stage-gates.md`](../docs/stage-gates.md) — gate discipline and output index.
- [`../standards/README.md`](../standards/README.md) — current module scaffold and lifecycle alignment.
- [`../schemas/artifact-metadata.schema.json`](../schemas/artifact-metadata.schema.json) — artifact metadata Schema v0.2.0.
- [`../research/source-register.md`](../research/source-register.md) — source, access-date, reliability, and verification conventions.
- [`../tests/test_repository_contracts.py`](../tests/test_repository_contracts.py) — read-only repository contract checks.

## Scope

- Correct the stale Sprint 04 status and lifecycle-to-standards description.
- Define and index the lifecycle template contract.
- Create one vendor-neutral template for each of the nine lifecycle stages.
- Create nine gate checklists, including Knowledge → Discovery.
- Replace the placeholder stage-gate output section with real mappings.
- Record the missing Template / Checklist Schema types as an open question.
- Extend repository contract tests and synchronize task and change records.

## Out of Scope

- Changes to any JSON file under `schemas/`.
- A new RFC or a new or renamed standard module directory.
- CLI, MCP server, website, extension, build pipeline, or application source.
- Changes to F2 or F3 status, the sibling validator repository, Sprint 2 gate conclusions, or GitHub Actions.
- Production dependencies, releases, commits, pushes, tags, or branches.

## Deliverables

- [`../templates/README.md`](../templates/README.md) — active template contract and index.
- Nine lifecycle templates: [`idea-brief.md`](../templates/idea-brief.md), [`discovery-interview-notes.md`](../templates/discovery-interview-notes.md), [`research-note.md`](../templates/research-note.md), [`validation-experiment-plan.md`](../templates/validation-experiment-plan.md), [`product-scope-spec.md`](../templates/product-scope-spec.md), [`business-viability-brief.md`](../templates/business-viability-brief.md), [`engineering-change-record.md`](../templates/engineering-change-record.md), [`growth-experiment-record.md`](../templates/growth-experiment-record.md), and [`retrospective-and-learning-record.md`](../templates/retrospective-and-learning-record.md).
- [`../checklists/README.md`](../checklists/README.md) and nine indexed `gate-N-*.md` checklists.
- Updated lifecycle, stage-gate, standards, and repository evolution documentation.
- Three additional tests in [`../tests/test_repository_contracts.py`](../tests/test_repository_contracts.py).
- Updated [`README.md`](README.md) task index and [`../CHANGELOG.md`](../CHANGELOG.md).

## Acceptance Criteria

- [x] The two Phase 0 inconsistencies are corrected without structural expansion.
- [x] Nine lifecycle templates and nine circular gate checklists exist and are indexed.
- [x] Every template has the repository metadata header, resolvable Table of Contents, evidence fields, Out of Scope section, and boundary statement.
- [x] Template bodies are vendor-neutral.
- [x] `templates/README.md` and `docs/stage-gates.md` are Active and no longer marked Placeholder.
- [x] OQ-11 records the Schema taxonomy gap, fallback, cost, and resolution trigger; Schema JSON is unchanged.
- [x] Repository contract tests total ten and cover metadata, type-prefix binding, and exact lifecycle / gate correspondence.
- [x] Local Markdown links and anchors resolve, and whitespace validation reports no error.

## Verification

Executed on Windows PowerShell on 2026-08-19:

- `uv run --with jsonschema python -B -m unittest discover -s tests -v` — passed, 10 tests, `OK`.
- `git diff --check` — passed with no error; the pre-existing `.gitignore` CRLF warning remains informational.
- The test suite scans repository-local Markdown links and anchors, exact template and gate file sets, required template metadata, Schema type-prefix binding, and prohibited vendor names in template bodies.

## Rollback

Remove the nine new files under `templates/`, the nine new `gate-N-*.md` files under `checklists/`, and this task file. Revert only the Sprint 05 hunks in `templates/README.md`, `checklists/README.md`, `docs/stage-gates.md`, `docs/lifecycle.md`, `standards/README.md`, `docs/repository-evolution-plan.md`, `tests/test_repository_contracts.py`, `CHANGELOG.md`, `tasks/README.md`, and `tasks/sprint-04-ai-coding-tool-guidance.md`, preserving all pre-existing user changes.

## Status

**Completed.** All scoped documentation and contract tests were implemented and verified on 2026-08-19. F2 remains `In Review`; Sprint 2 gate conclusions remain unchanged.
