# Sprint 00 — Repository Foundation

- Status: Completed
- Version: v0.1
- Owner: APES Maintainers
- Last Updated: 2026-08-03

## Table of Contents

- [Sprint Goal](#sprint-goal)
- [Scope](#scope)
- [Out of Scope](#out-of-scope)
- [Tasks](#tasks)
- [Acceptance Criteria](#acceptance-criteria)
- [Verification](#verification)
- [Notes](#notes)
- [Final Status](#final-status)

## Sprint Goal

Establish the APES repository foundation: structure, identity documents, governance scaffolding, GitHub integration, and a placeholder for every future module. No module standard is written in this sprint.

## Scope

In scope:

- Top-level directory layout per the sprint brief.
- Root identity files: `README.md`, `AGENTS.md`, `VISION.md`, `MANIFESTO.md`, `ROADMAP.md`, `CONTRIBUTING.md`, `CODE_OF_CONDUCT.md`, `CHANGELOG.md`, `LICENSE` (placeholder).
- `docs/` reader-facing documentation (placeholders).
- `standards/` placeholder README per module (no standard body).
- `protocols/`, `templates/`, `commands/`, `checklists/`, `research/`, `examples/`, `sessions/`, `assets/`, `scripts/`, `website/` placeholder READMEs.
- `governance/` with first ADR (`ADR-0001-project-positioning`) and adr/rfc/decisions scaffolding.
- `design/01-repository-architecture.md` Draft document.
- `.github/ISSUE_TEMPLATE/` (bug, feature, standard-proposal) and `.github/PULL_REQUEST_TEMPLATE.md`.
- `.github/workflows/markdown-check.yml` draft (no unverified third-party actions).

## Out of Scope

The following are explicitly forbidden this sprint and were not attempted:

- Any ecosystem, competitor, or paper research.
- Body text for any `standards/*` module (including Discovery, Research, Validation, Product, Business, Engineering, Growth, Knowledge).
- Any CLI, MCP server, VS Code extension, or website implementation.
- Any git commit or push to remote.
- Any deletion or reset of existing files.
- Rewriting any existing user-authored content.

## Tasks

- [x] Pre-execution checks: confirm working directory and absence of protected files.
- [x] Create full directory tree per the sprint spec.
- [x] Write root identity files (README, AGENTS, VISION, MANIFESTO, ROADMAP, CONTRIBUTING, CODE_OF_CONDUCT, CHANGELOG, LICENSE placeholder).
- [x] Write `docs/` content and table-of-contents files.
- [x] Write `standards/` README and per-module placeholder.
- [x] Write placeholder READMEs in `protocols/`, `templates/`, `commands/`, `checklists/`, `research/`, `examples/`, `sessions/`, `assets/`, `scripts/`, `website/`.
- [x] Write `governance/` structure and `ADR-0001-project-positioning.md`.
- [x] Write `design/01-repository-architecture.md` Draft.
- [x] Write `.github/ISSUE_TEMPLATE/` (bug, feature, standard-proposal) and PR template.
- [x] Write `.github/workflows/markdown-check.yml` draft (no unverified third-party actions).
- [x] Run verification: directory tree, file existence checks, Markdown spot-check, YAML indentation check, no application source code observed.

## Acceptance Criteria

- Every directory listed in the spec exists.
- Every file listed in the spec exists and is non-empty.
- `LICENSE` makes clear that license selection is pending maintainer decision.
- `ADR-0001-project-positioning.md` records the four positioning decisions listed in the spec, plus at least three alternatives considered.
- `design/01-repository-architecture.md` records repository positioning, directory responsibilities, standards-vs-protocol relationships, the deferral rationale for CLI/MCP/VS Code/website, known limitations, and an extension policy.
- `.github/workflows/markdown-check.yml` does not introduce unverified third-party actions and does not auto-fix files. The remaining lint step is left as a TODO, called out in the file.
- No file claims a finished standard; every module under `standards/` is explicitly Placeholder.
- No application code, dependency directory, or build artifact was produced.

## Verification

The following checks were run as part of the sprint:

- Working directory confirmed to be the `AI-Product-Engineering` repository root before any change.
- Directory tree printed after creation to confirm coverage of required structure.
- File existence check for every file listed in the sprint spec.
- Spot-check of relative Markdown links from `README.md` to top-level destinations.
- YAML file inspected by reading the full content back to confirm indentation and the absence of unknown action references.
- No `src/`, `dist/`, `build/`, `node_modules/`, or application file observed in the resulting tree.

Verification details are summarized in the agent's completion report.

## Notes

- A `LICENSE` placeholder is included because no license was present in the repository and the spec forbids guessing commercial intent.
- A formal Code of Conduct will be adopted in a later sprint; this sprint only added a placeholder.
- Sprint 0 does not commit any git history (the repository has not yet been initialized as a git repo). A git init step is deferred to maintainer decision.

## Final Status

**Completed** for the items listed in [Tasks](#tasks) above. Items left intentionally open (license, code of conduct, git initialization, MD lint action choice) are tracked in the agent's "Open Decisions" report.