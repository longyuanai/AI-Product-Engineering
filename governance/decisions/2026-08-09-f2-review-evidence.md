# F2 Independent Review Evidence — 2026-08-09

- Status: Reviewed — Changes Requested
- Version: v0.1
- Owner: APES Maintainers
- Last Updated: 2026-08-09
- Purpose: Freeze the automated evidence, reviewed snapshot, threat cases, and residual limits presented to the independent F2 reviewer.

## Table of Contents

- [Decision Scope](#decision-scope)
- [Frozen Snapshot](#frozen-snapshot)
- [Automated Evidence](#automated-evidence)
- [Adversarial Evidence](#adversarial-evidence)
- [Residual Limits](#residual-limits)
- [Independent Review Boundary](#independent-review-boundary)
- [Outcome](#outcome)

## Decision Scope

This note supports one reversible sprint decision: whether F2 Read-Only Validator may move from `In Review` to `Completed`. It does not change ADR-0002, ADR-0003, the F1 schema, the Research Gate, or later implementation authorization.

## Frozen Snapshot

| Artifact | Identifier |
| --- | --- |
| Runtime repository | `E:\001项目\001Github\APES-Validator` |
| Review commit | `35d4ccf7acaa5881038f907d7a8b7eb59d47fd7b` |
| Initial implementation commit | `b085162` |
| APES artifact schema SHA-256 | `02832F4C8A91A1C3F3764FB29FFAE3DF434A47F9CC70DF3B0C20660FB4C08160` |
| `uv.lock` SHA-256 | `6195EF0ADF5C46FFE3CD588E401413C1A9BA24BF5F3C6DD19D0A47A9E1900A0E` |
| Built wheel SHA-256 | `185724D3B9218B9B0431A9FB85B55C45E75156CC1A39FE9074B624D4A577ED57` |

## Automated Evidence

| Gate | Final result |
| --- | --- |
| pytest | 40/40 passed |
| Branch coverage | 93.98%; threshold 90% |
| Ruff | No findings |
| Strict mypy | No issues in 13 source and test files |
| Bandit | No issues; 1060 lines scanned; no `nosec` exclusions |
| Dependency audit | No known third-party vulnerabilities; unpublished local package skipped as expected |
| uv lock | Consistent; 43 packages |
| Package build | sdist and wheel succeeded |
| Real APES check | Passed: 85 Markdown files, 8 fixtures, 0 canonical front matter nodes, 0 edges |
| Target integrity | SHA-256 inventory unchanged before and after validation |

The earlier pytest temporary-directory failure, coverage shortfall, typing findings, and vulnerable pytest 8.4.2 result are preserved in the [F2 task record](../../tasks/implementation-f2-read-only-validator.md), together with their corrections.

## Adversarial Evidence

The security-hardening review added explicit tests and implementation controls for:

- Python-object YAML tags rejected by `safe_load`;
- remote and file-like non-fragment JSON Schema `$ref` values rejected before validation;
- 8 MiB Markdown, 64 KiB front matter, 1 MiB schema, and 1 MiB fixture limits;
- symbolic schema, fixture directory, fixture file, Markdown file, and directory boundaries;
- local-link traversal outside the repository root;
- malformed UTF-8, malformed YAML, malformed JSON, and invalid schemas;
- deterministic duplicate-ID, missing-reference, dependency-direction, and cycle diagnostics;
- iterative processing of a 2000-node dependency chain without recursion failure;
- repeat validation and file-hash invariance.

These changes are commit `35d4ccf` (`security: harden untrusted repository inputs`).

## Residual Limits

- Markdown link extraction is intentionally bounded and is not a full CommonMark parser.
- Existing APES documents have legacy bullet headers; therefore the real graph is empty until a separately reviewed metadata migration occurs.
- Runtime/package compatibility was exercised on Windows CPython 3.13.14; the declared Python 3.12 minimum still needs a future CI matrix before release publication.
- The local package is unpublished and was skipped by `pip-audit`; all third-party locked packages were audited.
- A same-user local attacker racing file replacement between path resolution and read is outside the current single-process CLI threat model.
- Automated checks do not establish reviewer independence or authorize F3.

## Independent Review Boundary

The implementation author prepared this evidence but does not sign the gate. The reviewer must use [`../../checklists/f2-independent-review.md`](../../checklists/f2-independent-review.md), confirm the frozen snapshot, inspect the relevant code and schema, reproduce material checks, and record one outcome.

## Outcome

- Reviewer: Independent Schema & Security Reviewer (Claude Opus 5 audit session, commissioned by APES Maintainers); not the author of `b085162` or `35d4ccf`
- Decision: Request changes
- Date: 2026-08-09
- Findings reference: [`../../checklists/f2-independent-review.md#independent-findings`](../../checklists/f2-independent-review.md#independent-findings) — 13 findings; blocking: F2-P0-1 (untrusted schema reaches the network and reads outside the repository root via `$dynamicRef` and subschema `$schema`), F2-P1-1, F2-P1-2, F2-P1-3 (unhandled crashes on untrusted input), F2-P1-4 (canonical unquoted YAML date rejected by the contract). The frozen snapshot, all automated gates, and the read-only guarantee reproduced exactly.

This initial review requested changes. The implementation response and new frozen snapshot are recorded in [`2026-08-09-f2-remediation-evidence.md`](2026-08-09-f2-remediation-evidence.md). F2 remains `In Review`, and F3 remains unstarted, pending independent re-review.
