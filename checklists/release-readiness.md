# v0.2.0-alpha.1 Release Readiness

- Status: Active
- Version: v0.1
- Owner: APES Maintainers
- Last Updated: 2026-08-19
- Purpose: Prepare auditable evidence for a human `Release / Hold` decision on the bounded APES alpha candidate.

## Table of Contents

- [Working Copy Rule](#working-copy-rule)
- [Artifact Contract](#artifact-contract)
- [Candidate Inputs](#candidate-inputs)
- [Release Eligibility Prerequisite](#release-eligibility-prerequisite)
- [Identity and License](#identity-and-license)
- [MVP User Path](#mvp-user-path)
- [Evidence and Boundaries](#evidence-and-boundaries)
- [Repository Integrity](#repository-integrity)
- [Human Decisions](#human-decisions)
- [Hard Stop](#hard-stop)

## Working Copy Rule

This is a canonical APES checklist. Copy it to a project-owned release record before checking boxes or recording a decision. Retain the candidate version and canonical source path. Never record a release decision in this source file.

## Artifact Contract

- Schema type: `Workflow`
- ID prefix: `WORKFLOW-`
- Suggested artifact ID: `WORKFLOW-RELEASE-READINESS-001`
- Compatibility note: OQ-11 remains unresolved; the Schema v0.2.0 fallback is unchanged.

## Candidate Inputs

- Candidate identifier and changelog entry.
- License text and accepted license ADR.
- Getting Started path, canonical command, adapters, templates, and gate checklists.
- Internal dogfood artifact and working Gate 1 record.
- Repository contract test output and protected-path diff evidence.
- Named human Gate 1 and release decision owners.

## Release Eligibility Prerequisite

- [ ] Internal dogfood Gate 1 is recorded as `Pass` by `longyuan` in the project-owned Gate 1 working record.

`Release` is eligible only when that prerequisite is checked against the recorded human result. A Gate 1 result of `Pending`, `Failed`, or `Deferred` makes the candidate ineligible for `Release`. This rule does not authorize an agent to select `Hold` or any other result; `longyuan` alone records the candidate decision.

## Identity and License

- [ ] `README.md`, `CHANGELOG.md`, and the candidate decision consistently use `v0.2.0-alpha.1`.
- [ ] No root `VERSION` file or unrelated document-version mass bump was introduced.
- [ ] `LICENSE` contains the canonical Apache License 2.0 text.
- [ ] `Apache-2.0`, the repository-authored content boundary, contribution terms, and ADR-0004 agree.
- [ ] Third-party rights remain distinct; `NOTICE` exists only if a concrete obligation requires it.

## MVP User Path

- [ ] The exact alpha promise is visible and links to Getting Started.
- [ ] All nine stages map to exactly one template and exit-gate checklist.
- [ ] The command requires `STAGE`, `APES_SOURCE_ROOT`, `PROJECT_WORK_ROOT`, `TEMPLATE_PATH`, `OUTPUT_PATH`, `EXIT_GATE_CHECKLIST_PATH`, `GATE_RECORD_PATH`, and `GATE_DECISION_OWNER`.
- [ ] Preflight inspects every component without first following links, rejects dangling links, resolves genuine missing-target ancestors, confines project-owned paths to `PROJECT_WORK_ROOT`, and rejects aliases or hard links to protected APES source before any write.
- [ ] A run stops before writing when its existing Gate Record Decision cell is already `Pass`, `Failed`, or `Deferred`; only a fresh undecided record may proceed.
- [ ] Canonical inputs remain read-only and project evidence goes only to working copies.
- [ ] Placeholder Standard modules are optional context and never define the alpha artifact.
- [ ] The agent prepares evidence but cannot select the final gate result.
- [ ] Every run stops after handoff and never begins the next stage automatically.

## Evidence and Boundaries

- [ ] Material claims require source and access date; unsupported statements remain hypotheses or unverified.
- [ ] Internal dogfood is labeled acceptance evidence only.
- [ ] No external validation, adoption, real-case, mature-standard, or industry-standard claim is made.
- [ ] The candidate is a provisional Project Layer snapshot, not final v0.2, Foundation/Research OS version assignment, F5, or deterministic Release Layer bundle.
- [ ] Sprint 2 is `In Review`; Research Gate is `RESEARCH AGAIN`; F2 is `In Review / Request changes`; F3 is unstarted.
- [ ] OQ-11 remains unresolved and `Workflow` / `WORKFLOW-` remains the documented fallback.

## Repository Integrity

- [ ] Fifteen read-only repository contract tests pass.
- [ ] Local Markdown links and anchors resolve.
- [ ] `git diff --check` reports no error; any known `.gitignore` EOL warning is recorded as pre-existing.
- [ ] `schemas/` and `.github/workflows/` have no alpha-preparation diff.
- [ ] HEAD, branch, and pre-existing dirty-tree entries remain preserved.
- [ ] No production dependency, application code, commit, branch, tag, push, bundle, checksum manifest, or hosted release was created.

## Human Decisions

| Decision | Owner | Evidence | Result | Date |
| --- | --- | --- | --- | --- |
| Internal dogfood Gate 1 | longyuan | Idea brief and Gate 1 working record | Pending: Pass / Failed / Deferred | YYYY-MM-DD |
| Alpha candidate | longyuan | Release task, project-owned readiness record, and a recorded Gate 1 `Pass` | Pending: Release / Hold | YYYY-MM-DD |

## Hard Stop

Stop at `Ready for Maintainer Decision`. This checklist never authorizes Git history changes or publication. Commit, tag, push, GitHub Release, hosted publication, release bundle, checksum manifest, and F5 require separate explicit authorization after the human decisions are recorded.
