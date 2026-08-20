# standards/

- Status: Placeholder
- Version: v0.1
- Owner: APES Maintainers
- Last Updated: 2026-08-19
- Purpose: Hold the AI Product Engineering Standard itself, organized by lifecycle stage.

## Table of Contents

- [Purpose](#purpose)
- [Layout](#layout)
- [Lifecycle Alignment](#lifecycle-alignment)
- [How Modules Are Added](#how-modules-are-added)
- [Current Status](#current-status)

## Purpose

This directory contains the actual APES standard. Each subdirectory corresponds to a lifecycle stage or to the repository itself. Subdirectories are placeholders in v0.1; the contents of each module standard are deliberately not yet written.

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

As of v0.1:

- No module standard has been written.
- This directory exists only to establish structure and to prevent future drift.
- Each module's `README.md` only states its placeholder purpose.
