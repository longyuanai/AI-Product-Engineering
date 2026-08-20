# tests/

- Status: Active
- Version: v0.2
- Owner: APES Maintainers
- Last Updated: 2026-08-19
- Purpose: Hold repeatable, read-only tests for repository-level contracts and documentation invariants.

## Table of Contents

- [Purpose](#purpose)
- [Running the Tests](#running-the-tests)
- [Contracts](#contracts)
- [Scope](#scope)

## Purpose

The suite checks contracts that can be exercised without application code or repository mutation. It guards Schema fixtures, Markdown navigation, research statistics, lifecycle mappings, alpha identity, copy safety, human decision ownership, and non-claim boundaries.

## Running the Tests

From the repository root:

```text
uv run --with jsonschema python -B -m unittest discover -s tests -v
```

`jsonschema` is an ephemeral verification dependency; it is not added to the repository's production dependencies.

## Contracts

The 15 tests cover:

1. valid and intentionally invalid artifact-metadata fixtures;
2. repository-local Markdown links and anchors;
3. current Source Register statistics;
4. verification-log record shape and sequence;
5. Coverage Map dimensions and distribution;
6. direct-child Markdown indexing;
7. root navigation to repository tests;
8. lifecycle template metadata and vendor neutrality;
9. template type/prefix compatibility with Schema v0.2.0;
10. exact nine-stage template and gate correspondence;
11. `v0.2.0-alpha.1` identity, bounded structural promise, unverified-usability boundary, and Apache-2.0 boundary;
12. exact same-row Getting Started stage/template/transition/gate mappings with repository-local link targets, required source/work roots, and one-stage stop;
13. explicit run-stage inputs, section-scoped exact command mappings, resolved-root containment, dangling-link and canonical file-identity protection, stale-decision hard stop, and human ownership;
14. canonical template/checklist working-copy rules, Gate 1 `Pass` release prerequisite, and project-owned readiness provenance; and
15. current authority, Idea evidence-chain and criterion traceability, valid human decision states, the `Release`-requires-`Pass` invariant, and internal-dogfood non-claim boundaries.

## Scope

The suite is intentionally local and read-only. It does not publish artifacts, modify inspected files, make a gate or release decision, or change GitHub Actions. Application, CLI, MCP, website, build-pipeline, F2, and F3 behavior remain outside this repository's alpha-preparation scope.
