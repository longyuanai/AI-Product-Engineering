# AGENTS.md

- Status: Draft
- Version: v0.1
- Owner: APES Maintainers
- Last Updated: 2026-08-03
- Purpose: Repository-level rules for AI agents (and humans) collaborating on APES.

## Table of Contents

- [Purpose](#purpose)
- [Rules](#rules)
- [Sprint Discipline](#sprint-discipline)
- [Evidence and Decision Discipline](#evidence-and-decision-discipline)
- [Markdown and Documentation Hygiene](#markdown-and-documentation-hygiene)
- [Scope Boundaries](#scope-boundaries)
- [Completion Reporting](#completion-reporting)

## Purpose

This document defines mandatory collaboration rules for AI agents working in this repository. Humans are encouraged to follow the same rules for consistency.

## Rules

1. **Check `git status` before any change.** Never modify files when there are unrelated user changes present.
2. **Protect existing user work.** Read existing files before editing. Never overwrite meaningful content without explicit instruction.
3. **Stay in the current sprint.** Do not jump to a later sprint or module without explicit maintainer approval.
4. **No silent module expansion.** Do not enter the next module (e.g., Discovery, Research) before its sprint is approved and scoped.
5. **Hypotheses, not facts.** Distinguish clearly between observed evidence and inferred opinion. Never state speculation as fact.
6. **Cited research only.** External research must include source, access date, and the evidence that supports the claim.
7. **Important decisions require an ADR.** Product, business, or architecture decisions with long-term impact must be captured in `governance/adr/`.
8. **Verify Markdown after every change.** Check links and the table of contents before finishing a task.
9. **No fake test passes.** Never claim a test, check, or build passed unless it was actually executed.
10. **Minimum-change principle.** Make the smallest change that satisfies the request. Avoid scope creep.
11. **Current stage is documentation-first.** Do not implement CLI, MCP servers, websites, or VS Code extensions at this stage.
12. **Update tasks and CHANGELOG on completion.** Mark subtasks and add an entry to `CHANGELOG.md` when work completes.

## Sprint Discipline

- Each sprint has its own task file under [`tasks/`](tasks/README.md).
- `Out of Scope` items must not be touched in that sprint.
- If a new need surfaces, surface it as a proposal — do not act on it unilaterally.

## Evidence and Decision Discipline

- Every claim about users, markets, competitors, or adoption must include a citation.
- Every architectural decision with cross-cutting impact must have an ADR.
- RFCs are required for standard-level changes; ADRs are required for repository-level decisions.

## Markdown and Documentation Hygiene

- Use the metadata header defined in the sprint brief for new files.
- Use relative links between files.
- Validate the table of contents after any structural change.

## Scope Boundaries

This repository currently targets documentation and standards. The following are explicitly out of scope at this stage and must not be created:

- CLI tools
- MCP servers
- VS Code extensions
- Website source code (the `website/` directory exists as a placeholder only)
- Build pipelines
- Application source code

## Completion Reporting

When finishing a task, an agent must:

1. Summarize what was done.
2. List files created or modified.
3. Show the commands executed for verification and their results.
4. Flag any decisions still pending human input.
5. Stop. Do not begin the next sprint or module.
