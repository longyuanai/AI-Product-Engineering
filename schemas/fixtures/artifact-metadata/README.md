# Artifact Metadata Fixtures

- Status: Active
- Version: v0.2
- Owner: APES Maintainers
- Last Updated: 2026-08-27
- Purpose: Provide deterministic positive and negative cases for the F1 artifact metadata schema.

## Table of Contents

- [Expected Results](#expected-results)
- [Validation Rule](#validation-rule)

## Expected Results

| Fixture | Expected | Constraint exercised |
| --- | --- | --- |
| [`valid/adr-0002.json`](valid/adr-0002.json) | Valid | Accepted ADR with evidence references. |
| [`valid/source-src-025.json`](valid/source-src-025.json) | Valid | Source node with empty relationship lists. |
| [`valid/task-foundation-0-3.json`](valid/task-foundation-0-3.json) | Valid | Active task with dependencies and evidence. |
| [`valid/audit-sprint-03-1.json`](valid/audit-sprint-03-1.json) | Valid | Completed audit with task dependency. |
| [`invalid/missing-owners.json`](invalid/missing-owners.json) | Invalid | Required `owners` field is absent. |
| [`invalid/malformed-version.json`](invalid/malformed-version.json) | Invalid | Version is not Semantic Versioning syntax. |
| [`invalid/type-id-mismatch.json`](invalid/type-id-mismatch.json) | Invalid | ADR type uses a `TASK-` identifier. |
| [`invalid/unexpected-field.json`](invalid/unexpected-field.json) | Invalid | Undeclared `notes` field violates `additionalProperties: false`. |
| [`invalid/unquoted-last-updated.yaml`](invalid/unquoted-last-updated.yaml) | Invalid | Unquoted YAML date becomes a date object instead of the required string. |

## Validation Rule

A fixture pass means every machine-readable fixture under `valid/` is accepted and every machine-readable fixture under `invalid/` is rejected for at least one schema constraint. YAML fixtures are parsed before validation. Negative fixtures are never counted as successful merely because a validator crashed or skipped them.
