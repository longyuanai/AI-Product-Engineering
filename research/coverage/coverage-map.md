# research/coverage/coverage-map.md

- Status: Draft
- Version: v0.1
- Owner: APES Maintainers
- Last Updated: 2026-08-03
- Purpose: Apply **Phase B (Coverage Map)** of `research/research-plan.md` §4.1 to the 10 Selected projects in `research/competitors/candidate-projects.md`. Describe each project's **lifecycle responsibility**, **primary purpose**, **artifact types**, **engineering scope**, **standards involved**, **governance role**, and **security role** based only on evidence recorded in `research/competitors/reverse-research.md` and `research/source-register.md`. This is **NOT** a feature comparison; this is **NOT** a gap analysis; this is **NOT** APES positioning.

## Coverage Mapping Rules (Applied Throughout)

1. **Coverage Mapping is NOT Feature Comparison.** A project covering the same lifecycle stage does **NOT** imply feature parity. Coverage describes **observed lifecycle responsibility** of the artifact as recorded in reverse research; it does **not** rate quality, completeness, or APES-compatibility.
2. **Never compare implementations.** Never compare product quality. Only describe observed lifecycle responsibility.
3. **If evidence does not exist: Unknown.** Never infer lifecycle coverage where no source-backed evidence exists.
4. **If evidence conflicts: record BOTH.** Do **not** resolve conflicts. Do **not** decide which side is correct.
5. **Source IDs only.** Every claim below references `SRC-NNN` from `research/source-register.md` and the corresponding section of `research/competitors/reverse-research.md`.
6. **No APES evaluation.** No statement that APES is missing something, that any project is better or worse, or that APES should adopt or reject anything. These are observed facts, not opinions.

## Lifecycle Stages Used

This Coverage Map uses the **Sprint 3 lifecycle stage set** (broader than the APES 9-stage lifecycle in `README.md`, so coverage can be described independently of APES's own taxonomy). The 19 stages:

- Idea
- Discovery
- Research
- Requirements
- Specification
- Architecture
- Planning
- Implementation
- Coding
- Testing
- Review
- Documentation
- Release
- Operation
- Maintenance
- Knowledge Management
- Governance
- Security
- Continuous Improvement

For each project, see `lifecycle-coverage-matrix.md` for the row-by-row cell values.

## Artifact Types Used

This Coverage Map references the artifact vocabulary defined in `artifact-relationship-map.md`: AGENTS.md, CLAUDE.md, SPEC, RFC, ADR, Task, Checklist, Template, Prompt, Policy, Workflow, Architecture Decision, Knowledge Base, Standard, Command. For each project, see `artifact-relationship-map.md` for artifact-level details.

---

## S-01. Continuous Discovery (Teresa Torres / Product Talk)

### Lifecycle Responsibility

Observed responsibility spans **Discovery** and **Research** stages. The project's process model begins with defining a desired outcome, mapping opportunities, generating solutions, designing assumption tests, and iterating weekly. None of the stages beyond Discovery/Research are claimed by the project's process model.

### Primary Purpose

Helping product teams move from periodic, episodic discovery to a weekly habit of customer touchpoints that inform product decisions. Source: S-01 §2 (Stated Problem) in `research/competitors/reverse-research.md`.

### Artifact Types

- **OST visualization** (S-01 §8): commonly rendered in Miro / FigJam / wall tools; not a self-contained artifact format.
- **Assumption-test cards / templates** (S-01 §8): paper templates; no canonical Markdown schema is defined by the project.
- **Interview synthesis notes** (S-01 §8): free-form practitioner artifact.

### Engineering Scope

The project does **not** prescribe engineering implementation, security practices, or business model design (S-01 §4 Scope Out). It explicitly stops at validated opportunities and tested solutions.

### Standards Involved

None observed in S-01 §4 (Scope In) or S-01 §10 (Adjacent). References to JTBD theory, Lean Startup framing, and Inspired (Cagan) are framed as **adjacent practitioner methodologies**, not as standards.

### Governance Role

None observed. The project is a practitioner methodology; no formal review board, change-control, or audit trail is described (S-01 §4 Scope Out; S-01 §6 Process Model).

### Security Role

None observed. The project does not address security controls or secure-development practice (S-01 §4 Scope Out).

### Evidence

- Source IDs: SRC-008, SRC-012, SRC-036.
- Claim Type: Practitioner opinion (book + practitioner templates).
- Claim Verification: Page Unverified (Product Talk site blocked by WebFetch); publisher and library catalog corroborate 2021 publication date (S-01 §13).
- Evidence Location: `research/competitors/reverse-research.md` §S-01.
- Confidence: Medium (multi-source corroboration of publication and scope; primary page not directly read in this access window).

---

## S-02. Inspired: Creating Tech Products Customers Love (Marty Cagan / SVPG)

### Lifecycle Responsibility

Observed responsibility spans **Discovery** and **Planning** stages. The project separates Discovery from Delivery (which it places in engineering's domain) and frames mission, prototype, and customer-validation cycles.

### Primary Purpose

Helping technology companies build products customers love by structuring empowered product teams and separating product discovery from product delivery. Source: S-02 §2 (Stated Problem).

### Artifact Types

- **Mission framing documents** (S-02 §8): no fixed template defined by the project.
- **Prototype assets** (S-02 §8): the artifact type is the prototype, not the spec.
- **Discovery artifacts** (S-02 §8): interview notes, opportunity assessments; no canonical schema.

### Engineering Scope

The project explicitly **does not** specify engineering pipeline, security, or lifecycle standards (S-02 §4 Scope Out). The Discovery / Delivery hand-off is a team-topology boundary, not an engineering process prescription.

### Standards Involved

None observed. References to Continuous Discovery, Shape Up, and Lean Startup are framed as **adjacent practitioner methodologies**, not as standards.

### Governance Role

Team-level governance only — the empowered-product-team pattern is organizational, not process-governance in the standards sense (S-02 §4 Scope Out; §6 Process Model).

### Security Role

None observed. The project does not address security practice (S-02 §4 Scope Out).

### Evidence

- Source IDs: SRC-009, SRC-035.
- Claim Type: Practitioner opinion (book + SVPG site content).
- Claim Verification: Page Unverified (SVPG site blocked); publisher corroborates first edition (S-02 §13).
- Evidence Location: `research/competitors/reverse-research.md` §S-02.
- Confidence: Medium.

---

## S-03. Shape Up (Basecamp / Ryan Singer)

### Lifecycle Responsibility

Observed responsibility spans **Discovery** (Shaping), **Planning** (Betting Table), **Implementation** (Build), and **Release** (Cool-down / ship). The fixed-time, variable-scope cycle explicitly stops short of continuous customer touchpoints.

### Primary Purpose

Helping teams ship meaningful work on a fixed cycle without the rigidities of traditional project management. Source: S-03 §2 (Stated Problem).

### Artifact Types

- **Hill Charts** (S-03 §8): a progress-visualization artifact, not a Markdown schema.
- **Shaping documents** (S-03 §8): no fixed template.
- **Betting table artifacts** (S-03 §8): the table itself is the artifact.

### Engineering Scope

The project **does not** specify engineering practice, security controls, or formal governance (S-03 §4 Scope Out). It is a project-management cycle, not an engineering methodology.

### Standards Involved

None observed. References to Lean Startup and Continuous Discovery are framed as adjacent methodologies with **disagreements** about cadence, not as standards.

### Governance Role

Betting Table is the closest equivalent to a governance mechanism, but it operates at project-selection granularity, not at engineering practice granularity (S-03 §6 Process Model).

### Security Role

None observed.

### Evidence

- Source IDs: SRC-011, SRC-037.
- Claim Type: Practitioner opinion (free online book + Basecamp product practice).
- Claim Verification: Page Unverified (basecamp.com/shapeup blocked); multiple independent community sources corroborate 2019 release (S-03 §13).
- Evidence Location: `research/competitors/reverse-research.md` §S-03.
- Confidence: Medium.

---

## S-04. Jobs to Be Done — Christensen Line

### Lifecycle Responsibility

Observed responsibility spans **Discovery** and **Research** stages, with the **Job Map** artifact positioned at the Requirements level (mapping jobs into functional / emotional / social dimensions).

### Primary Purpose

Helping firms understand why customers "hire" products, by focusing on the underlying job the customer is trying to get done rather than on product features or demographics. Source: S-04 §2 (Stated Problem).

### Artifact Types

- **Job Map** (S-04 §8): the 8-step universal-progress map is a defined artifact.
- **Job Story** (S-04 §8): "When... I want to... So I can..." format is a defined artifact.

### Engineering Scope

The project **does not** address engineering practice or governance (S-04 §4 Scope Out; §12 Open Questions). It is a theoretical framework, not a process standard.

### Standards Involved

None observed. JTBD is a theory-level lens; it is not codified as a formal standard.

### Governance Role

None observed.

### Security Role

None observed.

### Evidence

- Source IDs: SRC-013, SRC-038.
- Claim Type: Practitioner opinion + academic theory (HBS / publisher).
- Claim Verification: Page Unverified (HBS / Strategyn pages blocked); publisher corroborates 2016 book (S-04 §13).
- Evidence Location: `research/competitors/reverse-research.md` §S-04.
- Confidence: Medium.
- **Note on attribution dispute.** S-04 §11 and §12 record a **preserved, unresolved dispute** between Christensen and Ulwick (S-05) about the methodological origin of JTBD. APES does **not** adjudicate. Both are recorded.

---

## S-05. Outcome-Driven Innovation (Tony Ulwick / Strategyn)

### Lifecycle Responsibility

Observed responsibility spans **Discovery** and **Research** stages, with a **quantitative** angle (surveys, importance/satisfaction gap, opportunity scoring) that lands at the **Planning** stage as input to a prioritized roadmap.

### Primary Purpose

Helping firms identify and prioritize market opportunities by measuring customer desired outcomes rather than relying on demographic or feature-based segmentation. Source: S-05 §2 (Stated Problem).

### Artifact Types

- **Outcome surveys** (S-05 §8): structured surveys.
- **Opportunity scoring spreadsheet** (S-05 §8): the quantitative output is a spreadsheet, not a canonical artifact schema.

### Engineering Scope

The project **does not** address engineering practice or governance (S-05 §4 Scope Out).

### Standards Involved

None observed.

### Governance Role

None observed.

### Security Role

None observed.

### Evidence

- Source IDs: SRC-013, SRC-038 (shared with S-04).
- Claim Type: Practitioner opinion + proprietary methodology.
- Claim Verification: Page Unverified (Strategyn site blocked); publisher corroborates Ulwick's book (S-05 §13).
- Evidence Location: `research/competitors/reverse-research.md` §S-05.
- Confidence: Medium.
- **Note on attribution dispute.** Same preserved dispute as S-04 §11. APES does **not** adjudicate.

---

## S-06. Architecture Decision Record (Michael Nygard)

### Lifecycle Responsibility

Observed responsibility spans **Architecture** and **Documentation** stages. The record captures one architectural decision and persists it over time with status updates (Superseded / Deprecated).

### Primary Purpose

Helping teams capture architectural decisions, including their context and consequences, so the reasoning behind decisions is preserved over time. Source: S-06 §2 (Stated Problem).

### Artifact Types

- **ADR file** (S-06 §7; §8): typically Markdown in `docs/adr/` with filename pattern `NNNN-title.md`. This is the **canonical artifact** of the project.
- Adjacent variants: MADR (structured options / tradeoffs); lightweight ADR variants (stripped sections).

### Engineering Scope

The project **does not** prescribe execution details, customer research, or security policy (S-06 §4 Scope Out). It is a record format, not a process.

### Standards Involved

None formally codified by Nygard's original blog post. ADR is widely emulated and appears in adjacent artifact clusters (Spec Kit, OpenSpec) but is not itself an ISO/IEEE/NIST standard.

### Governance Role

The **Status field** (Proposed / Accepted / Deprecated / Superseded) is the closest mechanism to a governance role, but it is record-keeping, not enforcement. No prescribed review workflow (S-06 §12).

### Security Role

None observed.

### Evidence

- Source IDs: SRC-002, SRC-040.
- Claim Type: Practitioner convention + community tooling.
- Claim Verification: Partially Verified (cognitect blog + adr.github.io corroboration; full primary text not directly read in this access window).
- Evidence Location: `research/competitors/reverse-research.md` §S-06.
- Confidence: Medium (multi-source corroboration of publication and scope; primary page not directly read in this access window).
- **Sprint 3.1 audit correction.** Original Sprint 3 confidence label was `High`. Downgraded to `Medium` because SRC-002 and SRC-040 are both `Partially Verified` in `research/source-register.md` v0.5 — neither reaches the `High` threshold under the matrix Confidence Scale. Cell value (`Primary`) is unchanged.

---

## S-07. OpenSpec (Fission-AI)

### Lifecycle Responsibility

Observed responsibility spans **Specification**, **Planning** (Change Proposal), **Review**, **Implementation**, and **Documentation** (Update) stages. The format is described as a vendor-neutral spec/plan format for AI-coding workflows.

### Primary Purpose

Providing a vendor-neutral, open format for specifications and change proposals that AI coding tools and human teams can both consume. Source: S-07 §2 (Stated Problem).

### Artifact Types

- **Spec** (S-07 §5).
- **Change Proposal** (S-07 §5).
- **Task** (S-07 §5).
- **Approval** (S-07 §5): review state, not a separate artifact type.
- CLI commands for proposing / approving changes (S-07 §8).

### Engineering Scope

The project **does not** cover full project management, security policy, or business modeling (S-07 §4 Scope Out).

### Standards Involved

None observed. The project is a convention, not a standards-body document.

### Governance Role

The review/approval workflow is a lightweight governance mechanism at the spec/change level, not at the engineering process level (S-07 §6 Process Model).

### Security Role

None observed.

### Evidence

- Source IDs: SRC-026.
- Claim Type: Observable repository fact (community open source project).
- Claim Verification: Partially Verified (repo exists per repository metadata; license Unverified; v0.17.0 reference corroborated by community).
- Evidence Location: `research/competitors/reverse-research.md` §S-07.
- Confidence: Medium.

---

## S-08. Spec Kit (GitHub)

### Lifecycle Responsibility

Observed responsibility spans **Specification**, **Planning** (Change Proposal), **Review**, **Implementation**, and **Documentation** (Update) stages. Vendor-led counterpart to OpenSpec with GitHub CLI integration.

### Primary Purpose

Providing tooling and templates for spec-driven development, particularly aimed at AI-coding workflows. Source: S-08 §2 (Stated Problem).

### Artifact Types

- **Spec templates** (S-08 §8): Markdown templates.
- **Change Proposals** (S-08 §5).
- **Review / Approval states** (S-08 §5).
- GitHub CLI integration (S-08 §8).

### Engineering Scope

The project **does not** cover full lifecycle governance or business modeling (S-08 §4 Scope Out).

### Standards Involved

None observed.

### Governance Role

GitHub-native review/approval mechanisms are the closest equivalent to a governance role, operating at the spec/change level (S-08 §6 Process Model).

### Security Role

None observed.

### Evidence

- Source IDs: SRC-025.
- Claim Type: Observable repository fact (vendor-led open source project).
- Claim Verification: Partially Verified (repo exists per repository metadata; license Unverified; 2025-09 release corroborated by community).
- Evidence Location: `research/competitors/reverse-research.md` §S-08.
- Confidence: Medium.

---

## S-09. Claude Code (Anthropic)

### Lifecycle Responsibility

Observed responsibility spans **Planning** (Plan mode artifacts) and **Implementation** (agentic CLI coding). The vendor-documented process is: read project context (including AGENTS.md), plan, execute via tools, report back to the user.

### Primary Purpose

Providing an agentic CLI for coding tasks that combines a coding-capable model with tool use, file access, and execution context. Source: S-09 §2 (Stated Problem).

### Artifact Types

- **AGENTS.md** (S-09 §5; §8): per vendor docs, the project consumes this file as authoritative project context.
- **Plan mode artifacts** (S-09 §8): the plan-then-execute interaction produces plan artifacts.
- **Permission / tool-use configuration** (S-09 §8): the project exposes configuration of which tools the agent may invoke.

### Engineering Scope

The project **does not** cover full project lifecycle governance or security policy (S-09 §4 Scope Out). It is an agentic CLI, not a process standard.

### Standards Involved

None observed.

### Governance Role

Vendor-defined. Treats user confirmation as a checkpoint; treats AGENTS.md as authoritative project context (S-09 §9 Quality and Evidence Discipline). This is a product behavior, not a process governance standard.

### Security Role

None observed as a defined responsibility. The project **consumes** AGENTS.md (S-10) which may carry security rules, but the project itself does not define a security framework.

### Evidence

- Source IDs: SRC-014.
- Claim Type: Vendor self-description + observable product behavior.
- Claim Verification: Unverified (anthropic.com blocked by WebFetch; vendor documentation corroborated via community sources — S-09 §13).
- Evidence Location: `research/competitors/reverse-research.md` §S-09.
- Confidence: Low–Medium (vendor documentation not directly read).

---

## S-10. AGENTS.md (Open Community Convention)

### Lifecycle Responsibility

Observed responsibility spans **Coding** and **Implementation** stages in the lifecycle of AI-assisted development. The convention provides a top-level, predictable place in a repository where AI coding agents read project-specific guidance. It is a **consumer-side convention** for AI agents, not a process standard for human teams.

### Primary Purpose

Providing a top-level, predictable place in a repository where AI coding agents can read project-specific guidance (build, test, conventions, safety rules). Source: S-10 §2 (Stated Problem). Verified externally via EV-001: the project page positions AGENTS.md as a "simple, open format to guide AI coding agents."

### Artifact Types

- **AGENTS.md** (S-10 §5; §8): a single Markdown file at repo root.
- **Cross-references** (S-10 §5): commonly to CONTRIBUTING.md, README.md, docs/.

### Engineering Scope

The project **does not** provide execution enforcement or a security policy framework (S-10 §4 Scope Out). It is content that an agent reads; the agent's behavior modification is the responsibility of the consuming agent.

### Standards Involved

None observed. AGENTS.md is a convention, not a standards-body document.

### Governance Role

Maintainer-authored content is treated as authoritative project guidance (S-10 §9 Quality and Evidence Discipline). This is a content convention, not an enforcement mechanism.

### Security Role

None observed as a defined responsibility. AGENTS.md may **carry** security rules authored by the project maintainer, but the convention itself does not prescribe what those rules must be.

### Evidence

- Source IDs: SRC-001, SRC-044, SRC-045.
- Claim Type:
  - SRC-001: Official self-description (AGENTS.md project page). **Verified** via EV-001.
  - SRC-044: Independent empirical evidence (arXiv 2602.11988). **Verified** via EV-003.
  - SRC-045: Independent empirical evidence (arXiv 2601.20404). **Verified** via EV-004.
- Claim Verification: All three `Verified` per Sprint 2.3 external verification reconciliation. Method details beyond abstract remain `Partially Verified` for SRC-044 and SRC-045.
- Evidence Location: `research/competitors/reverse-research.md` §S-10 (identity, §11 conflicting approaches, §13 verification notes).
- Confidence: High for SRC-001 page content and abstract-level claims of SRC-044/SRC-045. Medium for full method comparison (PDF body not directly read).
- **Conflicting empirical evidence** (S-10 §11): SRC-044 and SRC-045 disagree on direction (one finds harm to task success and cost; the other finds similar task success and lower cost). APES does **not** adjudicate.

---

## Cross-Project Patterns Observed (Descriptive, Non-Conclusory)

The following observations are descriptive. They are **not** APES positioning, gap claims, or market conclusions.

1. **Discovery methodologies** (S-01 Continuous Discovery, S-02 Inspired, S-03 Shape Up, S-04 JTBD / S-05 ODI) all describe a Discovery / Research lifecycle responsibility. They differ in cadence (weekly vs. cyclical vs. as-needed) and structure (OST vs. mission vs. hill charts vs. job / outcome).
2. **Decision / spec / agent-context artifacts** (S-06 ADR, S-07 OpenSpec, S-08 Spec Kit, S-10 AGENTS.md) all share the convention of a structured, human-readable (and in some cases machine-readable) text artifact. They differ in scope: ADRs capture one decision; OpenSpec / Spec Kit capture plans and changes; AGENTS.md captures persistent agent guidance.
3. **AI coding agents** (S-09 Claude Code) **consume** the convention files and repo context; the cluster does not converge on a single shared spec format yet.
4. **None** of the 10 Selected projects describe themselves as a complete lifecycle standard covering all 19 Sprint 3 stages. The Coverage Map records what each project does describe, not what it does not.
5. **Standards / governance clusters** (S-04 / S-05 evidence base; S-06 record-keeping; S-07 / S-08 change review) are observed at the artifact level, not at the formal-standards-body level.

These are observed patterns only. They do not assert a coverage claim for APES.

## Cross-References

- `research/competitors/reverse-research.md` — 14-section source data for each project.
- `research/competitors/candidate-projects.md` — short list of 10 Selected projects.
- `research/source-register.md` — Source IDs cited above (SRC-001 through SRC-052).
- `research/notes/verification-log.md` — Sprint 2.2 Inaccessible attempts + Sprint 2.3 External Verification Reconciliation entries (EV-001 through EV-006).
- `research/coverage/lifecycle-coverage-matrix.md` — matrix view of lifecycle responsibility.
- `research/coverage/artifact-relationship-map.md` — artifact-level view across 15 artifact types.
- `research/research-plan.md` — Phase B definition.
- `tasks/sprint-03-coverage-map.md` — Sprint 3 task file.
