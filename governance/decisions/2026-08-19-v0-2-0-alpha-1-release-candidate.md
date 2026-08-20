# v0.2.0-alpha.1 Release Candidate Decision

- Status: Pending Maintainer Decision
- Version: v0.1
- Owner: longyuan
- Last Updated: 2026-08-19
- Purpose: Record the bounded APES Project Layer alpha candidate and the human release decision.

## Candidate

- Candidate identifier: `v0.2.0-alpha.1`
- Layer: provisional APES Project Layer snapshot
- License: Apache License 2.0 (`Apache-2.0`), governed by [`ADR-0004`](../adr/ADR-0004-apache-2-0-repository-license.md)
- Human decision owner: `longyuan`

## Release Promise

> `v0.2.0-alpha.1` provides documented and repository-contract-tested mappings for all nine APES lifecycle stages from canonical template/checklist inputs to project-owned artifact/gate-record paths. Internal maintainer dogfood has exercised only the Idea path; the other eight paths and unaffiliated first-time-user usability remain unverified. A named human alone records the final gate decision.

## Candidate Boundary

This candidate includes the nine lifecycle templates and exit-gate checklists, one-stage Getting Started path, tool-neutral command, two tool adaptations, copy-safe canonical-file rules, internal Idea-stage dogfood, a canonical release-readiness checklist and project-owned working record, repository contract tests, and Apache-2.0 licensing.

It is not final v0.2, a Foundation or Research OS version assignment, F5, a deterministic Release Layer bundle, a mature or externally validated methodology, an industry standard, adoption evidence, or evidence that F2 has been approved. Standard module bodies remain placeholders; no external real-project case exists.

## Preserved Authority

- Sprint 2: `In Review`
- Research Gate: `RESEARCH AGAIN`
- F2: `In Review / Request changes`
- F3: unstarted
- OQ-11: unresolved; templates and checklists retain `Workflow` / `WORKFLOW-`

Historical Sprint 2.4 `READY FOR REVIEW` text remains historical evidence and does not override this current release authority.

## Release Eligibility

`Release` is eligible only after `longyuan` records the internal dogfood Gate 1 result as `Pass` in the project-owned Gate 1 working record. A Gate 1 result of `Pending`, `Failed`, or `Deferred` makes `Release` ineligible. This prerequisite does not select `Hold` automatically and does not allow an agent to record either candidate result.

## Verification

Automated and manual verification evidence is recorded in [`../../tasks/release-v0-2-0-alpha-1-preparation.md`](../../tasks/release-v0-2-0-alpha-1-preparation.md) and the project-owned [`../../examples/v0.2.0-alpha.1-maintainer-release-readiness.md`](../../examples/v0.2.0-alpha.1-maintainer-release-readiness.md). Internal dogfood evidence is bounded to repository-local acceptance and requires a separate human Gate 1 decision.

## Decision

| Decision | Decision Owner | Gate 1 Result | Evidence | Date |
| --- | --- | --- | --- | --- |
| Pending: Release / Hold | longyuan | Deferred | Preparation, dogfood, and project-owned readiness records | YYYY-MM-DD |

This decision record does not authorize a commit, tag, push, GitHub Release, hosted publication, release bundle, checksum manifest, or F5 artifact. Those actions require separate explicit authorization after `Release` is recorded.
