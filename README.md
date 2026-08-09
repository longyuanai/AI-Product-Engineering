# AI Product Engineering

- Status: Draft
- Version: v0.1
- Owner: APES Maintainers
- Last Updated: 2026-08-10
- Purpose: Project landing page for the AI Product Engineering Standard (APES).

## Table of Contents

- [What is APES](#what-is-apes)
- [Current Status](#current-status)
- [Core Problem](#core-problem)
- [Lifecycle Overview](#lifecycle-overview)
- [Core Principles](#core-principles)
- [Repository Navigation](#repository-navigation)
- [Roadmap](#roadmap)
- [How to Use This Repository](#how-to-use-this-repository)
- [Contributing](#contributing)
- [License](#license)
- [Disclaimer](#disclaimer)
- [Foundation](#foundation)
- [Foundation 0.1.1](#foundation-011)
- [Foundation 0.2](#foundation-02)
- [Foundation 0.3](#foundation-03)
- [Implementation F2](#implementation-f2)

## What is APES

AI Product Engineering Standard (APES) is a vendor-neutral, evidence-driven framework that covers the full AI product journey — from idea discovery through launch and retrospective.

## Current Status

APES is an **early draft (v0.1)**. The standard has not been validated against multiple real projects yet. Treat all content as proposal-stage, not as established practice. F2 Read-Only Validator is implemented and `In Review` in the independent `APES-Validator` repository; ADR-0002 and ADR-0003 are `Accepted`, Sprint 2 remains `In Review`, and the Research Gate remains `RESEARCH AGAIN`.

## Core Problem

AI tools excel at generating code, but they do not provide a complete product-engineering workflow. Most teams can ship code quickly while still missing the discovery, validation, business, and learning loops that turn code into a product.

## Lifecycle Overview

APES organizes work into the following stages. Each stage has its own standards, templates, and checklists in this repository.

1. **Idea** — Capture an opportunity, problem, or hypothesis.
2. **Discovery** — Understand users, problems, and context.
3. **Research** — Investigate technical, market, and ecosystem evidence.
4. **Validation** — Test hypotheses with real users and real data.
5. **Product** — Define scope, requirements, and experience.
6. **Business** — Confirm viability, pricing, and go-to-market fit.
7. **Engineering** — Build the system with evidence-based practice.
8. **Growth** — Acquire, activate, and retain users.
9. **Knowledge** — Capture learnings and feed them back into discovery.

## Core Principles

- Product before code
- Evidence over opinion
- Validation before implementation
- Reuse before reinvent
- Iteration over perfection

These principles are explained in [`MANIFESTO.md`](MANIFESTO.md).

## Repository Navigation

- [`docs/`](docs/README.md) — Public documentation (lifecycle, stage gates, maturity model, glossary, FAQ).
- [`standards/`](standards/README.md) — The standard itself, organized by lifecycle stage.
- [`protocols/`](protocols/README.md) — Collaboration and review protocols.
- [`templates/`](templates/README.md) — Reusable document and artifact templates.
- [`commands/`](commands/README.md) — Standardized instructions for AI agents and humans.
- [`checklists/`](checklists/README.md) — Quality and gate checklists.
- [`research/`](research/README.md) — Ecosystem, competitor, and paper research notes.
- [`examples/`](examples/README.md) — Worked examples showing APES in practice.
- [`governance/`](governance/README.md) — ADRs, RFCs, and decision records.
- [`design/`](design/README.md) — Architecture and design documents for the repository and standard.
- [`tasks/`](tasks/README.md) — Sprint and task definitions.
- [`sessions/`](sessions/README.md) — Session logs and meeting notes.
- [`assets/`](assets/README.md) — Diagrams, images, and other media.
- [`schemas/`](schemas/README.md) — Language-neutral artifact contracts and compatibility fixtures.
- [`scripts/`](scripts/README.md) — Helper scripts for repository operations.
- [`website/`](website/README.md) — Future website source (not yet implemented).

## Roadmap

See [`ROADMAP.md`](ROADMAP.md) for current and planned versions.

Summary:

- **v0.1** — Foundation, research, core standard drafts, one real case study.
- **v0.2** — Templates, checklists, Claude Code / Codex usage guides.
- **v0.5** — More real cases, automated checks.
- **v1.0** — Stable release validated by multiple real projects.

## How to Use This Repository

1. Read [`VISION.md`](VISION.md) to understand the long-term direction.
2. Read [`docs/lifecycle.md`](docs/lifecycle.md) and [`docs/stage-gates.md`](docs/stage-gates.md).
3. Start with the stage relevant to your current work in [`standards/`](standards/README.md).
4. Track work via [`tasks/`](tasks/README.md) and decisions via [`governance/`](governance/README.md).

## Contributing

See [`CONTRIBUTING.md`](CONTRIBUTING.md). All contributions must cite evidence for product, market, or technical claims.

## License

See [`LICENSE`](LICENSE). License selection is pending maintainer decision at this stage.

## Disclaimer

APES does not claim to be an industry standard, and no adoption numbers, user counts, or market position have been verified.

## Foundation

APES is the first project in a planned family of research-driven, evidence-anchored standards. Foundation 0.1 (2026-08-03) defines the long-term repository evolution strategy — the layered model that lets future projects (such as AI Security, IoT Security, Binary Security, and a Research Library) inherit a shared research operating system and a shared standards foundation without rewriting them.

The architecture describes four layers with a strict downward dependency direction:

- **Research OS** — generic research operating system: source register, search log, verification log, coverage map, audit, statistics, reports. Project-agnostic by construction.
- **Standard Foundation** — cross-project commitments: manifesto, evidence policy, lifecycle model, governance framework, compatibility contract. Inherited by every family member.
- **Project Layer** — each project's domain content. APES is the first instance.
- **Release Layer** — tagged snapshots and public bundles.

Foundation 0.1 is **architecture only**. It introduces no implementation, no code, no scripts, no prompt writing, no engines, no new standards, no new templates, no new commands. It documents the shape, the boundary, and the direction. It does not move directories, does not modify research, does not change the Sprint 2 status (`In Review`) or the Research Gate (`RESEARCH AGAIN`). Later Foundation work requires its own scoped task and applicable decision record.

Read the full plan in [`docs/repository-evolution-plan.md`](docs/repository-evolution-plan.md). Read the sprint task file in [`tasks/foundation-0-1-repository-evolution.md`](tasks/foundation-0-1-repository-evolution.md). Foundation 0.1 reaffirms the deferred tooling scope established by [`governance/adr/ADR-0001-project-positioning.md`](governance/adr/ADR-0001-project-positioning.md) — no CLI, no MCP server, no IDE extension, no website at this stage.

## Foundation 0.1.1

Foundation 0.1.1 (2026-08-03) is an **architecture refinement sprint** that strengthens the Repository Evolution Plan into the definitive architectural document for Research OS. Foundation 0.2, Foundation 0.3, Foundation 0.4, Foundation 0.5, Foundation 1.0, and any research sprints (Sprint 4 onward) will reference this document rather than redefining repository architecture.

Seven architectural sections were appended to `docs/repository-evolution-plan.md` (sections 17 through 23). Sections 1 through 16 from Foundation 0.1 are preserved verbatim. One refinement note was appended to section 4.

The seven refinements:

- **Repository Evolution Principles (10 principles).** The philosophical foundation of Research OS. Backward Compatibility First; Research before Design; Evidence before Opinion; Audit before Release; Architecture before Implementation; Shared before Project-specific; Everything Versioned; Everything Traceable; Everything Reproducible; No Hidden Decisions.
- **Repository Layer Model (6 layers).** The 4-layer deployment view (Research OS → Standard Foundation → Project Layer → Release Layer) is preserved; the 6-layer architectural view adds the Meta Layer (principles, governance, decision hierarchy, document taxonomy, maturity model, dependency graph) and the Engine Layer (Source Register, Verification, Coverage, Audit, Statistics, Report engines) as explicit positions. Dependency direction is strictly downward.
- **Repository Lifecycle (9 stages).** Idea → Research → Audit → Architecture → Implementation → Validation → Release → Maintenance → Archive. Foundation 0.1 / 0.1.1 sit at the Architecture stage; Foundation 1.0 is the Release stage candidate.
- **Decision Hierarchy (10 tiers).** Principles → Constitution → RFC → Standard → Schema → Engine → Workflow → Prompt → Project → Sprint. Lower tiers cannot override higher tiers; cross-tier conflicts are resolved via RFC.
- **Document Taxonomy (15 types).** Policy, Constitution, RFC, ADR, Research, Coverage, Gap Analysis, Evidence, Statistics, Report, Task, Prompt, Checklist, Template, Release Notes. Each type carries Purpose, Owner, Lifecycle, and Version policy.
- **Repository Maturity Model (6 levels).** Level 0 Bootstrap → Level 1 Research → Level 2 Standardization → Level 3 Automation → Level 4 Platform → Level 5 Research OS. Current state is Level 1 (post Sprint 3.1); current target is Level 2 (post Foundation 0.1.1).
- **Repository Dependency Graph.** A canonical direction graph: Principles → Constitution → Schemas → Engines → Workflows → Prompts → Research → Coverage → Gap → Release.

Foundation 0.1.1 is **architecture refinement only**. It introduces no implementation, no code, no scripts, no engines, no prompt implementation, no constitution, no standards, no workflow implementation, no directory implementation. It does not modify any research file, does not change the Sprint 2 status (`In Review`), and does not change the Research Gate (`RESEARCH AGAIN`). It does not begin Foundation 0.2.

Read the refined plan in [`docs/repository-evolution-plan.md`](docs/repository-evolution-plan.md). Read the sprint task file in [`tasks/foundation-0-1-1-repository-evolution-upgrade.md`](tasks/foundation-0-1-1-repository-evolution-upgrade.md). The five philosophical principles in [`MANIFESTO.md`](MANIFESTO.md) are distinct from — and consistent with — the ten architectural principles in §17 of the plan.

## Foundation 0.2

Foundation 0.2 (2026-08-05) compared GitHub Spec Kit, OpenSpec, BMAD-METHOD, and Agent OS using canonical repository evidence, then added a documentation-only reference architecture to the Repository Evolution Plan. The current proposal is schema-first, file-native, Git-backed, deterministic, and adapter-driven.

The sprint produced a four-project [reference comparison](research/competitors/open-source-reference-comparison.md), plan sections 24–28, [ADR-0002](governance/adr/ADR-0002-schema-first-reference-architecture.md), and a [Foundation 0.2 task record](tasks/foundation-0-2-open-source-reference-architecture.md). It added no runtime code, schema file, workflow, agent adapter, build pipeline, or production dependency.

ADR-0002 was accepted on 2026-08-07 when the maintainer approved the separately scoped Foundation 0.3 implementation Sprint.

## Foundation 0.3

Foundation 0.3 executes **F1 Contract Prototype** from the staged implementation plan. It adds one JSON Schema 2020-12 contract, four valid fixtures, four intentionally invalid fixtures, and an explicit compatibility mapping for existing APES artifacts.

The prototype keeps existing Markdown canonical and unmoved. It adds no CLI, engine, package manifest, build pipeline, application source, production dependency, workflow, agent adapter, website, or MCP server. The separately governed F2 runtime now consumes this contract without changing the F1 repository boundary.

Read the [schema contract](schemas/artifact-metadata.schema.json), [compatibility mapping](schemas/compatibility-mapping.md), and [Foundation 0.3 task record](tasks/foundation-0-3-contract-prototype.md).

## Implementation F2

F2 (2026-08-09) implements the first deterministic runtime consumer of APES contracts in the independent sibling Git repository `APES-Validator`. Its `check`, `graph`, and `explain` commands validate metadata, fixtures, IDs, references, dependency direction, cycles, local links, anchors, and root-containment boundaries without writing to the inspected repository.

The first independent audit reproduced the automated gates but requested changes. Remediation commit `73bbe6e` and Schema v0.2.0 address all thirteen findings. Implementer self-review follow-up `9d58a9f` adds stricter resource-complexity and pre-resolution path boundaries; the latest snapshot passes 87 tests at 91.20% branch coverage, Ruff, strict mypy, Bandit, package build, dependency audit, and a real APES 103-file hash-preservation check. F2 remains `In Review` pending independent re-review. F3 has not started.

Read [ADR-0003](governance/adr/ADR-0003-f2-read-only-validator-runtime.md), the [F2 task record](tasks/implementation-f2-read-only-validator.md), the [initial review](governance/decisions/2026-08-09-f2-review-evidence.md), the [remediation evidence](governance/decisions/2026-08-09-f2-remediation-evidence.md), and the [independent review checklist](checklists/f2-independent-review.md).
