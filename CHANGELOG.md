# Changelog

- Status: Active
- Version: v0.1
- Owner: APES Maintainers
- Last Updated: 2026-08-10
- Purpose: Track notable changes to APES using the Keep a Changelog format.

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/).

## [Unreleased]

### Added — Implementation F2: Read-Only Validator (2026-08-09)

- Created the independent sibling Git repository `APES-Validator` and implemented the `apes-validator` Python 3.12+ package with `check`, `graph`, `explain`, and `--version` commands.
- Added deterministic text/JSON diagnostics and text/JSON/DOT graph output for JSON Schema metadata, F1 fixture expectations, unique IDs, references, dependency direction, cycles, local links, anchors, root containment, and symbolic-path boundaries.
- Added an initial 34 unit, property, CLI, security, determinism, and read-only tests. The initial implementation run passed 34/34 with 94.40% branch coverage; Ruff and strict mypy also passed.
- Locked 43 packages with uv and verified Hatchling sdist/wheel builds. Dependency audit initially found `PYSEC-2026-1845` in pytest 8.4.2; pytest was upgraded to 9.1.1 and the repeated audit reported no known vulnerabilities.
- Ran the validator against the real APES repository: all eight F1 fixtures validated, deterministic JSON output succeeded, and the before/after SHA-256 inventory was unchanged.
- Saved the independent implementation as clean root commit `b085162` (`feat: implement F2 read-only validator`); no remote or push was created.
- Continued F2 security review in commit `35d4ccf`: rejected external Schema `$ref` resolution, bounded Markdown/front matter/schema/fixture sizes, enforced symbolic fixture/schema containment, replaced recursive cycle traversal, and added adversarial YAML and 2000-node graph tests.
- Expanded the pre-audit suite to 40/40 tests at 93.98% branch coverage. Ruff, strict mypy, Bandit, dependency audit, lock verification, build, and real APES hash-preservation checks passed.
- Added [`checklists/f2-independent-review.md`](checklists/f2-independent-review.md) and [`governance/decisions/2026-08-09-f2-review-evidence.md`](governance/decisions/2026-08-09-f2-review-evidence.md) with commit/schema/lock/wheel hashes, reproduction commands, adversarial evidence, residual limits, and reviewer decision fields.
- The independent Claude Opus 5 audit reproduced the automated evidence and no-write guarantee but selected `Request changes`, recording one P0, four blocking P1, three P2, and five P3 findings.
- Added a closed no-retrieval Schema Registry, restricted APES Schema profile, recursion-safe input and diagnostic boundaries, exit code 3 / `APES900`, YAML date normalization, inline-code masking, Windows drive/device rejection, bounded diagnostic output, and total filename ordering in remediation commit `73bbe6e`.
- Upgraded the artifact contract to `urn:apes:schema:artifact-metadata:0.2.0`, binding all thirteen artifact types to canonical ID prefixes while retaining four valid and four intentionally invalid compatibility fixtures.
- Expanded the remediation suite to 71/71 tests at 91.74% branch coverage. Ruff, strict mypy, Bandit over 1300 lines, dependency audit, 43-package lock verification, sdist/wheel build, 88-file Markdown validation, and the 103-file APES hash-preservation check passed.
- Added [`governance/decisions/2026-08-09-f2-remediation-evidence.md`](governance/decisions/2026-08-09-f2-remediation-evidence.md) with exact commit/schema/lock/package hashes, all thirteen finding dispositions, revised residual limits, and a blank re-review outcome.
- Added implementer self-review hardening in commit `9d58a9f`: reviewed Schema-pattern and combinator restrictions; explicit Schema/instance depth, node, width, and branch limits; YAML alias rejection; a 64 KiB Markdown line cap; and pre-resolution rejection of absolute, UNC, malformed, control-character, and lexically escaping paths.
- Expanded the follow-up suite to 87/87 tests at 91.20% branch coverage after an initial 89.46% coverage run failed the unchanged 90% gate. Ruff, strict mypy, Bandit over 1578 lines, dependency audit, 43-package lock verification, build, and a byte-equivalent 103-file APES no-write check passed.
- Removed the agent-created `.f2-self-review-staging` directory after explicit maintainer approval, then reproduced `check`, `graph`, and `explain` against the real APES root with 88 Markdown files, 8 fixtures, no diagnostic, and all 103 non-Git file hashes unchanged.
- Reconciled stale current-state text in the evolution plan, architecture limitations, F1 task, and handoff: three ADRs are accepted, F2 is implemented in the sibling repository, and only F3 and later implementation phases remain unstarted.
- Added accepted [`ADR-0003`](governance/adr/ADR-0003-f2-read-only-validator-runtime.md) and [`tasks/implementation-f2-read-only-validator.md`](tasks/implementation-f2-read-only-validator.md); advanced the Repository Evolution Plan to v0.4.0 and synchronized architecture, governance, task, README, and handoff records.
- F2 remains `In Review` pending independent re-review of latest commit `9d58a9f`; the original thirteen-finding remediation is preserved in predecessor `73bbe6e`. F3, write commands, workflow evaluation, adapters, publication, and deployment remain unstarted.

### Added — Foundation 0.3: F1 Contract Prototype (2026-08-07)

- Accepted ADR-0002 after explicit maintainer approval of the implementation Sprint and recorded the five architecture-gate decisions in the ADR acceptance record.
- Added `schemas/artifact-metadata.schema.json`, a JSON Schema 2020-12 contract for parsed YAML front matter metadata covering IDs, artifact types, lifecycle status, Semantic Versioning, owners, relationships, evidence, and update dates.
- Added four representative valid fixtures and four intentionally invalid fixtures plus `schemas/compatibility-mapping.md`; the compatibility cases cover an ADR, Source Register source, Foundation task, and coverage audit.
- Executed the contract with an ephemeral `jsonschema` environment: all four valid fixtures passed and all four invalid fixtures were rejected for the intended constraint. No production dependency or package manifest was added.
- Added `tasks/foundation-0-3-contract-prototype.md`, updated current indexes and project handoff memory, and advanced the Repository Evolution Plan to v0.3.2.
- Updated `design/01-repository-architecture.md` to v0.2 so the accepted top-level `schemas/` contract registry and its non-runtime boundary are part of the repository layout contract.
- Reconciled the old Foundation 0.3 `research-os/` migration sketch as historical and unexecuted; the actual Foundation 0.3 scope is F1 Contract Prototype, while Research OS directory migration remains unassigned.
- Existing Markdown remains canonical and unmoved. F2 CLI, graph, workflow, adapters, website, MCP, application source, and build pipeline remain unstarted.
- Sprint 2 remains `In Review`; the Research Gate remains `RESEARCH AGAIN`; Sprint 4 remains unstarted.

### Changed — Project Reconciliation (2026-08-07)

- Reconciled APES project chats from 2026-08-03 through 2026-08-05 against the current working tree, task files, ADRs, research records, and prior CHANGELOG entries.
- Added `sessions/2026-08-07-project-handoff.md` and activated the sessions index as project-scoped handoff memory; generated Codex memory files were left machine-managed.
- Synchronized the root README and docs, research, governance, and task indexes with completed Foundation 0.2 while preserving ADR-0002 as `Proposed`.
- Corrected the repository count to 15 visible top-level directories plus `.github/` and documented that the original Foundation 0.2 migration label is historical planning context, not an active Sprint.
- Updated Source Register metadata to v0.6 for the existing 54-source Foundation 0.2 state without changing source rows or verification outcomes.
- Normalized the missing final LF newline in 40 pre-existing Markdown files so repository content now follows `.editorconfig` and `.gitattributes`.
- Added `tasks/maintenance-2026-08-07-project-reconciliation.md`. Sprint 4 and F1 remain unstarted; Sprint 2 remains `In Review`; Research Gate remains `RESEARCH AGAIN`.
- No external research, implementation artifact, dependency, commit, push, tag, release, file move, or deletion was performed.

### Added — Foundation 0.2: Open-Source Reference Architecture (2026-08-05)

- Compared four canonical GitHub projects as implementation references: GitHub Spec Kit (`SRC-025`), OpenSpec (`SRC-026`), BMAD-METHOD (`SRC-053`), and Agent OS (`SRC-054`). The comparison covers functions, architecture, technology stack, APES-oriented strengths, and APES-oriented limitations while separating observed facts from inference.
- Added `research/competitors/open-source-reference-comparison.md` and recorded the 2026-08-05 evidence pass in `research/notes/search-log.md` (`SE-032` through `SE-036`). The GitHub CLI attempt returned no result because the configured token was invalid and sandboxed API access was blocked; no credential was changed. Canonical public GitHub repository pages and raw files were used instead.
- Refreshed `SRC-025` and `SRC-026` from direct primary access and upgraded both to `Verified`; added directly inspected Level A sources `SRC-053` and `SRC-054`. Current row-level totals are 54 sources: Reliability A=25, B=18, C=9, D=2, E=0; Claim Verification Verified=10, Partially Verified=32, Unverified=12, Contradicted=0, Inaccessible=0.
- Updated `docs/repository-evolution-plan.md` to v0.3 with sections 24–28: open-source comparison, schema-first / file-native target architecture, recommended canonical and future validator stacks, staged implementation plan, and security / rollback / decision guardrails.
- Added `governance/adr/ADR-0002-schema-first-reference-architecture.md` with status `Proposed`. The proposal keeps Markdown + small YAML front matter canonical, uses JSON Schema before engines, derives the artifact graph, makes workflows declarative, keeps validation deterministic and read-only first, and treats agent integrations as generated projections.
- Added `tasks/foundation-0-2-open-source-reference-architecture.md` and updated the competitor, ADR, and task indexes.
- Foundation 0.2 is documentation and research only. It creates no CLI, MCP server, IDE extension, website, build pipeline, schema file, engine, workflow file, adapter, runtime dependency, application source, file move, release, commit, or push.
- Sprint 2 remains `In Review`; Research Gate remains `RESEARCH AGAIN`. ADR-0001 remains Accepted; ADR-0002 requires maintainer review before any implementation sprint.

### Changed — Repository Hygiene (2026-08-04)

- Reconciled root and directory indexes with the completed Sprint 3 / Sprint 3.1 and Foundation 0.1 / Foundation 0.1.1 artifacts.
- Updated stale Placeholder status text in `docs/`, `research/`, `tasks/`, `design/`, and `governance/` indexes without changing any research evidence, Sprint status, or Research Gate.
- Added missing root README Table of Contents entries and indexed the Repository Evolution Plan, Coverage Map, research logs, task files, and ADR-0001.
- Fixed three incorrect relative paths in standard-module placeholders and removed one pseudo-link from the Sprint 3.1 audit task.
- Added `.claude/settings.local.json` to `.gitignore` so local Claude permissions remain local.
- Added `.editorconfig` and `.gitattributes` to standardize UTF-8 text, LF line endings, and final-newline behavior across editors and Git checkouts.
- Added `tasks/maintenance-2026-08-04-repository-hygiene.md` as the maintenance record.
- Sprint 2 remains `In Review`; Research Gate remains `RESEARCH AGAIN`. License selection, further source verification, Foundation-RFC operationalization, and version-namespace decisions remain open.
- No commit, push, tag, or branch operation was performed.

### Added — Foundation 0.1.1: Repository Evolution Plan Upgrade (2026-08-03)

- Architecture refinement sprint that strengthens the Repository Evolution Plan into the definitive architectural document for Research OS. **This is NOT a rewrite.** **This is NOT Foundation 0.2.** **No redesign of the repository.** **No change to previous research.** **No implementation.** **No constitution.** **No prompt engine.** **No workflow.**
- Refined `docs/repository-evolution-plan.md` with seven new architectural sections appended after section 16 (sections 17 through 23). Sections 1 through 16 are preserved verbatim. One refinement note was appended to section 4 to clarify the relationship between the 4-layer deployment view and the 6-layer architectural view. The plan is now at v0.2.
- Section 17 — **Repository Evolution Principles**: ten principles codified as the philosophical foundation of Research OS. (1) Backward Compatibility First. (2) Research before Design. (3) Evidence before Opinion. (4) Audit before Release. (5) Architecture before Implementation. (6) Shared before Project-specific. (7) Everything Versioned. (8) Everything Traceable. (9) Everything Reproducible. (10) No Hidden Decisions.
- Section 18 — **Repository Layer Model (6 layers)**: Meta → Foundation → Engine → Research → Project → Release. Strict downward dependency. The 4-layer deployment view (Research OS → Standard Foundation → Project Layer → Release Layer) is preserved and explicitly identified as a deployment view; the 6-layer view is the architectural reference for future Foundation sprints.
- Section 19 — **Repository Lifecycle (9 stages)**: Idea → Research → Audit → Architecture → Implementation → Validation → Release → Maintenance → Archive. Foundation 0.1 / 0.1.1 sit at the Architecture stage. Transition rules: forward only; reverse transitions require a Decision Hierarchy artifact; archive is irreversible.
- Section 20 — **Decision Hierarchy (10 tiers)**: Principles → Constitution → RFC → Standard → Schema → Engine → Workflow → Prompt → Project → Sprint. Lower tiers cannot override higher tiers. Within a tier, `Accepted` > `Proposed` > `Draft`. Cross-tier conflicts are resolved via RFC. The Constitution tier is reserved as a slot (not yet written).
- Section 21 — **Document Taxonomy (15 types)**: Policy, Constitution, RFC, ADR, Research, Coverage, Gap Analysis, Evidence, Statistics, Report, Task, Prompt, Checklist, Template, Release Notes. Each type carries Purpose, Owner, Lifecycle, and Version policy.
- Section 22 — **Repository Maturity Model (6 levels)**: Level 0 Bootstrap → Level 1 Research → Level 2 Standardization → Level 3 Automation → Level 4 Platform → Level 5 Research OS. Current state: Level 1 (post Sprint 3.1). Current target: Level 2 (post Foundation 0.1.1).
- Section 23 — **Repository Dependency Graph**: Principles → Constitution → Schemas → Engines → Workflows → Prompts → Research → Coverage → Gap → Release. The dependency graph and the Decision Hierarchy are dual views of the same constraint set.
- Created `tasks/foundation-0-1-1-repository-evolution-upgrade.md` — sprint task file with Goal, Inputs, Architecture Refinements, Out of Scope, Acceptance Criteria, Verification, Remaining Questions, Status, Cross References.
- Appended a Foundation 0.1.1 section to `README.md` summarizing the seven refinements. The existing Foundation 0.1 section and all prior content are preserved verbatim.
- Explicitly **not** in this sprint: Gap Analysis (Phase C), Feature Matrix, Lifecycle Gap claim, Market Positioning, Competitive Positioning, SWOT, Roadmap, Recommendations, Vision, Priorities, Implementation Plan, APES Design, APES Architecture (separate from the Repository Evolution Plan), Standard Modules, Prompt Library, new APES Commands/Templates/Checklists, Plugin Design, CLI, MCP, Website, Business Strategy, Brand Strategy, statement that APES is missing something, implementation, code, scripts, engines, prompt implementation, constitution, standards, workflow implementation, directory implementation, new research, new sources, WebSearch, WebFetch.
- Explicitly **not** modified in this sprint: any research file, any research conclusion, Sprint 2 status (`In Review`), Research Gate (`RESEARCH AGAIN`), license selection, root identity documents, sections 1 through 16 of `docs/repository-evolution-plan.md` (except the appended refinement note in section 4).
- Foundation 0.1.1 reaffirms the deferred tooling scope from ADR-0001 (no CLI, no MCP server, no IDE extension, no website) and from `AGENTS.md` Rule 11 (documentation-first).
- Foundation 0.2 is a separate, future sprint. Foundation 0.1.1 explicitly does **not** begin it.
- No new WebSearch or WebFetch was performed.
- No file outside the allowed list (`docs/repository-evolution-plan.md`, `tasks/foundation-0-1-1-repository-evolution-upgrade.md`, `README.md`, `CHANGELOG.md`) was modified.
- No git commit, push, tag, or branch creation was performed.
- This CHANGELOG entry.

### Added — Foundation 0.1: Repository Evolution Plan (2026-08-03)

- Architecture-only sprint to establish the long-term repository evolution strategy for APES and for any future research-driven, evidence-anchored standard family. **This is NOT Sprint 4 and does NOT start Gap Analysis.**
- Created `docs/repository-evolution-plan.md` — architecture plan with 16 sections: Vision, Current Repository State, Problems of Current Structure, Future Repository Layers (Research OS → Standard Foundation → Project Layer → Release Layer), Repository Responsibilities, Shared Components (Manifesto, Evidence Policy, Lifecycle Model, Source Register schema, Coverage Map schema, Audit template, Statistics Reporter, Report Engine), Project-Specific Components, Migration Strategy, Directory Evolution, Future Projects (AI Security, IoT Security, Binary Security, Research Library as candidates — no commitment), Version Strategy, Governance Strategy (introduces Foundation-RFC type, Foundation Maintainer and Family Reviewer roles), Compatibility Rules, Risk Assessment, Open Questions (10 OQ items), Cross-References.
- Created `tasks/foundation-0-1-repository-evolution.md` — sprint task file with Goal, Inputs, Outputs, Architecture Summary, Scope, Out of Scope, Acceptance Criteria, Verification, Remaining Limitations, Status, Cross-References.
- Appended a Foundation section to `README.md` describing the layered model and Foundation 0.1's scope (architecture only; no implementation).
- Explicitly **not** in this sprint: Gap Analysis (Phase C), Feature Matrix, Lifecycle Gap claim, Market Positioning, Competitive Positioning, SWOT, Roadmap, Recommendations, Vision, Priorities, Implementation Plan, APES Design, APES Architecture, Standard Modules, Prompt Library, new APES Commands/Templates/Checklists, Plugin Design, CLI, MCP, Website, Business Strategy, Brand Strategy, statement that APES is missing something, implementation, code, scripts, prompts, engines, standards, templates, commands, new research, new sources, WebSearch, WebFetch.
- Explicitly **not** modified in this sprint: any research file, any research conclusion, Sprint 2 status (`In Review`), Research Gate (`RESEARCH AGAIN`), license selection, root identity documents.
- Foundation 0.1 reaffirms the deferred tooling scope from ADR-0001 (no CLI, no MCP server, no IDE extension, no website) and from `AGENTS.md` Rule 11 (documentation-first).
- Foundation 0.1 introduces the **Foundation-RFC** governance type as a written proposal only; it is not yet operationalized. Future Foundation sprints will define the exact submission and review procedure.
- The plan documents a strict downward dependency between layers: Research OS depends on nothing; Standard Foundation depends on Research OS; Project Layer depends on both; Release Layer depends on Project Layer.
- The plan documents 10 open questions (OQ-1 through OQ-10) to be resolved in future Foundation sprints (e.g., whether the Foundation is a separate repository, a branch, or a subdirectory).
- Migration is staged: Foundation 0.2 (documentation-only, no directory changes), Foundation 0.3 (introduce named Research OS subdirectory without moving files), Foundation 0.4 (first file moves with redirect paths), Foundation 0.5 (first family member validates the contract end-to-end), Foundation 1.0 (Research OS and Standard Foundation reach v1.0).
- Compatibility contract: directory moves preserve old paths via redirects for one MAJOR version; sprint files are append-only; external links must resolve across versions; the Project Layer may not modify the Standard Foundation or the Research OS without a Foundation-RFC; vendor neutrality is enforced at the layer boundary.
- No new WebSearch or WebFetch was performed.
- No file outside the allowed list (`docs/repository-evolution-plan.md`, `tasks/foundation-0-1-repository-evolution.md`, `README.md`, `CHANGELOG.md`) was modified.
- No git commit, push, tag, or branch creation was performed.
- This CHANGELOG entry.

### Added — Sprint 3.1: Coverage Audit (2026-08-03)

- Audit-only sprint for Sprint 3 (Coverage Map / Phase B). No new research, no new sources, no Gap Analysis, no Feature Matrix, no Lifecycle Gap claim, no Market Positioning, no Competitive Positioning, no SWOT, no Roadmap, no Recommendations, no Vision, no Priorities, no Implementation Plan, no APES Design, no APES Architecture, no Standard Modules, no Prompt Library, no new APES Commands/Templates/Checklists, no Plugin Design, no CLI, no MCP, no Website, no Business Strategy, no Brand Strategy, and no statement that APES is missing something.
- Created `tasks/sprint-03-1-coverage-audit.md` — audit task file with Goal, Inputs, Audit Methodology, eight Audit Tasks Executed, eleven Audit Findings (A through K), Final Aggregate Counts, Source ID Integrity Audit, Coverage Rules, Cell-Value Scale, Confidence Scale, Deliverables, Scope, Out of Scope, Acceptance Criteria, Verification, Remaining Limitations, Status.
- Eight audit tasks executed: (1) Verify Matrix Cell Triples, (2) Audit Unknown vs None (Strict Rule), (3) Audit Artifact Map Fields, (4) Coverage Traceability Review, (5) Confidence Review per Project, (6) Consistency Review, (7) Statistics Review, (8) Cross-Reference Review.
- Eleven audit findings applied to the Sprint 3 files: (A) S-08 Security overclaim `None` → `Unknown`; (B) S-03 Discovery underclaim `None` → `Primary`; (C) S-07 artifact count error 4 → 5; (D) S-06 ADR Confidence overclaim `High` → `Medium`; (E) Stage count discrepancy 18 → 19 across five files; (F) Coverage Footprint footnote error (footnote ² removed; counts 7 → 6 and 6 → 5); (G) Aggregate count `None=144/Unknown=1` too loose → reclassified to `None=15/Unknown=143`; (H) `research/README.md` Table of Contents missing Sprint 2/2.2/2.3/3 entries added; (I) Orphan heading "Sprint 2.3 Deliverables (Preserved)" removed; (J) `tasks/sprint-03-coverage-map.md` stage count 18 → 19; (K) `tasks/sprint-03-coverage-map.md` Cell-Value Scale ambiguity tightened.
- Final aggregate counts (post-audit): Primary=24, Secondary=1, Partial=7, None=15, Unknown=143 (of 190 cells = 10 projects × 19 lifecycle stages). Consistent across `research/coverage/lifecycle-coverage-matrix.md`, `research/coverage/coverage-map.md`, `research/README.md`, and this CHANGELOG entry.
- Source ID Integrity Audit: all 17 Source IDs cited across the three Sprint 3 files exist in `research/source-register.md` within the registered range SRC-001 to SRC-052. No Source ID was added, removed, or renumbered by Sprint 3.1.
- Sprint 2 remains **`In Review`**; Research Gate remains **`RESEARCH AGAIN`**. Sprint 3.1 does not change either.
- The 22 Sprint 2.2 Inaccessible verification attempts and the 6 Sprint 2.3 External Verification Reconciliation entries remain visible and unchanged; Sprint 3.1 builds on the existing evidence trail.
- No new WebSearch or WebFetch was performed.
- No file outside the allowed list (`research/coverage/*`, `tasks/sprint-03-coverage-map.md`, `tasks/sprint-03-1-coverage-audit.md`, `research/README.md`, `CHANGELOG.md`) was modified.
- No git commit, push, tag, or branch creation was performed.
- This CHANGELOG entry.

### Added — Sprint 3: Coverage Map / Phase B (2026-08-03)

- Phase B of `research/research-plan.md` §4.1. Descriptive coverage map only — no Gap Analysis, no Feature Matrix, no Lifecycle Gap claim, no Market Positioning, no Competitive Positioning, no SWOT, no Roadmap, no Recommendations, no Vision, no Priorities, no Implementation Plan, no APES Design, no APES Architecture, no Standard Modules, no Prompt Library, no new APES Commands/Templates/Checklists, no Plugin Design, no CLI, no MCP, no Website, no Business Strategy, no Brand Strategy, and no statement that APES is missing something.
- Created `research/coverage/coverage-map.md` (v0.1) — narrative coverage for each Selected project (S-01 through S-10): lifecycle responsibility, primary purpose, artifact types, engineering scope, standards involved, governance role, security role. Every claim references `SRC-NNN` from `research/source-register.md`.
- Created `research/coverage/lifecycle-coverage-matrix.md` (v0.1) — 10 projects × 19 Sprint 3 lifecycle stages matrix. Cell values: Primary / Secondary / Partial / None / Unknown. Every non-empty cell carries Source ID + Evidence Type + Confidence. Aggregate counts: Primary=24, Secondary=1, Partial=7, None=15, Unknown=143 (of 190 cells).
- Created `research/coverage/artifact-relationship-map.md` (v0.1) — 15 artifact types mapped to Selected projects that produce / consume them: AGENTS.md, CLAUDE.md, SPEC, RFC, ADR, Task, Checklist, Template, Prompt, Policy, Workflow, Architecture Decision, Knowledge Base, Standard, Command. Each artifact type carries Purpose / Inputs / Outputs / Dependencies / Lifecycle position / Ownership / Evidence. Of 15 artifact types, 8 are observed in at least one Selected project (AGENTS.md, SPEC, ADR, Task, Template, Workflow, Architecture Decision, Command) and 7 are not (CLAUDE.md, RFC, Checklist, Prompt, Policy, Knowledge Base, Standard).
- Sprint 3 lifecycle stage set: Idea, Discovery, Research, Requirements, Specification, Architecture, Planning, Implementation, Coding, Testing, Review, Documentation, Release, Operation, Maintenance, Knowledge Management, Governance, Security, Continuous Improvement (19 stages — broader than the APES 9-stage lifecycle in `README.md`; coverage is described independently of APES's own taxonomy).
- Created `tasks/sprint-03-coverage-map.md` — Sprint 3 task file with Goal, Inputs, Lifecycle Stages, Deliverables, Coverage Rules, Classification Rules, Acceptance Criteria, Verification, Remaining Limitations, Status.
- "Coverage Mapping is NOT Feature Comparison." A project covering the same lifecycle stage does **NOT** imply feature parity. Two projects touching the same lifecycle stage may do so with very different artifact types, cadences, or scopes.
- The conflicting empirical evidence between SRC-044 and SRC-045 on AGENTS.md (S-10) is preserved verbatim; APES does **not** adjudicate.
- Sprint 2 remains **`In Review`**; Research Gate remains **`RESEARCH AGAIN`**. Sprint 3 does not change either.
- The 22 Sprint 2.2 Inaccessible verification attempts and the 6 Sprint 2.3 External Verification Reconciliation entries remain visible and unchanged; Sprint 3 builds on the Sprint 2.3 evidence trail.
- No new WebSearch or WebFetch was performed.
- No file outside the allowed list (`research/coverage/*`, `tasks/sprint-03-coverage-map.md`, `research/README.md`, `CHANGELOG.md`) was modified.
- No git commit, push, tag, or branch creation was performed.
- This CHANGELOG entry.

### Added — Sprint 2.3: External Verification Reconciliation (2026-08-03)

- Reconciliation-only sprint. No new research scope, no new sources, no Source ID renumbering, no Coverage Map, Gap Analysis, Positioning Evidence, Feature Matrix, or Lifecycle Coverage Matrix.
- Six sources upgraded from `Partially Verified` to `Verified` in `research/source-register.md` based on external-verification (EV-###) evidence from an external reviewer with direct primary-source access (2026-08-03): SRC-001 (AGENTS.md, EV-001), SRC-003 (NIST SSDF, EV-006), SRC-006 (ISO/IEC/IEEE 12207:2026, EV-005), SRC-015 (OpenAI Codex CLI, EV-002), SRC-044 (arXiv 2602.11988, EV-003), SRC-045 (arXiv 2601.20404, EV-004).
- SRC-045 is **not** retracted; existence, title, authors, dates, and abstract content are confirmed by EV-004. Authors: Jai Lal Lulla, Seyedmoein Mohsenimofidi, Matthias Galster, Jie M. Zhang, Sebastian Baltes, Christoph Treude (v1 2026-01-28; v2 2026-03-30).
- Created `tasks/sprint-02-3-external-verification-reconciliation.md` with full sprint structure (Goal, Inputs, External Evidence Packet, Scope, Out of Scope, Reconciliation Tasks, Statistics Correction, Acceptance Criteria, Verification, Remaining Limitations, Status).
- Added "External Verification Reconciliation (Sprint 2.3, 2026-08-03)" section to `research/notes/verification-log.md` using the 8-field schema (External Verification ID, Source ID, Canonical URL, Verification Date, Verifier Type, Claims Verified, Remaining Limitations, Outcome). All six EV rows have `Outcome: Verified`.
- Corrected Sprint 2.2 statistics: `Verification attempts: 22 / Unique verification IDs: 22 / Unique source IDs attempted: 24 / Repeated source IDs: none`. The Attempt count and Source count are distinct reporting dimensions (some VR rows reference multiple Source IDs, e.g., VR-008 covers SRC-008+012+036) and must not be conflated.
- The 22 Sprint 2.2 Inaccessible verification attempts are **preserved** and remain visible alongside the new External Verification Reconciliation dimension — both reporting dimensions coexist.
- Recomputed `research/source-register.md` Source Audit Statistics (v0.5): Verified=6, Partially Verified=32, Unverified=14, Contradicted=0, Inaccessible=0 (of the 52 Source IDs).
- Cross-file backfill in `research/ecosystem/inventory.md` (v0.3), `research/competitors/candidate-projects.md` (v0.3), `research/competitors/reverse-research.md` (v0.3): per-row EV references; Sprint 2.3 reconciliation notes; updated §S-10 identity, §S-10 §11 conflicting approaches (full author lists for both arXiv papers; updated v1/v2 dates), §S-10 §13 verification notes (Sprint 2.3 outcome; SRC-001/044/045 now `Verified`; SRC-045 not retracted).
- Conflicting empirical evidence between SRC-044 and SRC-045 is preserved verbatim; APES does not adjudicate. The methodological note that "conclusions cannot be generalized to all repositories, models, agents, or tasks; experimental setup must be cited. The 'AGENTS.md is always harmful' generalization is not supported" is added to §S-10 §11.
- Research Gate remains **`RESEARCH AGAIN`**; Sprint 2 remains **`In Review`**. The 10-condition rule was met for the six sources only because the external reviewer had direct primary-source access; APES itself did not perform the verification and the under-15-Verified threshold is unchanged in spirit.
- No git commit, push, tag, or branch creation was performed.
- This CHANGELOG entry.

### Added — Sprint 2.2: Primary Source Verification (2026-08-03)

- Verification-only sprint. No new research scope, no new sources, no Source ID renumbering.
- Created `research/notes/verification-log.md` — 22 verification attempts (VR-001 through VR-022) using the 11-field schema. All 22 attempts ended with `Outcome: Inaccessible` because the access window (2026-08-03) blocks direct WebFetch on `arxiv.org`, `github.com`, `agents.md`, `anthropic.com`, `docs.claude.com`, `iso.org`, `csrc.nist.gov`, `owaspsamm.org`, `owasp.org`, `cognitect.com`, and `producttalk.org`.
- Created `tasks/sprint-02-2-primary-source-verification.md` — sprint task file with Goal, Scope, Out of Scope, Tasks, Acceptance Criteria, Verification Log reference, Source ID Integrity Audit (no renumbering), Research Gate determination (`RESEARCH AGAIN`), Final Status.
- Source ID integrity audit: zero renumbering, zero new Source IDs. The 52 Source IDs (SRC-001 through SRC-052) remain identical to the v0.3 schema produced by Sprint 2.1.
- Statistics recomputed in `research/source-register.md` (v0.4): no upgrades to `Verified`. All 22 P0 sources marked `Inaccessible` in the verification log preserve their existing Claim Verification status (a small number of `Partially Verified` rows remain so because they had been corroborated by community sources during Sprint 2.0; the new `Inaccessible` outcomes are recorded separately and do not downgrade prior corroborations).
- Updated `research/ecosystem/inventory.md` (v0.2), `research/competitors/candidate-projects.md` (v0.2), `research/competitors/reverse-research.md` (v0.2) with Sprint 2.2 verification notes and cross-references. No semantic change to project content; no project was added, removed, or re-ranked.
- Research Gate: **`RESEARCH AGAIN`** — no source was upgraded to `Verified`; the 10-condition rule could not be met for any priority source under the access window. Sprint 2 remains `In Review`.
- Flagged source: **SRC-045 (arXiv 2601.20404)** has no community corroboration and must be existence-checked by an external verifier before the next sprint. If it does not exist at the canonical arXiv ID, SRC-045 must be retracted in a future sprint (not silently retained).
- No Coverage Map, Feature Matrix, Lifecycle Coverage Matrix, Gap Analysis, or APES positioning conclusion was produced. No formal Standard module was written. No git commit, push, tag, or branch creation was performed.
- This CHANGELOG entry.

### Added — Sprint 2.1: Ecosystem Inventory Evidence Correction (2026-08-03)

- Audit and correction of Sprint 2 evidence. No new research was conducted.
- Phase definitions realigned with `research/research-plan.md`: Phase A = Inventory, Phase B = Coverage Map, Phase C = Gap Analysis, Phase D = Positioning Evidence. Sprint 2 Reverse Research is now labeled as **Initial Reverse Research / Phase A supplemental activity** — not Phase B.
- Source Register schema split: Source Reliability (Level A–E), Claim Verification (Verified / Partially Verified / Unverified / Contradicted / Inaccessible), and Claim Type (Official self-description / Observable repository fact / Independent empirical evidence / Practitioner opinion / Community signal / Marketing claim).
- Replaced SRC-044 with the specific arXiv paper 2602.11988 (Gloaguen et al., 2026-02-12).
- Added the conflicting arXiv paper 2601.20404 (2026-01-28) as SRC-045.
- Corrected ISO/IEC/IEEE 12207 entries: SRC-006 (ISO/IEC/IEEE 12207:2026 Edition 2, 2026-04); SRC-052 (ISO/IEC/IEEE 12207:2017 Edition 1, 2017-11, historical).
- Downgraded sources whose license / date / maintenance status were derived only from third-party summaries.
- Sprint 2 status changed to `In Review` pending human review; Sprint 2.1 task file created.
- Statistics recomputed and reported in `research/source-register.md` §"Source Audit Statistics".
- This CHANGELOG entry.

### Added — Sprint 2: Ecosystem Inventory & Reverse Research (2026-08-03)

- Built `research/source-register.md` (50 sources, 15-field schema, A–E reliability; counter-evidence SRC-044 ETH Zurich report recorded).
- Built `research/notes/search-log.md` (31 searches, 9-field schema, no fabricated counts).
- Built `research/ecosystem/inventory.md` (9 categories of adjacent artifacts).
- Built `research/competitors/candidate-projects.md` (long list → short list of 10 Selected projects; defer / decline reasons explicit).
- Built `research/competitors/reverse-research.md` (10 projects analyzed with the 14-section template; AGENTS.md section surfaces counter-evidence).
- Incremental pointer in `research/README.md` listing all Sprint 2 deliverables.
- New sprint task file `tasks/sprint-02-ecosystem-inventory.md`.
- This CHANGELOG entry.

### Added — Sprint 1.1: Research Plan Review Fix (2026-08-03)

- Refined the ecosystem research plan after methodology review.
- Added source register, reliability levels, candidate selection, search logging, and kill criteria.
- Corrected Git-status and copyright-handling language.

### Added — Sprint 1: Ecosystem Research Plan (2026-08-03)

- Draft ecosystem research plan in `research/research-plan.md`. Defines research purpose, principles, scope and non-scope, four-phase methodology (Inventory → Coverage Map → Gap Analysis → Positioning Evidence), source categories and sampling, hypotheses under test, evidence-quality criteria, anti-patterns to prevent, file layout, cadence, stop conditions, review governance, and feedback loop into APES decisions.
- New sprint task file `tasks/sprint-01-ecosystem-research-plan.md`.
- Additive pointer to the research plan added in `research/README.md`.
- This CHANGELOG entry.

### Added — Sprint 0: Repository Foundation (2026-08-03)

- Initial repository structure: `docs/`, `standards/`, `protocols/`, `templates/`, `commands/`, `checklists/`, `research/`, `examples/`, `governance/`, `design/`, `tasks/`, `sessions/`, `assets/`, `scripts/`, `website/`.
- Core documents: `README.md`, `VISION.md`, `MANIFESTO.md`, `ROADMAP.md`, `AGENTS.md`, `CONTRIBUTING.md`, `CODE_OF_CONDUCT.md`.
- Placeholder README files for every stage module under `standards/`.
- GitHub templates: bug report, feature request, standard proposal, pull request template.
- Initial GitHub Actions workflow (Markdown check, draft).
- Initial ADR (`ADR-0001-project-positioning`).
- Initial design document (`design/01-repository-architecture.md`).
- Sprint task file (`tasks/sprint-00-repository-foundation.md`).

### Notes

- The plan is a methodology, not a research finding. No claim about ecosystem, market, competitors, or adoption is made.
- Execution of Phases A–D is deferred to a later, separately-scoped sprint.
- No git operations were performed during this sprint.
- License selection remains pending maintainer decision.
- All standard module contents remain placeholders; no module standard has been written yet.
