# standards/research/

- Status: Draft
- Version: v0.2
- Owner: APES Maintainers
- Last Updated: 2026-08-25
- Purpose: Standard for the Research stage of APES — how evidence is gathered, classified, verified, and reported so that a later reader can tell what was actually confirmed from what was merely repeated.

## Table of Contents

- [Purpose](#purpose)
- [Scope](#scope)
- [Normative Language](#normative-language)
- [R-1 Source Register](#r-1-source-register)
- [R-2 Three Orthogonal Classifications](#r-2-three-orthogonal-classifications)
- [R-3 Verification Log](#r-3-verification-log)
- [R-4 Field-Specific Verification Rules](#r-4-field-specific-verification-rules)
- [R-5 Reporting and Statistics](#r-5-reporting-and-statistics)
- [R-6 Research Gate Outcomes](#r-6-research-gate-outcomes)
- [Provenance](#provenance)
- [Status](#status)

## Purpose

This module describes how APES-compliant teams conduct research: gathering and evaluating evidence about technology, market, and ecosystem.

The stage has one objective. A reader who was not present during the research must be able to determine, for any individual claim, whether a primary source was directly accessed, and what remains unconfirmed. Every rule below exists to keep that determination possible.

The failure mode this standard prevents is a specific one: a reputable publisher being silently treated as proof that a particular claim is true. Publisher quality and claim confirmation are different measurements, and conflating them produces research that reads as verified while resting on third-party restatement.

## Scope

In scope:

- Research planning and source selection.
- Evidence classification and verification criteria.
- Citation, reproducibility, and access-window rules.
- Synthesis from multiple sources into a research note.
- Research Gate outcomes.

Out of scope:

- Conducting research on competitors; that work is tracked under [`../../research/competitors/`](../../research/competitors/README.md).
- Coverage and gap analysis, which consume research output rather than produce it.
- Tooling that automates any rule here. Determination of verification status is a human judgment.

## Normative Language

`MUST` and `MUST NOT` are absolute requirements. `SHOULD` indicates a requirement that may be waived only with a recorded reason. `MAY` is genuinely optional.

## R-1 Source Register

Every research effort MUST maintain a single source register. Each source occupies one row with a stable `SRC-NNN` identifier that MUST NOT be reused or renumbered once assigned.

Each row MUST record at minimum: identifier, title, source type, publisher or author, URL, publication date, access date, the research question it addresses, the three classifications of [R-2](#r-2-three-orthogonal-classifications), key evidence, contradictory evidence, limitations, and notes.

Three rules govern register content:

1. **Unknown dates are named, not guessed.** A publication date that cannot be observed MUST be recorded as `n.d.` with the reason, not inferred from surrounding context.
2. **Contradictory evidence MUST be recorded in the row it contradicts**, naming the conflicting source identifier. A contradiction recorded only in a separate document is not discoverable by a reader of the row.
3. **Volatile metrics MUST NOT be recorded as fixed facts.** Star counts, download counts, and commit totals change. Where such a figure is load-bearing, it MUST carry the access date and be attributed to its reporter.

Claims a source cannot support MUST NOT be drawn from it. A vendor page supports what the vendor says about itself; it does not support that the claim is true.

## R-2 Three Orthogonal Classifications

Every claim drawn from a source MUST carry three independent classifications. They measure different things and MUST NOT be collapsed into a single score.

**Source Reliability** — the kind of publisher, Level A through Level E. This describes the publisher, never the truth of any particular claim.

**Claim Verification** — the status of the specific claim as used in this register:

| Value | Meaning |
|---|---|
| `Verified` | The primary source was directly accessed AND this specific claim was drawn from it. |
| `Partially Verified` | The primary source was reachable in principle, but this claim rests on a third-party or community summary, or key fields were not directly observed. |
| `Unverified` | The primary source was unreachable in this access window; only third-party restatements exist. |
| `Contradicted` | The claim is contradicted by another reliable source. |
| `Inaccessible` | The primary source is paywalled or otherwise unfetchable, with no legally open alternative. |

**Claim Type** — what kind of evidence the source can support: official self-description, observable repository fact, independent empirical evidence, practitioner opinion, community signal, or marketing claim.

The governing rule, and the reason these fields are separate:

> **Source Reliability levels are NOT verification statuses.** A `Level A` source whose primary page was unreachable MUST carry `Claim Verification: Unverified`. It MUST NOT be reported as a verified source in any statistic.

## R-3 Verification Log

Every direct verification attempt MUST be recorded, including attempts that failed. A verification log that contains only successes is not evidence of verification; it is evidence of selective recording.

Each entry MUST carry a stable `VR-NNN` identifier and record: the source identifier, the URL targeted, the access date, the access result, the specific claims checked, the evidence location where the claim was actually found, license observed, maintenance signal observed, the outcome per [R-2](#r-2-three-orthogonal-classifications), and notes.

Notes are mandatory for every `Unverified` and `Inaccessible` entry, and MUST name what a future verifier would need in order to resolve it.

Two further requirements:

- **Access-window constraints MUST be recorded.** Where domains were systematically unreachable, the affected domains and the sources they block MUST be listed, so that a reader can distinguish absent evidence from absent effort.
- **Superseded entries MUST be preserved.** Re-verification appends a new entry; it MUST NOT overwrite the original. The prior claim becomes historical evidence and is labelled as such.

Where verification is supplied by an external reviewer with access the primary researcher lacked, those entries MUST be distinguishable from first-hand verification, and MUST record the reviewer identifier and access date.

The hard rule:

> **A verification MUST NOT be recorded as passed unless it was actually performed.** Where sufficient primary sources cannot be accessed, the correct outcome is [`RESEARCH AGAIN`](#r-6-research-gate-outcomes) with the unverifiable sources named for a future researcher.

## R-4 Field-Specific Verification Rules

Three fields are verified more often than the evidence supports, so each carries an explicit bar:

| Field | `Verified` only when |
|---|---|
| License | The LICENSE file, or the vendor's published license notice, was directly accessed. |
| Publication date | The date was drawn from a directly accessed release, tag, commit, or official announcement. |
| Maintenance status | Drawn from directly observed repository activity or an official deprecation notice. |

Maintenance status MUST be written with its access date — `Active at access date (YYYY-MM-DD)` — because the underlying fact expires. An archived or read-only project MUST be recorded as such even where repository metadata disagrees with the project's own notice; the official notice controls.

## R-5 Reporting and Statistics

Any statistic summarizing research MUST be reproducible from the register by counting rows. Where a summary and the rows disagree, the rows are authoritative and the summary MUST be corrected.

Statistics MUST separate the three classifications. A count of `Level A` sources is not a count of verified claims, and the two MUST NOT be presented as one figure.

Observation MUST be separated from inference. Where a conclusion is drawn from a limited sample, the sample bound MUST travel with the conclusion in the same sentence, not in a distant footnote.

Claims about market position, adoption, or share MUST NOT be made from self-reported figures. Such figures MAY be recorded, attributed to their reporter and labelled as not independently audited.

## R-6 Research Gate Outcomes

The Research stage exits through a gate with exactly three possible outcomes:

| Outcome | Condition |
|---|---|
| `PASS` | Every load-bearing claim carries `Verified`, or carries a recorded and accepted limitation. |
| `RESEARCH AGAIN` | Load-bearing claims remain `Unverified` or `Inaccessible`. The unresolved sources MUST be named. |
| `FAILED` | The research question cannot be answered with available evidence. |

The outcome MUST be recorded by a named human. An agent MAY prepare criterion state and identify evidence gaps; it MUST NOT record the outcome.

`RESEARCH AGAIN` is not a failure state and MUST NOT be treated as one. It is the correct, expected outcome whenever verification was attempted honestly and came up short. Downstream stages MUST NOT consume claims from a stage whose gate is `RESEARCH AGAIN` without repeating that qualification.

## Provenance

Every rule above is extracted from practice in this repository's own `research/` directory rather than authored speculatively. [R-2](#r-2-three-orthogonal-classifications) and [R-4](#r-4-field-specific-verification-rules) come from the Sprint 2.1 evidence correction, which introduced the three-field model after a single-field model proved unable to express a reliable publisher with an unconfirmed claim. [R-3](#r-3-verification-log) comes from the Sprint 2.2 verification log and the Sprint 2.3 external reconciliation. [R-5](#r-5-reporting-and-statistics) comes from the Sprint 3.1 coverage audit.

Per [`../README.md`](../README.md), promotion beyond `Draft` requires validation against at least one real case, recorded through an RFC in `governance/rfc/`. No such case exists yet.

## Status

Draft. This module contains standard text extracted from repository-local practice. It has not been validated against an external project, and no RFC has been raised to promote it.
