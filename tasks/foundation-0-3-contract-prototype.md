# Foundation 0.3 — F1 Contract Prototype

- Status: Completed
- Version: v0.1
- Owner: APES Maintainers
- Last Updated: 2026-08-10
- Purpose: Execute the F1 Contract Prototype phase by defining and validating one minimal APES artifact metadata contract without moving existing files or introducing runtime tooling.

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

Turn the accepted schema-first architecture into a reviewable contract prototype. The prototype must prove that representative APES metadata can be expressed consistently and that intentionally invalid metadata is rejected, while existing Markdown remains canonical and unchanged.

## Approval and Inputs

- Maintainer approval: explicit approval of the implementation Sprint on 2026-08-07.
- [`../governance/adr/ADR-0002-schema-first-reference-architecture.md`](../governance/adr/ADR-0002-schema-first-reference-architecture.md) — accepted architecture contract.
- [`../docs/repository-evolution-plan.md`](../docs/repository-evolution-plan.md) §25–§28 — canonical contract and staged implementation plan.
- Existing compatibility cases: ADR-0002, SRC-025, Foundation 0.3 task metadata, and the Sprint 3.1 audit task.

## Scope

- Add one JSON Schema 2020-12 contract for parsed YAML front matter metadata.
- Add four representative valid fixtures and four intentionally invalid fixtures.
- Document how current APES metadata maps to the prototype without bulk migration.
- Validate the fixtures with an external, ephemeral schema validator; add no production dependency.
- Update repository indexes, ADR status, and CHANGELOG.

## Out of Scope

- F2 validator CLI, graph builder, `check`, `graph`, or `explain` commands.
- Python package, Node package, dependency manifest, build pipeline, or application source.
- Bulk conversion of existing Markdown headers to YAML front matter.
- Directory moves, generated indexes, workflow evaluator, agent adapter, website, MCP server, IDE extension, or release bundle.
- Phase C Gap Analysis, Phase D Positioning Evidence, new external research, or source-status changes.

## Deliverables

- [`../schemas/artifact-metadata.schema.json`](../schemas/artifact-metadata.schema.json)
- [`../schemas/fixtures/artifact-metadata/README.md`](../schemas/fixtures/artifact-metadata/README.md)
- Eight JSON fixtures under `schemas/fixtures/artifact-metadata/valid/` and `invalid/`.
- [`../schemas/compatibility-mapping.md`](../schemas/compatibility-mapping.md)
- Updated [`../design/01-repository-architecture.md`](../design/01-repository-architecture.md) with the accepted `schemas/` responsibility and extension-policy exception.
- Updated ADR, indexes, and CHANGELOG.

## Acceptance Criteria

- [x] The schema declares JSON Schema 2020-12 and rejects undeclared fields.
- [x] The contract covers identifier, artifact type, lifecycle status, semantic version, owners, typed references, evidence, and last-updated date.
- [x] All four valid fixtures pass schema validation.
- [x] All four invalid fixtures fail for their documented reason.
- [x] At least one fixture maps a real APES ADR and one maps a real APES research source.
- [x] Existing Markdown files remain readable and no existing artifact is moved.
- [x] No production dependency or runtime package is introduced.
- [x] Markdown links, table-of-contents anchors, JSON syntax, UTF-8, final newlines, and `git diff --check` pass.

## Verification

Executed on Windows PowerShell on 2026-08-07:

- PowerShell `ConvertFrom-Json` parse over `schemas/**/*.json` — passed for the schema plus eight fixtures (9 files).
- `uv run --with jsonschema python scripts/.f1-contract-validation.py` — passed with JSON Schema 2020-12 meta-schema checking and format checking enabled: 4/4 valid fixtures accepted; 4/4 invalid fixtures rejected for missing owners, malformed version, ID/type mismatch, and unexpected field respectively. The one-time script was removed after execution and the dependency was not added to the repository.
- The first inline `python -c` attempt failed before validation because PowerShell removed quotes from the native argument. The file-based rerun above passed; the failed attempt is not counted as contract evidence.
- `git diff --check` — passed; Git emitted only the pre-existing `.gitignore` CRLF normalization warning.
- Strict UTF-8 and final-LF scan — passed for 88 Markdown/JSON/YAML/TOML/text files at the time of the run.
- Local Markdown link scan — passed for 229 links across 79 Markdown files.
- Markdown anchor scan — passed for 342 local anchors across 79 Markdown files.
- Conflict-marker, high-confidence credential-pattern, runtime-source, dependency-manifest, and temporary-script scan — passed.

## Rollback

Remove `schemas/` and this task file, then revert the F1-specific ADR/index/CHANGELOG additions. Existing Markdown remains canonical and requires no migration rollback.

## Status

**Completed.** F1 exit criteria passed on 2026-08-07. At this task's closure, F2 and later phases were unstarted and required separate approval. F2 was subsequently approved under ADR-0003, implemented in the sibling `APES-Validator` repository, and remains `In Review`; F3 and later phases remain unstarted.
