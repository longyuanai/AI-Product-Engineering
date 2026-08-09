# Design 01 — Repository Architecture

- Status: Draft
- Version: v0.2.1
- Owner: APES Maintainers
- Last Updated: 2026-08-09
- Purpose: Record the architecture choices for the APES repository foundation.

## Table of Contents

- [Repository Positioning](#repository-positioning)
- [Top-Level Layout](#top-level-layout)
- [Top-Level Directory Responsibilities](#top-level-directory-responsibilities)
- [Relationship Between Standards, Protocols, Templates, Commands, and Examples](#relationship-between-standards-protocols-templates-commands-and-examples)
- [Why No CLI, MCP Server, Website, or VS Code Extension Yet](#why-no-cli-mcp-server-website-or-vs-code-extension-yet)
- [Known Limitations](#known-limitations)
- [Extension Policy](#extension-policy)

## Repository Positioning

This repository is the canonical home for the AI Product Engineering Standard (APES) and the supporting documentation, research notes, decision records, and worked examples that surround it. It is not a product, not a tool, and not an application. It is a **documentation and standard repository**.

## Top-Level Layout

```
AI-Product-Engineering/
├── README.md
├── AGENTS.md
├── LICENSE
├── CHANGELOG.md
├── ROADMAP.md
├── VISION.md
├── MANIFESTO.md
├── CONTRIBUTING.md
├── CODE_OF_CONDUCT.md
│
├── .github/
│   ├── ISSUE_TEMPLATE/
│   └── workflows/
│
├── docs/                 # Reader-facing documentation
├── standards/            # The standard itself (one subdirectory per stage)
├── protocols/            # How people (and agents) work day-to-day
├── templates/            # Reusable artifact templates
├── commands/             # Standardized instructions for agents and humans
├── checklists/           # Stage-gate and quality checklists
├── research/             # Ecosystem, competitor, paper, and free-form notes
├── examples/             # Worked examples showing APES in practice
├── governance/           # ADRs, RFCs, decision notes
├── schemas/              # Language-neutral artifact contracts and fixtures
├── design/               # Design documents (this file lives here)
├── tasks/                # Sprint and task definitions
├── sessions/             # Session logs
├── assets/               # Diagrams and other media
├── scripts/              # Repository utility scripts (not application code)
└── website/              # Placeholder only — implementation deferred
```

## Top-Level Directory Responsibilities

| Directory | Responsibility |
| --- | --- |
| Root docs (`README.md`, `VISION.md`, `MANIFESTO.md`, `ROADMAP.md`, `CONTRIBUTING.md`, `CODE_OF_CONDUCT.md`, `AGENTS.md`, `CHANGELOG.md`, `LICENSE`) | Project identity, contributor guidance, change log. |
| `docs/` | Reader-facing explanations: lifecycle, gates, maturity, glossary, FAQ, getting started. |
| `standards/` | The APES standard itself, organized by lifecycle stage. Each subdirectory corresponds to one stage. |
| `protocols/` | Day-to-day operational protocols (review, handoff, sprint rituals). Complements standards. |
| `templates/` | Reusable document templates aligned with standard artifacts. |
| `commands/` | Standardized instructions for AI agents and humans. |
| `checklists/` | Quality and stage-gate checklists. |
| `research/` | Citable research notes: ecosystem, competitors, papers, free-form observations. |
| `examples/` | Worked, validated examples of APES in practice. |
| `governance/` | Append-only decision records (ADRs, RFCs, decision notes). |
| `schemas/` | Language-neutral artifact contracts and compatibility fixtures; no runtime tooling. |
| `design/` | Architecture and design documents for APES and its repository. |
| `tasks/` | Sprint and task definitions. |
| `sessions/` | Dated session logs. |
| `assets/` | Diagrams and media. |
| `scripts/` | Repository maintenance scripts (not product code). |
| `website/` | Placeholder for a future public site. Empty by design. |

## Relationship Between Standards, Protocols, Templates, Commands, and Examples

- **Standards** define *what must be true* at the end of a stage (outputs, evidence, criteria).
- **Protocols** define *how* a stage operates day-to-day (rituals, review channels, handoffs).
- **Templates** give teams a starting point for the artifacts a standard requires.
- **Commands** are short, standardized instructions — for AI agents and humans — that can be replayed safely.
- **Examples** show the standard, protocol, template, and command set in action against a real project, including where they fall short.

The strict order is: standards set the bar → protocols operationalize → templates accelerate → commands automate → examples validate.

## Why No CLI, MCP Server, Website, or VS Code Extension Yet

The following are explicitly out of scope at the v0.1 stage:

- A CLI tool built from this repository.
- An MCP server built from this repository.
- A VS Code extension built from this repository.
- A built-and-deployed website.

Reasons:

1. **Standard before tooling.** APES has not yet been validated against enough real projects to know which commands and workflows are worth automating. Tooling based on a young standard will encode its current weaknesses.
2. **Vendor neutrality.** A owned CLI, MCP server, or editor extension would push the project toward a specific runtime, a specific model, and a specific editor — undermining neutrality.
3. **Maintenance cost.** Each tool creates a long-term support obligation that the current maintainer base cannot yet justify.
4. **Separation of concerns.** Tools that wrap APES should live in their own repositories, each with its own RFC, ADR, and contributing community.

F2 validates this boundary: the read-only `APES-Validator` runtime lives in an independent sibling Git repository under accepted [`ADR-0003`](../governance/adr/ADR-0003-f2-read-only-validator-runtime.md). This repository still contains contracts rather than runtime application source.

The placeholder directories (`scripts/`, `website/`, the implied absence of `cli/`, `mcp/`, `vscode/`) make the boundary visible and easy to challenge later.

## Known Limitations

- No module under `standards/` has content yet. The standard is structurally complete but substantively empty.
- No real case study has been published. Every example in this v0.1 is hypothetical.
- The maturity model is only stubbed. Adoption assessment is not yet reliable.
- The F2 validator provides deterministic local-link and anchor checks, but it is not yet wired into this repository's CI; no Markdown lint rule has been pinned and the CI workflow still defers linting behind a TODO.
- License has not been chosen by maintainers. This is intentionally a placeholder.

## Extension Policy

This architecture may grow, but only when:

1. A real project or a bounded compatibility prototype demonstrates the structural need.
2. The proposed extension has been captured as an ADR (for repo-structure changes) or an RFC (for standard-level changes).
3. The extension has been reviewed against the five Manifesto principles in [`../MANIFESTO.md`](../MANIFESTO.md).

Foundation 0.3 adds `schemas/` under accepted [`ADR-0002`](../governance/adr/ADR-0002-schema-first-reference-architecture.md) and its separately approved [F1 task](../tasks/foundation-0-3-contract-prototype.md). The repository layout in this document remains the contract; later runtime tooling remains outside this repository unless a future accepted decision changes that boundary.
