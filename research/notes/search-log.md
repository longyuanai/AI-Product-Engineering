# research/notes/search-log.md

- Status: Draft
- Version: v0.3
- Owner: APES Maintainers
- Last Updated: 2026-08-05
- Purpose: Record the searches actually executed during Sprint 2 (Ecosystem Inventory & Reverse Research) and Foundation 0.2 (open-source reference comparison). No result counts are fabricated; queries and selected sources are honest. Only processes are recorded; no APES conclusions are written here.

## Search Platform Legend

- **Web Search** — `claude.ai` WebSearch (Microsoft Bing index).
- **Web Fetch** — `claude.ai` WebFetch (direct page fetch). Used only where the domain was reachable.
- **GitHub CLI** — `gh` repository search / API access. In the 2026-08-05 access window the configured token was invalid and sandboxed API access was blocked, so this channel produced no selected result and no credentials were changed.
- **Public GitHub Pages** — Direct read-only access to canonical repository pages and raw repository files through the public web channel.
- **WebSearch was used because `claude.ai` WebFetch rejected GitHub, Anthropic, ISO, NIST, OWASP, and several other domains during Sprint 2.** Result counts are not always displayed by the search backend and are recorded as `not reported` where true.

| Search ID | Query | Platform | Search Date | Filters | Approximate Result Count | Selected Sources | Exclusion Reasons | Notes |
|---|---|---|---|---|---|---|---|---|
| SE-001 | "Claude Code Anthropic agentic coding CLI official documentation AGENTS.md support" | Web Search | 2026-08-03 | None | not reported | SRC-014 | Excluded secondary blog restatements; included vendor / project documentation only. | Vendor documentation captured at SRC-014. |
| SE-002 | "Model Context Protocol MCP open standard specification site 2024 2025" | Web Search | 2026-08-03 | None | not reported | SRC-027 | Excluded marketing-only restatements; relied on Anthropic project announcement + community corroborations. | Anthropic primary announcement page was blocked by WebFetch; third-party sources used to confirm 2024-11 release. |
| SE-003 | "github spec-kit repository description license spec driven development" | Web Search | 2026-08-03 | None | not reported | SRC-025 | Excluded blog restatements; relied on repo metadata + release context. | Repo `github/spec-kit` confirmed as 2025-09 release. |
| SE-004 | "Fission-AI OpenSpec GitHub repository description license" | Web Search | 2026-08-03 | None | not reported | SRC-026 | Excluded package mirrors (npm / CSDN); relied on repository metadata. | v0.17.0 referenced 2026-06. |
| SE-005 | "OpenAI Codex CLI repository description release version 2025" | Web Search | 2026-08-03 | None | not reported | SRC-015 | Excluded blog tutorials; relied on `openai/codex` repo + community release notes. | Open-source release confirmed 2025; Security CLI referenced 2026-07. |
| SE-006 | "Cursor Anysphere IDE AI coding description license 2025" | Web Search | 2026-08-03 | None | not reported | SRC-016 | Excluded third-party reviews; relied on cursor.com + community sources for Cursor 2.0 / Composer. | Cursor 2.0 referenced Oct 2025. |
| SE-007 | "aider chat AI pair programming repository license Paul Gauthier" | Web Search | 2026-08-03 | None | not reported | SRC-017 | Excluded forks; relied on `Aider-AI/aider`. | Repo on github.com reachable via WebSearch snippets only. |
| SE-008 | "cline VS Code AI agent repository license Cline Bot" | Web Search | 2026-08-03 | None | not reported | SRC-018 | Excluded forks; relied on `cline/cline`. | Confirmed rename from Claude Dev to Cline. |
| SE-009 | "OpenHands All-Hands-AI repository license open source autonomous coding" | Web Search | 2026-08-03 | None | not reported | SRC-019 | Excluded forks; relied on `All-Hands-AI/OpenHands`. | Community reports MIT license; confirm in repo. |
| SE-010 | "opencode opencode-ai terminal AI coding tool repository" | Web Search | 2026-08-03 | None | not reported | SRC-020 | Excluded CSDN tutorials; relied on opencode-ai/opencode. | License to verify. |
| SE-011 | "continue.dev repository description license VS Code AI extension" | Web Search | 2026-08-03 | None | not reported | SRC-021 | Excluded local config tutorials; relied on continuedev/continue. | Open-core model noted. |
| SE-012 | "Roo Code Roo-Code repository license AI coding agent VS Code" | Web Search | 2026-08-03 | None | not reported | SRC-022 | Excluded forks and tutorials; relied on RooCodeInc/Roo-Code. | Apache 2.0 inheritance from Cline fork lineage to be re-confirmed. |
| SE-013 | "sourcegraph cody AI coding assistant repository license maintenance status 2025" | Web Search | 2026-08-03 | None | not reported | SRC-031 | Excluded third-party reviews; relied on repo + "last public snapshot" commit reference. | Effective maintenance freeze 2025-08; used as decline case. |
| SE-014 | "Gemini CLI Google open source terminal AI assistant" | Web Search | 2026-08-03 | None | not reported | SRC-024 | Excluded marketing pages; relied on google-gemini/gemini-cli. | Apache 2.0 per community reports. |
| SE-015 | "Windsurf Codeium AI IDE description features" | Web Search | 2026-08-03 | None | not reported | SRC-016 (Cursor row updated), no separate row | Excluded — Windsurf has shifted to Cognition AI / Devin ecosystem per third-party reports; primary page not reachable. Recorded as competitor-landscape context; not advanced to inventory candidate. | Decision: Windsurf deferred from inventory due to verification limit. |
| SE-016 | "GitHub Copilot description official documentation features" | Web Search | 2026-08-03 | None | not reported | SRC-023 | Excluded third-party marketing; relied on docs.github.com features page. | Confirms vendor self-description. |
| SE-017 | "NIST SSDF SP 800-218 secure software development framework publication date" | Web Search | 2026-08-03 | None | not reported | SRC-003, SRC-049 | Excluded training-course restatements; relied on NIST CSRC + Synopsys mapping. | Confirms February 2022 publication. |
| SE-018 | "OWASP SAMM v2 software assurance maturity model publication" | Web Search | 2026-08-03 | None | not reported | SRC-004 | Excluded translation PDFs and presentations; relied on owaspsamm.org. | Confirms v2 line. |
| SE-019 | "OWASP ASVS 4.0 application security verification standard" | Web Search | 2026-08-03 | None | not reported | SRC-005 | Excluded translation PDFs; relied on OWASP project page. | Confirms v4.0.3 (2021-10). |
| SE-020 | "DORA DevOps Research Assessment State of DevOps report annual publication" | Web Search | 2026-08-03 | None | not reported | SRC-007 | Excluded analysis articles; relied on dora.dev. | Confirms annual cadence since 2014. |
| SE-021 | "ISO IEC IEEE 12207 software life cycle processes standard publication year" | Web Search | 2026-08-03 | None | not reported | SRC-006 | Excluded textbook PDFs; relied on iso.org/standard/90219.html reference. | Confirms multiple editions; latest listed 2026 on iso.org. |
| SE-022 | "Continuous Discovery Teresa Torres book Product Talk opportunity solution tree" | Web Search | 2026-08-03 | None | not reported | SRC-008, SRC-012, SRC-036 | Excluded blog restatements; relied on Product Talk publisher pages. | Confirms 2021 publication. |
| SE-023 | "Lean Startup Eric Ries book methodology 2011" | Web Search | 2026-08-03 | None | not reported | SRC-010 | Excluded douban/baidu secondary pages; relied on theleanstartup.com. | Confirms 2011 publication. |
| SE-024 | "Shape Up Basecamp Ryan Singer book table of contents 2019" | Web Search | 2026-08-03 | None | not reported | SRC-011, SRC-037 | Excluded unrelated search hits; relied on basecamp.com/shapeup. | Confirms free online version. |
| SE-025 | "Jobs to be Done Clayton Christensen theory strategic management" | Web Search | 2026-08-03 | None | not reported | SRC-013, SRC-038 | Excluded academic dissertation references; relied on Strategyn site + community sources. | Disputed attribution between Christensen and Ulwick recorded. |
| SE-026 | "Architecture Decision Record Michael Nygard ADR introduction blog post date" | Web Search | 2026-08-03 | None | not reported | SRC-002, SRC-040 | Excluded GitHub repository tutorials; relied on cognitect.com blog post + adr.github.io. | Confirms 2011-11-15 publication of Nygard's blog post. |
| SE-027 | "Inspired Marty Cagan SVPG product discovery book" | Web Search | 2026-08-03 | None | not reported | SRC-009, SRC-035 | Excluded book resale listings; relied on SVPG site. | Confirms first-edition 2008 publication. |
| SE-028 | "AGENTS.md standard agent guidance file format repository" | Web Search | 2026-08-03 | None | not reported | SRC-001, SRC-044 | Excluded tutorials and individual AGENTS.md examples; relied on agents.md + ETH report. | ETH Zurich counter-evidence recorded as SRC-044. |
| SE-029 | "LangGraph LangChain framework description repository license stateful agents" | Web Search | 2026-08-03 | None | not reported | SRC-028 | Excluded CSDN tutorials; relied on langchain-ai/langgraph repo. | Confirms 2024 initial release per community. |
| SE-030 | "AutoGen Microsoft multi-agent framework description repository license" | Web Search | 2026-08-03 | None | not reported | SRC-029, SRC-033, SRC-041 | Excluded CSDN tutorials; relied on microsoft/autogen + community consolidation report. | Confirms Microsoft Agent Framework consolidation context. |
| SE-031 | "crewAI repository license multi-agent orchestration framework" | Web Search | 2026-08-03 | None | not reported | SRC-030 | Excluded tutorials; relied on crewAIInc/crewAI. | License to confirm. |
| SE-032 | `gh search repos "spec driven development AI agent" --sort stars --limit 15` | GitHub CLI | 2026-08-05 | Repository search; sorted by stars | no result returned | None | Search did not complete because the configured GitHub token was invalid and sandboxed API access was blocked. | Failure recorded; no GitHub credential was modified. Public GitHub access was used for the evidence pass. |
| SE-033 | "site:github.com/github/spec-kit GitHub spec kit repository" plus direct repository / `pyproject.toml` inspection | Public GitHub Pages | 2026-08-05 | Canonical repository and raw primary files only | not reported | SRC-025 | Excluded tutorials, package mirrors, forks, and popularity claims. | Confirmed workflow, extension model, Python CLI stack, packaged templates/scripts, and MIT license. |
| SE-034 | "site:github.com/Fission-AI/OpenSpec OpenSpec repository" plus direct repository / `package.json` inspection | Public GitHub Pages | 2026-08-05 | Canonical repository and raw primary files only | not reported | SRC-026 | Excluded tutorials, package mirrors, forks, and popularity claims. | Confirmed artifact-guided workflow, change-package shape, Stores beta note, Node / TypeScript stack, and MIT license. |
| SE-035 | "site:github.com/bmad-code-org/BMAD-METHOD BMAD Method repository" plus workflow-map / `package.json` inspection | Public GitHub Pages | 2026-08-05 | Canonical repository and raw primary files only | not reported | SRC-053 | Excluded forks, older-version mirrors, third-party tutorials, and popularity claims. | Confirmed four-phase workflow, progressive artifacts and gates, Node-based installer, mixed JS / YAML / Markdown / Python helper stack, and MIT license. |
| SE-036 | "site:github.com/buildermethods/agent-os Agent OS repository" plus raw command / config / installer inspection | Public GitHub Pages | 2026-08-05 | Canonical repository and raw primary files only | not reported | SRC-054 | Excluded third-party documentation and popularity claims. | Confirmed standards discovery / injection / indexing / spec shaping, YAML profiles, shell installer, and adapter-specific command projection. |

## Process Notes

- All searches were run on 2026-08-03 during the Sprint 2 access window.
- WebSearch was used because WebFetch rejected `github.com`, `modelcontextprotocol.io`, `anthropic.com`, `iso.org`, `owasp.org`, `csrc.nist.gov`, `cursor.com`, and `producttalk.org` in this environment. Where the canonical primary page could not be fetched, the Source Register marks the **Claim Verification** as `Partially Verified` or `Unverified` and relies on third-party corroboration. Per Sprint 2.1, no search snippet is treated as a primary source.
- No search-result counts were invented. Where the search backend did not return a count, the cell shows `not reported`.
- Exclusion reasons recorded: forks, marketing restatements, translation PDFs, package mirrors, third-party reviews, tutorial sites (CSDN, cnblogs), and projects with no original primary source.

## Sprint 2.1 Corrections

- This file records **queries executed**, not verification outcomes. Verification outcomes are recorded in `research/source-register.md` per row.
- Several SE-### entries originally described their outcome as a confirmation ("confirms 2026-04 release", "confirms 2011-11-15 publication", etc.). Per Sprint 2.1, those outcomes are downgraded: the queries ran, but the **canonical primary page** was not directly fetched in this access window. The corresponding Source Register rows carry `Partially Verified` (where a third-party summary exists) or `Unverified` (where only a search snippet exists).
- The Sprint 2.1 audit reclassified each Source Register row using the new schema (Source Reliability / Claim Verification / Claim Type). The 31 searches in this log are preserved as a process record; they are not the basis for any "Verified" status.

## Cross-References

- `research/source-register.md` — sources selected from these searches.
- `research/ecosystem/inventory.md` — items built from the source set.
