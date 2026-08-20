# v0.2.0-alpha.1 Release Candidate Preparation

- Status: Ready for Gate 1 Re-review
- Version: v0.1
- Owner: APES Maintainers
- Last Updated: 2026-08-20
- Purpose: Prepare a bounded APES Project Layer alpha candidate for maintainer review without performing release actions.

## Table of Contents

- [Goal](#goal)
- [Baseline](#baseline)
- [Scope](#scope)
- [Out of Scope](#out-of-scope)
- [Acceptance Criteria](#acceptance-criteria)
- [Verification](#verification)
- [Limitations](#limitations)
- [Rollback](#rollback)
- [Status](#status)

## Goal

Prepare a complete documented one-stage path for each APES lifecycle stage while declaring the repository license and preserving every existing governance boundary. Repository contracts verify the mappings; internal dogfood exercises only Idea and does not establish unaffiliated first-time-user usability.

## Baseline

- Branch: `main` (`ahead 1` of `origin/main`)
- HEAD: `0814e68d9fd9f6060e4be4f7072cc54c1788ad06`
- Candidate tag before preparation: absent
- Working tree: intentionally dirty before this task. The original pre-alpha dirty state was not captured path-by-path and cannot now be independently reconstructed. A full repair-start path/status manifest and fingerprints for this review-remediation pass are recorded in [`../examples/v0.2.0-alpha.1-maintainer-release-readiness.md`](../examples/v0.2.0-alpha.1-maintainer-release-readiness.md).
- Release-readiness record SHA-256: `597a1d4c3fa1802f98a1b6e2813db09bc131554922584b6b772d1d98403361a2`

The known baseline included work in root documentation, research records, lifecycle documentation, Sprint tasks, templates, checklists, commands, examples, and tests. This task changes only its approved release-preparation surface. Preservation claims for the remediation pass are bounded to the newly captured repair-start manifest and delta ledger; they do not retroactively prove the uncaptured pre-alpha state.

## Scope

- Accept and document the repository-wide Apache-2.0 license.
- Establish the provisional `v0.2.0-alpha.1` Project Layer identity and exact promise.
- Connect one selected stage to its canonical template, working output, exit-gate checklist, working gate record, and human decision owner.
- Add bounded internal Idea-stage dogfood, a reusable canonical release-readiness checklist, and a project-owned readiness working record.
- Extend read-only repository contracts from 10 to 15 tests.

## Out of Scope

- Schema, fixtures, GitHub Actions, production dependencies, Standard module bodies, OQ-11 resolution, F2/F3 work or state changes, and detailed Sprint 2.4 evidence.
- Final v0.2, F5, Release Layer bundle, checksum manifest, or external validation.
- Commit, branch, tag, push, GitHub Release, hosted publication, or any other outward-facing release action.

## Acceptance Criteria

- [x] Root identity and release records use `v0.2.0-alpha.1` without adding a root `VERSION` file.
- [x] Apache-2.0 text, SPDX identifier, license boundary, contribution terms, and ADR are consistent.
- [x] Documentation and repository contracts map each of the nine stages to an exact template, exit gate, and bounded one-stage command path; recorded dogfood covers Idea only and does not establish new-user or other-stage usability.
- [x] Canonical templates and checklists remain read-only; only project-owned working copies are filled.
- [x] An agent prepares evidence but a named human owner records `Pass`, `Failed`, or `Deferred`.
- [x] Internal dogfood is visibly not external validation, adoption evidence, or a roadmap real case.
- [x] Current Sprint 2, Research Gate, F2, F3, and OQ-11 authority is preserved.
- [x] Fifteen read-only repository contract tests, the readiness-digest check, and closing integrity checks pass after the corrected P1 remediation.
- [x] The candidate reaches `Ready for Gate 1 Re-review` with the existing human `Deferred` result preserved and no Git or publication action.

## Verification

Executed from the repository root on Windows PowerShell on 2026-08-19:

- `uv run --with jsonschema python -B -m unittest discover -s tests -v` — passed, 15 tests, `OK`. The first run exposed one overly compressed dogfood non-claim phrase; the wording was made explicit and the full suite then passed.
- `git diff --check` — exited 0 with no whitespace error. The pre-existing `.gitignore` warning that CRLF will be replaced by LF remains informational.
- `git diff --exit-code -- schemas .github/workflows` — exited 0 with no output; protected Schema and workflow paths are unchanged.
- `git diff --name-only --diff-filter=U` — no unresolved conflict.
- `git rev-parse HEAD` — unchanged at `0814e68d9fd9f6060e4be4f7072cc54c1788ad06`.
- `git tag --list "v0.2.0-alpha.1"` — no output; no candidate tag exists.
- `git status --short --branch` — still `main...origin/main [ahead 1]`; the intentionally dirty tree remains present together with approved alpha-preparation and review-remediation files.

Review-remediation verification on 2026-08-19:

- First changed-tree run: `uv run --with jsonschema python -B -m unittest discover -s tests -v` — passed, exactly 15 tests, `OK`, 0.492 seconds.
- `git diff --check` — exited 0 with only the known `.gitignore` CRLF-to-LF warning.
- Protected Schema/workflow diff, conflict, HEAD, branch, and tag checks remained unchanged.
- The old overstrong alpha-promise sentence has zero active Markdown matches.
- The project-owned [`release-readiness working record`](../examples/v0.2.0-alpha.1-maintainer-release-readiness.md) holds the repair-start manifest, scoped delta ledger, finding closure, and pending human decisions.
- Final recorded-tree run: the same suite passed exactly 15 tests, `OK`, 0.551 seconds; integrity, protected-path, conflict, HEAD, branch, tag, and old-promise checks remained unchanged.

Release-task closure verification on 2026-08-20:

- Pre-freeze anchor-validation run: `uv run --with jsonschema python -B -m unittest discover -s tests` — passed, exactly 15 tests, `OK`, 0.499 seconds.
- The readiness record was then frozen at SHA-256 `597a1d4c3fa1802f98a1b6e2813db09bc131554922584b6b772d1d98403361a2`, and only this task's one-way digest anchor was updated.
- Frozen-record run: the same suite passed, exactly 15 tests, `OK`, 0.516 seconds, including the readiness-digest assertion.
- `git diff --check` — exited 0 with only the known `.gitignore` CRLF-to-LF warning.
- `git diff --exit-code -- schemas .github/workflows` — exited 0 with no output.
- `git diff --name-only --diff-filter=U` — exited 0 with no unresolved conflict and only the same known `.gitignore` EOL warning.
- `git rev-parse HEAD` — `0814e68d9fd9f6060e4be4f7072cc54c1788ad06`.
- `git branch --show-current` — `main`.
- `git tag --list "v0.2.0-alpha.1"` — no output; tag absent.
- Protected-path aggregate SHA-256 — unchanged at `7dc7e28da19528dacee3fd40c826bdc060f52ecb9a97c361487e4787951ea5d9`.
- The existing human `Deferred` Gate 1 result remained byte-identical at SHA-256 `4853dcfea8736556eb80ee3918a440d24461c66d1b69ab502c69004c89a3e9d9`; a separate undecided re-review record is prepared for `longyuan`.

No production dependency, commit, branch, tag, push, hosted release, release bundle, checksum manifest, or F5 artifact was created.

## Limitations

- Standard modules are placeholders and provide optional context only.
- No external real-project case has validated the workflow.
- Gate 1 is recorded as `Deferred` by `longyuan`; a later `Pass`, if any, requires a fresh undecided Gate record and a new explicit human review. The final `Release / Hold` decision also belongs to `longyuan`.
- F2 remains in review after an independent `Request changes` result; F3 is unstarted.

## Rollback

Reverse only the task-owned hunks listed in the project-owned readiness record's delta ledger. Existing files must return to their recorded repair-start SHA-256; the new readiness record may be removed only as an explicit rollback action. Do not use whole-tree checkout, restore, reset, or stash. If any expected fingerprint differs, stop and ask the maintainer to reconcile the overlapping change. No data migration or Git history operation is required.

## Status

**Ready for Gate 1 Re-review.** The corrected P1 findings have repository evidence prepared for independent human re-review. The existing human `Deferred` result remains authoritative; candidate `Release / Hold` remains pending and `Release` is ineligible. No Git or publication action is authorized.
