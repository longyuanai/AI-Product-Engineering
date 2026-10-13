# templates/

- Status: Active
- Version: v0.3
- Owner: APES Maintainers
- Last Updated: 2026-08-27
- Purpose: Hold reusable document templates for APES artifacts.

## Table of Contents

- [Purpose](#purpose)
- [Template Contract](#template-contract)
- [Canonical Working Copy Rule](#canonical-working-copy-rule)
- [Artifact Metadata Compatibility](#artifact-metadata-compatibility)
- [Lifecycle Templates](#lifecycle-templates)
- [Usage](#usage)

## Purpose

These templates provide one reusable core artifact for each APES lifecycle stage. They standardize structure, evidence capture, scope boundaries, and handoff readiness without prescribing a project's conclusions.

## Template Contract

Every lifecycle template must:

- use the repository metadata header in this exact order: `Title` as the level-one heading, then `Status`, `Version`, `Owner`, `Last Updated`, and `Purpose`;
- declare an artifact metadata Schema type and ID prefix in an `Artifact Contract` section;
- include a Table of Contents whose links resolve to headings in the same file;
- capture evidence with both a source and an access date, following [`../research/source-register.md`](../research/source-register.md);
- state what is out of scope and what the template does not replace;
- remain vendor-neutral; and
- end with a newline and use UTF-8 encoding.

## Canonical Working Copy Rule

Treat every file listed below as a read-only APES reference. Copy the selected template to the adopting project's `OUTPUT_PATH`, fill only that working copy, and retain the APES version and canonical `TEMPLATE_PATH` as provenance. Do not edit the canonical template during project execution.

A completed working copy is project evidence only to the extent that its claims cite actual sources and access dates. Filled fields do not create evidence by themselves.

## Artifact Metadata Compatibility

[`artifact-metadata.schema.json`](../schemas/artifact-metadata.schema.json), Schema v0.3.0, adds first-class `Template` / `TEMPLATE-` and `Checklist` / `CHECKLIST-` pairs. The standard-level change is proposed in [`RFC-0001`](../governance/rfc/RFC-0001-template-checklist-artifact-types.md), and OQ-11 is recorded as resolved for this review candidate.

Per Proposed [`ADR-0005`](../governance/adr/ADR-0005-fixture-only-artifact-metadata-boundary.md), those pairs currently govern parsed fixture objects only. They do not retroactively validate or rewrite the bullet-style headers or legacy Artifact Contract examples in canonical template Markdown. Both proposals await `longyuan`'s decision.

## Lifecycle Templates

- [`idea-brief.md`](idea-brief.md) — Idea opportunity and hypothesis brief.
- [`discovery-interview-notes.md`](discovery-interview-notes.md) — Discovery interview notes.
- [`research-note.md`](research-note.md) — Research question and evidence note.
- [`validation-experiment-plan.md`](validation-experiment-plan.md) — Validation experiment plan and outcome record.
- [`product-scope-spec.md`](product-scope-spec.md) — Product scope and acceptance specification.
- [`business-viability-brief.md`](business-viability-brief.md) — Business viability assumptions and evidence brief.
- [`engineering-change-record.md`](engineering-change-record.md) — Engineering change and verification record.
- [`growth-experiment-record.md`](growth-experiment-record.md) — Growth experiment and learning record.
- [`retrospective-and-learning-record.md`](retrospective-and-learning-record.md) — Knowledge-stage retrospective and learning record.

## Usage

Copy the relevant template into the project's artifact location, replace instructional placeholders with project-specific content, and retain unsupported statements as hypotheses. If the adopting project emits a Schema v0.3.0 parsed metadata object, use type `Template` and a `TEMPLATE-` identifier. A completed template is an input to the corresponding checklist under [`../checklists/`](../checklists/README.md); it is not evidence merely because its fields are filled in.
