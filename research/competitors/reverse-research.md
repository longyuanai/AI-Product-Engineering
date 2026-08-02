# research/competitors/reverse-research.md

- Status: Draft
- Version: v0.3
- Owner: APES Maintainers
- Last Updated: 2026-08-03
- Purpose: Apply the Core Project Analysis Schema (Appendix E of `research/research-plan.md`) — the 14-section template — to each project on the short list at `research/competitors/candidate-projects.md`. Surface both **confirming** and **contradicting** evidence for any APES-adjacent hypothesis. Do not derive APES positioning, market conclusions, gap claims, or standards here.

## Reverse Research Template (Applied to Each Project)

The 14 sections below are reproduced verbatim for every project. Where information is not verifiable in this access window, the section is filled with `Unverified — see Verification Notes`. No marketing copy is rewritten as objective fact.

### 14 Sections

1. **Project Identity** — name, author/maintainer, repository/publisher URL (if reachable), first release date, latest release observed, license (if verifiable).
2. **Stated Problem** — what problem the project says it solves, in its own words or in independent corroborations.
3. **Stated Audience** — who the project is for, per the project or per independent corroborations.
4. **Scope (In / Out)** — what is explicitly in scope and what is explicitly out of scope.
5. **Core Concepts / Vocabulary** — the names and definitions the project introduces or relies on.
6. **Process Model / Lifecycle Stages** — ordered stages, cycles, or methods the project prescribes.
7. **Inputs and Outputs** — what the project takes in and what it produces.
8. **Tooling and Artifact Conventions** — formats, templates, schemas, CLI flags, file conventions.
9. **Quality and Evidence Discipline** — what the project treats as evidence and what it rejects.
10. **Adjacent / Complementary Tools** — projects the author/maintainer or community pairs with this one.
11. **Conflicting or Competing Approaches** — known disagreements or alternative schools.
12. **Open Questions / Known Limits** — what the project does not claim, and where the maintainers have flagged limits.
13. **Verification Notes** — primary source status (Verified / Page Unverified / Not Found), third-party corroborations, and any counter-evidence located.
14. **Neutral Observations** — descriptive notes that do **not** imply an APES judgment.

---

## S-01. Continuous Discovery (Teresa Torres / Product Talk)

### 1. Project Identity

- Name: Continuous Discovery
- Author/Maintainer: Teresa Torres / Product Talk
- First Release: 2021 (book)
- Latest Release: 2021 book + ongoing practitioner templates on producttalk.org
- License: Book copyright (publisher); practitioner templates per Product Talk
- Sources: SRC-008, SRC-012, SRC-036

### 2. Stated Problem

Helping product teams move from periodic, episodic discovery to a weekly habit of customer touchpoints that inform product decisions.

### 3. Stated Audience

Product managers, product teams, and product leaders running discovery-led product organizations.

### 4. Scope (In / Out)

- **In**: weekly customer interviews, opportunity solution trees, assumption testing, discovery outcomes.
- **Out**: engineering implementation, security practices, business model design.

### 5. Core Concepts / Vocabulary

- Opportunity Solution Tree (OST)
- Desired Outcome
- Opportunity
- Solution
- Assumption Test
- Continuous Discovery Habits

### 6. Process Model / Lifecycle Stages

1. Define a desired outcome.
2. Map opportunities that may move the outcome.
3. Generate solutions for the most promising opportunity.
4. Design and run assumption tests.
5. Return weekly; iterate.

### 7. Inputs and Outputs

- **Inputs**: customer research data, business outcomes, opportunity backlog.
- **Outputs**: tested solutions, validated opportunities, updated OST.

### 8. Tooling and Artifact Conventions

- OST visualization (often Miro / FigJam / wall).
- Assumption-test cards / templates.
- Interview synthesis notes.

### 9. Quality and Evidence Discipline

Treats customer evidence as primary; rejects stakeholder opinion in place of customer data.

### 10. Adjacent / Complementary Tools

- JTBD (theory-level).
- Lean Startup (build-measure-learn framing).
- Inspired (Cagan) for discovery team framing.

### 11. Conflicting or Competing Approaches

- Disagrees with periodic, project-gated discovery (e.g., Shape Up's "shaping" approach prefers a longer cycle).
- Disagrees with feature-factory / output-driven PM.

### 12. Open Questions / Known Limits

- Does not prescribe how engineering / security practice is structured.
- Practitioner-authored; no peer-reviewed evidence base.

### 13. Verification Notes

- Page Unverified (Product Talk site blocked by WebFetch). Publisher and library catalog corroborate 2021 publication date.

### 14. Neutral Observations

The OST is widely used as a structural device. Continuous Discovery does not encode engineering or governance.

---

## S-02. Inspired: Creating Tech Products Customers Love (Marty Cagan / SVPG)

### 1. Project Identity

- Name: Inspired (book)
- Author/Maintainer: Marty Cagan / Silicon Valley Product Group (SVPG)
- First Release: 2008 (first edition)
- Latest Release: Multiple editions; SVPG site maintains current framing
- License: Publisher copyright; SVPG site content per SVPG
- Sources: SRC-009, SRC-035

### 2. Stated Problem

Helping technology companies build products customers love by structuring empowered product teams and separating product discovery from product delivery.

### 3. Stated Audience

Product leaders, founders, and product-team managers.

### 4. Scope (In / Out)

- **In**: product team structure, discovery vs delivery, empowered teams, mission, prototype-first validation.
- **Out**: engineering pipeline specifics, security, lifecycle standards.

### 5. Core Concepts / Vocabulary

- Empowered Product Team
- Product Discovery
- Product Delivery
- Mission
- Prototype / Customer Validation
- Product Manager / Product Trio (PM + Design + Tech Lead)

### 6. Process Model / Lifecycle Stages

1. Frame the mission.
2. Run product discovery (continuous).
3. Hand off to product delivery (engineering).
4. Iterate via ongoing discovery.

### 7. Inputs and Outputs

- **Inputs**: customer problems, prototypes, validated opportunities.
- **Outputs**: validated product direction, a clear build backlog.

### 8. Tooling and Artifact Conventions

- Mission framing documents (no fixed template).
- Prototype assets.
- Discovery artifacts (interview notes, opportunity assessments).

### 9. Quality and Evidence Discipline

Treats prototype + customer validation as primary evidence; rejects building without discovery.

### 10. Adjacent / Complementary Tools

- Continuous Discovery (Torres).
- Shape Up.
- Lean Startup.

### 11. Conflicting or Competing Approaches

- Disagrees with feature-factory PM.
- Disagrees with shallow discovery in favor of empowered-team / mission framing.

### 12. Open Questions / Known Limits

- Does not specify engineering governance or security practice.
- Practitioner text, not a peer-reviewed standard.

### 13. Verification Notes

- Page Unverified (SVPG site blocked). Publisher corroborates first edition.

### 14. Neutral Observations

A practitioner text that articulates team topology more than process steps. The discovery/delivery separation is widely adopted as terminology.

---

## S-03. Shape Up (Basecamp / Ryan Singer)

### 1. Project Identity

- Name: Shape Up
- Author/Maintainer: Ryan Singer / Basecamp
- First Release: 2019 (free online book)
- Latest Release: 2019 online book (free); Basecamp product-line updates continue
- License: Free online version (publisher terms)
- Sources: SRC-011, SRC-037

### 2. Stated Problem

Helping teams ship meaningful work on a fixed cycle without the rigidities of traditional project management.

### 3. Stated Audience

Software product teams that prefer a less-overhead, betting-cycle cadence.

### 4. Scope (In / Out)

- **In**: shaping, betting, building, cooling down; fixed time, variable scope.
- **Out**: continuous customer touchpoints (compared with Continuous Discovery), formal engineering governance.

### 5. Core Concepts / Vocabulary

- Shaping
- Betting Table
- Hill Charts
- Fixed Time, Variable Scope
- Cooldown

### 6. Process Model / Lifecycle Stages

1. Shape work into a clear problem and appetite.
2. Bet on which shaped work to pull into the next cycle.
3. Build during the fixed cycle.
4. Cool down after shipping.
5. Repeat.

### 7. Inputs and Outputs

- **Inputs**: raw ideas, customer pain, scoped appetite.
- **Outputs**: shaped projects, hill charts, shipped features.

### 8. Tooling and Artifact Conventions

- Hill Charts (progress visualization).
- Shaping documents (no fixed template).
- Betting table artifacts.

### 9. Quality and Evidence Discipline

Treats shipping as the unit of evidence; rejects long grooming backlogs.

### 10. Adjacent / Complementary Tools

- Lean Startup (build-measure-learn framing).
- Continuous Discovery (does weekly customer work; Shape Up does periodic shaping).

### 11. Conflicting or Competing Approaches

- Disagrees with Continuous Discovery's weekly-touchpoint cadence.
- Disagrees with feature-factory output-driven teams.

### 12. Open Questions / Known Limits

- Does not specify engineering practice or security controls.
- Practitioner text.

### 13. Verification Notes

- Page Unverified (basecamp.com/shapeup blocked). Multiple independent community sources corroborate 2019 release.

### 14. Neutral Observations

Shape Up provides a different unit of cadence than Continuous Discovery. The two are commonly compared in practitioner discourse.

---

## S-04. Jobs to Be Done — Christensen Line

### 1. Project Identity

- Name: Jobs to Be Done (theory)
- Author/Maintainer: Clayton Christensen (HBS) and collaborators
- First Release: 2003 onward; popular-press book "Competing Against Luck" (2016)
- Latest Release: Multiple academic and popular-press updates
- License: Publisher copyright; academic papers per HBS
- Sources: SRC-013, SRC-038

### 2. Stated Problem

Helping firms understand why customers "hire" products, by focusing on the underlying job the customer is trying to get done rather than on product features or demographics.

### 3. Stated Audience

Strategists, product leaders, marketers.

### 4. Scope (In / Out)

- **In**: causal customer "jobs", social / emotional / functional dimensions, segmentation.
- **Out**: engineering practice, governance.

### 5. Core Concepts / Vocabulary

- Job
- Functional / Emotional / Social Dimensions
- Hiring / Firing / Returning
- Milkshake Moment (canonical example)

### 6. Process Model / Lifecycle Stages

1. Identify a job.
2. Define dimensions and outcomes.
3. Discover unmet needs.
4. Design / grow accordingly.

### 7. Inputs and Outputs

- **Inputs**: customer research, behavioral data.
- **Outputs**: job map, growth plan.

### 8. Tooling and Artifact Conventions

- Job Map (8-step universal progress).
- Job Story (When... I want to... So I can...).

### 9. Quality and Evidence Discipline

Treats behavioral evidence as primary; rejects demographics / feature-count as causal.

### 10. Adjacent / Complementary Tools

- Strategyn / ODI (Ulwick).
- Continuous Discovery (Torres).
- Inspired (Cagan).

### 11. Conflicting or Competing Approaches

- Strategyn's ODI uses a different (desired-outcome, quantitative) framing; Christensen and Ulwick disagree on attribution and method.

### 12. Open Questions / Known Limits

- Theoretical framework, not a process standard.
- Disputed attribution between Christensen and Ulwick (recorded honestly in SRC-013 / SRC-038).

### 13. Verification Notes

- Page Unverified (HBS / Strategyn pages blocked). Publisher corroborates 2016 book.

### 14. Neutral Observations

JTBD is widely cited as a customer-research lens. It does not prescribe engineering or governance.

---

## S-05. Outcome-Driven Innovation (Tony Ulwick / Strategyn)

### 1. Project Identity

- Name: Outcome-Driven Innovation (ODI)
- Author/Maintainer: Tony Ulwick / Strategyn
- First Release: 2002 onward
- Latest Release: Continuous methodology updates
- License: Strategyn methodology; books publisher-copyrighted
- Sources: SRC-013, SRC-038

### 2. Stated Problem

Helping firms identify and prioritize market opportunities by measuring customer desired outcomes rather than relying on demographic or feature-based segmentation.

### 3. Stated Audience

Strategy teams, product managers, innovation teams.

### 4. Scope (In / Out)

- **In**: outcome-based segmentation, opportunity sizing, quantitative JTBD.
- **Out**: engineering practice, governance.

### 5. Core Concepts / Vocabulary

- Desired Outcome
- Outcome Statement
- Importance / Satisfaction Gap
- Opportunity Algorithm

### 6. Process Model / Lifecycle Stages

1. Define the job.
2. Uncover desired outcomes.
3. Survey to measure importance and satisfaction.
4. Calculate opportunity scores.
5. Prioritize and act.

### 7. Inputs and Outputs

- **Inputs**: structured customer surveys, outcome statements.
- **Outputs**: opportunity scores, prioritized roadmap inputs.

### 8. Tooling and Artifact Conventions

- Outcome surveys.
- Opportunity scoring spreadsheet.

### 9. Quality and Evidence Discipline

Quantitative; requires statistical sample sizes.

### 10. Adjacent / Complementary Tools

- JTBD (Christensen).
- Lean Startup.

### 11. Conflicting or Competing Approaches

- Disagrees with Christensen's framing of "job" as causal unit (claims methodological origin).
- Disagrees with feature / demographic segmentation.

### 12. Open Questions / Known Limits

- Methodology is proprietary (Strategyn).
- Does not address engineering / governance.

### 13. Verification Notes

- Page Unverified (Strategyn site blocked). Publisher corroborates Ulwick's book.

### 14. Neutral Observations

ODI is the operational counterpart of JTBD for those who adopt a quantitative angle. The Christensen / Ulwick attribution dispute is openly noted in sources and is preserved here without resolution.

---

## S-06. Architecture Decision Record (Michael Nygard)

### 1. Project Identity

- Name: Architecture Decision Record (ADR)
- Author/Maintainer: Michael Nygard (initial blog post); community maintainers for tooling
- First Release: 2011-11-15 (Nygard's blog post)
- Latest Release: ADR format is stable; tooling evolves
- License: Format is open; Nygard's blog post per his terms
- Sources: SRC-002, SRC-040

### 2. Stated Problem

Helping teams capture architectural decisions, including their context and consequences, so the reasoning behind decisions is preserved over time.

### 3. Stated Audience

Software architects, tech leads, engineering teams.

### 4. Scope (In / Out)

- **In**: decision context, decision status, consequences.
- **Out**: execution details, customer research, security policy.

### 5. Core Concepts / Vocabulary

- Decision
- Status (Proposed / Accepted / Deprecated / Superseded)
- Context
- Decision Drivers
- Considered Options
- Consequences

### 6. Process Model / Lifecycle Stages

1. Capture context.
2. Capture considered options.
3. Capture decision and consequences.
4. Update status over time (Superseded / Deprecated).

### 7. Inputs and Outputs

- **Inputs**: problem framing, options, tradeoffs.
- **Outputs**: an ADR file (typically Markdown).

### 8. Tooling and Artifact Conventions

- Markdown file in `docs/adr/` (commonly `NNNN-title.md`).
- Lightweight tooling (`adr-tools`, `log4brains`, MADR templates).

### 9. Quality and Evidence Discipline

Treats reasons and consequences as primary; rejects "decision by authority without record".

### 10. Adjacent / Complementary Tools

- Spec Kit (spec-driven dev).
- OpenSpec (spec/plan artifact).
- GitHub / GitLab for storage.

### 11. Conflicting or Competing Approaches

- MADR adds structured options / decision drivers.
- "Lightweight" ADR variants strip sections; Nygard's original is the baseline.

### 12. Open Questions / Known Limits

- ADR is a record format, not a process.
- No prescribed review workflow.

### 13. Verification Notes

- Page Unverified (cognitect.com blog post blocked). Multiple community sources corroborate 2011-11-15 publication.

### 14. Neutral Observations

ADR is a foundational record convention. Its scope is intentionally narrow.

---

## S-07. OpenSpec (Fission-AI)

### 1. Project Identity

- Name: OpenSpec
- Author/Maintainer: Fission-AI
- First Release: 2024 (open source release); ongoing
- Latest Release: v0.17.0 (referenced 2026-06)
- License: Open source (specific license to confirm at repo)
- Sources: SRC-026

### 2. Stated Problem

Providing a vendor-neutral, open format for specifications and change proposals that AI coding tools and human teams can both consume.

### 3. Stated Audience

AI coding-tool users, software teams adopting spec-driven development.

### 4. Scope (In / Out)

- **In**: spec / change proposal format, lightweight review workflow.
- **Out**: full project management, security policy, business modeling.

### 5. Core Concepts / Vocabulary

- Spec
- Change Proposal
- Task
- Approval

### 6. Process Model / Lifecycle Stages

1. Author a spec.
2. Propose a change.
3. Review.
4. Implement.
5. Update.

### 7. Inputs and Outputs

- **Inputs**: intent, proposed change.
- **Outputs**: spec / change artifact files, review state.

### 8. Tooling and Artifact Conventions

- Markdown / structured spec files.
- CLI commands for proposing / approving changes.

### 9. Quality and Evidence Discipline

Treats explicit spec text as primary; rejects implicit "in-the-head" plans for AI-driven work.

### 10. Adjacent / Complementary Tools

- Spec Kit.
- ADR (Nygard).
- Claude Code / OpenAI Codex CLI / Gemini CLI (consumers).

### 11. Conflicting or Competing Approaches

- Spec Kit is vendor-led; OpenSpec is community-led.
- Different ecosystems propose similar ideas; no canonical convergence yet.

### 12. Open Questions / Known Limits

- Adoption metrics not reported here.
- License to confirm at the repository level.

### 13. Verification Notes

- Page Unverified (GitHub repository blocked by WebFetch). Repository metadata and community corroborate v0.17.0 reference.

### 14. Neutral Observations

OpenSpec is one of two prominent AI-era spec formats observed in this window (with Spec Kit). The formats differ in scope and authoring community.

---

## S-08. Spec Kit (GitHub)

### 1. Project Identity

- Name: Spec Kit
- Author/Maintainer: GitHub
- First Release: 2025-09
- Latest Release: Updated post-2025-09
- License: Open source per GitHub
- Sources: SRC-025

### 2. Stated Problem

Providing tooling and templates for spec-driven development, particularly aimed at AI-coding workflows.

### 3. Stated Audience

Developers using GitHub-hosted repositories and AI coding tools.

### 4. Scope (In / Out)

- **In**: spec templates, reviewable change artifacts, CLI / GitHub integration.
- **Out**: full lifecycle governance, business modeling.

### 5. Core Concepts / Vocabulary

- Spec
- Change Proposal
- Review
- Approval

### 6. Process Model / Lifecycle Stages

1. Author spec.
2. Propose change.
3. Review.
4. Implement.
5. Update.

### 7. Inputs and Outputs

- **Inputs**: intent, proposed change.
- **Outputs**: spec files, change proposals, review states.

### 8. Tooling and Artifact Conventions

- GitHub CLI integration.
- Spec templates (Markdown).

### 9. Quality and Evidence Discipline

Treats explicit spec text as primary.

### 10. Adjacent / Complementary Tools

- OpenSpec.
- ADR (Nygard).
- GitHub Copilot (consumer).

### 11. Conflicting or Competing Approaches

- OpenSpec is community-led; Spec Kit is vendor-led.

### 12. Open Questions / Known Limits

- Adoption metrics not reported here.

### 13. Verification Notes

- Page Unverified (GitHub repo blocked by WebFetch). Repository metadata and community corroborate 2025-09 release.

### 14. Neutral Observations

Spec Kit is the vendor-led counterpart to OpenSpec. Both encode a similar shape; their author communities and ecosystems differ.

---

## S-09. Claude Code (Anthropic)

### 1. Project Identity

- Name: Claude Code
- Author/Maintainer: Anthropic
- First Release: 2025 (vendor release)
- Latest Release: Updated through 2026-08 (access window)
- License: Vendor terms of use
- Sources: SRC-014

### 2. Stated Problem

Providing an agentic CLI for coding tasks that combines a coding-capable model with tool use, file access, and execution context.

### 3. Stated Audience

Software developers using Anthropic Claude models for coding work.

### 4. Scope (In / Out)

- **In**: agentic CLI, tool use, project-context loading, plan-then-execute interaction.
- **Out**: full project lifecycle governance, security policy.

### 5. Core Concepts / Vocabulary

- Agentic CLI
- AGENTS.md support (per vendor docs)
- Plan mode
- Sub-agents / tool calls

### 6. Process Model / Lifecycle Stages

1. Read project context (including AGENTS.md).
2. Plan.
3. Execute via tools.
4. Report back to the user.

### 7. Inputs and Outputs

- **Inputs**: project files, user prompts, optional AGENTS.md.
- **Outputs**: file edits, command outputs, agentic actions.

### 8. Tooling and Artifact Conventions

- AGENTS.md (per vendor docs).
- Plan mode artifacts.
- Permission / tool-use configuration.

### 9. Quality and Evidence Discipline

Vendor-defined. Treats user confirmation as a checkpoint; treats AGENTS.md as authoritative project context.

### 10. Adjacent / Complementary Tools

- OpenAI Codex CLI.
- Cursor.
- Gemini CLI.
- MCP (Model Context Protocol) for tool interchange.

### 11. Conflicting or Competing Approaches

- Competes with other agentic CLIs (Codex CLI, Gemini CLI).
- Different from IDE-embedded agents (Cursor) by being CLI-first.

### 12. Open Questions / Known Limits

- Vendor-controlled; subject to Anthropic product decisions.
- Page Unverified for full feature set due to WebFetch restrictions.

### 13. Verification Notes

- Page Unverified (anthropic.com blocked). Vendor documentation corroborated via community sources.

### 14. Neutral Observations

Claude Code is one of multiple agentic CLIs. The presence of AGENTS.md support is itself a notable convention.

---

## S-10. AGENTS.md (Open Community Convention)

### 1. Project Identity

- Name: AGENTS.md
- Author/Maintainer: Open community (initial contributors coordinated via agents.md)
- First Release: n.d. (concrete release date Unverified; project page describes a simple open format for guiding coding agents)
- Latest Release: n.d.
- License: Convention; file content per project
- Sources: SRC-001, SRC-044, SRC-045
- **Verification (Sprint 2.3):** SRC-001 page content and official self-positioning verified via EV-001 (external reviewer with direct primary-source access). The `agents.md` page is framed as a "README for agents" and describes an open format covering build, test, code-style, security, and contribution rules. The "over 60,000 open-source projects" adoption figure is **project-maintainer-reported** and is not recorded as independent market share.

### 2. Stated Problem

Providing a top-level, predictable place in a repository where AI coding agents can read project-specific guidance (build, test, conventions, safety rules).

### 3. Stated Audience

AI coding agents, repository maintainers.

### 4. Scope (In / Out)

- **In**: file format, content guidance.
- **Out**: execution enforcement, security policy.

### 5. Core Concepts / Vocabulary

- AGENTS.md (root-level file)
- Markdown structure
- Cross-references (e.g., to CONTRIBUTING.md)

### 6. Process Model / Lifecycle Stages

1. Project authors author AGENTS.md.
2. AI agents read it on context load.
3. Agents incorporate guidance into behavior.

### 7. Inputs and Outputs

- **Inputs**: AGENTS.md text.
- **Outputs**: agent behavior modifiers.

### 8. Tooling and Artifact Conventions

- Single Markdown file at repo root.
- Multiple agents (Claude Code, Codex CLI, others) reportedly honor it.

### 9. Quality and Evidence Discipline

Treats maintainer-authored content as authoritative.

### 10. Adjacent / Complementary Tools

- Claude Code (consumer).
- OpenAI Codex CLI (consumer).
- Gemini CLI (consumer).

### 11. Conflicting or Competing Approaches

Two academic studies (now registered as `Verified` independent empirical evidence at the abstract level via EV-003 and EV-004) report **conflicting** findings on AGENTS.md's effect:

- **SRC-044 — arXiv 2602.11988 (Gloaguen, Mündler, Müller, Raychev, Vechev; 2026-02-12 v1; 2026-06-23 v2)** — *Evaluating AGENTS.md: Are Repository-Level Context Files Helpful for Coding Agents?*
  - Authors: Thibaud Gloaguen, Niels Mündler, Mark Müller, Veselin Raychev, Martin Vechev.
  - In their evaluation setting, repository-level context files (including AGENTS.md) generally tended to **lower task success and increase inference cost** (mean inference cost increased by over 20%).
  - Agents typically follow the instructions; non-standard engineering requirements may be useful, but repository overviews and unnecessary requirements should be used with caution.
  - Limitation: conclusions cannot be generalized to all repositories, models, agents, or tasks; experimental setup must be cited. The "AGENTS.md is always harmful" generalization is not supported.

- **SRC-045 — arXiv 2601.20404 (Lulla, Mohsenimofidi, Galster, Zhang, Baltes, Treude; 2026-01-28 v1; 2026-03-30 v2)** — *On the Impact of AGENTS.md Files on the Efficiency of AI Coding Agents*
  - Authors: Jai Lal Lulla, Seyedmoein Mohsenimofidi, Matthias Galster, Jie M. Zhang, Sebastian Baltes, Christoph Treude.
  - Analyzed 10 repositories and 124 Pull Requests; AGENTS.md was associated with **lower median runtime and lower output-token consumption**.
  - Task-completion performance was roughly similar to no-AGENTS.md runs.
  - Limitation: "correlation" is not automatically "causation"; the paper's tasks, models, agents, metrics, and research design differ from SRC-044; results are not directly comparable.

The two studies disagree on direction (one finds harm to task success and cost; the other finds similar task success and lower cost). APES does **not** adjudicate which is "correct" — the conflict is recorded honestly.

### 12. Open Questions / Known Limits

- Adoption metrics are **project-maintainer-reported**, not independently verified.
- Conflicting academic evidence means independent confirmation is needed before any normative claim about AGENTS.md value is made.

### 13. Verification Notes

- SRC-001: **Verified** (page content and official self-positioning verified externally via EV-001; 60k+ adoption figure is project-maintainer-reported, not independent market share).
- SRC-044: **Verified** (existence, title, authors, dates, abstract content verified externally via EV-003; method details remain `Partially Verified`).
- SRC-045: **Verified** (existence, title, authors, dates, abstract content verified externally via EV-004; method details remain `Partially Verified`). SRC-045 is **not** retracted.
- **Sprint 2.2 verification attempt (2026-08-03):** direct WebFetch on `https://agents.md/`, `https://arxiv.org/abs/2602.11988`, and `https://arxiv.org/abs/2601.20404` all returned `Unable to verify if domain X is safe to fetch`. The 22 Inaccessible attempts are recorded in `research/notes/verification-log.md` (VR-001, VR-021, VR-022).
- **Sprint 2.3 external verification reconciliation (2026-08-03):** EV-001, EV-003, and EV-004 supplied by an external reviewer with direct primary-source access; the underlying Source Register rows are now `Verified` at the abstract/metadata level. PDF body for both arXiv papers remains `Partially Verified` (full method details not directly read).

### 14. Neutral Observations

AGENTS.md is an emerging convention with active adoption, active vendor support, and **active academic disagreement** about its effect. Both sides are recorded.

---

## Cross-Project Patterns Observed (Descriptive, Non-Conclusory)

The following observations are descriptive. They are **not** APES positioning, gap claims, or market conclusions.

1. **Discovery methodologies** (Continuous Discovery, Inspired, Shape Up, JTBD / ODI) all emphasize customer evidence as primary. They differ in cadence (weekly vs. cyclical vs. as-needed) and structure (OST vs. mission vs. hill charts vs. job / outcome).
2. **Decision / spec artifacts** (ADR, OpenSpec, Spec Kit, AGENTS.md) all share the convention of a structured, machine-or-human-readable text artifact. They differ in scope: ADRs capture one decision; OpenSpec / Spec Kit capture plans and changes; AGENTS.md captures persistent agent guidance.
3. **AI coding agents** (Claude Code, OpenAI Codex CLI, Cursor, aider, Cline, OpenHands, GitHub Copilot, Gemini CLI) all consume convention files and repo context; the cluster does not converge on a single shared spec format yet.
4. **Multi-agent orchestration frameworks** (MCP, LangGraph, AutoGen, Microsoft Agent Framework, crewAI) are observed but not advanced to reverse research in Sprint 2 due to scope budget.
5. **Standards / governance** (NIST SSDF, OWASP SAMM v2, ISO 12207:2026 Edition 2, DORA, SRE Book, DHS/CISA Software Attestation) are observed but deferred to a standards-focused follow-up sprint.

These are observed patterns only. They do not assert a coverage claim for APES.

## Cross-References

- `research/competitors/candidate-projects.md` — short list source.
- `research/ecosystem/inventory.md` — broader inventory.
- `research/source-register.md` — sources cited in this file.
- `research/notes/search-log.md` — searches that surfaced each project.
- `research/notes/verification-log.md` — Sprint 2.2 direct verification attempts (all `Inaccessible`).
- `tasks/sprint-02-2-primary-source-verification.md` — Sprint 2.2 task file (Research Gate: `RESEARCH AGAIN`).
- `tasks/sprint-02-3-external-verification-reconciliation.md` — Sprint 2.3 task file (6 sources upgraded via external-verification evidence EV-001 through EV-006).