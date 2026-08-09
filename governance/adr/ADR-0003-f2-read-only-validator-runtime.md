# ADR-0003 — F2 Read-Only Validator Runtime

- **Title:** Python runtime and separate repository boundary for the F2 APES Validator
- **Status:** Accepted
- **Date:** 2026-08-09
- **Accepted:** 2026-08-09

## Table of Contents

- [Context](#context)
- [Decision](#decision)
- [Consequences](#consequences)
- [Security Boundary](#security-boundary)
- [Alternatives Considered](#alternatives-considered)
- [Initial Validation Evidence](#initial-validation-evidence)
- [Security Review Continuation](#security-review-continuation)
- [Independent Review Remediation](#independent-review-remediation)
- [Rollback](#rollback)

## Context

ADR-0002 accepted a schema-first, file-native architecture and required executable tooling to remain a separately governed consumer of APES contracts. Foundation 0.3 / F1 then supplied a JSON Schema 2020-12 contract, four valid fixtures, four invalid fixtures, and representative APES compatibility cases.

The maintainer requested continuation of the project technical plan on 2026-08-09. The next gated phase in the Repository Evolution Plan is F2: a deterministic, read-only validator with `check`, `graph`, and `explain` commands, machine-readable diagnostics, tests, and a security review.

## Decision

1. F2 is implemented in the independent sibling Git repository `APES-Validator`, not inside AI-Product-Engineering.
2. The package and command are named `apes-validator`.
3. Python 3.12+ is the supported runtime. Initial verification used CPython 3.13.14.
4. Typer provides the CLI; PyYAML parses safe YAML; `jsonschema` validates Draft 2020-12 contracts; `referencing` supplies an explicit closed Registry; uv and Hatchling provide locking and packaging.
5. pytest, Hypothesis, Ruff, mypy, coverage, and dependency auditing form the implementation quality gate.
6. `check` validates schema metadata, contract fixtures, unique IDs, references, dependency direction, cycles, local links, anchors, and path containment.
7. `graph` derives text, JSON, or DOT nodes and edges from validated front matter. Derived output is disposable and never canonical.
8. `explain` exposes stable diagnostic definitions and remediation in text or JSON.
9. Error diagnostics produce exit code 1; invalid CLI input or unknown diagnostic codes produce exit code 2; unexpected validator implementation failures produce bounded `APES900` output and exit code 3; a clean result produces exit code 0.
10. Runtime operation is offline and read-only. No production model SDK, telemetry, database, hosted service, plugin execution, hook execution, or write command is included.

## Consequences

Positive:

- APES contracts now have a deterministic executable consumer without adding application code to the standard repository.
- Text, JSON, and DOT outputs support humans, CI, and later workflow phases.
- Stable diagnostic codes separate machine integration from prose wording.
- Tests prove deterministic repeat results and unchanged target-file hashes.
- The locked environment and package build make the implementation reproducible.

Costs and limits:

- Contract and validator versions must now be coordinated across repositories.
- Existing APES Markdown still uses legacy bullet metadata, so the current real-repository graph contains zero canonical front matter nodes; F1 fixtures are nevertheless validated.
- Local Markdown parsing is deliberately bounded and is not a full CommonMark parser.
- Independent reviewer sign-off remains required before F2 is treated as a release rather than a validated implementation.

## Security Boundary

- Every supplied path is resolved before access and must remain inside the selected repository root.
- Directory traversal through links is rejected; symbolic directories and symbolic Markdown files are not traversed.
- Repository content is data only. YAML uses safe parsing and no Markdown, YAML, JSON, hook, or shell content is executed.
- Runtime performs no network call and writes no target file. Its Schema Registry has no retrieval hook; external `$ref`, every `$dynamicRef`, nested `$schema`, nested `$id`, and non-APES root `$id` are rejected before validation.
- The real APES integration compares SHA-256 file inventories before and after validation.
- The dependency audit initially found `PYSEC-2026-1845` in pytest 8.4.2; the development baseline was raised to pytest 9.0.3+ and the repeated audit reported no known vulnerabilities.

## Alternatives Considered

### In-repository Python script

Rejected because it would collapse the contract/tool boundary accepted in ADR-0002 and make runtime dependencies part of the standards repository.

### Node.js / TypeScript validator

Deferred. The F1 use case is document, schema, path, and graph validation; the accepted reference plan selected Python as the smaller first evaluation surface. No evidence from this implementation requires a stack change.

### LLM-based validation

Rejected for machine-verifiable contracts. Schema validity, identifiers, links, dependency direction, and cycles must produce deterministic results without a model or network.

### Automatic repair mode

Deferred beyond F2. Write behavior requires dry-run diffs, backups, explicit target confirmation, and separate approval.

## Initial Validation Evidence

- 34 pytest tests passed on Windows with CPython 3.13.14 and pytest 9.1.1.
- Branch coverage reached 94.40%, above the 90% exit threshold.
- Ruff reported no findings.
- Strict mypy reported no issues across 13 source and test files.
- `uv lock --check` and `uv build` succeeded for both sdist and wheel.
- Dependency audit reported no known vulnerabilities after the pytest upgrade.
- Real APES `check`, `graph`, `explain`, and `--version` commands succeeded; the APES SHA-256 inventory was unchanged.

Detailed commands and results are recorded in [`../../tasks/implementation-f2-read-only-validator.md`](../../tasks/implementation-f2-read-only-validator.md).

## Security Review Continuation

The 2026-08-09 review continuation hardened untrusted-input handling in commit `35d4ccf`:

- remote and file-like non-fragment JSON Schema `$ref` values are rejected before validation;
- Markdown, front matter, schemas, and fixtures have explicit size limits;
- symbolic schema and fixture paths are rejected in addition to existing Markdown/directory controls;
- dependency-cycle traversal is iterative and passed a 2000-node adversarial case;
- dangerous Python-object YAML tags are explicitly tested and rejected by safe loading.

The expanded suite passed 40/40 tests at 93.98% branch coverage. Ruff, strict mypy, Bandit, dependency audit, lock verification, package build, and the real APES no-write check also passed. The frozen evidence and residual limits are in [`../decisions/2026-08-09-f2-review-evidence.md`](../decisions/2026-08-09-f2-review-evidence.md); the independent reviewer uses [`../../checklists/f2-independent-review.md`](../../checklists/f2-independent-review.md).

## Independent Review Remediation

The independent review of `35d4ccf` reproduced the automated evidence but selected `Request changes`, recording one P0, four P1, three P2, and five P3 findings. Commit `73bbe6e` responds to all thirteen:

- the JSON Schema registry is explicitly closed, and only resolvable local JSON Pointer `$ref` values are accepted;
- malformed Markdown targets, deep JSON/YAML, dangling references, and internal CLI failures have bounded diagnostic boundaries;
- unquoted YAML date scalars normalize to the JSON Schema date string contract;
- Schema v0.2.0 binds all thirteen artifact types to their canonical prefixes;
- inline code, Windows drive/device targets, diagnostic size, and case-sensitive ordering have regression coverage.

The remediation suite passed 71/71 tests at 91.74% branch coverage. Ruff, strict mypy, Bandit, dependency audit, lock verification, build, real APES validation, and the 103-file no-write inventory passed. The exact snapshot, finding-by-finding response, hashes, and revised residual limits are frozen in [`../decisions/2026-08-09-f2-remediation-evidence.md`](../decisions/2026-08-09-f2-remediation-evidence.md). This implementation response does not replace independent re-review.

Implementer self-review follow-up commit `9d58a9f` further restricts untrusted Schema patterns and combinators, bounds Schema and instance structure, rejects YAML aliases, caps Markdown line length, and rejects absolute, UNC, malformed, control-character, and lexically escaping paths before canonical resolution. Its 87-test suite passed at 91.20% branch coverage together with the unchanged quality, dependency, lock, build, and no-write gates. This remains implementation evidence and does not replace independent re-review.

## Rollback

Stop using or remove the independent `APES-Validator` repository and revert this ADR's F2 status references. Canonical APES Markdown, schemas, fixtures, research, and decisions remain readable and unchanged. No data migration or runtime state must be reversed.
