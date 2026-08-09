# F2 Independent Review Remediation Evidence — 2026-08-09

- Status: Ready for Re-review
- Version: v0.1
- Owner: APES Maintainers
- Last Updated: 2026-08-10
- Purpose: Freeze the implementation response to the thirteen findings from the first independent F2 schema and security review.

## Table of Contents

- [Scope](#scope)
- [Remediation Snapshot](#remediation-snapshot)
- [Finding Disposition](#finding-disposition)
- [Verification Evidence](#verification-evidence)
- [Implementer Self-Review Follow-up](#implementer-self-review-follow-up)
- [Residual Limits](#residual-limits)
- [Re-review Boundary](#re-review-boundary)
- [Outcome](#outcome)

## Scope

The independent review of commit `35d4ccf` selected `Request changes` and recorded thirteen findings in [`../../checklists/f2-independent-review.md#independent-findings`](../../checklists/f2-independent-review.md#independent-findings). This note records the implementation response. It does not replace the initial review, declare reviewer approval, close F2, or authorize F3.

## Remediation Snapshot

| Artifact | Identifier |
| --- | --- |
| Runtime repository | `E:\001项目\001Github\APES-Validator` |
| Remediation commit | `73bbe6ede1deeb1d3c71deadcd8927da6e911be8` |
| Reviewed predecessor | `35d4ccf7acaa5881038f907d7a8b7eb59d47fd7b` |
| APES artifact schema | `urn:apes:schema:artifact-metadata:0.2.0` |
| APES artifact schema SHA-256 | `D6398943E352557E8D44337751746C3ABB2623C1DE0A10D613CF4B9B0799F0CE` |
| `uv.lock` SHA-256 | `170207EBF67649D584F7209934352927F413CC59E688581599B23427EA279785` |
| Built wheel SHA-256 | `B05AF816963627C25A32EB069B92599980AAD262DD9D3965936738E30BC60361` |
| Built sdist SHA-256 | `B721A73822CA44BDC0877B97CFB7BFABB5F101C36655C9850AFD6CB9EB21141A` |

## Finding Disposition

| Finding | Implementation response | Regression evidence |
| --- | --- | --- |
| F2-P0-1 | Added an explicit `referencing.Registry()` with no retrieval hook. The APES schema profile rejects external `$ref`, every `$dynamicRef`, nested `$schema`, nested `$id`, and non-APES root `$id`; local `$ref` values must be resolvable JSON Pointers. | External `$ref`, local/external `$dynamicRef`, nested `$schema`, rebasing `$id`, and dangling-pointer tests. |
| F2-P1-1 | Empty, whitespace-only, and empty angle-bracket Markdown targets now produce `APES010` rather than indexing an empty split. | Three parameterized empty-target cases. |
| F2-P1-2 | Schema, fixture, YAML, and validation recursion is caught and converted to bounded diagnostics; schema-policy traversal is iterative and its output is capped. Exception formatting itself is recursion-safe. | Deep JSON schema, deep JSON fixture, and deep YAML front matter cases. |
| F2-P1-3 | Every accepted local `$ref` JSON Pointer is resolved during schema loading; runtime `Unresolvable` failures are also caught as `APES031`. | Dangling local pointer test. |
| F2-P1-4 | A PyYAML `datetime.date` value in `last_updated` is normalized to its ISO string before JSON Schema validation; timestamps remain invalid. | Unquoted canonical YAML date test. |
| F2-P2-1 | Schema v0.2.0 now binds all thirteen artifact types to their canonical ID prefixes through an exhaustive `oneOf`. | Thirteen valid pairs and thirteen mismatched pairs. |
| F2-P2-2 | Unexpected CLI implementation failures emit bounded `APES900` output and exit with code 3; exit code 1 remains reserved for validation diagnostics. | `check` and `graph` internal-error tests. |
| F2-P2-3 | Inline backtick code spans are masked before Markdown link extraction; fenced blocks remain ignored. | Inline-code broken-link test plus existing fenced-block test. |
| F2-P3-1 | The final real-repository evidence records 88 Markdown files, including the checklist and both review decision notes; the count was reproduced after this evidence file existed. | Final real APES integration output in this note. |
| F2-P3-2 | Windows drive paths and reserved device names are rejected as local boundary violations without affecting real external URLs. | Drive, `NUL`, and external URL ending in `NUL` tests. |
| F2-P3-3 | Diagnostic messages are capped at 512 characters and structured context collections at 64 items, recursively bounding string values. | Diagnostic message and context bound test. |
| F2-P3-4 | Directory, Markdown, and fixture ordering uses `(casefold(name), name)` for a total deterministic order. | Casefold tie-breaker test. |
| F2-P3-5 | This note replaces the overstated pre-review security summary with the enforced closed-schema profile and the remaining limits below. | Documentation review plus the complete regression suite. |

## Verification Evidence

Executed from `E:\001项目\001Github\APES-Validator` on the remediation snapshot:

| Gate | Result |
| --- | --- |
| Ruff | Passed with no finding |
| Strict mypy | Passed with no issue in 13 source and test files |
| pytest | 71/71 passed |
| Branch coverage | 91.74%; threshold 90% |
| Bandit | No issue; 1300 lines scanned; no `nosec` exclusion |
| Dependency audit | No known third-party vulnerability; unpublished local package skipped as expected |
| uv lock | Consistent; 43 packages |
| Package build | sdist and wheel succeeded |
| Real APES check | Passed: 88 Markdown files, 8 fixtures, 0 artifacts, 0 edges |
| Real APES graph and `APES900` explanation | Passed with exit code 0 |
| Target integrity | All 103 non-Git files had identical SHA-256 inventories before and after validation |

## Implementer Self-Review Follow-up

The implementation author performed a second technical review after commit `73bbe6e`. This is additional implementation evidence, not independent approval. It found three related hardening gaps: custom Schema patterns and high-complexity structures could amplify CPU or memory use; lexically external paths could reach canonical resolution before rejection; and a single very long Markdown line could amplify regular-expression scanning. Malformed URL and control-character paths were covered while closing the same path boundary.

| Artifact | Identifier |
| --- | --- |
| Follow-up commit | `9d58a9ff3d94f80ff789a3db80963a691cf44bdf` |
| Follow-up predecessor | `73bbe6ede1deeb1d3c71deadcd8927da6e911be8` |
| APES artifact schema SHA-256 | `D6398943E352557E8D44337751746C3ABB2623C1DE0A10D613CF4B9B0799F0CE` |
| `uv.lock` SHA-256 | `170207EBF67649D584F7209934352927F413CC59E688581599B23427EA279785` |
| Built wheel SHA-256 | `1D26725E2998D9F9099259A80C41A23CF962CB057A67F66F7537B0B2C143FBA8` |
| Built sdist SHA-256 | `178E3675E0D7FF61C9F311C8B8962ABA121BAFF79DF13BA538FF088869C051C3` |

The follow-up restricts regular expressions to the reviewed canonical APES set, rejects high-complexity combinators, and bounds Schema and instance depth, node count, container width, and root `oneOf` branches. YAML aliases and cyclic containers are rejected. Markdown lines are limited to 64 KiB. Absolute, UNC, `file:`, control-character, malformed, and lexically escaping paths are rejected before canonical path resolution.

| Gate | Follow-up result |
| --- | --- |
| Ruff | Passed with no finding |
| Strict mypy | Passed with no issue in 13 source and test files |
| pytest | 87/87 passed |
| Branch coverage | 91.20%; threshold remained 90% |
| Bandit | No issue; 1578 lines scanned; no `nosec` exclusion |
| Dependency audit | No known third-party vulnerability; unpublished local package skipped as expected |
| uv lock | Consistent; 43 packages |
| Package build | sdist and wheel succeeded |
| APES integration | Passed on a byte-equivalent 103-file mirror: 88 Markdown files, 8 fixtures, 0 artifacts, 0 edges |
| Target integrity | All 103 mirror-file SHA-256 values were identical before and after validation |

The byte-equivalent mirror was used because the implementation workspace still contained an agent-created `.f2-self-review-staging` directory with hostile pytest fixtures; scanning that temporary directory correctly produced diagnostics. The mirror copied all 103 APES non-Git files except that temporary directory and preserved their bytes. An eligible reviewer should reproduce the check on a clean checkout of the APES repository.

On 2026-08-10 the maintainer explicitly approved removal of `.f2-self-review-staging`. A follow-up check against the real APES root passed with 88 Markdown files, 8 fixtures, 0 artifacts, 0 edges, and no diagnostic. All 103 non-Git file SHA-256 values were identical before and after `check`, `graph`, and `explain`; the temporary mirror is no longer the latest integration evidence.

## Residual Limits

- Markdown parsing remains intentionally bounded rather than a complete CommonMark implementation.
- The closed APES Schema profile intentionally excludes `$dynamicRef`, nested dialect/base declarations, external references, non-JSON-Pointer local references, unreviewed regular expressions, and high-complexity combinators.
- Existing APES documents still use legacy bullet headers, so the derived real graph remains empty until a separately reviewed metadata migration.
- Windows CPython 3.13.14 is the verified runtime; the declared Python 3.12 minimum still requires a future CI matrix before publication.
- The local unpublished package is absent from PyPI and is skipped by `pip-audit`; every third-party locked package is audited.
- Same-user replacement of a file between containment resolution and reading remains outside the current single-process CLI threat model.
- Exit code 3 deliberately exposes only the exception class; detailed debugging requires preservation of the reproducing fixture outside normal CI output.

## Re-review Boundary

The implementation author prepared this response and does not approve it. The eligible reviewer must check out the latest follow-up commit `9d58a9f`, reproduce the follow-up hashes and material tests, re-run the original hostile `file://` and loopback reference cases plus the new resource/path cases, inspect the closed registry and exception boundaries, and record a new decision in [`../../checklists/f2-independent-review.md#re-review-decision`](../../checklists/f2-independent-review.md#re-review-decision).

## Outcome

- Reviewer: Pending re-review
- Decision: Pending re-review
- Date: Pending
- Findings reference: Pending

F2 remains `In Review`, and F3 remains unstarted, until the independent re-review records an approval outcome.
