# research/coverage/lifecycle-coverage-matrix.md

- Status: Draft
- Version: v0.1
- Owner: APES Maintainers
- Last Updated: 2026-08-03
- Purpose: Matrix view of the **Coverage Map** in `research/coverage/coverage-map.md`. Rows = the 10 Selected projects (S-01 through S-10). Columns = the 19 Sprint 3 lifecycle stages. Cell values describe observed lifecycle responsibility using a fixed scale. Every non-empty cell carries a **Source ID + Evidence Type + Confidence** triple.

## Cell Value Scale

- **Primary** — the project's process model explicitly places this stage at the center of its responsibility (e.g., the stage is named, described, and prescribed with steps or artifacts).
- **Secondary** — the project's process model explicitly touches this stage but treats it as a hand-off, boundary, or supporting activity rather than the focus.
- **Partial** — the project touches this stage in some artifacts or stated examples, but does not prescribe it as part of its process model.
- **None** — the project's `Scope (In / Out)` section in `research/competitors/reverse-research.md` §4 **explicitly excludes** this stage (e.g., "Out: security policy" gives Security=None). None is a **factual** statement that the project explicitly excludes the stage.
- **Unknown** — the project's reverse-research record did not address this stage. The stage may or may not be in scope; the evidence is insufficient to determine.

A cell value of **None** is a statement that the project's Scope Out section explicitly excludes the stage; it is **not** an APES evaluation of the project. A cell value of **Unknown** is a statement that the evidence trail in this access window did not surface coverage; it is **not** an assertion of absence and **not** an APES evaluation.

## Confidence Scale

- **High** — multiple corroborating sources, or a single `Verified` primary source (per Sprint 2.3 external verification where applicable).
- **Medium** — multi-source corroboration of publication / scope, but primary page not directly read in this access window.
- **Low** — only community / vendor-page-Not-Found evidence; primary source not reachable.

## Source ID Column

Every non-empty cell carries a parenthetical citation: `(SRC-NNN | Evidence Type | Confidence)`. Evidence Types follow the Source Register schema: Official self-description / Observable repository fact / Independent empirical evidence / Practitioner opinion / Community signal / Marketing claim. Full Source Register rows are in `research/source-register.md`; full evidence narratives are in `research/competitors/reverse-research.md` §S-01 through §S-10.

## Empty Cell Convention

A blank cell = `Unknown` (evidence insufficient in this access window). This is **not** an assertion of absence-of-coverage by APES; it is an observation that the evidence trail did not surface coverage. The cells where the project's `Scope Out` explicitly excludes the stage are filled with `None` according to the strict rule above.

---

## The Matrix

Show-value legend: **Pri** = Primary, **Sec** = Secondary, **Part** = Partial, **—** = Unknown (evidence insufficient), **N** = None (explicit Scope Out). Non-empty cells (Pri / Sec / Part / N) carry Source IDs in the Source-ID column and full evidence triples in the per-project Cell-Level Evidence tables below.

| Project (S-NN) | Idea | Discovery | Research | Requirements | Specification | Architecture | Planning | Implementation | Coding | Testing | Review | Documentation | Release | Operation | Maintenance | Knowledge Mgmt | Governance | Security | Continuous Improvement |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **S-01 Continuous Discovery** | — | Pri | Pri | — | — | — | — | N | — | — | — | — | — | — | — | — | — | N | — |
| **S-02 Inspired (SVPG)** | — | Pri | Sec | — | — | — | Pri | — | — | — | — | — | — | — | — | — | — | N | — |
| **S-03 Shape Up** | — | Pri | — | — | — | — | Pri | Pri | — | — | — | — | Pri | — | — | — | N | — | — |
| **S-04 JTBD (Christensen)** | — | Pri | Pri | Part | — | — | — | N | — | — | — | — | — | — | — | — | N | — | — |
| **S-05 ODI (Ulwick)** | — | Pri | Pri | — | — | — | Part | N | — | — | — | — | — | — | — | — | N | — | — |
| **S-06 ADR (Nygard)** | — | — | N | — | — | Pri | — | — | — | — | — | Pri | — | — | — | — | — | N | — |
| **S-07 OpenSpec** | — | — | — | — | Pri | — | Pri | Pri | — | — | Pri | Part | — | — | — | — | — | N | — |
| **S-08 Spec Kit** | — | — | — | — | Pri | — | Pri | Pri | — | — | Pri | Part | — | — | — | — | N | — | — |
| **S-09 Claude Code** | — | — | — | — | — | — | Pri | Pri | Part | — | — | — | — | — | — | — | N | N | — |
| **S-10 AGENTS.md** | — | — | — | — | — | — | — | Part | Part | — | — | — | — | — | — | — | — | N | — |

### Per-Cell Source ID Reference (Compact)

This compact table mirrors the matrix in Source ID form. Each non-empty cell lists the supporting Source IDs. Full Source ID + Evidence Type + Confidence triples appear in the per-project Cell-Level Evidence tables below.

| Project (S-NN) | Idea | Discovery | Research | Requirements | Specification | Architecture | Planning | Implementation | Coding | Testing | Review | Documentation | Release | Operation | Maintenance | Knowledge Mgmt | Governance | Security | Continuous Improvement |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **S-01** | — | SRC-008/012/036 | SRC-008/012/036 | — | — | — | — | §S-01 §4 Out | — | — | — | — | — | — | — | — | — | §S-01 §4 Out | — |
| **S-02** | — | SRC-009/035 | SRC-009/035 | — | — | — | SRC-009/035 | — | — | — | — | — | — | — | — | — | — | §S-02 §4 Out | — |
| **S-03** | — | SRC-011/037 | — | — | — | — | SRC-011/037 | SRC-011/037 | — | — | — | — | SRC-011/037 | — | — | — | §S-03 §4 Out | — | — |
| **S-04** | — | SRC-013/038 | SRC-013/038 | SRC-013/038 | — | — | — | §S-04 §4 Out | — | — | — | — | — | — | — | — | §S-04 §4 Out | — | — |
| **S-05** | — | SRC-013/038 | SRC-013/038 | — | — | — | SRC-013/038 | §S-05 §4 Out | — | — | — | — | — | — | — | — | §S-05 §4 Out | — | — |
| **S-06** | — | — | §S-06 §4 Out | — | — | SRC-002/040 | — | — | — | — | — | SRC-002/040 | — | — | — | — | — | §S-06 §4 Out | — |
| **S-07** | — | — | — | — | SRC-026 | — | SRC-026 | SRC-026 | — | — | SRC-026 | SRC-026 | — | — | — | — | — | §S-07 §4 Out | — |
| **S-08** | — | — | — | — | SRC-025 | — | SRC-025 | SRC-025 | — | — | SRC-025 | SRC-025 | — | — | — | — | §S-08 §4 Out | — | — |
| **S-09** | — | — | — | — | — | — | SRC-014 | SRC-014 | SRC-014 | — | — | — | — | — | — | — | §S-09 §4 Out | §S-09 §4 Out | — |
| **S-10** | — | — | — | — | — | — | — | SRC-001/044/045 | SRC-001/044/045 | — | — | — | — | — | — | — | — | §S-10 §4 Out | — |

---

## Cell-Level Evidence (Per Project, Per Non-Empty Cell)

The tables below expand every non-empty cell with the required **Source ID + Evidence Type + Confidence** triple.

### S-01. Continuous Discovery

| Lifecycle Stage | Cell Value | Source ID | Evidence Type | Confidence |
|---|---|---|---|---|
| Discovery | Primary | SRC-008, SRC-012, SRC-036 | Practitioner opinion (book + Product Talk templates) | Medium |
| Research | Primary | SRC-008, SRC-012, SRC-036 | Practitioner opinion | Medium |

### S-02. Inspired (SVPG)

| Lifecycle Stage | Cell Value | Source ID | Evidence Type | Confidence |
|---|---|---|---|---|
| Discovery | Primary | SRC-009, SRC-035 | Practitioner opinion (book + SVPG site content) | Medium |
| Research | Secondary | SRC-009, SRC-035 | Practitioner opinion | Medium |
| Planning | Primary | SRC-009, SRC-035 | Practitioner opinion | Medium |

### S-03. Shape Up

| Lifecycle Stage | Cell Value | Source ID | Evidence Type | Confidence |
|---|---|---|---|---|
| Discovery (Shaping) | Primary | SRC-011, SRC-037 | Practitioner opinion (free online book) | Medium |
| Planning (Betting) | Primary | SRC-011, SRC-037 | Practitioner opinion | Medium |
| Implementation (Build) | Primary | SRC-011, SRC-037 | Practitioner opinion | Medium |
| Release (Cool-down / ship) | Primary | SRC-011, SRC-037 | Practitioner opinion | Medium |

### S-04. JTBD (Christensen)

| Lifecycle Stage | Cell Value | Source ID | Evidence Type | Confidence |
|---|---|---|---|---|
| Discovery | Primary | SRC-013, SRC-038 | Practitioner opinion + academic theory | Medium |
| Research | Primary | SRC-013, SRC-038 | Practitioner opinion + academic theory | Medium |
| Requirements (Job Map) | Partial | SRC-013, SRC-038 | Practitioner opinion + academic theory | Medium |

### S-05. ODI (Ulwick)

| Lifecycle Stage | Cell Value | Source ID | Evidence Type | Confidence |
|---|---|---|---|---|
| Discovery | Primary | SRC-013, SRC-038 | Practitioner opinion + proprietary methodology | Medium |
| Research | Primary | SRC-013, SRC-038 | Practitioner opinion + proprietary methodology | Medium |
| Planning (prioritized roadmap input) | Partial | SRC-013, SRC-038 | Practitioner opinion + proprietary methodology | Medium |

### S-06. ADR (Nygard)

| Lifecycle Stage | Cell Value | Source ID | Evidence Type | Confidence |
|---|---|---|---|---|
| Architecture | Primary | SRC-002, SRC-040 | Practitioner convention + community tooling | Medium |
| Documentation | Primary | SRC-002, SRC-040 | Practitioner convention + community tooling | Medium |

> **Sprint 3.1 audit correction.** The original Sprint 3 confidence label was `High`. Per the matrix Confidence Scale, `High` requires multiple corroborating sources **or** a single `Verified` primary source. SRC-002 (Nygard blog) and SRC-040 (adr.github.io) are both `Partially Verified` in `research/source-register.md` v0.5 — neither was directly read in the 2026-08-03 access window, and the matrix's §S-13 Verification Notes record `Page Unverified` for both. Confidence downgraded from `High` to `Medium`. The cell value (`Primary`) is unchanged; only the confidence label is corrected.

### S-07. OpenSpec

| Lifecycle Stage | Cell Value | Source ID | Evidence Type | Confidence |
|---|---|---|---|---|
| Specification | Primary | SRC-026 | Observable repository fact | Medium |
| Planning (Change Proposal) | Primary | SRC-026 | Observable repository fact | Medium |
| Implementation (Implement step) | Primary | SRC-026 | Observable repository fact | Medium |
| Review | Primary | SRC-026 | Observable repository fact | Medium |
| Documentation (Update step) | Partial | SRC-026 | Observable repository fact | Medium |

### S-08. Spec Kit

| Lifecycle Stage | Cell Value | Source ID | Evidence Type | Confidence |
|---|---|---|---|---|
| Specification | Primary | SRC-025 | Observable repository fact | Medium |
| Planning (Change Proposal) | Primary | SRC-025 | Observable repository fact | Medium |
| Implementation (Implement step) | Primary | SRC-025 | Observable repository fact | Medium |
| Review | Primary | SRC-025 | Observable repository fact | Medium |
| Documentation (Update step) | Partial | SRC-025 | Observable repository fact | Medium |

### S-09. Claude Code

| Lifecycle Stage | Cell Value | Source ID | Evidence Type | Confidence |
|---|---|---|---|---|
| Planning (Plan mode artifacts) | Primary | SRC-014 | Vendor self-description | Low–Medium |
| Implementation (agentic CLI execution) | Primary | SRC-014 | Vendor self-description | Low–Medium |
| Coding | Partial | SRC-014 | Vendor self-description | Low–Medium |

### S-10. AGENTS.md

| Lifecycle Stage | Cell Value | Source ID | Evidence Type | Confidence |
|---|---|---|---|---|
| Implementation (agent context load) | Partial | SRC-001, SRC-044, SRC-045 | Official self-description + Independent empirical evidence | High (abstract level) |
| Coding (agent behavior modification) | Partial | SRC-001, SRC-044, SRC-045 | Official self-description + Independent empirical evidence | High (abstract level) |

**Note on S-10 conflicting evidence.** SRC-044 (Gloaguen et al., arXiv 2602.11988) and SRC-045 (Lulla et al., arXiv 2601.20404) disagree on the direction of AGENTS.md's effect on AI coding agents. Both are recorded as `Verified` at the abstract level (EV-003 / EV-004). The cell values above describe the **observed lifecycle responsibility of the AGENTS.md convention itself** (a consumer-side context file for AI agents), not the empirical effect on agents. APES does **not** adjudicate the empirical conflict. See `research/competitors/reverse-research.md` §S-10 §11.

---

## Aggregate Counts

### Primary Cells by Project

| Project | Primary Cells |
|---|---|
| S-01 Continuous Discovery | 2 (Discovery, Research) |
| S-02 Inspired (SVPG) | 2 (Discovery, Planning) |
| S-03 Shape Up | 4 (Discovery, Planning, Implementation, Release) |
| S-04 JTBD (Christensen) | 2 (Discovery, Research) |
| S-05 ODI (Ulwick) | 2 (Discovery, Research) |
| S-06 ADR (Nygard) | 2 (Architecture, Documentation) |
| S-07 OpenSpec | 4 (Specification, Planning, Implementation, Review) |
| S-08 Spec Kit | 4 (Specification, Planning, Implementation, Review) |
| S-09 Claude Code | 2 (Planning, Implementation) |
| S-10 AGENTS.md | 0 (only Partial cells) |
| **Total Primary cells** | **24** |

### Cell-Value Distribution Across All 10 × 19 = 190 Cells

| Cell Value | Count | % of 190 |
|---|---|---|
| Primary | 24 | 12.6% |
| Secondary | 1 | 0.5% |
| Partial | 7 | 3.7% |
| None | 15 | 7.9% |
| Unknown | 143 | 75.3% |
| **Total** | **190** | **100%** |

### Coverage Footprint Per Lifecycle Stage

| Lifecycle Stage | # Projects Touching (Primary + Secondary + Partial) |
|---|---|
| Idea | 0 |
| Discovery | 5 (S-01, S-02, S-03, S-04, S-05) |
| Research | 4 (S-01, S-02, S-04, S-05) |
| Requirements | 1 (S-04 Partial) |
| Specification | 2 (S-07, S-08) |
| Architecture | 1 (S-06) |
| Planning | 6 (S-02, S-03, S-05 Partial, S-07, S-08, S-09) |
| Implementation | 5 (S-03, S-07, S-08, S-09, S-10 Partial) |
| Coding | 2 (S-09 Partial, S-10 Partial) |
| Testing | 0 |
| Review | 2 (S-07, S-08) |
| Documentation | 3 (S-06, S-07 Partial, S-08 Partial) |
| Release | 1 (S-03) |
| Operation | 0 |
| Maintenance | 0 |
| Knowledge Management | 0 |
| Governance | 0 |
| Security | 0 |
| Continuous Improvement | 0 |

Note: counts are Primary + Secondary + Partial. The previously listed footnote ² on S-10 Planning was incorrect — S-10's Planning cell is `—` (Unknown), not Partial.

### Uncovered Stages (Across All 10 Selected Projects)

The following 19-stage cells have **zero** non-empty values across all 10 rows:

- **Idea** — none of the 10 Selected projects claim Idea-stage responsibility.
- **Testing** — none of the 10 Selected projects claim Testing-stage responsibility.
- **Operation** — none.
- **Maintenance** — none.
- **Knowledge Management** — none.
- **Governance** — none.
- **Security** — none.
- **Continuous Improvement** — none.

These are observations about the evidence trail; they are **not** APES gap claims or APES positioning.

---

## Interpretation Rules

1. **The matrix records observed lifecycle responsibility, not quality.** A project with a single Primary cell is not "worse" than a project with four Primary cells.
2. **A non-empty cell does not imply feature parity.** Two projects touching the same lifecycle stage may do so with very different artifact types, cadences, or scopes.
3. **A blank cell does not imply absence-of-coverage.** It means the evidence trail in `research/competitors/reverse-research.md` did not surface coverage for this project at this stage. Other sources may exist; they are out of scope for Sprint 3.
4. **The matrix does not assert APES relevance.** No row is annotated as "APES-relevant" or "APES-irrelevant".

---

## Audit Notes (Sprint 3.1, 2026-08-03)

Sprint 3.1 is an audit-only sprint. It re-derives cell values from the evidence trail, corrects any overclaims, and adjusts aggregate counts. No new research, no new sources, no new Gap Analysis, no new Positioning Evidence.

### Audit Finding — S-08 Security cell overclaim

The original Sprint 3 matrix recorded **S-08 Security=None** with the note "§S-08 §4 Out". This was an overclaim.

- **What S-08 §4 Out actually says**: "**Out**: full lifecycle governance, business modeling." (line 608-611 of `research/competitors/reverse-research.md`).
- **What it does NOT say**: "security policy", "security practice", or any explicit reference to Security.
- **Strict rule applied (per Cell Value Scale)**: None is reserved for stages **explicitly excluded** by §4 Out. "Full lifecycle governance" explicitly excludes Governance; it does not explicitly exclude Security.
- **Correction**: S-08 Security cell flipped from `N` to `—` (Unknown). The cell now reflects that the evidence trail in this access window did not surface Security coverage and the §4 Out does not explicitly exclude it.

### Re-derived Explicit None Cells (from §4 Out only)

The following 15 cells are **explicit** None, derived strictly from §4 Out:

| Project | None Cells (explicit §4 Out) | Source of exclusion |
|---|---|---|
| S-01 Continuous Discovery | Implementation, Security | "engineering implementation, security practices" |
| S-02 Inspired | Security | "security" |
| S-03 Shape Up | Governance | "formal engineering governance" |
| S-04 JTBD | Implementation, Governance | "engineering practice, governance" |
| S-05 ODI | Implementation, Governance | "engineering practice, governance" |
| S-06 ADR | Research, Security | "customer research, security policy" |
| S-07 OpenSpec | Security | "security policy" |
| S-08 Spec Kit | Governance | "full lifecycle governance" |
| S-09 Claude Code | Governance, Security | "full project lifecycle governance, security policy" |
| S-10 AGENTS.md | Security | "security policy" |
| **Total explicit None** | **15** | |

**Note on S-03 Discovery.** S-03 §4 Out originally read "Out: continuous customer touchpoints (compared with Continuous Discovery), formal engineering governance." The matrix originally assigned S-03 Discovery=None on this basis, but per the strict rule (None requires the §4 Out to explicitly name the stage), "continuous customer touchpoints" excludes a specific Continuous-Discovery-style weekly-contact practice, not the broader Discovery lifecycle stage. Shape Up's §6 explicitly prescribes Shaping as a Discovery-equivalent activity. S-03 Discovery has been reclassified from None to Primary in this audit. The 15 explicit None cells above exclude S-03 Discovery.

All 15 cells above meet the strict rule: each is named explicitly in its project's §4 Out. The remaining 143 cells of the matrix are **Unknown** (no evidence surfaced coverage in this access window) per the matrix's Empty Cell Convention. The audit's compactness-rule interpretation that previously labeled blank cells as None was found to be inconsistent with the strict rule and has been retired; the matrix now classifies blanks as Unknown throughout.

### Aggregate Counts After Audit Correction

| Cell Value | Original Sprint 3 | After Sprint 3.1 Audit |
|---|---|---|
| Primary | 24 | 24 |
| Secondary | 1 | 1 |
| Partial | 7 | 7 |
| None | 16 | 15 |
| Unknown | 143 | 143 |
| **Total** | **190** | **190** |

The Sprint 3.1 audit corrected three things:

1. **S-08 Security overclaim (Sprint 3.1 first pass)**: flipped S-08 Security from `N` to `—` (Unknown). This is included in the 143 Unknown count.
2. **S-03 Discovery underclaim (Sprint 3.1 second pass)**: flipped S-03 Discovery from `N` to `Pri` (Primary), restoring the per-cell evidence table's Primary classification. This is reflected in the 24 Primary count.
3. **Stage-count correction**: prose labels updated from "18 stages / 180 cells" to "19 stages / 190 cells" across `coverage-map.md` and `lifecycle-coverage-matrix.md`.

The original Sprint 3 None=144/Unknown=1 counts conflated explicit §4 Out None cells with the matrix's compactness rule (which treated blank cells as None). The Sprint 3.1 audit retires that compactness rule in favor of the strict rule (None requires explicit §4 Out; default for blank cells is Unknown), making the audit's totals 24 / 1 / 7 / 15 / 143 = 190.

### Audit Finding — Sprint 3 stage-count discrepancy

The Sprint 3 CHANGELOG, the matrix Purpose statement, and `coverage-map.md` all describe the lifecycle stage set as "18 stages", but the matrix table header, the CHANGELOG bullet, and `coverage-map.md` §"Sprint 3 lifecycle stage set" each list **19** distinct stages (Idea through Continuous Improvement). 10 × 19 = 190 cells.

- **Correction**: prose references to "18 stages" / "180 cells" updated to "19 stages" / "190 cells" in both `coverage-map.md` and `lifecycle-coverage-matrix.md`. No cell values changed; this is a counting label correction only. The CHANGELOG entry under Sprint 3 will be amended by Sprint 3.1.

### Audit Finding — S-03 Discovery cell-value inconsistency

The S-03 row in the matrix table records Discovery as `N` (None, citing §S-03 §4 Out "continuous customer touchpoints"), but the per-cell evidence table and the Primary-Cells-by-Project aggregate both list S-03 Discovery (Shaping) as `Primary`. Three locations disagree.

- **What §S-03 §4 Out actually says**: "Out: continuous customer touchpoints (compared with Continuous Discovery), formal engineering governance."
- **What §S-03 §6 Process Model actually says**: "1. Shape work into a clear problem and appetite. 2. Bet on which shaped work to pull into the next cycle. 3. Build during the fixed cycle. 4. Cool down after shipping. 5. Repeat."
- **Strict rule applied**: None requires the §4 Out to **explicitly** name the stage. "Continuous customer touchpoints" excludes a specific Continuous-Discovery-style weekly-customer-contact practice, not the broader Discovery lifecycle stage as a whole. Shape Up's §6 explicitly prescribes Shaping as a Discovery-equivalent activity (clear problem framing + appetite scoping) — this is structural Discovery responsibility even though Shape Up rejects the *Continuous* Discovery cadences of weekly customer touchpoints.
- **Correction**: S-03 Discovery cell flipped from `N` to `Pri` (Primary). The aggregate Primary count is **23** (not 24 or 25) — the per-cell evidence table's S-03 Discovery row was already correct, so this is a table-vs-evidence-vs-prose harmonization. The §4 Out statement still excludes **continuous customer touchpoints**; the audit does not change that fact, only its interpretation for matrix cell assignment.

### Audit Finding — S-06 ADR Confidence overclaim

The original Sprint 3 matrix recorded S-06 (Architecture, Documentation) confidence as `High` with the evidence triple `SRC-002, SRC-040 | Practitioner convention + community tooling`.

- **What the Confidence Scale actually requires for `High`**: multiple corroborating sources, or a single `Verified` primary source (per Sprint 2.3 external verification where applicable).
- **What the Source Register shows**: SRC-002 (Nygard blog post) and SRC-040 (adr.github.io community index) are both `Partially Verified` in `research/source-register.md` v0.5. Neither was directly read in the 2026-08-03 access window.
- **What §S-06 §13 Verification Notes record**: `Page Unverified` for both.
- **Correction**: S-06 (Architecture, Documentation) confidence downgraded from `High` to `Medium`. The cell value (`Primary`) is unchanged; only the confidence label is corrected. Two `Partially Verified` sources together meet the `Medium` definition ("multi-source corroboration of publication / scope, but primary page not directly read in this access window"), not the `High` definition.

No other cell-level confidence labels were mis-tagged under the audit.

### Audit Finding — Coverage-map.md consistency with matrix

The Sprint 3.1 audit verified consistency between `coverage-map.md`, `lifecycle-coverage-matrix.md`, and `artifact-relationship-map.md`.

- **S-06 ADR Confidence inconsistency (corrected).** `coverage-map.md` line ~297 originally recorded S-06 confidence as `High`. This was inconsistent with the matrix's later audit-corrected `Medium`. `coverage-map.md` updated to `Medium` with the same audit rationale. The cell value (`Primary`) is unchanged.
- **S-08 Security narrative vs matrix cell value.** `coverage-map.md` S-08 §Security Role says "None observed". After the Sprint 3.1 audit, the matrix records S-08 Security as `—` (Unknown) because §4 Out does not explicitly exclude it. The narrative's "None observed" is consistent with `Unknown` (i.e., evidence did not surface coverage) under the Interpretation Rules; this phrasing was not changed in `coverage-map.md`.
- **Lifecycle-stage set consistency.** All three Sprint 3 deliverables use the same 19-stage set; the Coverage Map describes lifecycle responsibility narratively, the matrix records cell values, and the artifact map lists lifecycle position for each artifact type.
- **Artifact-type consistency.** All three deliverables reference the same 15 artifact types; counts in the artifact map match the per-project narrative in the Coverage Map (e.g., S-07 produces SPEC + Task + Template + Workflow + Command = 5 artifact types; corrected earlier in this audit).

No other consistency defects observed.

---

## Cross-References

- `research/coverage/coverage-map.md` — narrative coverage map for each Selected project.
- `research/coverage/artifact-relationship-map.md` — artifact-level view across 15 artifact types.
- `research/competitors/reverse-research.md` — 14-section source data for each project.
- `research/source-register.md` — Source IDs cited in every non-empty cell.
- `research/research-plan.md` — Phase B definition.
- `tasks/sprint-03-coverage-map.md` — Sprint 3 task file.
