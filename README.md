# AI Product Engineering

- Status: Draft
- Version: v0.1
- Owner: APES Maintainers
- Last Updated: 2026-08-03
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

## What is APES

AI Product Engineering Standard (APES) is a vendor-neutral, evidence-driven framework that covers the full AI product journey — from idea discovery through launch and retrospective.

## Current Status

APES is an **early draft (v0.1)**. The standard has not been validated against multiple real projects yet. Treat all content as proposal-stage, not as established practice.

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
