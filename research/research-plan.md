# Ecosystem Research Plan

- Status: Draft
- Version: v0.1
- Owner: APES Maintainers
- Last Updated: 2026-08-03
- Purpose: Define the scope, methodology, evidence rules, and outputs of the APES ecosystem research effort, before any actual research is conducted.

## Table of Contents

- [1. Research Purpose](#1-research-purpose)
- [2. Research Principles](#2-research-principles)
- [3. Scope and Non-Scope](#3-scope-and-non-scope)
- [4. Methodology](#4-methodology)
- [5. Source Categories and Sampling](#5-source-categories-and-sampling)
- [6. Research Questions and Hypotheses](#6-research-questions-and-hypotheses)
- [7. Evidence Quality Criteria](#7-evidence-quality-criteria)
- [8. Anti-Patterns to Prevent](#8-anti-patterns-to-prevent)
- [9. Deliverables and File Layout](#9-deliverables-and-file-layout)
- [10. Schedule, Cadence, and Stop Conditions](#10-schedule-cadence-and-stop-conditions)
- [11. Governance, Review, and Disagreement Handling](#11-governance-review-and-disagreement-handling)
- [12. Outputs That Feed Back Into APES](#12-outputs-that-feed-back-into-apes)
- [13. Risks, Limitations, and Known Unknowns](#13-risks-limitations-and-known-unknowns)
- [14. Research Priority Order](#14-research-priority-order)

## Appendix

- [A. Source Register Schema](#a-source-register-schema)
- [B. Reliability Classification (A–E)](#b-reliability-classification-ae)
- [C. Candidate Selection Criteria](#c-candidate-selection-criteria)
- [D. Search Log Schema](#d-search-log-schema)
- [E. Core Project Analysis Schema](#e-core-project-analysis-schema)

## 1. Research Purpose

APES claims a vendor-neutral, evidence-driven role across the full AI product lifecycle. That claim must be earned, not asserted. Without ecosystem research, APES risks becoming:

- A prompt collection with no underlying standard.
- A documentation dump that no team adopts because it overlaps with existing frameworks.
- A reinvention of well-tested product or engineering practices that already exist.

### 1.1 Why research must precede standard drafting

- Standards that codify the wrong gap produce noise, not value. Research defines what gap, if any, is real and worth codifying.
- Lifecycle coverage (Discovery → Knowledge) implies APES spans territory owned today by Lean Startup, Shape Up, Marty Cagan's *Inspired*, dual-track agile, DevOps, and various growth frameworks. APES must demonstrate a defensible complement, not duplication.
- "Vendor-neutral" is an empirical claim: research must show APES is positioned differently from any specific AI tool or framework.

### 1.2 Decisions this research must support

The ecosystem research is intended to support, and at minimum produce evidence for, the following decisions:

1. Whether APES, as currently scoped, has a real value gap worth continuing.
2. Which lifecycle stages APES should own versus delegate to existing standards.
3. Which adjacent standards and tools APES must explicitly *compose* with, *reference*, or *decline to overlap* with.
4. Whether APES should position itself as a standard, framework, protocol, workflow, or toolset — and whether the current positioning is defensible.
5. Which risks (adoption, lock-in, duplication, premature tooling) APES must mitigate before any module standard is written.
6. Which real, citable evidence APES needs to require from contributors before a module is promoted from Draft to Accepted.
7. Whether the project should be **continued, redirected, or stopped** at the end of this research phase.

### 1.3 Judgments that must not be made without evidence

- "Teams need a new standard" — must be backed by observed gaps in current standards.
- "AI tools accelerate code but ignore validation" — must be backed by examples or surveys, not vibes.
- "Our standard is vendor-neutral" — must be backed by an explicit inventory of how each module avoids endorsing tools.
- "We have traction" — must not be claimed before any adoption signal is citable.

### 1.4 If research is insufficient, APES may suffer these failure modes

- Mis-scoped standard: codifies the wrong lifecycle stages and leaves the real gap open.
- Duplication: writes what Lean, Shape Up, or existing engineering standards already say.
- Tooling drift: builds CLI / MCP / VS Code extensions before knowing which workflows are worth automating.
- Reputation risk: claims market position before evidence exists.
- Contributor friction: contributors cannot tell which adjacent framework their idea belongs to.

### 1.5 How this plan prevents APES becoming a prompt collection or doc dump

- Every research output must answer a specific decision listed in §1.2.
- Every note must have a documented citation with access date (`research/README.md` rules).
- Notes that do not change a decision are not stored as research; they belong in `research/notes/` and are explicitly labeled personal observation.
- Module drafting cannot begin until §6 research questions for that stage produce at least one Accepted evidence note each.

## 2. Research Principles

These principles govern how research is conducted, not what APES claims. They are derived from `MANIFESTO.md`.

1. **Evidence over opinion.** A claim is only as strong as its citation. Unsourced statements are not findings.
2. **Reuse before reinvent.** APES will not write a standard that already exists. The first question is always "what already covers this?"
3. **Iteration over perfection.** This plan will be revised as the research progresses. It is a v0.1 Draft, not a final methodology.
4. **Minimum-change principle.** A research output should change exactly one APES decision or none. Outputs that change nothing are not stored as research.
5. **Vendor neutrality by construction.** Every note must describe each tool/standard by what it does, not by whether we like it. Endorsement language is a research defect.
6. **Adversarial review.** Each finding must be challenged by at least one independent reviewer before it is marked Accepted (see §11).
7. **Provenance preserved.** Every quoted statement is linked to a source that can be re-opened, accessed on its original terms, and cited with author, title, publisher, date, and (for printed works) ISBN, DOI, or standard number. See §15 for copyright and paywall rules.

## 3. Scope and Non-Scope

### 3.1 In scope for this research phase

- AI-assisted software product lifecycle (Discovery → Knowledge), including how current tooling addresses each stage.
- Adjacent and competing product-engineering standards: Lean Startup, Shape Up, Marty Cagan's *Inspired*, Continuous Discovery, Dual-Track Agile, Obeya, JTBD, OKR-driven product practice.
- Adjacent engineering and process standards: ISO/IEC/IEEE 12207, ISO 21500, PMBOK, ITIL, OWASP, NIST SSDF, Site Reliability Engineering (SRE), DevOps Research and Assessment (DORA) framework, Architecture Decision Records (ADRs), RFC process.
- AI tooling ecosystem: Claude Code, OpenAI Codex, Cursor, GitHub Copilot, Gemini CLI, Windsurf, aider, Continue, Cody, MCP, AGENTS.md/CLAUDE.md conventions.
- Spec-driven Development tools: e.g., Spec-Kit, OpenSpec, github/spec-kit and similar.
- Academic and industry literature on AI-assisted software engineering, prompt engineering as a practice, and human-AI collaboration patterns.
- Real-world case studies where any of the above are claimed to be in use.

### 3.2 Out of scope (this research phase)

- Internal product strategy decisions of any specific AI vendor.
- Predictions about future model capability beyond what published benchmarks support.
- Adoption counts, market share, or "industry leadership" claims that cannot be sourced.
- Vendor-internal architecture or roadmaps (treated as rumors unless published officially).
- Benchmarking model quality — APES does not measure models.
- Detailed feature comparisons that read as buying guides.

## 4. Methodology

### 4.1 Phases

The research runs in four phases, each gated by an evidence quality review.

1. **Phase A — Inventory.** List every standard, framework, tool, and protocol potentially relevant to APES. One-liner each, with primary source.
2. **Phase B — Coverage Map.** For each APES lifecycle stage, record which of the inventoried items already cover the stage and how. Output: a stage × item matrix.
3. **Phase C — Gap Analysis.** For each stage, identify what is *not* covered, *under-covered*, or *conflicted across existing standards*. Output: a gap description per stage, with citations.
4. **Phase D — Positioning Evidence.** Pull together the evidence needed to support or revise the seven decisions in §1.2. Output: a Positioning Evidence Note that goes to maintainers.

Each phase ends with a review (see §11). No phase is allowed to skip review, even under time pressure.

### 4.2 Per-note workflow

For each research note:

1. **Question.** State the question or hypothesis this note addresses. Reference §6.
2. **Source.** Cite the primary source. URLs preferred; print sources require stable identifiers.
3. **Access date.** Required.
4. **Claim.** Quote or paraphrase, with section/page pointer.
5. **Strength.** Self-assess against §7 criteria.
6. **Counter-evidence.** List at least one disconfirming search you ran, and what you found.
7. **Implication for APES.** Which decision in §1.2 this affects.

A note that cannot complete step 6 is not Accepted — at most Draft.

### 4.3 Counter-evidence search (mandatory)

For every Accepted claim, the researcher must record at least one search they ran to *disconfirm* the claim, and the result. Example: if a claim is "X covers validation", the counter-evidence search must be "does X have a documented validation methodology?" with a yes/no answer and citation.

### 4.4 Tools allowed for research

- Public web search and web fetch.
- Official documentation sites of standards bodies, foundations, and tool vendors.
- arXiv, ACM, IEEE, USENIX, and conference proceedings for academic sources.
- Public GitHub repositories and their README, ADR, RFC, and `examples/` directories.
- Public case studies from organizations that publish them.

### 4.5 Tools NOT allowed as primary evidence

- Model-generated summaries without a cited primary source.
- Marketing pages taken as factual claims (they may be cited *as marketing* but not as evidence).
- Anonymous blog posts or forum threads, unless they are themselves the subject of the research.
- Internal documents from any organization that has not consented to public release.

### 4.6 Source Register Schema

Every primary or secondary source used in research is recorded once in a shared register. The register is the canonical inventory of evidence; per-note citations point back into it.

Fields:

- **Source ID.** Stable identifier (e.g., `SR-0007`) used by all downstream notes.
- **Title.** Full title of the work or page.
- **Source Type.** Standards document, vendor docs, academic paper, conference talk, book, blog post, repository, case study, social thread.
- **Publisher / Author.** Issuing organization or principal author.
- **URL.** Canonical URL, or stable identifier (DOI, ISBN, arXiv ID, standard number).
- **Publication Date.** As stamped by the publisher. `unknown` only with explicit justification.
- **Access Date.** Date the source was last retrieved by the researcher.
- **Related Research Question / Hypothesis.** Pointer to one or more §6 hypotheses this source informs.
- **Reliability Level.** Level A–E per Appendix B.
- **Primary / Secondary Source.** Whether the source is itself the primary record (e.g., an ISO standard) or a secondary report on a primary record.
- **Key Evidence.** Verbatim quote(s) or precise paraphrase with section/page pointer.
- **Contradictory Evidence.** Any known counter-claim within the source, or "none observed".
- **Limitations.** Stated scope, recency gaps, known biases, paywall status.
- **Verification Status.** `Pending`, `Verified`, `Disputed`. A Source starts at `Pending` and only becomes `Verified` after the §11 review confirms Primary/Secondary classification and Access Date.
- **Notes.** Anything that does not fit elsewhere.

The register itself lives at `research/source-register.md` (see §9) and is created at the start of formal research execution. This Sprint does **not** populate it.

### 4.7 Search Log Schema

Every search that produced candidate sources is recorded. This is what makes the source register auditable, not curated-after-the-fact.

Fields:

- **Search ID.** Stable identifier (e.g., `SE-0012`).
- **Query.** Exact query string used.
- **Platform.** Search engine, GitHub search, arXiv, vendor docs site, etc.
- **Search Date.** Date the query was run.
- **Filters.** Language, date range, file type, license filter — whatever was applied.
- **Approximate Result Count.** As returned by the platform.
- **Selected Sources.** Source IDs from the register that were retained from this search.
- **Exclusion Reasons.** Why other top results were rejected (not relevant, marketing-only, broken URL, Level E by §B, etc.).
- **Notes.** Anything else worth recording, including search variants tried.

The search log lives at `research/notes/search-log.md` (see §9) and is created at the start of formal research execution. This Sprint does **not** populate it.

### 4.8 Core Project Analysis Schema

For each project (standard, framework, tool, or protocol) that survives the Candidate Selection Criteria (Appendix C), an analysis note is produced.

Fields:

- **Project ID.** Stable identifier (e.g., `PRJ-0003`).
- **Name.** Display name.
- **Official URL.** Marketing or project home page.
- **Repository URL.** Primary repository, if any.
- **Positioning.** Self-description in the project's own words, quoted.
- **Target Users.** Self-description, quoted.
- **License.** SPDX identifier or "no clear license".
- **Created Date.**
- **Last Updated.** Most recent release, commit, or dated doc update.
- **Maintenance Status.** Active, maintenance mode, archived, abandoned — with the evidence used.
- **Technology Stack.** Languages, runtimes, key dependencies, as declared.
- **Core Features.** Three to ten feature areas, in the project's own vocabulary.
- **Workflow.** How a user is guided through the workflow, step by step.
- **Lifecycle Coverage.** Which APES stages (Discovery → Knowledge) the project addresses.
- **Supported AI Tools.** Which AI tools the project explicitly supports, endorses, or excludes.
- **Vendor Neutrality.** Self-claim and external assessment.
- **Human Approval Support.** Whether the project provides explicit gates, checkpoints, or review requirements.
- **Evidence Management.** Whether the project requires evidence for advancing through stages.
- **Assumption / Experiment Management.** Whether the project treats hypotheses as artifacts.
- **Product and Business Coverage.** Whether pricing, distribution, or viability is addressed.
- **Launch and Growth Coverage.** Whether distribution, activation, or retention is addressed.
- **Strengths.** Evidence-backed strengths, with citation.
- **Weaknesses.** Evidence-backed weaknesses, with citation.
- **Reusable Elements.** Artifacts APES should consider referencing or composing with.
- **Elements Not to Copy.** Artifacts APES should deliberately not duplicate.
- **Relationship to APES.** Compose, reference, decline-to-overlap, exclude.
- **Primary Evidence.** The source used to fill the fields above (Source IDs).
- **Access Date.**
- **Research Limitations.** What could not be verified, and why.

Core project analyses live as individual notes under `research/competitors/` or `research/ecosystem/` (see §9).

## 5. Source Categories and Sampling

| Category | Why included | Quality expectation | Sampling rule |
| --- | --- | --- | --- |
| Standards bodies (ISO, IEEE, NIST, OWASP) | Authoritative, durable, often vendor-neutral | High when primary; cross-check with at least one secondary source | Cover at least 5 distinct bodies across product and engineering. |
| Major open-source frameworks (Shape Up, Continuous Discovery, Spec-Kit, etc.) | Practitioner-scale adoption, public repos | Medium-high; check repo activity, not just stars | Cover at least 8 frameworks spanning product and AI coding. |
| AI coding tool vendors (Anthropic, OpenAI, Google, Cursor, etc.) | Direct ecosystem context | Medium; distinguish marketing from documentation | Treat official docs as primary; treat blog posts as secondary. |
| Academic literature | Generalizable claims | High when peer-reviewed | At least 3 peer-reviewed sources across software engineering and HCI. |
| Practitioner literature (books, conference talks) | Field-tested heuristics | Medium | Cross-check any "best practice" claim against at least one independent practitioner source. |
| Public case studies | Validate "in-use" claims | Variable | Verify the publishing organization and date. |
| Public roadmap documents (e.g., GitHub issues labeled roadmap) | Direction-of-travel evidence | Low–Medium | Use only when dated and attributed. |

The sampling rule is a floor, not a ceiling. If a category cannot meet the floor, that itself is a finding worth recording.

## 6. Research Questions and Hypotheses

These are the questions this research phase exists to answer. Each is a hypothesis to be tested, not a fact to be confirmed.

### 6.1 Lifecycle coverage

- **H-LC1.** Each APES lifecycle stage has at least one existing standard or framework that addresses it in depth.
- **H-LC2.** For at least one stage, no existing standard provides an *evidence-driven, AI-era–aware* methodology.
- **H-LC3.** For at least one stage, existing standards conflict with each other in ways that AI-assisted teams have to resolve ad hoc.

### 6.2 Tooling alignment

- **H-T1.** AI coding tools (Claude Code, Codex, Cursor, Copilot, Gemini CLI, aider, Continue, Cody) ship their own prompts, conventions, or `AGENTS.md`-style guidance that competes with — rather than composes with — a process-level standard.
- **H-T2.** Spec-driven Development tooling (e.g., github/spec-kit, OpenSpec) overlaps with APES's Validation → Product stage. The overlap must be characterized, not ignored.
- **H-T3.** MCP is a runtime protocol, not a process standard. APES must not duplicate or compete with MCP.

### 6.3 Standards and frameworks

- **H-S1.** Lean Startup, Continuous Discovery, Shape Up, and *Inspired*-style product practice already cover Discovery and Validation. APES must position *next to* these, not on top of them.
- **H-S2.** Engineering quality standards (OWASP, NIST SSDF, SRE, DORA) cover Engineering and Growth. APES must compose with these.
- **H-S3.** No widely-adopted standard today explicitly addresses the *evidence handoff* between AI-assisted engineering output and product/learning feedback loops.

### 6.4 Positioning

- **H-P1.** "Vendor-neutral, evidence-driven" is a defensible positioning if APES avoids prescribing tools, prompts, or model choices.
- **H-P2.** The "standard" framing (vs. framework, protocol, or workflow) is appropriate because APES is intended to be referenced by other projects, not run as a service.
- **H-P3.** If H-P2 is false, APES should reposition before drafting any module body.

### 6.5 Value gap

- **H-V1.** AI-assisted teams today ship code before validating the problem more often than non-AI-assisted teams, because AI lowers the cost of building.
- **H-V2.** If H-V1 is false, APES has no defensible reason to exist beyond curating existing standards.
- **H-V3.** The strongest value gap, if any, is at the boundary between Validation and Engineering — where AI lowers the cost of building *faster than teams can validate*.

H-V3 is the working hypothesis behind APES as currently scoped. This research phase must either confirm it with evidence or trigger a redirect.

## 7. Evidence Quality Criteria

Every Accepted note must score on four dimensions. Any single dimension scoring "Weak" disqualifies the note from Accepted status.

| Dimension | Strong | Moderate | Weak |
| --- | --- | --- | --- |
| Source authority | Primary source from standards body, vendor docs, or peer-reviewed paper | Secondary source from a credible practitioner publication | Anonymous, undated, or marketing-only source |
| Recency | Within the last 24 months for fast-moving areas (AI tools); within 5 years for stable standards | Within 5 years for fast-moving; older only with justification | Older without justification, or stale in a fast-moving area |
| Replicability | Source can be opened and re-read; URL stable; quote verifiable | Source exists but URL is unstable or behind a paywall (requires mirror in `research/`) | Source cannot be re-opened or quoted |
| Counter-evidence | Note records at least one disconfirming search and its result | Note records a disconfirming search but result is partial | Note does not attempt disconfirmation |

A note that scores "Weak" on any dimension is at most Draft and cannot drive a §1.2 decision.

## 8. Anti-Patterns to Prevent

The following are research defects. Each is paired with how this plan prevents it.

| Anti-pattern | Why it would harm APES | How this plan prevents it |
| --- | --- | --- |
| **Prompt-collection drift** | APES becomes a list of AI tips, not a standard. | Each note must tie to a §6 hypothesis and a §1.2 decision. Tips that do not change a decision are filed in `research/notes/`, not as Accepted evidence. |
| **Documentation accumulation** | The standard grows in pages but not in decisions supported. | Quarterly review (§10) prunes notes that did not change any decision. |
| **Reinventing existing standards** | APES duplicates Lean Startup, Shape Up, etc. | §6 H-S1/H-S2 force explicit "already covered" mapping before drafting. |
| **Vendor capture** | APES ends up endorsing a specific tool. | §2 Principle 5 + per-note "endorse vs. describe" check in §11 review. |
| **Premature tooling** | CLI/MCP/extension work begins before evidence exists. | §6 H-T* must produce Accepted evidence before any tooling proposal is allowed. |
| **Marketing-as-fact** | Claims about market position, adoption, or industry leadership appear in APES documents. | §1.3 forbids these claims, and §7 criterion 1 disqualifies marketing sources as primary evidence. |
| **Speculation dressed as research** | The note reads like an essay, not a finding. | §4.2 workflow forces Question, Source, Access date, Claim, Strength, Counter-evidence, Implication. |
| **Single-source claims** | Important decisions rest on one citation. | §1.2 decisions require at least two independent sources per Accepted claim. |

## 9. Deliverables and File Layout

This research phase produces exactly six artifact types, all under `research/`:

```
research/
├── research-plan.md                  # This file
├── source-register.md                # Source Register (Appendix A) populated from §4.6
├── ecosystem/
│   └── README.md                     # Final ecosystem note (Phase A+B output)
├── competitors/
│   └── README.md                     # Final competitor matrix (Phase B+C output)
├── papers/
│   └── README.md                     # Annotated bibliography
├── notes/
│   ├── README.md                     # Free-form observations (Draft only)
│   └── search-log.md                 # Search Log (Appendix D) populated from §4.7
└── positioning-evidence.md           # Phase D output; explicit go/redirect/stop evidence
```

In addition, this phase creates or modifies:

```
tasks/sprint-01-ecosystem-research-plan.md   # Sprint task file (input to this plan)
tasks/sprint-01-1-research-plan-review-fix.md # Plan review sprint
CHANGELOG.md                                  # Unreleased entry recording this sprint
research/README.md                            # Pointer to research-plan.md and phase outputs
```

**Per-phase output rules:**

- Phase A → populate `source-register.md` (Appendix A schema), at least one Source per category in §5, each reaching `Verified` via §11 review.
- Phase B → a stage × item matrix in `ecosystem/README.md` (or its appendix); one Core Project Analysis note per surviving project (Appendix E schema).
- Phase C → at least one gap note per lifecycle stage, each Accepted-quality, with conflicts and overlapping coverage preserved.
- Phase D → `positioning-evidence.md` with a per-decision §1.2 table and an explicit Research Gate decision (GO / PIVOT / STOP / RESEARCH AGAIN, see Appendix F).

No additional directories are created during research execution. New directories require an RFC.

## 10. Schedule, Cadence, and Stop Conditions

### 10.1 Cadence

- **Weekly:** reviewer passes the new notes from the week.
- **Bi-weekly:** maintainers review Accepted notes and confirm they change a §1.2 decision.
- **Quarterly:** prune Drafts that did not become Accepted; reaffirm or revise this plan.

### 10.2 Stop conditions

The research phase is considered complete, and the *next* decision point begins, when all of the following are true:

1. Every hypothesis in §6 has at least one Accepted-quality note addressing it.
2. `positioning-evidence.md` exists and covers all seven §1.2 decisions.
3. At least one maintainer has reviewed the evidence and recorded a *continue / redirect / stop* decision as an ADR (or as a proposal to do so).

### 10.3 Stop-the-research conditions (Kill Criteria)

Research is paused, redirected, or aborted when **any** of the following become supportable with Accepted evidence. Each item is a Go / Pivot / Stop signal; none is "neutral."

1. A mature, vendor-neutral existing solution already covers APES's full target surface end to end.
2. No credible evidence of an unmet product-engineering need can be found.
3. The only product APES could honestly produce is a prompt or template collection.
4. User research consistently shows the actual unmet need is better integration of existing tools, not a new standard.
5. The complexity required to follow APES exceeds the demonstrated adoption value.
6. APES cannot be validated against any real project within the planned scope.
7. APES cannot draw a stable, defensible boundary against existing standards.
8. "AI Product Engineering" turns out to be a re-labeling of existing software-engineering methodology without new content.
9. Maintainer resources are insufficient to meet the review and governance requirements in §10 and §11.

A single Kill Criterion firing is sufficient to trigger a Research Gate review. It is not a failure of the plan; it is the plan working. The next deliverable after a Kill firing is one of:

- **PIVOT** — revise positioning, scope, or artifact form based on evidence.
- **STOP** — halt APES, document the decision as an ADR.
- **RESEARCH AGAIN** — fill specific evidence gaps before re-entering the gate.

### 10.4 Research Checkpoints

Every phase must pass through six checkpoints before its output is marked Accepted. A checkpoint is a documented review that produces an explicit pass or fail.

1. **Search Coverage Checkpoint.** Has every §6 hypothesis been searched for at least once in primary-source channels?
2. **Source Quality Checkpoint.** Does every Source in the register have a Reliability Level (Appendix B) and Verification Status (Pending / Verified / Disputed)?
3. **Core Project Selection Checkpoint.** Have all surviving candidates passed the Candidate Selection Criteria (Appendix C)?
4. **Evidence Review Checkpoint.** Has every Accepted claim produced counter-evidence (per §4.3) and at least two independent supporting sources?
5. **Gap Review Checkpoint.** Has every APES lifecycle stage been mapped against the inventoried projects and given an explicit gap statement?
6. **Final Research Gate.** Final go / pivot / stop decision (see Appendix F).

A phase is not allowed to skip a checkpoint. A failed checkpoint returns the phase to its drafting step.

## 11. Governance, Review, and Disagreement Handling

### 11.1 Roles

- **Researcher.** Drafts notes per §4.2. Cannot self-accept.
- **Reviewer.** Independently challenges each Draft. Confirms or rejects.
- **Maintainer.** Accepts evidence into APES decision-making; writes or commissions the resulting ADR.

### 11.2 Review rules

- Every Accepted note requires at least one reviewer challenge per §7 dimensions.
- If reviewer and researcher disagree, the disagreement is recorded inline in the note, not silently resolved.
- Endorsement language in a note is a review failure, regardless of the underlying claim.

### 11.3 Disagreement log

When two reviewers cannot agree, the dispute is logged in `research/notes/` with:

- The disputed claim.
- Each side's evidence and counter-evidence.
- The unresolved question.

The log is itself Draft, not Accepted, until a maintainer issues an ADR.

## 12. Outputs That Feed Back Into APES

The research phase is not an end in itself. Each Accepted note must specify its target, drawn from this list:

- A positioning decision in §1.2 → ADR.
- A lifecycle-stage coverage gap → RFC for a module standard.
- A lifecycle-stage duplication → design document or RFC for a *composition* pattern with the existing standard.
- An AI-tool ecosystem observation → usage note in `docs/` or `commands/` once those directories become Drafts (not in this sprint).
- A paper → annotated bibliography entry that informs a future module.

Outputs that have no target are not Accepted. They remain in `research/notes/` as observations.

## 13. Risks, Limitations, and Known Unknowns

- **Confirmation bias.** The plan's strongest hypothesis (H-V3) is the one most likely to drive every note. Counter-evidence searches (§4.3) are the planned mitigation.
- **Recency bias in AI-tool sources.** Vendor docs change weekly. Every Accepted AI-tool claim must carry an access date and be rechecked before use in downstream APES documents.
- **Standards-body access.** Some standards are paywalled or only available to members. Where mirrors are not available, the note's replicability score (§7) drops to Moderate at best, and the Reliability Level (Appendix B) is capped at Level B.
- **Maintainer bandwidth.** Review cadence (§10) assumes at least one reviewer has time weekly. If not, the research pauses rather than ships un-reviewed notes.
- **Coverage illusion.** Inventorying many sources does not mean we have read them in depth. Phase A records a *coverage* claim and Phase B/C apply the depth check.
- **Unknown unknowns.** Some relevant standards may exist but not surface in standard search. This is acceptable; the plan is not exhaustive by design.

## 14. Research Priority Order

Priority determines **search and analysis order**, not quality or importance ranking. Sources in Priority 0 are searched first; lower priorities are visited only when higher-priority evidence is insufficient to support a §1.2 decision.

### Priority 0 — Direct Adjacencies and Official Tooling

The candidates below sit directly next to APES's planned scope. They are searched first because their answers most directly decide whether APES is duplicating or complementing existing work.

- `AGENTS.md` / `CLAUDE.md` conventions
- Claude Code (Anthropic)
- OpenAI Codex
- GitHub Copilot
- Cursor
- Gemini CLI
- Model Context Protocol (MCP)
- Spec Kit (github/spec-kit)
- OpenSpec

### Priority 1 — Product Discovery and Validation Methods

- Lean Startup
- Continuous Discovery (Marty Cagan / Teresa Torres)
- Shape Up (Basecamp)
- Dual-Track Agile
- Jobs to Be Done (JTBD)
- Product Discovery (general practitioner literature)

### Priority 2 — Engineering, Governance, and Security Standards

- Architecture Decision Records (ADRs)
- RFC process
- NIST SSDF (Secure Software Development Framework)
- OWASP
- Site Reliability Engineering (SRE)
- DORA metrics / DevOps Research and Assessment
- Relevant ISO / IEEE software life-cycle standards

### Priority 3 — Supplementary Material

- Peer-reviewed academic papers
- Community discussion (Level D per Appendix B)
- Case studies (verified)
- Failed or archived projects
- Stopped-maintenance projects

---

# Appendix

## A. Source Register Schema

> Specified in §4.6. Reprinted here as a stand-alone reference.

| Field | Required | Notes |
| --- | --- | --- |
| Source ID | yes | Stable, e.g., `SR-0007`. |
| Title | yes | Full title. |
| Source Type | yes | Standards document, vendor docs, paper, talk, book, blog, repo, case study, thread. |
| Publisher / Author | yes | |
| URL | yes | Canonical URL or stable identifier. |
| Publication Date | yes | `unknown` only with justification. |
| Access Date | yes | |
| Related Research Question / Hypothesis | yes | Pointer to §6. |
| Reliability Level | yes | A–E per Appendix B. |
| Primary / Secondary Source | yes | |
| Key Evidence | yes | Quote or precise paraphrase with section/page pointer. |
| Contradictory Evidence | yes | `none observed` acceptable. |
| Limitations | yes | Scope, recency, bias, paywall. |
| Verification Status | yes | `Pending` → `Verified` after §11 review. |
| Notes | optional | |

## B. Reliability Classification (A–E)

Level A–E evaluates **the source itself**, distinct from the per-note Strong / Moderate / Weak score in §7 which evaluates **the evidence note's quality**. A Level A source can still host a Weak note if the quote is misleading; a Level C source can still host a Strong note if the claim is well-framed and counter-evidenced.

### Level A

Official standards documents, official specifications, official repositories, original peer-reviewed papers.

Examples: ISO/IEC standards, IEEE standards, NIST publications, official vendor documentation, the canonical repository of an active project, peer-reviewed papers in established venues.

### Level B

Maintainer documentation, formal technical reports, mature project design documents.

Examples: ADRs/RFCs from active projects, technical white papers from recognized research labs, design documents published with an active project, well-cited conference proceedings.

### Level C

High-quality technical analysis, conference talks by named practitioners, credible case studies.

Examples: ACM Queue articles, well-attributed blog posts by practitioners with verifiable track records, conference talk recordings with slides, documented case studies from identifiable organizations.

### Level D

GitHub Discussions, Hacker News, Reddit, Product Hunt, user reviews.

Examples: product reviews, forum threads, social discussions. Used primarily to discover user language, pain points, and disagreements. Never the sole support for a critical conclusion.

### Level E

Sources of unknown provenance, unverifiable claims, marketing re-posts without original citation, AI-generated content without a cited primary source.

Examples: unattributed listicles, recycling of marketing copy, model-generated summaries without citation. **Level E sources cannot support a critical conclusion under any circumstance.**

### Cross-source rules

- Critical conclusions require at least two independent supporting sources **of different types**. Two Level A sources of the same type from the same publisher do not satisfy this.
- Conflicts and counter-evidence are preserved and recorded; they are not papered over.
- Level D is permitted to inform user language and pain points, not to drive conclusions.
- A note that depends on Level E alone cannot be Accepted; at most Draft.

## C. Candidate Selection Criteria

A candidate project enters the Core Project Analysis only when **all** inclusion criteria are satisfied. A candidate is excluded when **any** exclusion criterion fires.

### Inclusion criteria

- Directly relevant to one or more §6 research questions.
- Has official documentation or an original repository.
- Has an actual implementation, not only a marketing introduction.
- License is identifiable.
- Maintenance state is discernible from evidence.
- Provides analyzable features, architecture, or workflow.
- Either still active, or has clear historical research value.
- Contributes reusable experience or a well-documented counter-example.

### Exclusion criteria

- Empty repository.
- Fork with no substantive modifications.
- Promotional page only.
- Author and provenance cannot be confirmed.
- Severely outdated with no historical research value.
- No direct relationship to the APES lifecycle.
- Substantially duplicates another candidate's content.
- Relies primarily on unverified promotional claims.

A candidate that fails any exclusion criterion is logged in the search log (Appendix D) with the reason, then not analyzed further.

## D. Search Log Schema

> Specified in §4.7. Reprinted here as a stand-alone reference.

| Field | Required | Notes |
| --- | --- | --- |
| Search ID | yes | e.g., `SE-0012`. |
| Query | yes | Exact string used. |
| Platform | yes | |
| Search Date | yes | |
| Filters | yes | Language, range, type, license filters. |
| Approximate Result Count | yes | As returned. |
| Selected Sources | yes | Source IDs from the register. |
| Exclusion Reasons | yes | Why other top results were rejected. |
| Notes | optional | Variants tried, etc. |

## E. Core Project Analysis Schema

> Specified in §4.8. Fields enumerated below for fast lookup.

- Project ID
- Name
- Official URL
- Repository URL
- Positioning (self-quoted)
- Target Users (self-quoted)
- License (SPDX or "no clear license")
- Created Date
- Last Updated
- Maintenance Status (Active / Maintenance / Archived / Abandoned, with evidence)
- Technology Stack
- Core Features (3–10, in project vocabulary)
- Workflow (step by step)
- Lifecycle Coverage (Discovery → Knowledge)
- Supported AI Tools
- Vendor Neutrality (self-claim + external)
- Human Approval Support
- Evidence Management
- Assumption / Experiment Management
- Product and Business Coverage
- Launch and Growth Coverage
- Strengths (cited)
- Weaknesses (cited)
- Reusable Elements
- Elements Not to Copy
- Relationship to APES (Compose / Reference / Decline-to-overlap / Exclude)
- Primary Evidence (Source IDs)
- Access Date
- Research Limitations

## F. Final Research Gate

The Final Research Gate is reached when §10.2's stop-conditions are met. The output of the gate is exactly one of:

- **GO.** Evidence supports continuing APES into module-level work.
- **PIVOT.** Evidence supports continuing APES in a redirected scope, framing, or artifact form.
- **STOP.** Evidence does not support continuing APES; the project pauses and the decision is captured as an ADR.
- **RESEARCH AGAIN.** Evidence is insufficient at specific points; targeted research is commissioned and the gate is re-entered.

The default is **not** GO. A gate fires PIVOT, STOP, or RESEARCH AGAIN whenever the evidence does not unambiguously support GO.
