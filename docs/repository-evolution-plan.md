# Repository Evolution Plan

- Status: Draft
- Version: v0.4.2
- Owner: APES Maintainers
- Last Updated: 2026-08-10
- Purpose: Define the long-term evolution path, reference architecture, and staged implementation strategy of the AI-Product-Engineering repository (and the family of research repositories that may inherit its standards). This document does **not** implement any component.

> **Scope.** Foundation 0.1 architecture sprint, refined by Foundation 0.1.1 (architecture refinement sprint). No research modifications. No engine or prompt design. No directory implementation. No constitution. No standard. No workflow. This document is a planning artifact, not a release.

> **Foundation 0.1.1 refinement.** Seven architectural sections were appended (sections 17–23) without removing any prior content. The layer model was refined to six layers (Meta → Foundation → Engine → Research → Project → Release). Decision hierarchy, document taxonomy, lifecycle model, maturity model, and dependency graph were added. The philosophical foundation (ten Repository Evolution Principles) is now codified in section 17.

> **Foundation 0.2 reference design.** Sections 24–28 add an evidence-backed comparison of four adjacent open-source projects and a documentation-only implementation proposal. No CLI, engine, schema file, workflow, adapter, website, build pipeline, or application source code was created in Foundation 0.2. That Sprint ended with ADR-0002 `Proposed`; Foundation 0.3 later accepted it through a separately approved Sprint.

> **Foundation 0.3 implementation note.** On 2026-08-07 the maintainer accepted ADR-0002 and approved F1 Contract Prototype. F1 adds one JSON Schema contract, representative parsed-metadata fixtures, and a compatibility mapping. Existing Markdown remains canonical and unmoved; it supplied the contract gate later consumed by F2.

> **F2 implementation note.** On 2026-08-09 the maintainer directed continuation of this technical plan. F2 now exists in the independent `APES-Validator` Git repository with `check`, `graph`, and `explain` commands. The first independent review requested changes; commit `73bbe6e` and Schema v0.2.0 respond to all thirteen findings, and implementer follow-up `9d58a9f` adds resource-complexity and pre-resolution path hardening. F2 remains `In Review` pending independent re-review and is not released.

## Table of Contents

- [1. Vision](#1-vision)
- [2. Current Repository State](#2-current-repository-state)
- [3. Problems of Current Structure](#3-problems-of-current-structure)
- [4. Future Repository Layers](#4-future-repository-layers)
- [5. Repository Responsibilities](#5-repository-responsibilities)
- [6. Shared Components](#6-shared-components)
- [7. Project-Specific Components](#7-project-specific-components)
- [8. Migration Strategy](#8-migration-strategy)
- [9. Directory Evolution](#9-directory-evolution)
- [10. Future Projects](#10-future-projects)
- [11. Version Strategy](#11-version-strategy)
- [12. Governance Strategy](#12-governance-strategy)
- [13. Compatibility Rules](#13-compatibility-rules)
- [14. Risk Assessment](#14-risk-assessment)
- [15. Open Questions](#15-open-questions)
- [16. Cross-References](#16-cross-references)
- [17. Repository Evolution Principles](#17-repository-evolution-principles)
- [18. Repository Layer Model](#18-repository-layer-model)
- [19. Repository Lifecycle](#19-repository-lifecycle)
- [20. Decision Hierarchy](#20-decision-hierarchy)
- [21. Document Taxonomy](#21-document-taxonomy)
- [22. Repository Maturity Model](#22-repository-maturity-model)
- [23. Repository Dependency Graph](#23-repository-dependency-graph)
- [24. Open-Source Reference Comparison](#24-open-source-reference-comparison)
- [25. APES Target Implementation Architecture](#25-apes-target-implementation-architecture)
- [26. Recommended Technical Stack](#26-recommended-technical-stack)
- [27. Staged Implementation Plan](#27-staged-implementation-plan)
- [28. Guardrails, Risks, and Decision Status](#28-guardrails-risks-and-decision-status)

## 1. Vision

The repository will evolve from a single-purpose standard (APES) into a **family of research-driven, evidence-anchored repositories** that share a common operating layer — a "research OS" — and a common standards layer — a "standard foundation" — while remaining project-specific in their content.

The long-term direction:

- **Today.** A single repository holding one standard (APES), one research effort, and one set of supporting artifacts.
- **Tomorrow.** A modular family in which each project (APES, AI Security, IoT Security, Binary Security, Research Library, etc.) carries its own domain content but inherits the shared operating layer, the shared audit posture, and the shared evidence schema.
- **Why.** A new domain (AI Security, IoT Security, Binary Security) should not need to re-design the repository, the governance process, the evidence trail, or the version cadence. It should inherit them.

The vision is **operating system, not single project**: design once, inherit everywhere.

## 2. Current Repository State

The repository exists today as the canonical home of APES. Its character is established by the v0.1 deliverables (Sprint 0 through Sprint 3.1):

- **Sprint 0** — Repository foundation: 15 visible top-level directories plus `.github/`, root identity documents (`README.md`, `VISION.md`, `MANIFESTO.md`, `ROADMAP.md`, `CONTRIBUTING.md`, `CODE_OF_CONDUCT.md`, `AGENTS.md`, `CHANGELOG.md`, `LICENSE`), and design/governance scaffolding.
- **Sprint 1** — Ecosystem research plan (`research/research-plan.md`).
- **Sprint 2** — Source register (52 sources), search log, ecosystem inventory, candidate projects, reverse-research records.
- **Sprint 2.1** — Evidence correction (three orthogonal fields per source row).
- **Sprint 2.2** — Verification attempt (22 attempts, all Inaccessible; Research Gate `RESEARCH AGAIN`).
- **Sprint 2.3** — External Verification Reconciliation (6 sources upgraded to `Verified`).
- **Sprint 3** — Coverage Map (10×19 lifecycle matrix, 15-artifact-type map, narrative coverage for S-01 through S-10).
- **Sprint 3.1** — Coverage Audit (8 audit tasks, 11 findings applied).
- **Foundation 0.1 / 0.1.1** — Repository Evolution Plan and its six-layer architectural refinement.
- **Foundation 0.2 / 0.3** — Four-project open-source reference comparison, accepted schema-first architecture, and the F1 contract prototype; ADR-0002 is `Accepted`.

Current structural facts:

- 16 visible top-level directories plus `.github/`; the Foundation 0.3 `schemas/` contract registry is the only addition to the 15-directory Foundation baseline.
- Research evidence trail in `research/` is preserved verbatim: Sprint 2 status `In Review`; Research Gate `RESEARCH AGAIN`.
- `standards/` is structurally complete but substantively empty (placeholders only, per `docs/01` "Known Limitations").
- `governance/` contains three Accepted ADRs (ADR-0001 through ADR-0003), the initial F2 review record, and the remediation evidence; RFCs remain placeholders.
- This canonical repository contains no CLI, MCP server, IDE extension, or built website. The separately governed sibling repository `APES-Validator` contains the approved F2 read-only CLI under ADR-0003.
- License selection is pending maintainer decision.

## 3. Problems of Current Structure

The v0.1 structure is correct for one project. It does not yet support reuse, multi-project families, or long-term composition.

Identified problems:

1. **No shared operating layer.** Every directory currently serves APES specifically. There is no separation between "what is generic to any research repository" and "what is APES-specific content."
2. **No abstraction for the research pipeline.** `research/research-plan.md`, `source-register.md`, `verification-log.md`, `coverage/`, and `gap-analysis/` are scattered across one research effort. A new project will need to replicate this pattern by hand.
3. **No clear seam between policy (shared) and content (project-specific).** `MANIFESTO.md`, `CONTRIBUTING.md`, `AGENTS.md` are written in APES voice. A future project that wants the same evidence discipline will not be able to inherit them as-is.
4. **Standards modules are tied to one lifecycle.** The APES 9-stage lifecycle (`README.md` §Lifecycle Overview) is encoded throughout `standards/`. A future project (e.g., IoT Security) with a different lifecycle will not be able to reuse the structure without modification.
5. **Governance is APES-shaped.** ADR-0001 commits APES-specific decisions (project name, standard name, scope). A new project would need a parallel ADR-0001.
6. **No explicit version-of-repository contract.** Versions are tracked per file, but there is no documented rule for what "v0.2 of the repository" means versus "v0.2 of a standard module."
7. **No defined migration policy.** When a future project reuses or forks the structure, the rules for what can change and what must remain stable are not written down.
8. **Audit and evidence engines are implicit.** Sprint 3.1 ran an audit by hand. The rules and schemas exist (`source-register.md`, the lifecycle matrix), but there is no named, reusable audit component.
9. **No explicit compatibility boundary.** Future contributors cannot tell which changes will break older consumers (case studies, external mirrors, tooling) and which will not.

These problems do not invalidate v0.1. They define what Foundation 0.1 must answer before the next family member begins.

## 4. Future Repository Layers

The target shape is a layered repository. Each layer has a single responsibility and a single dependency direction: higher layers depend on lower layers; lower layers know nothing about higher layers.

> **Foundation 0.1.1 refinement.** The 4-layer view below (Research OS → Standard Foundation → Project Layer → Release Layer) is preserved as a *deployment* view. The 6-layer architectural view in §18 (Meta → Foundation → Engine → Research → Project → Release) refines this by adding the Meta Layer and the Engine Layer as explicit positions, separating philosophical and architectural rules from generic engines and from generic research artifacts. The 6-layer view is the canonical reference for future Foundation sprints.

```
┌─────────────────────────────────────────────────────────────────┐
│                        Release Layer                            │
│   (Tagged snapshots, public bundles, website output)            │
│   depends on: Project Layer                                     │
└─────────────────────────────────────────────────────────────────┘
                                │
┌─────────────────────────────────────────────────────────────────┐
│                       Project Layer                             │
│   (APES, AI Security, IoT Security, Binary Security, etc.)      │
│   depends on: Standard Foundation, Research OS                  │
└─────────────────────────────────────────────────────────────────┘
                                │
┌─────────────────────────────────────────────────────────────────┐
│                  Standard Foundation Layer                      │
│   (Lifecycle model, manifesto, evidence policy, governance      │
│    framework, compatibility contract)                           │
│   depends on: Research OS                                       │
└─────────────────────────────────────────────────────────────────┘
                                │
┌─────────────────────────────────────────────────────────────────┐
│                       Research OS Layer                         │
│   (Source register, search log, verification log, coverage,      │
│    gap analysis, audit, statistics, reports — generic)          │
│   depends on: (nothing)                                         │
└─────────────────────────────────────────────────────────────────┘
```

Layer responsibilities:

- **Research OS.** Generic research operating system. Defines schemas, audit posture, evidence trails, and reporting — without binding to any particular subject. Any project can run a Research OS sprint (Inventory → Coverage Map → Gap Analysis → Positioning Evidence) using the OS's schemas.
- **Standard Foundation.** Cross-project commitments: lifecycle model, evidence policy, governance framework, compatibility contract. Every project in the family inherits these.
- **Project Layer.** Each project's domain content. APES is the first instance. Future projects reuse the Research OS and Standard Foundation but carry their own modules, examples, and case studies.
- **Release Layer.** Tagged snapshots and public bundles. This layer is what external consumers see.

The dependency direction is strictly downward. The Research OS has no knowledge of any project. The Standard Foundation has no knowledge of any specific lifecycle stage. The Project Layer inherits both and adds content. The Release Layer freezes a Project Layer's state for external consumption.

## 5. Repository Responsibilities

What this repository is responsible for:

- Holding the canonical Research OS (schemas, audit rules, evidence policy).
- Holding the canonical Standard Foundation (lifecycle model, manifesto, governance framework).
- Holding the first Project Layer instance (APES).
- Producing reviewable snapshots (Release Layer).

What this repository is **not** responsible for:

- It is not responsible for tools (CLI, MCP server, IDE extension, website). ADR-0001 deferred these; Foundation 0.1 reaffirms the deferral.
- It is not responsible for hosting other projects' content. Future projects (AI Security, IoT Security, Binary Security) will live in their own repositories and inherit the OS + Foundation via a versioning contract.
- It is not responsible for academic citation. Sprint 2 evidence trail already notes that academic references and ISBN / DOI handling belong to a future, separately-scoped repository (per `research/research-plan.md` §13).
- It is not responsible for collecting adoption metrics or vendor comparisons. Per ADR-0001, vendor neutrality is preserved by keeping these out of scope.
- It is not responsible for runtime distribution. The Release Layer produces markdown bundles, not compiled artifacts.

The boundary is "research-driven, evidence-anchored, documentation-first standards families." Everything inside that boundary is fair game for Foundation 0.1; everything outside is a future, separately-scoped project.

## 6. Shared Components

The shared components live in the **Standard Foundation** and the **Research OS**. They are project-agnostic by construction.

Standard Foundation components:

- **Manifesto.** The five principles (Product Before Code, Evidence Over Opinion, Validation Before Implementation, Reuse Before Reinvent, Iteration Over Perfection). Inherited by every project. Versioned as a separate component because principles change slowly.
- **Evidence Policy.** Rules for what counts as evidence, how sources are registered, how claims are verified, and how audits run. Currently distributed across `AGENTS.md`, `CONTRIBUTING.md`, and `research/source-register.md`; Foundation 0.1 plans (in future sprints) to consolidate these into a single named policy.
- **Lifecycle Model.** The 9-stage lifecycle (`README.md` §Lifecycle Overview) plus the broader 19-stage Sprint 3 research set. Inherited by every project that runs research.
- **Governance Framework.** ADR / RFC / Decision Note rules (`governance/README.md`). Inherited as-is.
- **Compatibility Contract.** Rules for what may change without notice and what must follow a deprecation path. Documented in Foundation 0.1 (this plan).

Research OS components:

- **Source Register.** 15-field schema per `research/research-plan.md` §4.6 / Appendix A. Generic. Used by any project's research pipeline.
- **Search Log.** 9-field schema per `research/research-plan.md` Appendix D. Generic.
- **Verification Log.** 11-field verification schema (Sprint 2.2) + 8-field External Verification Reconciliation schema (Sprint 2.3). Generic.
- **Coverage Map.** Matrix schema (Sprint 3). Generic. Reusable for any project that maps standards against its own lifecycle.
- **Artifact Map.** Artifact-type × project map (Sprint 3). Generic.
- **Audit Engine.** Audit-task structure (Sprint 3.1). Generic. Eight tasks in that audit (cell triples, Unknown vs None, artifact fields, traceability, confidence, consistency, statistics, cross-references) form a reusable audit template.
- **Statistics Reporter.** Aggregate counts across Coverage / Audit / Gap analyses. Generic.
- **Report Engine.** Per-phase report format. Generic.

Naming conventions for shared components are reserved words: `Manifesto`, `Evidence Policy`, `Lifecycle Model`, `Source Register`, `Coverage Map`, `Audit`, `Statistics`, `Report`. Projects that introduce a new shared component must do so via a Foundation-RFC (a new document type introduced in §12).

## 7. Project-Specific Components

Project-specific components live in the **Project Layer**. They depend on the Standard Foundation and the Research OS but carry project content.

Project-specific component types:

- **Lifecycle Modules.** For APES: `standards/discovery/`, `standards/research/`, etc. For a future IoT Security project: `standards/device-firmware/`, `standards/physical-access/`, etc. Inherited structure, project-specific content.
- **Templates.** `templates/` — APES uses one set; future projects may add project-specific templates but the schema follows Standard Foundation.
- **Commands.** `commands/` — APES-specific instructions. Future projects inherit the schema but not the contents.
- **Checklists.** `checklists/` — APES-specific quality gates. Future projects inherit the schema.
- **Research Content.** `research/competitors/`, `research/papers/`, `research/ecosystem/` — APES competitors are APES-specific; IoT Security will have its own competitors. The Research OS schemas are shared; the rows are project-specific.
- **Coverage Map Data.** `research/coverage/` — APES projects (S-01 through S-10). Future projects populate their own coverage maps using the same schema.
- **Gap Analysis Data.** `research/gap-analysis/` (post Sprint 4) — APES-specific gap conclusions, derived from the shared OS + APES-specific coverage map.
- **Worked Examples.** `examples/` — APES-specific case studies. Future projects carry their own.
- **ADRs and RFCs.** Each project's governance directory carries its own decision records. ADRs that affect the shared layers (Standard Foundation, Research OS) live in the Foundation ADR index (see §12).

The strict rule: a project-specific component **never** modifies a shared component. If a project needs to change a shared rule, it must go through a Foundation-RFC.

## 8. Migration Strategy

The migration from v0.1 to the target layered shape follows a controlled, evidence-driven path. It does not happen in a single sprint.

Migration phases:

> **Roadmap reconciliation (2026-08-07).** The actual Foundation 0.2 sprint delivered the open-source reference architecture in sections 24–28, not the boundary-separation work originally sketched below. The actual Foundation 0.3 sprint then executed F1 Contract Prototype, not the `research-os/` directory proposal. The original labels below are retained as historical planning context; boundary separation, a named Research OS directory, and later migration steps remain unassigned until maintainers approve new scoped tasks.

1. **Foundation 0.1 (this document).** Establish the layered model in writing. No directory changes yet. No code.
2. **Foundation 0.2 (future).** Identify the boundary between Standard Foundation content and APES-specific content. Likely candidates to move into Standard Foundation: `MANIFESTO.md`, `CONTRIBUTING.md`, `AGENTS.md`, `governance/` framework rules. Likely candidates to remain APES-specific: lifecycle stage modules in `standards/`.
3. **Foundation 0.3 (historical proposal; not executed).** Introduce the Research OS as a formally-named subdirectory (`research-os/` or equivalent) without moving existing files. The actual Foundation 0.3 scope was reassigned to F1 Contract Prototype.
4. **Foundation 0.4 (future).** Begin moving research files into the Research OS subdirectory under semantic versioning rules. Each move is paired with an ADR (Foundation-ADR).
5. **Foundation 0.5 (future).** First family-member repository (e.g., AI Security) forks or re-uses the Research OS + Standard Foundation. Compatibility contract validated end-to-end.
6. **Foundation 1.0 (future).** Research OS and Standard Foundation reach v1.0. APES remains at its own v0.x until its own validation is complete.

Compatibility during migration:

- During Foundation 0.2–0.4, no file moves or renames are visible to external readers. The directory shape remains the v0.1 contract.
- During Foundation 0.5, the first family member is a **read-only consumer** of the OS + Foundation. It does not modify the source repository.
- Files moved into the Research OS during Foundation 0.4 retain their original paths as compatibility symlinks or aliases for one major version, then are deprecated in the next.

Deprecation rules:

- A deprecated file is moved to `archive/<version>/` with a `DEPRECATED.md` pointer.
- Deprecated files remain readable for one major version after deprecation.
- A deprecation is recorded in `CHANGELOG.md` and, if it affects external readers, in a Foundation-RFC.

Versioning rules:

- The repository follows Semantic Versioning (`MAJOR.MINOR.PATCH`).
- `MAJOR` increments signal a breaking change to the directory shape or the Standard Foundation contract.
- `MINOR` increments signal new shared components or new layers without breaking existing ones.
- `PATCH` increments signal corrections, documentation fixes, and link repairs.

## 9. Directory Evolution

Foundation 0.1 does not move any directory. Future Foundation sprints may. The evolution map below documents the target shape; it is a contract for future sprints, not a current change.

Current directory → target layer assignment:

| Current path | Target layer | Notes |
| --- | --- | --- |
| `README.md`, `VISION.md`, `MANIFESTO.md`, `ROADMAP.md`, `CONTRIBUTING.md`, `CODE_OF_CONDUCT.md`, `AGENTS.md`, `CHANGELOG.md`, `LICENSE` | Project Layer (APES-specific identity) + Standard Foundation candidates | Some root docs are APES-specific (project name); others (`MANIFESTO.md`, `AGENTS.md`) are candidates for the Standard Foundation in Foundation 0.2. |
| `docs/` | Project Layer | APES-specific documentation. Future projects carry their own. |
| `standards/` | Project Layer (APES-specific modules) | APES 9-stage modules. Future projects carry their own. |
| `protocols/` | Project Layer | APES-specific protocols. |
| `templates/`, `commands/`, `checklists/` | Project Layer | APES-specific schemas follow Standard Foundation; contents are APES-specific. |
| `research/research-plan.md`, `research/README.md` | Standard Foundation candidates | Methodology and policies are generic. Foundation 0.2 may promote these. |
| `research/source-register.md`, `research/notes/search-log.md`, `research/notes/verification-log.md` | Research OS candidates | Generic research schemas. |
| `research/ecosystem/inventory.md`, `research/competitors/`, `research/coverage/`, `research/gap-analysis/` (post Sprint 4) | Project Layer | APES-specific rows. |
| `research/competitors/candidate-projects.md`, `research/competitors/reverse-research.md` | Project Layer | APES-specific candidates and reverse-research records. |
| `research/papers/` | Project Layer | APES-specific paper notes. |
| `examples/` | Project Layer | APES-specific worked examples. |
| `governance/adr/`, `governance/rfc/`, `governance/decisions/` | Standard Foundation (framework rules) + Project Layer (APES-specific decisions) | The framework rules (`governance/README.md`) belong in the Standard Foundation; the actual ADR/RFC records are project-specific. Foundation 0.2 may split these. |
| `design/` | Standard Foundation candidates | Design documents that describe the OS or the Foundation are generic; project-specific design docs are not. |
| `tasks/` | Project Layer | Sprints are project-specific. Future projects carry their own. |
| `sessions/` | Project Layer | Session logs are project-specific. |
| `assets/` | Project Layer | APES-specific diagrams and media. |
| `scripts/` | Project Layer | APES-specific repository maintenance scripts. |
| `website/` | Release Layer (deferred) | Implementation deferred per ADR-0001 and `AGENTS.md` Scope Boundaries. |
| `.github/` | Project Layer | APES-specific GitHub templates and workflows. |

Why these assignments matter:

- Promoting `MANIFESTO.md`, `AGENTS.md`, `CONTRIBUTING.md`, and the governance framework rules to the Standard Foundation means a future project (IoT Security) can inherit the same evidence discipline without rewriting them.
- Promoting `research/research-plan.md`, `research/README.md`, and the research schemas to the Research OS means a future project's research pipeline follows the same audit and verification cadence.
- Keeping `standards/`, `examples/`, and `commands/` in the Project Layer means APES-specific content stays APES-specific.
- The Release Layer is currently implicit (tagged git commits). Foundation 0.x future sprints may add an explicit `release/` or `dist/` directory, but Foundation 0.1 does not.

## 10. Future Projects

The family may eventually include projects beyond APES. Foundation 0.1 names the candidates the maintainers have considered, without committing to any of them.

Candidates (descriptive, not prescriptive):

- **AI Security.** An evidence-driven standard for AI-specific security practice (prompt injection defense, model supply chain, agent runtime safety). Likely reuses the Research OS for ecosystem coverage of AI red-team tooling.
- **IoT Security.** A standard for connected-device security lifecycle (device identity, firmware integrity, over-the-air update governance). Likely reuses the Research OS for ecosystem coverage of IoT platform vendors and standards bodies.
- **Binary Security.** A standard for binary analysis, reverse engineering, and exploit development practice. Likely reuses the Research OS for ecosystem coverage of academic and tooling landscape.
- **Research Library.** A documentation-only repository that aggregates APES-family research without itself being a standard. Could function as the canonical Research OS host.

Future projects inherit:

- The Research OS (schemas, audit posture, evidence trail).
- The Standard Foundation (manifesto, governance framework, compatibility contract).
- The release cadence and version strategy.

Future projects **do not** inherit:

- APES-specific lifecycle modules (`standards/` content).
- APES-specific competitors or reverse-research.
- APES-specific examples or case studies.

Each future project requires its own ADR-0001-equivalent: a project-positioning ADR that names its standard, scope, and out-of-scope. This rule prevents silent reuse that would otherwise create implicit vendor capture.

## 11. Version Strategy

The repository follows Semantic Versioning (`MAJOR.MINOR.PATCH`) at three levels, kept distinct:

- **Repository version** — `MAJOR.MINOR.PATCH` for the repository as a whole.
- **Standard version** — `MAJOR.MINOR.PATCH` for the standard itself (APES today; future projects get their own).
- **Research OS version** — `MAJOR.MINOR.PATCH` for the Research OS component alone.

Version rules:

- **MAJOR** increments on a breaking change to the directory shape, the Standard Foundation contract, or the Research OS schema.
- **MINOR** increments on a backward-compatible addition (new shared component, new lifecycle module, new artifact type).
- **PATCH** increments on corrections, documentation fixes, link repairs, and non-semantic edits.

Examples:

- Adding `standards/launch/` (a new APES module): repository MINOR.
- Renaming `research/coverage/` to `research-os/coverage/`: repository MAJOR.
- Adding a new column to the Source Register schema: Research OS MAJOR.
- Fixing a broken link in `docs/lifecycle.md`: repository PATCH.
- Publishing Sprint 4 (Gap Analysis): repository MINOR (no schema changes).
- Publishing Sprint 3.1 (Audit): repository PATCH (audit findings applied to existing files).

Cross-version rules:

- A Project Layer MAY increment its MINOR without affecting the Standard Foundation or Research OS versions.
- A Standard Foundation change that breaks a Project Layer requires both to increment MAJOR.
- The Standard Foundation and Research OS versions are recorded in their own `VERSION` files (Foundation 0.x introduces them) so a family member can pin to a known-good pair.

## 12. Governance Strategy

The current governance framework (`governance/README.md`) distinguishes ADR / RFC / Decision Note. Foundation 0.1 extends it with a fourth type: **Foundation-RFC** for proposals that affect the shared layers.

Governance types:

| Type | Where it lives | When to use |
| --- | --- | --- |
| ADR | `governance/adr/` | Decision with structural, long-term impact. ADRs are append-only. |
| RFC | `governance/rfc/` | Proposal to change the standard. Needs community input. |
| Decision Note | `governance/decisions/` | Stage- or sprint-scoped choice that does not need full ADR ceremony. |
| Foundation-RFC | `governance/foundation-rfc/` (future) | Proposal to change the Standard Foundation or the Research OS. Affects every family member. |

Why a new type:

- Standard ADRs and RFCs are scoped to one project. Foundation-RFCs are scoped to the shared layers and therefore require explicit cross-project consent (from maintainers of every active family member, where applicable).
- Future Foundation 0.x work that moves a directory or promotes a doc to the Standard Foundation must originate as a Foundation-RFC.

Governance roles (preserved from `governance/README.md`):

- **Researcher.** Drafts notes per `research/research-plan.md` §4.2. Cannot self-accept.
- **Reviewer.** Independently challenges each Draft. Confirms or rejects.
- **Maintainer.** Accepts evidence into APES decision-making; writes or commissions the resulting ADR.

Foundation-specific roles (introduced for future family members):

- **Foundation Maintainer.** Has authority over the Standard Foundation and the Research OS. A project maintainer is not automatically a Foundation Maintainer. The list of Foundation Maintainers is recorded in `governance/foundation-maintainers.md` (future).
- **Family Reviewer.** Reviews Foundation-RFCs from the perspective of a downstream family member. Required at least one such reviewer per active family member.

Foundation-RFC rules:

- Status values: `Proposed`, `Accepted`, `Superseded`, `Deprecated`.
- A Foundation-RFC that is `Accepted` triggers a repository MAJOR version increment if the change is breaking.
- A Foundation-RFC must reference the affected layer (Research OS or Standard Foundation) and the affected version.

## 13. Compatibility Rules

Compatibility is the bridge between today and tomorrow. Foundation 0.1 codifies the rules.

Compatibility rules (in order from strictest to most lenient):

1. **The Research OS schema is contractually stable.** Once a Research OS version reaches MAJOR 1, its schemas (Source Register, Search Log, Verification Log, Coverage Map, Audit) do not change without a deprecation cycle. Sprint 4 Gap Analysis does not change Research OS schemas; if it did, that would be a Research OS MINOR.
2. **The Standard Foundation contract is contractually stable.** The lifecycle model, the evidence policy, and the governance framework do not change without a Foundation-RFC.
3. **External links are preserved across versions.** Any link from a CHANGELOG entry, an ADR, or a published snapshot must resolve to the same content in the next MAJOR version (possibly via an `archive/` redirect).
4. **Sprint files preserve their evidence trail.** Sprint files (`tasks/sprint-NN-*.md`) are append-only. Findings applied to other files are documented in the sprint file. Sprint evidence (Source IDs, verification IDs, audit findings) is not rewritten retroactively.
5. **Versioned directories are the migration seam.** When a directory moves, the old path remains as a redirect or stub for one MAJOR version. The move itself is a Foundation-RFC.
6. **The Project Layer may not modify the Standard Foundation or the Research OS.** If APES needs a change in a shared rule, it raises a Foundation-RFC.
7. **Adoption signals are never claimed in the repository.** ADR-0001 already enforces this; Foundation 0.1 reaffirms.
8. **Vendor neutrality is enforced at the layer boundary.** The Standard Foundation is vendor-neutral. The Project Layer (APES) is vendor-neutral. A future Project Layer that wants to endorse a tool must raise a Foundation-RFC explicitly forbidding it.

Original compatibility sketch during migration (historical; phases unassigned):

- Original Foundation 0.2 proposal — documentation-only boundary separation. Not executed under that label.
- Original Foundation 0.3 proposal — introduce a named Research OS subdirectory without moving files. Not executed under that label.
- Foundation 0.4 — first file move. Each move is paired with a `redirect.md` at the old path for one MAJOR version.
- Foundation 0.5 — first external family member. The compatibility contract is validated end-to-end.

## 14. Risk Assessment

Foundation 0.1 introduces risks the project must manage.

| Risk | Likelihood | Impact | Mitigation |
| --- | --- | --- | --- |
| **Premature standardization.** Locking in a layered model before any family member exists may over-engineer. | Medium | Medium | Foundation 0.1 only writes the plan; migration directory changes require a future scoped decision. |
| **Scope creep during migration.** Future sprints moving files could trigger scope creep. | Medium | Medium | Each Foundation-RFC names exactly one move; the redirect rule prevents silent breakage. |
| **Compatibility drift.** A change in one layer breaks consumers in another. | Medium | High | Compatibility rules §13; MAJOR version on breaking changes; redirect rule for one MAJOR version. |
| **Naming collisions.** Shared components and project-specific components may share names. | Medium | Low | Reserved shared-component names listed in §6; project-specific components must use names that do not collide. |
| **Governance overhead.** A Foundation-RFC is more ceremony than an ADR. | High | Low | Foundation-RFCs are required only when the shared layers change. Project-internal changes still use the lighter ADR / RFC / Decision Note path. |
| **Stale Research Gate.** Sprint 2 remains `In Review`; Research Gate is `RESEARCH AGAIN`. Foundation 0.1 does not change this. | Low | Low | Foundation 0.1 explicitly does not modify research evidence. The Research Gate is independent of the Foundation work. |
| **Future project drift.** A future family member forks the Foundation but drifts away. | Medium | Medium | Compatibility contract + Foundation-RFC review by Family Reviewers. The Foundation can deprecate a fork's "Foundation member" status if it diverges. |
| **Tooling temptation.** The Repository Evolution Plan may be read as permission to build CLI / MCP / website. | Medium | Medium | Foundation 0.1 explicitly reaffirms ADR-0001: no CLI, no MCP server, no IDE extension, no website. The Foundation is documentation only. |
| **Vendor capture.** A future family member may want to endorse a tool. | Low | High | Compatibility rule §13.8 forbids it; Foundation-RFC required to override. |

## 15. Open Questions

Foundation 0.1 raises questions that future Foundation sprints must answer. They are listed here as commitments to resolve.

- **OQ-1.** Should the Research OS become a separately-versioned package (npm / PyPI / similar) or remain a documentation-only contract? The actual Foundation 0.3 F1 prototype did not decide packaging; this remains open.
- **OQ-2.** Which root documents (`MANIFESTO.md`, `AGENTS.md`, `CONTRIBUTING.md`) are promoted to the Standard Foundation, and which remain APES-specific? The completed Foundation 0.2 reference-architecture sprint did not decide this; it remains open and requires per-document governance review.
- **OQ-3.** Where does the AGENTS.md-style agent guidance live in the layered model — Standard Foundation (as a generic discipline) or Project Layer (as APES-specific guidance)? The completed Foundation 0.2 sprint did not decide this; no follow-up sprint is assigned.
- **OQ-4.** How is `release/` (or equivalent) structured? Foundation 0.5 candidate.
- **OQ-5.** What is the canonical dependency graph between Project Layers when multiple family members exist? Foundation 1.0 candidate.
- **OQ-6.** Does the Foundation take on its own `LICENSE` distinct from APES? The completed Foundation 0.2 sprint did not decide this; an ADR-equivalent remains required.
- **OQ-7.** How does the Foundation handle Sprint 4 (Gap Analysis) outputs without entering Phase D? Documented in Foundation 0.1 §13: Sprint 4 is a Project Layer output; it does not modify the Standard Foundation or the Research OS.
- **OQ-8.** What is the protocol for "Research Gate `RESEARCH AGAIN`" if it persists past Foundation 1.0? Foundation 1.0 candidate.
- **OQ-9.** Does a future family member have to write its own ADR-0001, or can it inherit the Foundation's positioning ADR? Foundation 0.5 candidate; the working assumption is "each project writes its own ADR-0001-equivalent."
- **OQ-10.** Is the Foundation itself a GitHub organization, a branch, a tag, or a separate repository? Open. Default position: separate repository, future.

## 16. Cross-References

- [`docs/README.md`](README.md) — Reader-facing documentation.
- [`docs/lifecycle.md`](lifecycle.md) — End-to-end lifecycle as APES defines it (current 9-stage model).
- [`design/01-repository-architecture.md`](../design/01-repository-architecture.md) — v0.1 architectural decision; this Foundation 0.1 plan extends it.
- [`governance/README.md`](../governance/README.md) — Governance framework; Foundation 0.1 extends it with the Foundation-RFC type.
- [`governance/adr/ADR-0001-project-positioning.md`](../governance/adr/ADR-0001-project-positioning.md) — Project positioning; Foundation 0.1 reaffirms its scope boundaries.
- [`MANIFESTO.md`](../MANIFESTO.md) — Five principles; candidate for Standard Foundation promotion in Foundation 0.2.
- [`AGENTS.md`](../AGENTS.md) — Agent collaboration rules; candidate for Standard Foundation promotion in Foundation 0.2.
- [`CONTRIBUTING.md`](../CONTRIBUTING.md) — Contribution rules; candidate for Standard Foundation promotion in Foundation 0.2.
- [`research/research-plan.md`](../research/research-plan.md) — Methodology; candidate for a future, unassigned Research OS promotion task.
- [`research/source-register.md`](../research/source-register.md) — Source Register schema; Research OS candidate.
- [`research/notes/verification-log.md`](../research/notes/verification-log.md) — Verification schemas; Research OS candidate.
- [`research/coverage/`](../research/coverage/) — Coverage Map files; Project Layer data, Research OS schema.
- [`research/competitors/reverse-research.md`](../research/competitors/reverse-research.md) — Project Layer data.
- [`tasks/foundation-0-1-repository-evolution.md`](../tasks/foundation-0-1-repository-evolution.md) — Foundation 0.1 sprint task file.
- [`tasks/foundation-0-1-1-repository-evolution-upgrade.md`](../tasks/foundation-0-1-1-repository-evolution-upgrade.md) — Foundation 0.1.1 architecture refinement sprint task file.
- [`tasks/foundation-0-2-open-source-reference-architecture.md`](../tasks/foundation-0-2-open-source-reference-architecture.md) — Foundation 0.2 reference-architecture task file.
- [`governance/adr/ADR-0002-schema-first-reference-architecture.md`](../governance/adr/ADR-0002-schema-first-reference-architecture.md) — Accepted schema-first reference-architecture decision.
- [`CHANGELOG.md`](../CHANGELOG.md) — Sprint and Foundation Unreleased entries.

---

> **Foundation 0.1.1 — Architecture refinement note.** The seven sections below (17 through 23) refine, but do not replace, the Foundation 0.1 plan. The 4-layer model in §4 (Research OS → Standard Foundation → Project Layer → Release Layer) is preserved as a *deployment* view; the 6-layer model below (Meta → Foundation → Engine → Research → Project → Release) is the *architectural* view that explains how Research OS is structured above the Project Layer. Future Foundation sprints (0.2 onward) and any research sprints (Sprint 4 onward) reference this document for architecture rather than redefining it.

## 17. Repository Evolution Principles

These principles are the philosophical foundation of Research OS. Every architectural decision, every Foundation sprint, and every future research repository should be checkable against this list. When in doubt, the higher-numbered principle does not override a lower-numbered one; principles are listed in order of architectural precedence.

### 1. Backward Compatibility First

A new architecture layer or a new schema MUST preserve the contract of every layer below it. Breaking changes trigger a MAJOR version increment and a deprecation cycle (see §13 Compatibility Rules). When two valid designs conflict, prefer the one that does not invalidate earlier work. Backward compatibility is the strongest commitment this repository makes.

### 2. Research before Design

No standard, schema, engine, prompt, workflow, or template is written before the underlying evidence is registered in the Source Register and verified through the verification log. The Research Gate (`RESEARCH AGAIN` at the time of writing) is the operationalization of this principle. Design work that has not passed the gate is provisional and must be labeled as such.

### 3. Evidence before Opinion

Every non-trivial claim about an external project, an ecosystem, a market, or a technical practice must reference a Source ID. Claims without a Source ID are not accepted into any Decision Hierarchy artifact (RFC, ADR, Standard). When evidence is absent, the cell is `Unknown` (per Sprint 3 conventions) — not inferred.

### 4. Audit before Release

A snapshot is not released until it has been audited against its evidence trail. Sprint 3.1 (Coverage Audit) is the operationalization of this principle for the Coverage Map; the same audit posture applies to Gap Analysis (Sprint 4), to standard modules, to engines, and to releases. Audit findings are append-only and applied to the audited file in the same sprint or the next sprint — never silently.

### 5. Architecture before Implementation

No code, script, engine, prompt, workflow, or standard is implemented until the architectural layer that contains it is documented in this plan and accepted via the Decision Hierarchy (§20). Implementation that precedes architecture is treated as exploratory and is not promoted to Project Layer or Release Layer.

### 6. Shared before Project-specific

When a component is reusable across projects, it is moved into a shared layer (Meta, Foundation, Engine, or Research) before being duplicated across projects. The rule "shared before project-specific" prevents accidental fork-and-rewrites when a new family member is added. Project-specific content is allowed only when the shared layer cannot host it without losing its generic shape.

### 7. Everything Versioned

Every shared component, every project-specific artifact, and every Foundation sprint produces a Semantic Version. Versions are recorded in the file's front matter, in `CHANGELOG.md`, and in the Dependency Graph (§23). Unversioned artifacts are not eligible for promotion to the Release Layer.

### 8. Everything Traceable

Every claim, every decision, every audit finding, every verification attempt has a reference back to its source. Source IDs (SRC-NNN), Verification IDs (VR-NNN), External Verification IDs (EV-NNN), Audit Findings (A, B, C, …), Sprint IDs, and RFC IDs are the canonical identifiers. Files that lose their traceability chain are not accepted into a future sprint.

### 9. Everything Reproducible

Every audit, every statistic, every coverage map, and every report must be reproducible from the underlying evidence trail. A reader who starts from the Source Register and follows the cited references must be able to reconstruct the artifact. Reproducibility is the operationalization of "Evidence before Opinion" and "Audit before Release."

### 10. No Hidden Decisions

Every non-trivial decision is recorded in an ADR, RFC, Foundation-RFC, or Decision Note before it takes effect. Decisions made in conversation, in private notes, or in unmerged drafts are not promoted to Project Layer or Release Layer. The Decision Hierarchy (§20) makes the recording path explicit.

These ten principles supersede ad-hoc reasoning in any future sprint. They do not replace the Manifesto (`MANIFESTO.md`); they extend it with architectural commitments.

## 18. Repository Layer Model

The Repository Evolution Plan uses a **6-layer architectural model**. The 4-layer view in §4 (Research OS → Standard Foundation → Project Layer → Release Layer) is preserved as a deployment view; the 6-layer view below is the architectural view that explains how Research OS is structured above the Project Layer.

```
┌─────────────────────────────────────────────────────────────────┐
│                          Meta Layer                             │
│   Principles, governance framework, compatibility contract,    │
│   version policy, decision hierarchy, document taxonomy,       │
│   maturity model, dependency graph.                             │
│   Depends on: (nothing)                                         │
└─────────────────────────────────────────────────────────────────┘
                                │
┌─────────────────────────────────────────────────────────────────┐
│                       Foundation Layer                          │
│   Manifesto, evidence policy, lifecycle model, contributor      │
│   compact, license posture, archival policy.                    │
│   Depends on: Meta Layer                                        │
└─────────────────────────────────────────────────────────────────┘
                                │
┌─────────────────────────────────────────────────────────────────┐
│                         Engine Layer                            │
│   Source Register engine, Verification engine, Coverage engine, │
│   Audit engine, Statistics engine, Report engine, Schema        │
│   validators, Migration engine.                                 │
│   Depends on: Meta Layer, Foundation Layer                      │
└─────────────────────────────────────────────────────────────────┘
                                │
┌─────────────────────────────────────────────────────────────────┐
│                        Research Layer                           │
│   Research plan, source register rows, search log, verification │
│   log, coverage maps, gap analyses, evidence trails, audit      │
│   findings. Generic. Project-agnostic.                          │
│   Depends on: Meta Layer, Foundation Layer, Engine Layer        │
└─────────────────────────────────────────────────────────────────┘
                                │
┌─────────────────────────────────────────────────────────────────┐
│                        Project Layer                            │
│   APES, AI Security, IoT Security, Binary Security, Research    │
│   Library (candidates). Lifecycle modules, templates, commands, │
│   checklists, examples, project-specific ADRs, project-specific │
│   research content (rows).                                      │
│   Depends on: Meta Layer, Foundation Layer, Engine Layer,       │
│               Research Layer                                    │
└─────────────────────────────────────────────────────────────────┘
                                │
┌─────────────────────────────────────────────────────────────────┐
│                        Release Layer                            │
│   Tagged snapshots, public bundles, change logs, distribution    │
│   manifests. Frozen Project Layer state for external consumers. │
│   Depends on: Project Layer                                     │
└─────────────────────────────────────────────────────────────────┘
```

Layer responsibilities (architecture only; no implementation described):

- **Meta Layer.** The repository's own architectural rules. Holds principles (this section), the governance framework (`governance/README.md`), the compatibility contract (§13), the version policy (§11), the decision hierarchy (§20), the document taxonomy (§21), the maturity model (§22), and the dependency graph (§23). The Meta Layer is the only layer that knows about the existence of all other layers.

- **Foundation Layer.** Cross-project commitments that are not Meta. Includes the Manifesto (the five principles in `MANIFESTO.md`, candidate for promotion in Foundation 0.2), the evidence policy (currently distributed across `AGENTS.md` and `CONTRIBUTING.md`), the lifecycle model (the 9-stage APES lifecycle and the broader 19-stage Sprint 3 lifecycle), the contributor compact, the license posture, and the archival policy. The Foundation Layer is the contract every family member inherits.

- **Engine Layer.** Generic engines that operate on the schemas defined in the Foundation Layer. Most remain architecture positions. F2 implements only the read-only validator and derived artifact graph in the separately governed `APES-Validator` repository under ADR-0003; Source Register, Verification, Coverage, Audit, Statistics, Report, and Migration engines remain unimplemented.

- **Research Layer.** Generic research artifacts. The Source Register, the Search Log, the Verification Log, the Coverage Map, the Gap Analysis, the Audit Findings, the Evidence trails, the Statistics outputs, the Reports. The Research Layer is project-agnostic — its schemas are reusable for any future research effort.

- **Project Layer.** Each project's domain content. APES is the first instance; AI Security, IoT Security, Binary Security, Research Library are candidates. Project-specific lifecycle modules (`standards/discovery/`, etc.), project-specific templates, project-specific commands, project-specific checklists, project-specific examples, project-specific research content (the rows in the Coverage Map, the rows in the Gap Analysis). The Project Layer is the only layer that contains project identity.

- **Release Layer.** Tagged snapshots. Public bundles. Frozen Project Layer state. The Release Layer is what an external consumer reads, imports, or mirrors.

Dependency direction (strict):

- Higher layers depend on lower layers; lower layers know nothing about higher layers.
- The Meta Layer has no dependency.
- The Foundation Layer depends only on the Meta Layer.
- The Engine Layer depends on the Meta Layer and the Foundation Layer.
- The Research Layer depends on the Meta Layer, the Foundation Layer, and the Engine Layer.
- The Project Layer depends on the Meta Layer, the Foundation Layer, the Engine Layer, and the Research Layer.
- The Release Layer depends on the Project Layer.

A violation of this direction (e.g., the Foundation Layer referencing a project-specific module) is a Foundation-RFC-blocking issue.

## 19. Repository Lifecycle

The repository evolves through a **9-stage repository lifecycle**. This is the lifecycle of *the repository itself*, not the lifecycle of any single product or standard that the repository hosts.

```
Idea → Research → Audit → Architecture → Implementation
      → Validation → Release → Maintenance → Archive
```

Stage responsibilities:

- **Idea.** A repository concept is proposed. The proposal is captured as a Decision Note or a lightweight ADR. No directory is created yet; no schema is defined.
- **Research.** The proposal is researched against external evidence. A Source Register is started; Search Log entries are produced; Verification Log entries are produced. Research Gate is applied. The Research stage is mandatory; a repository cannot move to Architecture without passing the Research Gate for at least its core claims.
- **Audit.** The Research stage's outputs are audited. Audit Findings are recorded; inconsistencies and gaps are surfaced and applied. The audit is append-only and applied before the repository progresses.
- **Architecture.** The repository's layered shape, principles, decision hierarchy, document taxonomy, maturity model, and dependency graph are documented. This is the stage Foundation 0.1 / 0.1.1 belongs to.
- **Implementation.** Code, scripts, engines, prompts, workflows, standards, and templates are produced. Implementation MUST follow the architecture; architecture MUST be in place before implementation begins. (Principle 5: Architecture before Implementation.)
- **Validation.** Implementation is validated against the architecture and against the evidence trail. Validation may produce Audit Findings that loop back to Architecture or to Implementation.
- **Release.** A snapshot is tagged and published. The Release Layer content is frozen. A release note is written.
- **Maintenance.** Bug fixes, documentation corrections, link repairs, and minor refactors. Maintenance preserves backward compatibility (Principle 1). A change in maintenance can trigger a PATCH or MINOR version increment; a MAJOR increment requires returning to Architecture.
- **Archive.** The repository reaches end-of-life. An `archive/<version>/` directory holds frozen snapshots; redirects preserve external links for one additional MAJOR version.

Transition rules:

- A repository advances forward only. There is no skipping a stage. A repository may revisit an earlier stage only via a Decision Hierarchy artifact (RFC, ADR, or Foundation-RFC).
- Forward transitions are gated: each stage has explicit entry conditions. The entry conditions are recorded in the Decision Hierarchy (§20).
- Reverse transitions are exceptional and must be justified in writing. A return from Validation to Architecture is allowed when a validation finding invalidates an architectural assumption. A return from Implementation to Architecture is allowed when an implementation constraint contradicts the architecture. A return from Release to Architecture is allowed only for a hotfix or a security patch.
- Archive is irreversible. An archived repository cannot return to Maintenance; a successor repository must be created and linked from the archive.

Lifecycle and Foundation sprints:

- Foundation 0.1 = Architecture stage.
- Foundation 0.1.1 = Architecture stage refinement.
- Foundation 0.2, 0.3, 0.4 = Architecture → early Implementation.
- Foundation 0.5 = Validation stage (first family member validates the contract).
- Foundation 1.0 = Release stage candidate (Research OS and Standard Foundation reach v1.0).
- Future Maintenance and Archive stages are far beyond the current horizon.

## 20. Decision Hierarchy

Decisions in this repository follow a strict hierarchy. Each tier constrains the tier below it; a lower tier cannot override a higher tier.

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

Tier responsibilities:

- **Principles.** The Repository Evolution Principles (§17). The five Manifesto principles in `MANIFESTO.md` are the philosophical core; the ten Repository Evolution Principles are the architectural commitment. Principles are the slowest-changing tier.
- **Constitution.** A future document (currently `OQ-N` in the open questions list) that consolidates the principles, the evidence policy, the governance framework, the compatibility contract, the version policy, and the lifecycle model into a single root document. The Constitution is the single document a future family member MUST accept to be considered a member of the repository family. The Constitution does not exist yet; Foundation 0.1.1 reserves the slot but does not write it.
- **RFC.** A Request for Comments. Used to propose changes to the Constitution, to introduce a new Standard or a new Schema, or to modify the layered architecture. RFCs require explicit community input. The current `governance/rfc/` directory is a placeholder for the future RFC framework.
- **Standard.** A named, scoped rule that applies across the repository family. APES itself is the first Standard. Future Standards (AI Security, IoT Security, Binary Security, Research Library) will each have their own position in this tier. Standards inherit the Constitution and the active RFCs.
- **Schema.** A structured definition of a document, a row, or a message. The Source Register schema, the Coverage Map schema, the Audit Finding schema are Schemas. Schemas are versioned independently of Standards; a Schema MAY change without an RFC if the change preserves compatibility (Principle 1).
- **Engine.** A named capability that operates on Schemas. The Source Register engine, Verification engine, Coverage engine, Audit engine, Statistics engine, and Report engine are Engines in this tier. F2 now implements the bounded read-only validator and graph derivation in a separate repository; the remaining engines are still reserved architecture positions.
- **Workflow.** A named sequence of steps that uses Engines and Schemas to produce a Project artifact. Workflows are project-specific in their *content* but generic in their *shape*. Foundation 0.1.1 reserves the tier.
- **Prompt.** A named instruction template that runs inside a Workflow. Prompts are project-specific and may inherit Foundation Layer constraints. Foundation 0.1.1 reserves the tier.
- **Project.** A concrete instance that consumes Schemas, Engines, Workflows, and Prompts to produce a Standard's evidence and outputs. APES is the first Project. Each Project carries its own identity, positioning ADR, and lifecycle modules.
- **Sprint.** A time-boxed unit of work that updates a Project. Sprint files (`tasks/sprint-NN-*.md` and `tasks/foundation-N-N-*.md`) are the canonical record. Sprints are the most short-lived tier.

Conflict resolution:

- A lower tier cannot override a higher tier. A Sprint cannot redefine a Principle; a Project cannot redefine a Standard; a Prompt cannot redefine a Schema.
- When two artifacts in the same tier conflict, the more recent one is not automatically authoritative. Authority within a tier is recorded by the artifact's status: `Accepted` > `Proposed` > `Draft`.
- A conflict between tiers is resolved by raising an RFC that proposes a change to the higher tier. The Sprint that surfaced the conflict MUST be paused (or its scope amended) until the RFC is decided.
- Conflict resolution is recorded in the affected file's front matter as a `Resolution:` line that references the deciding artifact.

## 21. Document Taxonomy

Every artifact in the repository belongs to exactly one document type. The taxonomy below is exhaustive at the level of Foundation 0.1.1; future Foundation sprints may add types via Foundation-RFC.

| Type | Purpose | Owner | Lifecycle | Version policy |
| --- | --- | --- | --- | --- |
| **Policy** | Authoritative rule that constrains behavior across the repository family. | Meta Layer maintainers | Slow-changing; one major revision per year at most. | MAJOR on rule change; MINOR on addition; PATCH on wording. |
| **Constitution** | The consolidated root document a future family member MUST accept. | Meta Layer maintainers | Reserved slot; not yet written. | Reserved. |
| **RFC** | Proposal that affects the Constitution, a Standard, or the layered architecture. | RFC author + Reviewer + Maintainer | Open for review; once `Accepted`, append-only. | MAJOR on accept if it changes a higher-tier rule. |
| **ADR** | Decision with structural, long-term impact at the Project level. | Project maintainers | Append-only. | MAJOR on accept; rarely. |
| **Research** | Evidence-driven study of an ecosystem, a competitor, or a paper. | Researcher + Reviewer | Research Gate controlled. | MINOR on new sprint; PATCH on corrections. |
| **Coverage** | Matrix mapping a Project's lifecycle stages to external artifacts. | Coverage author + Reviewer | Built after Research; audited before Release. | MINOR on new sprint; PATCH on audit findings. |
| **Gap Analysis** | Evidence-driven identification of gaps between a Standard and the external landscape. | Gap author + Reviewer | Built after Coverage. | MINOR on new sprint. |
| **Evidence** | A single piece of evidence: a Source Register row, a Verification Log row, an External Verification row, an Audit Finding. | Evidence owner | Append-only; corrections via new Evidence entries that reference the original. | PATCH per entry. |
| **Statistics** | Aggregate counts derived from Evidence. | Statistics engine (future) or hand-calculated in a Sprint | Reproducible from Evidence. | PATCH on recomputation. |
| **Report** | Per-sprint or per-stage narrative explaining what was researched, audited, decided, and shipped. | Sprint owner | One per sprint. | PATCH per revision. |
| **Task** | A unit of work scoped to a single Sprint. | Sprint owner | Append-only; superseded tasks are marked, not removed. | PATCH per revision. |
| **Prompt** | A named instruction template (architecture position only; no implementation in Foundation 0.1.1). | Engine Layer (future) | Reserved. | Reserved. |
| **Checklist** | A quality or gate checklist for a specific stage or artifact. | Checklist owner | Updated when the stage or artifact changes. | PATCH per revision. |
| **Template** | A reusable document or artifact template. | Template owner | Updated when the underlying Schema changes. | MAJOR on Schema change; PATCH on wording. |
| **Release Notes** | A summary of what changed in a tagged snapshot. | Release owner | One per Release. | PATCH per release. |

Target taxonomy rules for artifacts promoted through the future metadata migration:

- Every migrated machine-checkable artifact carries a `type:` field naming exactly one supported type.
- Legacy Markdown remains canonical and readable until a separately reviewed migration; F2 currently reports zero migrated artifacts rather than treating legacy headers as contract metadata.
- A newly promoted artifact that does not fit the taxonomy is not accepted into the repository.
- New types are added only via Foundation-RFC.

## 22. Repository Maturity Model

The repository progresses through **six maturity levels**. The current target (post-Foundation 0.1.1) is Level 2; higher levels are documented as targets for future sprints.

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

Level characteristics:

- **Level 0 — Bootstrap.** The repository exists. Identity documents are in place (`README.md`, `VISION.md`, `MANIFESTO.md`, `ROADMAP.md`, `CONTRIBUTING.md`, `AGENTS.md`, `CHANGELOG.md`, `LICENSE`). No research has been conducted. No standards have been written. Governance is a placeholder. **Current state at Sprint 0.**

- **Level 1 — Research.** The repository has a documented research plan, a Source Register, a Search Log, a Verification Log, and at least one Coverage Map. The Research Gate is operational. Sprint 2 (Inventory) through Sprint 3 (Coverage Map) belong to this level. **Current state at Sprint 3.1.**

- **Level 2 — Standardization.** The repository has at least one Gap Analysis, at least one Standard module, and a documented Repository Evolution Plan. The Decision Hierarchy is defined. The Document Taxonomy is defined. The Repository Layer Model is defined. Foundation 0.1 / 0.1.1 belong to this level. **Current target.**

- **Level 3 — Automation.** The Engines in the Engine Layer exist as code. The Audit engine runs automatically on every Coverage commit. The Statistics engine produces reproducible aggregate counts. The Report engine produces per-sprint narratives. Schemas are enforced by validators. F2 provides an initial read-only validator, but Level 3 is not reached until the remaining automation and workflow gates exist.

- **Level 4 — Platform.** A second Project Layer instance exists (e.g., AI Security or IoT Security). The compatibility contract is validated end-to-end. Family members consume the Foundation and the Research OS without modification. Foundation 0.5 targets this level.

- **Level 5 — Research OS.** The Research OS is at v1.0. The Standard Foundation is at v1.0. Multiple Project Layer instances are in Maintenance. The Meta Layer (Principles, Constitution, Decision Hierarchy, Document Taxonomy, Maturity Model, Dependency Graph) is stable. Foundation 1.0 targets this level.

Maturity rules:

- The repository advances only when its current level's expected outputs are present and stable.
- A regression (e.g., losing the Source Register) drops the repository to the previous level until the artifact is restored.
- The maturity level is recorded in `README.md` and in `CHANGELOG.md` as it changes.

## 23. Repository Dependency Graph

The dependency graph documents the canonical order in which artifacts depend on each other. The graph below is a *direction* graph, not an *implementation* graph — it explains what may reference what, not what has been written.

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

Dependency direction (strict):

- **Principles → Constitution.** The Constitution is constructed from the Principles. A Principle can exist without a Constitution; the reverse is not allowed.
- **Constitution → Schemas.** Schemas are constructed in the framework defined by the Constitution. A Schema can be drafted before the Constitution is finalized, but cannot be promoted without Constitutional alignment.
- **Schemas → Engines.** Engines operate on Schemas. An Engine without a Schema is not a valid Engine.
- **Engines → Workflows.** Workflows call Engines. A Workflow without an Engine is a script, not a Workflow.
- **Workflows → Prompts.** Prompts run inside Workflows. A Prompt without a Workflow is an instruction, not a Prompt in this taxonomy.
- **Prompts → Research.** Research uses Prompts (e.g., search prompts, extraction prompts). Research is the first place where Schemas, Engines, Workflows, and Prompts converge.
- **Research → Coverage.** Coverage consumes Research outputs (Source Register, Verification Log). Coverage cannot exist without Research.
- **Coverage → Gap.** Gap Analysis consumes Coverage outputs. Gap cannot exist without Coverage.
- **Gap → Release.** Release consumes Gap outputs (the Release Notes summarize the Gap). Release cannot exist without Gap.

The graph forbids:

- A Research artifact depending on a Release artifact.
- A Coverage artifact depending on a Gap artifact.
- A Schema depending on an Engine.
- A Principle depending on any lower-tier artifact.

A violation of these rules is a Foundation-RFC-blocking issue, with one exception: an exploratory Sprint MAY produce an out-of-order artifact as long as it is labeled `Provisional` in its front matter and is not promoted to a higher tier.

The dependency graph and the Decision Hierarchy (§20) are dual views of the same constraint set. The Decision Hierarchy is *who decides*; the dependency graph is *what depends on what*. Future Foundation sprints consult both.

---

**End of Foundation 0.1.1 architectural refinements.** Sections 1–16 are Foundation 0.1; sections 17–23 are Foundation 0.1.1. Future Foundation sprints (0.2 onward) and any research sprints (Sprint 4 onward) reference this document for architecture rather than redefining it.

---

> **Foundation 0.2 — Open-source reference architecture.** Sections 24 through 28 translate the existing six-layer model into an implementable, documentation-first design. They are informed by direct inspection of GitHub Spec Kit, OpenSpec, BMAD-METHOD, and Agent OS on 2026-08-05. Detailed evidence and APES-oriented trade-offs are recorded in [`research/competitors/open-source-reference-comparison.md`](../research/competitors/open-source-reference-comparison.md). The research sample is limited to four projects and the Research Gate remains `RESEARCH AGAIN`.

## 24. Open-Source Reference Comparison

The four projects were selected for complementary architecture patterns, not popularity. Every observed external fact below references the Source Register. Strengths and trade-offs are APES-oriented inferences from those facts, not independent effectiveness claims.

| Project | Observable function and architecture | Technology stack | Strengths for APES (inference) | Trade-offs for APES (inference) | Pattern to adopt |
| --- | --- | --- | --- | --- | --- |
| **GitHub Spec Kit** | Constitution → Specify → Plan → Tasks → Implement core flow; optional Clarify / Analyze / Checklist controls; Python CLI; agent integrations; extensions, presets, workflows, and bundles; packaged offline templates and scripts. `SRC-025` | Python 3.11+, Typer, Click, Rich, PyYAML, Hatchling, pytest; Markdown plus Bash, PowerShell, Python, YAML / JSON assets. `SRC-025` | Strong separation between stable core, organization customization, and agent-specific projections; reproducible offline assets. | The ecosystem surface is larger than APES currently needs; the core starts after much of APES's evidence and discovery lifecycle; copying the CLI now would violate ADR-0001. | Core-versus-adapter boundary, deterministic packaging, explicit override priority. |
| **OpenSpec** | Explore → Propose → Apply → Archive; one change package contains proposal, requirements / scenarios, design, and tasks; optional cross-repository Stores. `SRC-026` | Node.js 20.19+, TypeScript ESM, pnpm, Commander, Inquirer, YAML, Zod, Vitest. `SRC-026` | Compact, reviewable, diffable change envelope; strong brownfield orientation; plain Markdown requirements. | Narrower than APES's research and decision chain; Node and post-install behavior add runtime surface; Stores are beta and would create a source-of-truth decision. | Append-only change package with explicit archive state. |
| **BMAD-METHOD** | Analysis → Planning → Solutioning → Implementation; specialized skills / agents; progressive context artifacts; readiness, review, sprint, and retrospective gates. `SRC-053` | Node.js 20.12+, JavaScript, YAML, Markdown, Python helper scripts, Astro / Starlight, ESLint, Markdownlint, test scripts. `SRC-053` | Closest full-lifecycle coverage; clear artifact handoffs; proportional quick and deep paths; explicit readiness checks. | Large role and workflow surface raises context and governance cost; adopting its installer / agent framework would undermine APES's standard-first positioning. | Progressive context, readiness gates, and proportional workflow depth without mandatory personas. |
| **Agent OS** | Discover, index, inject, and shape standards; Markdown standards with YAML index; profile inheritance; timestamped specs; shell installer projecting agent commands. `SRC-054` | Shell, Markdown, YAML; no service runtime observed. `SRC-054` | Lightweight and inspectable; selective injection addresses context cost; human confirmation reduces silent policy drift. | Inspected projection targets a vendor-specific command directory; shell-first installation is less uniform on Windows; mined conventions can preserve local mistakes without evidence review. | Standards index plus selective, generated, non-canonical projections. |

Cross-project convergence:

- Canonical knowledge is primarily Markdown; machine-readable YAML / JSON structures make it operational. `SRC-025`, `SRC-026`, `SRC-053`, `SRC-054`
- Phase artifacts carry context forward instead of relying on one-shot prompts. `SRC-025`, `SRC-026`, `SRC-053`, `SRC-054`
- Host-agent commands are projections of a process model, not the process's canonical source. `SRC-025`, `SRC-026`, `SRC-053`, `SRC-054`
- Quality improves when there are explicit pre-implementation review or readiness steps. `SRC-025`, `SRC-026`, `SRC-053`, `SRC-054`
- None of the inspected core projects exposes the complete APES chain of Source Register → Verification → Coverage → Audit → Decision → Standard → Release. This limited-sample finding is APES's main differentiation opportunity, not a market-positioning claim. `SRC-025`, `SRC-026`, `SRC-053`, `SRC-054`

## 25. APES Target Implementation Architecture

The recommended design is **schema-first, file-native, Git-backed, deterministic, and adapter-driven**. APES remains the canonical standard and evidence repository. Any future executable tooling is a separate consumer of the contracts defined here, consistent with ADR-0001.

### 25.1 Logical component model

```text
Canonical Markdown + YAML front matter
                │
                ▼
Contract and Schema Registry
                │
                ▼
Artifact Graph and Index ──────► Deterministic Validators / Audits
                │                              │
                ▼                              ▼
Declarative Workflows and Gates ───────► Reports / Release Bundles
                │
                ▼
Agent Adapters and Context Projections
```

The components map onto the existing six layers without redefining them:

| Logical component | Six-layer owner | Responsibility | Canonical? |
| --- | --- | --- | --- |
| Principles, governance, compatibility, version rules | Meta Layer | Constrain every lower component. | Yes |
| Artifact contracts and evidence policy | Foundation Layer | Define mandatory metadata, status, identifiers, and citation rules. | Yes |
| Schema registry | Foundation Layer | Define machine-checkable structures for artifacts and relationships. | Yes |
| Validators, graph builder, gate evaluator, report generator | Engine Layer | Deterministic read-only operations over contracts and files. | No; implementations consume the canonical contracts. |
| Source rows, verification rows, coverage, audits, reports | Research Layer | Store reusable evidence-shaped artifacts and their traceability chain. | Yes |
| APES modules, templates, examples, project decisions | Project Layer | Provide domain-specific content while inheriting shared contracts. | Yes |
| Agent adapters and context projections | Project / Release boundary | Render only the relevant subset for Codex, Claude Code, Cursor, or a generic agent. | No; generated and replaceable. |
| Release manifest and frozen bundle | Release Layer | Pin versions, checksums, dependency graph, and included artifacts. | Yes for the manifest; bundle is derived. |

### 25.2 Canonical artifact contract

Every future machine-checkable artifact should remain readable as plain Markdown and carry a small YAML front matter contract:

```yaml
---
id: ADR-0002
type: ADR
status: Proposed
version: 0.1.0
owners: [APES-Maintainers]
depends_on: [ADR-0001, SRC-025, SRC-026, SRC-053, SRC-054]
supersedes: []
evidence: [SRC-025, SRC-026, SRC-053, SRC-054]
last_updated: 2026-08-05
---
```

This example informed the F1 contract created later in Foundation 0.3. The canonical schema now lives at [`schemas/artifact-metadata.schema.json`](../schemas/artifact-metadata.schema.json) and validates the common metadata shape; F2 adds repository-aware reference, dependency, link, and graph checks. Existing legacy Markdown has not yet been migrated to front matter.

### 25.3 Artifact graph

The artifact graph is derived from front matter and links. It must not become a second hand-edited source of truth.

Nodes:

- Source, Verification, Research, Coverage, Gap, ADR, RFC, Standard, Schema, Workflow, Task, Audit, Release.

Edges:

- `depends_on`, `evidence_for`, `supersedes`, `implements`, `validates`, `produces`, `consumes`, `released_in`.

Required graph checks:

- All referenced IDs exist and are unique.
- Dependency direction matches §23.
- A lower-tier artifact cannot silently override a higher tier.
- A release has no unresolved `Draft`, failed gate, missing evidence, or broken link in its included set.
- Generated agent projections point back to canonical artifacts and are never accepted as canonical evidence.

### 25.4 Declarative workflow and gate model

Workflow definitions should be data, not hard-coded agent prompts. A future workflow contract should declare:

- stage identifier and permitted predecessors;
- required inputs and produced artifacts;
- deterministic validators;
- human approval points;
- evidence and decision requirements;
- rollback / archive behavior;
- adapter hints that do not change the canonical workflow.

APES should support two depths:

- **Fast path:** maintenance and narrowly scoped documentation corrections. Requires status check, relevant file read, link validation, diff review, task update, and CHANGELOG entry.
- **Full path:** research, architecture, standard, schema, or cross-cutting change. Requires Source Register entries, review, ADR / RFC where applicable, artifact graph checks, readiness gate, validation, and release audit.

The workflow evaluator must be deterministic. LLMs may help draft artifacts but cannot be the authority that decides whether a schema, link, checksum, identifier, or status transition is valid.

### 25.5 Adapter boundary

Agent-facing instructions are generated projections, following the strongest common pattern in the four references:

- one generic adapter contract;
- one adapter per supported agent only when a real project needs it;
- adapters render canonical standards, relevant evidence, task scope, and allowed commands;
- adapters cannot edit Meta / Foundation rules or hide required gates;
- generated files include source artifact IDs and generator version;
- users can inspect a dry-run diff before any projection writes files;
- no agent SDK or model API is required by the core.

This keeps APES compatible with agent conventions without competing with them, preserving ADR-0001.

## 26. Recommended Technical Stack

### 26.1 Canonical contract stack (recommended now)

| Concern | Recommendation | Rationale |
| --- | --- | --- |
| Human-readable artifacts | CommonMark / GitHub-Flavored Markdown | Already canonical in the repository and used across all four references. `SRC-025`, `SRC-026`, `SRC-053`, `SRC-054` |
| Structured metadata | YAML 1.2 front matter with a deliberately small field set | Supports readable versioned metadata and matches the surrounding ecosystem without making prose machine-only. |
| Formal schemas | JSON Schema 2020-12 | Vendor-neutral, language-neutral, and suitable for validating YAML-parsed objects and JSON release manifests. |
| Versioning and history | Git + Semantic Versioning | Preserves diffability, review, provenance, and rollback without adding a database. |
| Canonical storage | Repository files only | Offline-first; no service dependency; compatible with the current documentation-first contract. |
| Diagrams | Text / Mermaid embedded in Markdown | Reviewable in Git and reproducible without binary design files. |

No new production dependency is added in Foundation 0.2.

### 26.2 F2 validator / CLI stack (implemented, independent re-review pending)

ADR-0003 approved the first executable as a **read-only validator in a separate tooling repository**. The implemented F2 stack is:

| Concern | Recommended candidate | Why |
| --- | --- | --- |
| Runtime | Python 3.12+ | Cross-platform, strong document / data tooling, and a proven pattern in Spec Kit. `SRC-025` |
| CLI | Typer + Rich | Typed commands and readable diagnostics; keeps the first runtime small. |
| YAML / schema | PyYAML + `jsonschema` | Direct implementation of the canonical YAML / JSON Schema contract. |
| Packaging | `uv` + Hatchling | Reproducible tool environments and isolated CLI installation; does not affect this repository until approved. |
| Tests | pytest, golden fixtures, property tests for identifiers / graph rules | Deterministic validation and regression coverage. |
| Static checks | Ruff + mypy | Small, fast quality baseline. |
| Markdown checks | markdownlint plus a repository-aware relative-link checker | Enforces existing documentation hygiene. |

Why Python instead of adopting Node / TypeScript immediately:

- Spec Kit demonstrates that a Python CLI can package Markdown templates and cross-platform scripts for offline use. `SRC-025`
- OpenSpec and BMAD demonstrate that Node / TypeScript is viable, but both include broader installer / website / ecosystem surfaces than the first APES validator needs. `SRC-026`, `SRC-053`
- APES's first executable requirement is deterministic document and graph validation, not an interactive agent runtime.

This stack was accepted for F2 by ADR-0003. F2 remains `In Review` until an eligible independent reviewer approves the remediated snapshot; later engines or a technology-stack change require their own scoped decision.

### 26.3 Explicit non-goals

The first implementation must not include:

- a database, hosted API, SaaS control plane, telemetry service, or user account system;
- direct model API calls, prompt routing, autonomous coding, or multi-agent orchestration;
- remote extension catalogs or arbitrary post-install hooks;
- a website, VS Code extension, MCP server, or in-repository application source;
- automatic destructive migration or overwriting of existing user files.

## 27. Staged Implementation Plan

Each phase is independently reviewable and stops at its exit gate. Later phases are proposals, not active Sprint scope.

| Phase | Scope | Deliverables | Exit gate | Rollback |
| --- | --- | --- | --- | --- |
| **F0 — Reference design (completed)** | Compare references and define the target. | Reference-design plan, comparison report, Source Register updates, ADR-0002 (`Accepted`). | Completed: Markdown links and evidence IDs validate; maintainer accepted ADR-0002 on 2026-08-07. | Revert only Foundation 0.2 additive sections and records; no runtime state exists. |
| **F1 — Contract prototype (completed)** | Define one minimal artifact front matter schema and fixtures without moving existing files. | JSON Schema 2020-12 contract, eight representative valid / invalid fixtures, compatibility mapping for existing docs. | Completed: schema and fixtures validated; all existing files remain readable; zero directory moves. | Remove prototype files; existing Markdown remains canonical. |
| **F2 — Read-only validator (In Review — Remediation Ready)** | Parse and validate metadata, IDs, links, and dependency direction in a separate tooling repository. | Implemented `check`, `graph`, and `explain`; closed Schema Registry; Schema v0.2.0; 87 tests at 91.20% coverage; initial-review, remediation, and implementer follow-up evidence. | All thirteen initial findings have implementation responses, follow-up hardening and automated gates pass; independent re-review approval remains pending. | Stop using or remove the validator; canonical Markdown remains unchanged. |
| **F3 — Workflow and gates** | Encode fast and full paths as declarative workflows. | Workflow schema, gate evaluator, readiness report, dry-run transition command. | Manual and generated results agree on representative cases; no LLM required for pass/fail. | Disable workflow evaluation; F2 validation remains usable. |
| **F4 — Agent adapters** | Generate minimal context projections for one generic adapter and one validated real-agent adapter. | Adapter contract, source mapping, dry-run diff, generated-file provenance. | A real project completes one scoped task without editing canonical Foundation rules. | Delete generated projections; canonical artifacts remain intact. |
| **F5 — Release reporting** | Produce deterministic reports and frozen bundles. | Release manifest, checksums, evidence summary, audit report, archive path. | Rebuild produces identical manifest and checksums; compatibility links resolve. | Withdraw derived bundle; source repository history remains authoritative. |

Recommended sequencing constraints:

1. Do not start F1 until ADR-0002 is Accepted and the Foundation 0.2 review is complete.
2. Do not start F2 until F1 schemas have at least one real APES case and one intentionally invalid fixture set.
3. Do not start F3 until the read-only validator is stable; workflow automation must not hide schema failures.
4. Do not start F4 until a real project names the context-injection problem and the generic adapter contract exists.
5. Do not start F5 until an end-to-end case reaches validation and its evidence trail can be reproduced.

## 28. Guardrails, Risks, and Decision Status

### 28.1 Security and data-safety guardrails

- Resolve every input path to the repository root and reject traversal outside it.
- Treat symlinks, junctions, and generated paths as untrusted until resolved.
- Never execute commands declared in repository YAML / Markdown.
- No `shell=True`, arbitrary hooks, remote catalog execution, or implicit package installation.
- Read-only is the default. Any future write command requires `--dry-run`, a diff preview, explicit target confirmation, and a backup / rollback path.
- Never collect or transmit repository content, secrets, tokens, private source text, or customer data.
- Use a closed JSON Schema Registry with no retrieval hook; accept only the deliberately restricted local APES Schema profile.
- Pin release dependencies and verify downloaded artifacts before any future installer exists.

### 28.2 Main risks and mitigations

| Risk | Mitigation |
| --- | --- |
| Prematurely encoding an unvalidated standard | Keep F0 documentation-only; require a real case and accepted ADR before schemas or tooling. |
| Taxonomy / schema over-complexity | Start F1 with one minimal contract and representative fixtures; add fields only from observed failures. |
| Canonical / generated drift | Canonical Markdown is the only editable truth; projections carry source IDs and are disposable. |
| Vendor capture through adapters | Generic adapter first; no model SDK in core; adapters cannot change gates or policy. |
| Hidden workflow decisions | Declarative workflow files, deterministic gate results, and ADR / RFC for cross-cutting changes. |
| Supply-chain expansion | No runtime dependency in F0/F1; separate tooling repository; minimal pinned dependencies if F2 is approved. |
| Windows portability gaps | Validate paths and line endings on Windows first; avoid shell-only core behavior; retain Bash / PowerShell only as optional projections. |
| Research overclaim | Keep the comparison Draft, cite Source IDs, distinguish observation from inference, and preserve `RESEARCH AGAIN`. |

### 28.3 Decision status

- `ADR-0001` remains Accepted: APES is a vendor-neutral documentation and standards repository; tooling remains deferred and separate.
- `ADR-0002` is **Accepted** as of 2026-08-07: schema-first, file-native, Git-backed contracts; deterministic read-only tooling later; generated agent adapters; no model runtime in core.
- Foundation 0.2 completed the documentation and reference-research work; Foundation 0.3 executes only F1 Contract Prototype.
- No CLI, schema file, engine, workflow file, adapter, website, build pipeline, application source, dependency, file move, release, commit, or push is produced by Foundation 0.2.
- Foundation 0.3 adds the contract schema and fixtures but no CLI, engine, production dependency, workflow, adapter, website, build pipeline, application source, or file move.
- F2 is implemented in the separate `APES-Validator` repository under accepted ADR-0003. The first independent review requested changes; commit `73bbe6e` addresses all thirteen findings and follow-up `9d58a9f` adds resource/path hardening. Independent re-review is pending; F3 remains unstarted.
- Sprint 2 remains `In Review`; the Research Gate remains `RESEARCH AGAIN`.

### 28.4 Foundation 0.2 cross-references

- [`research/competitors/open-source-reference-comparison.md`](../research/competitors/open-source-reference-comparison.md) — detailed functions, architectures, technology stacks, and APES-oriented trade-offs.
- [`research/source-register.md`](../research/source-register.md) — SRC-025, SRC-026, SRC-053, and SRC-054.
- [`research/notes/search-log.md`](../research/notes/search-log.md) — SE-032 through SE-036.
- [`governance/adr/ADR-0002-schema-first-reference-architecture.md`](../governance/adr/ADR-0002-schema-first-reference-architecture.md) — accepted long-term decision.
- [`tasks/foundation-0-2-open-source-reference-architecture.md`](../tasks/foundation-0-2-open-source-reference-architecture.md) — Foundation 0.2 task record.
- [`schemas/artifact-metadata.schema.json`](../schemas/artifact-metadata.schema.json) — F1 common artifact metadata contract.
- [`schemas/compatibility-mapping.md`](../schemas/compatibility-mapping.md) — representative mapping from existing APES artifacts.
- [`tasks/foundation-0-3-contract-prototype.md`](../tasks/foundation-0-3-contract-prototype.md) — Foundation 0.3 / F1 implementation task.
- [`governance/adr/ADR-0003-f2-read-only-validator-runtime.md`](../governance/adr/ADR-0003-f2-read-only-validator-runtime.md) — accepted F2 runtime and repository-boundary decision.
- [`tasks/implementation-f2-read-only-validator.md`](../tasks/implementation-f2-read-only-validator.md) — F2 implementation and verification record.
- [`governance/decisions/2026-08-09-f2-remediation-evidence.md`](../governance/decisions/2026-08-09-f2-remediation-evidence.md) — exact remediation snapshot, finding dispositions, hashes, and re-review boundary.

---

**End of Foundation 0.2 reference architecture, updated through Foundation 0.3 / F1 and Implementation F2 status.** Sections 24–28 remain the staged architecture; F1 supplies the canonical contract and the separately governed F2 runtime consumes it without moving canonical Markdown.
