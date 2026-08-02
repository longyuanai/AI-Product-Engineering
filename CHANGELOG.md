# Changelog

- Status: Active
- Version: v0.1
- Owner: APES Maintainers
- Last Updated: 2026-08-03
- Purpose: Track notable changes to APES using the Keep a Changelog format.

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/).

## [Unreleased]

### Added — Sprint 2.3: External Verification Reconciliation (2026-08-03)

- Reconciliation-only sprint. No new research scope, no new sources, no Source ID renumbering, no Coverage Map, Gap Analysis, Positioning Evidence, Feature Matrix, or Lifecycle Coverage Matrix.
- Six sources upgraded from `Partially Verified` to `Verified` in `research/source-register.md` based on external-verification (EV-###) evidence from an external reviewer with direct primary-source access (2026-08-03): SRC-001 (AGENTS.md, EV-001), SRC-003 (NIST SSDF, EV-006), SRC-006 (ISO/IEC/IEEE 12207:2026, EV-005), SRC-015 (OpenAI Codex CLI, EV-002), SRC-044 (arXiv 2602.11988, EV-003), SRC-045 (arXiv 2601.20404, EV-004).
- SRC-045 is **not** retracted; existence, title, authors, dates, and abstract content are confirmed by EV-004. Authors: Jai Lal Lulla, Seyedmoein Mohsenimofidi, Matthias Galster, Jie M. Zhang, Sebastian Baltes, Christoph Treude (v1 2026-01-28; v2 2026-03-30).
- Created `tasks/sprint-02-3-external-verification-reconciliation.md` with full sprint structure (Goal, Inputs, External Evidence Packet, Scope, Out of Scope, Reconciliation Tasks, Statistics Correction, Acceptance Criteria, Verification, Remaining Limitations, Status).
- Added "External Verification Reconciliation (Sprint 2.3, 2026-08-03)" section to `research/notes/verification-log.md` using the 8-field schema (External Verification ID, Source ID, Canonical URL, Verification Date, Verifier Type, Claims Verified, Remaining Limitations, Outcome). All six EV rows have `Outcome: Verified`.
- Corrected Sprint 2.2 statistics: `Verification attempts: 22 / Unique verification IDs: 22 / Unique source IDs attempted: 24 / Repeated source IDs: none`. The Attempt count and Source count are distinct reporting dimensions (some VR rows reference multiple Source IDs, e.g., VR-008 covers SRC-008+012+036) and must not be conflated.
- The 22 Sprint 2.2 Inaccessible verification attempts are **preserved** and remain visible alongside the new External Verification Reconciliation dimension — both reporting dimensions coexist.
- Recomputed `research/source-register.md` Source Audit Statistics (v0.5): Verified=6, Partially Verified=32, Unverified=14, Contradicted=0, Inaccessible=0 (of the 52 Source IDs).
- Cross-file backfill in `research/ecosystem/inventory.md` (v0.3), `research/competitors/candidate-projects.md` (v0.3), `research/competitors/reverse-research.md` (v0.3): per-row EV references; Sprint 2.3 reconciliation notes; updated §S-10 identity, §S-10 §11 conflicting approaches (full author lists for both arXiv papers; updated v1/v2 dates), §S-10 §13 verification notes (Sprint 2.3 outcome; SRC-001/044/045 now `Verified`; SRC-045 not retracted).
- Conflicting empirical evidence between SRC-044 and SRC-045 is preserved verbatim; APES does not adjudicate. The methodological note that "conclusions cannot be generalized to all repositories, models, agents, or tasks; experimental setup must be cited. The 'AGENTS.md is always harmful' generalization is not supported" is added to §S-10 §11.
- Research Gate remains **`RESEARCH AGAIN`**; Sprint 2 remains **`In Review`**. The 10-condition rule was met for the six sources only because the external reviewer had direct primary-source access; APES itself did not perform the verification and the under-15-Verified threshold is unchanged in spirit.
- No git commit, push, tag, or branch creation was performed.
- This CHANGELOG entry.

### Added — Sprint 2.2: Primary Source Verification (2026-08-03)

- Verification-only sprint. No new research scope, no new sources, no Source ID renumbering.
- Created `research/notes/verification-log.md` — 22 verification attempts (VR-001 through VR-022) using the 11-field schema. All 22 attempts ended with `Outcome: Inaccessible` because the access window (2026-08-03) blocks direct WebFetch on `arxiv.org`, `github.com`, `agents.md`, `anthropic.com`, `docs.claude.com`, `iso.org`, `csrc.nist.gov`, `owaspsamm.org`, `owasp.org`, `cognitect.com`, and `producttalk.org`.
- Created `tasks/sprint-02-2-primary-source-verification.md` — sprint task file with Goal, Scope, Out of Scope, Tasks, Acceptance Criteria, Verification Log reference, Source ID Integrity Audit (no renumbering), Research Gate determination (`RESEARCH AGAIN`), Final Status.
- Source ID integrity audit: zero renumbering, zero new Source IDs. The 52 Source IDs (SRC-001 through SRC-052) remain identical to the v0.3 schema produced by Sprint 2.1.
- Statistics recomputed in `research/source-register.md` (v0.4): no upgrades to `Verified`. All 22 P0 sources marked `Inaccessible` in the verification log preserve their existing Claim Verification status (a small number of `Partially Verified` rows remain so because they had been corroborated by community sources during Sprint 2.0; the new `Inaccessible` outcomes are recorded separately and do not downgrade prior corroborations).
- Updated `research/ecosystem/inventory.md` (v0.2), `research/competitors/candidate-projects.md` (v0.2), `research/competitors/reverse-research.md` (v0.2) with Sprint 2.2 verification notes and cross-references. No semantic change to project content; no project was added, removed, or re-ranked.
- Research Gate: **`RESEARCH AGAIN`** — no source was upgraded to `Verified`; the 10-condition rule could not be met for any priority source under the access window. Sprint 2 remains `In Review`.
- Flagged source: **SRC-045 (arXiv 2601.20404)** has no community corroboration and must be existence-checked by an external verifier before the next sprint. If it does not exist at the canonical arXiv ID, SRC-045 must be retracted in a future sprint (not silently retained).
- No Coverage Map, Feature Matrix, Lifecycle Coverage Matrix, Gap Analysis, or APES positioning conclusion was produced. No formal Standard module was written. No git commit, push, tag, or branch creation was performed.
- This CHANGELOG entry.

### Added — Sprint 2.1: Ecosystem Inventory Evidence Correction (2026-08-03)

- Audit and correction of Sprint 2 evidence. No new research was conducted.
- Phase definitions realigned with `research/research-plan.md`: Phase A = Inventory, Phase B = Coverage Map, Phase C = Gap Analysis, Phase D = Positioning Evidence. Sprint 2 Reverse Research is now labeled as **Initial Reverse Research / Phase A supplemental activity** — not Phase B.
- Source Register schema split: Source Reliability (Level A–E), Claim Verification (Verified / Partially Verified / Unverified / Contradicted / Inaccessible), and Claim Type (Official self-description / Observable repository fact / Independent empirical evidence / Practitioner opinion / Community signal / Marketing claim).
- Replaced SRC-044 with the specific arXiv paper 2602.11988 (Gloaguen et al., 2026-02-12).
- Added the conflicting arXiv paper 2601.20404 (2026-01-28) as SRC-045.
- Corrected ISO/IEC/IEEE 12207 entries: SRC-006 (ISO/IEC/IEEE 12207:2026 Edition 2, 2026-04); SRC-052 (ISO/IEC/IEEE 12207:2017 Edition 1, 2017-11, historical).
- Downgraded sources whose license / date / maintenance status were derived only from third-party summaries.
- Sprint 2 status changed to `In Review` pending human review; Sprint 2.1 task file created.
- Statistics recomputed and reported in `research/source-register.md` §"Source Audit Statistics".
- This CHANGELOG entry.

### Added — Sprint 2: Ecosystem Inventory & Reverse Research (2026-08-03)

- Built `research/source-register.md` (50 sources, 15-field schema, A–E reliability; counter-evidence SRC-044 ETH Zurich report recorded).
- Built `research/notes/search-log.md` (31 searches, 9-field schema, no fabricated counts).
- Built `research/ecosystem/inventory.md` (9 categories of adjacent artifacts).
- Built `research/competitors/candidate-projects.md` (long list → short list of 10 Selected projects; defer / decline reasons explicit).
- Built `research/competitors/reverse-research.md` (10 projects analyzed with the 14-section template; AGENTS.md section surfaces counter-evidence).
- Incremental pointer in `research/README.md` listing all Sprint 2 deliverables.
- New sprint task file `tasks/sprint-02-ecosystem-inventory.md`.
- This CHANGELOG entry.

### Added — Sprint 1.1: Research Plan Review Fix (2026-08-03)

- Refined the ecosystem research plan after methodology review.
- Added source register, reliability levels, candidate selection, search logging, and kill criteria.
- Corrected Git-status and copyright-handling language.

### Added — Sprint 1: Ecosystem Research Plan (2026-08-03)

- Draft ecosystem research plan in `research/research-plan.md`. Defines research purpose, principles, scope and non-scope, four-phase methodology (Inventory → Coverage Map → Gap Analysis → Positioning Evidence), source categories and sampling, hypotheses under test, evidence-quality criteria, anti-patterns to prevent, file layout, cadence, stop conditions, review governance, and feedback loop into APES decisions.
- New sprint task file `tasks/sprint-01-ecosystem-research-plan.md`.
- Additive pointer to the research plan added in `research/README.md`.
- This CHANGELOG entry.

### Added — Sprint 0: Repository Foundation (2026-08-03)

- Initial repository structure: `docs/`, `standards/`, `protocols/`, `templates/`, `commands/`, `checklists/`, `research/`, `examples/`, `governance/`, `design/`, `tasks/`, `sessions/`, `assets/`, `scripts/`, `website/`.
- Core documents: `README.md`, `VISION.md`, `MANIFESTO.md`, `ROADMAP.md`, `AGENTS.md`, `CONTRIBUTING.md`, `CODE_OF_CONDUCT.md`.
- Placeholder README files for every stage module under `standards/`.
- GitHub templates: bug report, feature request, standard proposal, pull request template.
- Initial GitHub Actions workflow (Markdown check, draft).
- Initial ADR (`ADR-0001-project-positioning`).
- Initial design document (`design/01-repository-architecture.md`).
- Sprint task file (`tasks/sprint-00-repository-foundation.md`).

### Notes

- The plan is a methodology, not a research finding. No claim about ecosystem, market, competitors, or adoption is made.
- Execution of Phases A–D is deferred to a later, separately-scoped sprint.
- No git operations were performed during this sprint.
- License selection remains pending maintainer decision.
- All standard module contents remain placeholders; no module standard has been written yet.
