# Gate 8 — Growth to Knowledge

- Status: Active
- Version: v0.1
- Owner: APES Maintainers
- Last Updated: 2026-08-19
- Purpose: Determine whether Growth activity produced trustworthy results and learning for the Knowledge stage.

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

- From stage: **Growth**
- To stage: **Knowledge**

## Artifact Contract

- Schema type: `Workflow`
- ID prefix: `WORKFLOW-`
- Suggested artifact ID: `WORKFLOW-GATE-8-001`

## Entry Artifacts

- A completed [`growth-experiment-record.md`](../templates/growth-experiment-record.md) with baseline, thresholds, guardrails, actual results, and decision.

## Required Evidence

- The Growth hypothesis, primary metric, guardrail metric, and decision thresholds are recorded.
- Baselines and results cite dated observations or datasets.
- Segment differences, confounders, harms, and unexpected effects are visible.
- The adopt, iterate, stop, or collect-more-evidence decision follows from the results.

## Gate Checklist

- [ ] The experiment identifies intended user value, not only an organization metric.
- [ ] Metric definitions and measurement windows are stable.
- [ ] Evidence includes source and access date.
- [ ] Guardrail outcomes and audience safeguards are recorded.
- [ ] Results distinguish correlation, inference, and direct observation.
- [ ] Durable and short-term effects are not conflated.

## Failure and Compensating Evidence

If the gate does not pass, record `Failed` or `Deferred`, the missing baseline, unreliable metric, harmed guardrail, or unresolved confounder, plus owner and review date. A future reporting cycle is not current evidence.

Compensating evidence may be a longitudinal cohort analysis, independently verified operational data, or a convergent experiment. It must address the same metric and audience, include access dates, expose selection effects, and narrow any claim that exceeds the evidence.

## Gate Record

| Decision | Decision Owner | Evidence References | Unmet Criteria | Compensating Evidence | Review Date |
| --- | --- | --- | --- | --- | --- |
| Pass / Failed / Deferred |  |  |  |  | YYYY-MM-DD |
