# Gate 3 — Research to Validation

- Status: Active
- Version: v0.1
- Owner: APES Maintainers
- Last Updated: 2026-08-19
- Purpose: Determine whether Research supports a bounded, falsifiable Validation experiment.

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

- From stage: **Research**
- To stage: **Validation**

## Artifact Contract

- Schema type: `Workflow`
- ID prefix: `WORKFLOW-`
- Suggested artifact ID: `WORKFLOW-GATE-3-001`

## Entry Artifacts

- A completed [`research-note.md`](../templates/research-note.md) for each question that materially shapes the proposed Validation experiment.

## Required Evidence

- The Research question, scope, method, and stop condition are documented.
- Findings cite dated sources and keep source reliability separate from claim verification.
- Counter-evidence, inaccessible evidence, and generalization limits are visible.
- The proposed Validation hypothesis follows from the evidence rather than from an uncited preference.

## Gate Checklist

- [ ] Every material claim points to a source and access date.
- [ ] Primary and independent evidence were preferred where available.
- [ ] Contradictory findings were retained and assessed.
- [ ] Inferences are labeled separately from observations.
- [ ] The strongest remaining hypothesis is falsifiable.
- [ ] Validation can produce a decision-relevant result within stated constraints.

## Failure and Compensating Evidence

If the gate does not pass, record `Failed` or `Deferred`, the unsupported claim or unresolved contradiction, an evidence owner, and a review date. A planned search or uncited summary is not evidence.

Compensating evidence may be an independently reproduced result, an alternative primary source, or a documented expert assessment that directly addresses the missing claim. Record provenance, access date, method, conflicts of interest, and why it is sufficient for a bounded experiment.

## Gate Record

| Decision | Decision Owner | Evidence References | Unmet Criteria | Compensating Evidence | Review Date |
| --- | --- | --- | --- | --- | --- |
| Pass / Failed / Deferred |  |  |  |  | YYYY-MM-DD |
