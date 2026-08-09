# Implementation F2 — Read-Only Validator

- Status: In Review
- Version: v0.2
- Owner: APES Maintainers
- Last Updated: 2026-08-10
- Purpose: Implement and validate the first deterministic runtime consumer of APES contracts in a separate tooling repository.

## Table of Contents

- [Goal](#goal)
- [Approval and Preconditions](#approval-and-preconditions)
- [Repositories](#repositories)
- [Scope](#scope)
- [Out of Scope](#out-of-scope)
- [Deliverables](#deliverables)
- [Acceptance Criteria](#acceptance-criteria)
- [Verification Record](#verification-record)
- [Observed Failures and Corrections](#observed-failures-and-corrections)
- [Remaining Gate](#remaining-gate)
- [Rollback](#rollback)
- [Status](#status)

## Goal

Deliver the F2 `check`, `graph`, and `explain` commands as deterministic, offline, read-only consumers of APES schemas and Markdown. Prove behavior with unit, property, CLI, security, packaging, dependency, and real-repository tests.

## Approval and Preconditions

- Maintainer direction: "继续执行项目技术方案" on 2026-08-09.
- ADR-0002 is `Accepted`.
- Foundation 0.3 / F1 is completed with one real APES compatibility set and intentionally invalid fixtures.
- [`../docs/repository-evolution-plan.md`](../docs/repository-evolution-plan.md) identifies F2 as the next phase.
- [`../governance/adr/ADR-0003-f2-read-only-validator-runtime.md`](../governance/adr/ADR-0003-f2-read-only-validator-runtime.md) accepts the runtime and repository boundary.

## Repositories

- Canonical contracts and governance: `AI-Product-Engineering`.
- Runtime implementation: sibling Git repository `E:\001项目\001Github\APES-Validator`.

The runtime repository contains its own `AGENTS.md`, source tree, tests, `pyproject.toml`, `uv.lock`, and Git history. It is not nested in the APES standard repository.

## Scope

- Python 3.12+ package with Typer, PyYAML, and JSON Schema 2020-12 validation.
- `check` command with text and JSON diagnostics.
- `graph` command with text, JSON, and DOT output.
- `explain` command with text and JSON diagnostic documentation.
- Strict repository-root containment, symbolic-path handling, safe YAML parsing, deterministic sorting, and no target writes.
- Schema, valid/invalid fixture, ID, reference, dependency-direction, cycle, local-link, and anchor checks.
- Unit, property, CLI, security-boundary, determinism, and read-only tests.
- uv locking, Hatchling packaging, Ruff, strict mypy, coverage threshold, dependency audit, and real APES integration.

## Out of Scope

- F3 workflow evaluator or gate automation.
- Write, repair, migration, formatting, or generated-file commands.
- Model SDK, prompt routing, agent framework, telemetry, network runtime, database, hosted API, website, MCP server, IDE extension, or plugin execution.
- Bulk conversion of APES Markdown to YAML front matter.
- Release publication, package-index upload, remote repository creation, or deployment.
- Sprint 4 Gap Analysis, Research Gate changes, new research, or Source Register changes.

## Deliverables

- Independent `APES-Validator` Git repository.
- `src/apes_validator/` implementation and console entry point.
- `tests/` unit, property, CLI, security, deterministic, and read-only coverage.
- Locked `pyproject.toml` / `uv.lock` environment.
- Wheel and source-distribution build proof.
- ADR-0003 and this task record.
- Initial review evidence, remediation evidence, and the independent checklist: [`../governance/decisions/2026-08-09-f2-review-evidence.md`](../governance/decisions/2026-08-09-f2-review-evidence.md), [`../governance/decisions/2026-08-09-f2-remediation-evidence.md`](../governance/decisions/2026-08-09-f2-remediation-evidence.md), and [`../checklists/f2-independent-review.md`](../checklists/f2-independent-review.md).
- Updated APES indexes, plan status, CHANGELOG, and project handoff memory.

## Acceptance Criteria

- [x] `check`, `graph`, `explain`, and `--version` execute successfully.
- [x] JSON diagnostics are deterministic and carry stable codes, severity, location, and context.
- [x] Target paths are root-contained; symbolic paths are skipped; repository content is never executed.
- [x] All valid F1 fixtures are accepted and all invalid F1 fixtures are rejected.
- [x] ID uniqueness, reference existence, dependency direction, dependency cycles, local links, and anchors are checked.
- [x] Repeated validation returns identical results and leaves target hashes unchanged.
- [x] Test coverage exceeds 90%.
- [x] Ruff and strict mypy pass.
- [x] The lock file is consistent and wheel/sdist packaging succeeds.
- [x] Dependency audit reports no known vulnerabilities.
- [x] A real APES repository check passes without writes.
- [ ] Independent reviewer signs off on schema and security boundaries.

## Verification Record

Executed in `E:\001项目\001Github\APES-Validator` on 2026-08-09:

- `uv sync --all-groups` — passed using CPython 3.13.14; 43 packages resolved after the security correction.
- `uv run ruff check .` — passed with no findings.
- `uv run mypy src tests` — remediation run passed with no issues in 13 source and test files.
- `uv run pytest --basetemp .pytest-tmp --cov=apes_validator --cov-report=term-missing --cov-fail-under=90` — remediation run passed 71/71 tests; total branch coverage 91.74%.
- `uv lock --check` — passed.
- `uv build` — produced `apes_validator-0.1.0.tar.gz` and `apes_validator-0.1.0-py3-none-any.whl`.
- `uv run --with bandit bandit -r src -ll -ii` — remediation run passed; 1300 lines scanned, no issue, no `nosec` exclusion.
- `uv run --with pip-audit pip-audit` — final run reported no known vulnerabilities; the local unpublished package was correctly skipped because it is not on PyPI.
- `uv run apes-validator check ..\AI-Product-Engineering --format text` — final remediation run passed over 88 Markdown files and 8 F1 fixtures.
- `uv run apes-validator graph ..\AI-Product-Engineering --format json` — passed with deterministic JSON output; current canonical front matter graph has 0 nodes and 0 edges because existing APES Markdown remains on legacy headers.
- `uv run apes-validator explain APES900 --format json` and `uv run apes-validator --version` — passed.
- SHA-256 inventory comparison around the final real APES check — all 103 non-Git files matched and `target_unchanged=True`.
- `git commit -m "feat: implement F2 read-only validator"` — created clean initial implementation commit `b085162` in `APES-Validator`; no remote push was performed.
- `git commit -m "security: harden untrusted repository inputs"` — created review commit `35d4ccf` with resource limits, external `$ref` rejection, fixture path containment, iterative deep-graph handling, and adversarial tests.
- `git commit -m "fix: remediate independent F2 audit findings"` — created clean remediation commit `73bbe6e`; no remote push was performed.
- `git commit -m "security: bound schema and path complexity"` — created clean implementer self-review follow-up commit `9d58a9f`; no remote push was performed.
- Follow-up `uv run pytest --basetemp .pytest-tmp --cov=apes_validator --cov-report=term-missing --cov-fail-under=90` — passed 87/87 tests at 91.20% branch coverage; the threshold remained 90%.
- Follow-up Ruff and strict mypy — passed; Bandit scanned 1578 lines with no issue or `nosec`; dependency audit, 43-package lock check, and build passed.
- Follow-up APES integration — a byte-equivalent 103-file mirror passed with 88 Markdown files, 8 fixtures, 0 artifacts, 0 edges, and identical before/after SHA-256 inventories. The mirror excluded only the agent-created `.f2-self-review-staging` test directory; independent review must use a clean APES checkout.
- Post-cleanup APES integration on 2026-08-10 — after explicit maintainer approval removed `.f2-self-review-staging`, the real repository root passed `check`, `graph`, and `explain` with 88 Markdown files, 8 fixtures, 0 artifacts, 0 edges, no diagnostic, and all 103 non-Git SHA-256 values unchanged.

## Observed Failures and Corrections

- The first pytest run used the system temporary directory and 18 tests were blocked by an existing Windows permission error. Rerunning with repository-contained `--basetemp .pytest-tmp` executed the suite normally.
- The next run passed 23/23 tests but reached only 84.48% coverage. Additional parser, schema-error, fixture-error, diagnostics, UTF-8, file-root, and symbolic-file tests raised the initial suite to 34 tests and 94.40% coverage; the threshold was not lowered. Review hardening expanded it to 40 tests at 93.98%, still above the same threshold.
- Initial mypy found missing `jsonschema` stubs and one Hypothesis annotation mismatch. A development-only `types-jsonschema` dependency and a typed explicit property-test alphabet resolved both; runtime dependencies were unchanged.
- Initial dependency audit found `PYSEC-2026-1845` in pytest 8.4.2. The development constraint was raised to pytest 9.0.3+, the lock resolved pytest 9.1.1, and the repeated audit found no known vulnerabilities.
- The independent Claude Opus 5 audit reproduced the automated gates but selected `Request changes`: one P0 external Schema retrieval path, four blocking P1 crash/contract defects, and eight P2/P3 correctness or documentation findings.
- Commit `73bbe6e` closes Schema retrieval with an explicit no-retrieval Registry and restricted Schema profile; converts malformed-link, deep-input, dangling-reference, and unexpected internal failures into bounded diagnostics; normalizes YAML date scalars; binds all thirteen type prefixes in Schema v0.2.0; and handles inline code, Windows device paths, bounded diagnostic output, and total case-sensitive ordering.
- The first remediation test run exposed a recursion in third-party `SchemaError.__str__`; exception summaries were made recursion-safe before the final 71-test pass. The threshold remained 90% and was not lowered.
- Implementer self-review then found three related hardening gaps: custom Schema complexity, path rejection after premature canonical resolution, and long-line scan amplification. Commit `9d58a9f` adds reviewed-pattern and combinator restrictions; Schema/instance node, depth, width, and branch limits; YAML alias rejection; a 64 KiB Markdown line limit; and pre-resolution rejection for absolute, UNC, malformed, control-character, and lexically escaping paths.
- The first follow-up coverage run passed all 85 tests but reached 89.46%, below the 90% gate. New boundary tests raised the final suite to 87 tests and 91.20%; the threshold was not lowered.

## Remaining Gate

The initial independent review requested changes. All thirteen findings have an implementation response frozen in [`../governance/decisions/2026-08-09-f2-remediation-evidence.md`](../governance/decisions/2026-08-09-f2-remediation-evidence.md), but the blank [re-review decision](../checklists/f2-independent-review.md#re-review-decision) must be completed by an eligible reviewer. F2 is not promoted before approval; F3 remains unstarted.

## Rollback

Remove or stop using `APES-Validator` and revert F2 status/index additions in this repository. Canonical APES artifacts remain unchanged because the validator has no write path.

## Status

**In Review — Remediation Ready.** The first independent review requested changes. Commit `73bbe6e` addresses all thirteen findings; follow-up commit `9d58a9f` adds implementer-discovered resource and path hardening. Schema v0.2.0 and all automated gates pass, but independent re-review is still pending before F2 closes.
