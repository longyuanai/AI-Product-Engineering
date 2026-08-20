# examples/

- Status: Active
- Version: v0.2
- Owner: APES Maintainers
- Last Updated: 2026-08-20
- Purpose: Hold tool adaptations and bounded evidence showing how APES is applied.

## Table of Contents

- [Purpose](#purpose)
- [Selection Criteria](#selection-criteria)
- [Tool Adaptation Examples](#tool-adaptation-examples)
- [Internal Maintainer Dogfood](#internal-maintainer-dogfood)
- [Status](#status)

## Purpose

Examples make the APES workflow concrete and expose gaps in the current guidance. Every example must state whether it is a tool adapter, internal acceptance evidence, or an external real-project case; those categories are not interchangeable.

## Selection Criteria

A future real-project example is admitted only when:

- it documents its scope, stages, and evidence;
- it cites the APES version used;
- it records limitations and what APES failed to handle; and
- its authors authorize the evidence and any sensitive-data treatment.

Internal dogfood and tool adaptations do not satisfy the roadmap real-case criterion.

## Tool Adaptation Examples

These project the same tool-neutral command onto a specific coding tool. They preserve exact paths, canonical-file safety, named human gate ownership, and the stop after handoff.

- [`claude-code-apes.md`](claude-code-apes.md) — Validation-stage example using Claude Code and the adopting project's own instructions.
- [`codex-cli-apes.md`](codex-cli-apes.md) — Research-stage example using Codex CLI without depending on unverified `AGENTS.md` loading.

## Internal Maintainer Dogfood

These files exercise the Idea stage against APES's own alpha onboarding problem:

- [`v0.2.0-alpha.1-maintainer-dogfood-idea-brief.md`](v0.2.0-alpha.1-maintainer-dogfood-idea-brief.md) — Project-owned Idea artifact with repository-local evidence and explicit non-claims.
- [`v0.2.0-alpha.1-maintainer-dogfood-gate-1.md`](v0.2.0-alpha.1-maintainer-dogfood-gate-1.md) — Preserved Gate 1 working record with the authoritative human `Deferred` result.
- [`v0.2.0-alpha.1-maintainer-dogfood-gate-1-rereview.md`](v0.2.0-alpha.1-maintainer-dogfood-gate-1-rereview.md) — Fresh undecided Gate 1 re-review record with criterion evidence and itemized P1 closure conclusions for `longyuan`.
- [`v0.2.0-alpha.1-maintainer-release-readiness.md`](v0.2.0-alpha.1-maintainer-release-readiness.md) — Frozen project-owned release-readiness record with criterion evidence, repair integrity snapshot, Gate 1 prerequisite, and pending human decisions.

This dogfood is internal acceptance evidence only. It is not adoption evidence, external validation, a full-lifecycle case, a roadmap real case, or release authority.

## Status

Active. Two tool adaptations, one internal Idea artifact, the preserved `Deferred` Gate 1 record, one fresh `Pending` re-review record, and one frozen project-owned release-readiness record exist. No external real-project case study exists yet.
