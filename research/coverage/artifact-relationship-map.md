# research/coverage/artifact-relationship-map.md

- Status: Draft
- Version: v0.1
- Owner: APES Maintainers
- Last Updated: 2026-08-03
- Purpose: Map each of 15 **artifact types** to the Selected projects that produce or consume them, based only on evidence in `research/competitors/reverse-research.md`. For each artifact type, describe Purpose, Inputs, Outputs, Dependencies, Lifecycle position, Ownership, and Evidence. This is **NOT** an APES design; it is a **descriptive** map of what artifact conventions already exist in the observed landscape.

## Artifact Types Covered

This map covers the 15 artifact types named in the Sprint 3 brief:

1. **AGENTS.md** — root-level repository guidance file for AI coding agents.
2. **CLAUDE.md** — vendor-specific guidance file (Anthropic Claude Code convention; referenced in the brief but not produced by any of the 10 Selected projects in this access window).
3. **SPEC** — formal specification document.
4. **RFC** — Request for Comments document.
5. **ADR** — Architecture Decision Record.
6. **Task** — discrete unit of work.
7. **Checklist** — enumerated verification or process steps.
8. **Template** — pre-structured document scaffold.
9. **Prompt** — instruction text for an AI/LLM.
10. **Policy** — organization-level rule.
11. **Workflow** — defined process sequence.
12. **Architecture Decision** — recorded decision and its consequences.
13. **Knowledge Base** — persistent organized repository of information.
14. **Standard** — formally codified practice.
15. **Command** — CLI invocation or shell command.

For each artifact type, the map records which Selected projects (S-01 through S-10) **produce**, **consume**, or **reference** the artifact, with source-backed evidence. Where no Selected project touches an artifact type, the cell is marked "Not observed in Selected projects".

---

## 1. AGENTS.md

- **Purpose** (per S-10 §2; verified externally via EV-001): top-level, predictable place in a repository where AI coding agents can read project-specific guidance (build, test, conventions, safety rules).
- **Inputs**: AGENTS.md text authored by project maintainers; cross-references to CONTRIBUTING.md, README.md, docs/.
- **Outputs**: agent behavior modifiers (consumed at agent context load time).
- **Dependencies**: Markdown; a consuming agent (Claude Code, OpenAI Codex CLI, Gemini CLI per S-10 §10).
- **Lifecycle position**: Coding / Implementation stages (per `research/coverage/lifecycle-coverage-matrix.md` S-10).
- **Ownership**: Project maintainers; open convention, no single steward.
- **Selected projects producing or consuming**:
  - **Produced by**: open convention (S-10).
  - **Consumed by**: S-09 (Claude Code, per vendor docs), and reportedly by S-10 (other AI coding agents).
- **Evidence**: SRC-001 (Verified via EV-001), SRC-044 (Verified via EV-003 at abstract level), SRC-045 (Verified via EV-004 at abstract level).
- **Conflicting empirical evidence**: SRC-044 finds repository-level context files (including AGENTS.md) generally tended to lower task success and increase inference cost; SRC-045 finds AGENTS.md associated with lower median runtime and lower output-token consumption with task-completion performance roughly similar. Both `Verified` at abstract level. APES does **not** adjudicate.

## 2. CLAUDE.md

- **Purpose**: vendor-specific guidance file for Anthropic Claude Code (referenced in the Sprint 3 brief; **no Selected project in this access window produces or consumes CLAUDE.md as its primary artifact**).
- **Inputs**: project maintainer content.
- **Outputs**: Claude Code behavior modifiers.
- **Dependencies**: Claude Code vendor; Markdown.
- **Lifecycle position**: Coding / Implementation stages (similar to AGENTS.md).
- **Ownership**: Anthropic; project maintainers.
- **Selected projects producing or consuming**: **Not observed in Selected projects.** S-09 (Claude Code) consumes guidance files per vendor docs, but the artifact is AGENTS.md, not CLAUDE.md, in the recorded reverse-research evidence.
- **Evidence**: No direct evidence in `research/competitors/reverse-research.md` §S-09 for CLAUDE.md as a distinct artifact type. AGENTS.md is the named artifact in S-09 §5 and §8.

## 3. SPEC

- **Purpose** (per S-07 §5; S-08 §5): formal specification document capturing intent and proposed change for AI-coding workflows.
- **Inputs**: intent, proposed change.
- **Outputs**: spec / change artifact files (Markdown per S-08 §8; structured Markdown per S-07 §8).
- **Dependencies**: a consuming agent or human reviewer.
- **Lifecycle position**: Specification, Planning (Change Proposal) stages (per `lifecycle-coverage-matrix.md`).
- **Ownership**: project / spec author; review/approval may be vendor- or community-led.
- **Selected projects producing or consuming**:
  - **Produced by**: S-07 (OpenSpec), S-08 (Spec Kit).
  - **Consumed by**: S-09 (Claude Code, as a consumer of spec artifacts in plan-then-execute flows, per S-09 §10 adjacency).
- **Evidence**: SRC-026 (OpenSpec; Partially Verified), SRC-025 (Spec Kit; Partially Verified).

## 4. RFC

- **Purpose**: Request for Comments document capturing a proposal for community input before formalization.
- **Inputs**: proposal text.
- **Outputs**: RFC document.
- **Dependencies**: community review process.
- **Lifecycle position**: Specification / Review stages.
- **Ownership**: varies by adopting organization.
- **Selected projects producing or consuming**: **Not observed in Selected projects.** No Selected project in the reverse-research evidence records producing or consuming RFC artifacts.
- **Evidence**: No direct evidence in `research/competitors/reverse-research.md`.

## 5. ADR

- **Purpose** (per S-06 §2): capturing architectural decisions, including their context and consequences, so the reasoning behind decisions is preserved over time.
- **Inputs**: problem framing, options, tradeoffs.
- **Outputs**: an ADR file (typically Markdown; per S-06 §7; §8).
- **Dependencies**: Markdown; `docs/adr/` directory convention (commonly `NNNN-title.md`).
- **Lifecycle position**: Architecture, Documentation stages (per `lifecycle-coverage-matrix.md` S-06).
- **Ownership**: project / architect / tech lead; format is open.
- **Selected projects producing or consuming**:
  - **Produced by**: S-06 (ADR / Nygard).
  - **Consumed by**: S-07 (OpenSpec, per S-07 §10 adjacency), S-08 (Spec Kit, per S-08 §10 adjacency).
- **Evidence**: SRC-002, SRC-040 (Partially Verified; cognitect blog + adr.github.io corroboration).

## 6. Task

- **Purpose** (per S-07 §5; S-08 §5): discrete unit of work referenced inside a spec or change proposal.
- **Inputs**: spec or change proposal text.
- **Outputs**: task references / IDs.
- **Dependencies**: a parent SPEC or change proposal.
- **Lifecycle position**: Implementation stage (per `lifecycle-coverage-matrix.md`).
- **Ownership**: project / task author.
- **Selected projects producing or consuming**:
  - **Produced by**: S-07 (OpenSpec), S-08 (Spec Kit).
  - **Consumed by**: S-09 (Claude Code, via tool use).
- **Evidence**: SRC-026, SRC-025.

## 7. Checklist

- **Purpose**: enumerated verification or process steps.
- **Inputs**: process or verification criteria.
- **Outputs**: completed checklist.
- **Dependencies**: a defined process.
- **Lifecycle position**: varies (Review, Testing).
- **Ownership**: project / team.
- **Selected projects producing or consuming**: **Not observed in Selected projects as a distinct artifact type.** Sprint 2 evidence shows checklists as an APES-side artifact concept (per the repository scaffolding under `checklists/`), but no Selected project in the reverse-research evidence names a Checklist artifact as its own output.
- **Evidence**: No direct evidence in `research/competitors/reverse-research.md`.

## 8. Template

- **Purpose** (per S-07 §8; S-08 §8): pre-structured document scaffold (e.g., Markdown spec template; OST visualization template; Job Map template).
- **Inputs**: intent, structured schema.
- **Outputs**: completed template (a spec, an OST, a Job Map).
- **Dependencies**: Markdown or visualization tool.
- **Lifecycle position**: varies by artifact being templated.
- **Ownership**: project / community.
- **Selected projects producing or consuming**:
  - **Produced by**:
    - S-01 (Continuous Discovery) — assumption-test cards/templates (S-01 §8).
    - S-04 (JTBD) — Job Map (S-04 §8) and Job Story formats (S-04 §8).
    - S-07 (OpenSpec) — spec / change proposal templates (S-07 §8).
    - S-08 (Spec Kit) — spec templates (S-08 §8).
  - **Consumed by**: same projects' users (practitioners).
- **Evidence**: SRC-008 (S-01 templates), SRC-013 / SRC-038 (S-04 / S-05 templates), SRC-025 / SRC-026 (S-07 / S-08 templates).

## 9. Prompt

- **Purpose**: instruction text for an AI/LLM, often scoped to a specific tool or context.
- **Inputs**: natural-language intent.
- **Outputs**: prompt text consumed by an AI coding agent.
- **Dependencies**: an AI coding agent (Claude Code, Codex CLI, Gemini CLI, etc.).
- **Lifecycle position**: Coding / Implementation stages.
- **Ownership**: project maintainer / agent user.
- **Selected projects producing or consuming**: **Not observed in Selected projects as a distinct artifact type.** S-09 (Claude Code) consumes prompts at runtime (per S-09 §7), but the project does not define a Prompt artifact format; prompts are user-typed text.
- **Evidence**: SRC-014 (vendor self-description, Unverified).

## 10. Policy

- **Purpose**: organization-level rule applied across a project or repository.
- **Inputs**: organizational rule statement.
- **Outputs**: policy document.
- **Dependencies**: organizational authority.
- **Lifecycle position**: Governance.
- **Ownership**: organization.
- **Selected projects producing or consuming**: **Not observed in Selected projects as a distinct artifact type.** No Selected project records itself as producing a Policy artifact.
- **Evidence**: No direct evidence in `research/competitors/reverse-research.md`.

## 11. Workflow

- **Purpose** (per multiple Selected projects): defined process sequence.
- **Inputs**: inputs to the workflow.
- **Outputs**: outputs of the workflow.
- **Dependencies**: tools, artifacts, reviewers.
- **Lifecycle position**: spans multiple stages; varies by workflow.
- **Ownership**: project / community.
- **Selected projects producing or consuming**:
  - **Produced by**:
    - S-01 (Continuous Discovery) — the OST + assumption-test weekly cycle (S-01 §6).
    - S-02 (Inspired) — the Discovery → Delivery cycle (S-02 §6).
    - S-03 (Shape Up) — Shape → Bet → Build → Cool-down (S-03 §6).
    - S-04 (JTBD) — Identify job → Define dimensions → Discover unmet needs → Design (S-04 §6).
    - S-05 (ODI) — Define job → Uncover outcomes → Survey → Calculate opportunity → Prioritize (S-05 §6).
    - S-06 (ADR) — Capture context → Capture options → Capture decision → Update status (S-06 §6).
    - S-07 (OpenSpec) — Author → Propose → Review → Implement → Update (S-07 §6).
    - S-08 (Spec Kit) — Author → Propose → Review → Implement → Update (S-08 §6).
    - S-09 (Claude Code) — Read context → Plan → Execute → Report (S-09 §6).
    - S-10 (AGENTS.md) — Author → Agent reads → Agent incorporates (S-10 §6).
- **Evidence**: all 10 Selected projects (SRC-001 through SRC-045 as cited above; per reverse-research §6 for each project).

## 12. Architecture Decision

- **Purpose** (per S-06 §5): captured decision and its consequences; the **content** of an ADR is an Architecture Decision.
- **Inputs**: problem framing, options, tradeoffs.
- **Outputs**: a decision and a consequence record (inside an ADR file).
- **Dependencies**: an ADR format (see ADR above).
- **Lifecycle position**: Architecture, Documentation stages.
- **Ownership**: project / architect / tech lead.
- **Selected projects producing or consuming**:
  - **Produced by**: S-06 (ADR / Nygard).
  - **Consumed by**: same project users (architects, tech leads).
- **Evidence**: SRC-002, SRC-040.

## 13. Knowledge Base

- **Purpose**: persistent organized repository of information.
- **Inputs**: documents, decisions, learnings.
- **Outputs**: queryable knowledge.
- **Dependencies**: storage, retrieval mechanism.
- **Lifecycle position**: Knowledge Management.
- **Ownership**: organization / community.
- **Selected projects producing or consuming**: **Not observed in Selected projects as a distinct artifact type.** No Selected project records itself as a Knowledge Base, though several projects contribute knowledge artifacts (e.g., books, websites, repositories).
- **Evidence**: No direct evidence in `research/competitors/reverse-research.md` for any Selected project producing a Knowledge Base artifact.

## 14. Standard

- **Purpose**: formally codified practice (e.g., ISO/IEC/IEEE, NIST, OWASP).
- **Inputs**: standards-body process.
- **Outputs**: standard document.
- **Dependencies**: standards-body governance.
- **Lifecycle position**: Governance.
- **Ownership**: standards body.
- **Selected projects producing or consuming**: **Not produced by any of the 10 Selected projects.** Held candidates not in the final 10 include ISO/IEC/IEEE 12207, NIST SSDF, OWASP SAMM v2 — these are Standards but they are not part of the Selected 10 in Sprint 2 (see `research/competitors/candidate-projects.md` §"Held Candidates").
- **Evidence**: No Selected project row in `research/competitors/reverse-research.md` records itself as a Standard.

## 15. Command

- **Purpose**: CLI invocation or shell command.
- **Inputs**: command line text.
- **Outputs**: command execution result.
- **Dependencies**: shell, CLI tool.
- **Lifecycle position**: varies by command.
- **Ownership**: tool vendor.
- **Selected projects producing or consuming**:
  - **Produced by**:
    - S-07 (OpenSpec) — CLI commands for proposing / approving changes (S-07 §8).
    - S-08 (Spec Kit) — GitHub CLI integration (S-08 §8).
    - S-09 (Claude Code) — agentic CLI itself (S-09 §1; §5).
  - **Consumed by**: same projects' users.
- **Evidence**: SRC-026 (S-07 CLI), SRC-025 (S-08 CLI), SRC-014 (S-09 CLI).

---

## Artifact Coverage Summary Table

| Artifact Type | Selected Projects Producing | Selected Projects Consuming | Notes |
|---|---|---|---|
| AGENTS.md | open convention (S-10) | S-09, S-10 (other agents) | Verified at abstract level via EV-001; conflicting empirical evidence SRC-044 / SRC-045 preserved |
| CLAUDE.md | none observed in Selected projects | none observed in Selected projects | Vendor concept; not in Selected 10's reverse-research evidence |
| SPEC | S-07, S-08 | S-09 (via plan-then-execute) | Two adjacent projects with overlapping scope |
| RFC | none observed in Selected projects | none observed in Selected projects | No Selected project records RFC artifacts |
| ADR | S-06 | S-07, S-08 (as adjacent) | Format is open; widely emulated |
| Task | S-07, S-08 | S-09 (via tool use) | Sub-artifact of SPEC / change proposal |
| Checklist | none observed in Selected projects | none observed in Selected projects | APES-side concept; not in Selected 10 |
| Template | S-01, S-04, S-07, S-08 | their users | Several distinct template types |
| Prompt | none observed in Selected projects | S-09 (at runtime) | User-typed; no format |
| Policy | none observed in Selected projects | none observed in Selected projects | Not produced by Selected 10 |
| Workflow | all 10 (S-01 through S-10) | same projects' users | All projects define a workflow |
| Architecture Decision | S-06 | same project users | The content of an ADR |
| Knowledge Base | none observed in Selected projects | none observed in Selected projects | Not produced by Selected 10 |
| Standard | none observed in Selected projects | none observed in Selected projects | Held-candidate cluster only (ISO, NIST, OWASP) |
| Command | S-07, S-08, S-09 | same projects' users | CLI tooling across 3 of 10 |

### Counts

- **Artifact types observed in at least one Selected project**: 8 of 15 (AGENTS.md, SPEC, ADR, Task, Template, Workflow, Architecture Decision, Command).
- **Artifact types NOT observed in any Selected project**: 7 of 15 (CLAUDE.md, RFC, Checklist, Prompt, Policy, Knowledge Base, Standard).
- **Total (Project, Artifact-type) producing pairs observed**: 22 across the 10 projects × 15 artifact types = 150 cells.
  - S-01: 2 (Template, Workflow).
  - S-02: 1 (Workflow).
  - S-03: 1 (Workflow).
  - S-04: 2 (Template, Workflow).
  - S-05: 1 (Workflow).
  - S-06: 3 (ADR, Workflow, Architecture Decision).
  - S-07: 5 (SPEC, Task, Template, Workflow, Command).
  - S-08: 5 (SPEC, Task, Template, Workflow, Command).
  - S-09: 2 (Workflow, Command).
  - S-10: 2 (AGENTS.md, Workflow).

### Selected Projects Touching Each Artifact Type

| Artifact Type | # Projects Producing |
|---|---|
| Workflow | 10 |
| Template | 4 (S-01, S-04, S-07, S-08) |
| Command | 3 (S-07, S-08, S-09) |
| SPEC | 2 (S-07, S-08) |
| Task | 2 (S-07, S-08) |
| ADR | 1 (S-06) |
| Architecture Decision | 1 (S-06) |
| AGENTS.md | 1 (S-10) |

---

## Interpretation Rules

1. **An "observed" artifact type means the Selected project's reverse-research record describes producing or consuming that artifact.** It does **not** mean the artifact type is unique to that project.
2. **A "not observed" artifact type means no Selected project in the reverse-research evidence produces or consumes it.** It does **not** mean the artifact type does not exist in the broader landscape.
3. **The map is descriptive, not prescriptive.** It does not state which artifact types APES should adopt.
4. **Counts are descriptive.** A project producing 5 artifact types is not "more complete" than a project producing 1; the lifecycle coverage matrix (`lifecycle-coverage-matrix.md`) records lifecycle responsibility, not artifact diversity.

---

## Cross-References

- `research/coverage/coverage-map.md` — narrative coverage map for each Selected project.
- `research/coverage/lifecycle-coverage-matrix.md` — matrix view of lifecycle responsibility.
- `research/competitors/reverse-research.md` — 14-section source data for each project.
- `research/source-register.md` — Source IDs cited above.
- `research/research-plan.md` — Phase B definition.
- `tasks/sprint-03-coverage-map.md` — Sprint 3 task file.
