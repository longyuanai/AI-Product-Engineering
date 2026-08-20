# templates/

- Status: Active
- Version: v0.2
- Owner: APES Maintainers
- Last Updated: 2026-08-19
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

The templates correspond to [`artifact-metadata.schema.json`](../schemas/artifact-metadata.schema.json), Schema v0.2.0. That Schema does not yet define `Template` or `Checklist` types. Until the taxonomy is revised through an approved compatibility change, lifecycle templates and stage-gate checklists use the existing `Workflow` type and `WORKFLOW-` ID prefix.

This fallback keeps identifiers schema-valid but collapses distinct artifact kinds into one type. The open taxonomy decision, its cost, and its resolution trigger are recorded as OQ-11 in [`repository-evolution-plan.md`](../docs/repository-evolution-plan.md#15-open-questions).

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

Copy the relevant template into the project's artifact location, replace instructional placeholders with project-specific content, assign a schema-valid `WORKFLOW-` identifier, and retain unsupported statements as hypotheses. A completed template is an input to the corresponding checklist under [`../checklists/`](../checklists/README.md); it is not evidence merely because its fields are filled in.
