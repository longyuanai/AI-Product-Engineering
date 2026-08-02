# Changelog

- Status: Active
- Version: v0.1
- Owner: APES Maintainers
- Last Updated: 2026-08-03
- Purpose: Track notable changes to APES using the Keep a Changelog format.

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/).

## [Unreleased]

### Added — Sprint 1.1: Research Plan Review Fix (2026-08-03)

- Refined the ecosystem research plan after methodology review.
- Added source register, reliability levels, candidate selection, search logging, and kill criteria.
- Corrected Git-status and copyright-handling language.

### Added — Sprint 1: Ecosystem Research Plan (2026-08-03)

- Draft ecosystem research plan in `research/research-plan.md`. Defines research purpose, principles, scope and non-scope, four-phase methodology (Inventory → Coverage Map → Gap Analysis → Positioning Evidence), source categories and sampling, hypotheses under test, evidence-quality criteria, anti-patterns to prevent, file layout, cadence, stop conditions, review governance, and feedback loop into APES decisions.
- New sprint task file `tasks/sprint-01-ecosystem-research-plan.md`.
- Additive pointer to the research plan added in `research/README.md`.
- This CHANGELOG entry.

### Added — Sprint 0: Repository Foundation (2026-08-03)

- Initial repository structure: `docs/`, `standards/`, `protocols/`, `templates/`, `commands/`, `checklists/`, `research/`, `examples/`, `governance/`, `design/`, `tasks/`, `sessions/`, `assets/`, `scripts/`, `website/`.
- Core documents: `README.md`, `VISION.md`, `MANIFESTO.md`, `ROADMAP.md`, `AGENTS.md`, `CONTRIBUTING.md`, `CODE_OF_CONDUCT.md`.
- Placeholder README files for every stage module under `standards/`.
- GitHub templates: bug report, feature request, standard proposal, pull request template.
- Initial GitHub Actions workflow (Markdown check, draft).
- Initial ADR (`ADR-0001-project-positioning`).
- Initial design document (`design/01-repository-architecture.md`).
- Sprint task file (`tasks/sprint-00-repository-foundation.md`).

### Notes

- The plan is a methodology, not a research finding. No claim about ecosystem, market, competitors, or adoption is made.
- Execution of Phases A–D is deferred to a later, separately-scoped sprint.
- No git operations were performed during this sprint.
- License selection remains pending maintainer decision.
- All standard module contents remain placeholders; no module standard has been written yet.
