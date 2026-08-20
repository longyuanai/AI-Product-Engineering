# research/notes/verification-log.md

- Status: Draft (post Sprint 2.2 + Sprint 2.3 External Verification Reconciliation + Sprint 2.4 Targeted Re-verification)
- Version: v0.3
- Owner: APES Maintainers
- Last Updated: 2026-08-15
- Purpose: Record every direct primary-source verification attempt made during Sprint 2.2 (Primary Source Verification), with honest Access Result, Evidence Location, and Outcome. Per Sprint 2.2 brief §15: **"若无法直接访问足够原始来源: 不得伪造通过; Sprint 2 保持 In Review; 最终结论输出 RESEARCH AGAIN; 明确列出需要由其他具备网络访问能力的研究者验证的来源."** This file is the record of those attempts. Sprint 2.3 adds an External Verification Reconciliation section that records the EV-### entries supplied by an external reviewer with direct primary-source access. Sprint 2.4 appends VR-023 through VR-034 for targeted direct re-verification. The original Sprint 2.2 Inaccessible rows are preserved unchanged.

## Schema (11 fields per Sprint 2.2 brief §11)

| # | Field | Description |
|---|---|---|
| 1 | Verification ID | `VR-NNN` identifier (sequential) |
| 2 | Source ID | `SRC-NNN` from `research/source-register.md` |
| 3 | Original URL | The canonical primary URL that was targeted |
| 4 | Access Date | Date the verification attempt was made (`2026-08-03` for this sprint) |
| 5 | Access Result | Outcome of the WebFetch attempt: `Success` / `Blocked (domain)` / `Blocked (network)` / `Search-only` / `Other error` |
| 6 | Claims Checked | The specific factual claims being verified (1–5 bullets) |
| 7 | Evidence Location | Where the evidence was actually obtained: URL fragment, repository path, search-result title, etc. (`—` if not obtained) |
| 8 | License Checked | License observed: license name (e.g., `Apache-2.0`, `MIT`, `CC-BY-4.0`, `—`) or `Not reachable` |
| 9 | Maintenance Checked | Maintenance signal: latest release / tag / commit date, or `—` |
| 10 | Outcome | One of: `Verified` / `Partially Verified` / `Unverified` / `Contradicted` / `Inaccessible` |
| 11 | Notes | Free-form note; mandatory for every `Inaccessible` and `Unverified` row |

## Access-Window Constraints (2026-08-03)

The following primary domains returned `Unable to verify if domain X is safe to fetch` from `claude.ai` WebFetch during this sprint's access window and could not be opened directly. This list is the union of Sprint 2 restrictions and the Sprint 2.2 newly-probed domains:

| Domain | Class of source | Verified via direct fetch? |
|---|---|---|
| `arxiv.org` | Academic preprints (SRC-044, SRC-045) | No — both `2602.11988` and `2601.20404` returns blocked |
| `github.com` | Open-source repositories (all C6 / C9 / C5 items) | No |
| `agents.md` | AGENTS.md official site (SRC-001) | No |
| `anthropic.com` | Claude Code vendor docs (SRC-014) | No |
| `docs.claude.com` | Claude Code docs subdomain (SRC-014) | No |
| `iso.org` | ISO 12207 standards pages (SRC-006, SRC-052) | No |
| `csrc.nist.gov` | NIST SSDF (SRC-003, SRC-050) | No |
| `owaspsamm.org` | OWASP SAMM (SRC-004) | No |
| `owasp.org` | OWASP ASVS (SRC-005) | No |
| `cognitect.com` | Nygard ADR blog post (SRC-002) | No |
| `producttalk.org` | Continuous Discovery (SRC-008, SRC-012) | No |
| `svpg.com` | Inspired / Cagan (SRC-009, SRC-035) | No — not yet probed in Sprint 2.2; expected blocked |
| `basecamp.com` | Shape Up (SRC-011, SRC-037) | No — not yet probed; expected blocked |
| `cursor.com` | Cursor (SRC-016) | No — not yet probed; expected blocked |

Per Sprint 2.2 brief §15: WebSearch result snippets are **not** treated as direct primary access. They are used here only to record what the agent could observe about a source without opening it, so the limitation is visible.

---

## Verification Attempts

### VR-001 — AGENTS.md (SRC-001)

- **Verification ID:** VR-001
- **Source ID:** SRC-001
- **Original URL:** https://agents.md/
- **Access Date:** 2026-08-03
- **Access Result:** Blocked (domain — `agents.md` not in WebFetch allow-list)
- **Claims Checked:**
  - Project site exists and positions AGENTS.md as a "README for agents"
  - Adoption figure ("over 60,000 open-source projects")
  - Governance under "Linux Foundation AAIF"
  - Format specification
- **Evidence Location:** WebSearch snippet for `agents.md AGENTS.md open convention GitHub repository 2025` returned the URL `https://agents.md/` and the phrasing "a simple, open format for guiding coding agents" / "a README for agents". Third-party CSDN article `https://blog.csdn.net/gitblog_00776/article/details/157234753` corroborates the README-for-agents framing.
- **License Checked:** Not reachable (project site blocked; no LICENSE file observable via WebFetch)
- **Maintenance Checked:** Not reachable (project site blocked; no release/tag observable)
- **Outcome:** **Inaccessible**
- **Notes:** Per §15, no upgrade to `Verified`. The phrasing matches the inventory record, but the canonical primary page was not opened directly. A future verifier with `agents.md` access should confirm: (a) the exact wording on the homepage; (b) any explicit version / license notice; (c) the governance claim about Linux Foundation AAIF; (d) the adoption figure and its date.

### VR-002 — Claude Code (SRC-014)

- **Verification ID:** VR-002
- **Source ID:** SRC-014
- **Original URL:** https://docs.claude.com/en/docs/claude-code
- **Access Date:** 2026-08-03
- **Access Result:** Blocked (domain — `docs.claude.com` not in WebFetch allow-list)
- **Claims Checked:**
  - Vendor's positioning statement for Claude Code
  - AGENTS.md support claim
  - Supported features list (CLAUDE.md, plan mode, hooks, etc.)
  - Installation / distribution model
- **Evidence Location:** WebSearch snippets referencing `https://new.qq.com/rain/a/20251029A052U600` and `https://www.sohu.com/...` describe "Claude Code official documentation features" but do not constitute a direct primary access. A WebSearch for the project name returned the docs URL but not its contents.
- **License Checked:** Not reachable (vendor docs blocked; CLI distribution model not verifiable)
- **Maintenance Checked:** Not reachable (no release notes page opened)
- **Outcome:** **Inaccessible**
- **Notes:** Per §15, no upgrade. The Source Register row remains `Partially Verified` (community-corroborated vendor self-description). A future verifier should open `docs.claude.com/en/docs/claude-code` directly and confirm: page title, AGENTS.md mention, current feature list, and any visible versioning.

### VR-003 — OpenAI Codex CLI (SRC-015)

- **Verification ID:** VR-003
- **Source ID:** SRC-015
- **Original URL:** https://github.com/openai/codex
- **Access Date:** 2026-08-03
- **Access Result:** Blocked (domain — `github.com` not in WebFetch allow-list)
- **Claims Checked:**
  - Full repo name (`openai/codex`)
  - Default branch
  - README positioning
  - LICENSE presence and type
  - Latest release date
  - Supported tools
- **Evidence Location:** WebSearch snippet for `"openai/codex"` referenced "open-source release confirmed 2025; Security CLI referenced 2026-07" via community release notes. Repo existence corroborated by multiple WebSearch hits but no canonical primary page opened.
- **License Checked:** Not reachable (LICENSE file not opened)
- **Maintenance Checked:** Not reachable (no Release / Tag observable)
- **Outcome:** **Inaccessible**
- **Notes:** Per §15, no upgrade. A future verifier should confirm the LICENSE type (community reports Apache-2.0), default branch, latest release tag, and the README's first paragraph.

### VR-004 — Model Context Protocol / MCP (SRC-027)

- **Verification ID:** VR-004
- **Source ID:** SRC-027
- **Original URL:** https://modelcontextprotocol.io/ (and the introduction page)
- **Access Date:** 2026-08-03
- **Access Result:** Blocked (domain — `modelcontextprotocol.io` not in WebFetch allow-list; same restriction observed in Sprint 2)
- **Claims Checked:**
  - MCP specification exists at the canonical URL
  - Anthropic as primary maintainer
  - Open standard positioning
  - 2024-11 launch window
- **Evidence Location:** WebSearch snippet "Model Context Protocol MCP open standard specification site 2024 2025" referenced "Anthropic project announcement + community corroborations" but the canonical primary page was not opened.
- **License Checked:** Not reachable
- **Maintenance Checked:** Not reachable
- **Outcome:** **Inaccessible**
- **Notes:** Per §15, no upgrade. The Source Register row remains `Partially Verified`. A future verifier should open `modelcontextprotocol.io` and confirm the spec home, license notice, and version history.

### VR-005 — GitHub Spec Kit (SRC-025)

- **Verification ID:** VR-005
- **Source ID:** SRC-025
- **Original URL:** https://github.com/github/spec-kit
- **Access Date:** 2026-08-03
- **Access Result:** Blocked (domain — `github.com` not in WebFetch allow-list)
- **Claims Checked:**
  - Full repo name (`github/spec-kit`)
  - README positioning ("Spec-Driven Development")
  - LICENSE presence and type
  - Latest release (v... series mentioned in WebSearch)
  - Supported agents (Copilot, Claude Code, Gemini CLI)
- **Evidence Location:** WebSearch snippet for `"github/spec-kit" spec driven development repository release 2025` returned: URL `https://github.com/github/spec-kit`, documentation at `https://github.github.io/spec-kit/`, "Maintainer: GitHub's official team", "Created: August 21, 2025", "Stats (as of June 2026): ~108,392 Stars / 9,588 Forks". Community summary describes Specify → Plan → Tasks → Implement workflow.
- **License Checked:** Not reachable (LICENSE file not opened)
- **Maintenance Checked:** Not reachable (no Release / Tag page opened). **WebSearch snippet gives a creation date of 2025-08-21; this is a third-party summary, not a verified primary fact.**
- **Outcome:** **Inaccessible**
- **Notes:** Per §15, no upgrade. The WebSearch snippet supplies useful orientation (date, maintainer, feature description), but the brief explicitly forbids treating search snippets as primary access. A future verifier should: (a) open the README and confirm the SDD positioning; (b) read LICENSE for the license type; (c) read the latest Release notes; (d) confirm the supported-agents list from the official docs site `github.github.io/spec-kit`.

### VR-006 — OpenSpec (SRC-026)

- **Verification ID:** VR-006
- **Source ID:** SRC-026
- **Original URL:** https://github.com/Fission-AI/OpenSpec
- **Access Date:** 2026-08-03
- **Access Result:** Blocked (domain — `github.com` not in WebFetch allow-list)
- **Claims Checked:**
  - Full repo name (`Fission-AI/OpenSpec`)
  - README positioning
  - LICENSE presence and type
  - Latest release (v0.17.0 referenced)
  - Maintainer organization
- **Evidence Location:** WebSearch snippet for `"Fission-AI/OpenSpec"` references `SRC-026` and a "v0.17.0 referenced 2026-06" note from Sprint 2. Repo existence corroborated by multiple search hits.
- **License Checked:** Not reachable
- **Maintenance Checked:** Not reachable. **Version 0.17.0 (2026-06) is a third-party summary claim.**
- **Outcome:** **Inaccessible**
- **Notes:** Per §15, no upgrade. A future verifier should confirm the repo's full name, LICENSE, latest release tag, and README positioning.

### VR-007 — ADR (Nygard blog post) (SRC-002)

- **Verification ID:** VR-007
- **Source ID:** SRC-002
- **Original URL:** https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions
- **Access Date:** 2026-08-03
- **Access Result:** Blocked (domain — `cognitect.com` not in WebFetch allow-list)
- **Claims Checked:**
  - Author identity (Michael Nygard)
  - Publication date (2011-11-15)
  - Title ("Documenting Architecture Decisions")
  - ADR template sections (Status, Context, Decision, Consequences)
- **Evidence Location:** WebSearch snippet for "Architecture Decision Record Michael Nygard ADR introduction blog post date" referenced "cognitect.com blog post + adr.github.io" but the canonical Nygard post was not opened. Community sources (`adr.github.io`) provide corroboration of the template structure but are independent of the Nygard page.
- **License Checked:** Not reachable
- **Maintenance Checked:** Not applicable (historical artifact)
- **Outcome:** **Inaccessible**
- **Notes:** Per §15, no upgrade. The Nygard blog post is the canonical primary source for the ADR convention; without direct access, the Source Register row remains `Partially Verified` based on `adr.github.io` and community summaries. A future verifier should open the Nygard post and confirm author, date, and the four-section template.

### VR-008 — Continuous Discovery (Torres) (SRC-008, SRC-012, SRC-036)

- **Verification ID:** VR-008
- **Source ID:** SRC-008 (book), SRC-012 (Product Talk), SRC-036 (publisher)
- **Original URL:** https://www.producttalk.org/2021/04/continuous-discovery-habits/ (publisher page)
- **Access Date:** 2026-08-03
- **Access Result:** Blocked (domain — `producttalk.org` not in WebFetch allow-list)
- **Claims Checked:**
  - Author (Teresa Torres)
  - Publisher (Product Talk / Brown Paper Tickets / Kindle etc.)
  - Publication year (2021)
  - Framework name ("Continuous Discovery Habits")
  - Opportunity Solution Tree as core visual
- **Evidence Location:** WebSearch snippet for "Continuous Discovery Teresa Torres book Product Talk opportunity solution tree" referenced "Product Talk publisher pages" but no publisher page was opened. Community corroboration exists but is not direct access.
- **License Checked:** Not applicable (book)
- **Maintenance Checked:** Not applicable (book, fixed edition)
- **Outcome:** **Inaccessible**
- **Notes:** Per §15, no upgrade. A future verifier should confirm author, publisher, year, and the Opportunity Solution Tree diagram description from the Product Talk publisher page.

### VR-009 — Inspired (Cagan / SVPG) (SRC-009, SRC-035)

- **Verification ID:** VR-009
- **Source ID:** SRC-009
- **Original URL:** https://svpg.com/inspired/
- **Access Date:** 2026-08-03
- **Access Result:** Not probed in Sprint 2.2 (expected blocked per Sprint 2 pattern; not WebFetched in this sprint)
- **Claims Checked:**
  - Author (Marty Cagan)
  - Publisher (SVPG / Wiley)
  - First-edition year (2008)
  - Core framing ("product discovery vs delivery teams", "empowered teams")
- **Evidence Location:** Sprint 2 WebSearch snippet recorded "SVPG site" corroboration.
- **License Checked:** Not applicable
- **Maintenance Checked:** Not applicable
- **Outcome:** **Inaccessible**
- **Notes:** Per §15, no upgrade. The source remains `Partially Verified` per Sprint 2.1. A future verifier should open the SVPG book page directly.

### VR-010 — Shape Up (Basecamp / Singer) (SRC-011, SRC-037)

- **Verification ID:** VR-010
- **Source ID:** SRC-011
- **Original URL:** https://basecamp.com/shapeup
- **Access Date:** 2026-08-03
- **Access Result:** Not probed in Sprint 2.2 (expected blocked per Sprint 2 pattern)
- **Claims Checked:**
  - Author (Ryan Singer)
  - Publisher / host (Basecamp)
  - Free online availability
  - Shaping / Betting / Building cycle
  - 2019 publication
- **Evidence Location:** Sprint 2 WebSearch snippet recorded "basecamp.com/shapeup corroboration".
- **License Checked:** Not applicable (free online book)
- **Maintenance Checked:** Not applicable
- **Outcome:** **Inaccessible**
- **Notes:** Per §15, no upgrade. A future verifier should open `basecamp.com/shapeup` and confirm the table of contents, the 6-week cycle framing, and the free-online status.

### VR-011 — Lean Startup (Ries) (SRC-010)

- **Verification ID:** VR-011
- **Source ID:** SRC-010
- **Original URL:** https://theleanstartup.com/
- **Access Date:** 2026-08-03
- **Access Result:** Not probed in Sprint 2.2 (expected blocked per Sprint 2 pattern)
- **Claims Checked:**
  - Author (Eric Ries)
  - 2011 publication
  - Build-Measure-Learn methodology
- **Evidence Location:** Sprint 2 WebSearch snippet recorded "theleanstartup.com corroboration".
- **License Checked:** Not applicable
- **Maintenance Checked:** Not applicable
- **Outcome:** **Inaccessible**
- **Notes:** Per §15, no upgrade. A future verifier should confirm author, year, and methodology framing from the canonical site.

### VR-012 — Jobs to Be Done (Christensen / Ulwick) (SRC-013, SRC-038)

- **Verification ID:** VR-012
- **Source ID:** SRC-013
- **Original URL:** Strategyn site and Christensen publisher pages
- **Access Date:** 2026-08-03
- **Access Result:** Not probed in Sprint 2.2
- **Claims Checked:**
  - Christensen / Ulwick attribution dispute
  - Foundational theory year
  - Quantitative outcome-based segmentation
- **Evidence Location:** Sprint 2 WebSearch snippet recorded "Strategyn site + community sources".
- **License Checked:** Not applicable
- **Maintenance Checked:** Not applicable
- **Outcome:** **Inaccessible**
- **Notes:** Per §15, no upgrade. The attribution dispute is a known item per Sprint 2.1; without direct access, it remains `Partially Verified`. A future verifier should open Strategyn, the Christensen publisher pages, and the Ulwick publisher pages to confirm dates and authorship.

### VR-013 — NIST SSDF SP 800-218 (SRC-003, SRC-050)

- **Verification ID:** VR-013
- **Source ID:** SRC-003
- **Original URL:** https://csrc.nist.gov/publications/detail/sp/800-218/final
- **Access Date:** 2026-08-03
- **Access Result:** Blocked (domain — `csrc.nist.gov` not in WebFetch allow-list)
- **Claims Checked:**
  - Document number (`SP 800-218`)
  - Publication date (2022-02)
  - Title ("Secure Software Development Framework")
  - Version (1.1)
  - Status (`Final`)
- **Evidence Location:** WebSearch snippet referenced "NIST CSRC + Synopsys mapping" but the canonical NIST page was not opened. Synopsys mapping is a third-party secondary source.
- **License Checked:** Not reachable
- **Maintenance Checked:** Not reachable
- **Outcome:** **Inaccessible**
- **Notes:** Per §15, no upgrade. A future verifier should open the NIST CSRC publication page and confirm document number, version, publication date, and final status.

### VR-014 — OWASP SAMM v2 (SRC-004)

- **Verification ID:** VR-014
- **Source ID:** SRC-004
- **Original URL:** https://owaspsamm.org/v2-0/
- **Access Date:** 2026-08-03
- **Access Result:** Blocked (domain — `owaspsamm.org` not in WebFetch allow-list)
- **Claims Checked:**
  - Project name (`SAMM`)
  - Version line (v2)
  - OWASP governance
  - License (CC-BY-SA per community reports)
  - Latest revision date
- **Evidence Location:** WebSearch snippet referenced "owaspsamm.org" but no page was opened.
- **License Checked:** Not reachable. Community reports indicate CC-BY-SA; this is unverified.
- **Maintenance Checked:** Not reachable
- **Outcome:** **Inaccessible**
- **Notes:** Per §15, no upgrade. A future verifier should confirm version, license, and latest revision date from the canonical project page.

### VR-015 — OWASP ASVS v4 (SRC-005)

- **Verification ID:** VR-015
- **Source ID:** SRC-005
- **Original URL:** https://owasp.org/www-project-application-security-verification-standard/
- **Access Date:** 2026-08-03
- **Access Result:** Blocked (domain — `owasp.org` not in WebFetch allow-list)
- **Claims Checked:**
  - Version (4.0.3 per Sprint 2 community report)
  - 2021-10 publication date
  - OWASP governance
- **Evidence Location:** WebSearch snippet referenced "OWASP project page".
- **License Checked:** Not reachable
- **Maintenance Checked:** Not reachable
- **Outcome:** **Inaccessible**
- **Notes:** Per §15, no upgrade.

### VR-016 — ISO/IEC/IEEE 12207:2026 (SRC-006)

- **Verification ID:** VR-016
- **Source ID:** SRC-006
- **Original URL:** https://www.iso.org/standard/90219.html
- **Access Date:** 2026-08-03
- **Access Result:** Blocked (domain — `www.iso.org` not in WebFetch allow-list)
- **Claims Checked:**
  - Standard number (`ISO/IEC/IEEE 12207:2026`)
  - Edition (2)
  - Publication date (2026-04)
  - Title ("Systems and software engineering — Software life cycle processes")
  - Supersedes relationship to ISO/IEC/IEEE 12207:2017
- **Evidence Location:** WebSearch snippet referenced "iso.org/standard/90219.html" but no ISO page was opened.
- **License Checked:** Not applicable (paywalled standard)
- **Maintenance Checked:** Not applicable
- **Outcome:** **Inaccessible**
- **Notes:** Per §15, no upgrade. The paywall status of ISO standards is acknowledged and recorded; no upgrade to `Verified` is possible without direct page access to the ISO listing. A future verifier should open the canonical ISO page and confirm number, edition, and publication date.

### VR-017 — ISO/IEC/IEEE 12207:2017 (SRC-052)

- **Verification ID:** VR-017
- **Source ID:** SRC-052
- **Original URL:** https://www.iso.org/standard/63712.html (canonical 2017 URL)
- **Access Date:** 2026-08-03
- **Access Result:** Blocked (domain — `www.iso.org` not in WebFetch allow-list)
- **Claims Checked:**
  - Standard number (`ISO/IEC/IEEE 12207:2017`)
  - Edition (1, historical)
  - Publication date (2017-11)
  - Superseded-by relationship to ISO/IEC/IEEE 12207:2026
- **Evidence Location:** WebSearch snippets did not directly resolve the 2017 ISO page in this sprint.
- **License Checked:** Not applicable
- **Maintenance Checked:** Not applicable
- **Outcome:** **Inaccessible**
- **Notes:** Per §15, no upgrade.

### VR-018 — DORA / Accelerate (SRC-007)

- **Verification ID:** VR-018
- **Source ID:** SRC-007
- **Original URL:** https://dora.dev/
- **Access Date:** 2026-08-03
- **Access Result:** Not probed in Sprint 2.2 (expected blocked per Sprint 2 pattern)
- **Claims Checked:**
  - Annual report cadence since 2014
  - Sponsorship by Google Cloud / DORA
  - Metric framework (deployment frequency, lead time, change fail rate, MTTR)
- **Evidence Location:** Sprint 2 WebSearch snippet recorded "dora.dev".
- **License Checked:** Not applicable
- **Maintenance Checked:** Not applicable
- **Outcome:** **Inaccessible**
- **Notes:** Per §15, no upgrade.

### VR-019 — SRE Book (Google) (SRC-049)

- **Verification ID:** VR-019
- **Source ID:** SRC-049
- **Original URL:** https://sre.google/sre-book/table-of-contents/
- **Access Date:** 2026-08-03
- **Access Result:** Not probed in Sprint 2.2 (expected blocked per Sprint 2 pattern)
- **Claims Checked:**
  - Title ("Site Reliability Engineering")
  - Authors (Beyer, Jones, Petoff, Murphy)
  - Publisher (O'Reilly / Google)
  - SLO and error budget concepts
- **Evidence Location:** Sprint 2 WebSearch snippet recorded "sre.google corroboration".
- **License Checked:** Not applicable
- **Maintenance Checked:** Not applicable
- **Outcome:** **Inaccessible**
- **Notes:** Per §15, no upgrade.

### VR-020 — DHS / CISA Software Attestation (SRC-051)

- **Verification ID:** VR-020
- **Source ID:** SRC-051
- **Original URL:** CISA Software Attestation page
- **Access Date:** 2026-08-03
- **Access Result:** Not probed in Sprint 2.2
- **Claims Checked:**
  - Federal attestation guidance
  - Issuer (DHS / CISA)
  - Publication year
- **Evidence Location:** Sprint 2 WebSearch snippet referenced "community-reported".
- **License Checked:** Not applicable
- **Maintenance Checked:** Not applicable
- **Outcome:** **Inaccessible**
- **Notes:** Per §15, no upgrade.

### VR-021 — arXiv 2602.11988 (SRC-044)

- **Verification ID:** VR-021
- **Source ID:** SRC-044
- **Original URL:** https://arxiv.org/abs/2602.11988
- **Access Date:** 2026-08-03
- **Access Result:** Blocked (domain — `arxiv.org` not in WebFetch allow-list)
- **Claims Checked:**
  - arXiv ID
  - Title
  - Authors (per Sprint 2.1: Thibaud Gloaguen, Niels Mündler, Mark Müller, Veselin Raychev, Martin Vechev)
  - Submission date (2026-02-12)
  - Affiliation (SRI Lab, ETH Zurich per community sources)
  - Abstract / research question / experimental setup / results / limitations
- **Evidence Location:** WebSearch results for "2602.11988 Gloaguen Mundler Muller Raychev Vechev 2026" did not surface the canonical arXiv abstract; a search for "AGENTS.md Gloaguen ETH Zurich 2026" surfaced a Chinese-language summary at `https://so.html5.qq.com/page/real/search_news?docid=70000021_29269b7d50a72752` titled "新研究重新评估 AGENTS.md 文件在 AI 编码中的价值" describing: 4 agents (Claude 3.5 Sonnet, Codex GPT-5.2, GPT-5.1 mini, Qwen Code); three scenarios (no context file, LLM-generated, human-written); conclusion that AGENTS.md may often hinder AI coding agents and that instructions should be limited to non-inferable details. **This is a secondary news summary, not the primary source.**
- **License Checked:** Not reachable
- **Maintenance Checked:** Not applicable (paper)
- **Outcome:** **Inaccessible**
- **Notes:** Per §15, no upgrade. The arXiv ID `2602.11988` could not be opened. The WebSearch did not return a direct hit on the canonical arXiv abstract; the secondary news summary does not confirm the full title, author list, or specific experimental figures. A future verifier must open the arXiv abstract page directly and confirm: arXiv ID, full title, author list with affiliations, submission date, abstract text, experimental design, results table, and explicit limitations.

### VR-022 — arXiv 2601.20404 (SRC-045)

- **Verification ID:** VR-022
- **Source ID:** SRC-045
- **Original URL:** https://arxiv.org/abs/2601.20404
- **Access Date:** 2026-08-03
- **Access Result:** Blocked (domain — `arxiv.org` not in WebFetch allow-list)
- **Claims Checked:**
  - arXiv ID
  - Title
  - Authors
  - Submission date (2026-01-28 per Sprint 2.1)
  - Abstract / research question / experimental setup / results / limitations
  - Direction of finding (faster / less tokens vs. SRC-044)
- **Evidence Location:** WebSearch for `"2601.20404" arxiv AGENTS.md efficiency AI coding agents 2026` returned no direct hit on the paper. The search results were unrelated (CSDN tutorials, GitHub Topics, AI-coding-agents repositories). No secondary news summary was found that substantiates the SRC-045 entry.
- **License Checked:** Not reachable
- **Maintenance Checked:** Not applicable
- **Outcome:** **Inaccessible**
- **Notes:** Per §15, no upgrade. The arXiv ID `2601.20404` could not be opened, and **no WebSearch result corroborates its existence, title, authors, or findings**. The Sprint 2.1 Source Register entry is currently based on a citation whose primary source was not reachable during Sprint 2 either. **This is a higher-risk item than SRC-044** because no community corroboration surfaced in this sprint's WebSearch. A future verifier must: (a) open `arxiv.org/abs/2601.20404` and confirm whether the paper exists; (b) record the actual title, authors, and submission date; (c) note the direction of the empirical finding for comparison with SRC-044. **If the paper does not exist, SRC-045 must be retracted from `source-register.md` as part of the next sprint, not silently retained.**

---

## Summary of Verification Outcomes

| Outcome | Count | Sources |
|---|---|---|
| `Verified` | 0 | — |
| `Partially Verified` (no change) | 0 | — |
| `Unverified` (no change) | 0 | — |
| `Contradicted` | 0 | — |
| `Inaccessible` | 22 | VR-001 through VR-022 |
| **Total attempts** | **22** | |

**No source was upgraded from `Partially Verified` to `Verified`** during Sprint 2.2. The 10-condition rule from the brief could not be met for any priority source because the access window does not allow direct primary page retrieval.

## Sources Flagged for External Verification

Per Sprint 2.2 brief §15, the following sources require verification by a researcher with network access to the canonical primary pages. Each item names what must be confirmed.

| Source | What must be verified | Reason it could not be verified here |
|---|---|---|
| SRC-001 (AGENTS.md) | Homepage wording, governance (AAIF?), adoption figure, license | `agents.md` blocked |
| SRC-002 (Nygard ADR) | Author, 2011-11-15 date, 4-section template | `cognitect.com` blocked |
| SRC-003 (NIST SSDF) | SP 800-218, version, 2022-02 date, final status | `csrc.nist.gov` blocked |
| SRC-004 (OWASP SAMM v2) | Version, license, latest revision date | `owaspsamm.org` blocked |
| SRC-005 (OWASP ASVS v4) | Version 4.0.3, 2021-10 date | `owasp.org` blocked |
| SRC-006 (ISO 12207:2026) | Standard number, Edition 2, 2026-04 date | `iso.org` blocked |
| SRC-014 (Claude Code) | Positioning, AGENTS.md support, feature list | `docs.claude.com` blocked |
| SRC-015 (OpenAI Codex CLI) | Repo name, LICENSE, latest release | `github.com` blocked |
| SRC-025 (Spec Kit) | Repo name, LICENSE, latest release, SDD positioning | `github.com` blocked |
| SRC-026 (OpenSpec) | Repo name, LICENSE, latest release | `github.com` blocked |
| SRC-027 (MCP) | Spec home, license, version history | `modelcontextprotocol.io` blocked |
| SRC-044 (arXiv 2602.11988) | arXiv abstract, authors, submission date, experimental setup, results, limitations | `arxiv.org` blocked |
| SRC-045 (arXiv 2601.20404) | **Existence check first**, then title, authors, date, direction of finding | `arxiv.org` blocked; no community corroboration found |

## Process Notes

- All 22 attempts were made on 2026-08-03 during the Sprint 2.2 access window.
- No search-result snippet was treated as direct primary access. Where snippets were used, they are clearly labeled as such in the Evidence Location field.
- No source was upgraded to `Verified` because the 10-condition rule requires direct page access and the access window does not permit it for any priority source.
- No fabrication: every Access Result is honestly reported. Where the domain was not probed at all (e.g., `svpg.com`, `basecamp.com`, `theleanstartup.com`, `dora.dev`, `sre.google`), the entry records `Not probed in Sprint 2.2` rather than a false `Success`.
- The `Outcome` column is determined by the brief's 10-condition rule, not by the agent's optimism.

---

## External Verification Reconciliation (Sprint 2.3, 2026-08-03)

Sprint 2.3 reconciles six sources via an external verifier with direct primary-source access. The original 22 Sprint 2.2 Inaccessible rows above are preserved verbatim — they record the Claude-side access barrier, not the external reviewer's success. The new section below is the canonical record of the EV-### entries.

### Schema (External Verification, 8 fields per Sprint 2.3 brief §5)

| # | Field | Description |
|---|---|---|
| 1 | External Verification ID | `EV-###` identifier (sequential) |
| 2 | Source ID | `SRC-NNN` from `research/source-register.md` |
| 3 | Canonical URL | The canonical primary URL that was directly accessed |
| 4 | Verification Date | `2026-08-03` for every Sprint 2.3 entry |
| 5 | Verifier Type | `External reviewer with direct primary-source access` |
| 6 | Claims Verified | The specific factual claims that were verified (1–5 bullets) |
| 7 | Remaining Limitations | Items that remain `Partially Verified` because the PDF body, full text, or downstream pages were not directly read |
| 8 | Outcome | `Verified` (claim type + key metadata directly observed) or `Partially Verified` (only metadata/abstract verified, not full body) |

### Reconciliation

| EV-### | Source ID | Canonical URL | Verification Date | Verifier Type | Claims Verified | Remaining Limitations | Outcome |
|---|---|---|---|---|---|---|---|
| EV-001 | SRC-001 | https://agents.md/ | 2026-08-03 | External reviewer with direct primary-source access | (1) Page title is `AGENTS.md`. (2) Page defines AGENTS.md as a simple open format for guiding coding agents, framed as a "README for agents". (3) Page describes the format covering build, test, code-style, security, and contribution rules. (4) Page declares adoption by over 60,000 open-source projects (project-maintainer-reported figure — not independently audited). (5) Page describes it as an open format developed via cross-ecosystem collaboration among multiple coding-agent projects. | (a) AAIF governance claim and explicit version/license notice on the homepage still require confirmation; (b) the 60k+ adoption figure is maintainer-reported and is not recorded as independent market share. | Verified |
| EV-002 | SRC-015 | https://github.com/openai/codex | 2026-08-03 | External reviewer with direct primary-source access | (1) Repository exists at `openai/codex`. (2) README positions it as a coding agent running in the local terminal. (3) Repository contains CLI, Rust implementation, documentation, and SDK directories. (4) Official repository License is Apache-2.0. (5) Repository is actively maintained — numerous commits and releases observed at access date. | Precise Star / Commit / Release counts are intentionally not recorded (these numbers change). Dynamic counters are deliberately omitted from the Source Register. | Verified |
| EV-003 | SRC-044 | https://arxiv.org/abs/2602.11988 | 2026-08-03 | External reviewer with direct primary-source access | (1) arXiv ID `2602.11988`. (2) Title `Evaluating AGENTS.md: Are Repository-Level Context Files Helpful for Coding Agents?`. (3) Authors: Thibaud Gloaguen, Niels Mündler, Mark Müller, Veselin Raychev, Martin Vechev. (4) v1 submitted 2026-02-12; v2 revised 2026-06-23. (5) Abstract-supported core findings: covers SWE-bench tasks and repository problems with developer-submitted context files; context files generally did not improve task success; mean inference cost increased by over 20%; agents typically follow instructions; non-standard engineering requirements may be useful but repository overviews and unnecessary requirements should be used with caution. | (a) Method details and full-text limitations beyond the abstract remain `Partially Verified` (PDF body not directly read). (b) The findings cannot be generalized to all repositories, models, agents, or tasks; experimental setup must be cited. (c) The "AGENTS.md is always harmful" generalization is not supported. | Verified |
| EV-004 | SRC-045 | https://arxiv.org/abs/2601.20404 | 2026-08-03 | External reviewer with direct primary-source access | (1) arXiv ID `2601.20404`. (2) Title `On the Impact of AGENTS.md Files on the Efficiency of AI Coding Agents`. (3) Authors: Jai Lal Lulla, Seyedmoein Mohsenimofidi, Matthias Galster, Jie M. Zhang, Sebastian Baltes, Christoph Treude. (4) v1 submitted 2026-01-28; v2 revised 2026-03-30. (5) Abstract-supported core findings: 10 repositories and 124 Pull Requests analyzed; AGENTS.md associated with lower median runtime; associated with lower output-token consumption; task-completion performance was roughly comparable. | (a) Method details beyond the abstract remain `Partially Verified` (PDF body not directly read). (b) "Correlation" is not automatically "causation". (c) The paper's tasks, models, agents, metrics, and research design differ from SRC-044; results are not directly comparable. | Verified |
| EV-005 | SRC-006 | https://www.iso.org/standard/90219.html | 2026-08-03 | External reviewer with direct primary-source access | (1) Standard number `ISO/IEC/IEEE 12207:2026`. (2) Title `Systems and software engineering — Software life cycle processes`. (3) Edition 2. (4) Publication date 2026-04. (5) Status: Published. The official ISO page lists the 2017 edition as the previous version. | Full text is paywalled. Only public metadata and abstract are verified. No claim is made about reading or verifying the paywalled full text. | Verified |
| EV-006 | SRC-003 | https://csrc.nist.gov/pubs/sp/800/218/final | 2026-08-03 | External reviewer with direct primary-source access | (1) Document number `NIST SP 800-218`. (2) Title `Secure Software Development Framework (SSDF) Version 1.1`. (3) Publication date 2022-02. (4) Authors: Murugiah Souppaya, Karen Scarfone, Donna Dodson. (5) Official summary: most SDLCs do not address software security in detail; SSDF provides high-level secure-development practices that can be integrated into any SDLC; goals include reducing published-software vulnerabilities, lowering the impact of exploited vulnerabilities, and addressing root causes. | (a) Full document text not verified line-by-line. (b) SSDF is a security practices framework, not a complete product-engineering standard; description is limited to what the official page exposes. | Verified |

### Sprint 2.2 vs Sprint 2.3 — Verification Attempts vs Source Counts

Per Sprint 2.3 brief §3, the following is the unambiguous statistic for the Sprint 2.2 verification log:

```
Verification attempts: 22
Unique verification IDs: 22
Unique source IDs attempted: 24
Repeated source IDs: none
```

The Attempt count (22) and the Source count (24) are not the same number, because some VR rows reference multiple Source IDs (e.g., VR-008 covers SRC-008 + SRC-012 + SRC-036; VR-013 covers SRC-003 + SRC-050; VR-012 covers SRC-013). All 22 VR IDs are unique; no Source ID was attempted twice.

### Notes on Reconciliation

- The 22 Sprint 2.2 Inaccessible rows are **not** edited to reflect Sprint 2.3 outcomes. They record the Claude-side access barrier and remain a true process record.
- The Sprint 2.3 EV-### entries do not invalidate the Sprint 2.2 statistics. They are a separate reporting dimension: "what Claude could verify directly" vs. "what was verified by an external reviewer with network access."
- Six sources were upgraded from `Partially Verified` to `Verified` in the Source Register (SRC-001, SRC-003, SRC-006, SRC-015, SRC-044, SRC-045). SRC-045 is **not** retracted; its existence, title, authors, dates, and abstract are confirmed by EV-004.
- The remaining 14 currently `Unverified` sources and 32 currently `Partially Verified` sources are unchanged by Sprint 2.3 and remain to be verified in a future sprint with broader access.

### Cross-References (Sprint 2.3)

- `research/source-register.md` — the 6 upgraded rows record the EV-### identifier in the Notes column.
- `tasks/sprint-02-3-external-verification-reconciliation.md` — Sprint 2.3 task file.

### Cross-References

- `research/source-register.md` — the underlying 52 sources.
- `research/ecosystem/inventory.md` — descriptive catalog using these sources.
- `research/competitors/candidate-projects.md` — Selected list.
- `research/competitors/reverse-research.md` — 10 Selected projects analyzed using the 14-section template.
- `tasks/sprint-02-2-primary-source-verification.md` — the Sprint 2.2 task file.
- `tasks/sprint-02-3-external-verification-reconciliation.md` — the Sprint 2.3 task file.

---

## Targeted Primary-Source Re-verification (Sprint 2.4, 2026-08-15)

This section records direct primary-source access performed during Sprint 2.4. The Sprint 2.2 VR-001 through VR-022 records and the Sprint 2.3 EV-001 through EV-006 records above are preserved unchanged. Search-result summaries and third-party restatements were not used to promote any source.

### VR-023 — SRC-017 (aider)

- **Verification ID:** VR-023
- **Source ID:** SRC-017
- **Original URL:** https://github.com/Aider-AI/aider
- **Access Date:** 2026-08-15
- **Access Result:** Success
- **Claims Checked:** Repository existence; README positioning as “AI Pair Programming in Your Terminal” and pair programming with LLMs; license name; maintenance signal.
- **Evidence Location:** Canonical repository; https://raw.githubusercontent.com/Aider-AI/aider/main/README.md; https://raw.githubusercontent.com/Aider-AI/aider/main/LICENSE.txt; https://api.github.com/repos/Aider-AI/aider/commits/main; https://api.github.com/repos/Aider-AI/aider/releases/latest
- **License Checked:** Yes — `LICENSE.txt` contains Apache License, Version 2.0.
- **Maintenance Checked:** Yes — latest observed `main` commit dated 2026-05-22; latest observed release v0.86.0 dated 2025-08-09. Maintenance: Active at access date (2026-08-15).
- **Outcome:** Verified
- **Notes:** No dynamic star, commit-total, or release-total count recorded. Project-maintainer positioning is not independent effectiveness evidence.

### VR-024 — SRC-018 (Cline)

- **Verification ID:** VR-024
- **Source ID:** SRC-018
- **Original URL:** https://github.com/cline/cline
- **Access Date:** 2026-08-15
- **Access Result:** Success
- **Claims Checked:** Repository existence; README positioning as an open-source coding agent in the IDE and terminal; documented CLI, VS Code, JetBrains, and SDK surfaces; license name; maintenance signal.
- **Evidence Location:** Canonical repository; https://raw.githubusercontent.com/cline/cline/main/README.md; https://raw.githubusercontent.com/cline/cline/main/LICENSE; https://api.github.com/repos/cline/cline/commits/main; https://api.github.com/repos/cline/cline/releases/latest
- **License Checked:** Yes — `LICENSE` contains Apache License, Version 2.0.
- **Maintenance Checked:** Yes — latest observed `main` commit dated 2026-08-14; latest observed release `desktop-v0.0.13` dated 2026-08-14. Maintenance: Active at access date (2026-08-15).
- **Outcome:** Verified
- **Notes:** Precise rename history was not checked. No dynamic counters recorded.

### VR-025 — SRC-019 (OpenHands)

- **Verification ID:** VR-025
- **Source ID:** SRC-019
- **Original URL:** https://github.com/All-Hands-AI/OpenHands
- **Access Date:** 2026-08-15
- **Access Result:** Success (redirected to `OpenHands/OpenHands`)
- **Claims Checked:** Repository existence and current canonical path; current README positioning of Agent Canvas as a self-hosted developer control center for coding agents and automations; license name; maintenance signal.
- **Evidence Location:** https://github.com/OpenHands/OpenHands; https://raw.githubusercontent.com/OpenHands/OpenHands/main/README.md; https://raw.githubusercontent.com/OpenHands/OpenHands/main/LICENSE; https://api.github.com/repos/All-Hands-AI/OpenHands; https://api.github.com/repos/OpenHands/OpenHands/commits/main; https://api.github.com/repos/OpenHands/OpenHands/releases/latest
- **License Checked:** Yes — `LICENSE` contains the MIT License.
- **Maintenance Checked:** Yes — latest observed `main` commit dated 2026-08-14; latest observed release v1.13.0 dated 2026-08-13. Maintenance: Active at access date (2026-08-15).
- **Outcome:** Verified
- **Notes:** The current canonical path and README positioning differ from the earlier All-Hands-AI autonomous-software-engineering-agent framing; the current primary evidence controls this record.

### VR-026 — SRC-020 (OpenCode)

- **Verification ID:** VR-026
- **Source ID:** SRC-020
- **Original URL:** https://github.com/opencode-ai/opencode
- **Access Date:** 2026-08-15
- **Access Result:** Success
- **Claims Checked:** Repository existence; README historical positioning as a terminal-based AI assistant and move notice; license name; maintenance/archive signal.
- **Evidence Location:** Canonical repository; https://raw.githubusercontent.com/opencode-ai/opencode/main/README.md; https://raw.githubusercontent.com/opencode-ai/opencode/main/LICENSE; https://api.github.com/repos/opencode-ai/opencode; https://api.github.com/repos/opencode-ai/opencode/commits/main; https://api.github.com/repos/opencode-ai/opencode/releases/latest
- **License Checked:** Yes — `LICENSE` contains the MIT License.
- **Maintenance Checked:** Yes — latest observed `main` commit dated 2025-09-18; repository metadata reports `archived: true`. Maintenance: Archived at access date (2026-08-15).
- **Outcome:** Verified
- **Notes:** The README states that the project moved and names a successor. No claim of active maintenance is made.

### VR-027 — SRC-021 (Continue)

- **Verification ID:** VR-027
- **Source ID:** SRC-021
- **Original URL:** https://github.com/continuedev/continue
- **Access Date:** 2026-08-15
- **Access Result:** Success
- **Claims Checked:** Repository existence; README positioning of the coding-agent CLI and VS Code / JetBrains extensions; official read-only notice; license name; maintenance signal.
- **Evidence Location:** Canonical repository; https://raw.githubusercontent.com/continuedev/continue/main/README.md; https://raw.githubusercontent.com/continuedev/continue/main/LICENSE; https://api.github.com/repos/continuedev/continue; https://api.github.com/repos/continuedev/continue/commits/main; https://api.github.com/repos/continuedev/continue/releases/latest
- **License Checked:** Yes — `LICENSE` contains Apache License, Version 2.0.
- **Maintenance Checked:** Yes — README states that the repository is no longer actively maintained and is read-only; final release v2.0.0 dated 2026-06-19; latest observed `main` commit dated 2026-07-21. Maintenance: Read-only / no longer actively maintained at access date (2026-08-15).
- **Outcome:** Verified
- **Notes:** GitHub metadata reports `archived: false`, but the explicit README notice controls the maintenance description.

### VR-028 — SRC-022 (Roo Code)

- **Verification ID:** VR-028
- **Source ID:** SRC-022
- **Original URL:** https://github.com/RooCodeInc/Roo-Code
- **Access Date:** 2026-08-15
- **Access Result:** Success
- **Claims Checked:** Repository existence; README positioning as an AI-powered development team in the editor; official shutdown notice; license name; maintenance/archive signal.
- **Evidence Location:** Canonical repository; https://raw.githubusercontent.com/RooCodeInc/Roo-Code/main/README.md; https://raw.githubusercontent.com/RooCodeInc/Roo-Code/main/LICENSE; https://api.github.com/repos/RooCodeInc/Roo-Code; https://api.github.com/repos/RooCodeInc/Roo-Code/commits/main; https://api.github.com/repos/RooCodeInc/Roo-Code/releases/latest
- **License Checked:** Yes — `LICENSE` contains Apache License, Version 2.0.
- **Maintenance Checked:** Yes — latest observed `main` commit and release v3.54.0 dated 2026-05-15; repository metadata reports `archived: true`; README records the extension shutdown. Maintenance: Archived at access date (2026-08-15).
- **Outcome:** Verified
- **Notes:** The README names successor alternatives. Fork lineage was not reconstructed in this sprint.

### VR-029 — SRC-024 (Gemini CLI)

- **Verification ID:** VR-029
- **Source ID:** SRC-024
- **Original URL:** https://github.com/google-gemini/gemini-cli
- **Access Date:** 2026-08-15
- **Access Result:** Success
- **Claims Checked:** Repository existence; README positioning as an open-source AI agent bringing Gemini into the terminal; built-in tools and MCP extensibility; license name; maintenance signal.
- **Evidence Location:** Canonical repository; https://raw.githubusercontent.com/google-gemini/gemini-cli/main/README.md; https://raw.githubusercontent.com/google-gemini/gemini-cli/main/LICENSE; https://api.github.com/repos/google-gemini/gemini-cli/commits/main; https://api.github.com/repos/google-gemini/gemini-cli/releases/latest
- **License Checked:** Yes — `LICENSE` contains Apache License, Version 2.0.
- **Maintenance Checked:** Yes — latest observed `main` commit dated 2026-08-13; latest observed release v0.55.1 dated 2026-08-11. Maintenance: Active at access date (2026-08-15).
- **Outcome:** Verified
- **Notes:** Geo-restriction claims and first-release date were not checked. No dynamic counters recorded.

### VR-030 — SRC-002 (Nygard ADR post)

- **Verification ID:** VR-030
- **Source ID:** SRC-002
- **Original URL:** https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions
- **Access Date:** 2026-08-15
- **Access Result:** Success
- **Claims Checked:** Author; publication date; the four ADR body sections Context, Decision, Status, and Consequences, plus the Title field.
- **Evidence Location:** Canonical Cognitect post at the Original URL; the byline identifies Michael Nygard and 2011-11-15; the format section defines Title, Context, Decision, Status, and Consequences.
- **License Checked:** Yes — the post carries a CC0 waiver.
- **Maintenance Checked:** Not applicable — this is a dated historical practitioner post.
- **Outcome:** Verified
- **Notes:** Verification applies to the canonical template and metadata, not to later ADR variants or independent effectiveness.

### VR-031 — SRC-004 (OWASP SAMM v2)

- **Verification ID:** VR-031
- **Source ID:** SRC-004
- **Original URL:** https://owaspsamm.org/
- **Access Date:** 2026-08-15
- **Access Result:** Success
- **Claims Checked:** Version 2.0; model structure; license; latest revision/maintenance signal.
- **Evidence Location:** https://owaspsamm.org/model/; https://owaspsamm.org/release-notes-v2/; https://github.com/owaspsamm/core; https://api.github.com/repos/owaspsamm/core; https://api.github.com/repos/owaspsamm/core/commits/develop
- **License Checked:** Yes — official site footer and canonical repository identify Creative Commons Attribution-ShareAlike 4.0 (`CC-BY-SA-4.0`).
- **Maintenance Checked:** Yes — latest observed `develop` commit dated 2026-07-06. Maintenance: Active at access date (2026-08-15).
- **Outcome:** Verified
- **Notes:** Direct official pages support version, license, model structure, and activity; they do not independently establish outcome effectiveness.

### VR-032 — SRC-005 (OWASP ASVS)

- **Verification ID:** VR-032
- **Source ID:** SRC-005
- **Original URL:** https://owasp.org/www-project-application-security-verification-standard/
- **Access Date:** 2026-08-15
- **Access Result:** Success
- **Claims Checked:** ASVS purpose; current stable version and release date; historical 4.0.3 version and release date.
- **Evidence Location:** Canonical OWASP project page at the Original URL; the page lists latest stable version 5.0.0, its 2025-05-30 release announcement, and the 4.0.3 release announcement dated 2021-10-28.
- **License Checked:** Not checked — not required for the specific SRC-005 claim in this sprint.
- **Maintenance Checked:** Yes — current stable release 5.0.0 is identified on the directly accessed official page.
- **Outcome:** Verified
- **Notes:** The earlier v4/2021 row was a historical snapshot. Sprint 2.4 records both the current stable version and the historical claim without conflating them.

### VR-033 — SRC-014 (Claude Code)

- **Verification ID:** VR-033
- **Source ID:** SRC-014
- **Original URL:** https://www.anthropic.com/claude-code
- **Access Date:** 2026-08-15
- **Access Result:** Success (official product URL resolved to current official documentation)
- **Claims Checked:** Official positioning; documented feature list; project-instruction file behavior; the flagged AGENTS.md-support claim.
- **Evidence Location:** https://code.claude.com/docs/en/overview; https://code.claude.com/docs/en/memory
- **License Checked:** Not applicable — vendor product documentation, not a repository-license claim.
- **Maintenance Checked:** Not recorded — no release/commit claim was required for SRC-014.
- **Outcome:** Verified
- **Notes:** The overview documents file reading/editing, command execution, terminal/IDE/desktop/browser availability, Git, MCP, CLAUDE.md, skills, hooks, and multi-agent features. The memory page explicitly states that Claude Code reads `CLAUDE.md`, not `AGENTS.md`; `AGENTS.md` can be imported from `CLAUDE.md`, copied during initialization, or referenced through a symlink. Native automatic AGENTS.md loading was not verified and is not claimed.

### VR-034 — SRC-027 (Model Context Protocol)

- **Verification ID:** VR-034
- **Source ID:** SRC-027
- **Original URL:** https://www.anthropic.com/news/model-context-protocol
- **Access Date:** 2026-08-15
- **Access Result:** Success via the current canonical MCP specification and repository
- **Claims Checked:** Specification home and protocol definition; current version; version-history mechanism and dated schema history; license terms; maintenance signal.
- **Evidence Location:** https://modelcontextprotocol.io/specification/latest; https://modelcontextprotocol.io/docs/2026-07-28/learn/versioning; https://github.com/modelcontextprotocol/modelcontextprotocol/tree/main/schema; https://raw.githubusercontent.com/modelcontextprotocol/modelcontextprotocol/main/LICENSE; https://api.github.com/repos/modelcontextprotocol/modelcontextprotocol/commits/main
- **License Checked:** Yes — canonical `LICENSE` records an MIT-to-Apache-2.0 transition: new code/spec contributions are Apache-2.0; documentation outside the specifications is CC BY 4.0; some older contributions remain MIT.
- **Maintenance Checked:** Yes — current specification is 2026-07-28; latest observed repository commit dated 2026-08-14. Maintenance: Active at access date (2026-08-15).
- **Outcome:** Verified
- **Notes:** The repository README's short MIT label is less specific than the controlling transition notice in `LICENSE`; this limitation is preserved rather than flattened to a single license label.

### Sprint 2.4 Outcome

| Metric | Before Sprint 2.4 (actual repository baseline) | After Sprint 2.4 | Change |
|---|---:|---:|---:|
| Total Source IDs | 54 | 54 | 0 |
| Verified | 10 | 22 | +12 |
| Partially Verified | 32 | 22 | -10 |
| Unverified | 12 | 10 | -2 |
| Contradicted | 0 | 0 | 0 |
| Inaccessible (Source Register status) | 0 | 0 | 0 |

All twelve targeted sources were upgraded because the specific claims were directly observed in primary pages. This does not erase the historical Sprint 2.2 access failures.

For the Sprint 2.4 project gate, a conservative repository/project-only count is used: 13 unique projects. It comprises the six already directly verified projects SRC-001, SRC-015, SRC-025, SRC-026, SRC-053, and SRC-054, plus the seven P0 repositories SRC-017, SRC-018, SRC-019, SRC-020, SRC-021, SRC-022, and SRC-024. The five P1 items are not used to inflate the project count.

**Research Gate: `READY FOR REVIEW`.** The current register has 22 Verified sources (threshold ≥15) and 13 directly verified repository/project rows under the conservative Sprint 2.4 counting rule (threshold ≥8). No Source ID was added, removed, or renumbered. Sprint 2 remains `In Review` until maintainer review.

### Sources Still Requiring Direct Primary-Source Verification

- **Partially Verified (22):** SRC-007, SRC-008, SRC-009, SRC-010, SRC-011, SRC-012, SRC-013, SRC-023, SRC-028, SRC-029, SRC-030, SRC-031, SRC-035, SRC-036, SRC-037, SRC-038, SRC-039, SRC-040, SRC-049, SRC-050, SRC-051, SRC-052.
- **Unverified (10):** SRC-016, SRC-032, SRC-033, SRC-034, SRC-041, SRC-042, SRC-043, SRC-046, SRC-047, SRC-048.

### Sprint 2.4 Reconciliation Notes

- The task brief stated a 60-source baseline with 16 Verified sources, while the checked-in v0.6 register actually contained 54 Source IDs with 10 Verified, 32 Partially Verified, and 12 Unverified. Sprint 2.4 uses the checked-in repository as its auditable baseline and does not invent SRC-055 through SRC-060.
- The legacy Sprint 2.2 gate wording refers to directly verified “Selected projects,” while the Sprint 2.4 brief explicitly designates the seven P0 repositories as raising the project count. This section applies the current brief's project/artifact counting rule; maintainers should confirm that interpretation when reviewing the gate.
- No dynamic popularity or repository-total counts were recorded.

### Cross-References (Sprint 2.4)

- `research/source-register.md` — twelve updated source rows, v0.7.
- `research/ecosystem/inventory.md` — synchronized verification states and maintenance caveats.
- `research/competitors/candidate-projects.md` — verification-only candidate reconciliation; no re-ranking.
- `research/competitors/reverse-research.md` — ADR and Claude Code evidence corrections plus P0 status note.
- `tasks/sprint-02-4-targeted-reverification.md` — Sprint 2.4 task file and gate record.
