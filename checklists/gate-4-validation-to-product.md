# Gate 4 — Validation to Product

- Status: Active
- Version: v0.1
- Owner: APES Maintainers
- Last Updated: 2026-08-19
- Purpose: Determine whether Validation results justify defining Product scope and requirements.

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

- From stage: **Validation**
- To stage: **Product**

## Artifact Contract

- Schema type: `Workflow`
- ID prefix: `WORKFLOW-`
- Suggested artifact ID: `WORKFLOW-GATE-4-001`

## Entry Artifacts

- A completed [`validation-experiment-plan.md`](../templates/validation-experiment-plan.md) containing the predeclared decision rule, results, and decision.

## Required Evidence

- The hypothesis, population, measure, and pass, fail, and inconclusive thresholds were defined.
- Results cite dated raw observations or analysis outputs.
- The threshold comparison and decision are reproducible from the recorded evidence.
- Confounders, harms, and generalization limits are documented.

## Gate Checklist

- [ ] The experiment tested a falsifiable hypothesis.
- [ ] Decision thresholds were not rewritten to fit the result.
- [ ] Evidence entries include source and access date.
- [ ] Actual results and unexpected effects are recorded.
- [ ] Risk controls and stop conditions were followed.
- [ ] The Product decision is supported, bounded, and owned.

## Failure and Compensating Evidence

If the gate does not pass, record `Failed` or `Deferred`, the failed or inconclusive threshold, evidence gaps, an owner, and a review date. Intent to rerun the experiment is not current evidence.

Compensating evidence may be a replicated observational study, a credible quasi-experiment, or convergent results from independent methods. It must address the same hypothesis, expose confounders and access dates, and justify any narrower Product scope.

## Gate Record

| Decision | Decision Owner | Evidence References | Unmet Criteria | Compensating Evidence | Review Date |
| --- | --- | --- | --- | --- | --- |
| Pass / Failed / Deferred |  |  |  |  | YYYY-MM-DD |
