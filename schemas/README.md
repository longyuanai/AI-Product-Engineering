# schemas/

- Status: Active
- Version: v0.2
- Owner: APES Maintainers
- Last Updated: 2026-08-09
- Purpose: Hold canonical, language-neutral contract prototypes for APES artifacts.

## Table of Contents

- [Purpose](#purpose)
- [Current Contract](#current-contract)
- [Boundary](#boundary)

## Purpose

Schemas make structural metadata reviewable before any engine or CLI is implemented. Human-readable Markdown remains canonical; a future YAML 1.2 front matter block is parsed into an object and validated against the applicable JSON Schema.

## Current Contract

- [`artifact-metadata.schema.json`](artifact-metadata.schema.json) — F1 common artifact metadata object, corrected to v0.2.0 during F2 independent review remediation so all thirteen artifact types have matching ID prefixes.
- [`compatibility-mapping.md`](compatibility-mapping.md) — mapping from representative existing APES artifacts to the prototype.
- [`fixtures/artifact-metadata/`](fixtures/artifact-metadata/README.md) — four valid and four intentionally invalid parsed-metadata fixtures.

## Boundary

This directory contains contracts and fixtures, not executable tooling. Existing Markdown metadata is not bulk-migrated in F1. Validator CLI, graph, workflow, adapter, and release behavior remain later, separately approved phases.
