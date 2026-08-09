# F2 Independent Schema and Security Review Checklist

- Status: Remediation Ready for Re-review
- Version: v0.2
- Owner: Independent APES Reviewer
- Last Updated: 2026-08-10
- Purpose: Provide the human sign-off gate required before F2 Read-Only Validator can leave `In Review`.

## Table of Contents

- [Review Snapshot](#review-snapshot)
- [Reviewer Eligibility](#reviewer-eligibility)
- [Reproduction Commands](#reproduction-commands)
- [Schema Review](#schema-review)
- [Security Review](#security-review)
- [Behavior and Compatibility Review](#behavior-and-compatibility-review)
- [Independent Findings](#independent-findings)
- [Decision](#decision)
- [Remediation Response](#remediation-response)
- [Re-review Decision](#re-review-decision)

## Review Snapshot

- Runtime repository: `E:\001项目\001Github\APES-Validator`
- Review commit: `35d4ccf7acaa5881038f907d7a8b7eb59d47fd7b`
- Initial implementation commit: `b085162`
- APES artifact schema SHA-256: `02832F4C8A91A1C3F3764FB29FFAE3DF434A47F9CC70DF3B0C20660FB4C08160`
- `uv.lock` SHA-256: `6195EF0ADF5C46FFE3CD588E401413C1A9BA24BF5F3C6DD19D0A47A9E1900A0E`
- Wheel SHA-256: `185724D3B9218B9B0431A9FB85B55C45E75156CC1A39FE9074B624D4A577ED57`
- Evidence record: [`../governance/decisions/2026-08-09-f2-review-evidence.md`](../governance/decisions/2026-08-09-f2-review-evidence.md)
- Implementation task: [`../tasks/implementation-f2-read-only-validator.md`](../tasks/implementation-f2-read-only-validator.md)

The reviewer must verify that the checked-out commit and hashes match before signing.

## Reviewer Eligibility

- [x] I am not the author of commits `b085162` or `35d4ccf`. Both are authored by `longyuan <1507205727@qq.com>`; this review session produced neither.
- [x] I reviewed the implementation and contract rather than relying only on the implementation author's summary. Source, tests, schema, and dependency configuration were read directly, and independent adversarial fixtures were executed outside both repositories.
- [x] I will record any requested change before approving the gate.
- [x] I understand that approval closes F2 only; it does not authorize F3, write commands, publication, or deployment.

Independence caveat for the maintainer: the reviewed commits are recorded under the maintainer's own Git identity. This checklist attests only that the reviewer did not produce those commits and re-derived every conclusion from the artifacts. Organizational reviewer independence remains a maintainer attestation.

Reviewer name or handle: `Independent Schema & Security Reviewer (Claude Opus 5 audit session, commissioned by APES Maintainers)`

Review date: `2026-08-09`

## Reproduction Commands

Run from `E:\001项目\001Github\APES-Validator`:

```powershell
git status --short --branch
git rev-parse HEAD
uv sync --frozen --all-groups
uv run ruff check .
uv run mypy src tests
uv run pytest --basetemp .pytest-tmp --cov=apes_validator --cov-report=term-missing --cov-fail-under=90
uv run --with bandit bandit -r src -ll -ii
uv run --with pip-audit pip-audit
uv lock --check
uv build
$env:PYTHONUTF8='1'
uv run apes-validator check ..\AI-Product-Engineering --format text
uv run apes-validator graph ..\AI-Product-Engineering --format json
uv run apes-validator explain APES023 --format json
```

- [x] The checkout is clean and `HEAD` equals the review commit. All four frozen hashes (schema, `uv.lock`, wheel, HEAD) reproduced exactly; `uv build` regenerated a bit-identical wheel.
- [x] All commands complete with the documented outcome, with one reconciled deviation recorded as F2-P3-1.
- [x] The final APES check reports 8 fixtures and no error diagnostic. Markdown file count is 87, not the frozen 85; see F2-P3-1.

## Schema Review

- [x] The JSON Schema declares Draft 2020-12 and rejects undeclared fields. `$schema` is the 2020-12 dialect and `additionalProperties` is `false`.
- [x] Required fields match the F1 decision: ID, type, status, version, owners, relations, evidence, and update date. All nine are present in `required`.
- [ ] ID and type-prefix constraints are internally consistent for the current representative types. **Not met — see F2-P2-1.** Only `ADR`, `Source`, `Task`, and `Audit` are bound to a prefix; the other nine enum types accept any prefix.
- [ ] Semantic-version and date validation are enabled and tested. **Not met — see F2-P1-4.** The SemVer pattern is correct and `format: date` is correctly strict, but `"type": "string"` rejects the unquoted YAML date used by the repository's own canonical example.
- [x] Valid and invalid fixture expectations match the intended contract boundary. Both directions were re-derived; the 8 real fixtures classify correctly.
- [ ] Runtime rejects every non-fragment `$ref`; schema validation cannot trigger remote retrieval. **Not met — see F2-P0-1.** Non-fragment `$ref` is rejected, but `$dynamicRef` and subschema `$schema` are not, and both trigger real retrieval.
- [x] No implementation rule silently overrides ADR-0002 or the canonical schema. The runtime `TYPE_ORDER` layer table adds graph-direction semantics that the schema does not encode, but it neither relaxes nor contradicts the contract.

Schema findings: F2-P0-1, F2-P1-4, F2-P2-1 in [Independent Findings](#independent-findings).

## Security Review

- [ ] All supplied and discovered paths are resolved and contained within the selected repository root. **Not met — see F2-P0-1.** Markdown, link, schema, and fixture paths are contained, but a crafted schema reads a `file://` resource outside the root through the JSON Schema reference layer, which never passes through `is_within_root`.
- [x] Symbolic directories, Markdown files, schemas, and fixture paths cannot escape containment checks. Symlink and junction handling was re-read and the four existing tests were reproduced.
- [x] YAML uses safe loading; dangerous Python tags are rejected and tested. `yaml.safe_load` is the only loader; `!!python/object/apply` is rejected. A YAML alias expansion bomb was additionally tested and is safe, because PyYAML keeps aliases as shared references.
- [x] Repository Markdown, YAML, JSON, hooks, and commands are treated only as data and are never executed. No execution path was found for repository content.
- [x] Markdown, front matter, schema, and fixture sizes have explicit resource limits, and each limit is enforced before the corresponding parse. The limits bound size but not nesting depth; see F2-P1-2.
- [x] Dependency-cycle detection is iterative and handles the 2000-node adversarial test without recursion failure. The explicit-stack traversal was read and the test reproduced.
- [ ] Runtime source contains no subprocess, shell execution, model SDK, telemetry, database, or network client. **Qualified — see F2-P0-1.** First-party source is clean; a repository-wide search found no `subprocess`, `eval`, `exec`, dynamic import, socket, or HTTP client, and the only `urllib` import is `urllib.parse`. However the process does perform outbound HTTP at runtime through the unrestricted default `jsonschema` retrieval registry.
- [x] Validation does not modify the target repository; repeat results and SHA-256 inventories remain unchanged. An independent 102-file SHA-256 inventory of the APES repository was identical before and after validation, `.git/index` included, and a hostile fixture repository was likewise unmodified.
- [x] Bandit reports no issue and dependency audit reports no known vulnerability for third-party packages. Both reproduced: 1060 lines scanned with no `nosec`, and no known vulnerabilities.
- [x] Diagnostic output does not expose file contents or secrets beyond path, line, code, and bounded context. Exposure is bounded by the 64 KiB front matter limit and originates in the scanned repository; see F2-P3-3.

Security findings: F2-P0-1, F2-P1-1, F2-P1-2, F2-P1-3, F2-P3-3 in [Independent Findings](#independent-findings).

## Behavior and Compatibility Review

- [x] Text and JSON diagnostics are deterministic and stable enough for machine consumption. Repeated `check --format json` and `graph --format dot` runs against the real repository were byte-identical, and all three collections are explicitly sorted in `finalize`. One cross-platform ordering caveat is recorded as F2-P3-4.
- [x] `graph` output is derived and disposable; it does not become a second source of truth. Nothing is persisted; all output goes to stdout.
- [x] Exit codes 0, 1, and 2 match documented success, validation-error, and CLI-input behavior. Verified: clean pass 0, error diagnostics 1, invalid `--format` 2, unknown diagnostic code 2. An undocumented collision on code 1 is recorded as F2-P2-2.
- [x] Existing APES legacy headers remain readable and unmoved. All 87 Markdown files parsed without diagnostics and no file changed.
- [x] The current zero-node real APES graph is understood as a migration-state limitation, not a parser success claim. F2-P1-4 shows the migration cannot in fact succeed as documented until the date contract is reconciled.
- [x] Rollback consists of stopping use of the independent tool; canonical APES artifacts require no repair. Confirmed by the unchanged-inventory evidence.

Compatibility findings: F2-P2-2, F2-P2-3, F2-P3-1, F2-P3-2, F2-P3-4 in [Independent Findings](#independent-findings).

## Independent Findings

Thirteen findings were confirmed by execution, not by inspection alone. Every reproduction used fixtures created outside both repositories; neither repository was modified. Unless stated otherwise, file paths refer to `E:\001项目\001Github\APES-Validator` at commit `35d4ccf`.

### F2-P0-1 — Untrusted schema reaches the network and reads files outside the repository root

- Severity: P0, blocking.
- Location: `E:\001项目\001Github\APES-Validator\src\apes_validator\validator.py:393` (the guard tests only the literal key `$ref`) and `:371` (the validator is constructed on the unrestricted default `jsonschema` registry).
- Evidence: `_external_schema_refs({"properties": {"id": {"$dynamicRef": "https://attacker.invalid/evil.json"}}})` returns `[]`, so the pre-validation guard never sees the reference. `jsonschema` then resolves it through `_REMOTE_WARNING_REGISTRY`, whose `retrieve` hook is `_warn_for_remote_retrieve` and calls `urlopen` on any unresolved URI.
- Reproduction: place a `schemas/artifact-metadata.schema.json` containing `{"properties": {"id": {"$dynamicRef": "<uri>"}}}` in any repository and run `apes-validator check` against it. With `<uri>` set to a `file://` path outside the root, the external document is fetched and applied as a schema, producing `'SRC-001' is not of type 'integer'` from a planted `{"type": "integer"}` file. With `<uri>` set to `http://127.0.0.1:1/evil.json`, the process performs a real `socket.connect` and fails with `ConnectionRefusedError [WinError 10061]`. The same escape works through a subschema `$schema` value, which is likewise unguarded.
- Impact: repository content controls both an outbound request to an arbitrary URL and a read of an arbitrary local JSON document outside the selected root. This contradicts ADR-0003 Security Boundary, which states that runtime performs no network call and that every path must remain inside the repository root, and it contradicts the frozen claim that non-fragment references are rejected before validation. The realistic exposure is a validator run in CI over an untrusted branch or pull request, where the request doubles as a reachability beacon and the fetched content can steer diagnostics.
- Recommended handling: build the validator on an explicit closed registry, for example `referencing.Registry()` with no `retrieve` hook, so that any unresolved reference raises instead of being fetched. Then extend the pre-validation deny-list beyond `$ref` to `$dynamicRef` and to any non-root `$schema`, and add regression tests for both keywords using a `file://` target and a loopback target.

### F2-P1-1 — Whitespace-only Markdown link target crashes the validator

- Severity: P1, blocking.
- Location: `E:\001项目\001Github\APES-Validator\src\apes_validator\validator.py:237`.
- Evidence: `LINK_PATTERN` accepts `[^)]+`, so a link whose target is only whitespace yields the empty string after `.strip()`; `"".split(maxsplit=1)[0]` then raises `IndexError: list index out of range`. The triggering form, and two neighbouring forms that must stay covered, are shown below. This block is fenced deliberately, because a fenced block is the only place these can be written safely in this repository, as F2-P2-3 explains.

```markdown
[label]( )
[label]()
[label](<>)
```

- Reproduction: create a `README.md` containing the first line above and run `apes-validator check` on its directory. The command prints a traceback and exits 1. The second form does not match `LINK_PATTERN` at all and the third is handled correctly; only the whitespace-only target crashes.
- Impact: a single malformed link, which is an ordinary authoring typo rather than an attack, aborts the entire validation run before any diagnostic is emitted. In CI the traceback is reported as a normal validation failure. This finding was reproduced unintentionally during the review itself: an early draft of this checklist quoted the malformed link in inline code and crashed the validator when the reviewer ran it over the APES repository.
- Recommended handling: treat an empty or whitespace-only target as an unresolvable link and emit `APES010`, and add regression tests for all three forms above.

### F2-P1-2 — Deeply nested JSON or YAML crashes the validator with `RecursionError`

- Severity: P1, blocking.
- Location: `E:\001项目\001Github\APES-Validator\src\apes_validator\validator.py:365` (schema), `:450` (fixture), and `:128` (front matter). The surrounding `except` clauses at `:372` and `:451` catch `OSError`, `UnicodeError`, `ValueError`, `json.JSONDecodeError`, `SchemaError`, and `yaml.YAMLError`, none of which is a superclass of `RecursionError`.
- Evidence: a 117 KiB schema of 60000 nested arrays raises `RecursionError: maximum recursion depth exceeded while decoding a JSON array`; the same payload as a contract fixture raises it at `:450`; a 39 KiB front matter of 20000 nested YAML flow sequences raises it inside `parse_front_matter`. All three are far below the 1 MiB and 64 KiB limits, because the limits bound byte size and not nesting depth. The recursive generator `_external_schema_refs` at `:390` has the same exposure for any schema deep enough to survive `json.loads`.
- Reproduction: write `"[" * 60000 + "]" * 60000` to `schemas/artifact-metadata.schema.json` and run `apes-validator check`.
- Impact: untrusted repository content aborts validation with an unhandled traceback. This is the same denial-of-validation class as F2-P1-1 but is deliberately reachable and is not covered by any existing test.
- Recommended handling: catch `RecursionError` alongside the existing exception set and map it to `APES004` or `APES031`, or add an explicit nesting-depth bound checked before parsing. Convert `_external_schema_refs` to an iterative walk. Add regression tests for deep JSON in both the schema and a fixture, and for deep YAML front matter.

### F2-P1-3 — Dangling local `$ref` pointer passes `check_schema` and crashes during validation

- Severity: P1, blocking.
- Location: `E:\001项目\001Github\APES-Validator\src\apes_validator\validator.py:370` (`check_schema` accepts the schema), with the failure surfacing at `:691` for front matter and `:461` for fixtures.
- Evidence: a schema whose `properties.id` is `{"$ref": "#/$defs/absent"}` is accepted by `Draft202012Validator.check_schema`, because the 2020-12 metaschema does not verify that a JSON pointer resolves. The first `iter_errors` call then raises `jsonschema.exceptions._WrappedReferencingError: PointerToNowhere`, which is not caught. The same occurs when an external `$id` rebases the fragment.
- Reproduction: set `properties.id` to `{"$ref": "#/$defs/absent"}` in the repository schema and run `apes-validator check`.
- Impact: a fragment-only reference, which the current guard explicitly treats as the safe case, still escapes the schema-loading error boundary and crashes at validation time. The `APES031` diagnostic that exists precisely for invalid schemas is bypassed.
- Recommended handling: resolve all internal pointers during schema loading, or wrap the `iter_errors` calls so that a referencing failure is reported as `APES031` against the schema rather than raised. Add a regression test for a dangling local pointer.

### F2-P1-4 — Canonical unquoted YAML date is rejected by the artifact contract

- Severity: P1, blocking.
- Location: `E:\001项目\001Github\AI-Product-Engineering\schemas\artifact-metadata.schema.json:77` (`"type": "string"` with `"format": "date"`), consumed at `E:\001项目\001Github\APES-Validator\src\apes_validator\validator.py:691`.
- Evidence: `yaml.safe_load` resolves an unquoted `last_updated: 2026-08-09` to a Python `datetime.date`, not a string, so validation fails with `datetime.date(2026, 8, 9) is not of type 'string'`. Quoting the value yields `ok=True` with one artifact. The repository's own canonical front matter example at `E:\001项目\001Github\AI-Product-Engineering\docs\repository-evolution-plan.md:845` writes the date unquoted.
- Reproduction: validate a document whose front matter contains `last_updated: 2026-08-09` unquoted, then repeat with `last_updated: '2026-08-09'`.
- Impact: the documented canonical metadata form cannot pass the contract that is meant to accept it. The defect is invisible today for three reinforcing reasons: all eight fixtures are JSON, which has no date type; `tests/helpers.py:32` serialises through `yaml.safe_dump`, which quotes the value; and the real repository still has zero front matter blocks. It would surface immediately at the first metadata migration, which is exactly the milestone F2 exists to support. The `format: date` checker itself is correct and was verified to reject `20260809` and `2026-W32-1`.
- Recommended handling: decide the contract explicitly and record it. Either accept both forms, for example by allowing a date-typed value in the schema or normalising `datetime.date` to an ISO string before validation, or keep string-only and state the quoting requirement in the schema documentation and the compatibility mapping. Either way add a YAML-sourced fixture, since JSON fixtures structurally cannot cover this.

### F2-P2-1 — Type-to-prefix binding covers only four of thirteen artifact types

- Severity: P2, non-blocking but should be recorded.
- Location: `E:\001项目\001Github\AI-Product-Engineering\schemas\artifact-metadata.schema.json:82` through `:158`.
- Evidence: the `allOf` block binds a prefix only for `ADR`, `Source`, `Task`, and `Audit`. The remaining nine enum types are unconstrained beyond the shared `artifactId` pattern. Confirmed by execution: `type: RFC` with `id: SRC-999`, `type: Standard` with `id: GAP-1`, `type: Release` with `id: TASK-1`, `type: Verification` with `id: ADR-1`, and `type: Schema` with `id: REL-1` all validate cleanly, while `type: ADR` with `id: SRC-1` is correctly rejected.
- Reproduction: validate a document with `type: RFC` and `id: SRC-999` and a quoted `last_updated`.
- Impact: identifiers can contradict their declared type. Because the graph keys on the identifier while `TYPE_ORDER` keys on the type, a mismatched pair produces a technically valid but misleading dependency graph. This is a contract completeness gap rather than a safety gap.
- Recommended handling: either bind the remaining nine types, or state in the schema description that prefix binding is intentionally partial for the current representative types and record which prefix maps to `Verification`, given that `EV` appears in the identifier pattern but in no `if`/`then` pair.

### F2-P2-2 — Unhandled crashes exit with code 1, indistinguishable from a validation failure

- Severity: P2, non-blocking but should be recorded.
- Location: `E:\001项目\001Github\APES-Validator\src\apes_validator\cli.py:98`, `:128`, and `:168`; no command wraps `validate_repository` in an error boundary.
- Evidence: the crash in F2-P1-1 exits 1, and a clean validation failure also exits 1. Documented codes are otherwise correct: clean pass 0, invalid `--format` 2, unknown diagnostic code 2.
- Reproduction: compare `$LASTEXITCODE` after checking the crashing repository from F2-P1-1 against one containing only a broken link.
- Impact: an automated consumer cannot distinguish "the repository has errors" from "the validator broke", so crash regressions can hide indefinitely behind expected CI failures. This amplifies F2-P1-1, F2-P1-2, and F2-P1-3.
- Recommended handling: add a top-level handler that reports an internal error and exits with a distinct code, for example 3, and document that code in ADR-0003.

### F2-P2-3 — Inline code spans are not excluded from link extraction

- Severity: P2, non-blocking but should be recorded.
- Location: `E:\001项目\001Github\APES-Validator\src\apes_validator\validator.py:100` through `:109`.
- Evidence: `extract_links` tracks fenced blocks through `FENCE_PATTERN` but has no notion of an inline code span, so a link written inside backticks is extracted as a real link. A document containing a backtick-quoted link to `does-not-exist.md` reports `ERROR APES010 README.md:3 local link target does not exist: does-not-exist.md`, while the same link inside a fenced block is correctly ignored.
- Reproduction: create a Markdown file whose prose quotes a link to a non-existent file inside single backticks and run `apes-validator check`.
- Impact: false-positive broken-link diagnostics in exactly the documents a standards repository is most likely to contain, namely documentation that discusses Markdown or link syntax. Combined with F2-P1-1, quoting a malformed link does not merely produce a false positive but aborts the run; that is how F2-P1-1 was first observed during this review.
- Recommended handling: strip inline code spans before link extraction, or document that inline code is intentionally scanned so that authors know to use fenced blocks. The existing residual limit about the bounded Markdown parser should name this case explicitly.

### F2-P3-1 — Frozen Markdown file count is no longer reproducible

- Severity: P3.
- Location: `E:\001项目\001Github\AI-Product-Engineering\governance\decisions\2026-08-09-f2-review-evidence.md:46`.
- Evidence: the frozen record states 85 Markdown files; an independent run reports 87. The difference is fully accounted for: `checklists/f2-independent-review.md` was created at 00:59:54 and `governance/decisions/2026-08-09-f2-review-evidence.md` at 00:59:56, both after the recorded `check` run at commit time 00:58:37. Fixture count, artifact count, edge count, and the zero-diagnostic result all reproduce exactly.
- Impact: none technically; the drift is caused by the review artifacts themselves. It does mean the frozen number is self-invalidating and cannot be reproduced by any later reviewer.
- Recommended handling: record counts that exclude the review artifacts, or note that the Markdown count grows as review records are added.

### F2-P3-2 — Drive-absolute and device link targets are silently skipped

- Severity: P3.
- Location: `E:\001项目\001Github\APES-Validator\src\apes_validator\validator.py:252` through `:256`.
- Evidence: `urlsplit("C:/Windows/win.ini").scheme` is `"c"`, so a drive-absolute Windows link is classified as an external URL and skipped without a diagnostic, while the POSIX-style `/Windows/win.ini` is correctly reported as `APES011`. A link to the Windows device name `NUL` resolves inside the root and is accepted as valid.
- Reproduction: validate a document containing `[b](C:/Windows/win.ini)` and `[d](NUL)`.
- Impact: missed detection only. No read occurs in either case, and containment is not breached. Percent-encoded traversal such as `%2e%2e/%2e%2e/outside.md` is correctly decoded and rejected.
- Recommended handling: treat a single-letter scheme on Windows as a local absolute path and report it, and exclude reserved device names from link resolution.

### F2-P3-3 — Front matter values are echoed verbatim into diagnostics

- Severity: P3.
- Location: `E:\001项目\001Github\APES-Validator\src\apes_validator\validator.py:701`.
- Evidence: `APES021` carries the raw `jsonschema` message, which embeds the offending instance value. A 2000-character identifier is reproduced in full in the diagnostic text.
- Impact: bounded by the 64 KiB front matter limit, and the content originates in the repository being validated rather than crossing a privilege boundary. It does mean a single run can emit tens of kilobytes of repository text into CI logs.
- Recommended handling: truncate echoed instance values to a fixed length in the diagnostic message.

### F2-P3-4 — Directory and file ordering is not total on case-sensitive filesystems

- Severity: P3.
- Location: `E:\001项目\001Github\APES-Validator\src\apes_validator\validator.py:152` and `:179`.
- Evidence: traversal sorts with `key=str.casefold`. On Windows, names differing only in case cannot coexist, so ordering is total and output was verified byte-identical across runs. On a case-sensitive filesystem, `A.md` and `a.md` compare equal under the key, and Python's stable sort then preserves the `os.walk` order, which is filesystem-dependent.
- Impact: a determinism claim that holds on the verified platform but is not guaranteed on Linux or macOS. Diagnostics are re-sorted in `finalize`, so the residual exposure is limited to traversal-order effects such as which duplicate identifier is reported as the original.
- Recommended handling: sort on `(str.casefold(name), name)` to make the ordering total, and cover it in the future CI matrix that the residual limits already anticipate.

### F2-P3-5 — Residual limits omit the crash vectors and the retrieval channel

- Severity: P3.
- Location: `E:\001项目\001Github\AI-Product-Engineering\governance\decisions\2026-08-09-f2-review-evidence.md:67` through `:74`.
- Evidence: the residual-limits list discloses the bounded Markdown parser, the legacy-header migration state, the single-platform runtime check, the unpublished local package, and the TOCTOU exclusion. It does not disclose that untrusted input can raise unhandled exceptions, that nesting depth is unbounded, or that schema reference resolution is not confined to the repository root. The adversarial-evidence list states that non-fragment `$ref` values are rejected before validation, which is true only for the `$ref` keyword.
- Impact: the freeze record overstates the security boundary in the one area a reviewer is most likely to rely on it.
- Recommended handling: after F2-P0-1 through F2-P1-3 are fixed, restate the reference-containment claim in terms of what is actually enforced, and list any remaining unbounded-input cases.

## Decision

Select exactly one:

- [ ] **Approve F2.** Schema and security boundaries are acceptable for closing F2.
- [ ] **Approve with recorded follow-up.** F2 may close; non-blocking items are listed below.
- [x] **Request changes.** F2 remains `In Review`; blocking findings are listed below.

Blocking or follow-up findings:

- Blocking: F2-P0-1, F2-P1-1, F2-P1-2, F2-P1-3, F2-P1-4. F2-P0-1 alone invalidates the stated security boundary, because untrusted repository content drives both an outbound network request and a read outside the repository root. The four P1 findings are one correctness defect at the F1/F2 contract boundary plus three unhandled-crash classes on untrusted input.
- Follow-up, not blocking: F2-P2-1, F2-P2-2, F2-P2-3, F2-P3-1, F2-P3-2, F2-P3-3, F2-P3-4, F2-P3-5.
- Re-review scope once fixes land: the reference-containment control and its regression tests, the exception boundary and exit-code contract, the date contract with a YAML-sourced fixture, and a restated residual-limits list. The frozen snapshot must be re-cut, since every fix changes `HEAD` and the wheel hash.

What the review confirmed as sound, so that a re-review need not re-derive it: the frozen snapshot reproduced exactly on all four hashes and `uv build` produced a bit-identical wheel; every automated gate reproduced its recorded result, including 40/40 tests at 93.98% branch coverage, clean Ruff, clean strict mypy, clean Bandit over 1060 lines, no known dependency vulnerabilities, and a consistent 43-package lock; the read-only guarantee held, with an independent 102-file SHA-256 inventory of the APES repository identical before and after validation and a hostile fixture repository likewise unmodified; output was byte-identical across repeated runs; safe YAML loading rejects Python object tags and is not vulnerable to alias expansion bombs; cycle detection is genuinely iterative; symbolic-path containment holds for directories, Markdown files, schemas, and fixtures; percent-encoded traversal is decoded and rejected; and the first-party source contains no execution, network, or write primitive of any kind.

Reviewer signature or recorded approval reference: `Independent F2 audit, 2026-08-09, against commit 35d4ccf7acaa5881038f907d7a8b7eb59d47fd7b. Decision: Request changes. Thirteen findings recorded in Independent Findings above; five are blocking.`

## Remediation Response

Implementation-author response only; this section does not alter the initial `Request changes` decision or establish reviewer approval.

- Remediation commit: `73bbe6ede1deeb1d3c71deadcd8927da6e911be8`
- APES artifact schema: `urn:apes:schema:artifact-metadata:0.2.0`
- APES artifact schema SHA-256: `D6398943E352557E8D44337751746C3ABB2623C1DE0A10D613CF4B9B0799F0CE`
- `uv.lock` SHA-256: `170207EBF67649D584F7209934352927F413CC59E688581599B23427EA279785`
- Wheel SHA-256: `B05AF816963627C25A32EB069B92599980AAD262DD9D3965936738E30BC60361`
- Detailed disposition and verification: [`../governance/decisions/2026-08-09-f2-remediation-evidence.md`](../governance/decisions/2026-08-09-f2-remediation-evidence.md)

The response addresses all thirteen original findings. The P0 retrieval path is closed by an explicit no-retrieval Registry and a restricted APES Schema profile. The P1 crash and YAML-date cases have bounded diagnostics and regression coverage. The P2/P3 findings are covered by exhaustive type-prefix constraints, exit code 3 / `APES900`, inline-code masking, Windows-path handling, bounded output, total ordering, reproducible counts, and restated residual limits.

The remediation run passed 71/71 tests at 91.74% branch coverage, Ruff, strict mypy, Bandit, dependency audit, lock verification, build, and a real APES 103-file hash-preservation check. These are implementer claims until independently reproduced.

The implementation author's follow-up review added resource- and path-complexity hardening. The latest review target supersedes the remediation commit as `HEAD` while preserving the original response above:

- Follow-up commit: `9d58a9ff3d94f80ff789a3db80963a691cf44bdf`
- APES artifact schema SHA-256: `D6398943E352557E8D44337751746C3ABB2623C1DE0A10D613CF4B9B0799F0CE`
- `uv.lock` SHA-256: `170207EBF67649D584F7209934352927F413CC59E688581599B23427EA279785`
- Wheel SHA-256: `1D26725E2998D9F9099259A80C41A23CF962CB057A67F66F7537B0B2C143FBA8`
- sdist SHA-256: `178E3675E0D7FF61C9F311C8B8962ABA121BAFF79DF13BA538FF088869C051C3`
- Gates: 87/87 tests, 91.20% branch coverage, Ruff, strict mypy, Bandit over 1578 lines, dependency audit, 43-package lock check, and build passed.
- Integration: after the temporary staging directory was removed, the real 103-file APES root reported 88 Markdown files, 8 fixtures, no diagnostic, and identical before/after hashes. Reproduce this result against a clean APES checkout during independent review.

## Re-review Decision

The eligible independent reviewer must select exactly one after checking the latest follow-up snapshot:

- [ ] `HEAD`, Schema, `uv.lock`, wheel, and sdist match the follow-up snapshot.
- [ ] The original `file://`, loopback `$dynamicRef`, and nested `$schema` reproductions are rejected before retrieval; no file or socket access occurs.
- [ ] Empty links, deep JSON/YAML, dangling local references, and unquoted YAML dates produce the documented bounded outcomes.
- [ ] All thirteen type-prefix pairs, exit code 3, inline code, Windows paths, diagnostic bounds, and total ordering match the remediation record.
- [ ] Ruff, strict mypy, 87 tests, coverage, Bandit, dependency audit, lock check, build, and real APES validation reproduce materially.
- [ ] Unreviewed Schema patterns/combinators, over-wide or over-deep structures, YAML aliases, long Markdown lines, absolute/UNC paths, malformed URLs, and control-character paths produce bounded diagnostics.
- [ ] The real APES check reports 88 Markdown files, 8 fixtures, no diagnostic, and an unchanged 103-file SHA-256 inventory.

- [ ] **Approve F2 remediation.** All original blocking findings are resolved and the revised boundaries are acceptable for closing F2.
- [ ] **Approve remediation with recorded follow-up.** F2 may close; remaining non-blocking items are recorded below.
- [ ] **Request further changes.** F2 remains `In Review`; unresolved blocking findings are recorded below.

Re-reviewer name or handle: `____________________________`

Re-review date: `____________________________`

Re-review findings: `________________________________________________________`

Re-review signature or recorded approval reference: `________________________`
