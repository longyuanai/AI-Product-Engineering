# Stage Gates

- Status: Active
- Version: v0.2
- Owner: APES Maintainers
- Last Updated: 2026-08-19
- Purpose: Define what must be true to advance between lifecycle stages.

## Table of Contents

- [What is a Stage Gate](#what-is-a-stage-gate)
- [Gate Outputs](#gate-outputs)
- [Working Copy Rule](#working-copy-rule)
- [Gate Discipline](#gate-discipline)
- [Next Steps](#next-steps)

## What is a Stage Gate

A stage gate is the set of artifacts, evidence, and decisions required before moving from one stage to the next. Gates make it hard to skip validation and easy to audit later.

## Gate Outputs

The lifecycle is circular, so APES defines nine gates. Each checklist names the stage output required at entry and the evidence needed to advance.

| Gate | Transition | Required Stage Output | Checklist |
| --- | --- | --- | --- |
| 1 | Idea → Discovery | [`idea-brief.md`](../templates/idea-brief.md) | [`gate-1-idea-to-discovery.md`](../checklists/gate-1-idea-to-discovery.md) |
| 2 | Discovery → Research | [`discovery-interview-notes.md`](../templates/discovery-interview-notes.md) | [`gate-2-discovery-to-research.md`](../checklists/gate-2-discovery-to-research.md) |
| 3 | Research → Validation | [`research-note.md`](../templates/research-note.md) | [`gate-3-research-to-validation.md`](../checklists/gate-3-research-to-validation.md) |
| 4 | Validation → Product | [`validation-experiment-plan.md`](../templates/validation-experiment-plan.md) | [`gate-4-validation-to-product.md`](../checklists/gate-4-validation-to-product.md) |
| 5 | Product → Business | [`product-scope-spec.md`](../templates/product-scope-spec.md) | [`gate-5-product-to-business.md`](../checklists/gate-5-product-to-business.md) |
| 6 | Business → Engineering | [`business-viability-brief.md`](../templates/business-viability-brief.md) | [`gate-6-business-to-engineering.md`](../checklists/gate-6-business-to-engineering.md) |
| 7 | Engineering → Growth | [`engineering-change-record.md`](../templates/engineering-change-record.md) | [`gate-7-engineering-to-growth.md`](../checklists/gate-7-engineering-to-growth.md) |
| 8 | Growth → Knowledge | [`growth-experiment-record.md`](../templates/growth-experiment-record.md) | [`gate-8-growth-to-knowledge.md`](../checklists/gate-8-growth-to-knowledge.md) |
| 9 | Knowledge → Discovery | [`retrospective-and-learning-record.md`](../templates/retrospective-and-learning-record.md) | [`gate-9-knowledge-to-discovery.md`](../checklists/gate-9-knowledge-to-discovery.md) |

A gate result belongs in a project-owned working copy of the checklist's Gate Record. Repository-level or long-term decisions still belong in [`../governance/decisions/`](../governance/decisions/README.md) or the applicable ADR process.

## Working Copy Rule

Canonical APES checklists are read-only. Copy the selected checklist to `GATE_RECORD_PATH`, retain the APES version and canonical source path, and add project evidence only to that working copy. The agent may prepare criterion state and evidence gaps; the named human `GATE_DECISION_OWNER` alone records `Pass`, `Failed`, or `Deferred`.

Never mark the canonical checklist, silently waive a criterion, or let a gate decision start the next stage automatically.

## Gate Discipline

- No stage gate is waived silently. If a gate cannot be met, record why and what compensating evidence exists.
- "We will add it later" is not evidence. Cite what you observed now.
- Compensating evidence must address the same criterion, include provenance and access date, document its limitations, and identify an owner and expiry or review date.

## Next Steps

- Use the corresponding checklist under [`../checklists/`](../checklists/README.md) before advancing to the next lifecycle stage.
- See [`../standards/`](../standards/README.md) for the current module scaffold and its documented lifecycle asymmetry.
- See [`maturity-model.md`](maturity-model.md) for how gate adherence contributes to overall maturity.
