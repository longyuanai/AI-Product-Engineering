# Artifact Metadata Compatibility Mapping

- Status: Active
- Version: v0.2
- Owner: APES Maintainers
- Last Updated: 2026-08-09
- Purpose: Show how representative existing APES artifacts map to the F1 metadata contract without rewriting or moving them.

## Table of Contents

- [Compatibility Rule](#compatibility-rule)
- [Representative Mapping](#representative-mapping)
- [Known Prototype Limits](#known-prototype-limits)
- [Migration Boundary](#migration-boundary)

## Compatibility Rule

The F1 schema validates the object produced after YAML front matter is parsed. JSON fixtures are used because JSON and parsed YAML share the same object model and JSON fixtures can be validated without changing canonical Markdown.

Existing bullet-style metadata headers remain readable and authoritative during F1. The fixture mapping demonstrates compatibility intent; it is not a bulk migration or a claim that every existing document already conforms.

## Representative Mapping

| Existing artifact | Prototype fixture | Mapping note |
| --- | --- | --- |
| [`../governance/adr/ADR-0002-schema-first-reference-architecture.md`](../governance/adr/ADR-0002-schema-first-reference-architecture.md) | [`fixtures/artifact-metadata/valid/adr-0002.json`](fixtures/artifact-metadata/valid/adr-0002.json) | Uses the real ADR ID, accepted status, evidence references, and maintainer ownership. |
| `SRC-025` in [`../research/source-register.md`](../research/source-register.md) | [`fixtures/artifact-metadata/valid/source-src-025.json`](fixtures/artifact-metadata/valid/source-src-025.json) | Represents a Source Register row as an artifact node without changing the row schema. |
| [`../tasks/foundation-0-3-contract-prototype.md`](../tasks/foundation-0-3-contract-prototype.md) | [`fixtures/artifact-metadata/valid/task-foundation-0-3.json`](fixtures/artifact-metadata/valid/task-foundation-0-3.json) | Demonstrates task identity, dependencies, evidence, owner, and active lifecycle state. |
| [`../tasks/sprint-03-1-coverage-audit.md`](../tasks/sprint-03-1-coverage-audit.md) | [`fixtures/artifact-metadata/valid/audit-sprint-03-1.json`](fixtures/artifact-metadata/valid/audit-sprint-03-1.json) | Represents the completed coverage audit as a typed Audit node. |

## Known Prototype Limits

- The contract validates shape, local identifier syntax, and all thirteen type-to-ID-prefix rules; F2 resolves IDs across repository files.
- JSON Schema validates semantic-version syntax but does not evaluate lifecycle transitions.
- Evidence references are syntactically validated but not checked against Source Register rows.
- Date format is declared as a JSON Schema string with `date` format. F2 normalizes a YAML date scalar such as unquoted `2026-08-09` to its ISO string before validation; JSON consumers continue to supply a string.
- Existing title-block metadata uses `Owner` while the prototype uses the normalized array field `owners`.

Those repository-aware checks belong to F2 and are not implied by an F1 schema pass.

## Migration Boundary

F1 moves no files and rewrites no existing header. A future migration requires a separately approved task, a compatibility report, dry-run output, and rollback paths. Removing the prototype leaves all current APES documents readable and authoritative.
