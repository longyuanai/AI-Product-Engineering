# Foundation 0.1.1 — Repository Evolution Plan Upgrade

- Status: Completed
- Sprint: Foundation 0.1.1
- Owner: APES Maintainers
- Last Updated: 2026-08-03
- Purpose: Architecture refinement sprint that strengthens `docs/repository-evolution-plan.md` into the definitive architectural document for Research OS. Foundation 0.1.1 is **not** a rewrite and **not** Foundation 0.2. It appends seven architectural refinement sections and one refinement note to section 4.

> **Scope.** Architecture refinement only. No implementation. No code. No scripts. No engines. No prompt implementation. No constitution. No standards. No workflow implementation. No directory implementation. No new research. No new sources. No modification of any research file. No change to Sprint 2 status (`In Review`). No change to Research Gate (`RESEARCH AGAIN`).

## Goal

Refine the Foundation 0.1 Repository Evolution Plan into the definitive architectural document for Research OS so that:

- **Foundation 0.2, 0.3, 0.4, 0.5, 1.0** all reference this document for architecture rather than redefining it.
- **Sprint 4 onward** (Gap Analysis, Positioning Evidence, etc.) reference this document for the layered model, the decision hierarchy, the document taxonomy, the maturity model, and the dependency graph.

The upgrade is purely additive. Existing sections (1 through 16) are preserved. One refinement note is appended to section 4 to clarify the relationship between the 4-layer deployment view and the 6-layer architectural view.

## Inputs

- `docs/repository-evolution-plan.md` (Foundation 0.1 version, 409 lines, 16 sections).
- `README.md` — Foundation section appended in Foundation 0.1.
- `CHANGELOG.md` — Foundation 0.1 entry appended at top of `[Unreleased]`.
- `tasks/foundation-0-1-repository-evolution.md` — Foundation 0.1 task file.
- `MANIFESTO.md` — five philosophical principles.
- `AGENTS.md` — Rule 11 (documentation-first).
- `governance/adr/ADR-0001-project-positioning.md` — deferred tooling scope.
- Sprint 0 through Sprint 3.1 deliverables and the Research Gate (`RESEARCH AGAIN`).

Foundation 0.1.1 does not modify any of these inputs except `docs/repository-evolution-plan.md`, `README.md`, and `CHANGELOG.md`.

## Architecture Refinements

Seven sections appended to `docs/repository-evolution-plan.md` (sections 17 through 23), plus one refinement note in section 4. Existing sections 1 through 16 are preserved verbatim.

### Section 17 — Repository Evolution Principles (10 principles)

The philosophical foundation of Research OS. Each principle is explained. Principles are listed in order of architectural precedence; higher-numbered principles do not override lower-numbered ones.

1. **Backward Compatibility First.** New architectures and schemas preserve the contract of every layer below.
2. **Research before Design.** No standard, schema, engine, prompt, workflow, or template is written before the underlying evidence is registered and verified.
3. **Evidence before Opinion.** Every non-trivial claim references a Source ID; absent evidence is `Unknown`, not inferred.
4. **Audit before Release.** A snapshot is not released until it has been audited against its evidence trail.
5. **Architecture before Implementation.** No code, script, engine, prompt, workflow, or standard is implemented until the architectural layer that contains it is documented and accepted.
6. **Shared before Project-specific.** Reusable components are moved to a shared layer before being duplicated.
7. **Everything Versioned.** Every shared component, every project-specific artifact, and every Foundation sprint produces a Semantic Version.
8. **Everything Traceable.** Every claim, decision, audit finding, and verification has a reference back to its source.
9. **Everything Reproducible.** Audits, statistics, coverage maps, and reports must be reconstructible from the evidence trail.
10. **No Hidden Decisions.** Every non-trivial decision is recorded in an ADR, RFC, Foundation-RFC, or Decision Note before it takes effect.

### Section 18 — Repository Layer Model (6 layers)

Refined layer model. The 4-layer view in §4 (Research OS → Standard Foundation → Project Layer → Release Layer) is preserved as a *deployment* view. The 6-layer view below is the *architectural* view.

```
Meta Layer
    ↓
Foundation Layer
    ↓
Engine Layer
    ↓
Research Layer
    ↓
Project Layer
    ↓
Release Layer
```

Each layer's responsibility is described. Strict downward dependency: Meta depends on nothing; Foundation depends only on Meta; Engine depends on Meta + Foundation; Research depends on Meta + Foundation + Engine; Project depends on Meta + Foundation + Engine + Research; Release depends on Project.

### Section 19 — Repository Lifecycle (9 stages)

The lifecycle of *the repository itself*, not of any product or standard hosted by it.

```
Idea → Research → Audit → Architecture → Implementation
      → Validation → Release → Maintenance → Archive
```

Each stage's responsibility is described. Transition rules: forward only; reverse transitions require a Decision Hierarchy artifact; archive is irreversible.

### Section 20 — Decision Hierarchy

A 10-tier hierarchy showing authority.

```
Principles
    ↓
Constitution
    ↓
RFC
    ↓
Standard
    ↓
Schema
    ↓
Engine
    ↓
Workflow
    ↓
Prompt
    ↓
Project
    ↓
Sprint
```

Each tier's responsibility is described. Conflict resolution: a lower tier cannot override a higher tier; within a tier, `Accepted` > `Proposed` > `Draft`; cross-tier conflicts are resolved via RFC.

### Section 21 — Document Taxonomy (15 types)

Every artifact belongs to exactly one of 15 document types: Policy, Constitution, RFC, ADR, Research, Coverage, Gap Analysis, Evidence, Statistics, Report, Task, Prompt, Checklist, Template, Release Notes. Each type is described by Purpose, Owner, Lifecycle, and Version policy.

### Section 22 — Repository Maturity Model (6 levels)

```
Level 0 — Bootstrap
    ↓
Level 1 — Research
    ↓
Level 2 — Standardization
    ↓
Level 3 — Automation
    ↓
Level 4 — Platform
    ↓
Level 5 — Research OS
```

Current state is Level 1 (post Sprint 3.1). Current target is Level 2 (post Foundation 0.1.1). Each level's expected characteristics are described.

### Section 23 — Repository Dependency Graph

A canonical direction graph showing what may reference what.

```
Principles
    ↓
Constitution
    ↓
Schemas
    ↓
Engines
    ↓
Workflows
    ↓
Prompts
    ↓
Research
    ↓
Coverage
    ↓
Gap
    ↓
Release
```

The dependency graph and the Decision Hierarchy are dual views: the hierarchy is *who decides*; the dependency graph is *what depends on what*.

### Section 4 Refinement Note

A 5-line refinement note was appended to section 4 to clarify the relationship between the 4-layer deployment view and the 6-layer architectural view. The 4-layer view is preserved; the note documents that §18 is the canonical reference for future sprints.

## Outputs

| # | Deliverable | Action | Status |
|---|---|---|---|
| 1 | `docs/repository-evolution-plan.md` — refined with 7 new sections + 1 section-4 note | Modified | Completed |
| 2 | `tasks/foundation-0-1-1-repository-evolution-upgrade.md` (this file) | Created | Completed |
| 3 | `README.md` — Foundation 0.1.1 section appended | Modified | Completed |
| 4 | `CHANGELOG.md` — Foundation 0.1.1 entry appended | Modified | Completed |

Foundation 0.1.1 produces **no other files**.

## Out of Scope

Explicitly forbidden in this sprint and **not** attempted:

- **No Gap Analysis** (Phase C).
- **No Feature Matrix.**
- **No Lifecycle Gap claim.**
- **No Market Positioning.**
- **No Competitive Positioning.**
- **No SWOT.**
- **No Roadmap.**
- **No Recommendations.**
- **No Vision.**
- **No Priorities.**
- **No Implementation Plan.**
- **No APES Design.**
- **No APES Architecture** (separate from the Repository Evolution Plan).
- **No Standard Modules.**
- **No Prompt Library.**
- **No Commands, Templates, or Checklists (new APES ones).**
- **No Plugin Design, CLI, MCP, Website.**
- **No Business Strategy.**
- **No Brand Strategy.**
- **No statement that APES is missing something.**
- **No implementation.** No code. No scripts. No engines. No prompt implementation. No constitution. No standards. No workflow implementation. No directory implementation.
- **No new research.** No new sources. No WebSearch. No WebFetch.
- **No modification of any research file.**
- **No modification of any research conclusion.**
- **No modification of Sprint 2 status** (remains `In Review`).
- **No modification of Research Gate** (remains `RESEARCH AGAIN`).
- **No removal of any existing section from `docs/repository-evolution-plan.md`.** Sections 1 through 16 are preserved verbatim.
- **No modification of any file outside the allowed list** (`docs/repository-evolution-plan.md`, `tasks/foundation-0-1-1-repository-evolution-upgrade.md`, `README.md`, `CHANGELOG.md`).
- **No git commit, push, tag, or branch creation.**
- **No beginning of Foundation 0.2.** Foundation 0.2 is a separate, future sprint.

## Acceptance Criteria

- `docs/repository-evolution-plan.md` exists and contains, in addition to the 16 Foundation 0.1 sections, the following 7 sections appended after section 16: Repository Evolution Principles, Repository Layer Model, Repository Lifecycle, Decision Hierarchy, Document Taxonomy, Repository Maturity Model, Repository Dependency Graph.
- Sections 1 through 16 are preserved verbatim. Section 4 has one appended refinement note; no other modifications.
- `tasks/foundation-0-1-1-repository-evolution-upgrade.md` exists and contains Goal, Inputs, Architecture Refinements, Out of Scope, Acceptance Criteria, Verification, Remaining Questions, Status, Cross References.
- `README.md` has an additive Foundation 0.1.1 section appended after the Foundation 0.1 section; existing content is preserved verbatim.
- `CHANGELOG.md` has a Foundation 0.1.1 entry at the top of `[Unreleased]` (above the Foundation 0.1 entry); existing entries are preserved verbatim.
- No Gap Analysis, Feature Matrix, Lifecycle Gap claim, Market Positioning, Competitive Positioning, SWOT, Roadmap, Recommendations, Vision, Priorities, Implementation Plan, APES Design, APES Architecture, Standard Modules, Prompt Library, new APES Commands/Templates/Checklists, Plugin Design, CLI, MCP, Website, Business Strategy, Brand Strategy, or statement that APES is missing something appears in any Foundation 0.1.1 deliverable.
- No implementation, code, scripts, engines, prompt implementation, constitution, standards, workflow implementation, or directory implementation appears in any Foundation 0.1.1 deliverable.
- No research file is modified. No research conclusion is modified. Sprint 2 status remains `In Review`; Research Gate remains `RESEARCH AGAIN`.
- No new WebSearch or WebFetch was performed.
- No file outside the allowed list was modified.
- No git commit, push, tag, or branch creation was performed.

## Verification

- File-existence check for the four deliverables.
- Section-coverage check: `docs/repository-evolution-plan.md` contains all 7 new sections named in the brief (Repository Evolution Principles, Layer Model, Lifecycle Model, Decision Hierarchy, Document Taxonomy, Repository Maturity Model, Dependency Graph), plus the section-4 refinement note.
- Preservation check: sections 1 through 16 of `docs/repository-evolution-plan.md` are byte-identical to the Foundation 0.1 version (except for the section-4 refinement note, which is appended without removing prior text).
- Allowed-files check: only `docs/repository-evolution-plan.md`, `tasks/foundation-0-1-1-repository-evolution-upgrade.md`, `README.md`, and `CHANGELOG.md` were created or modified by Foundation 0.1.1.
- Sprint 2 status preserved at `In Review`; Research Gate preserved at `RESEARCH AGAIN`.
- No git operations performed (no commit, push, tag, or branch).
- Working tree left in uncommitted but reviewable state.

## Remaining Questions

- **RQ-1.** Should the Constitution tier (§20) be promoted from "reserved slot" to a written document in Foundation 0.2? Currently `OQ-N`. Foundation 0.2 candidate.
- **RQ-2.** Is the 6-layer architectural model (Meta → Foundation → Engine → Research → Project → Release) correctly aligned with the 4-layer deployment model (Research OS → Standard Foundation → Project Layer → Release Layer)? The mapping in §18 collapses Meta + Foundation → Standard Foundation, Engine + Research → Research OS. Future sprints may refine.
- **RQ-3.** Should the Maturity Model (§22) add a "Level -1: Pre-bootstrap" tier for repositories that do not yet have identity documents? Currently `OQ-N`.
- **RQ-4.** Should the Document Taxonomy (§21) split `Research` into `Research Plan`, `Research Report`, and `Research Note`? Currently `OQ-N`.
- **RQ-5.** Should the Decision Hierarchy (§20) insert `Policy` between `Constitution` and `RFC`? Currently `OQ-N`.
- **RQ-6.** Does the Engine Layer (§18) require a dedicated ADR for each Engine before the Engine can be implemented? Future Foundation sprint.
- **RQ-7.** Does the Repository Lifecycle (§19) need a `Decommission` stage distinct from `Archive`? Currently `OQ-N`.
- **RQ-8.** Should the Dependency Graph (§23) be encoded as a machine-readable file (e.g., a YAML graph) in addition to the diagram? Currently `OQ-N`.

## Status

**Completed** for the items listed in [Outputs](#outputs) above. Foundation 0.1.1 produced one refined architecture document (`docs/repository-evolution-plan.md`), this task file, and additive updates to `README.md` and `CHANGELOG.md`. Sprint 2 remains `In Review`; Research Gate remains `RESEARCH AGAIN`. Foundation 0.2 is a separate, future sprint; Foundation 0.1.1 explicitly does not begin it.

## Cross References

- `docs/repository-evolution-plan.md` — architecture plan, refined in this sprint.
- `README.md` — Foundation 0.1 + Foundation 0.1.1 sections appended.
- `CHANGELOG.md` — Foundation 0.1.1 entry at top of `[Unreleased]`.
- `tasks/foundation-0-1-repository-evolution.md` — Foundation 0.1 task file (parent).
- `design/01-repository-architecture.md` — v0.1 architectural decision; superseded by the 6-layer model in §18 for future Foundation sprints.
- `governance/README.md` — governance framework; will be refined to add the `Constitution` tier in a future Foundation sprint.
- `governance/adr/ADR-0001-project-positioning.md` — project positioning; reaffirmed by Foundation 0.1.1 (deferred tooling scope).
- `MANIFESTO.md` — five philosophical principles; distinct from the ten architectural principles in §17 but consistent with them.
- `AGENTS.md` — Rule 11 reaffirmed by Foundation 0.1.1 (documentation-first).
- `research/research-plan.md` — referenced but not modified; methodology preserved.
- `research/source-register.md` — referenced but not modified; 52 Source IDs preserved.
- `CHANGELOG.md` — Sprint 0 through Foundation 0.1 entries preserved; Foundation 0.1.1 entry appended at top of `[Unreleased]`.
