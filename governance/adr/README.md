# governance/adr/

- Status: Draft
- Version: v0.1
- Owner: APES Maintainers
- Last Updated: 2026-08-09
- Purpose: Hold Architecture Decision Records for APES.

## Table of Contents

- [Purpose](#purpose)
- [Index](#index)
- [ADR Format](#adr-format)
- [Status Rules](#status-rules)

## Purpose

ADRs document significant architectural decisions that affect multiple parts of APES or this repository. They are append-only.

## Index

- [`ADR-0001-project-positioning.md`](ADR-0001-project-positioning.md) — Project name, standard name, positioning, and scope boundaries.
- [`ADR-0002-schema-first-reference-architecture.md`](ADR-0002-schema-first-reference-architecture.md) — Accepted schema-first, file-native reference architecture and phased tooling boundary.
- [`ADR-0003-f2-read-only-validator-runtime.md`](ADR-0003-f2-read-only-validator-runtime.md) — Accepted Python runtime, independent repository, deterministic CLI, and security boundary for F2.

## ADR Format

Required sections:

- Title
- Status
- Date
- Context
- Decision
- Consequences
- Alternatives Considered

## Status Rules

- ADRs are never edited to revise history. Supersede by writing a new ADR.
- Status values: `Proposed`, `Accepted`, `Superseded`, `Deprecated`.
