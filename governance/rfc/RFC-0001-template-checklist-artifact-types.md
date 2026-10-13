# RFC-0001 — First-Class Template and Checklist Artifact Types

- **Status:** Proposed
- **Date:** 2026-08-27
- **Owner:** APES Maintainers

## Table of Contents

- [Summary](#summary)
- [Motivation](#motivation)
- [Detailed Proposal](#detailed-proposal)
- [Impact on Existing Modules](#impact-on-existing-modules)
- [Backward Compatibility](#backward-compatibility)
- [Validation Plan](#validation-plan)
- [Open Questions](#open-questions)

## Summary

Add `Template` and `Checklist` to the artifact metadata type taxonomy with required `TEMPLATE-` and `CHECKLIST-` ID prefixes. Clarify that `last_updated` is an ISO date string and therefore must be quoted in YAML so parsers do not convert it to a native date object.

This RFC is the standard-level proposal required by [`AGENTS.md`](../../AGENTS.md). [`ADR-0005`](../adr/ADR-0005-fixture-only-artifact-metadata-boundary.md) separately defines the repository-level fixture-only boundary.

## Motivation

Schema v0.2.0 forced lifecycle templates and stage-gate checklists to use the generic `Workflow` type and `WORKFLOW-` prefix. That fallback erased a distinction already present in the APES document taxonomy and prevented consumers from querying or validating either kind independently.

The schema also declared `last_updated` as a string with `date` format. An unquoted YAML date-like scalar can be parsed as a native date rather than a string, causing a type failure that the contract did not explain.

## Detailed Proposal

1. Advance the artifact metadata prototype identifier from `0.2.0` to `0.3.0`.
2. Add `Template` to the `type` enum, bind it to IDs beginning with `TEMPLATE-`, and add `TEMPLATE` to the shared artifact ID pattern.
3. Add `Checklist` to the `type` enum, bind it to IDs beginning with `CHECKLIST-`, and add `CHECKLIST` to the shared artifact ID pattern.
4. Keep `last_updated` as a JSON Schema `string` with `date` format and add the normative producer rule that YAML date-like scalars must be quoted.
5. Add a negative fixture showing that unquoted `last_updated: 2026-08-27` parses to the wrong instance type.
6. Apply these rules only to parsed fixture objects while ADR-0005 is Proposed. Do not migrate repository Markdown metadata headers in this change.

## Impact on Existing Modules

No file under `standards/` changes. The proposal affects the shared artifact metadata schema, its fixtures, compatibility documentation, and the reader-facing descriptions that previously recorded OQ-11 as unresolved.

Existing canonical template and checklist Markdown files remain unchanged. Their bullet-style headers and embedded legacy compatibility examples are outside the fixture-only schema boundary until a separately approved migration exists.

## Backward Compatibility

The two enum and prefix additions are backward-compatible for existing valid schema instances: no existing type or prefix is removed. Consumers with a closed local allow-list must add the two new values before accepting v0.3.0 instances.

The `last_updated` rule clarifies the existing JSON Schema type instead of widening it. Quoted YAML dates and JSON string dates remain valid; unquoted YAML date objects are explicitly invalid.

## Validation Plan

- Validate the JSON Schema against the Draft 2020-12 meta-schema.
- Accept every fixture under `schemas/fixtures/artifact-metadata/valid/`.
- Reject every fixture under `schemas/fixtures/artifact-metadata/invalid/` for a documented constraint, including the unquoted YAML date case.
- Confirm the schema type enum and `oneOf` prefix bindings have identical membership.
- Run all fifteen read-only repository contract tests.
- Validate repository-local Markdown links and anchors and run `git diff --check`.

## Open Questions

- Will `longyuan` accept ADR-0005 and this RFC?
- If accepted, should a later task update the legacy Artifact Contract examples inside canonical template and checklist Markdown files, or retain them as pre-v0.3.0 compatibility examples?
- No question here authorizes a front matter migration, a validator change, or work in F2/F3.
