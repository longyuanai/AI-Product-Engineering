# checklists/

- Status: Active
- Version: v0.3
- Owner: APES Maintainers
- Last Updated: 2026-08-27
- Purpose: Hold quality and stage-gate checklists.

## Table of Contents

- [Purpose](#purpose)
- [Stage-Gate Contract](#stage-gate-contract)
- [Canonical Working Copy Rule](#canonical-working-copy-rule)
- [Checklists](#checklists)
- [Status](#status)

## Purpose

Checklists make stage gates and quality baselines concrete. They are the simplest artifact in APES and the easiest to misuse. A checklist is not a substitute for evidence — it is a tool for asking "Did we do the things that produce evidence?"

## Stage-Gate Contract

The nine lifecycle gates form a loop from Idea through Knowledge and back to Discovery. Each gate identifies its entry artifact, required evidence, failure record, and acceptable compensating evidence. A gate promise, unchecked box, or planned future activity is not evidence.

Schema v0.3.0 adds the first-class `Checklist` type with the `CHECKLIST-` ID prefix; [`RFC-0001`](../governance/rfc/RFC-0001-template-checklist-artifact-types.md) carries the standard-level proposal, and OQ-11 is resolved for this review candidate. Proposed [`ADR-0005`](../governance/adr/ADR-0005-fixture-only-artifact-metadata-boundary.md) limits that contract to parsed fixture objects, so P0-1 does not rewrite canonical checklist Markdown or its existing bullet-style metadata. Both proposals await `longyuan`'s decision.

## Canonical Working Copy Rule

Treat lifecycle and release-readiness checklists as read-only APES references. Copy the selected checklist to the adopting project's `GATE_RECORD_PATH`, record evidence and criterion state only in that working copy, and retain the APES version and canonical source path as provenance.

An agent may prepare evidence, unmet criteria, compensating evidence, owners, and review dates. Only the named human `GATE_DECISION_OWNER` records the final `Pass`, `Failed`, or `Deferred` result. Never mark or decide a gate in the canonical APES file.

## Checklists

- [`f2-independent-review.md`](f2-independent-review.md) — Initial F2 review, thirteen recorded findings, remediation and implementer follow-up snapshots, and blank independent re-review gate.
- [`gate-1-idea-to-discovery.md`](gate-1-idea-to-discovery.md) — Idea to Discovery.
- [`gate-2-discovery-to-research.md`](gate-2-discovery-to-research.md) — Discovery to Research.
- [`gate-3-research-to-validation.md`](gate-3-research-to-validation.md) — Research to Validation.
- [`gate-4-validation-to-product.md`](gate-4-validation-to-product.md) — Validation to Product.
- [`gate-5-product-to-business.md`](gate-5-product-to-business.md) — Product to Business.
- [`gate-6-business-to-engineering.md`](gate-6-business-to-engineering.md) — Business to Engineering.
- [`gate-7-engineering-to-growth.md`](gate-7-engineering-to-growth.md) — Engineering to Growth.
- [`gate-8-growth-to-knowledge.md`](gate-8-growth-to-knowledge.md) — Growth to Knowledge.
- [`gate-9-knowledge-to-discovery.md`](gate-9-knowledge-to-discovery.md) — Knowledge to Discovery.
- [`release-readiness.md`](release-readiness.md) — Reusable alpha identity, boundary, integrity, and human release-decision checklist.

## Status

Active. Nine lifecycle gate checklists and one reusable release-readiness checklist are available. The separate F2 review requested changes; its remediation and implementer follow-up are ready for re-review, and completion still requires a new eligible reviewer decision.
