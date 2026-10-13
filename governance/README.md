# governance/

- Status: Draft
- Version: v0.2
- Owner: APES Maintainers
- Last Updated: 2026-08-27
- Purpose: Hold decision records, requests for comments, and governance policies.

## Table of Contents

- [Purpose](#purpose)
- [Subdirectories](#subdirectories)
- [Decision Types](#decision-types)
- [Status](#status)

## Purpose

Governance documents capture *why* APES looks the way it does. They are append-only memory of decisions and proposals.

## Subdirectories

- [`adr/`](adr/README.md) — Architecture Decision Records (cross-cutting repository or standard decisions).
- [`rfc/`](rfc/README.md) — Requests for Comments (standard-level proposals under review).
- [`decisions/`](decisions/README.md) — Per-stage or per-sprint decision notes (lighter weight).

## Decision Types

| Type | Where it lives | When to use |
| --- | --- | --- |
| ADR | `adr/` | Decision with structural, long-term impact |
| RFC | `rfc/` | Proposal to change the standard, needs community input |
| Decision note | `decisions/` | Stage- or sprint-scoped choice that does not need full ADR ceremony |

## Status

Draft. ADR-0001 through ADR-0004 are `Accepted`; ADR-0005 is `Proposed` and awaits `longyuan`'s decision on the fixture-only schema boundary. RFC-0001 is the first standard-level RFC and is also `Proposed`; no RFC is accepted. The decision-note directory preserves the F2 review trail and the pending `v0.2.0-alpha.1` release-candidate decision. F2 remains `In Review` pending eligible independent re-review, and the proposed Foundation-RFC mechanism is not yet operational.
