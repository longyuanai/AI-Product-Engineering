# Gate 5 — Product to Business

- Status: Active
- Version: v0.1
- Owner: APES Maintainers
- Last Updated: 2026-08-19
- Purpose: Determine whether Product scope is clear enough for a Business viability decision.

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

- From stage: **Product**
- To stage: **Business**

## Artifact Contract

- Schema type: `Workflow`
- ID prefix: `WORKFLOW-`
- Suggested artifact ID: `WORKFLOW-GATE-5-001`

## Entry Artifacts

- A completed [`product-scope-spec.md`](../templates/product-scope-spec.md) with users, scenarios, requirements, acceptance evidence, constraints, and exclusions.

## Required Evidence

- The scoped problem and intended outcome trace to Discovery and Validation evidence.
- User scenarios and requirements cite dated sources.
- Acceptance criteria are observable and tied to evidence, not implementation preference.
- Security, privacy, accessibility, operational, and dependency constraints are visible.

## Gate Checklist

- [ ] In-scope capabilities and explicit non-goals are unambiguous.
- [ ] Requirements are traceable to evidence and intended outcomes.
- [ ] Acceptance evidence is defined for each mandatory requirement.
- [ ] Unsupported user or market claims remain hypotheses.
- [ ] Dependencies and constraints have owners.
- [ ] Business analysis can evaluate a stable, bounded scope.

## Failure and Compensating Evidence

If the gate does not pass, record `Failed` or `Deferred`, the ambiguous scope or unsupported requirement, an owner, and a review date. A future design or implementation plan does not fill a Product evidence gap.

Compensating evidence may be a tested prototype, task observation, or comparable operational result that directly supports a requirement. It must include provenance, access date, context limits, and a rationale for applying it to the scoped users.

## Gate Record

| Decision | Decision Owner | Evidence References | Unmet Criteria | Compensating Evidence | Review Date |
| --- | --- | --- | --- | --- | --- |
| Pass / Failed / Deferred |  |  |  |  | YYYY-MM-DD |
