# Open-Source Reference Comparison for the APES Implementation Architecture

- Status: Draft
- Version: v0.1
- Owner: APES Maintainers
- Last Updated: 2026-08-05
- Type: Research
- Purpose: Compare four adjacent open-source projects and extract evidence-backed implementation patterns for the APES Repository Evolution Plan.

> **Scope.** Foundation 0.2 reference research only. This document compares observable functions, repository architecture, and technology choices. Strengths, limitations, and APES fit are explicitly labeled as inferences. It does not claim market leadership, adoption, or independent outcome effectiveness. It does not change Sprint 2's `In Review` status or the Research Gate (`RESEARCH AGAIN`).

## Table of Contents

- [Method and Evidence Boundary](#method-and-evidence-boundary)
- [Why These Four Projects](#why-these-four-projects)
- [Functional Comparison](#functional-comparison)
- [Architecture and Technology Comparison](#architecture-and-technology-comparison)
- [Project-by-Project Assessment](#project-by-project-assessment)
- [Cross-Project Patterns](#cross-project-patterns)
- [Implications for APES](#implications-for-apes)
- [Sources and Access Date](#sources-and-access-date)
- [Cross-References](#cross-references)

## Method and Evidence Boundary

The comparison used canonical GitHub repository pages and raw repository files accessed on **2026-08-05**. The evidence pass inspected README files, package manifests, workflow documentation, command definitions, configuration, and installer scripts. Exact star, fork, contributor, and integration counts are intentionally omitted because they are time-sensitive and are not needed for the architecture decision.

The GitHub CLI route was attempted first, as recorded in `SE-032`, but returned no data because the local token was invalid and sandboxed API access was blocked. No GitHub credential was changed. `SE-033` through `SE-036` record the successful public GitHub evidence pass.

Interpretation rules:

- **Observed** means directly present in a canonical repository file and cites `SRC-NNN`.
- **Inference** means an APES-oriented trade-off derived from the observed design; it is not a claim made by the referenced project.
- **Unknown** means the inspected files did not support a conclusion.
- Project self-description is evidence of intended behavior, not independent evidence that the method improves delivery outcomes.

## Why These Four Projects

The sample covers four distinct implementation patterns adjacent to APES:

| Project | Pattern represented | Selection reason |
| --- | --- | --- |
| GitHub Spec Kit | Extensible spec-driven toolchain | Demonstrates a portable CLI, Markdown artifact pipeline, agent adapters, presets, extensions, workflows, and bundles. `SRC-025` |
| OpenSpec | Lightweight change-package workflow | Demonstrates a compact brownfield-oriented proposal/spec/design/tasks envelope and archive flow. `SRC-026` |
| BMAD-METHOD | Full-lifecycle role and workflow system | Demonstrates analysis, planning, architecture, implementation, readiness gates, reviews, and progressive context artifacts. `SRC-053` |
| Agent OS | Standards index and selective context projection | Demonstrates discovery of repository conventions, a standards index, profile inheritance, spec shaping, and agent-specific command projection. `SRC-054` |

Spec Kit and OpenSpec were already present in the APES source register. BMAD-METHOD and Agent OS were added because they expose lifecycle and standards-injection patterns that the earlier two do not cover.

## Functional Comparison

The values below describe the inspected core project, not every community extension.

| Capability | Spec Kit | OpenSpec | BMAD-METHOD | Agent OS |
| --- | --- | --- | --- | --- |
| Up-front principles / standards | Project constitution is a core artifact. `SRC-025` | Requirements and scenarios are central; a separate constitution was not observed in the inspected core flow. `SRC-026` | Project context and explicit architecture decisions guide later work. `SRC-053` | Discovers, indexes, and injects codebase standards. `SRC-054` |
| Discovery / research | Core flow begins at specification; richer discovery can be added through extensions. `SRC-025` | `explore` supports pre-proposal investigation but no Source Register-style evidence chain was observed. `SRC-026` | Analysis phase includes brainstorming, deep research, briefs, and PRFAQ artifacts. `SRC-053` | Spec shaping can inspect product context and reference implementations; formal external research governance was not observed. `SRC-054` |
| Product / requirements planning | Specify, clarify, plan, and task generation. `SRC-025` | Proposal, requirements/scenarios, design, and tasks. `SRC-026` | PRD, UX, canonical SPEC, architecture, epics, stories, and sprint planning. `SRC-053` | Product context plus shaped plan, standards, references, and implementation tasks. `SRC-054` |
| Architecture decisions | Technical plan and customizable governance templates. `SRC-025` | `design.md` is part of a change package. `SRC-026` | A dedicated architecture workflow produces an architecture spine. `SRC-053` | Architecture can be captured in product context and the shaped plan; no independent ADR mechanism was observed. `SRC-054` |
| Implementation dispatch | Core implement command plus convergent and extension workflows. `SRC-025` | Apply executes the approved task package. `SRC-026` | Build, auto-build, code review, correction, and retrospective workflows. `SRC-053` | Produces an implementation plan; execution is delegated to the host coding agent. `SRC-054` |
| Quality gates | Analyze and checklist commands check cross-artifact consistency and requirements quality. `SRC-025` | Human review before code and archive lifecycle are explicit; the inspected core description did not show an evidence audit system. `SRC-026` | Readiness result, code review, sprint status, and evidence-based retrospective are explicit. `SRC-053` | Repeated human confirmation is embedded in discovery and shaping commands. `SRC-054` |
| Cross-agent portability | Multiple integrations plus a generic escape hatch; agent files are projections. `SRC-025` | Skills and generated assistant integrations are part of the repository. `SRC-026` | Workflows can run through supported tool skills or loaded agents. `SRC-053` | README claims multiple tools; the inspected installer projects commands to `.claude/commands/agent-os/`, demonstrating an adapter-specific path. `SRC-054` |
| Formal citation / evidence traceability | No Source Register / verification-log equivalent was observed in the core flow. `SRC-025` | No Source Register / verification-log equivalent was observed in the core flow. `SRC-026` | Deep research is described as verified and cited, but no repository-wide source-ID contract equivalent to APES was observed in the inspected files. `SRC-053` | Reference pointers are recorded in shaped specs, but no source-verification registry was observed. `SRC-054` |

## Architecture and Technology Comparison

| Project | Observable architecture | Technology stack | Distribution model |
| --- | --- | --- | --- |
| Spec Kit | Python CLI; packaged core templates and command assets; project-local `.specify` state; priority-ordered local overrides, presets, extensions, and core templates; installable workflows and bundles. `SRC-025` | Python 3.11+, Typer, Click, Rich, PyYAML, JSON5, Hatchling, pytest; bundled Bash, PowerShell, and Python scripts; Markdown and YAML/JSON assets. `SRC-025` | `uv` / PyPI CLI with offline core assets and project initialization. `SRC-025` |
| OpenSpec | Node CLI; canonical `openspec/` specifications plus change directories containing proposal, specs, design, and tasks; archive flow; optional cross-repository Store. `SRC-026` | Node.js 20.19+, TypeScript ESM, pnpm, Commander, Inquirer, YAML, Zod, Vitest, ESLint. `SRC-026` | npm package with CLI binary, compiled `dist`, schemas, and post-install behavior. `SRC-026` |
| BMAD-METHOD | Modular skills / agents / workflows; progressive phase artifacts; Node installer and bundler; project context passed across phases; documentation site and extensive validators. `SRC-053` | Node.js 20.12+, JavaScript, YAML, Markdown, selected Python 3.11 helper scripts, Commander, js-yaml, Astro / Starlight, ESLint, Markdownlint, Jest and custom test scripts. `SRC-053` | npm CLI / installer that installs selected modules and agent-facing assets. `SRC-053` |
| Agent OS | Markdown command set; repository-local `agent-os/standards/` with `index.yml`; profiles with optional inheritance; shell installer; timestamped spec folders; command projection into a host-agent directory. `SRC-054` | Shell scripts, Markdown, YAML; no application package manifest or service runtime was observed in the inspected repository. `SRC-054` | Repository / shell-script installation into an existing project and agent command directory. `SRC-054` |

## Project-by-Project Assessment

The following strengths and limitations are **APES-oriented inferences**, not independent product reviews.

### GitHub Spec Kit

Observed design: a structured Constitution → Specify → Plan → Tasks → Implement artifact chain with optional Clarify, Analyze, and Checklist controls; a Python CLI projects templates and commands into many agent environments; extensions, presets, workflows, and bundles compose behavior. `SRC-025`

Inferred strengths:

- The strongest reference for separating a stable core from integrations and organization-specific customization.
- Offline-packaged templates and cross-platform scripts are a practical model for reproducibility.
- Project-local overrides and priority ordering make customization explicit instead of encouraging edits to canonical core files.

Inferred limitations for APES:

- The core lifecycle starts after much of APES's research, evidence registration, and product-discovery work.
- The extension / preset / workflow / bundle surface is too large to adopt during APES's documentation-first stage.
- A CLI-first implementation now would conflict with ADR-0001 and the current repository scope.

APES takeaway: adopt the **core-versus-projection boundary**, versioned composition contracts, and offline determinism later; do not copy the current ecosystem breadth.

### OpenSpec

Observed design: an artifact-guided Explore → Propose → Apply → Archive lifecycle. A change directory holds `proposal.md`, requirement specs, `design.md`, and `tasks.md`; cross-repository Stores are available but described as beta. `SRC-026`

Inferred strengths:

- The change package is easy to review, diff, archive, and relate to implementation.
- Requirements and concrete scenarios remain plain Markdown, lowering authoring friction.
- Brownfield changes are a first-class use case instead of an afterthought.

Inferred limitations for APES:

- The change envelope is narrower than APES's research → evidence → decision → standard → validation lifecycle.
- Node / post-install runtime behavior would add operational and supply-chain surface before APES has validated its contracts.
- A cross-repository Store adds coordination value but introduces another source-of-truth decision that APES has not yet earned.

APES takeaway: adopt an **append-only change package** and archive lifecycle, but keep Git as the only source of truth and add evidence / decision links to every package.

### BMAD-METHOD

Observed design: four progressive phases (Analysis, Planning, Solutioning, Implementation), specialized skills and agents, context artifacts passed between phases, readiness gates, code review, sprint state, and retrospective outputs. `SRC-053`

Inferred strengths:

- Closest functional coverage to APES's product-to-engineering lifecycle.
- Makes artifact handoffs and implementation readiness explicit.
- Provides both a quick path and a deeper path, avoiding a single ceremony level for every change.

Inferred limitations for APES:

- The large role, agent, module, and workflow surface can increase context cost and governance burden.
- Workflow breadth risks turning APES into an agent framework rather than a vendor-neutral standard.
- The Node installer and documentation site exceed the current repository's approved implementation scope.

APES takeaway: adopt **progressive context, readiness gates, and scalable workflow depth**; keep roles abstract and avoid mandatory agent personas.

### Agent OS

Observed design: discover repository patterns, confirm them with the user, write concise standards, index those standards, inject only relevant standards, and shape feature specs with product context and reference implementations. YAML profiles can inherit from one another; shell scripts install commands and standards into a project. `SRC-054`

Inferred strengths:

- The indexed, selective-injection approach directly addresses context-window cost.
- Human confirmation before creating or injecting standards reduces silent policy drift.
- Markdown / YAML / shell keep the system lightweight and inspectable.

Inferred limitations for APES:

- The inspected installer is coupled to a `.claude/commands/` projection path even though the conceptual model is broader.
- Shell-first installation is less uniform on Windows than a portable runtime.
- Extracting existing patterns can preserve local mistakes unless evidence and review gates sit above discovery.

APES takeaway: adopt a **standards index and selective projection**, but make adapters generated and non-canonical, require evidence links, and provide a portable read-only validator before any installer.

## Cross-Project Patterns

The following patterns are observed across at least two projects:

1. **Markdown is the durable interchange format.** All four projects use Markdown as a primary human- and agent-readable artifact. `SRC-025`, `SRC-026`, `SRC-053`, `SRC-054`
2. **Structured sidecars make Markdown operational.** YAML / JSON manifests, indexes, schemas, or package metadata provide machine-readable structure around the prose. `SRC-025`, `SRC-026`, `SRC-053`, `SRC-054`
3. **Artifacts carry context forward.** Spec Kit, OpenSpec, and BMAD explicitly feed one phase's documents into the next; Agent OS writes standards and references into each shaped spec. `SRC-025`, `SRC-026`, `SRC-053`, `SRC-054`
4. **Agent integration is a projection concern.** The canonical process is expressed as templates / skills / workflows, then installed into agent-specific locations. `SRC-025`, `SRC-026`, `SRC-053`, `SRC-054`
5. **A small path and a deep path both matter.** OpenSpec emphasizes lightweight iteration; BMAD exposes quick and full tracks; Spec Kit allows step-by-step or workflow execution. `SRC-025`, `SRC-026`, `SRC-053`
6. **None of the inspected cores provides APES's full evidence chain.** No direct equivalent of Source Register → Verification Log → Coverage → Audit → ADR / Standard was observed. This is an APES comparison finding, limited to the inspected core files. `SRC-025`, `SRC-026`, `SRC-053`, `SRC-054`

## Implications for APES

APES should combine the strongest patterns without becoming another coding-agent framework:

- From **Spec Kit**: stable core contracts, project-local overrides, versioned composition, offline-first packaging, and agent adapters.
- From **OpenSpec**: one reviewable change envelope with proposal, evidence impact, design, tasks, and archive status.
- From **BMAD-METHOD**: progressive lifecycle artifacts, explicit readiness gates, and proportional workflow depth.
- From **Agent OS**: a standards index and selective context projection.
- Retain APES's differentiator: every external claim, architectural decision, standard rule, and release gate remains traceable through Source IDs, decision records, and reproducible audits.

This synthesis supports the schema-first, file-native reference architecture proposed in `ADR-0002` and sections 24–28 of the Repository Evolution Plan. It does **not** authorize runtime implementation. The next implementation gate is acceptance of the ADR plus a separately scoped Foundation sprint.

## Sources and Access Date

| Source ID | Canonical repository | Primary files inspected | Access date |
| --- | --- | --- | --- |
| SRC-025 | https://github.com/github/spec-kit | `README.md`, `pyproject.toml`, repository tree | 2026-08-05 |
| SRC-026 | https://github.com/Fission-AI/OpenSpec | `README.md`, `package.json`, repository tree | 2026-08-05 |
| SRC-053 | https://github.com/bmad-code-org/BMAD-METHOD | `README.md`, `docs/reference/workflow-map.md`, `package.json`, repository tree | 2026-08-05 |
| SRC-054 | https://github.com/buildermethods/agent-os | `README.md`, `config.yml`, `commands/agent-os/*.md`, `scripts/project-install.sh`, repository tree | 2026-08-05 |

## Cross-References

- [`../source-register.md`](../source-register.md) — canonical source rows and current verification statistics.
- [`../notes/search-log.md`](../notes/search-log.md) — SE-032 through SE-036 search and access record.
- [`candidate-projects.md`](candidate-projects.md) — earlier Sprint 2 candidate set; unchanged by this comparison.
- [`reverse-research.md`](reverse-research.md) — earlier detailed research for Spec Kit and OpenSpec; unchanged by this comparison.
- [`../../docs/repository-evolution-plan.md`](../../docs/repository-evolution-plan.md) — updated technical plan and staged implementation proposal.
- [`../../governance/adr/ADR-0002-schema-first-reference-architecture.md`](../../governance/adr/ADR-0002-schema-first-reference-architecture.md) — proposed architecture decision.
- [`../../tasks/foundation-0-2-open-source-reference-architecture.md`](../../tasks/foundation-0-2-open-source-reference-architecture.md) — Foundation 0.2 task record.
