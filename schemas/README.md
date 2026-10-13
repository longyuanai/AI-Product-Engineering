# schemas/

- Status: Active
- Version: v0.3
- Owner: APES Maintainers
- Last Updated: 2026-08-27
- Purpose: Hold canonical, language-neutral contract prototypes for APES artifacts.

## Table of Contents

- [Purpose](#purpose)
- [Current Contract](#current-contract)
- [Boundary](#boundary)

## Purpose

Schemas make structural metadata reviewable without changing the repository's canonical Markdown. The current contract is a Foundation 0.3 / F1 prototype for parsed fixture objects; it does not assert that repository Markdown already contains YAML front matter.

## Current Contract

- [`artifact-metadata.schema.json`](artifact-metadata.schema.json) — Schema v0.3.0 review candidate for the F1 common artifact metadata object, including first-class `Template` / `TEMPLATE-` and `Checklist` / `CHECKLIST-` pairs.
- [`compatibility-mapping.md`](compatibility-mapping.md) — mapping from representative existing APES artifacts to the prototype.
- [`fixtures/artifact-metadata/`](fixtures/artifact-metadata/README.md) — parsed-metadata fixtures, including an unquoted YAML date negative case.

## Boundary

This directory contains contracts and fixtures, not executable tooling. [`artifact-metadata.schema.json`](artifact-metadata.schema.json) currently constrains only parsed metadata objects represented under [`fixtures/`](fixtures/artifact-metadata/README.md). It does not constrain the bullet-style metadata headers used by repository Markdown files, and P0-1 performs no front matter migration.

[`ADR-0005`](../governance/adr/ADR-0005-fixture-only-artifact-metadata-boundary.md) records this repository boundary as `Proposed`. [`RFC-0001`](../governance/rfc/RFC-0001-template-checklist-artifact-types.md) separately proposes the standard-level taxonomy change; both await `longyuan`'s decision.
