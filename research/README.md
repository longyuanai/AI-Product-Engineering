# research/

- Status: Draft
- Version: v0.4
- Owner: APES Maintainers
- Last Updated: 2026-08-19
- Purpose: Hold research notes used to inform the APES standard.

## Table of Contents

- [Purpose](#purpose)
- [Subdirectories](#subdirectories)
- [Citation Rules](#citation-rules)
- [Status](#status)
- [Research Plan](#research-plan)
- [Sprint 2 Deliverables](#sprint-2-deliverables)
- [Sprint 2.2 Deliverables](#sprint-22-deliverables)
- [Sprint 2.3 Deliverables](#sprint-23-deliverables)
- [Sprint 2.4 Deliverables](#sprint-24-deliverables)
- [Sprint 3 Deliverables](#sprint-3-deliverables)
- [Sprint 3.1 Deliverables](#sprint-31-deliverables)
- [Foundation 0.2 Reference Research](#foundation-02-reference-research)

## Purpose

Research notes accumulate evidence about the AI product-engineering ecosystem and inform which practices APES should codify. Research here is *about* the environment in which APES will be applied, not about APES itself.

## Subdirectories

- [`ecosystem/`](ecosystem/README.md) — Note on the broader AI tooling ecosystem as it affects APES.
- [`competitors/`](competitors/README.md) — Note on competing standards, frameworks, and tools.
- [`papers/`](papers/README.md) — Academic and industry literature relevant to APES.
- [`notes/`](notes/README.md) — Free-form research notes and observations.
- [`coverage/`](coverage/coverage-map.md) — Phase B coverage mapping and its audited lifecycle and artifact maps.

## Citation Rules

Every note must include:

- Source (URL or citation)
- Access date
- The specific claim drawn from the source
- A quote, table, or figure pointer where possible

## Status

Research execution has begun and remains in Draft / In Review status. Phase A inventory and Initial Reverse Research, source verification work, Phase B coverage mapping, and the Foundation 0.2 reference comparison are present. Sprint 2 remains `In Review`. Sprint 2.4 recorded a `READY FOR REVIEW` recommendation based on 22 Verified sources and 13 directly verified repositories/projects under a conservative counting rule; current release authority remains `RESEARCH AGAIN`. No research artifact should be treated as an accepted APES conclusion until maintainer review is complete.

## Research Plan

A research plan for the APES ecosystem effort — covering scope, methodology, evidence criteria, anti-patterns, deliverables, schedule, and stop conditions — is being maintained as a Draft:

- [`research-plan.md`](research-plan.md) — Draft (v0.1). Defines how research is conducted; it is not itself a research finding.

Phase A and Phase B have been executed in separately scoped sprints. Phase C and Phase D have not begun.

## Sprint 2 Deliverables

Sprint 2 (Ecosystem Inventory & Initial Reverse Research, 2026-08-03) adds the following artifacts. None of these are APES positioning, gap analysis, or market conclusions — they are descriptive and reviewable.

> **Phase alignment.** Per `research/research-plan.md` §4.1, this sprint runs **Phase A (Inventory)** and an **Initial Reverse Research** activity treated as a Phase A supplemental investigation. Reverse Research is **not** Phase B. Phase B (Coverage Map), Phase C (Gap Analysis), and Phase D (Positioning Evidence) are deliberately deferred to future sprints.

> **Sprint 2.1 status.** Per Sprint 2.1 (evidence correction, see `tasks/sprint-02-1-evidence-correction.md`), Sprint 2's `Status` is `In Review`. The Source Register uses three orthogonal fields: Source Reliability (Level A–E), Claim Verification (Verified / Partially Verified / Unverified / Contradicted / Inaccessible), and Claim Type (Official self-description / Observable repository fact / Independent empirical evidence / Practitioner opinion / Community signal / Marketing claim).

- [`source-register.md`](source-register.md) — Draft (v0.3). 52 sources (SRC-001 to SRC-052). Includes arXiv 2602.11988 (SRC-044) and arXiv 2601.20404 (SRC-045) as conflicting empirical evidence on AGENTS.md; ISO 12207:2026 Edition 2 (SRC-006) and ISO 12207:2017 Edition 1 (SRC-052).
- [`notes/search-log.md`](notes/search-log.md) — Draft (v0.2). 31 searches actually executed (SE-001 to SE-031). No fabricated counts.
- [`ecosystem/inventory.md`](ecosystem/inventory.md) — Draft (v0.1). 9 categories describing adjacent artifacts.
- [`competitors/candidate-projects.md`](competitors/candidate-projects.md) — Draft (v0.1). Long list → short list of 10 Selected projects.
- [`competitors/reverse-research.md`](competitors/reverse-research.md) — Draft (v0.1). 10 Selected projects analyzed with the 14-section template; §S-10 AGENTS.md registers both conflicting academic studies.

Sprint 2 explicitly did **not** produce: a Feature Matrix, a Lifecycle Coverage Matrix, a Gap Analysis, APES market conclusions, APES positioning changes, new ADRs, or any formal standard module content. Sprint 2 also did not enter Phase B (Coverage Map), Phase C (Gap Analysis), or Phase D (Positioning Evidence).

## Sprint 2.2 Deliverables

Sprint 2.2 (Primary Source Verification, 2026-08-03) is a verification-only sprint. Per the brief: "Reduce uncertainty before increasing scope." It does **not** enter Coverage Map, Gap Analysis, Positioning Evidence, or APES standard writing.

> **Outcome.** The 2026-08-03 access window blocks direct WebFetch on every priority primary domain (`arxiv.org`, `github.com`, `agents.md`, `anthropic.com`, `docs.claude.com`, `iso.org`, `csrc.nist.gov`, `owaspsamm.org`, `owasp.org`, `cognitect.com`, `producttalk.org`). 22 verification attempts (VR-001 through VR-022) all ended with `Outcome: Inaccessible`. No source was upgraded to `Verified`. The Research Gate is `RESEARCH AGAIN`. Sprint 2 remains `In Review`.

- [`notes/verification-log.md`](notes/verification-log.md) — Draft (v0.1). 22 verification attempts using the 11-field schema (Verification ID, Source ID, Original URL, Access Date, Access Result, Claims Checked, Evidence Location, License Checked, Maintenance Checked, Outcome, Notes). All 22 outcomes are `Inaccessible`.
- [`tasks/sprint-02-2-primary-source-verification.md`](../tasks/sprint-02-2-primary-source-verification.md) — Sprint 2.2 task file with full sprint structure, Source ID Integrity Audit (no renumbering), and Research Gate determination.

The Source Register's Claim Verification column is preserved from Sprint 2.1; the Sprint 2.2 verification attempts are recorded in the verification log without altering existing rows. SRC-045 (arXiv 2601.20404) is flagged for an existence check by an external verifier — if it does not exist at the canonical arXiv ID, SRC-045 must be retracted in a future sprint.

## Sprint 2.3 Deliverables

Sprint 2.3 (External Verification Reconciliation, 2026-08-03) is a reconciliation-only sprint. Per the brief: "Reduce uncertainty before increasing scope." It does **not** enter Coverage Map, Gap Analysis, Positioning Evidence, or APES standard writing. It does **not** add new sources, renumber Source IDs, or expand the candidate list.

> **Outcome.** Six sources are upgraded from `Partially Verified` to `Verified` based on external-verification (EV-###) entries from an external reviewer with direct primary-source access. The 22 Sprint 2.2 Inaccessible verification attempts remain visible alongside the new External Verification Reconciliation dimension — both dimensions coexist. Sprint 2.2 statistics are corrected: 22 verification attempts / 22 unique VR IDs / 24 unique source IDs attempted / 0 repeated source IDs.

- [`notes/verification-log.md`](notes/verification-log.md) — Draft (v0.2). New "External Verification Reconciliation (Sprint 2.3)" section with the 8-field schema (External Verification ID, Source ID, Canonical URL, Verification Date, Verifier Type, Claims Verified, Remaining Limitations, Outcome). Six EV rows (EV-001 through EV-006), all `Outcome: Verified`.
- [`tasks/sprint-02-3-external-verification-reconciliation.md`](../tasks/sprint-02-3-external-verification-reconciliation.md) — Sprint 2.3 task file with full sprint structure, External Evidence Packet table, Statistics Correction, Acceptance Criteria, Remaining Limitations.
- [`source-register.md`](source-register.md) — Draft (v0.5). Six source rows upgraded to `Verified` (SRC-001, SRC-003, SRC-006, SRC-015, SRC-044, SRC-045) with EV-### citations in the Notes column. Source Audit Statistics recomputed: Verified=6, Partially Verified=32, Unverified=14, Contradicted=0, Inaccessible=0.
- [`ecosystem/inventory.md`](ecosystem/inventory.md) — Draft (v0.3). Per-row EV references for the six sources.
- [`competitors/candidate-projects.md`](competitors/candidate-projects.md) — Draft (v0.3). Sprint 2.3 reconciliation note in the Short List section.
- [`competitors/reverse-research.md`](competitors/reverse-research.md) — Draft (v0.3). §S-10 identity, §S-10 §11 conflicting approaches (full author lists and v1/v2 dates for both arXiv papers), §S-10 §13 verification notes, Cross-References.

- **Status:** Draft (v0.5, post Sprint 2.1 evidence correction; Sprint 2.2 verification attempted; Sprint 2.3 external verification reconciliation).
- **Source Audit Statistics (post-Sprint 2.3):** Verified=6, Partially Verified=32, Unverified=14, Contradicted=0, Inaccessible=0 (of 52 Source IDs).
- Conflicting empirical evidence between SRC-044 and SRC-045 is preserved verbatim; APES does not adjudicate. The methodological note that "conclusions cannot be generalized to all repositories, models, agents, or tasks; experimental setup must be cited. The 'AGENTS.md is always harmful' generalization is not supported" is recorded.
- Research Gate remains **`RESEARCH AGAIN`**; Sprint 2 remains **`In Review`**. The 10-condition rule was met for the six sources only because the external reviewer had direct primary-source access.

## Sprint 2.4 Deliverables

Sprint 2.4 (Targeted Primary-Source Re-verification, 2026-08-15) directly accessed canonical primary pages for seven priority repositories and five previously flagged official sources. It does not enter Phase C (Gap Analysis), Phase D (Positioning Evidence), or APES standard writing; it adds no source, candidate, ADR, RFC, dependency, or implementation artifact.

> **Outcome.** Twelve Source Register rows were upgraded: SRC-002, SRC-004, SRC-005, SRC-014, SRC-017, SRC-018, SRC-019, SRC-020, SRC-021, SRC-022, SRC-024, and SRC-027. The checked-in v0.6 baseline was 54 sources with Verified=10, Partially Verified=32, and Unverified=12; the v0.7 result is Verified=22, Partially Verified=22, and Unverified=10. The task brief's 60/16/32/12 baseline did not match the repository and no missing Source IDs were invented.

- [`notes/verification-log.md`](notes/verification-log.md) — VR-023 through VR-034 using the Sprint 2.2 11-field schema, each with actual access date 2026-08-15 and direct evidence locations.
- [`source-register.md`](source-register.md) — Draft v0.7; twelve claim-level promotions with direct primary evidence, current maintenance wording, and explicit limitations.
- [`ecosystem/inventory.md`](ecosystem/inventory.md) — synchronized verification states, current versions, canonical project positioning, and maintenance caveats.
- [`competitors/candidate-projects.md`](competitors/candidate-projects.md) — verification-only reconciliation; no candidate was added, removed, or re-ranked.
- [`competitors/reverse-research.md`](competitors/reverse-research.md) — direct ADR / Claude Code corrections and a bounded P0 repository evidence note.
- [`tasks/sprint-02-4-targeted-reverification.md`](../tasks/sprint-02-4-targeted-reverification.md) — scope, verification evidence, gate calculation, open questions, and final Sprint status.

Three material maintenance corrections are preserved: OpenCode and Roo Code are archived; Continue is read-only and no longer actively maintained. The requested OpenHands URL now resolves to `OpenHands/OpenHands`, whose current README positions Agent Canvas as a self-hosted developer control center. Claude Code's official memory documentation reads `CLAUDE.md` by default and documents `AGENTS.md` through import, copy, or symlink workflows rather than native automatic loading.

**Research Gate: `READY FOR REVIEW`.** The source threshold is 22 ≥ 15. A conservative repository/project-only count gives 13 unique directly verified projects: six prior projects plus the seven P0 repositories; the five P1 items are excluded from this count. This exceeds the threshold of 8. Sprint 2 remains `In Review` until maintainers confirm the gate interpretation and reconcile the task-brief baseline mismatch. Phase C and Phase D remain unstarted.

## Sprint 3 Deliverables

Sprint 3 (Coverage Map / Phase B, 2026-08-03) runs **Phase B (Coverage Map)** of `research/research-plan.md` §4.1 for the 10 Selected projects in `research/competitors/candidate-projects.md`. Coverage Mapping is descriptive, not feature-comparison, not gap analysis, not APES positioning. Sprint 3 does **not** enter Phase C (Gap Analysis), Phase D (Positioning Evidence), or APES standard writing.

> **Phase alignment.** Sprint 3 = Phase B only. Phase A was Sprint 2 (Inventory + Initial Reverse Research). Phase C and Phase D are deliberately deferred to future sprints.

> **Sprint 2 status note.** At Sprint 3 execution time, Sprint 2 remained `In Review` and the Research Gate was `RESEARCH AGAIN` per Sprint 2.2. Sprint 3 did not change either; Sprint 2.4 later moved the gate to `READY FOR REVIEW` while retaining `In Review` status.

- [`coverage/coverage-map.md`](coverage/coverage-map.md) — Draft (v0.1). Narrative coverage for each Selected project (S-01 through S-10): lifecycle responsibility, primary purpose, artifact types, engineering scope, standards involved, governance role, security role. Every claim references `SRC-NNN`.
- [`coverage/lifecycle-coverage-matrix.md`](coverage/lifecycle-coverage-matrix.md) — Draft (v0.1). 10 projects × 19 Sprint 3 lifecycle stages matrix. Cell values: Primary / Secondary / Partial / None / Unknown. Every non-empty cell carries Source ID + Evidence Type + Confidence.
- [`coverage/artifact-relationship-map.md`](coverage/artifact-relationship-map.md) — Draft (v0.1). 15 artifact types mapped to Selected projects that produce / consume them: AGENTS.md, CLAUDE.md, SPEC, RFC, ADR, Task, Checklist, Template, Prompt, Policy, Workflow, Architecture Decision, Knowledge Base, Standard, Command.

Sprint 3 explicitly did **not** produce: a Gap Analysis, Feature Matrix, Lifecycle Gap claim, Market Positioning, Competitive Positioning, SWOT, Roadmap, Recommendations, Vision, Priorities, Implementation Plan, APES Design, APES Architecture, Standard Modules, Prompt Library, new APES Commands/Templates/Checklists, Plugin Design, CLI, MCP, Website, Business Strategy, Brand Strategy, or any statement that APES is missing something. The 22 Sprint 2.2 Inaccessible verification attempts and the 6 Sprint 2.3 External Verification Reconciliation entries remain visible. Sprint 3 itself did not alter Sprint 2 evidence; Sprint 2.4 later appended a separate verification dimension.

## Sprint 3.1 Deliverables

Sprint 3.1 (Coverage Audit, 2026-08-03) is an audit-only sprint that verifies Sprint 3 (Coverage Map / Phase B) deliverables are consistent with their source evidence. Sprint 3.1 audits Sprint 3 outputs; it does not re-research the 10 Selected projects, does not add new sources, and does not enter Phase C (Gap Analysis), Phase D (Positioning Evidence), or APES standard writing.

> **Outcome.** Eight audit tasks were executed; eleven findings (A through K) were surfaced and applied to the Sprint 3 files. Final aggregate counts (post-audit): Primary=24, Secondary=1, Partial=7, None=15, Unknown=143 (of 190 cells = 10 projects × 19 lifecycle stages). All 17 Source IDs cited across the three Sprint 3 files exist in `source-register.md` within the registered range SRC-001 to SRC-052; no Source ID was added, removed, or renumbered.

- [`coverage/coverage-map.md`](coverage/coverage-map.md) — Draft (v0.1, post-audit). Narrative coverage for each Selected project (S-01 through S-10). S-06 ADR Confidence downgraded from `High` to `Medium` per Audit Finding D; "18 stages" / "180 cells" prose references corrected to "19 stages" / "190 cells" per Audit Finding E; aggregate count line corrected per Audit Finding G.
- [`coverage/lifecycle-coverage-matrix.md`](coverage/lifecycle-coverage-matrix.md) — Draft (v0.1, post-audit). 10 projects × 19 Sprint 3 lifecycle stages matrix. Cell values: Primary / Secondary / Partial / None / Unknown. Audit Finding A reclassified S-08 Security from `None` to `Unknown`; Audit Finding B reclassified S-03 Discovery from `None` to `Primary`; Audit Finding E corrected stage-count prose references; Audit Finding F removed incorrect Coverage Footprint footnote; Audit Finding G reclassified the aggregate `None=144/Unknown=1` count to the strict-rule totals. Per-cell evidence table now shows all 11 audit corrections in the "Audit Correction" / "Audit Finding" notes.
- [`coverage/artifact-relationship-map.md`](coverage/artifact-relationship-map.md) — Draft (v0.1, post-audit). 15 artifact types mapped to Selected projects that produce / consume them. Audit Finding C corrected the S-07 artifact-type summary count from 4 to 5.
- [`tasks/sprint-03-1-coverage-audit.md`](../tasks/sprint-03-1-coverage-audit.md) — Sprint 3.1 audit task file with Goal, Inputs, Audit Methodology, eight Audit Tasks Executed, eleven Audit Findings (A through K), Final Aggregate Counts, Source ID Integrity Audit, Coverage Rules, Cell-Value Scale, Confidence Scale, Deliverables, Scope, Out of Scope, Acceptance Criteria, Verification, Remaining Limitations, Status.

Sprint 3.1 explicitly did **not** produce: new research, new sources, Source ID renumbering, a Gap Analysis, a Feature Matrix, a Lifecycle Gap claim, Market Positioning, Competitive Positioning, SWOT, Roadmap, Recommendations, Vision, Priorities, Implementation Plan, APES Design, APES Architecture, Standard Modules, Prompt Library, new APES Commands/Templates/Checklists, Plugin Design, CLI, MCP, Website, Business Strategy, Brand Strategy, or any statement that APES is missing something. At Sprint 3.1 execution time, Sprint 2 remained `In Review` and the Research Gate remained `RESEARCH AGAIN`; Sprint 2.4 later changed only the gate determination.

## Foundation 0.2 Reference Research

Foundation 0.2 (2026-08-05) performed a bounded implementation-reference comparison outside the Phase A–D research sequence. It inspected canonical GitHub evidence for GitHub Spec Kit, OpenSpec, BMAD-METHOD, and Agent OS, while separating observed repository facts from APES-oriented inferences.

- [`competitors/open-source-reference-comparison.md`](competitors/open-source-reference-comparison.md) — functions, architecture, technology stack, strengths, limitations, and cross-project patterns for four reference projects.
- [`source-register.md`](source-register.md) — current v0.7 register of 54 sources (SRC-001 through SRC-054): Verified=22, Partially Verified=22, Unverified=10.
- [`notes/search-log.md`](notes/search-log.md) — SE-032 through SE-036 record the GitHub CLI failure and the successful canonical public evidence pass.
- [`../tasks/foundation-0-2-open-source-reference-architecture.md`](../tasks/foundation-0-2-open-source-reference-architecture.md) — completed documentation-only task record.

The comparison supported Proposed ADR-0002 at the time of Foundation 0.2; later governance records control its current state. Phase C and Phase D remain unstarted; Sprint 2 remains `In Review`, and Sprint 2.4 moved the Research Gate to `READY FOR REVIEW` pending maintainer confirmation.
