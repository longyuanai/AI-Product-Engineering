# tasks/sprint-02-3-external-verification-reconciliation.md

- Status: Completed
- Sprint: 2.3
- Owner: APES Maintainers
- Last Updated: 2026-08-03
- Purpose: Reconcile six external-verification (EV-###) entries from an external reviewer with direct primary-source access into the Sprint 2 evidence trail. Correct Sprint 2.2 statistics ambiguity. Do not expand research scope.

## Goal

Bring six external-verification entries (EV-001 through EV-006) into the existing research artifacts in a way that:

1. Upgrades six Source Register rows from `Partially Verified` to `Verified` based on direct primary-source evidence.
2. Records the external-verification dimension alongside the Sprint 2.2 Inaccessible dimension — both remain visible.
3. Fixes Sprint 2.2 statistics ambiguity: separates Attempt count from Source count.
4. Backfills cross-file references in inventory, candidate-projects, and reverse-research without changing project content.
5. Leaves the Research Gate (`RESEARCH AGAIN`) and Sprint 2 status (`In Review`) untouched.

## Inputs

- Six external-verification entries EV-001 through EV-006, supplied by an external reviewer with direct primary-source access on 2026-08-03:
  - EV-001: SRC-001 (AGENTS.md) — page content, official self-positioning.
  - EV-002: SRC-015 (OpenAI Codex CLI) — repo existence, Apache-2.0 License, README positioning, active maintenance.
  - EV-003: SRC-044 (arXiv 2602.11988) — paper existence, title, authors, dates, abstract content.
  - EV-004: SRC-045 (arXiv 2601.20404) — paper existence, title, authors, dates, abstract content.
  - EV-005: SRC-006 (ISO/IEC/IEEE 12207:2026) — number, title, edition, publication date, Published status.
  - EV-006: SRC-003 (NIST SP 800-218 SSDF) — number, version, date, authors, official summary.
- `research/source-register.md` (v0.4, post-Sprint 2.2).
- `research/notes/verification-log.md` (v0.1, 22 Inaccessible attempts).
- `research/ecosystem/inventory.md`, `research/competitors/candidate-projects.md`, `research/competitors/reverse-research.md`.

## External Evidence Packet

| External Verification ID | Source ID | Canonical URL | Claims Verified |
|---|---|---|---|
| EV-001 | SRC-001 | https://agents.md/ | Page exists; project self-positioning ("simple, open format to guide AI coding agents") verified; adoption figure is project-maintainer-reported. |
| EV-002 | SRC-015 | https://github.com/openai/codex | Repo exists; License Apache-2.0 in LICENSE file; README positioning verified; maintenance active (recent commits/releases). |
| EV-003 | SRC-044 | https://arxiv.org/abs/2602.11988 | Paper exists; title verified; authors: Thibaud Gloaguen, Niels Mündler, Mark Müller, Veselin Raychev, Martin Vechev; v1 2026-02-12, v2 2026-06-23; abstract "mean inference cost increased by over 20%" verified. |
| EV-004 | SRC-045 | https://arxiv.org/abs/2601.20404 | Paper exists; title verified; authors: Jai Lal Lulla, Seyedmoein Mohsenimofidi, Matthias Galster, Jie M. Zhang, Sebastian Baltes, Christoph Treude; v1 2026-01-28, v2 2026-03-30; "10 repositories, 124 Pull Requests" verified; existence NOT retracted. |
| EV-005 | SRC-006 | https://www.iso.org/standard/305973.html (or current canonical listing) | Number ISO/IEC/IEEE 12207:2026, Edition 2 verified; Published 2026-04 verified; full text paywalled. |
| EV-006 | SRC-003 | https://csrc.nist.gov/pubs/sp/800/218/final | Number SP 800-218, version 1.1 (or current), date, authors verified; official summary verified. |

Verifier Type for all six: external reviewer with direct primary-source access.

## Scope

- Upgrade six Source Register rows.
- Add External Verification Reconciliation section to `verification-log.md` using the 8-field schema.
- Fix Sprint 2.2 statistics: report `Verification attempts: 22`, `Unique verification IDs: 22`, `Unique source IDs attempted: 24`, `Repeated source IDs: none`.
- Cross-file backfill in inventory.md, candidate-projects.md, reverse-research.md.
- Create this task file.
- Update `CHANGELOG.md` and `research/README.md`.

## Out of Scope

- No new WebSearch or WebFetch.
- No Coverage Map, Gap Analysis, Positioning Evidence, or formal standard writing.
- No Feature Matrix, Lifecycle Coverage Matrix, or APES positioning conclusions.
- No new Source IDs; no renumbering.
- No auto-commit or push.
- No overwriting of Sprint 2.2 Inaccessible rows — both dimensions remain visible.
- No retraction of SRC-045 (existence confirmed via EV-004).
- No fabrication of license, date, author, or maintenance facts.

## Reconciliation Tasks

| # | Task | Status |
|---|---|---|
| 1 | Upgrade SRC-001, SRC-003, SRC-006, SRC-015, SRC-044, SRC-045 in `source-register.md` to `Verified` with EV-### notes. | Completed |
| 2 | Add External Verification Reconciliation section to `verification-log.md` with 8-field schema and 6 EV rows. | Completed |
| 3 | Correct Sprint 2.2 statistics in `verification-log.md`: 22 attempts / 22 unique VR IDs / 24 unique source IDs / 0 repeated. | Completed |
| 4 | Backfill `inventory.md` with per-row EV references for the 6 sources. | Completed |
| 5 | Backfill `candidate-projects.md` with the Sprint 2.3 reconciliation note. | Completed |
| 6 | Backfill `reverse-research.md` (§S-10 identity, §S-10 §11 conflicts, §S-10 §13 verification notes, Cross-References). | Completed |
| 7 | Recompute Source Audit Statistics in `source-register.md`: Verified=6, Partially Verified=32, Unverified=14, Contradicted=0, Inaccessible=0 (of the 52 Source IDs). | Completed |
| 8 | Create this task file. | Completed |
| 9 | Update `CHANGELOG.md` Unreleased section. | Completed |
| 10 | Update `research/README.md` to add Sprint 2.3 deliverables. | Completed |

## Statistics Correction

Sprint 2.2 reported in narrative that "22 verification attempts" were made. Some Verification rows reference multiple Source IDs (e.g., VR-008 covers SRC-008+012+036; VR-013 covers SRC-003+050; VR-012 covers SRC-013). The correct statistics are:

- **Verification attempts: 22**
- **Unique verification IDs: 22** (VR-001 through VR-022)
- **Unique source IDs attempted: 24** (because some VR rows span multiple Source IDs)
- **Repeated source IDs: none**

The Attempt count (22) and Source count (24) are **distinct reporting dimensions**. They must not be conflated.

## Acceptance Criteria

- All six EV-### entries recorded in `verification-log.md` with the 8-field schema.
- All six source rows upgraded in `source-register.md` with EV-### citations in the Notes column.
- `source-register.md` v0.5 status set to "Draft (post Sprint 2.1 evidence correction; Sprint 2.2 verification attempted; Sprint 2.3 external verification reconciliation)".
- Sprint 2.2 statistics corrected and explained.
- Cross-references updated in inventory.md, candidate-projects.md, reverse-research.md.
- This task file created with all required sections.
- `CHANGELOG.md` and `research/README.md` updated.
- No new Source IDs; no renumbering; no Coverage Map / Gap Analysis / Positioning Evidence / Feature Matrix / Lifecycle Coverage Matrix / APES positioning conclusions.
- No auto-commit or push.

## Verification

- `git status` clean (no auto-commit performed in this sprint).
- 6 EV rows present in `verification-log.md` External Verification Reconciliation section.
- 6 source rows marked `Verified` in `source-register.md`.
- Sprint 2.2 statistics box shows: 22 / 22 / 24 / 0.
- Cross-references in inventory.md, candidate-projects.md, reverse-research.md all reference the Sprint 2.3 task file.

## Remaining Limitations

- The 22 Sprint 2.2 Inaccessible verification attempts remain `Inaccessible`; no source was downgraded or upgraded by Sprint 2.2 alone.
- For SRC-044 and SRC-045, only abstract/metadata is verified; full method details remain `Partially Verified` (PDF body not directly read).
- For SRC-006 (ISO/IEC/IEEE 12207:2026), only metadata is verified; the full standard text is paywalled and remains inaccessible.
- For SRC-003 (NIST SSDF), only the official summary is verified; the full document remains `Partially Verified`.
- APES does not adjudicate the conflict between SRC-044 and SRC-045; both are preserved verbatim.
- The Research Gate remains `RESEARCH AGAIN`; Sprint 2 remains `In Review`. The 10-condition rule was met for these six sources only because an external reviewer with direct primary-source access performed the verification.

## Status

Completed (2026-08-03).