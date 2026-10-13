# Glossary

- Status: Active
- Version: v0.3
- Owner: APES Maintainers
- Last Updated: 2026-08-27
- Purpose: Define the terms required to run the APES alpha one-stage workflow consistently.

## Table of Contents

- [How to Use](#how-to-use)
- [Terms](#terms)
- [Boundary](#boundary)

## How to Use

These definitions govern the `v0.2.0-alpha.1` user path. A module may add narrower definitions later, but it must not silently change these workflow meanings.

## Terms

### Alpha / Prerelease

A provisional, incomplete release intended for bounded use and feedback. The APES alpha is not final v0.2, F5, a mature standard, or an externally validated methodology.

### Canonical Checklist

The read-only APES source checklist mapped to a lifecycle transition. Users copy it to a project-owned gate record before adding evidence or decisions.

### Canonical Template

The read-only APES source structure mapped to a lifecycle stage. Users copy it to a project-owned stage artifact before filling it.

### Compensating Evidence

Evidence that addresses the same criterion when the preferred evidence is unavailable. It must state provenance, access date, limitations, owner, and expiry or review date; it never creates a silent waiver.

### Decision Owner

The named human accountable for recording the final manual gate result. An agent may prepare evidence and criterion state but may not impersonate this owner.

### Evidence

A traceable observation, source, dataset, test result, or record used to support a claim. Material evidence includes its source and access date and exposes relevant limitations.

### Exit Gate

The evidence-based decision point between the selected stage and its next lifecycle stage. The permitted results are `Pass`, `Failed`, or `Deferred`.

### Gate Record

The project-owned working copy of a canonical checklist that contains criterion state, evidence references, gaps, compensating evidence, ownership, review date, and the human decision.

### Internal Dogfood

Use of APES by its maintainers to test clarity and operability. It is internal acceptance evidence, not external validation, adoption evidence, or a real-project case.

### Lifecycle Stage

One bounded position in the APES cycle: Idea, Discovery, Research, Validation, Product, Business, Engineering, Growth, or Knowledge.

### Stage Artifact

The project-owned output produced from the canonical template for one selected lifecycle stage.

### Working Copy

A project-owned copy of a canonical APES file. Project evidence and decisions are recorded in working copies so upstream APES sources remain clean and upgradeable.

## Boundary

The glossary defines the active alpha workflow only. OQ-11 is resolved for the Schema v0.3.0 review candidate: parsed fixture objects use `Template` / `TEMPLATE-` and `Checklist` / `CHECKLIST-`. Proposed [`ADR-0005`](../governance/adr/ADR-0005-fixture-only-artifact-metadata-boundary.md) and [`RFC-0001`](../governance/rfc/RFC-0001-template-checklist-artifact-types.md) await `longyuan`'s decision and do not migrate canonical Markdown headers.
