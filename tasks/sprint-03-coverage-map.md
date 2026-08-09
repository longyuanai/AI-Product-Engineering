# Sprint 03 — Coverage Map (Phase B)

- Status: Completed
- Sprint: 3
- Owner: APES Maintainers
- Last Updated: 2026-08-03
- Purpose: Run **Phase B (Coverage Map)** of `research/research-plan.md` §4.1 for the 10 Selected projects in `research/competitors/candidate-projects.md`. Describe observed lifecycle responsibility, primary purpose, artifact types, engineering scope, standards involved, governance role, and security role. Do **NOT** enter Phase C (Gap Analysis), Phase D (Positioning Evidence), or APES standard writing. Do **NOT** modify any file outside the allowed list.

## Goal

Produce a reviewable, evidence-anchored **Coverage Map** of the 10 Selected projects in three deliverables:

1. `research/coverage/coverage-map.md` — narrative coverage for each project (lifecycle responsibility, primary purpose, artifact types, engineering scope, standards involved, governance role, security role).
2. `research/coverage/lifecycle-coverage-matrix.md` — matrix of 10 projects × 19 Sprint 3 lifecycle stages, with cell values Primary/Secondary/Partial/None/Unknown and per-cell Source ID + Evidence Type + Confidence.
3. `research/coverage/artifact-relationship-map.md` — map of 15 artifact types to projects that produce / consume them, with Purpose, Inputs, Outputs, Dependencies, Lifecycle position, Ownership, Evidence.

Coverage Mapping is **NOT** Feature Comparison. A project covering the same lifecycle stage does **NOT** imply feature parity.

## Inputs

- `research/competitors/candidate-projects.md` — short list of 10 Selected projects (S-01 through S-10).
- `research/competitors/reverse-research.md` — 14-section narrative for each Selected project.
- `research/source-register.md` — 52 Source IDs (SRC-001 through SRC-052); Verified=6, Partially Verified=32, Unverified=14.
- `research/notes/verification-log.md` — Sprint 2.2 Inaccessible attempts + Sprint 2.3 External Verification Reconciliation entries (EV-001 through EV-006).
- `research/research-plan.md` — Phase B definition.
- `README.md`, `AGENTS.md`, `CHANGELOG.md` — repository context.
- Tasks: `sprint-01-ecosystem-research-plan.md`, `sprint-01-1-research-plan-review-fix.md`, `sprint-02-ecosystem-inventory.md`, `sprint-02-1-evidence-correction.md`, `sprint-02-2-primary-source-verification.md`, `sprint-02-3-external-verification-reconciliation.md`.

## Lifecycle Stages Used (19)

Idea, Discovery, Research, Requirements, Specification, Architecture, Planning, Implementation, Coding, Testing, Review, Documentation, Release, Operation, Maintenance, Knowledge Management, Governance, Security, Continuous Improvement.

Note: this is the **Sprint 3 lifecycle stage set**, broader than the APES 9-stage lifecycle in `README.md`. Coverage is described independently of APES's own taxonomy.

## Cell-Value Scale (Lifecycle Matrix)

- **Primary** — the project's process model explicitly places this stage at the center of its responsibility.
- **Secondary** — the project's process model explicitly touches this stage but treats it as a hand-off or supporting activity.
- **Partial** — the project touches this stage in some artifacts or examples but does not prescribe it.
- **None** — the project's `Scope (In / Out)` section in `research/competitors/reverse-research.md` §4 **explicitly excludes** this stage. None is reserved for cells with explicit §4 Out exclusion.
- **Unknown** — the project's reverse-research record did not address this stage. Unknown is the default for blank cells.

## Artifact Types Covered (15)

AGENTS.md, CLAUDE.md, SPEC, RFC, ADR, Task, Checklist, Template, Prompt, Policy, Workflow, Architecture Decision, Knowledge Base, Standard, Command.

## Deliverables

| # | Deliverable | Status |
|---|---|---|
| 1 | `research/coverage/coverage-map.md` — narrative coverage for S-01 through S-10 | Completed |
| 2 | `research/coverage/lifecycle-coverage-matrix.md` — 10×18 matrix with Source ID + Evidence Type + Confidence per non-empty cell | Completed |
| 3 | `research/coverage/artifact-relationship-map.md` — 15 artifact types mapped to producing / consuming Selected projects | Completed |
| 4 | `tasks/sprint-03-coverage-map.md` (this file) | Completed |
| 5 | Update `research/README.md` to add Sprint 3 deliverables pointer | Completed |
| 6 | Update `CHANGELOG.md` Unreleased section with Sprint 3 entry | Completed |

## Coverage Rules (Applied Throughout)

1. **Coverage Mapping is NOT Feature Comparison.** A project covering the same lifecycle stage does **NOT** imply feature parity.
2. **Never compare implementations.** Never compare product quality. Only describe observed lifecycle responsibility.
3. **If evidence does not exist: Unknown.** Never infer lifecycle coverage.
4. **If evidence conflicts: record BOTH.** Do **NOT** resolve conflicts. Do **NOT** decide which side is correct.
5. **Source IDs only.** Every claim references `SRC-NNN` from `research/source-register.md`.
6. **No APES evaluation.** No statement that APES is missing something, that any project is better or worse, or that APES should adopt or reject anything.

## Classification Rules (Applied Throughout)

- **Primary** is reserved for stages that a project explicitly centers in its process model (named, described, prescribed).
- **Secondary** is reserved for stages that a project explicitly touches but treats as a hand-off.
- **Partial** is reserved for stages that appear in some artifacts or stated examples but are not prescribed.
- **None** is the default when no evidence is located; this is **not** an APES evaluation.
- **Unknown** is used only when the evidence trail is genuinely indeterminate.

## Scope

In scope (allowed files):

- Create `research/coverage/` directory.
- Create `research/coverage/coverage-map.md`, `research/coverage/lifecycle-coverage-matrix.md`, `research/coverage/artifact-relationship-map.md`.
- Create `tasks/sprint-03-coverage-map.md` (this file).
- Update `research/README.md` to add Sprint 3 deliverables pointer.
- Update `CHANGELOG.md` Unreleased section with Sprint 3 entry.

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
- **No new WebSearch or WebFetch** (uses Sprint 2.3 evidence only).
- **No modification of any file outside the allowed list** (`research/coverage/*`, `tasks/sprint-03-coverage-map.md`, `research/README.md`, `CHANGELOG.md`).
- **No auto-commit, push, tag, or branch creation.**

## Acceptance Criteria

- `research/coverage/coverage-map.md` exists and contains narrative coverage for all 10 Selected projects (S-01 through S-10).
- `research/coverage/lifecycle-coverage-matrix.md` exists and contains a 10×18 matrix; every non-empty cell carries a Source ID + Evidence Type + Confidence triple.
- `research/coverage/artifact-relationship-map.md` exists and covers all 15 artifact types named in the Sprint 3 brief.
- No Gap Analysis, Feature Matrix, Lifecycle Gap claim, Market Positioning, Competitive Positioning, SWOT, Roadmap, Recommendations, Vision, Priorities, Implementation Plan, APES Design, APES Architecture, Standard Modules, Prompt Library, new APES Commands/Templates/Checklists, Plugin Design, CLI, MCP, Website, Business Strategy, Brand Strategy, or statement that APES is missing something appears in any Sprint 3 deliverable.
- Sprint 2 status remains `In Review`; Research Gate remains `RESEARCH AGAIN`. No change to either unless evidence requires it (it does not).
- No new WebSearch or WebFetch was performed.
- No file outside the allowed list was modified.
- No git commit, push, tag, or branch creation was performed.
- `tasks/sprint-03-coverage-map.md` exists with Goal, Inputs, Lifecycle Stages, Deliverables, Coverage Rules, Classification Rules, Acceptance Criteria, Verification, Remaining Limitations, Status.

## Verification

- File-existence check for all three Coverage Map deliverables + this task file.
- Matrix structural check: 10 rows × 18 columns; every non-empty cell carries a parenthetical `(SRC-NNN | Evidence Type | Confidence)`.
- Artifact Map structural check: all 15 artifact types present; each carries Purpose / Inputs / Outputs / Dependencies / Lifecycle position / Ownership / Evidence.
- Sprint 2 status preserved at `In Review`; Research Gate preserved at `RESEARCH AGAIN`.
- No file outside the allowed list was modified.
- Working tree left in uncommitted but reviewable state (no auto commit / push).

## Remaining Limitations

- Page Unverified sources (e.g., S-01 Product Talk, S-02 SVPG, S-03 basecamp.com/shapeup, S-04 / S-05 HBS / Strategyn, S-07 / S-08 repos) remain so because the access window of 2026-08-03 blocks direct WebFetch on the canonical primary pages. Multi-source corroboration of publication and scope is recorded; primary page content is not directly read in this sprint.
- For SRC-044 and SRC-045, only abstract/metadata is `Verified`; method details beyond abstract remain `Partially Verified`. The conflicting empirical evidence on AGENTS.md (S-10) is preserved verbatim; APES does not adjudicate.
- For SRC-006 (ISO/IEC/IEEE 12207:2026), only metadata is `Verified`; full text is paywalled and not in scope of this sprint.
- The 18-stage lifecycle set used in this sprint is broader than the APES 9-stage lifecycle in `README.md`. Coverage is described independently of APES's own taxonomy; this is **not** an APES critique.
- "None" cells in the lifecycle matrix are observations about the evidence trail, not APES gap claims.
- "Not observed in Selected projects" entries in the artifact map are observations about the Selected 10's reverse-research evidence, not assertions about the broader landscape.
- Per the brief: "Stop after the report. Do not continue into Gap Analysis. Do not continue into APES design. Wait for the next sprint."

## Status

**Completed** for the items listed in [Deliverables](#deliverables) above. Sprint 3 produced three Coverage Map files, this task file, and additive updates to `research/README.md` and `CHANGELOG.md`. No Gap Analysis, no Positioning Evidence, no APES standard writing. Sprint 2 remains `In Review`; Research Gate remains `RESEARCH AGAIN`.

## Cross-References

- `research/coverage/coverage-map.md` — narrative coverage.
- `research/coverage/lifecycle-coverage-matrix.md` — matrix view.
- `research/coverage/artifact-relationship-map.md` — artifact-type map.
- `research/research-plan.md` — Phase B definition (§4.1).
- `research/competitors/reverse-research.md` — 14-section source data.
- `research/source-register.md` — Source IDs (SRC-001 to SRC-052).
- `research/notes/verification-log.md` — verification log + EV reconciliation.
- `research/README.md` — Sprint 3 deliverables pointer.
- `CHANGELOG.md` — Sprint 3 Unreleased entry.
