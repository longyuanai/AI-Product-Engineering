# Foundation 0.2 — Open-Source Reference Architecture

- Status: Completed
- Version: v0.1
- Owner: APES Maintainers
- Last Updated: 2026-08-05
- Purpose: Compare adjacent open-source implementations and convert the Repository Evolution Plan into a staged, documentation-only implementation proposal.

## Table of Contents

- [Goal](#goal)
- [Inputs](#inputs)
- [Outputs](#outputs)
- [Scope](#scope)
- [Out of Scope](#out-of-scope)
- [Work Completed](#work-completed)
- [Acceptance Criteria](#acceptance-criteria)
- [Verification](#verification)
- [Remaining Decisions](#remaining-decisions)
- [Status](#status)
- [Cross-References](#cross-references)

## Goal

Provide an evidence-backed technical implementation proposal for APES by comparing several similar open-source projects across function, architecture, technology stack, strengths, and limitations, while preserving ADR-0001 and the repository's documentation-first boundary.

## Inputs

- `AGENTS.md` — repository collaboration and scope rules.
- `docs/repository-evolution-plan.md` v0.2 — Foundation 0.1 / 0.1.1 architecture baseline.
- `design/01-repository-architecture.md` — repository layout and deferred-tooling rationale.
- `governance/adr/ADR-0001-project-positioning.md` — vendor-neutral documentation-first positioning.
- `research/research-plan.md` — evidence, source, and claim-discipline rules.
- `research/source-register.md` — existing SRC-025 and SRC-026 rows.
- Canonical GitHub repositories and primary files for Spec Kit, OpenSpec, BMAD-METHOD, and Agent OS, accessed 2026-08-05.

## Outputs

- `research/competitors/open-source-reference-comparison.md` — four-project comparison and APES synthesis.
- `research/source-register.md` — refreshed SRC-025 / SRC-026; added SRC-053 / SRC-054; recomputed current statistics.
- `research/notes/search-log.md` — SE-032 through SE-036, including the failed GitHub CLI route and successful public GitHub evidence pass.
- `docs/repository-evolution-plan.md` v0.3 — sections 24 through 28: comparison, target architecture, stack, phased plan, guardrails and status.
- `governance/adr/ADR-0002-schema-first-reference-architecture.md` — Proposed architecture decision.
- Additive index and CHANGELOG updates required by repository policy.

## Scope

- Direct read-only inspection of canonical GitHub repositories and raw primary files.
- Comparison of observable functions, architecture, technology stack, and distribution model.
- Explicit APES-oriented strengths / limitations as labeled inferences.
- Schema-first, file-native, Git-backed reference architecture.
- Recommended future technology stack and staged implementation gates.
- Security, rollback, compatibility, and vendor-neutral adapter boundaries.
- Documentation, research evidence, ADR, task, index, and CHANGELOG updates only.

## Out of Scope

- No CLI, MCP server, IDE extension, website, build pipeline, application source, runtime engine, schema file, workflow file, adapter, generated command, or release bundle.
- No production dependency or technology-stack change in this repository.
- No database, hosted service, model API, telemetry, remote catalog, or post-install execution.
- No directory move, migration, deletion, overwrite, commit, push, tag, release, or publish action.
- No popularity or adoption ranking; no star / fork / contributor counts.
- No claim that project self-description proves outcome effectiveness.
- No modification of the Sprint 2 short list, Sprint 3 coverage matrix, Sprint 2 `In Review` status, or Research Gate (`RESEARCH AGAIN`).
- No beginning of a runtime implementation sprint; ADR-0002 remains `Proposed`.

## Work Completed

1. Checked `git status` before changes and reviewed existing uncommitted documentation work.
2. Read the current Repository Evolution Plan, Foundation 0.1.1 task, repository design, and ADR-0001 before editing.
3. Attempted the GitHub CLI search route; recorded the invalid local token and sandboxed API failure without changing credentials.
4. Used canonical public GitHub pages and raw repository files to inspect:
   - GitHub Spec Kit (`README.md`, `pyproject.toml`, repository tree).
   - OpenSpec (`README.md`, `package.json`, repository tree).
   - BMAD-METHOD (`README.md`, workflow map, `package.json`, repository tree).
   - Agent OS (`README.md`, `config.yml`, command files, shell installer, repository tree).
5. Separated observed facts from APES-oriented inferences.
6. Updated the source and search records with access date, evidence, limitations, and verification status.
7. Added a comparative research report and translated the synthesis into plan sections 24 through 28.
8. Recorded the cross-cutting architecture decision as Proposed ADR-0002.
9. Updated required indexes and `CHANGELOG.md`.

## Acceptance Criteria

- At least four comparable open-source projects are sourced from canonical GitHub repositories.
- The comparison covers function, architecture, technology stack, strengths, and limitations.
- Every external claim in the comparison references a Source ID.
- Access date and inspected primary files are recorded.
- Observation and inference are clearly separated.
- The implementation proposal defines canonical contracts, logical architecture, stack, phases, gates, rollback, and security constraints.
- The proposal preserves ADR-0001 and creates no runtime code or production dependency.
- ADR-0002 exists with `Proposed` status.
- Sprint 2 remains `In Review`; Research Gate remains `RESEARCH AGAIN`.
- Relevant Markdown links and Table of Contents entries validate.
- `CHANGELOG.md` and task indexes are updated.

## Verification

Required checks:

- `git diff --check`
- Source-ID uniqueness and continuity check for SRC-001 through SRC-054.
- Source-register row count and current reliability / verification totals.
- Relative Markdown link existence check across modified Markdown files.
- Table of Contents anchor check for `docs/repository-evolution-plan.md` and the new comparison / task / ADR files.
- Scope scan confirming no prohibited runtime directories or dependency manifests were created.
- `git status --short` review to distinguish Foundation 0.2 changes from pre-existing work.

Verification executed on 2026-08-05:

- `git diff --check` — passed for tracked changes; only the pre-existing `.gitignore` line-ending warning was emitted.
- Source-register audit — passed: IDs are unique and continuous from SRC-001 through SRC-054; current counts are A=25, B=18, C=9, D=2 and Verified=10, Partially Verified=32, Unverified=12.
- Relative-link check across the ten Foundation 0.2 touched Markdown files — passed.
- Table of Contents anchor check for the plan, comparison, ADR, and task — passed.
- New-file trailing-whitespace and final-newline check — passed for all four Foundation 0.2 new / expanded deliverables.
- Prohibited runtime / build artifact scan — passed; no CLI, MCP, website source, dependency manifest, or workflow pipeline was introduced by Foundation 0.2.

## Remaining Decisions

- Accept, amend, or reject ADR-0002.
- Approve the YAML front matter + JSON Schema contract direction.
- Decide whether the first schema prototype belongs in this repository or a separate tooling repository while it is still documentation-only.
- Select representative existing artifacts for compatibility fixtures.
- Assign an independent reviewer for schema and path-safety rules.
- Decide whether a minimal Python spike is justified after the contract review; no spike is authorized by this task.

## Status

**Completed** for the documentation and research outputs listed above. The verification checks in this task passed on 2026-08-05. ADR-0002 is `Proposed`; implementation has not begun. Sprint 2 remains `In Review`; Research Gate remains `RESEARCH AGAIN`.

## Cross-References

- [`../docs/repository-evolution-plan.md`](../docs/repository-evolution-plan.md) — v0.3 sections 24 through 28.
- [`../research/competitors/open-source-reference-comparison.md`](../research/competitors/open-source-reference-comparison.md) — detailed comparison.
- [`../research/source-register.md`](../research/source-register.md) — SRC-025, SRC-026, SRC-053, SRC-054 and current counts.
- [`../research/notes/search-log.md`](../research/notes/search-log.md) — SE-032 through SE-036.
- [`../governance/adr/ADR-0002-schema-first-reference-architecture.md`](../governance/adr/ADR-0002-schema-first-reference-architecture.md) — Proposed decision.
- [`../governance/adr/ADR-0001-project-positioning.md`](../governance/adr/ADR-0001-project-positioning.md) — preserved scope boundary.
- [`../CHANGELOG.md`](../CHANGELOG.md) — Foundation 0.2 entry.
