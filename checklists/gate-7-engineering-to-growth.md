# Gate 7 — Engineering to Growth

- Status: Active
- Version: v0.1
- Owner: APES Maintainers
- Last Updated: 2026-08-19
- Purpose: Determine whether an Engineering change is verified, operable, and bounded for Growth activity.

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

- From stage: **Engineering**
- To stage: **Growth**

## Artifact Contract

- Schema type: `Workflow`
- ID prefix: `WORKFLOW-`
- Suggested artifact ID: `WORKFLOW-GATE-7-001`

## Entry Artifacts

- A completed [`engineering-change-record.md`](../templates/engineering-change-record.md) with impact analysis, actual verification results, and rollback steps.

## Required Evidence

- The change traces to approved requirements and decisions.
- Executed checks record the command or method, actual result, and status.
- Security, privacy, compatibility, accessibility, and operational impacts are assessed.
- Rollback triggers and post-rollback verification are defined.

## Gate Checklist

- [ ] Implementation deviations and affected components are recorded.
- [ ] Required tests, reviews, and security checks were actually executed.
- [ ] Failed or skipped checks are visible and owned.
- [ ] Operational signals and guardrails needed by Growth are available.
- [ ] Recovery prerequisites and rollback steps are verified proportionately to risk.
- [ ] Known limitations bound the eligible Growth audience.

## Failure and Compensating Evidence

If the gate does not pass, record `Failed` or `Deferred`, each failed or unexecuted check, risk, owner, and review date. A plan to test later is not evidence.

Compensating evidence may be an independent analysis, a constrained rollout with effective monitoring and rollback, or a verified equivalent check. It must address the same risk, cite dated results, define an expiry, and never silently waive a mandatory control.

## Gate Record

| Decision | Decision Owner | Evidence References | Unmet Criteria | Compensating Evidence | Review Date |
| --- | --- | --- | --- | --- | --- |
| Pass / Failed / Deferred |  |  |  |  | YYYY-MM-DD |
