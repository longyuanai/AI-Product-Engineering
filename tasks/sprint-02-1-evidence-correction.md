# Sprint 02.1 — Ecosystem Inventory Evidence Correction

- Status: Completed
- Version: v0.1
- Owner: APES Maintainers
- Last Updated: 2026-08-03

## Table of Contents

- [Goal](#goal)
- [Scope](#scope)
- [Issues Found](#issues-found)
- [Tasks](#tasks)
- [Acceptance Criteria](#acceptance-criteria)
- [Verification](#verification)
- [Status](#status)

## Goal

Audit the Sprint 2 evidence and fix quality, phase-definition, and source-status problems without expanding the scope of research. Specifically:

1. Realign phase definitions with `research/research-plan.md` (Phase A = Inventory, Phase B = Coverage Map, Phase C = Gap Analysis, Phase D = Positioning Evidence).
2. Relabel Sprint 2 Reverse Research as **Initial Reverse Research / Phase A supplemental activity** (it is **not** Phase B).
3. Distinguish **Source Reliability** (Level A–E) from **Claim Verification** (Verified / Partially Verified / Unverified / Contradicted / Inaccessible), and require a **Claim Type** tag on every source.
4. Downgrade sources whose primary evidence was not directly accessed or whose license / date / maintenance status came from a third-party summary or community report.
5. Replace SRC-044 (vague ETH Zurich report) with the specific arXiv paper 2602.11988 and register the **conflicting** paper 2601.20404.
6. Correct ISO/IEC/IEEE 12207 to the concrete 2026-04 Edition 2 publication (with 2017 Edition 1 recorded as a historical version).
7. Remove precise facts that cannot be verified from a primary source (commit counts, vague version numbers, exact release dates, "reported" events, unverified licenses, unverified adoption numbers, third-party business or organizational conclusions).
8. Recompute source statistics (totals by reliability, by verification, by claim type).
9. Mark Sprint 2 status as **In Review** pending human review.

## Scope

In scope (allowed files):

- `research/source-register.md`
- `research/ecosystem/inventory.md`
- `research/competitors/candidate-projects.md`
- `research/competitors/reverse-research.md`
- `research/notes/search-log.md`
- `research/README.md`
- `tasks/sprint-02-ecosystem-inventory.md`
- `CHANGELOG.md`

Allowed to create:

- `tasks/sprint-02-1-evidence-correction.md` (this file)

## Out of Scope

Explicitly forbidden in this sprint and **not** attempted:

- Adding new candidate projects in bulk.
- Adding low-quality sources to pad counts.
- Beginning Coverage Map (Phase B).
- Beginning Gap Analysis (Phase C).
- Drawing APES positioning / market conclusions.
- Writing any formal Standard module content.
- Auto-committing or auto-pushing.
- Marking search snippets as primary sources.
- Treating vendor marketing statements as independent evidence.
- Deleting contradicting evidence.
- Filling source facts from AI memory.

## Issues Found

### Phase-definition drift

Sprint 2 deliverables (notably `tasks/sprint-02-ecosystem-inventory.md`, `research/README.md`, `CHANGELOG.md`) used "Phase A and Phase B" language for what was actually an **Initial Reverse Research** activity. Per `research/research-plan.md`, Phase A is Inventory, Phase B is Coverage Map. Reverse Research is best characterized as a Phase A supplemental activity.

### Verification Status field overloaded

The Verification Status field conflated page-fetch status with claim truth. Per the brief, it must be split into Source Reliability (Level A–E) and Claim Verification (Verified / Partially Verified / Unverified / Contradicted / Inaccessible).

### Claim Type missing

Sources were not tagged by what kind of claim they support (official self-description, observable repo fact, independent empirical evidence, practitioner opinion, community signal, marketing claim). Many entries made claims the source type could not actually support.

### Specific evidence problems

- SRC-014, SRC-017, SRC-018, SRC-019, SRC-020, SRC-022, SRC-024, SRC-025, SRC-026, SRC-029, SRC-030 — license terms were derived from third-party or "community reports" rather than from LICENSE files. Must be **Partially Verified** at best, **Unverified** where no direct LICENSE evidence exists.
- SRC-006 — ISO 12207 entry used placeholder language ("per search"; "edition referenced as 2026"). Must be rewritten with concrete ISO 12207:2026 Edition 2 (2026-04) data, with ISO 12207:2017 Edition 1 (2017-11) recorded as a historical version.
- SRC-031 — precise "2025-08" snapshot date asserted without direct primary evidence. Must be **Unverified**.
- SRC-033 — Microsoft Agent Framework consolidation framed as fact with only third-party report. Must be **Unverified** or downgraded.
- SRC-034 — Codex Security CLI release date "2026-07-28" asserted with third-party attribution. Must be **Unverified**.
- SRC-042 — Devin page referenced but Page Unverified; marketing-leaning. Must be **Partially Verified** or downgraded.
- SRC-044 — vague "ETH Zurich report" with placeholder URL. Must be replaced with arXiv 2602.11988 (Gloaguen et al., 2026-02-12).
- SRC-045, SRC-046, SRC-047, SRC-048, SRC-049, SRC-050 — many entries used placeholder URLs, "Page Unverified", or "concept recorded". Must be audited and either corrected or downgraded.

### Counter-evidence incomplete

Only one side of the AGENTS.md academic debate was recorded. The conflicting arXiv paper 2601.20404 (2026-01-28) had not been registered.

### Statistics conflation

Sprint 2 reported "36 Level A/B" as if that equalled verified sources. Per the brief, Level A/B are reliability levels, **not** verification status. Statistics must be recomputed.

## Tasks

- [x] Pre-execution checks (`git status`, `git diff --stat`, `git diff --check`).
- [x] Realign phase definitions in `tasks/sprint-02-ecosystem-inventory.md`, `research/README.md`, `CHANGELOG.md`.
- [x] Update `research/source-register.md`:
  - Replace the Verification Status column with separate Source Reliability, Claim Verification, and Claim Type columns.
  - Downgrade rows whose primary evidence was not directly accessed.
  - Rewrite SRC-006 (ISO 12207) with concrete ISO 12207:2026 Edition 2 (2026-04); add SRC-051 (ISO 12207:2017 Edition 1, 2017-11).
  - Replace SRC-044 with the specific arXiv paper 2602.11988 (Gloaguen et al., 2026-02-12).
  - Add the conflicting arXiv paper 2601.20404 (2026-01-28).
  - Remove precise facts that cannot be verified from a primary source.
  - Recompute statistics.
- [x] Update `research/ecosystem/inventory.md` to reflect corrected verification statuses and remove unverified specifics.
- [x] Update `research/competitors/candidate-projects.md` to remove unverified license / date specifics and reflect downgrade decisions.
- [x] Update `research/competitors/reverse-research.md` §S-10 to register both academic papers and surface the conflict.
- [x] Update `research/notes/search-log.md` to mark entries accurately (the searches were performed; the question is whether they yielded primary evidence or only summaries).
- [x] Mark Sprint 2 status as `In Review` in `tasks/sprint-02-ecosystem-inventory.md`.
- [x] Add an Unreleased entry in `CHANGELOG.md` for Sprint 2.1.
- [x] Create this task file.
- [x] Run verification.

## Acceptance Criteria

1. Phase definitions in Sprint 2 deliverables match `research/research-plan.md` exactly (A: Inventory, B: Coverage Map, C: Gap Analysis, D: Positioning Evidence).
2. Sprint 2 Reverse Research is labeled as a Phase A supplemental activity / Initial Reverse Research — **not** Phase B.
3. The Source Register separates Source Reliability, Claim Verification, and Claim Type as distinct columns.
4. No source is marked `Verified` unless its primary source was directly accessed (page loaded and key evidence drawn from it).
5. Sources whose license / date / maintenance status were derived from third-party summaries are downgraded to `Partially Verified` or `Unverified`.
6. SRC-044 is replaced with arXiv 2602.11988 (Gloaguen et al., 2026-02-12), with title, URL, authors, and publication date.
7. The conflicting arXiv paper 2601.20404 (2026-01-28) is registered with its findings.
8. ISO 12207 entries are accurate: ISO/IEC/IEEE 12207:2026 Edition 2 (2026-04) as the primary, ISO/IEC/IEEE 12207:2017 Edition 1 (2017-11) as historical.
9. Official self-descriptions are distinguished from independent evidence in Claim Type.
10. Source statistics are recomputed and reported in the Source Audit Statistics section of this file and in the Source Register.
11. Sprint 2 status is `In Review`.
12. Sprint 2.1 task file exists.
13. No next-phase file has been created.
14. No file outside the allowed list has been modified.
15. No commit / push / tag / branch operation has been performed.

## Verification

- `git status`, `git diff --stat`, `git diff --check` recorded.
- Source Register column count and schema confirmed.
- Row counts re-verified.
- Statistics recomputed and reported in `research/source-register.md`.
- File existence checks for all modified files.

## Status

**Completed** for the items listed in [Tasks](#tasks) above. Sprint 2 itself remains `In Review` until human review is performed.