# Gate 9 — Knowledge to Discovery

- Status: Active
- Version: v0.1
- Owner: APES Maintainers
- Last Updated: 2026-08-19
- Purpose: Determine whether captured learning is traceable and actionable enough to feed the next Discovery cycle.

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

- From stage: **Knowledge**
- To stage: **Discovery**

## Artifact Contract

- Schema type: `Workflow`
- ID prefix: `WORKFLOW-`
- Suggested artifact ID: `WORKFLOW-GATE-9-001`

## Entry Artifacts

- A completed [`retrospective-and-learning-record.md`](../templates/retrospective-and-learning-record.md) with outcome evidence, learning, actions, and Discovery feedback.

## Required Evidence

- Expected and actual outcomes are compared using dated measurements, feedback, incidents, or decisions.
- Lessons cite evidence and name plausible alternative explanations.
- Actions and decisions have owners, dates, and verification methods.
- At least one Discovery question or assumption is revised, confirmed, or explicitly retired.

## Gate Checklist

- [ ] Learning is based on recorded evidence rather than memory alone.
- [ ] Source and access date are present for material outcomes.
- [ ] What helped and hindered are separated from unsupported attribution.
- [ ] Unresolved uncertainty is carried forward visibly.
- [ ] Discovery feedback identifies evidence to collect and an owner.
- [ ] Sensitive personnel discussion is excluded from the reusable record.

## Failure and Compensating Evidence

If the gate does not pass, record `Failed` or `Deferred`, the missing outcome evidence or unactionable learning, an owner, and a review date. Holding another meeting without a traceable record does not satisfy the gate.

Compensating evidence may be a dated incident analysis, longitudinal outcome record, independent retrospective, or preserved decision log. It must connect the claimed lesson to observable evidence, include provenance and limitations, and yield a concrete Discovery question.

## Gate Record

| Decision | Decision Owner | Evidence References | Unmet Criteria | Compensating Evidence | Review Date |
| --- | --- | --- | --- | --- | --- |
| Pass / Failed / Deferred |  |  |  |  | YYYY-MM-DD |
