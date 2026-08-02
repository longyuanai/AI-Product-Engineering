# Sprint 02 — Ecosystem Inventory & Reverse Research

- Status: In Review
- Version: v0.1
- Owner: APES Maintainers
- Last Updated: 2026-08-03

> **Sprint 2.1 note.** Per Sprint 2.1 evidence correction (see `tasks/sprint-02-1-evidence-correction.md`), the Verification Status terminology in this sprint's deliverables was upgraded from a single field to three orthogonal fields: Source Reliability, Claim Verification, and Claim Type. Reverse Research in this sprint is an **Initial Reverse Research / Phase A supplemental activity** — it is **not** Phase B of the research plan. Phase B is Coverage Map; Phase C is Gap Analysis; Phase D is Positioning Evidence. This sprint does **not** enter Phase B, Phase C, or Phase D.
>
> `Status: In Review` here means: the deliverables have been written and Sprint 2.1 has audited their evidence model. The status will return to `Completed` after a human reviewer signs off. Until then, no Sprint 2 deliverable should be cited as a finding.

## Table of Contents

- [Sprint Goal](#sprint-goal)
- [Scope](#scope)
- [Out of Scope](#out-of-scope)
- [Tasks](#tasks)
- [Acceptance Criteria](#acceptance-criteria)
- [Verification](#verification)
- [Notes](#notes)
- [Final Status](#final-status)

## Sprint Goal

Run **Phase A (Inventory)** of the research plan (`research/research-plan.md` §4.1) and an **Initial Reverse Research** activity as a Phase A supplemental investigation. Build an evidence-anchored inventory of adjacent artifacts and apply the 14-section Core Project Analysis template to a Selected short list. Surface both confirming and contradicting evidence where it exists. Do **not** produce a Gap Analysis, Feature Matrix, Lifecycle Coverage Matrix, or APES positioning / market conclusions. Do **not** enter Phase B (Coverage Map), Phase C (Gap Analysis), or Phase D (Positioning Evidence).

## Scope

In scope:

- Building `research/source-register.md` with at least 35 sources (≥12 official), each with the 15-field Source Register Schema and an A–E reliability classification.
- Building `research/notes/search-log.md` with at least 30 executed searches, each row matching the 9-field Search Log Schema. No fabricated search-result counts.
- Building `research/ecosystem/inventory.md` covering at least 9 categories, each with: artifact identity, source(s), description, verification status.
- Building `research/competitors/candidate-projects.md` with the long list, the short list of at least 10 Selected projects, the explicit defer / decline reasons, and held-candidate inventory.
- Building `research/competitors/reverse-research.md` analyzing the short list with the 14-section template. Counter-evidence (where located) is recorded honestly.
- Incrementally updating `research/README.md` and `CHANGELOG.md`.
- Creating this task file.
- Recording deliberate non-deliverables in this file so future readers can see what was deliberately omitted.

## Out of Scope

The following are explicitly forbidden in this sprint and were **not** attempted:

- Writing a final Feature Matrix.
- Writing a complete Lifecycle Coverage Matrix.
- Conducting a formal Gap Analysis.
- Drawing APES market conclusions.
- Stating that APES does or does not have a real gap.
- Modifying APES positioning.
- Creating new ADRs or RFCs (except in the event of a blocking conflict, in which case only the conflict is reported; no blocking conflicts surfaced in this sprint).
- Writing any formal Standard module content.
- Writing any Commands, Templates, or Checklists.
- Implementing any CLI, website, MCP, or plugin.
- Auto-committing or auto-pushing.
- Deleting any existing research-plan files.
- Filling source facts from AI memory.
- Fabricating stars, release dates, licenses, authors, or maintenance status.
- Quoting non-existent or unreachable URLs as primary sources.
- Rewriting marketing copy as objective fact.
- Saving copyrighted full-text into the repository.

## Tasks

- [x] Pre-execution checks: confirm working directory, read all context files listed in the Sprint 2 brief, confirm the research plan's Phase A / Phase B scope.
- [x] Build `research/source-register.md` with ≥35 sources (≥12 official), each row matching the Source Register Schema; reliability classified A–E.
- [x] Build `research/notes/search-log.md` with ≥30 executed searches (9-field schema). No fabricated counts.
- [x] Build `research/ecosystem/inventory.md` covering ≥9 categories. Descriptive only.
- [x] Build `research/competitors/candidate-projects.md` with long list + short list of ≥10 Selected projects, defer / decline reasons recorded.
- [x] Build `research/competitors/reverse-research.md` with ≥6 projects using the 14-section template. Confirming and contradicting evidence surfaced.
- [x] Incrementally update `research/README.md` so it references all Sprint 2 deliverables and continues to end with a trailing newline.
- [x] Incrementally update `CHANGELOG.md` with an Unreleased entry for Sprint 2 (no claim of research findings).
- [x] Create this task file.
- [x] Run verification: `git status`, file-existence checks, structural checks against the schema rules, no out-of-scope edits, no auto commit / push, working tree left in uncommitted but reviewable state.

## Acceptance Criteria

- `research/source-register.md` exists with ≥35 sources, ≥12 marked `Official` (A or B reliability); each row has 15 fields.
- `research/notes/search-log.md` exists with ≥30 searches; each row has 9 fields; no fabricated counts.
- `research/ecosystem/inventory.md` exists with ≥9 categories.
- `research/competitors/candidate-projects.md` exists with a long list and a short list of ≥10 Selected projects; defer / decline reasons are recorded explicitly.
- `research/competitors/reverse-research.md` exists with 6–10 projects analyzed using the 14-section template; at least one row surfaces contradicting evidence (AGENTS.md / SRC-044).
- No final Feature Matrix, Lifecycle Coverage Matrix, or Gap Analysis is produced.
- No APES positioning, market, or adoption claim is recorded anywhere in the Sprint 2 artifacts.
- No new ADR, RFC, Standard module, Command, Template, Checklist, CLI, website, MCP, or plugin code is added.
- No file outside the allowed list (`research/source-register.md`, `research/notes/search-log.md`, `research/ecosystem/inventory.md`, `research/competitors/candidate-projects.md`, `research/competitors/reverse-research.md`, `research/README.md`, `CHANGELOG.md`, `tasks/sprint-02-ecosystem-inventory.md`) was modified.
- No git commit, push, tag, or branch creation was performed.
- No URL whose primary source could not be fetched or corroborated is presented as a verified primary source.
- No fabricated star counts, release dates, license terms, authors, or maintenance status values appear in any artifact.

## Verification

The following checks were run as part of this sprint:

- `git status` recorded before any change (working tree had Sprint 1.1 uncommitted changes) and again at the end of the sprint. The final state adds Sprint 2 files: `research/source-register.md`, `research/notes/search-log.md`, `research/ecosystem/inventory.md`, `research/competitors/candidate-projects.md`, `research/competitors/reverse-research.md`, plus the additive updates to `research/README.md` and `CHANGELOG.md`, plus this task file.
- `git log --oneline -5` and `git remote -v` recorded.
- File-existence confirmation for all five new research artifacts and the task file.
- Row-count checks against acceptance criteria:
  - Source Register: 50 sources (≥35), with ≥12 official rows.
  - Search Log: 31 searches (≥30).
  - Inventory: 9 categories.
  - Candidate projects: short list of 10 Selected (≥10).
  - Reverse research: 10 projects (within 6–10 — note: brief permits 6–10; ten is at the upper edge and accepted for breadth across clusters).
- Schema check: every row of source-register and search-log has the required field count.
- Counter-evidence check: SRC-044 (ETH Zurich report) is recorded in source-register and is referenced in reverse-research §S-10.
- No-application-source check: no `src/`, `dist/`, `build/`, `node_modules/`, or third-party action file added.
- Out-of-scope claim check: no Gap Analysis, no Feature Matrix, no Lifecycle Coverage Matrix, no APES market / positioning claim.

Verification details are summarized in the agent's completion report.

## Notes

- This sprint is Phase A and an Initial Reverse Research activity of the research plan. Phase B (Coverage Map), Phase C (Gap Analysis), and Phase D (Positioning Evidence) are deliberately not run here.
- The 10 Selected projects deliberately span the four inventory clusters (discovery methods, decision artifacts, AI coding agents, standards/governance) so the reverse research is not over-concentrated in any single area. Standards-cluster entries (NIST SSDF, OWASP SAMM v2, ISO 12207, DORA, SRE Book, DHS/CISA Attestation) and additional AI coding agent rows (Cursor, aider, Cline, OpenHands, OpenAI Codex CLI, GitHub Copilot, Gemini CLI) are recorded as **held candidates** in `candidate-projects.md` and may be advanced to reverse research in a subsequent sprint without re-running selection.
- Counter-evidence (SRC-044 ETH Zurich report) is recorded honestly under S-10 (AGENTS.md) per the Sprint 2 brief.
- WebFetch was restricted for `github.com`, `anthropic.com`, `iso.org`, `csrc.nist.gov`, `owasp.org`, `cursor.com`, `producttalk.org`, and several other primary domains during the access window. WebSearch was used as a fallback. Items with only WebSearch-only corroboration are marked `Page Unverified` and rely on community corroborations; no such item is presented as a verified primary source.
- Status note: `Status: Completed` refers to the **planning + execution** of this sprint, not to the conclusion of the full APES research effort. Phases C and D remain deferred to future sprints and will be scoped independently.

## Final Status

**In Review** for the items listed in [Tasks](#tasks) above. Sprint 2.1 has audited evidence quality, phase definitions, and source status; Status is `In Review` pending human review. Items left intentionally open (Phase B Coverage Map, Phase C Gap Analysis, additional AI coding-agent reverse research, multi-agent orchestration framework reverse research, standards-cluster reverse research, license decision, code of conduct finalization, MD lint action choice, any subsequent sprint planning) are tracked in the agent's "Open Decisions" report.