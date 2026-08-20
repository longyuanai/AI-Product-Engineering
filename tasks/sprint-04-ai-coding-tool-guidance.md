# Sprint 04 — AI Coding Tool Guidance

- Status: Completed
- Version: v0.1
- Owner: APES Maintainers
- Last Updated: 2026-08-19
- Purpose: Provide a tool-agnostic instruction for running APES lifecycle stages with any AI coding agent, plus worked adaptation examples for OpenAI Codex CLI and Claude Code.

## Table of Contents

- [Goal](#goal)
- [Approval and Inputs](#approval-and-inputs)
- [Scope](#scope)
- [Out of Scope](#out-of-scope)
- [Deliverables](#deliverables)
- [Acceptance Criteria](#acceptance-criteria)
- [Verification](#verification)
- [Rollback](#rollback)
- [Status](#status)

## Goal

Turn the v0.2 "worked examples for Claude Code, Codex" roadmap item into a reviewable, tool-agnostic instruction plus two tool-specific adaptation examples. The standard itself must remain vendor-neutral; tool-specific behavior is documented only as an adapter/projection, never as an endorsement.

## Approval and Inputs

- Maintainer approval: direct instruction in the 2026-08-15 session to implement the tool-agnostic APES usage guidance plus Codex and Claude adaptation examples.
- [`../governance/adr/ADR-0001-project-positioning.md`](../governance/adr/ADR-0001-project-positioning.md) — vendor-neutral scope boundary.
- [`../docs/lifecycle.md`](../docs/lifecycle.md) and [`../docs/stage-gates.md`](../docs/stage-gates.md) — stage and gate definitions.
- [`../ROADMAP.md`](../ROADMAP.md) v0.2 — "Worked examples for Claude Code, Codex".
- [`../research/source-register.md`](../research/source-register.md) — SRC-014 (Claude Code, Verified), SRC-015 (OpenAI Codex CLI, Verified).

## Scope

- One tool-agnostic instruction for running an APES stage with any AI coding agent.
- One worked adaptation example for OpenAI Codex CLI.
- One worked adaptation example for Claude Code.
- Index updates for `commands/` and `examples/`.

## Out of Scope

- Document templates for each lifecycle stage (`templates/`).
- Quality and stage-gate checklists beyond the existing F2 checklist (`checklists/`).
- Glossary and FAQ expansion.
- CLI, MCP server, IDE extension, website, build pipeline, or application source.
- Any claim that a specific tool is endorsed or preferred by APES.

## Deliverables

- [`../commands/run-apes-stage.md`](../commands/run-apes-stage.md) — tool-agnostic instruction.
- [`../examples/codex-cli-apes.md`](../examples/codex-cli-apes.md) — Codex CLI adaptation example.
- [`../examples/claude-code-apes.md`](../examples/claude-code-apes.md) — Claude Code adaptation example.
- Updated [`../commands/README.md`](../commands/README.md) and [`../examples/README.md`](../examples/README.md) indexes.

## Acceptance Criteria

- [x] The tool-agnostic instruction references the nine lifecycle stages and gate discipline without naming a preferred tool.
- [x] Both examples reuse the same tool-agnostic instruction and differ only in the tool-specific projection.
- [x] Every external claim carries a source and access date from `research/source-register.md`; unverified behavior is marked as a hypothesis, not fact.
- [x] The Claude example records the verified `CLAUDE.md` (not `AGENTS.md`) default per SRC-014.
- [x] The Codex example marks `AGENTS.md` auto-loading as unverified per SRC-015.
- [x] Markdown links, table-of-contents anchors, UTF-8, final newlines, and `git diff --check` pass.

## Verification

Executed on Windows PowerShell on 2026-08-15:

- `git diff --check` over the six touched files — passed; no whitespace errors.
- Relative Markdown link scan over the six touched files — passed; every local link resolves.
- Table-of-contents anchor scan over the six touched files — passed; every anchor resolves to a heading.
- The four new Markdown files and two edited indexes are present and UTF-8 with final newlines.
- `CHANGELOG.md` and `tasks/README.md` index entries are intentionally deferred: both files carried uncommitted Sprint 02-4 changes at the start of this sprint and were left untouched per instruction.

## Rollback

Remove `commands/run-apes-stage.md`, `examples/codex-cli-apes.md`, `examples/claude-code-apes.md`, and this task file, then revert the two index edits.

## Status

**Completed.** Tool-agnostic instruction and both adaptation examples written and verified on 2026-08-15. The examples are Draft (not yet validated against a real project). `CHANGELOG.md` and `tasks/README.md` index entries remain a pending manual step because those files held uncommitted changes at sprint start.
