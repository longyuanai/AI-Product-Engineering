# ADR-0005 — Fixture-Only Artifact Metadata Contract Boundary

- **Title:** Limit the F1 artifact metadata contract to parsed fixture objects
- **Status:** Proposed
- **Date:** 2026-08-27

## Table of Contents

- [Context](#context)
- [Decision](#decision)
- [Consequences](#consequences)
- [Alternatives Considered](#alternatives-considered)

## Context

[`artifact-metadata.schema.json`](../../schemas/artifact-metadata.schema.json) requires nine fields in an object described as parsed YAML front matter. The repository's real Markdown files do not use YAML front matter; they use level-one titles followed by bullet-style metadata headers. The schema is exercised by objects under [`schemas/fixtures/`](../../schemas/fixtures/artifact-metadata/README.md), not by the Markdown headers themselves.

Treating the prototype as if it already governed repository Markdown would overstate conformance and obscure the migration work needed to make front matter normative. P0-1 also resolves OQ-11 at the schema prototype level by adding first-class Template and Checklist types. Because that taxonomy is a standard-level change, [`RFC-0001`](../rfc/RFC-0001-template-checklist-artifact-types.md) carries it separately.

## Decision

This ADR proposes the following repository boundary:

1. Schema v0.3.0 is a Foundation 0.3 / F1 demonstration contract for parsed metadata objects represented under `schemas/fixtures/`.
2. The schema does not constrain or validate the bullet-style metadata headers in repository Markdown files.
3. P0-1 does not migrate, rewrite, or claim conformance for any real Markdown metadata header.
4. A future Markdown-to-front-matter migration requires a separately approved task and decision, an explicit compatibility report, dry-run evidence, and rollback paths.
5. The Template / `TEMPLATE-` and Checklist / `CHECKLIST-` pairs proposed in RFC-0001 apply to schema fixture objects. They do not silently retype existing Markdown artifacts.

The status remains `Proposed`; only `longyuan` may accept or reject this boundary.

## Consequences

Positive:

- The documented contract matches what the repository actually validates.
- Existing Markdown remains canonical and unchanged.
- Schema experiments can continue without implying a repository-wide metadata migration.
- The OQ-11 taxonomy can be reviewed independently from any future storage-format decision.

Costs and limits:

- Passing the schema proves only that a parsed fixture object conforms.
- Repository Markdown metadata remains governed by its document conventions rather than this JSON Schema.
- Consumers cannot assume that every APES Markdown file exposes the nine schema fields.
- The proposed boundary and RFC remain subject to maintainer acceptance.

## Alternatives Considered

### Migrate real Markdown files to YAML front matter now

Rejected for P0-1. No repository Markdown file currently uses front matter, so migration would create a broad, high-risk diff across canonical documents. It would violate the minimum-change principle, exceed this task's scope, and require dedicated compatibility and rollback evidence.

### Treat bullet-style metadata as implicitly schema-conformant

Rejected because the field names and shapes differ, and no parser maps all real headers to the nine-field object. An implicit claim would not be testable.

### Remove the schema and fixtures

Rejected because the F1 prototype still provides useful, reviewable contract evidence. The defect is its overstated boundary, not the existence of the prototype.
