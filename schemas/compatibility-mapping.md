# Artifact Metadata Compatibility Mapping

- Status: Active
- Version: v0.3
- Owner: APES Maintainers
- Last Updated: 2026-08-27
- Purpose: Show how representative existing APES artifacts map to the F1 metadata contract without rewriting or moving them.

## Table of Contents

- [Compatibility Rule](#compatibility-rule)
- [Representative Mapping](#representative-mapping)
- [Type and ID Prefix Resolution](#type-and-id-prefix-resolution)
- [Known Prototype Limits](#known-prototype-limits)
- [Migration Boundary](#migration-boundary)

## Compatibility Rule

The F1 schema validates parsed metadata objects represented by fixtures under [`fixtures/artifact-metadata/`](fixtures/artifact-metadata/README.md). JSON fixtures are used because JSON and parsed YAML share the same object model and can be validated without changing canonical Markdown.

Existing bullet-style metadata headers remain readable and authoritative. The fixture mapping demonstrates compatibility intent only; it is not a bulk migration, a claim that repository Markdown contains YAML front matter, or a claim that existing files conform to the fixture-only contract. This boundary is proposed in [`ADR-0005`](../governance/adr/ADR-0005-fixture-only-artifact-metadata-boundary.md).

## Representative Mapping

| Existing artifact | Prototype fixture | Mapping note |
| --- | --- | --- |
| [`../governance/adr/ADR-0002-schema-first-reference-architecture.md`](../governance/adr/ADR-0002-schema-first-reference-architecture.md) | [`fixtures/artifact-metadata/valid/adr-0002.json`](fixtures/artifact-metadata/valid/adr-0002.json) | Uses the real ADR ID, accepted status, evidence references, and maintainer ownership. |
| `SRC-025` in [`../research/source-register.md`](../research/source-register.md) | [`fixtures/artifact-metadata/valid/source-src-025.json`](fixtures/artifact-metadata/valid/source-src-025.json) | Represents a Source Register row as an artifact node without changing the row schema. |
| [`../tasks/foundation-0-3-contract-prototype.md`](../tasks/foundation-0-3-contract-prototype.md) | [`fixtures/artifact-metadata/valid/task-foundation-0-3.json`](fixtures/artifact-metadata/valid/task-foundation-0-3.json) | Demonstrates task identity, dependencies, evidence, owner, and active lifecycle state. |
| [`../tasks/sprint-03-1-coverage-audit.md`](../tasks/sprint-03-1-coverage-audit.md) | [`fixtures/artifact-metadata/valid/audit-sprint-03-1.json`](fixtures/artifact-metadata/valid/audit-sprint-03-1.json) | Represents the completed coverage audit as a typed Audit node. |

## Type and ID Prefix Resolution

Schema v0.3.0 adds the two first-class pairs proposed by [`RFC-0001`](../governance/rfc/RFC-0001-template-checklist-artifact-types.md):

| Artifact type | Required ID prefix |
| --- | --- |
| `Template` | `TEMPLATE-` |
| `Checklist` | `CHECKLIST-` |

These pairs apply to fixture objects validated by the schema. They do not retroactively rewrite or validate repository Markdown headers.

## Known Prototype Limits

- The contract validates shape, local identifier syntax, and all fifteen type-to-ID-prefix rules; repository-aware resolution is outside this fixture-only contract.
- JSON Schema validates semantic-version syntax but does not evaluate lifecycle transitions.
- Evidence references are syntactically validated but not checked against Source Register rows.
- `last_updated` remains a JSON Schema string with `date` format. YAML producers must quote date-like values so a loader preserves the string type; [`invalid/unquoted-last-updated.yaml`](fixtures/artifact-metadata/invalid/unquoted-last-updated.yaml) records the rejected unquoted-scalar case.
- Existing title-block metadata uses `Owner` while the prototype uses the normalized array field `owners`.

Those repository-aware checks belong to F2 and are not implied by an F1 schema pass.

## Migration Boundary

F1 and P0-1 move no files and rewrite no existing header. A future migration requires a separately approved task, an accepted decision, a compatibility report, dry-run output, and rollback paths. Removing the prototype leaves all current APES documents readable and authoritative.
