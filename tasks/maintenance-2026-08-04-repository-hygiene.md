# Repository Hygiene — 2026-08-04

- Status: Completed
- Version: v0.1
- Owner: APES Maintainers
- Last Updated: 2026-08-04
- Purpose: Reconcile repository indexes and repair documentation hygiene findings without changing research evidence or architecture.

## Goal

Repair the safe, non-decision findings from the repository audit: stale directory indexes, broken relative links, missing root README Table of Contents entries, and accidental tracking risk for local Claude settings.

## Scope

- Reconcile directory README status text with artifacts that already exist.
- Index Sprint 3, Sprint 3.1, Foundation 0.1, and Foundation 0.1.1 task files.
- Repair known local Markdown links.
- Ignore `.claude/settings.local.json`.
- Define cross-platform UTF-8, LF, and final-newline behavior.
- Record the maintenance change in `CHANGELOG.md`.

## Out of Scope

- License selection.
- New source research or source verification.
- Changing Sprint 2 status or the Research Gate.
- Starting Phase C, Phase D, Foundation 0.2, or another research sprint.
- Operationalizing Foundation-RFC.
- Resolving repository, Foundation, Research OS, or APES version namespaces.
- Adding implementation code, tooling, engines, standards, templates, or commands.
- Git commit, push, tag, or branch creation.

## Corrections

- Root README Table of Contents now includes Disclaimer and Foundation sections.
- `docs/README.md` indexes the Repository Evolution Plan and no longer claims every document is a placeholder.
- `tasks/README.md` indexes completed and in-review Sprint and Foundation task files.
- `research/README.md` and the ecosystem, competitors, and notes indexes reflect existing Draft artifacts.
- Design, governance, and ADR indexes reflect their existing Draft documents.
- Three incorrect relative links in standard-module placeholders are corrected.
- One pseudo-link in the Sprint 3.1 audit record is converted to plain text.
- Local Claude settings are excluded through `.gitignore`.
- `.editorconfig` and `.gitattributes` define consistent text encoding and line-ending behavior without adding a runtime dependency.

## Acceptance Criteria

- All known local Markdown path targets resolve.
- No status index claims that an existing research, coverage, architecture, or ADR artifact does not exist.
- Sprint 2 remains `In Review`.
- Research Gate remains `RESEARCH AGAIN`.
- No research evidence or source status is modified.
- No implementation artifact is added.
- Text-format configuration is present for UTF-8, LF, and final newlines.

## Verification

Run:

- `git status --short --branch`
- `git diff --stat`
- `git diff --check`
- Local Markdown path validation
- Strict UTF-8 decoding check
- Conflict-marker scan

## Remaining Decisions

- License selection.
- Additional primary-source verification required by the Research Gate.
- Foundation-RFC bootstrap and review procedure.
- Version-namespace reconciliation.
- Markdown lint and automated link-check dependency choice.

## Status

Completed for the corrections listed above. This maintenance task does not approve Sprint 2, change the Research Gate, or authorize the next Sprint or Foundation phase.
