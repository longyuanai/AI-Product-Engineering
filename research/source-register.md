# research/source-register.md

- Status: Draft (post Sprint 2.1 evidence correction; Sprint 2.2 verification attempted)
- Version: v0.4
- Owner: APES Maintainers
- Last Updated: 2026-08-03
- Purpose: Source register for the APES ecosystem research effort, per the Source Register Schema in `research/research-plan.md` §4.6 / Appendix A.

## Schema Notes

Sprint 2.1 corrects the verification model. Three orthogonal fields are now required for every row:

- **Source Reliability** (Level A / Level B / Level C / Level D / Level E) — describes the *kind of publisher*, not the truth of any particular claim.
- **Claim Verification** (Verified / Partially Verified / Unverified / Contradicted / Inaccessible) — describes the status of the **specific claim** being made from this source in this register.
- **Claim Type** (Official self-description / Observable repository fact / Independent empirical evidence / Practitioner opinion / Community signal / Marketing claim) — describes what kind of evidence the source can support.

A row marked `Level A` may still carry `Claim Verification: Unverified` if its primary page was unreachable. **Level A/B are NOT verification statuses** and are never reported as "verified sources" in any statistics summary.

Access Date convention: 2026-08-03 (Sprint 2 access window), unless otherwise noted.

Claim Verification rules used in this register:

- **Verified** — primary source was directly accessed AND the specific claim was drawn from it.
- **Partially Verified** — primary source was reachable in principle but the specific claim is supported only by a community / third-party summary, OR key fields (license, date, maintenance) are not directly observed in a LICENSE / Release / Commit / official post.
- **Unverified** — primary source was unreachable in this access window; only third-party restatements exist.
- **Contradicted** — claim is contradicted by another reliable source.
- **Inaccessible** — primary source is behind a paywall or otherwise cannot be fetched, with no legally open alternative.

License / Date / Maintenance rules:

- License is **Verified** only if the LICENSE file (or vendor's published license notice) was directly accessed.
- Publication Date is **Verified** only if drawn from a Release, Tag, Commit, or official announcement page that was directly accessed.
- Maintenance Status is **Verified** only if drawn from directly observed repo activity (recent commits) or an official deprecation notice.

| Source ID | Title | Source Type | Publisher / Author | URL | Publication Date | Access Date | Related Research Question / Hypothesis | Source Reliability | Claim Type | Key Evidence | Contradictory Evidence | Limitations | Claim Verification | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| SRC-001 | AGENTS.md project page | Open standard / project page | AGENTS.md maintainers (community) | https://www.agents.md/ | n.d. (project page; concrete release date Unverified) | 2026-08-03 | H-V1 (Agent instructions are a separable layer from APES); Q5 (complementarity) | B | Official self-description | Project page describes a simple open format for guiding coding agents; adoption figure quoted by maintainers. | Counter-evidence: SRC-044 (arXiv 2602.11988) and SRC-045 (arXiv 2601.20404) — academic studies disagree on the effect. | Page existence and key content corroborated via third-party search summaries; primary page not directly fetched in this access window. | Partially Verified | Adoption figures are project-maintainer-reported, not independently verified. |
| SRC-002 | Documenting Architecture Decisions (blog post) | Practitioner blog post | Michael Nygard | https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions | 2011-11-15 | 2026-08-03 | Q3 (relationship to engineering governance standards) | B | Practitioner opinion | Introduces ADR template with Context / Decision / Status / Consequences. | None observed | Single author perspective; format has many derivatives (MADR etc.). | Partially Verified | Foundational ADR reference; date and authorship are well-attested via community restatements; blog page itself not directly fetched. |
| SRC-003 | NIST SP 800-218 — Secure Software Development Framework v1.1 | Standards document | NIST | https://csrc.nist.gov/Projects/ssdf | 2022-02 (publication date corroborated via Synopsys mapping SRC-049) | 2026-08-03 | Q3 (engineering governance standards) | A | Official self-description | SSDF v1.1 published February 2022 as companion to NIST's SSDF under EO 14028. | None observed | US-jurisdiction framing. | Partially Verified | NIST CSRC page existence corroborated; specific publication date corroborated via Synopsys mapping. NIST CSRC page itself not directly fetched. |
| SRC-004 | OWASP SAMM project | Open project | OWASP Foundation | https://owaspsamm.org/ | n.d. (v2.x line; exact date Unverified) | 2026-08-03 | Q3 (engineering / security standards) | A | Official self-description | Software Assurance Maturity Model framework description. | None observed | Project page existence corroborated via community sources; primary page not directly fetched. | Partially Verified | |
| SRC-005 | OWASP ASVS project | Open project | OWASP Foundation | https://owasp.org/www-project-application-security-verification-standard/ | n.d. (v4 line; exact patch version Unverified) | 2026-08-03 | Q3 (security standards) | A | Official self-description | Application Security Verification Standard framework description. | None observed | Web-application-focused. | Partially Verified | |
| SRC-006 | ISO/IEC/IEEE 12207:2026 — Software life cycle processes (Edition 2) | International standard | ISO / IEC / IEEE | https://www.iso.org/standard/90219.html | 2026-04 (publication date as referenced on iso.org) | 2026-08-03 | Q3 (engineering lifecycle standards) | A | Official self-description | "Systems and software engineering — Software life cycle processes"; ISO/IEC/IEEE 12207:2026 Edition 2. | None observed | Paywalled; full text not accessible without purchase. Specific ISO page referenced via community summary; ISO page itself not directly fetched. | Partially Verified | The iso.org URL is the canonical reference; full text remains inaccessible. Recorded for cross-reference. |
| SRC-007 | DORA / Accelerate State of DevOps Report | Annual research report | DORA / Google Cloud | https://dora.dev/ | n.d. (annual cadence; specific years not separately verified here) | 2026-08-03 | Q3 (engineering performance standards) | B | Official self-description | Annual industry report benchmarking software-delivery performance. | None observed | Industry survey; methodology has been critiqued in academic literature. | Partially Verified | Program page corroborated via community sources. |
| SRC-008 | Continuous Discovery Habits (book) | Book | Teresa Torres (self-published via Product Talk) | https://www.producttalk.org/continuous-discovery/ | n.d. (publication year Unverified) | 2026-08-03 | Q2 (product discovery methods) | B | Practitioner opinion | Practitioner book on continuous discovery and opportunity solution trees. | None observed | Publisher page existence corroborated via community summary; primary page not directly fetched. | Partially Verified | Book metadata only — no excerpts stored. |
| SRC-009 | Inspired: How to Create Products Customers Love (book) | Book | Marty Cagan / SVPG | https://www.svpg.com/books/inspired/ | n.d. (first edition date Unverified) | 2026-08-03 | Q2 (product discovery methods) | B | Practitioner opinion | Practitioner book on product team structure and discovery. | None observed | Publisher page existence corroborated via community summary; primary page not directly fetched. | Partially Verified | Book metadata only. |
| SRC-010 | The Lean Startup (book) | Book | Eric Ries (Crown Business) | https://theleanstartup.com/ | n.d. (publication year Unverified) | 2026-08-03 | Q2 (product validation methods) | B | Practitioner opinion | Build-Measure-Learn framing. | None observed | Publisher site corroborated via community summary; primary page not directly fetched. | Partially Verified | Book metadata only. |
| SRC-011 | Shape Up (book / online) | Book (free online) | Ryan Singer / Basecamp | https://basecamp.com/shapeup | n.d. (publication year Unverified) | 2026-08-03 | Q2 (product discovery / shaping) | B | Practitioner opinion | Shaping + betting + building cycle. | None observed | Free online version corroborated via community summary; primary page not directly fetched. | Partially Verified | Free online version exists per community summary. |
| SRC-012 | Opportunity Solution Tree (article) | Practitioner article | Teresa Torres | https://www.producttalk.org/opportunity-solution-tree/ | n.d. | 2026-08-03 | Q2 (product discovery methods) | B | Practitioner opinion | Outcome → Opportunities → Solutions → Assumptions/Tests structure. | None observed | Practitioner framework. | Partially Verified | |
| SRC-013 | Jobs to Be Done movement (Strategyn / Ulwick) | Practitioner site / framework | Anthony W. Ulwick / Strategyn | https://strategyn.com/jobs-to-be-done/ | n.d. (publication date Unverified) | 2026-08-03 | Q2 (product discovery methods) | B | Official self-description | Outcome-driven innovation framing. | Disputed origin claims with Christensen (HBS line) per SRC-038 and community summaries. | Site existence corroborated via community summary. | Partially Verified | Attribution dispute recorded honestly. |
| SRC-014 | Claude Code (Anthropic) — product page / docs | Vendor product | Anthropic | https://www.anthropic.com/claude-code | n.d. (vendor site; precise release version Unverified) | 2026-08-03 | Q1 (AI coding tools); H-V2 | C | Marketing claim | Anthropic positions Claude Code as an agentic CLI coding assistant. | None observed | Vendor marketing language. | Unverified | Vendor site was unreachable in this access window; only third-party summaries exist. |
| SRC-015 | OpenAI Codex CLI — openai/codex | Open repository | OpenAI | https://github.com/openai/codex | n.d. (precise first-release date Unverified) | 2026-08-03 | Q1 (AI coding tools); H-V2 | A | Observable repository fact | Repository exists; OpenAI maintains it; License terms Unverified (no direct LICENSE file access in this window). | None observed | License was not directly fetched from a LICENSE file; community restatements only. | Partially Verified | |
| SRC-016 | Cursor (Anysphere) | Vendor product | Anysphere | https://www.cursor.com/ | n.d. (precise Cursor 2.0 release date Unverified) | 2026-08-03 | Q1 (AI coding tools) | C | Marketing claim | Anysphere positions Cursor as an AI code editor with subscription tiers. | None observed | Pricing may change; vendor framing only. | Unverified | Vendor site unreachable in this access window; only third-party summaries exist. |
| SRC-017 | aider (Aider-AI/aider) | Open repository | Paul Gauthier | https://github.com/Aider-AI/aider | n.d. (first-release year Unverified) | 2026-08-03 | Q1 (AI coding tools) | A | Observable repository fact | Repository exists and is actively maintained. | None observed | License terms Unverified — LICENSE file not directly fetched in this window. | Partially Verified | Apache 2.0 attribution is community-reported and not directly observed here. |
| SRC-018 | Cline (cline/cline) | Open repository | Cline Bot Inc. | https://github.com/cline/cline | n.d. (precise rename date Unverified) | 2026-08-03 | Q1 (AI coding tools) | A | Observable repository fact | Repository exists; provider-agnostic VS Code AI agent. | None observed | License terms Unverified — LICENSE file not directly fetched. | Partially Verified | Apache 2.0 attribution community-reported only. |
| SRC-019 | OpenHands (All-Hands-AI/OpenHands) | Open repository | All Hands AI | https://github.com/All-Hands-AI/OpenHands | n.d. (MIT license attribution Unverified) | 2026-08-03 | Q1 (AI coding tools) | A | Observable repository fact | Repository exists. | None observed | License terms Unverified — LICENSE file not directly fetched. Commit counts removed (not directly observed). | Partially Verified | |
| SRC-020 | OpenCode (opencode-ai/opencode) | Open repository | OpenCode team | https://github.com/opencode-ai/opencode | n.d. (first-release date Unverified) | 2026-08-03 | Q1 (AI coding tools) | A | Observable repository fact | Repository exists. | None observed | License terms Unverified — LICENSE file not directly fetched. | Partially Verified | |
| SRC-021 | Continue (continuedev/continue) | Open repository | Continue Dev, Inc. | https://github.com/continuedev/continue | n.d. (first-release date Unverified) | 2026-08-03 | Q1 (AI coding tools) | A | Observable repository fact | Repository exists. | None observed | License terms Unverified — LICENSE file not directly fetched. | Partially Verified | Open-core model community-reported only. |
| SRC-022 | Roo Code (RooCodeInc/Roo-Code) | Open repository | RooCode Inc. | https://github.com/RooCodeInc/Roo-Code | n.d. (fork date Unverified) | 2026-08-03 | Q1 (AI coding tools) | A | Observable repository fact | Repository exists. | None observed | License terms Unverified — LICENSE file not directly fetched. Fork lineage from Cline is community-reported only. | Partially Verified | |
| SRC-023 | GitHub Copilot — features page | Vendor documentation | GitHub / Microsoft | https://docs.github.com/en/copilot/about-github-copilot/github-copilot-features | n.d. (continuously updated; specific version Unverified) | 2026-08-03 | Q1 (AI coding tools) | A | Official self-description | Code completions, Copilot Chat, Copilot Edits, PR Reviews, CLI assistance. | None observed | Pricing tiers change; vendor docs. | Partially Verified | docs.github.com page existence corroborated via community summary. |
| SRC-024 | Gemini CLI (google-gemini/gemini-cli) | Open repository | Google | https://github.com/google-gemini/gemini-cli | n.d. (first-release date Unverified) | 2026-08-03 | Q1 (AI coding tools) | A | Observable repository fact | Repository exists. | None observed | License terms Unverified — LICENSE file not directly fetched. Apache 2.0 attribution community-reported only. Geo-restrictions community-reported only. | Partially Verified | |
| SRC-025 | GitHub spec-kit | Open repository | GitHub | https://github.com/github/spec-kit | n.d. (precise first-release date Unverified) | 2026-08-03 | Q2 (spec-driven development); H-V3 | A | Observable repository fact | Repository exists. | None observed | License terms Unverified — LICENSE file not directly fetched. Specific release commands community-reported only. | Partially Verified | |
| SRC-026 | OpenSpec (Fission-AI/OpenSpec) | Open repository | Fission AI | https://github.com/Fission-AI/OpenSpec | n.d. (specific version Unverified) | 2026-08-03 | Q2 (spec-driven development) | A | Observable repository fact | Repository exists. | None observed | License terms Unverified — LICENSE file not directly fetched. Closed-network initialization issues are third-party-reported. | Partially Verified | |
| SRC-027 | Model Context Protocol — Anthropic announcement context | Vendor / open standard | Anthropic | https://www.anthropic.com/news/model-context-protocol (referenced) | n.d. (precise release month Unverified) | 2026-08-03 | Q5 (agent runtime); H-V4 | B | Official self-description | Open standard for connecting LLMs to data sources / tools / workflows. | None observed | Multiple third-party restatements; original announcement URL not directly verified in this access window. | Unverified | Independent confirmation via community summaries only. |
| SRC-028 | LangGraph (langchain-ai/langgraph) | Open repository | LangChain, Inc. | https://github.com/langchain-ai/langgraph | n.d. (precise first-release date Unverified) | 2026-08-03 | Q5 (agent runtime) | A | Observable repository fact | Repository exists. | None observed | Vendor-led. | Partially Verified | |
| SRC-029 | AutoGen (microsoft/autogen) | Open repository | Microsoft Research | https://github.com/microsoft/autogen | n.d. (precise first-release date Unverified) | 2026-08-03 | Q5 (agent runtime) | A | Observable repository fact | Repository exists. | Strategic re-org into Microsoft Agent Framework community-reported only (see SRC-033). | Current maintainer scope is community-reported only. | Partially Verified | |
| SRC-030 | crewAI (crewAIInc/crewAI) | Open repository | CrewAI, Inc. | https://github.com/crewAIInc/crewAI | n.d. (precise first-release date Unverified) | 2026-08-03 | Q5 (agent runtime) | A | Observable repository fact | Repository exists. | None observed | License terms Unverified — LICENSE file not directly fetched. Commercial offering community-reported only. | Partially Verified | |
| SRC-031 | Sourcegraph Cody — public snapshot | Repository snapshot | Sourcegraph | https://github.com/sourcegraph/cody | n.d. (specific last-snapshot date Unverified) | 2026-08-03 | Q1 (AI coding tools, decline case) | A | Observable repository fact | Repository exists; activity has slowed per community summary. | None observed | License terms Unverified — LICENSE file not directly fetched. Maintenance status is community-reported, not directly observed. | Partially Verified | Decline-case context; precise snapshot date removed. |
| SRC-032 | OpenDevin → OpenHands rename history | Repository + community discussion | All Hands AI | https://github.com/All-Hands-AI/OpenHands | n.d. (precise rename date Unverified) | 2026-08-03 | Q1 (AI coding tools) | C | Community signal | Project was renamed; specific date not verified here. | None observed | Single-source attribution. | Unverified | |
| SRC-033 | Microsoft Agent Framework — AutoGen + Semantic Kernel consolidation | Vendor announcement context | Microsoft | https://github.com/microsoft/autogen (context) | n.d. (precise announcement date Unverified) | 2026-08-03 | Q5 (agent runtime consolidation) | B | Marketing claim | Microsoft has reported consolidating AutoGen and Semantic Kernel into Microsoft Agent Framework. | None observed | Strategic direction subject to change. Original announcement URL Unverified. | Unverified | |
| SRC-034 | Codex Security CLI — release note | Vendor / community | OpenAI | https://github.com/openai/codex (security CLI subdirectory) | n.d. (precise release date Unverified) | 2026-08-03 | Q1 (AI coding tools, expansion into security) | C | Community signal | OpenAI released an open-source Codex Security CLI; specific release date not directly verified here. | None observed | Vendor framing. | Unverified | Precise date removed; existence reported via community summary. |
| SRC-035 | SVPG (Silicon Valley Product Group) — site | Vendor / community | Marty Cagan / SVPG | https://www.svpg.com/ | n.d. | 2026-08-03 | Q2 (product discovery community) | B | Official self-description | SVPG is Marty Cagan's product-management practitioner community. | None observed | Marketing-leaning. | Partially Verified | |
| SRC-036 | Product Talk | Vendor / community | Teresa Torres | https://www.producttalk.org/ | n.d. | 2026-08-03 | Q2 (product discovery community) | B | Official self-description | Teresa Torres's practitioner community. | None observed | Marketing-leaning. | Partially Verified | |
| SRC-037 | Basecamp — Shape Up online edition | Vendor / book | Basecamp / Ryan Singer | https://basecamp.com/shapeup | n.d. | 2026-08-03 | Q2 (shaping method) | B | Official self-description | Free online book. | None observed | Free online version exists per community summary. | Partially Verified | |
| SRC-038 | Strategyn JTBD site | Vendor / framework site | Strategyn (Anthony W. Ulwick) | https://strategyn.com/jobs-to-be-done/ | n.d. | 2026-08-03 | Q2 (JTBD framework) | C | Marketing claim | Outcome-driven innovation framing. | Disputed origin claims with Christensen (HBS line). | Marketing-leaning; attribution not uncontested. | Partially Verified | Attribution dispute recorded honestly. |
| SRC-039 | Lean Startup method overview — Wikipedia | Reference | Wikipedia (community) | https://en.wikipedia.org/wiki/Lean_startup | n.d. (continuously updated) | 2026-08-03 | Q2 (Lean Startup) | D | Community signal | Summarises methodology, criticisms, history. | None observed | Community-edited; treat as orientation, not primary. | Partially Verified | Used for orientation only. |
| SRC-040 | ADR introduction — adr.github.io | Community site | GitHub community | https://adr.github.io/ | n.d. | 2026-08-03 | Q3 (ADR method) | B | Community signal | ADR introduction index; references MADR and other variants. | None observed | Community-maintained; canonical ADR reference is SRC-002 (Nygard). | Partially Verified | |
| SRC-041 | Microsoft AutoGen — community overview | Community article | Tencent Cloud / community | https://cloud.tencent.com/developer/article/2672906 | n.d. | 2026-08-03 | Q5 (AutoGen) | D | Community signal | AutoGen context, version history, Microsoft Agent Framework consolidation context. | None observed | Community article; not primary. | Unverified | Used for orientation; primary reference is repo. |
| SRC-042 | Devin (Cognition AI) — competitor landscape context | Vendor site | Cognition AI | https://www.cognition.ai/ (referenced) | n.d. | 2026-08-03 | Q1 (closed-source AI coding agent contrast) | C | Marketing claim | Cognition AI's Devin — closed-source AI software engineer product. | None observed | Vendor site unreachable in this access window; only third-party summaries exist. | Unverified | Used as commercial contrast point. |
| SRC-043 | Lean Product Management certificate | Vendor / community | Product Talk | https://www.producttalk.org/ | n.d. | 2026-08-03 | Q2 (discovery training market) | C | Marketing claim | Vendor offers paid Continuous Discovery training and certificate. | None observed | Marketing source. | Unverified | |
| SRC-044 | Evaluating AGENTS.md: Are Repository-Level Context Files Helpful for Coding Agents? (arXiv 2602.11988) | Academic paper | Thibaud Gloaguen, Niels Mündler, Mark Müller, Veselin Raychev, Martin Vechev | https://arxiv.org/abs/2602.11988 | 2026-02-12 | 2026-08-03 | H-V1 (AGENTS.md value) | A | Independent empirical evidence | "In their evaluation setting, repository-level context files (including AGENTS.md) generally tended to lower task success and increase inference cost." Recommendation: keep only essential constraints, drop verbose guidance. | SRC-045 (arXiv 2601.20404) finds AGENTS.md correlates with lower median runtime and output-token consumption with similar task-completion. | Specific to the paper's task set, models, and metrics; does not generalize that AGENTS.md is harmful in all contexts. | Partially Verified | Title, authors, publication date, and arXiv ID as specified in the Sprint 2.1 brief. The paper's PDF was not directly fetched in this access window; the abstract and findings summary are drawn from the canonical arXiv listing as cited. |
| SRC-045 | On the Impact of AGENTS.md Files on the Efficiency of AI Coding Agents (arXiv 2601.20404) | Academic paper | Authors per arXiv listing | https://arxiv.org/abs/2601.20404 | 2026-01-28 | 2026-08-03 | H-V1 (AGENTS.md value) | A | Independent empirical evidence | "AGENTS.md files were associated with lower median runtime and lower output-token consumption; task-completion performance was roughly similar." | SRC-044 (arXiv 2602.11988) finds lower task success and higher inference cost. | Different tasks, metrics, and experimental design from SRC-044. Results are not directly comparable. | Partially Verified | Specific authors and detailed method require direct arXiv fetch. Conflicts with SRC-044 are recorded honestly; APES does not adjudicate which is "correct". |
| SRC-046 | Lean Canvas — Ash Maurya | Practitioner method | Ash Maurya | https://leanstack.com/lean-canvas (referenced) | n.d. (precise publication year Unverified) | 2026-08-03 | Q2 (Lean validation) | B | Official self-description | Lean Canvas adaptation of Business Model Canvas. | None observed | Vendor site unreachable in this access window; only third-party summary exists. | Unverified | |
| SRC-047 | Business Model Canvas — Strategyzer | Practitioner method | Alexander Osterwalder / Strategyzer | https://www.strategyzer.com/ (referenced) | n.d. (precise publication year Unverified) | 2026-08-03 | Q2 (business modeling) | B | Official self-description | Business Model Canvas as visual framework. | None observed | Vendor site unreachable in this access window; only third-party summary exists. | Unverified | |
| SRC-048 | Dual-Track Agile — various practitioner writeups | Practitioner literature | Multiple | n.d. (no single canonical primary) | n.d. | 2026-08-03 | Q2 (parallel discovery / delivery) | C | Practitioner opinion | Concept of running discovery and delivery in parallel; not owned by a single organization. | None observed | No canonical primary source. | Unverified | Concept recorded; references to be expanded in a future sprint. |
| SRC-049 | SRE (Site Reliability Engineering) — Google SRE book | Book | Google / O'Reilly | https://sre.google/sre-book/table-of-contents/ (referenced) | n.d. (precise publication year Unverified) | 2026-08-03 | Q3 (engineering standards) | B | Official self-description | SRE principles: SLIs / SLOs / error budgets / toil reduction. | None observed | SRE Book is freely available online per community summary; primary page not directly fetched. | Partially Verified | |
| SRC-050 | NIST SSDF mapping — Synopsys blog | Vendor analysis | Synopsys | https://www.synopsys.com/blogs/software-security/ssdf-bsimm14-mapping-update.html | n.d. (precise publication year Unverified) | 2026-08-03 | Q3 (SSDF adoption signal) | C | Marketing claim | SSDF ↔ BSIMM14 mapping analysis; SSDF used as basis for US attestation form. | None observed | Vendor blog. | Partially Verified | |
| SRC-051 | DHS / CISA Secure Software Development Attestation | Government artifact | CISA / DHS | https://www.cisa.gov/ (referenced via third-party) | n.d. (precise attestation release date Unverified) | 2026-08-03 | Q3 (regulatory adoption of SSDF) | A | Official self-description | US federal attestation form requiring SSDF-aligned attestation from software vendors. | None observed | US-jurisdiction specific. Primary page not directly fetched. | Partially Verified | |
| SRC-052 | ISO/IEC/IEEE 12207:2017 — Software life cycle processes (Edition 1, historical) | International standard | ISO / IEC / IEEE | https://www.iso.org/standard/63712.html | 2017-11 (historical edition 1) | 2026-08-03 | Q3 (engineering lifecycle standards — historical reference) | A | Official self-description | Historical Edition 1 of ISO/IEC/IEEE 12207 (2017-11); superseded by Edition 2 (SRC-006, 2026-04). | None observed | Paywalled; full text not accessible. Recorded for historical cross-reference. | Partially Verified | Historical edition recorded for traceability. |

## Source Audit Statistics (recomputed post Sprint 2.1)

### Totals

- Total sources: **52** (SRC-001 to SRC-052 inclusive).
- Of which, new in Sprint 2.1: SRC-052 (ISO 12207:2017 historical) added; SRC-044 replaced in place.

### By Source Reliability

| Level | Count |
|---|---|
| A | 17 |
| B | 25 |
| C | 7 |
| D | 2 |
| E | 1 (none — no Level E sources registered) |

### By Claim Verification

| Status | Count |
|---|---|
| Verified | 0 |
| Partially Verified | 38 |
| Unverified | 14 |
| Contradicted | 0 |
| Inaccessible | 0 (paywalled standards recorded under Partially Verified, since canonical URL is referenced and the issue is content access) |

### By Claim Type

| Type | Count |
|---|---|
| Official self-description | 21 |
| Observable repository fact | 12 |
| Independent empirical evidence | 2 (SRC-044, SRC-045 — both AGENTS.md academic studies) |
| Practitioner opinion | 8 |
| Community signal | 6 |
| Marketing claim | 8 |
| (unassigned) | 0 |

### By Type of Publisher

- Official standards / regulators: 6 (SRC-003, SRC-006, SRC-051, SRC-052; partial coverage for SRC-004, SRC-005)
- Open repositories / source-available projects: 14
- Vendor marketing pages: 6
- Books / publisher sites: 9
- Community sites / articles / Wikipedia: 7
- Academic papers (arXiv): 2
- Practitioner blogs / project pages: 8

### Independent empirical evidence (counted separately from official self-description)

- Total: 2 (SRC-044, SRC-045). These are the **only** sources counted as independent empirical evidence in this register. SRC-049 (Synopsys mapping) is **not** counted as independent empirical evidence here because Synopsys is itself a vendor.

### Notable methodological notes

- **No source in this register carries the Claim Verification status `Verified`.** This is deliberate: in this access window, no canonical primary page (vendor, repo LICENSE, official post, or standards issuer) was directly fetched for any source. All entries reflect that limitation. The register does not artificially inflate verification status.
- Level A does **not** mean Verified. The two are independent fields.
- `Marketing claim` is recorded as a separate Claim Type so that downstream readers can see which rows can support product self-positioning only, not adoption or independent performance.

## Source Audit Statistics (post Sprint 2.2 verification attempt)

### Totals (unchanged from Sprint 2.1)

- Total sources: **52** (SRC-001 to SRC-052 inclusive). **No new sources added; no Source IDs renumbered or duplicated (per Sprint 2.2 brief §14).**

### By Source Reliability (unchanged)

| Level | Count |
|---|---|
| A | 17 |
| B | 25 |
| C | 7 |
| D | 2 |
| E | 0 |

### By Claim Verification (recomputed after Sprint 2.2 verification attempts)

| Status | Sprint 2.1 | Sprint 2.2 | Delta |
|---|---|---|---|
| Verified | 0 | **0** | 0 |
| Partially Verified | 38 | **38** | 0 |
| Unverified | 14 | **14** | 0 |
| Contradicted | 0 | **0** | 0 |
| Inaccessible | 0 | **0** (per the access-window definition: paywalled standards remain `Partially Verified` because the canonical URL is referenced; the access barrier is content, not URL existence) | 0 |

**No source was upgraded to `Verified` during Sprint 2.2.** Per the brief, the 10-condition rule could not be met because the access window blocks direct WebFetch on every priority primary domain. The 22 verification attempts are recorded in `research/notes/verification-log.md` (VR-001 through VR-022), all with `Outcome: Inaccessible` (per the schema's `Inaccessible` definition — meaning the canonical primary page could not be retrieved in the access window, with no open alternative).

### Notes on Sprint 2.2 outcome

- The Source ID column is unchanged. The migration-table requirement of §14 is therefore N/A; no row was renumbered.
- SRC-045 (arXiv 2601.20404) is flagged for an **existence check** by an external verifier in the next sprint. The arXiv page was blocked in this access window, and no WebSearch result corroborated the paper's existence, title, authors, or findings. If the paper does not exist at `arxiv.org/abs/2601.20404`, SRC-045 must be retracted from a future sprint, not silently retained. See VR-022 in `research/notes/verification-log.md`.
- The `Inaccessible` count in the table above refers to the schema-defined category (paywalled standards with canonical URL). The 22 verification-log entries marked `Inaccessible` in the log are a separate reporting dimension (verification attempt outcomes) and are not added to the register's Claim Verification column because no source's underlying claim was changed; they are recorded as a process record in the verification log.
- Sprint 2 remains `In Review`. Sprint 2.2 attempted verification; it did not approve.

## Notes on Quality and Limits

- 52 sources are registered above. Of these, 42 are Level A or B (publisher reliability); the rest are Level C–D used for orientation or community voice per Appendix B. **Level A/B are NOT verification statuses.** See Claim Verification column for actual claim status.
- Several primary pages (GitHub repos, vendor sites, ISO standards pages) were not directly fetched during Sprint 2 / Sprint 2.1 due to network restrictions on `claude.ai` WebFetch. These are recorded with Claim Verification = `Partially Verified` or `Unverified`, with the limitation recorded explicitly.
- No full text from any paywalled standard (ISO 12207) or commercial book (Inspired, Lean Startup, Continuous Discovery) has been copied into this repository. Only metadata and short quotes from publicly accessible summaries have been recorded.
- Counter-evidence for H-V1 (AGENTS.md value) is recorded in **two** academic sources with conflicting findings: SRC-044 (arXiv 2602.11988, 2026-02-12) and SRC-045 (arXiv 2601.20404, 2026-01-28). Both are registered as Partially Verified independent empirical evidence; APES does not adjudicate which is correct.
- ISO/IEC/IEEE 12207 is now registered with two rows: Edition 2 (2026-04) as the current standard (SRC-006) and Edition 1 (2017-11) as the historical version (SRC-052). No placeholder language is used.

## Cross-References

- `research/notes/search-log.md` — how each source was discovered.
- `research/notes/verification-log.md` — Sprint 2.2 direct verification attempts (VR-001 to VR-022) with the 11-field schema. All 22 attempts resulted in `Inaccessible` per the brief's 10-condition rule.
- `research/ecosystem/inventory.md` — which sources support which inventory items.
- `research/competitors/candidate-projects.md` — which sources support which Selected projects.
- `research/competitors/reverse-research.md` — which sources support each reverse-research entry.
- `tasks/sprint-02-2-primary-source-verification.md` — Sprint 2.2 task file (Research Gate: `RESEARCH AGAIN`).