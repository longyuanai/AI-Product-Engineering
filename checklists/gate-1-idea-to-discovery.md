# Gate 1 — Idea to Discovery

- Status: Active
- Version: v0.1
- Owner: APES Maintainers
- Last Updated: 2026-08-19
- Purpose: Determine whether an Idea has enough traceable context and bounded uncertainty to enter Discovery.

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

- From stage: **Idea**
- To stage: **Discovery**

## Artifact Contract

- Schema type: `Workflow`
- ID prefix: `WORKFLOW-`
- Suggested artifact ID: `WORKFLOW-GATE-1-001`

## Entry Artifacts

- A completed [`idea-brief.md`](../templates/idea-brief.md) with an evidence table, explicit unknowns, and an Out of Scope section.

## Required Evidence

- At least one dated source, observation, or record supports the opportunity or problem signal.
- The affected people, systems, or context are identified without presenting assumptions as facts.
- The problem hypothesis is falsifiable and includes a disconfirming observation.
- Material safety, privacy, security, or compliance unknowns are visible.

## Gate Checklist

- [ ] The Idea brief identifies an evidence-backed signal worth investigating.
- [ ] Source and access date are present for every asserted fact.
- [ ] Hypotheses and assumptions are labeled.
- [ ] Intended outcomes are stated without committing to a solution.
- [ ] Discovery questions target the highest-impact unknowns.
- [ ] Out-of-scope boundaries are explicit.

## Failure and Compensating Evidence

If the gate does not pass, record `Failed` or `Deferred`, the unmet criterion, the evidence gap, an owner, and a review date in the Gate Record. A roadmap promise or "we will add it later" does not count.

Compensating evidence may be a dated behavioral dataset, service record, or independently collected observation when direct Discovery evidence is not yet available. It must address the same criterion, identify provenance and limitations, and remain clearly labeled as a proxy.

## Gate Record

| Decision | Decision Owner | Evidence References | Unmet Criteria | Compensating Evidence | Review Date |
| --- | --- | --- | --- | --- | --- |
| Pass / Failed / Deferred |  |  |  |  | YYYY-MM-DD |
