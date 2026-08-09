# Foundation 0.1 — Repository Evolution Plan

- Status: Completed
- Sprint: Foundation 0.1
- Owner: APES Maintainers
- Last Updated: 2026-08-03
- Purpose: Establish the long-term repository evolution strategy for APES and for any future research-driven, evidence-anchored standard family. This is **architecture only** — a planning artifact, not a release.

> **Scope.** Foundation 0.1 is a documentation-only architecture sprint. No implementation, no code, no scripts, no prompt writing, no engines, no standards, no templates, no commands, no commit, no push, no tag, no branch, no modification of research conclusions, no new research, no new sources. The output is reusable for every future research repository, not only APES.

## Goal

Produce a single architecture document that:

1. Defines the layered target shape (Foundation → Research OS → Project Layer → Release Layer).
2. Separates shared components (project-agnostic) from project-specific components.
3. Codifies a migration strategy that does not break the v0.1 contract.
4. Codifies a compatibility contract so external readers and downstream consumers are not surprised.
5. Codifies a governance extension (Foundation-RFC) so future shared-layer changes are explicit.
6. Names future projects (AI Security, IoT Security, Binary Security, Research Library) as candidates without committing to them.

Foundation 0.1 is deliberately **not** Sprint 4, **not** Gap Analysis, **not** Phase C, **not** Phase D. It runs **before** research resumes.

## Inputs

- `README.md` — APES landing page; 9-stage lifecycle; 5 core principles.
- `VISION.md` — long-term intent; vendor-neutral positioning.
- `MANIFESTO.md` — 5 principles: Product Before Code, Evidence Over Opinion, Validation Before Implementation, Reuse Before Reinvent, Iteration Over Perfection.
- `ROADMAP.md` — v0.1 Foundation through v1.0 Stable.
- `AGENTS.md` — Rule 11: documentation-first; no CLI, no MCP, no IDE extension, no website at this stage.
- `CONTRIBUTING.md` — contribution process.
- `design/01-repository-architecture.md` — current top-level layout; extension policy.
- `governance/README.md` — ADR / RFC / Decision Note hierarchy.
- `governance/adr/ADR-0001-project-positioning.md` — repository name, standard name, deferred tooling scope.
- `governance/adr/README.md` — ADR format and status rules.
- `standards/README.md` — standard module organization.
- `docs/README.md` — reader-facing documentation.
- `tasks/README.md` — sprint file naming convention.
- `research/research-plan.md` — Phase A–D methodology (referenced but **not modified**).
- `research/source-register.md` — 52 Source IDs (referenced but **not modified**).

Foundation 0.1 does not perform any new research, does not modify any research file, and does not change the Sprint 2 status or the Research Gate.

## Outputs

| # | Deliverable | Status |
|---|---|---|
| 1 | `docs/repository-evolution-plan.md` — architecture plan with 16 sections (Vision, Current Repository State, Problems of Current Structure, Future Repository Layers, Repository Responsibilities, Shared Components, Project-Specific Components, Migration Strategy, Directory Evolution, Future Projects, Version Strategy, Governance Strategy, Compatibility Rules, Risk Assessment, Open Questions, Cross-References) | Completed |
| 2 | `tasks/foundation-0-1-repository-evolution.md` (this file) | Completed |
| 3 | Append Foundation section to `README.md` | Completed |
| 4 | Append Foundation 0.1 entry to `CHANGELOG.md` | Completed |

Foundation 0.1 produces **no other files**.

## Architecture Summary

The plan in `docs/repository-evolution-plan.md` describes four layers with a strict downward dependency direction:

- **Research OS** — generic research operating system (schemas, audit posture, evidence trails). No knowledge of any project.
- **Standard Foundation** — cross-project commitments (manifesto, evidence policy, lifecycle model, governance framework, compatibility contract). No knowledge of any specific lifecycle stage content.
- **Project Layer** — each project's domain content. APES is the first instance. Future projects (AI Security, IoT Security, Binary Security, Research Library) carry their own content but inherit both layers above.
- **Release Layer** — tagged snapshots and public bundles.

Shared components include the Manifesto, Evidence Policy, Lifecycle Model, Governance Framework, Source Register schema, Search Log schema, Verification Log schema, Coverage Map schema, Artifact Map schema, Audit template, Statistics Reporter, and Report Engine. Project-specific components include lifecycle modules, templates, commands, checklists, research content (rows), Coverage Map data, Gap Analysis data, examples, and project-specific ADRs.

Foundation 0.1 introduces the **Foundation-RFC** governance type for proposals that affect the shared layers, and introduces **Foundation Maintainer** and **Family Reviewer** roles for future family members.

The plan also enumerates 10 open questions (OQ-1 through OQ-10) to be resolved in later Foundation sprints.

## Scope

In scope (allowed files):

- Create `docs/repository-evolution-plan.md`.
- Create `tasks/foundation-0-1-repository-evolution.md` (this file).
- Update `README.md` to append a Foundation section.
- Update `CHANGELOG.md` to append a Foundation 0.1 entry.

## Out of Scope

Explicitly forbidden in this sprint and **not** attempted:

- **No Gap Analysis** (Phase C).
- **No Feature Matrix.**
- **No Lifecycle Gap claim.**
- **No Market Positioning.**
- **No Competitive Positioning.**
- **No SWOT.**
- **No Roadmap.**
- **No Recommendations.**
- **No Vision.**
- **No Priorities.**
- **No Implementation Plan.**
- **No APES Design.**
- **No APES Architecture.**
- **No Standard Modules.**
- **No Prompt Library.**
- **No Commands, Templates, or Checklists (new APES ones).**
- **No Plugin Design, CLI, MCP, Website.**
- **No Business Strategy.**
- **No Brand Strategy.**
- **No statement that APES is missing something.**
- **No implementation.** No code. No scripts. No prompt writing. No engines.
- **No standards, templates, commands, or checklists** of any kind.
- **No new research.** No new sources. No WebSearch. No WebFetch.
- **No modification of any research file.**
- **No modification of any research conclusion.**
- **No modification of Sprint 2 status** (remains `In Review`).
- **No modification of Research Gate** (remains `RESEARCH AGAIN`).
- **No modification of any file outside the allowed list** (`docs/repository-evolution-plan.md`, `tasks/foundation-0-1-repository-evolution.md`, `README.md`, `CHANGELOG.md`).
- **No git commit, push, tag, or branch creation.**
- **No directory moves, renames, or content relocations.**

Foundation 0.1 is a planning artifact. The plan describes what future Foundation sprints (Foundation 0.2, 0.3, 0.4, 0.5, 1.0) may do — it does not do them.

## Acceptance Criteria

- `docs/repository-evolution-plan.md` exists and contains all 16 specified sections (Vision, Current Repository State, Problems of Current Structure, Future Repository Layers, Repository Responsibilities, Shared Components, Project-Specific Components, Migration Strategy, Directory Evolution, Future Projects, Version Strategy, Governance Strategy, Compatibility Rules, Risk Assessment, Open Questions, Cross-References).
- `tasks/foundation-0-1-repository-evolution.md` exists and contains Goal, Inputs, Outputs, Architecture Summary, Scope, Out of Scope, Acceptance Criteria, Verification, Remaining Limitations, Status, Cross-References.
- `README.md` has an additive Foundation section appended; existing content is preserved verbatim.
- `CHANGELOG.md` has a Foundation 0.1 entry in the `[Unreleased]` section; existing entries are preserved verbatim.
- No Gap Analysis, Feature Matrix, Lifecycle Gap claim, Market Positioning, Competitive Positioning, SWOT, Roadmap, Recommendations, Vision, Priorities, Implementation Plan, APES Design, APES Architecture, Standard Modules, Prompt Library, new APES Commands/Templates/Checklists, Plugin Design, CLI, MCP, Website, Business Strategy, Brand Strategy, or statement that APES is missing something appears in any Foundation 0.1 deliverable.
- No implementation, code, scripts, prompts, engines, standards, templates, or commands appear in any Foundation 0.1 deliverable.
- No research file is modified. No research conclusion is modified. Sprint 2 status remains `In Review`; Research Gate remains `RESEARCH AGAIN`.
- No new WebSearch or WebFetch was performed.
- No file outside the allowed list was modified.
- No git commit, push, tag, or branch creation was performed.

## Verification

- File-existence check for the four deliverables above.
- Section-coverage check: `docs/repository-evolution-plan.md` contains all 16 sections named in the Acceptance Criteria.
- Allowed-files check: only `docs/repository-evolution-plan.md`, `tasks/foundation-0-1-repository-evolution.md`, `README.md`, and `CHANGELOG.md` were modified.
- Sprint 2 status preserved at `In Review`; Research Gate preserved at `RESEARCH AGAIN`.
- No git operations performed (no commit, push, tag, or branch).
- Working tree left in uncommitted but reviewable state.

## Remaining Limitations

- Foundation 0.1 is **architecture only**. Future Foundation sprints (0.2, 0.3, 0.4, 0.5, 1.0) will progressively move directories and promote root documents to the Standard Foundation. None of those moves are authorized by Foundation 0.1.
- Foundation 0.1 introduces the Foundation-RFC governance type and the Foundation Maintainer / Family Reviewer roles in writing only. These are not yet operationalized; a future Foundation sprint will define the exact submission and review procedure.
- The plan names AI Security, IoT Security, Binary Security, and Research Library as future-project candidates. No commitment is made to any of them. Each future project, if it starts, must write its own ADR-0001-equivalent.
- The plan does not yet decide whether the Foundation is a separate repository, a branch, a tag, or a subdirectory (Open Question OQ-10). The default position is a separate repository, future.
- The plan does not change the Research Gate. Sprint 2 remains `In Review`; Research Gate remains `RESEARCH AGAIN`. Foundation 0.1 explicitly does not enter Phase B, Phase C, or Phase D.
- The plan does not implement any tooling. ADR-0001 deferred CLI / MCP / IDE extension / website; Foundation 0.1 reaffirms that deferral.

## Status

**Completed** for the items listed in [Outputs](#outputs) above. Foundation 0.1 produced one architecture document (`docs/repository-evolution-plan.md`), this task file, and additive updates to `README.md` and `CHANGELOG.md`. Sprint 2 remains `In Review`; Research Gate remains `RESEARCH AGAIN`. Future Foundation sprints will be tracked in their own task files.

## Cross-References

- `docs/repository-evolution-plan.md` — architecture plan.
- `README.md` — APES landing page; new Foundation section appended.
- `CHANGELOG.md` — Foundation 0.1 entry appended in `[Unreleased]`.
- `design/01-repository-architecture.md` — v0.1 architectural decision extended by Foundation 0.1.
- `governance/README.md` — governance framework extended by Foundation 0.1 (Foundation-RFC type).
- `governance/adr/ADR-0001-project-positioning.md` — project positioning; reaffirmed by Foundation 0.1 (deferred tooling scope).
- `MANIFESTO.md` — candidate for Standard Foundation promotion in Foundation 0.2.
- `AGENTS.md` — candidate for Standard Foundation promotion in Foundation 0.2.
- `CONTRIBUTING.md` — candidate for Standard Foundation promotion in Foundation 0.2.
- `research/research-plan.md` — referenced but not modified; methodology preserved.
- `research/source-register.md` — referenced but not modified; 52 Source IDs preserved.
- `CHANGELOG.md` — Sprint 0 through Sprint 3.1 entries preserved; Foundation 0.1 entry appended.
