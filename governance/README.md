# governance/

- Status: Draft
- Version: v0.1
- Owner: APES Maintainers
- Last Updated: 2026-08-09
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

Draft. ADR-0001, ADR-0002, and ADR-0003 are `Accepted`. ADR-0002 authorizes the schema-first direction; ADR-0003 authorizes the independent Python F2 validator runtime. The decision-note directory preserves the initial `Request changes` review, frozen remediation response, and implementer hardening follow-up. F2 remains `In Review` pending eligible independent re-review. RFC remains a placeholder, and the proposed Foundation-RFC mechanism is not yet operational.
