# ADR-0002 — Schema-First, File-Native Reference Architecture

- **Title:** Schema-first, file-native, Git-backed architecture with deterministic tooling and generated agent adapters
- **Status:** Accepted
- **Date:** 2026-08-05
- **Accepted:** 2026-08-07

## Table of Contents

- [Context](#context)
- [Decision](#decision)
- [Consequences](#consequences)
- [Alternatives Considered](#alternatives-considered)
- [Evidence](#evidence)
- [Review and Implementation Gate](#review-and-implementation-gate)
- [Acceptance Record](#acceptance-record)

## Context

ADR-0001 positions APES as a vendor-neutral, evidence-driven documentation and standards repository and defers CLI, MCP, IDE-extension, and website implementation. Foundation 0.1 / 0.1.1 defined a six-layer architecture but did not specify how future contracts, validators, workflows, and agent integrations should be implemented.

Foundation 0.2 inspected four adjacent open-source projects:

- GitHub Spec Kit: extensible CLI, Markdown artifact pipeline, offline templates, workflows, presets, bundles, and agent projections. `SRC-025`
- OpenSpec: proposal / spec / design / tasks change package with apply and archive lifecycle. `SRC-026`
- BMAD-METHOD: full progressive lifecycle with readiness, review, and retrospective gates. `SRC-053`
- Agent OS: standards discovery, YAML index, selective injection, profile inheritance, and agent-specific command projection. `SRC-054`

All four make Markdown operational through structured metadata, templates, indexes, schemas, or workflow assets. None of the inspected cores provides the complete APES evidence chain from source registration through verification, audit, decision, standard, and release. The detailed evidence boundary and APES-oriented inferences are in `research/competitors/open-source-reference-comparison.md`.

APES needs a reference architecture that can eventually support deterministic validation and selective agent context without making a tool, agent, or hosted service the source of truth.

## Decision

If this ADR is accepted, APES will use the following architecture contract:

1. **Canonical artifacts remain repository files.** Human-readable Markdown is canonical. A deliberately small YAML front matter block carries machine-checkable metadata.
2. **Schemas precede engines.** JSON Schema defines artifact metadata and relationship contracts before any validator, workflow evaluator, adapter, or report engine is implemented.
3. **Git remains the system of record.** No database, hosted API, or remote state service is required for canonical APES operation.
4. **The artifact graph is derived.** IDs and typed relationships are read from canonical artifacts; generated indexes and graphs are disposable outputs, not independently edited truth.
5. **Validation is deterministic and read-only first.** Schema, identifier, dependency, status-transition, link, and citation checks do not require an LLM and do not write files by default.
6. **Workflows and gates are declarative.** Fast and full paths declare inputs, outputs, validators, human approvals, evidence requirements, and rollback behavior. Agent prompts do not define canonical gates.
7. **Agent integrations are projections.** A generic adapter contract renders canonical artifacts into agent-specific instructions. Generated projections are replaceable, identify their sources and generator version, and cannot change Meta or Foundation rules.
8. **Runtime tooling remains separate and deferred.** If validation evidence justifies a CLI, it will live in a separately governed tooling repository and consume the contracts defined by APES. No runtime implementation is authorized by this ADR while it is `Proposed`.
9. **The recommended first runtime candidate is Python 3.12+.** Typer / Rich, PyYAML, `jsonschema`, `uv` / Hatchling, pytest, Ruff, and mypy form the initial evaluation stack. Final adoption requires an implementation ADR or an accepted amendment based on prototype evidence.
10. **Offline and safe-by-default operation is mandatory.** No model SDK, telemetry, remote execution catalog, arbitrary post-install hook, destructive migration, or implicit file overwrite belongs in the core.

## Consequences

Positive:

- Canonical artifacts stay readable without APES tooling.
- The standard remains vendor-neutral and agent integrations remain replaceable.
- Deterministic checks can enforce traceability without asking an LLM to judge machine-verifiable facts.
- Git provides review, history, rollback, and offline operation without infrastructure cost.
- A standards index and selective projections can reduce unnecessary agent context.
- The design preserves the Source Register → Verification → Coverage → Audit → Decision → Standard → Release chain as an APES differentiator.

Negative and risks:

- Markdown plus front matter can drift unless schema validation becomes reliable.
- JSON Schema and graph rules introduce concepts contributors must learn.
- A separate tooling repository adds version coordination between contracts and their implementation.
- Generated agent projections can confuse users unless they are visibly marked and reproducible.
- Python is not the dominant runtime in OpenSpec or BMAD-METHOD; the recommendation must be tested rather than assumed.
- File-native storage will be slower than a database for very large graphs; APES does not yet have evidence that such scale exists.

Operational consequences:

- Foundation 0.2 creates only documentation, research evidence, and this Proposed ADR.
- The first follow-up is a minimal contract prototype with representative fixtures, not a CLI.
- Existing paths do not move and existing Markdown remains valid during the prototype.
- A later runtime must reject path traversal, resolve symlinks / junctions safely, avoid shell execution, and show dry-run diffs before any write.
- Every future adapter must prove that deleting its generated output does not delete canonical APES content.

## Alternatives Considered

### Alternative A — Adopt GitHub Spec Kit as the APES runtime

Pros:

- Mature portable CLI pattern, cross-agent integrations, offline assets, and rich composition. `SRC-025`

Cons:

- Core focus begins at specification rather than APES's evidence and research stages.
- APES would inherit a broad extension / preset / workflow / bundle model before validating its own minimal contract.
- Direct adoption now conflicts with ADR-0001's standard-first boundary.

Decision: rejected as a direct runtime; selected as an architectural reference.

### Alternative B — Adopt OpenSpec change packages and Node runtime directly

Pros:

- Compact, reviewable, brownfield-friendly change lifecycle. `SRC-026`

Cons:

- The change envelope does not include APES's full evidence and governance chain.
- Node / post-install behavior adds runtime and supply-chain surface before a validator requirement is proven.
- Cross-repository Stores are beta and would create a new source-of-truth choice.

Decision: reject direct adoption; adopt the append-only change-package pattern.

### Alternative C — Adopt BMAD-METHOD's full agent and workflow system

Pros:

- Broad lifecycle coverage, progressive artifacts, readiness gates, and scalable workflow depth. `SRC-053`

Cons:

- Large agent / role / workflow surface increases ceremony and context cost.
- APES would risk becoming an agent framework instead of a standard.
- Installer, website, and orchestration scope exceed the current stage.

Decision: reject framework adoption; adopt progressive context and readiness-gate patterns.

### Alternative D — Use Agent OS as a prompt-only implementation

Pros:

- Lightweight Markdown / YAML approach, standards index, selective injection, and human confirmation. `SRC-054`

Cons:

- Inspected installation projects commands into an agent-specific directory.
- Shell-first behavior is less uniform for Windows.
- Mining local patterns without APES evidence gates could formalize poor conventions.

Decision: reject prompt files as the canonical runtime; adopt indexed standards and generated projections.

### Alternative E — Hosted database and web control plane

Pros:

- Centralized querying, collaboration, and graph traversal at scale.

Cons:

- Adds accounts, network, hosting, security, privacy, backup, and vendor-dependency concerns.
- Breaks the current offline, Git-native, documentation-first model.
- No evidence shows APES currently needs that scale.

Decision: rejected.

## Evidence

- `SRC-025` — GitHub Spec Kit repository, README, and `pyproject.toml`; direct access 2026-08-05.
- `SRC-026` — OpenSpec repository, README, and `package.json`; direct access 2026-08-05.
- `SRC-053` — BMAD-METHOD repository, workflow map, and `package.json`; direct access 2026-08-05.
- `SRC-054` — Agent OS repository, commands, configuration, and shell installer; direct access 2026-08-05.
- [`../../research/competitors/open-source-reference-comparison.md`](../../research/competitors/open-source-reference-comparison.md) — detailed comparison and inference boundary.
- [`../../docs/repository-evolution-plan.md`](../../docs/repository-evolution-plan.md) — sections 24 through 28 implement the proposal at plan level.

## Review and Implementation Gate

This section records the review questions that had to be closed before acceptance.

Before acceptance, maintainers must decide:

- whether YAML front matter plus JSON Schema is the canonical contract format;
- whether the first tooling prototype belongs in a separate repository from day one;
- whether Python should remain the first runtime candidate after a minimal spike;
- which existing APES artifacts form the initial compatibility fixture set;
- who reviews schema and security boundaries independently.

No CLI, engine, workflow, adapter, website, build pipeline, application source, or runtime dependency is authorized until its separately scoped phase is approved.

## Acceptance Record

The APES maintainer approved the implementation Sprint on 2026-08-07. That approval accepts this ADR and authorizes only Foundation 0.3 / F1 Contract Prototype as scoped in [`../../tasks/foundation-0-3-contract-prototype.md`](../../tasks/foundation-0-3-contract-prototype.md).

The review questions are resolved as follows:

- YAML 1.2 front matter parsed as an object and validated by JSON Schema 2020-12 is the canonical contract direction.
- Contract schemas and compatibility fixtures belong in this repository. Runtime tooling, beginning with F2, remains separately governed and is not authorized by this acceptance.
- Python 3.12+ remains the first runtime candidate; F1 adopts no runtime or production dependency.
- The initial compatibility set covers an ADR, a task, a source record, and an audit record derived from existing APES artifacts.
- Before F2 exits review, schema and security boundaries require review by an APES maintainer who was not the implementation author.

Acceptance does not change Sprint 2 (`In Review`), the Research Gate (`RESEARCH AGAIN`), or the prohibition on CLI, MCP, IDE-extension, website, agent-runtime, or application implementation in this Sprint.
