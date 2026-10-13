# tasks/

- Status: Active
- Version: v0.1
- Owner: APES Maintainers
- Last Updated: 2026-08-19
- Purpose: Hold sprint and task definitions for APES development.

## Table of Contents

- [Purpose](#purpose)
- [Naming Convention](#naming-convention)
- [Status](#status)

## Purpose

This directory keeps a dated record of sprints — what was planned, what was in scope, what was deliberately out of scope, and how completion was verified.

## Naming Convention

- `sprint-NN-short-name.md` for active or completed sprints.
- `sprint-NN-N-short-name.md` for review, correction, or audit work attached to a sprint.
- `foundation-N-N-short-name.md` for Foundation architecture work.
- `implementation-fN-short-name.md` for staged runtime implementation work.
- A sprint file may reference task files by short id, but tasks live inline within the sprint file unless they grow large.

## Status

Current authority: Sprint 2 remains `In Review`, and the Research Gate remains `RESEARCH AGAIN`. The Sprint 2.4 `READY FOR REVIEW` wording below is retained as that task's historical recommendation and is not current release authority.

Ready for maintainer decision:

- [`release-v0-2-0-alpha-1-preparation.md`](release-v0-2-0-alpha-1-preparation.md) — Apache-2.0, contract-tested mappings for nine bounded one-stage paths, Idea-only internal dogfood, and automated verification prepared; other-stage and unaffiliated first-time-user usability remain unverified, Gate 1 and `Release / Hold` remain with `longyuan`, and Git/publication actions remain unauthorized.

Completed:

- [`sprint-00-repository-foundation.md`](sprint-00-repository-foundation.md) — Repository Foundation.
- [`sprint-01-ecosystem-research-plan.md`](sprint-01-ecosystem-research-plan.md) — Ecosystem Research Plan.
- [`sprint-01-1-research-plan-review-fix.md`](sprint-01-1-research-plan-review-fix.md) — Research Plan Review Fix.
- [`sprint-02-1-evidence-correction.md`](sprint-02-1-evidence-correction.md) — Evidence Correction.
- [`sprint-02-3-external-verification-reconciliation.md`](sprint-02-3-external-verification-reconciliation.md) — External Verification Reconciliation.
- [`sprint-02-4-targeted-reverification.md`](sprint-02-4-targeted-reverification.md) — Targeted Primary-Source Re-verification; 12 direct source upgrades and a historical `READY FOR REVIEW` recommendation; Sprint 2 remains `In Review`.
- [`sprint-03-coverage-map.md`](sprint-03-coverage-map.md) — Coverage Map.
- [`sprint-03-1-coverage-audit.md`](sprint-03-1-coverage-audit.md) — Coverage Audit.
- [`sprint-04-ai-coding-tool-guidance.md`](sprint-04-ai-coding-tool-guidance.md) — Tool-agnostic AI coding tool guidance and adaptation examples.
- [`sprint-05-lifecycle-templates-and-gates.md`](sprint-05-lifecycle-templates-and-gates.md) — Nine lifecycle document templates, nine circular stage-gate checklists, and repository contract coverage.
- [`foundation-0-1-repository-evolution.md`](foundation-0-1-repository-evolution.md) — Repository Evolution Plan.
- [`foundation-0-1-1-repository-evolution-upgrade.md`](foundation-0-1-1-repository-evolution-upgrade.md) — Repository Evolution Plan Upgrade.
- [`foundation-0-2-open-source-reference-architecture.md`](foundation-0-2-open-source-reference-architecture.md) — Open-source comparison and documentation-only reference architecture; the Sprint ended with ADR-0002 Proposed.
- [`foundation-0-3-contract-prototype.md`](foundation-0-3-contract-prototype.md) — F1 JSON Schema contract, valid/invalid fixtures, and compatibility mapping; ADR-0002 accepted.

In review:

- [`sprint-02-ecosystem-inventory.md`](sprint-02-ecosystem-inventory.md) — Ecosystem Inventory and Initial Reverse Research.
- [`sprint-02-2-primary-source-verification.md`](sprint-02-2-primary-source-verification.md) — Primary Source Verification attempt; Research Gate remains `RESEARCH AGAIN`.
- [`implementation-f2-read-only-validator.md`](implementation-f2-read-only-validator.md) — Independent read-only validator; all thirteen initial findings remediated, implementer resource/path follow-up complete, independent re-review pending.

Maintenance:

- [`maintenance-2026-08-17-repository-contract-tests.md`](maintenance-2026-08-17-repository-contract-tests.md) — Repository contract tests and consistency fixes.
- [`maintenance-2026-08-04-repository-hygiene.md`](maintenance-2026-08-04-repository-hygiene.md) — Repository index, link, and local-configuration hygiene.
- [`maintenance-2026-08-07-project-reconciliation.md`](maintenance-2026-08-07-project-reconciliation.md) — Chat-to-repository reconciliation, project handoff, and Foundation 0.2 index sync.
- [`maintenance-2026-08-27-p0-1-schema-contract-alignment.md`](maintenance-2026-08-27-p0-1-schema-contract-alignment.md) — Fixture-only F1 schema boundary, OQ-11 taxonomy proposal, and quoted YAML date contract.
