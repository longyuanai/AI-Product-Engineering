# ADR-0004 — Apache-2.0 Repository License

- **Title:** One Apache License 2.0 boundary for repository-authored APES content
- **Status:** Accepted
- **Date:** 2026-08-19
- **Accepted:** 2026-08-19

## Table of Contents

- [Context](#context)
- [Decision](#decision)
- [Consequences](#consequences)
- [Alternatives Considered](#alternatives-considered)

## Context

The repository foundation included a placeholder `LICENSE` that reserved all rights until maintainers selected a license. The `v0.2.0-alpha.1` candidate needs a clear reuse and contribution boundary before any public release can be considered. APES contains documentation, templates, checklists, schemas, fixtures, tests, examples, commands, and governance records, so a split license would add interpretation cost at the first-user stage.

## Decision

1. Repository-authored APES content is licensed under the Apache License 2.0, SPDX identifier `Apache-2.0`.
2. The license boundary covers repository-authored documentation, templates, checklists, schemas, fixtures, tests, examples, commands, and governance records.
3. Contributions intentionally submitted for inclusion are accepted under the same terms, consistent with section 5 of Apache-2.0, unless the contributor conspicuously designates the submission otherwise.
4. Third-party material retains its original copyright, license, and attribution requirements. Inclusion in this repository does not relicense that material.
5. A `NOTICE` file will be added only if a concrete attribution obligation requires one.
6. This decision does not require file-by-file SPDX headers and does not create a separate documentation license.

## Consequences

Positive:

- Users and contributors have one repository-wide license boundary.
- The license permits reuse, modification, and distribution while preserving notice and patent terms.
- Documentation and machine-readable contracts can travel together without a dual-license interpretation step.

Costs and limits:

- Redistributors must comply with Apache-2.0 conditions.
- Third-party material still requires case-specific license review.
- This ADR records the project decision; it is not legal advice.

## Alternatives Considered

### MIT for the whole repository

Rejected for this alpha because Apache-2.0 provides an explicit patent grant and a more detailed contribution and notice framework.

### Apache-2.0 for code and CC BY 4.0 for documentation

Rejected because the repository mixes human-readable and machine-readable standard artifacts. A dual-license boundary would make copying a complete APES workflow less clear.

### Continue with the all-rights-reserved placeholder

Rejected because it prevents the intended public reuse of the alpha and leaves contribution terms ambiguous.
