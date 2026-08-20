# Sprint 02.4 — Targeted Primary-Source Re-verification

- Status: Completed
- Sprint: 2.4
- Owner: APES Maintainers
- Last Updated: 2026-08-15
- Purpose: Re-verify twelve targeted Source Register claims through direct access to canonical primary pages, synchronize only the approved research artifacts, and evaluate the Research Gate without optimizing for a passing result.

## Table of Contents

- [Scope](#scope)
- [Out of Scope](#out-of-scope)
- [Subtasks](#subtasks)
- [Verification](#verification)
- [Research Gate](#research-gate)
- [Open Questions](#open-questions)
- [Sprint Status](#sprint-status)

## Scope

- Directly inspect the canonical repository, README, LICENSE file, and recent commit or release / official maintenance notice for seven P0 repositories: SRC-017, SRC-018, SRC-019, SRC-020, SRC-021, SRC-022, and SRC-024.
- Directly inspect the specific official claims flagged for five P1 sources: SRC-002, SRC-004, SRC-005, SRC-014, and SRC-027.
- Append VR-023 through VR-034 to `research/notes/verification-log.md` using the existing 11-field schema and actual access date 2026-08-15.
- Change only the targeted Source Register rows' Claim Verification, Key Evidence, Notes, and Limitations fields; advance `research/source-register.md` to v0.7 and update its Last Updated date.
- Synchronize verification outcomes in `research/ecosystem/inventory.md`, `research/competitors/candidate-projects.md`, `research/competitors/reverse-research.md`, and `research/README.md`.
- Register this sprint in `tasks/README.md` and add its change record under `[Unreleased]` in `CHANGELOG.md`.

## Out of Scope

- Phase C Gap Analysis and Phase D Positioning Evidence.
- Any `standards/` body text, template, checklist, command, or implementation artifact.
- The APES-Validator repository, `schemas/`, F2 files, or any sibling repository.
- New or renumbered Source IDs, candidate expansion, re-ranking, or deletion.
- New ADRs or RFCs. Potential policy decisions are recorded only under Open Questions.
- File moves/deletions, dependency changes, publishing, flashing, Git commit, push, or tag operations.

## Subtasks

| # | Subtask | Status |
|---:|---|---|
| 1 | Read `AGENTS.md`, check the worktree, and read the relevant existing research/task files. | Completed |
| 2 | Directly verify the seven P0 repositories at README, LICENSE, and maintenance-signal level. | Completed |
| 3 | Directly verify the five P1 official sources and narrow any contradicted or overbroad claim. | Completed |
| 4 | Append VR-023 through VR-034 without altering Sprint 2.2 or Sprint 2.3 records. | Completed |
| 5 | Update the twelve related Source Register rows without adding or renumbering a Source ID. | Completed |
| 6 | Synchronize the approved inventory, candidate, reverse-research, and research-index files. | Completed |
| 7 | Compute the gate from the checked-in repository baseline and record unresolved discrepancies. | Completed |
| 8 | Run diff, source-count, ID-integrity, VR-schema, Markdown-link, and table-of-contents checks. | Completed |

### Claim Verification Changes

| Source | Before | After | Direct evidence used |
|---|---|---|---|
| SRC-002 | Partially Verified | Verified | Canonical Cognitect page: Michael Nygard, 2011-11-15, Title plus Context / Decision / Status / Consequences, CC0 waiver. |
| SRC-004 | Partially Verified | Verified | Official SAMM model/release pages and canonical repository: Version 2.0, model structure, CC BY-SA 4.0, 2026-07-06 activity. |
| SRC-005 | Partially Verified | Verified | Official OWASP page: current stable 5.0.0 released 2025-05-30 and historical 4.0.3 release on 2021-10-28. |
| SRC-014 | Unverified | Verified | Official Claude Code overview and memory docs: positioning, feature surface, native `CLAUDE.md`, optional AGENTS.md import/copy/symlink behavior. |
| SRC-017 | Partially Verified | Verified | aider repository README, Apache-2.0 `LICENSE.txt`, latest observed `main` commit 2026-05-22. |
| SRC-018 | Partially Verified | Verified | Cline README, Apache-2.0 `LICENSE`, latest observed commit/release 2026-08-14. |
| SRC-019 | Partially Verified | Verified | Redirect to `OpenHands/OpenHands`, current Agent Canvas README positioning, MIT `LICENSE`, 2026-08-14 activity. |
| SRC-020 | Partially Verified | Verified | OpenCode README move notice, MIT `LICENSE`, archive state, latest observed `main` commit 2025-09-18. |
| SRC-021 | Partially Verified | Verified | Continue README and read-only notice, Apache-2.0 `LICENSE`, final v2.0.0 release 2026-06-19. |
| SRC-022 | Partially Verified | Verified | Roo Code README shutdown notice, Apache-2.0 `LICENSE`, archive state, 2026-05-15 commit/release. |
| SRC-024 | Partially Verified | Verified | Gemini CLI README, Apache-2.0 `LICENSE`, 2026-08-13 commit and 2026-08-11 release. |
| SRC-027 | Unverified | Verified | Current MCP specification 2026-07-28, versioning/history pages, canonical transitional LICENSE, 2026-08-14 repository activity. |

### Maintenance Findings

- Active at access date (2026-08-15): aider, Cline, OpenHands / Agent Canvas, Gemini CLI, OWASP SAMM, and MCP.
- Archived at access date (2026-08-15): OpenCode and Roo Code.
- Read-only / no longer actively maintained at access date (2026-08-15): Continue.
- Dynamic popularity, commit-total, and release-total counts are deliberately omitted.

## Verification

| Check | Command / Method | Result |
|---|---|---|
| Worktree scope and whitespace | `git status --short`; `git diff --check`; `git diff --name-only` | Passed — eight tracked files modified, one allowed task file untracked, no whitespace errors |
| Source counts | Parse Source Register rows and group the Claim Verification field | Passed — Verified=22, Partially Verified=22, Unverified=10, total=54 |
| Source ID integrity | Confirm 54 unique IDs, range SRC-001 through SRC-054, no duplicates or gaps | Passed — 54 unique contiguous IDs |
| New verification records | Confirm VR-023 through VR-034 are each present once and contain all 11 fields | Passed — 12 records, 11 required fields each, all Access Date 2026-08-15 and Outcome Verified |
| Historical preservation | Compare the pre-Sprint-2.4 portion of `verification-log.md` against `HEAD` | Passed — diff numstat reports zero deleted lines; Sprint 2.4 is append-only |
| Markdown links | Resolve every relative Markdown link in the nine changed Markdown files | Passed — no broken relative link |
| Table of contents | Compare explicit TOC anchors with headings in files that have a TOC | Passed — all explicit TOC anchors resolve |
| Markdown tables | Check consistent pipe counts within each table block in the nine changed Markdown files | Passed |
| Scope | Confirm every changed path is in the Sprint 2.4 allowlist | Passed — exactly nine allowed paths; no out-of-scope path |

## Research Gate

### Auditable Baseline and Result

The task brief states 60 total sources with 16 Verified, 32 Partially Verified, and 12 Unverified. The checked-in `research/source-register.md` v0.6 instead contains 54 Source IDs (SRC-001 through SRC-054) with this baseline: Verified=10, Partially Verified=32, Unverified=12. This sprint uses the checked-in file as the auditable baseline and does not create SRC-055 through SRC-060.

| Metric | Before Sprint 2.4 | After Sprint 2.4 | Change |
|---|---:|---:|---:|
| Total Source IDs | 54 | 54 | 0 |
| Verified | 10 | 22 | +12 |
| Partially Verified | 32 | 22 | -10 |
| Unverified | 12 | 10 | -2 |
| Contradicted | 0 | 0 | 0 |
| Inaccessible (Source Register status) | 0 | 0 | 0 |

### Directly Verified Project Count

A conservative repository/project-only rule is used. It excludes the five P1 items from the project total even though their specific claims are Verified.

- Six previously direct-verified projects: SRC-001, SRC-015, SRC-025, SRC-026, SRC-053, SRC-054.
- Seven newly direct-verified P0 repositories: SRC-017, SRC-018, SRC-019, SRC-020, SRC-021, SRC-022, SRC-024.
- Total: **13 unique directly verified projects**.

### Determination

**`READY FOR REVIEW`**

- Verified source threshold: 22 ≥ 15 — met.
- Directly verified project threshold: 13 ≥ 8 — met under the conservative repository/project-only count.
- Source ID integrity: no Source ID added, removed, or renumbered.
- Sprint 2 remains `In Review`; this gate result requests maintainer review and is not acceptance of the research conclusions.

### Sources Still Requiring Direct Primary-Source Verification

- Partially Verified (22): SRC-007, SRC-008, SRC-009, SRC-010, SRC-011, SRC-012, SRC-013, SRC-023, SRC-028, SRC-029, SRC-030, SRC-031, SRC-035, SRC-036, SRC-037, SRC-038, SRC-039, SRC-040, SRC-049, SRC-050, SRC-051, SRC-052.
- Unverified (10): SRC-016, SRC-032, SRC-033, SRC-034, SRC-041, SRC-042, SRC-043, SRC-046, SRC-047, SRC-048.

## Open Questions

1. **Baseline reconciliation:** Which six sources or reconciliation changes were assumed by the task brief's 60/16/32/12 baseline? The repository currently ends at SRC-054. No ID is inferred or backfilled in this sprint.
2. **Gate wording:** Sprint 2.2 used “Selected projects,” while the Sprint 2.4 brief explicitly designates seven P0 repositories as raising the project count. This sprint applies the current brief with a conservative repository/project-only set of 13. Maintainers should confirm this interpretation before accepting the gate.
3. **Candidate maintenance states:** Should OpenCode and Roo Code move based on archive status, and should Continue move based on its read-only notice? Sprint 2.4 records the evidence but leaves candidate placement unchanged.
4. **OpenHands identity:** Should the Source Register title/publisher/URL fields be updated in a later approved sprint to reflect the redirect from `All-Hands-AI/OpenHands` to `OpenHands/OpenHands` and the Agent Canvas positioning? Those fields were outside this sprint's permitted Source Register edits.

## Sprint Status

Completed (2026-08-15) — direct evidence, synchronization, gate calculation, and repository verification are complete. Sprint 2 remains `In Review` pending maintainer review. Phase C and Phase D remain unstarted.
