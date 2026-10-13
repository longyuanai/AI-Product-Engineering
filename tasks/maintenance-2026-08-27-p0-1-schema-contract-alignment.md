# Maintenance — P0-1 Schema Contract Alignment

- Status: Completed
- Version: v0.1
- Owner: APES Maintainers
- Last Updated: 2026-08-27
- Purpose: Align the F1 artifact metadata prototype with its actual fixture-only use, resolve OQ-11 at review-candidate level, and document the YAML date-string rule.

## Table of Contents

- [Goal](#goal)
- [Scope](#scope)
- [Governance](#governance)
- [Out of Scope](#out-of-scope)
- [Verification](#verification)
- [Status](#status)

## Goal

Remove the contract claim gap without migrating repository Markdown: describe Schema v0.3.0 as a fixture-only prototype, add first-class Template and Checklist types with distinct prefixes, and make unquoted YAML dates an explicit negative case.

## Scope

- Add `Template` / `TEMPLATE-` and `Checklist` / `CHECKLIST-` to the artifact metadata schema.
- Require YAML producers to quote `last_updated` so the parsed value remains a JSON Schema string.
- Add and document an invalid unquoted-date YAML fixture.
- Synchronize the requested schema, template, checklist, FAQ, glossary, and OQ-11 descriptions.
- Preserve canonical Markdown metadata headers and the release-readiness evidence record.

## Governance

- [`../governance/adr/ADR-0005-fixture-only-artifact-metadata-boundary.md`](../governance/adr/ADR-0005-fixture-only-artifact-metadata-boundary.md) is `Proposed` and records the repository-level boundary.
- [`../governance/rfc/RFC-0001-template-checklist-artifact-types.md`](../governance/rfc/RFC-0001-template-checklist-artifact-types.md) is `Proposed` and carries the standard-level change required by `AGENTS.md`.
- Final acceptance belongs to `longyuan`.

## Out of Scope

- No APES-Validator, F2 finding, CI/workflow, application, CLI, MCP, website, or build-pipeline change.
- No file under `standards/`.
- No front matter migration or bulk Markdown metadata rewrite.
- No P1/P2 work and no Git commit, branch, tag, or push.
- No change to Sprint 2 `In Review`, Research Gate `RESEARCH AGAIN`, F2 `In Review / Request changes`, or F3 unstarted.

## Verification

Executed on Windows on 2026-08-27:

- `pytest --basetemp=.pytest-tmp` — did not start because `pytest` is not installed as a PATH command; this failed invocation is not counted as a pass.
- `C:\Users\15072\AppData\Local\Programs\Python\Python314\python.exe -m pytest --basetemp=.pytest-tmp` — passed: 15 collected, 15 passed.
- Direct Draft 2020-12 and fixture validation with Python 3.14.6, jsonschema 4.26.0, and PyYAML 6.0.3 — passed: meta-schema valid, 4/4 valid JSON fixtures accepted, 4/4 invalid JSON fixtures rejected, 1/1 unquoted YAML date fixture rejected as a native `datetime.date`, and 15/15 type-prefix pairs matched.
- Targeted `test_markdown_local_links_and_anchors_resolve` — passed: 1/1. The full 15-test run also included this repository-wide check.
- `git diff --check` — passed with exit code 0 and no output.

## Status

**Completed.** P0-1 content and verification are complete. ADR-0005 and RFC-0001 remain `Proposed`; `longyuan` retains final acceptance authority. No P1 or P2 work began.
