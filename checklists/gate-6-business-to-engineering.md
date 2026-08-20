# Gate 6 — Business to Engineering

- Status: Active
- Version: v0.1
- Owner: APES Maintainers
- Last Updated: 2026-08-19
- Purpose: Determine whether Business viability is sufficiently evidenced and bounded for Engineering investment.

## Table of Contents

- [Working Copy Rule](#working-copy-rule)
- [Transition](#transition)
- [Artifact Contract](#artifact-contract)
- [Entry Artifacts](#entry-artifacts)
- [Required Evidence](#required-evidence)
- [Gate Checklist](#gate-checklist)
- [Failure and Compensating Evidence](#failure-and-compensating-evidence)
- [Gate Record](#gate-record)

## Working Copy Rule

Copy this canonical checklist to `GATE_RECORD_PATH` before use. Record evidence and criterion state only in that project-owned working copy; never mark or decide the canonical APES file. An agent may prepare the record, but only the human named by `GATE_DECISION_OWNER` records `Pass`, `Failed`, or `Deferred`.

## Transition

- From stage: **Business**
- To stage: **Engineering**

## Artifact Contract

- Schema type: `Workflow`
- ID prefix: `WORKFLOW-`
- Suggested artifact ID: `WORKFLOW-GATE-6-001`

## Entry Artifacts

- A completed [`business-viability-brief.md`](../templates/business-viability-brief.md) with value, economic, delivery, and decision assumptions.

## Required Evidence

- The beneficiary, buyer or funding owner, and value exchange are identified.
- Material cost, demand, capacity, pricing, or adoption assumptions cite dated evidence or are labeled hypotheses.
- High-sensitivity assumptions and viability conditions are visible.
- The proceed, revise, stop, or collect-more-evidence decision has an owner.

## Gate Checklist

- [ ] Product scope and Business assumptions refer to the same bounded outcome.
- [ ] Material claims include source and access date.
- [ ] Estimates and projections are not presented as observed facts.
- [ ] Delivery and operational capabilities are identified.
- [ ] Financial, legal, procurement, or compliance dependencies have owners.
- [ ] Engineering investment is conditional on explicit viability assumptions.

## Failure and Compensating Evidence

If the gate does not pass, record `Failed` or `Deferred`, the unsupported viability assumption, its sensitivity, an owner, and a review date. A funding aspiration or forecast without inputs is not evidence.

Compensating evidence may be a binding pilot commitment, verified cost benchmark, operational capacity record, or observed willingness-to-pay signal. It must address the specific assumption, include provenance and access date, and document transferability limits.

## Gate Record

| Decision | Decision Owner | Evidence References | Unmet Criteria | Compensating Evidence | Review Date |
| --- | --- | --- | --- | --- | --- |
| Pass / Failed / Deferred |  |  |  |  | YYYY-MM-DD |
