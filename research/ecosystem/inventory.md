# research/ecosystem/inventory.md

- Status: Draft
- Version: v0.3
- Owner: APES Maintainers
- Last Updated: 2026-08-03
- Purpose: Descriptive catalog of adjacent artifacts APES might coexist with. Each entry records what the artifact is, where it lives, and which APES lifecycle stage (if any) it nominally touches. No gap analysis, no positioning claims, no APES conclusions.

## Scope and Limits

- This inventory lists **what is in the adjacent landscape**, not what APES needs or does not need. Categories below are organized by their primary subject area, not by APES stages.
- Coverage is constrained by the access window of 2026-08-03 and by the `claude.ai` WebSearch / WebFetch restrictions that affected several primary sources. Per Sprint 2.1, every entry's verification status is now drawn from the corresponding row in `research/source-register.md` (Claim Verification field). Marketing pages are tagged as such; only independent empirical evidence is counted separately.
- Several popular-but-unverified items (e.g., Windsurf after the Cognition / Devin transition) are intentionally **not** included as inventory items, since no stable primary source could be confirmed.
- This document is descriptive only. The "Adjacent APES Stages" column is informational and does **not** express a coverage claim.

## Sprint 2.2 Verification Note (2026-08-03)

Per Sprint 2.2 (Primary Source Verification), every priority primary page corresponding to this inventory's items was attempted via direct WebFetch. The access window blocks `arxiv.org`, `github.com`, `agents.md`, `anthropic.com`, `docs.claude.com`, `iso.org`, `csrc.nist.gov`, `owaspsamm.org`, `owasp.org`, `cognitect.com`, and `producttalk.org`. The 22 attempts are recorded in `research/notes/verification-log.md` (VR-001 through VR-022), all with `Outcome: Inaccessible`. No Verification Status in this inventory was upgraded. Per the brief, this is the expected honest outcome under the access window; the Research Gate is `RESEARCH AGAIN`.

## Sprint 2.3 External Verification Reconciliation (2026-08-03)

Six sources were upgraded from `Partially Verified` to `Verified` in `research/source-register.md` based on external-verification evidence (EV-001 through EV-006) supplied by a reviewer with direct primary-source access. The inventory rows below are updated to reflect the new verification status where it changed. The original Sprint 2.2 Inaccessible rows in the verification log are preserved unchanged — they record the Claude-side access barrier, not the external reviewer's success.

The 6 upgrades:

- **SRC-001 (AGENTS.md project page)** → C5 row. Promotion from `Partially Verified` to `Verified`. The 60k+ adoption figure is tagged as project-maintainer-reported.
- **SRC-003 (NIST SP 800-218 SSDF v1.1)** → C4 and C7 rows. Promotion from `Partially Verified` to `Verified`. SSDF is a security practices framework, not a complete product-engineering standard.
- **SRC-006 (ISO/IEC/IEEE 12207:2026)** → C7 row. Promotion from `Partially Verified` to `Verified`. Only public metadata and abstract are verified; full text is paywalled.
- **SRC-015 (OpenAI Codex CLI)** → C6 row. Promotion from `Partially Verified` to `Verified`. License (Apache-2.0), repo existence, official positioning, and active maintenance status are confirmed.
- **SRC-044 (arXiv 2602.11988)** → C5 row. Promotion from `Partially Verified` to `Verified`. Abstract content verified; method details remain `Partially Verified`.
- **SRC-045 (arXiv 2601.20404)** → C5 row. Promotion from `Partially Verified` to `Verified`. Not retracted; abstract content verified. Conflicts with SRC-044 are preserved verbatim; APES does not adjudicate.

Sprint 2 still `In Review` per the original gate (≥15 Verified + ≥8 projects).

## Cross-Reference Conventions

- Sources cited inline as `(SRC-NNN)` refer to `research/source-register.md`.
- Categories below map to the APES 9-stage lifecycle as follows:
  - C1 ↔ Discovery, Research, Validation
  - C2 ↔ Research, Validation
  - C3 ↔ Research, Product
  - C4 ↔ Product, Engineering, Knowledge
  - C5 ↔ Research, Validation
  - C6 ↔ Discovery, Research, Validation, Product
  - C7 ↔ Engineering, Knowledge
  - C8 ↔ Business, Growth
  - C9 ↔ Discovery, Research, Validation, Product, Engineering

## Inventory Categories

| Code | Category | Items (see details below) | Adjacent APES Stages (informational) |
|---|---|---|---|
| C1 | Product Discovery Methods & Practitioner Literature | 8 | Discovery, Research, Validation |
| C2 | Evidence-Centric Research Methodology Literature | 5 | Research, Validation |
| C3 | Spec / Plan / Decision Authoring Conventions | 6 | Research, Product |
| C4 | Open Engineering Process / Practice Frameworks | 7 | Product, Engineering, Knowledge |
| C5 | Adjacent AI-Specific Process Guidance | 4 | Research, Validation |
| C6 | LLM Coding Agents & Agentic IDE Tools | 12 | Discovery, Research, Validation, Product |
| C7 | Engineering Standards, Security Baselines, Governance Documents | 8 | Engineering, Knowledge |
| C8 | Business / Strategy Modeling Tools | 5 | Business, Growth |
| C9 | Multi-Agent Orchestration Frameworks | 5 | Discovery, Research, Validation, Product, Engineering |

---

### C1. Product Discovery Methods & Practitioner Literature

| Item | Author / Maintainer | Year | Source(s) | What It Is | Verification Status |
|---|---|---|---|---|---|
| Continuous Discovery (book + framework) | Teresa Torres / Product Talk | 2021 | SRC-008, SRC-012, SRC-036 | Practitioner methodology for weekly customer touchpoints and Opportunity Solution Trees | Page Unverified (Product Talk + publisher corroboration) |
| Inspired: Creating Tech Products Customers Love (SVPG) | Marty Cagan / SVPG | 2008 | SRC-009, SRC-035 | Practitioner book on product discovery vs delivery teams and empowered product teams | Page Unverified (SVPG + publisher corroboration) |
| Lean Startup | Eric Ries | 2011 | SRC-010 | Build-Measure-Learn methodology; validated learning; innovation accounting | Page Unverified (theleanstartup.com corroboration) |
| Shape Up | Basecamp / Ryan Singer | 2019 | SRC-011, SRC-037 | Fixed-time, variable-scope shaping and betting cycles for product development | Page Unverified (basecamp.com/shapeup corroboration) |
| Dual-Track Development | Various (Hasso Plattner Institute popularized term; practitioners include Tony Ulwick, Jeff Patton) | 2010s | SRC-039 | Parallel Discovery and Delivery tracks | Page Unverified (community sources only) |
| Lean Canvas | Ash Maurya | 2010s | SRC-046 | One-page business plan adapted from BMC for startups | Page Unverified (leancanvas.com corroboration) |
| Business Model Canvas | Alexander Osterwalder | 2008 | SRC-047 | 9-block business model description | Page Unverified (strategyzer.com corroboration) |
| Opportunity Solution Tree (visual practice) | Teresa Torres / Product Talk | 2021 | SRC-008 | Visualization technique within Continuous Discovery | Same as Continuous Discovery |

### C2. Evidence-Centric Research Methodology Literature

| Item | Author / Maintainer | Year | Source(s) | What It Is | Verification Status |
|---|---|---|---|---|---|
| Jobs to Be Done (JTBD) — Christensen line | Clayton Christensen et al. (HBS) | 2003 onward | SRC-013, SRC-038 | Theory of customer "job" as causal unit of demand | Page Unverified (Strategyn + community sources) |
| Outcome-Driven Innovation (JTBD — Ulwick line) | Tony Ulwick / Strategyn | 2002 onward | SRC-013, SRC-038 | Desired-Outcome form of JTBD with patented process | Page Unverified (Strategyn site corroboration) |
| Jobs to Be Done — Strategyn Papers | Strategyn research group | 2000s onward | SRC-038 | Quantitative outcome-based segmentation | Page Unverified |
| Christensen "Competing Against Luck" book | Clayton Christensen et al. | 2016 | SRC-013 | Popular-press articulation of JTBD theory | Page Unverified (publisher corroboration) |
| Ulwick "Jobs to Be Done" book | Tony Ulwick | 2016 | SRC-038 | Practitioner-oriented JTBD text | Page Unverified (publisher corroboration) |

### C3. Spec / Plan / Decision Authoring Conventions

| Item | Author / Maintainer | Year | Source(s) | What It Is | Verification Status |
|---|---|---|---|---|---|
| Architecture Decision Record (ADR) | Michael Nygard | 2011 | SRC-002, SRC-040 | Status/Context/Decision/Consequences template for capturing architectural decisions | Partially Verified (cognitect blog + adr.github.io corroboration) |
| ADRs GitHub catalog (adr.github.io) | Community | n.d. | SRC-040 | Public catalog of ADR examples and tooling | Partially Verified |
| Markdown Any Decision Record (MADR) | Oliver Kopp et al. | 2018 (per community) | SRC-040 (related) | ADR variant with structured options and tradeoffs | Partially Verified (community-reported only) |
| OpenSpec | Fission-AI | n.d. (precise version Unverified) | SRC-026 | Open spec/plan format for AI coding workflows | Partially Verified (repo exists; license Unverified) |
| Spec Kit | GitHub | n.d. (precise release date Unverified) | SRC-025 | GitHub's spec-driven development toolkit | Partially Verified (repo exists; license Unverified) |
| Plan-mode artifacts (Claude Code / Gemini CLI / others) | Anthropic / Google / various | 2024 onward | SRC-014, SRC-024 | Plan-then-execute conversational artifact patterns | Unverified (vendor pages unreachable) |

### C4. Open Engineering Process / Practice Frameworks

| Item | Author / Maintainer | Year | Source(s) | What It Is | Verification Status |
|---|---|---|---|---|---|
| Site Reliability Engineering (SRE book) | Google | n.d. (precise year Unverified) | SRC-049 | Engineering practice for operations, SLOs, error budgets | Partially Verified (sre.google corroboration) |
| Continuous Delivery (book) | Jez Humble, David Farley | n.d. (year Unverified) | SRC-049 (related) | Deployment pipeline and lean software delivery | Partially Verified |
| The Phoenix Project / DevOps Handbook | Gene Kim et al. | n.d. (years Unverified) | SRC-049 (related) | DevOps narrative and process references | Partially Verified |
| DORA / Accelerate State of DevOps Reports | DORA / Google Cloud | n.d. (annual cadence; specific years Unverified) | SRC-007 | Annual metrics-driven DevOps survey | Partially Verified (dora.dev corroboration) |
| NIST SSDF (SP 800-218) | NIST | 2022-02 | SRC-003, SRC-050 | Secure software development framework | Verified (number, version, date, authors, official summary verified externally via EV-006; SSDF is a security practices framework, not a complete product-engineering standard) |
| OWASP SAMM v2 | OWASP | n.d. (v2.x line) | SRC-004 | Software assurance maturity model | Partially Verified |
| OWASP ASVS v4 | OWASP | n.d. (v4 line) | SRC-005 | Application security verification standard | Partially Verified |

### C5. Adjacent AI-Specific Process Guidance

| Item | Author / Maintainer | Year | Source(s) | What It Is | Verification Status |
|---|---|---|---|---|---|
| AGENTS.md convention | Open community (per project page; concrete release date Unverified) | 2025 onward | SRC-001 | Top-level repo guidance file for AI coding agents | Verified (page content and official self-positioning verified externally via EV-001; adoption figure is project-maintainer-reported) |
| arXiv 2602.11988 — Evaluating AGENTS.md (Gloaguen et al.) | Thibaud Gloaguen, Niels Mündler, Mark Müller, Veselin Raychev, Martin Vechev | 2026-02-12 | SRC-044 | Independent empirical evidence: in their evaluation setting, repository-level context files (including AGENTS.md) generally tended to lower task success and increase inference cost. Recommendation: keep only essential constraints. | Verified (existence, title, authors, dates, abstract content verified externally via EV-003; method details beyond abstract remain `Partially Verified`) |
| arXiv 2601.20404 — On the Impact of AGENTS.md Files on the Efficiency of AI Coding Agents | Jai Lal Lulla, Seyedmoein Mohsenimofidi, Matthias Galster, Jie M. Zhang, Sebastian Baltes, Christoph Treude | 2026-01-28 | SRC-045 | Independent empirical evidence: AGENTS.md associated with lower median runtime and lower output-token consumption; task-completion performance was roughly similar. | Verified (existence, title, authors, dates, abstract content verified externally via EV-004; method details beyond abstract remain `Partially Verified`). **Conflicts with SRC-044** on direction; APES does not adjudicate. |
| AI agent risk management — NIST AI 600-1 / ISO/IEC 42001 | NIST / ISO | 2024 onward | SRC-006 (ISO) + community corroboration | Standards-aligned AI risk management frameworks | Partially Verified |
| Anthropic / Claude responsible AI docs | Anthropic | 2024 onward | SRC-014, community sources | Vendor self-published responsible AI guidance | Unverified (vendor page unreachable) |

### C6. LLM Coding Agents & Agentic IDE Tools

| Item | Author / Maintainer | Year | Source(s) | What It Is | Verification Status |
|---|---|---|---|---|---|
| Claude Code | Anthropic | n.d. (vendor site unreachable; precise date Unverified) | SRC-014 | Agentic CLI coding agent | Unverified (vendor marketing claim) |
| OpenAI Codex CLI | OpenAI | n.d. (precise release date Unverified; dynamic dates intentionally not recorded) | SRC-015 | Open-source agentic coding CLI | Verified (repo exists, README positions as terminal coding agent, Apache-2.0 License, active maintenance at access date 2026-08-03 — verified externally via EV-002) |
| Cursor | Anysphere | n.d. (Cursor 2.0 release date Unverified) | SRC-016 | AI-native IDE | Unverified (vendor marketing claim) |
| aider | Paul Gauthier (Aider-AI) | n.d. (first-release year Unverified) | SRC-017 | Terminal AI pair-programming tool | Partially Verified (repo exists; license Unverified) |
| Cline | cline/cline | n.d. (precise rename date Unverified) | SRC-018 | VS Code AI agent extension | Partially Verified (repo exists; license Unverified) |
| OpenHands | All-Hands-AI | n.d. (MIT license attribution Unverified) | SRC-019 | Autonomous software engineering agent | Partially Verified (repo exists; license Unverified) |
| OpenCode | opencode-ai | n.d. (first-release date Unverified) | SRC-020 | Terminal AI coding tool | Partially Verified (repo exists; license Unverified) |
| Continue | continuedev | n.d. (first-release date Unverified) | SRC-021 | VS Code / JetBrains AI extension | Partially Verified (repo exists; license Unverified) |
| Roo Code | RooCodeInc | n.d. (fork date Unverified) | SRC-022 | VS Code AI coding agent | Partially Verified (repo exists; license Unverified) |
| GitHub Copilot | GitHub / Microsoft | n.d. (continuously updated) | SRC-023 | AI pair-programmer | Partially Verified (vendor docs corroborated) |
| Gemini CLI | Google | n.d. (first-release date Unverified) | SRC-024 | Open-source terminal AI assistant | Partially Verified (repo exists; license Unverified) |
| Sourcegraph Cody (decline case) | Sourcegraph | n.d. (specific snapshot date Unverified) | SRC-031 | AI coding assistant, activity diminished | Partially Verified (repo exists; maintenance status community-reported) |

### C7. Engineering Standards, Security Baselines, Governance Documents

| Item | Author / Maintainer | Year | Source(s) | What It Is | Verification Status |
|---|---|---|---|---|---|
| NIST SSDF (SP 800-218) | NIST | 2022-02 | SRC-003, SRC-050 | Secure software development practices | Verified (number, version, date, authors, official summary verified externally via EV-006; SSDF is a security practices framework, not a complete product-engineering standard) |
| OWASP SAMM v2 | OWASP | n.d. (v2.x line) | SRC-004 | Software assurance maturity model | Partially Verified |
| OWASP ASVS v4 | OWASP | n.d. (v4 line) | SRC-005 | Application security verification | Partially Verified |
| ISO/IEC/IEEE 12207:2026 (Edition 2) | ISO / IEC / IEEE | 2026-04 | SRC-006 | Current edition of "Systems and software engineering — Software life cycle processes" | Verified (number, title, edition, publication date, Published status verified externally via EV-005; full text paywalled; only public metadata and abstract are verified) |
| ISO/IEC/IEEE 12207:2017 (Edition 1, historical) | ISO / IEC / IEEE | 2017-11 | SRC-052 | Historical edition, superseded by 2026 Edition 2 | Partially Verified (canonical URL referenced; full text paywalled) |
| DHS/CISA Software Attestation | DHS / CISA | n.d. (precise attestation release date Unverified) | SRC-051 | Federal secure software development attestation guidance | Partially Verified |
| CISA Secure-by-Design Pledge | CISA | 2024 (community-reported) | SRC-051 (related) | Voluntary industry pledge on secure software development | Partially Verified |
| Synopsys SSDF analysis (BSIMM-style) | Synopsys | n.d. | SRC-050 | Industry adoption mapping to NIST SSDF | Partially Verified (vendor blog) |
| SRE Book | Google | n.d. (precise year Unverified) | SRC-049 | Reliability engineering practice guide | Partially Verified |

### C8. Business / Strategy Modeling Tools

| Item | Author / Maintainer | Year | Source(s) | What It Is | Verification Status |
|---|---|---|---|---|---|
| Business Model Canvas (BMC) | Alexander Osterwalder | n.d. (precise year Unverified) | SRC-047 | 9-block business model description | Unverified (vendor page unreachable) |
| Lean Canvas | Ash Maurya | n.d. (precise year Unverified) | SRC-046 | Startup-adapted BMC variant | Unverified (vendor page unreachable) |
| Strategyzer's Value Proposition Canvas | Osterwalder et al. | n.d. | SRC-047 (related) | Customer-jobs / pains / gains ↔ products / pain relievers / gain creators | Unverified |
| Christensen "Seeing What's Next" book | Clayton Christensen et al. | n.d. | SRC-013 (related) | Disruption theory and innovation strategy | Partially Verified |
| Strategyn's Outcome-Based Segmentation | Strategyn | n.d. | SRC-038 | Quantitative segmentation based on desired outcomes | Partially Verified |

### C9. Multi-Agent Orchestration Frameworks

| Item | Author / Maintainer | Year | Source(s) | What It Is | Verification Status |
|---|---|---|---|---|---|
| Model Context Protocol (MCP) | Anthropic / open community | n.d. (precise release month Unverified) | SRC-027 | Open protocol for tool/context interchange with LLMs | Unverified (vendor announcement page unreachable) |
| LangGraph | LangChain | n.d. (first-release date Unverified) | SRC-028 | Stateful multi-agent orchestration graph | Partially Verified (repo exists) |
| AutoGen | Microsoft Research | n.d. (first-release date Unverified) | SRC-029 | Multi-agent conversation framework | Partially Verified (repo exists) |
| Microsoft Agent Framework (consolidation) | Microsoft | n.d. (announcement date Unverified) | SRC-033 | Consolidated agent framework reported to absorb AutoGen + Semantic Kernel | Unverified (original announcement URL Unverified) |
| crewAI | crewAIInc | n.d. (first-release date Unverified) | SRC-030 | Role-based multi-agent orchestration | Partially Verified (repo exists; license Unverified) |

## Items Considered but Not Included

The following were inspected during Sprint 2 but were excluded from inventory:

- **Windsurf (Codeium / Cognition)** — community sources indicate a shift into the Cognition / Devin ecosystem in 2025, but no stable canonical primary source was reachable via the available WebFetch / WebSearch. Recorded in `research/notes/search-log.md` (SE-015) and re-evaluated later if a verifiable primary source emerges.
- **Devin (Cognition)** — marketing-heavy product with limited verifiable primary documentation during this access window; deferred.
- **Zed editor AI features** — out of the agentic-coding focus for this sprint.
- **Replit Ghostwriter** — out of focus; not adjacent to APES stages mapped here.
- **Various proprietary enterprise AI assistants** — no public, verifiable primary documentation available in this window.

## Notes on Quality and Limits

- Many entries are flagged `Partially Verified` or `Unverified` because the `claude.ai` WebFetch rejected the canonical primary domains during Sprint 2. Third-party corroborations are noted where used.
- Per Sprint 2.1, the **Verification Status** column reflects the **Claim Verification** field in the source register, not a self-defined label. Marketing pages are tagged as marketing claims; only independent empirical evidence (currently SRC-044 and SRC-045) is counted separately.
- No popularity, market share, or adoption claim is recorded anywhere in this inventory. Such figures were deliberately omitted to avoid presenting marketing-grade numbers as objective facts.
- No URL is included unless it was either successfully fetched or corroborated by a second, independent source during this access window.
- The "Adjacent APES Stages" column is informational and reflects where each item naturally sits relative to the APES 9-stage lifecycle. It does not constitute a coverage claim.

## Cross-References

- `research/source-register.md` — full source set supporting each inventory entry.
- `research/notes/search-log.md` — searches actually executed.
- `research/notes/verification-log.md` — Sprint 2.2 direct verification attempts (all `Inaccessible`).
- `research/competitors/candidate-projects.md` — Selected projects advanced to deeper reverse research.
- `research/research-plan.md` — original research plan that defined this inventory's structure.
- `tasks/sprint-02-2-primary-source-verification.md` — Sprint 2.2 task file.
- `tasks/sprint-02-3-external-verification-reconciliation.md` — Sprint 2.3 task file (6 sources upgraded via external-verification evidence).
