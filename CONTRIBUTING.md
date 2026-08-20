# Contributing

- Status: Draft
- Version: v0.1
- Owner: APES Maintainers
- Last Updated: 2026-08-03
- Purpose: Define how to contribute to APES.

## Table of Contents

- [Before You Start](#before-you-start)
- [Small Changes](#small-changes)
- [Standard-Level Changes](#standard-level-changes)
- [Architectural Decisions](#architectural-decisions)
- [Pull Request Rules](#pull-request-rules)
- [What We Do Not Accept](#what-we-do-not-accept)
- [Review Process](#review-process)
- [Contribution License](#contribution-license)

## Before You Start

- Search existing issues and discussions to avoid duplicates.
- Read [`MANIFESTO.md`](MANIFESTO.md) and the relevant module under [`standards/`](standards/README.md).
- For large or controversial changes, open an issue or discussion first.

## Small Changes

- Typos, clarifications, broken links, and minor wording fixes can go straight to a Pull Request.
- Use the [PR template](.github/PULL_REQUEST_TEMPLATE.md).

## Standard-Level Changes

Changes that alter a lifecycle stage, define a new stage, or modify a gate require a **Request for Comments (RFC)** in [`governance/rfc/`](governance/rfc/README.md).

The RFC must include:

- The current problem and the evidence supporting it.
- The proposed change and its rationale.
- The impact on existing modules and existing case studies.
- A migration or compatibility plan.

## Architectural Decisions

Cross-cutting repository decisions — directory layout, tooling, scope boundaries, contributor governance — require an **Architecture Decision Record (ADR)** in [`governance/adr/`](governance/adr/README.md).

ADRs are written in append-only form. A new ADR can supersede a previous one but cannot rewrite history.

## Pull Request Rules

Every Pull Request must state:

- **What** was changed.
- **Why** the change was needed (with evidence or an issue link).
- **Impact** on existing modules, templates, or tooling.
- **Verification** steps you ran locally.
- **Risks** and rollback plan if applicable.

## What We Do Not Accept

- Market claims without a citation and access date.
- "Works on my machine" assertions as a substitute for evidence.
- Claims of standardized adoption that cannot be verified.
- Any change that conceals uncertainty or pretends a hypothesis is a fact.

## Review Process

1. A maintainer triages the PR within a reasonable window.
2. Domain reviewers are assigned based on the affected stage.
3. The PR is merged once consensus is reached and required checks pass.
4. Any meaningful change is reflected in [`CHANGELOG.md`](CHANGELOG.md).

## Contribution License

APES is licensed under the [Apache License 2.0](LICENSE), SPDX identifier `Apache-2.0`. Unless you explicitly state otherwise, a contribution intentionally submitted for inclusion in this repository is provided under the same terms, consistent with section 5 of the license.

Third-party material retains its original copyright, license, and attribution requirements. Contributors must identify such material and its provenance rather than assuming the repository license relicenses it. This project guidance is not legal advice; contributors remain responsible for rights they grant and material they submit.
