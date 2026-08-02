# research/

- Status: Placeholder
- Version: v0.2
- Owner: APES Maintainers
- Last Updated: 2026-08-03
- Purpose: Hold research notes used to inform the APES standard.

## Table of Contents

- [Purpose](#purpose)
- [Subdirectories](#subdirectories)
- [Citation Rules](#citation-rules)
- [Status](#status)

## Purpose

Research notes accumulate evidence about the AI product-engineering ecosystem and inform which practices APES should codify. Research here is *about* the environment in which APES will be applied, not about APES itself.

## Subdirectories

- [`ecosystem/`](ecosystem/README.md) — Note on the broader AI tooling ecosystem as it affects APES.
- [`competitors/`](competitors/README.md) — Note on competing standards, frameworks, and tools.
- [`papers/`](papers/README.md) — Academic and industry literature relevant to APES.
- [`notes/`](notes/README.md) — Free-form research notes and observations.

## Citation Rules

Every note must include:

- Source (URL or citation)
- Access date
- The specific claim drawn from the source
- A quote, table, or figure pointer where possible

## Status

Placeholder. No research note has been published yet. Sprint 0 forbids conducting this research; later sprints will collect it.

## Research Plan

A research plan for the APES ecosystem effort — covering scope, methodology, evidence criteria, anti-patterns, deliverables, schedule, and stop conditions — is being maintained as a Draft:

- [`research-plan.md`](research-plan.md) — Draft (v0.1). Defines how research is conducted; it is not itself a research finding.

Execution of the plan (Phases A–D in `research-plan.md` §4.1) is a separate, later sprint.

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

SRC-045 is **not** retracted: existence, title, authors, dates, and abstract content are confirmed by EV-004. Conflicting empirical evidence between SRC-044 and SRC-045 is preserved verbatim; APES does not adjudicate. The Research Gate remains `RESEARCH AGAIN`; Sprint 2 remains `In Review`.
