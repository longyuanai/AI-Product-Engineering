# Sprint 02.2 — Primary Source Verification

- Status: In Review
- Version: v0.1
- Owner: APES Maintainers
- Last Updated: 2026-08-03

> **This sprint is verification-only.** Per §2 of the brief: "Reduce uncertainty before increasing scope." It explicitly does **not** enter Coverage Map, Gap Analysis, Positioning Evidence, or APES standard writing. The goal is to upgrade as many `Partially Verified` or `Unverified` rows in `research/source-register.md` to `Verified` as the access window allows, and to honestly record what could not be upgraded.

> **Sprint 2 status note.** Sprint 2 remains `In Review` per Sprint 2.1. Sprint 2.2 does not change that status; it attempts verification, not approval.

## Table of Contents

- [Sprint Goal](#sprint-goal)
- [Scope](#scope)
- [Out of Scope](#out-of-scope)
- [Tasks](#tasks)
- [Acceptance Criteria](#acceptance-criteria)
- [Verification Log](#verification-log)
- [Source ID Integrity Audit](#source-id-integrity-audit)
- [Research Gate](#research-gate)
- [Final Status](#final-status)
- [Notes](#notes)

## Sprint Goal

Run direct primary-source verification on the P0 sources identified by Sprint 2 / 2.1: AGENTS.md (SRC-001), Claude Code (SRC-014), OpenAI Codex CLI (SRC-015), MCP (SRC-027), GitHub Spec Kit (SRC-025), OpenSpec (SRC-026), ADR (Nygard, SRC-002), the two arXiv papers (SRC-044, SRC-045), the Selected core projects in the short list (S-01 through S-10), at least 2 Product Discovery methods, and at least 2 Engineering / Governance standards.

Record every attempt in `research/notes/verification-log.md` with the 11-field schema. A source is upgraded to `Verified` only when all 10 conditions in the brief are met.

If insufficient sources can be directly verified, the Research Gate must be `RESEARCH AGAIN` per §15.

## Scope

In scope:

- Direct WebFetch attempts on all P0 source URLs (per brief §3–§10).
- Honest recording of every attempt (Access Result, Evidence Location, Outcome).
- Source ID integrity audit (no silent overwrites; migration table if any Source ID is renumbered).
- Statistics recomputation in `research/source-register.md` after verification attempts.
- This task file (`tasks/sprint-02-2-primary-source-verification.md`).
- The verification log (`research/notes/verification-log.md`).
- Incremental updates to `research/README.md` and `CHANGELOG.md` reflecting the new sprint.

## Out of Scope

The following are explicitly forbidden in this sprint and were **not** attempted:

- Adding more than 5 non-essential sources (only re-verification of existing sources).
- Re-expanding the candidate project scope.
- Starting Coverage Map (Phase B).
- Starting Feature Matrix.
- Starting Lifecycle Coverage Matrix.
- Starting Gap Analysis (Phase C).
- Producing APES positioning conclusions (Phase D).
- Writing any formal Standard module.
- Modifying project positioning.
- Auto-committing or auto-pushing.
- Marking a source `Verified` from a search-result snippet.
- Marking a source `Verified` solely because the issuer is authoritative.
- Overwriting or duplicating any Source ID.
- Falsifying access success.
- Saving copyrighted full-text.

## Tasks

- [x] Pre-execution checks: confirm working directory, read all required context files (research-plan.md, source-register.md, inventory.md, candidate-projects.md, reverse-research.md, search-log.md, sprint-02-ecosystem-inventory.md, sprint-02-1-evidence-correction.md, research/README.md, CHANGELOG.md), record `git status`.
- [x] Attempt direct WebFetch on all P0 source URLs in §3–§10 of the brief.
- [x] Record each attempt in `research/notes/verification-log.md` using the 11-field schema (VR-NNN, Source ID, Original URL, Access Date, Access Result, Claims Checked, Evidence Location, License Checked, Maintenance Checked, Outcome, Notes).
- [x] Source ID integrity audit: confirm no Source ID was overwritten or duplicated; record migration table if any renumbering occurred (none in this sprint).
- [x] Update `research/source-register.md` with verification outcomes (preserving existing Claim Verification status; recording new `Inaccessible` entries where applicable; recomputing statistics).
- [x] Update `research/ecosystem/inventory.md` Verification Status column where the underlying Source Register row changed status.
- [x] Update `research/competitors/candidate-projects.md` and `research/competitors/reverse-research.md` with verification references where applicable (no semantic change to project content).
- [x] Update `research/README.md` to point to the new verification log.
- [x] Update `CHANGELOG.md` Unreleased section with a Sprint 2.2 entry.
- [x] Recompute statistics: Verified / Partially Verified / Unverified / Contradicted / Inaccessible counts.
- [x] Determine Research Gate (READY FOR REVIEW or RESEARCH AGAIN).
- [x] Run final structural and consistency checks.

## Acceptance Criteria

- `research/notes/verification-log.md` exists; every row uses the 11-field schema.
- Every P0 source listed in §3–§10 of the brief has at least one `VR-NNN` row in the log.
- No source is marked `Verified` unless all 10 conditions in the brief are met (direct page access, title match, publisher / author confirmation, evidence location, date in page, license from LICENSE/metadata/official notice, maintenance from Release/Tag/Commit/notice, etc.).
- The Source ID column in `research/source-register.md` is unchanged. If any Source ID was renumbered, a migration table appears here mapping old → new.
- No `Inaccessible` row is recorded as `Verified` or as a successful pass-through.
- Statistics recomputation is visible: previous Verified / Partially Verified / Unverified counts vs. new counts.
- Research Gate is one of `READY FOR REVIEW` (≥15 Verified + ≥8 projects + no Source ID conflicts) or `RESEARCH AGAIN` (the fallback per §15).
- No Coverage Map, Feature Matrix, Lifecycle Coverage Matrix, Gap Analysis, or APES positioning conclusion is produced.
- No file outside the allowed list (CHANGELOG.md, research/README.md, research/source-register.md, research/ecosystem/inventory.md, research/competitors/candidate-projects.md, research/competitors/reverse-research.md, research/notes/verification-log.md, this task file) was modified.
- No git commit, push, tag, or branch creation was performed.

## Verification Log

The log is at `research/notes/verification-log.md` (separate file). 22 attempts are recorded: VR-001 through VR-022. Every attempt resulted in `Inaccessible` because the access window (2026-08-03) blocks direct WebFetch on `arxiv.org`, `github.com`, `agents.md`, `anthropic.com`, `docs.claude.com`, `iso.org`, `csrc.nist.gov`, `owaspsamm.org`, `owasp.org`, `cognitect.com`, and `producttalk.org`. Several additional vendor / publisher sites (svpg.com, basecamp.com, theleanstartup.com, dora.dev, sre.google) were not probed in this sprint and are marked `Not probed in Sprint 2.2`.

### Aggregate Outcome

| Outcome | Count |
|---|---|
| `Verified` | **0** |
| `Partially Verified` (newly upgraded) | **0** |
| `Unverified` (newly assigned) | **0** |
| `Contradicted` | **0** |
| `Inaccessible` | **22** |
| **Total attempts** | **22** |

No source was upgraded to `Verified` during Sprint 2.2.

## Source ID Integrity Audit

Per brief §14: **"Source ID integrity check: if any Source ID is renumbered, a migration table must be added; otherwise state explicitly that no Source IDs were renumbered."**

**No Source ID was renumbered during Sprint 2.2.** The 52 Source IDs (SRC-001 through SRC-052) in `research/source-register.md` remain identical to the v0.3 schema produced by Sprint 2.1. No new Source IDs were added (per the §14 constraint that new IDs require a migration entry — none was needed because no new IDs were created).

Verification attempts reference existing Source IDs only. No two `VR-NNN` rows refer to the same `SRC-NNN` row. The mapping is one-to-many (`SRC-NNN` can have multiple verification attempts — e.g., SRC-006 and SRC-052 share the ISO 12207 identity but are separate entries).

## Research Gate

Per brief §15:

> **The Research Gate for this sprint must be one of:**
> - **`READY FOR REVIEW`** — if at least 15 sources can be upgraded to `Verified`, at least 8 Selected projects are directly verified, and there are no Source ID conflicts; OR
> - **`RESEARCH AGAIN`** — if direct access to sufficient original sources is not achievable.

### Gate Evaluation

| Required condition | Status |
|---|---|
| ≥15 sources upgraded to `Verified` | **NOT MET** (0 upgraded) |
| ≥8 Selected projects directly verified | **NOT MET** (0 directly verified) |
| No Source ID conflicts | **MET** (no renumbering) |

### Gate Decision

**`RESEARCH AGAIN`**

The access window of 2026-08-03 blocks direct WebFetch on every priority primary domain (`arxiv.org`, `github.com`, `agents.md`, `anthropic.com`, `docs.claude.com`, `iso.org`, `csrc.nist.gov`, `owaspsamm.org`, `owasp.org`, `cognitect.com`, `producttalk.org`). No source could be upgraded to `Verified`. The 10-condition rule from the brief could not be met for any priority source. Per §15:

> "若无法直接访问足够原始来源: 不得伪造通过; Sprint 2 保持 In Review; 最终结论输出 RESEARCH AGAIN; 明确列出需要由其他具备网络访问能力的研究者验证的来源."

Sprint 2 remains `In Review`. The verification log explicitly lists the sources requiring external verification (VR-001 through VR-022 with `Inaccessible` outcomes; especially **VR-022 (SRC-045 arXiv 2601.20404)** which has no community corroboration and must be existence-checked by an external verifier before the next sprint).

## Final Status

**In Review.** Sprint 2.2 produced the verification log and updated the source-register, inventory, candidates, and reverse-research files with the honest `Inaccessible` outcomes. No source was upgraded. The Research Gate is `RESEARCH AGAIN`. No git operations were performed. No file outside the allowed list was modified.

### Items left intentionally open

- All 22 priority sources require external verification.
- SRC-045 (arXiv 2601.20404) is flagged for an existence check; if the paper does not exist, SRC-045 must be retracted from the source register in a subsequent sprint (not silently retained).
- The next sprint should resume verification under an access environment that permits direct primary page retrieval.

## Notes

- WebSearch was used as a fallback channel to record what was observable about each source without opening the canonical primary page. Per §15, no search snippet was treated as a `Verified` basis.
- The 10-condition rule for upgrading to `Verified` is intentionally strict. It exists to prevent the same kind of "marketing copy as evidence" pattern Sprint 2.1 corrected. The conditions are: (1) direct page access; (2) title match; (3) publisher / author confirmation; (4) evidence location; (5) date in page; (6) license from LICENSE / metadata / official notice; (7) maintenance from Release / Tag / Commit / official notice; plus the structural conditions on claim type and source reliability. No priority source met all 10 in this access window.
- The `Inaccessible` outcome is the honest and expected result of the access window's restrictions. It is not a failure of methodology; it is the methodology producing the correct verdict under constrained access.

## Cross-References

- `research/notes/verification-log.md` — every verification attempt with the 11-field schema.
- `research/source-register.md` — the 52 sources with verification outcomes preserved.
- `research/ecosystem/inventory.md` — descriptive catalog using these sources.
- `research/competitors/candidate-projects.md` — Selected list.
- `research/competitors/reverse-research.md` — Selected projects analyzed using the 14-section template.
- `research/notes/search-log.md` — Sprint 2 search log (31 searches).
- `tasks/sprint-02-ecosystem-inventory.md` — Sprint 2 task file.
- `tasks/sprint-02-1-evidence-correction.md` — Sprint 2.1 task file.
- `CHANGELOG.md` — Unreleased entry added for Sprint 2.2.
- `research/README.md` — pointer to the verification log added.
