# research/competitors/candidate-projects.md

- Status: Draft
- Version: v0.4
- Owner: APES Maintainers
- Last Updated: 2026-08-15
- Purpose: Apply Sprint 1's Candidate Selection Criteria (Appendix C of `research/research-plan.md`) to the inventory in `research/ecosystem/inventory.md`. List the **long list** of candidates, document the **short list** that advances to reverse research, and record explicit defer / decline reasons for the rest. No APES positioning conclusions are drawn here.

## Candidate Selection Criteria (Recap)

The criteria below mirror Appendix C of the research plan. They are applied **consistently and only** — no project is dropped for reasons outside this list.

### Inclusion (must hold)

1. The project has a primary public source (repo / vendor doc / publisher page) that exists and is either reachable or independently corroborated during this access window.
2. The project has a discernible scope: a defined set of features, stages, or standards it aims to cover. (This is observable; this file does **not** decide whether that scope is "good enough.")
3. The project is current enough to be informative — not abandoned before 2024 unless used as a **decline case** (see Decline Cases below).

### Exclusion (any one disqualifies)

1. The project has only marketing copy and no observable primary documentation.
2. The project's only available source is a third-party review that quotes marketing copy.
3. The project has no discernible boundary of scope (i.e., it is impossible to describe what it does and does not cover without speculation).
4. The project is deprecated, sunset, or replaced before 2024 with no successor artifact. (Such cases are recorded separately under Decline Cases, not dropped silently.)
5. The primary source is fully paywalled and no legally open alternative exists.

### Decline Case Recording

A "Decline" is not the same as a deletion. The reasons a project is declined are recorded explicitly so future sprints can revisit the decision if new sources become available.

---

## Sprint 2.2 Verification Note (2026-08-03)

Direct primary-source verification was attempted for every Selected project (S-01 through S-10) and most held candidates. Per the access-window restrictions (see `research/notes/verification-log.md`), no Selected project could be directly verified. The 10-condition rule for upgrading to `Verified` was not met for any entry. The short list, long list, defer/decline reasons, and held-candidate inventory below are **unchanged** from Sprint 2.1; no project was added, removed, or re-ranked. No Source ID was renumbered.

## Sprint 2.3 External Verification Reconciliation (2026-08-03)

Six sources were upgraded from `Partially Verified` to `Verified` in `research/source-register.md` based on external-verification evidence (EV-001 through EV-006). The Selected list and Short List below are unchanged in structure — no project was added, removed, or re-ranked. The change here is that the underlying Source Register row has been upgraded for the entries whose claims were verified by EV-001 through EV-006:

- **SRC-001 (AGENTS.md)** — affects S-10. Page content and official self-positioning now `Verified` (per EV-001). 60k+ adoption figure is project-maintainer-reported, not independent market share.
- **SRC-015 (OpenAI Codex CLI)** — affects the held candidates cluster (OpenAI Codex CLI). Repo existence, Apache-2.0 License, README positioning, and active maintenance now `Verified` (per EV-002).
- **SRC-044 / SRC-045 (arXiv)** — affects S-10. Both papers' existence, title, authors, dates, and abstract content now `Verified` (per EV-003 / EV-004). Method details remain `Partially Verified`. Conflicts preserved verbatim; APES does not adjudicate.
- **SRC-003 (NIST SSDF)** — affects the held candidates cluster (standards). Now `Verified` for number, version, date, authors, official summary (per EV-006).
- **SRC-006 (ISO/IEC/IEEE 12207:2026)** — affects the held candidates cluster (standards). Now `Verified` for number, title, edition, publication date, Published status (per EV-005). Full text remains paywalled.

Sprint 2 still `In Review`.

## Sprint 2.4 Targeted Primary-Source Re-verification (2026-08-15)

Sprint 2.4 directly accessed the canonical primary pages for twelve sources. This is a verification-only reconciliation: the Long List, Final Short List, held/decline placement, and ranking are not changed.

| Source | Project / Artifact | Before | After | Directly observed state at 2026-08-15 |
|---|---|---|---|---|
| SRC-002 | ADR (Nygard) | Partially Verified | Verified | Author, 2011-11-15 date, Title plus four body sections, and CC0 waiver observed. |
| SRC-004 | OWASP SAMM v2 | Partially Verified | Verified | Version 2.0, model structure, CC BY-SA 4.0, and 2026-07-06 repository activity observed; Active at access date. |
| SRC-005 | OWASP ASVS | Partially Verified | Verified | Current stable 5.0.0 released 2025-05-30; historical 4.0.3 release dated 2021-10-28. |
| SRC-014 | Claude Code | Unverified | Verified | Official positioning and feature documentation observed; `CLAUDE.md` is read by default, while `AGENTS.md` requires import, copy, or symlink handling. |
| SRC-017 | aider | Partially Verified | Verified | README, Apache-2.0 `LICENSE.txt`, and recent commit evidence observed; Active at access date. |
| SRC-018 | Cline | Partially Verified | Verified | README, Apache-2.0 `LICENSE`, and 2026-08-14 commit/release evidence observed; Active at access date. |
| SRC-019 | OpenHands / Agent Canvas | Partially Verified | Verified | Requested path redirects to `OpenHands/OpenHands`; current positioning, MIT `LICENSE`, and 2026-08 activity observed; Active at access date. |
| SRC-020 | OpenCode | Partially Verified | Verified | README move notice, MIT `LICENSE`, and archive state observed; Archived at access date. |
| SRC-021 | Continue | Partially Verified | Verified | README, Apache-2.0 `LICENSE`, final release, and official read-only notice observed; no longer actively maintained. |
| SRC-022 | Roo Code | Partially Verified | Verified | README shutdown notice, Apache-2.0 `LICENSE`, and archive state observed; Archived at access date. |
| SRC-024 | Gemini CLI | Partially Verified | Verified | README, Apache-2.0 `LICENSE`, and 2026-08 commit/release evidence observed; Active at access date. |
| SRC-027 | MCP | Unverified | Verified | Current 2026-07-28 specification, version history, transitional license notice, and recent repository activity observed; Active at access date. |

The newly observed archive/read-only states may justify a later selection-policy review, but Sprint 2.4 does not unilaterally re-rank or move candidates. Under a conservative repository/project-only count, 13 projects are directly verified (six prior projects plus the seven P0 repositories; the five P1 items are excluded from this count), so the Research Gate is `READY FOR REVIEW`; Sprint 2 remains `In Review` pending maintainer review.

---

## Long List (Inspected)

Each long-list row states: project / author / inventory code / inspection status.

| # | Project / Artifact | Author / Maintainer | Inventory Code | Inspection Status |
|---|---|---|---|---|
| 1 | Continuous Discovery (book) | Teresa Torres / Product Talk | C1 | Selected |
| 2 | Inspired (book) | Marty Cagan / SVPG | C1 | Selected |
| 3 | Lean Startup (book) | Eric Ries | C1 | Deferred (covered by other discovery literature) |
| 4 | Shape Up (book + online) | Basecamp / Ryan Singer | C1 | Selected |
| 5 | Dual-Track Development | HPI community / various | C1 | Deferred (term captured in C1 rows; no single artifact to reverse) |
| 6 | Lean Canvas | Ash Maurya | C8 | Selected |
| 7 | Business Model Canvas | Alexander Osterwalder | C8 | Selected |
| 8 | Value Proposition Canvas | Osterwalder et al. | C8 | Deferred (covered by BMC row) |
| 9 | Jobs to Be Done (theory) | Christensen / Ulwick | C2 | Selected |
| 10 | Outcome-Driven Innovation | Tony Ulwick / Strategyn | C2 | Selected |
| 11 | ADR (Nygard template) | Michael Nygard | C3 | Selected |
| 12 | MADR (Markdown ADR) | Oliver Kopp et al. | C3 | Deferred (variant; covered by ADR row) |
| 13 | OpenSpec | Fission-AI | C3, C5 | Selected |
| 14 | Spec Kit | GitHub | C3, C5 | Selected |
| 15 | Claude Code | Anthropic | C6 | Selected |
| 16 | OpenAI Codex CLI | OpenAI | C6 | Selected |
| 17 | Cursor | Anysphere | C6 | Selected |
| 18 | aider | Paul Gauthier (Aider-AI) | C6 | Selected |
| 19 | Cline | cline/cline | C6 | Selected |
| 20 | OpenHands | All-Hands-AI | C6 | Selected |
| 21 | OpenCode | opencode-ai | C6 | Deferred (overlap with Codex CLI/Claude Code; covered by Selected peers) |
| 22 | Continue | continuedev | C6 | Deferred (overlap with Cline / Roo Code; covered by Selected peers) |
| 23 | Roo Code | RooCodeInc | C6 | Deferred (Cline fork lineage; covered by Cline row) |
| 24 | GitHub Copilot | GitHub / Microsoft | C6 | Selected |
| 25 | Gemini CLI | Google | C6 | Selected |
| 26 | Sourcegraph Cody | Sourcegraph | C6 | Declined (effective maintenance freeze 2025) |
| 27 | Model Context Protocol (MCP) | Anthropic / community | C9 | Selected |
| 28 | LangGraph | LangChain | C9 | Selected |
| 29 | AutoGen | Microsoft Research | C9 | Selected |
| 30 | Microsoft Agent Framework | Microsoft | C9 | Selected |
| 31 | crewAI | crewAIInc | C9 | Selected |
| 32 | AGENTS.md | Open community | C5 | Selected (with counter-evidence from SRC-044 and SRC-045) |
| 33 | NIST SSDF (SP 800-218) | NIST | C4, C7 | Selected |
| 34 | OWASP SAMM v2 | OWASP | C4, C7 | Selected |
| 35 | OWASP ASVS v4 | OWASP | C4, C7 | Deferred (consumed by SSDF/SAMM for governance; no separate reverse-research need) |
| 36 | ISO/IEC/IEEE 12207 | ISO / IEEE | C7 | Selected |
| 37 | DORA / Accelerate | DORA / Google Cloud | C4 | Selected |
| 38 | SRE Book | Google | C4, C7 | Selected |
| 39 | DHS/CISA Software Attestation | DHS / CISA | C7 | Selected |
| 40 | Synopsys SSDF analysis | Synopsys | C7 | Deferred (industry adoption report; consumed by NIST SSDF row) |

---

## Short List (Selected for Reverse Research)

10 projects / artifacts advance to reverse research. They are deliberately distributed across the inventory so the reverse research draws on:

- **Discovery methods**: Continuous Discovery, Inspired, Shape Up, Lean Canvas, Business Model Canvas, JTBD (Christensen), ODI (Ulwick).
- **Decision / spec artifacts**: ADR (Nygard), OpenSpec, Spec Kit, AGENTS.md.
- **AI coding agents / orchestration**: Claude Code, OpenAI Codex CLI, Cursor, aider, Cline, OpenHands, GitHub Copilot, Gemini CLI, MCP, LangGraph, AutoGen, Microsoft Agent Framework, crewAI.
- **Standards / governance**: NIST SSDF, OWASP SAMM v2, ISO 12207, DORA, SRE Book, DHS/CISA Attestation.

### Final Short List (10)

| # | Selected Project / Artifact | Inventory Code | Rationale |
|---|---|---|---|
| S-01 | Continuous Discovery | C1 | Practitioner product-discovery methodology referenced widely in C1 / C2 / C5 inventory rows. |
| S-02 | Inspired (SVPG) | C1 | Practitioner product-team and discovery-team framing. |
| S-03 | Shape Up | C1 | Shaping / betting / building cycle with a free online version available. |
| S-04 | Jobs to Be Done — Christensen line | C2 | Foundational customer-research theory with broad reach. |
| S-05 | Outcome-Driven Innovation (Ulwick) | C2 | Operationally distinct JTBD variant; comparison exposes intra-JTBD disagreement. |
| S-06 | ADR (Nygard) | C3 | Canonical decision-capture template; widely emulated. |
| S-07 | OpenSpec | C3, C5 | AI-coding-era spec/plan artifact (open source). |
| S-08 | Spec Kit | C3, C5 | Vendor-led spec-driven development toolkit (GitHub, 2025). |
| S-09 | Claude Code | C6 | Vendor agentic CLI representing the CLI/agent branch. |
| S-10 | AGENTS.md convention | C5 | Open convention capturing the AGENTS.md rise **and** academic counter-evidence from SRC-044 (arXiv 2602.11988) and SRC-045 (arXiv 2601.20404) — which disagree on direction. |

### Additional Candidates Beyond the 10 (held in reserve for Sprint 3 if extended)

These candidates passed selection criteria but were not included in the 10 above to keep the Sprint 2 reverse-research scope focused. They are recorded here for traceability:

| Held Candidate | Inventory Code | Why Held |
|---|---|---|
| Lean Canvas | C8 | Captured by S-04 / S-05 for adjacent modeling; full reverse not strictly needed in Sprint 2. |
| BMC | C8 | Same as Lean Canvas. |
| NIST SSDF | C4, C7 | Important for governance, but Covered by the broader Sprint 2 reverse-research budget. Deferred to a standards-focused follow-up. |
| OWASP SAMM v2 | C4, C7 | Same as SSDF. |
| ISO 12207 | C7 | Same. |
| DORA / Accelerate | C4 | Same. |
| SRE Book | C4, C7 | Same. |
| DHS/CISA Software Attestation | C7 | Same. |
| Cursor / aider / Cline / OpenHands / GitHub Copilot / Gemini CLI | C6 | AI coding agents; one (Claude Code, S-09) selected as representative. Sprint 3 may add more. |
| MCP / LangGraph / AutoGen / Microsoft Agent Framework / crewAI | C9 | Multi-agent orchestration; deferred in Sprint 2. |
| OpenAI Codex CLI | C6 | Same representative-cluster deferral as Cursor/aider/Cline. |

The held candidates are **not** declined. They are deferred to a future sprint's reverse-research budget, which will be scoped independently.

---

## Decline Cases

| Project / Artifact | Inventory Code | Decline Reason |
|---|---|---|
| Sourcegraph Cody | C6 | Effective maintenance freeze mid-2025 (community snapshot evidence). Recorded for reference as a "what happens when AI coding tools are not maintained" case. Will not be advanced to reverse research. |
| OpenCode | C6 | Substantial overlap with Claude Code / Codex CLI in agentic-CLI scope. Excluded to avoid duplicate reverse-research findings; covered via S-09. |
| Continue | C6 | Overlap with Cline / Roo Code (VS Code AI extension lineage). Covered via S-09 / Cline notes. |
| Roo Code | C6 | Fork lineage from Cline. Covered via S-09 / Cline notes. |
| MADR (Markdown ADR) | C3 | Variant of ADR; covered by S-06 (Nygard). |
| OWASP ASVS v4 | C4, C7 | Verification-level standard; consumed by SSDF/SAMM for governance. Captured via standards-cluster deferral. |
| Synopsys SSDF analysis | C7 | Industry adoption report; consumed by NIST SSDF row. |
| Dual-Track Development | C1 | Term, not a single artifact; not reverse-researchable as a project. |
| Lean Startup | C1 | Older work; sufficiently covered by other discovery literature in the short list (S-01, S-03). |
| Value Proposition Canvas | C8 | Captured by S-04 / S-05 for adjacent modeling. |
| Windsurf / Devin / Zed / Replit Ghostwriter | — | Inspected but not included; see `research/ecosystem/inventory.md` §"Items Considered but Not Included". |

---

## Notes on Quality and Limits

- The 10 Selected entries span the four inventory clusters (discovery, decision artifacts, AI coding agents, standards/governance). One row (S-10, AGENTS.md) deliberately surfaces **two** academic studies with conflicting findings (SRC-044 and SRC-045) per the Sprint 2.1 brief.
- The AI-coding-agent cluster (C6) has only one representative in the final 10 (S-09, Claude Code). Sprint 3 may expand this without re-doing selection; the held candidates above are already pre-cleared.
- Per Sprint 2.1 corrections: license, first-release date, and maintenance status have been removed where not directly verified from a LICENSE file, Release, Tag, Commit, or official post. The Candidate Selection Criteria still apply: Inclusion requires a primary public source that exists and is either reachable or independently corroborated during the access window, even when those specific facts remain Unverified.
- No popularity, market share, or adoption ranking is recorded here. Such figures are deliberately omitted.
- No license-decision is implied by inclusion. License notes are kept at the source-register level.

## Cross-References

- `research/ecosystem/inventory.md` — items considered.
- `research/source-register.md` — sources cited in selection.
- `research/notes/verification-log.md` — Sprint 2.2 direct verification attempts (all `Inaccessible`).
- `research/competitors/reverse-research.md` — Selected projects analyzed using the 14-section template.
- `tasks/sprint-02-2-primary-source-verification.md` — Sprint 2.2 task file (Research Gate: `RESEARCH AGAIN`).
- `tasks/sprint-02-3-external-verification-reconciliation.md` — Sprint 2.3 task file (6 sources upgraded via external-verification evidence).
- `tasks/sprint-02-4-targeted-reverification.md` — Sprint 2.4 task file (12 direct primary-source upgrades; Research Gate: `READY FOR REVIEW`).
