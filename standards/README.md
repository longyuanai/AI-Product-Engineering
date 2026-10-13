# standards/

- Status: Draft
- Version: v0.2
- Owner: APES Maintainers
- Last Updated: 2026-08-25
- Purpose: Hold the AI Product Engineering Standard itself, organized by lifecycle stage.

## Table of Contents

- [Purpose](#purpose)
- [Layout](#layout)
- [Lifecycle Alignment](#lifecycle-alignment)
- [How Modules Are Added](#how-modules-are-added)
- [Current Status](#current-status)

## Purpose

This directory contains the actual APES standard. Each subdirectory corresponds to a lifecycle stage or to the repository itself.

One module, [`research/`](research/README.md), now carries `Draft` standard text. Every other module remains a placeholder whose body is deliberately not yet written. Each module's own `Status` field is authoritative; this index does not restate it.

## Layout

- [`repository/`](repository/README.md) — How APES-related repositories are organized.
- [`discovery/`](discovery/README.md) — Understanding users, problems, and context.
- [`research/`](research/README.md) — Investigating evidence.
- [`validation/`](validation/README.md) — Testing hypotheses with real users.
- [`product/`](product/README.md) — Defining scope and experience.
- [`business/`](business/README.md) — Confirming viability and go-to-market.
- [`engineering/`](engineering/README.md) — Building the system.
- [`growth/`](growth/README.md) — Acquiring and retaining users.
- [`knowledge/`](knowledge/README.md) — Capturing and reusing learnings.

## Lifecycle Alignment

The current scaffold is intentionally asymmetric with the nine-stage lifecycle:

- Discovery through Knowledge have matching placeholder module directories.
- Idea has no standard module directory. In the current boundary it is captured by the lifecycle definition and the reusable Idea brief template, without implying that a permanent Idea standard module has been approved.
- `repository/` is cross-cutting guidance for APES-related repository organization and does not represent a lifecycle stage.

Changing this directory structure would be a separately reviewed structural decision. This documentation records the current boundary without creating, renaming, or removing modules.

## How Modules Are Added

A module standard is added through:

1. An RFC in [`../governance/rfc/`](../governance/rfc/README.md) for any cross-cutting change.
2. A Draft status in its own `README.md` once review is complete.
3. Validation against at least one real case before being marked Accepted.

## Current Status

As of v0.2:

- [`research/`](research/README.md) is `Draft`. Its rules were extracted from this repository's own `research/` practice, not authored speculatively. No RFC has been raised to promote it beyond `Draft`, and it has not been validated against an external project.
- The remaining eight modules are placeholders. No standard text has been written for them.
- Because no module has been validated against a real case, no module is Accepted.
