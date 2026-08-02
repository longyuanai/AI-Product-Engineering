# Sprint 01.1 — Research Plan Review Fix

- Status: Completed
- Version: v0.1
- Owner: APES Maintainers
- Last Updated: 2026-08-03

## Table of Contents

- [Sprint Goal](#sprint-goal)
- [Scope](#scope)
- [Out of Scope](#out-of-scope)
- [Tasks](#tasks)
- [Acceptance Criteria](#acceptance-criteria)
- [Verification](#verification)
- [Notes](#notes)
- [Final Status](#final-status)

## Sprint Goal

Refine the Sprint 1 ecosystem research plan so it is submittable, executable, and reviewable — without starting any actual research. Resolve the issues identified in the methodology review of `research/research-plan.md` and tighten the language so future sprints can act on the plan without ambiguity.

## Scope

In scope:

- Diagnose the encoding-anomaly reports in encoding markers seen in the research plan and accompanying files; confirm whether the underlying files are intact.
- Add to `research/research-plan.md`:
  - Source Register Schema (15 fields).
  - Reliability Classification (A–E).
  - Candidate Selection Criteria (inclusion + exclusion).
  - Search Log Schema (9 fields).
  - Core Project Analysis Schema (28 fields).
  - Six Research Checkpoints and a Final Research Gate (GO / PIVOT / STOP / RESEARCH AGAIN).
  - Kill Criteria (≥9 specific stop conditions).
  - Research Priority Order (P0–P3).
- Distinguish between A–E source reliability and Strong / Moderate / Weak note quality.
- Correct Git-status language in `tasks/sprint-01-ecosystem-research-plan.md`: clarify that "Completed" refers to the planning task only, and that working tree is intentionally not clean after Sprint 1.
- Replace "no git operation of any kind" with the accurate scope: no **mutating** Git operation, while read-only ops remain permitted.
- Rewrite copyright and paywall rules to forbid public mirrors, require metadata + short quotes + page numbers, and prefer legal open versions.
- Add a minimal `Sprint 1.1` entry to `CHANGELOG.md`.
- Update `research/README.md` so it correctly references the refined plan and ends with a trailing newline.
- Add this task file under `tasks/`.

## Out of Scope

The following are explicitly forbidden in this sprint and were not attempted:

- Beginning any formal ecosystem research.
- Accessing or registering 20 candidate projects.
- Starting Phase A of the research plan.
- Writing any Gap Analysis conclusions.
- Stating that APES is worth continuing.
- Writing any standard module body content.
- Creating new research directories.
- Rewriting the entire research plan (only the targeted additions in Scope are applied).
- Replacing characters based on guesswork to "fix" mojibake that is a terminal display artifact.
- Auto-committing or pushing.
- Modifying project positioning.
- Any mutating Git operation.

## Tasks

- [x] Pre-execution checks: confirm working directory, read the Sprint 1.1 brief, read the current state of `research/research-plan.md`, `tasks/sprint-01-ecosystem-research-plan.md`, `research/README.md`, and `CHANGELOG.md`.
- [x] Encoding diagnosis: confirm UTF-8 / no BOM; verify the reported markers are display artifacts rather than file corruption.
- [x] Update §2 Principle 7 with copyright-aware provenance language.
- [x] Add §4.6 Source Register Schema.
- [x] Add §4.7 Search Log Schema.
- [x] Add §4.8 Core Project Analysis Schema.
- [x] Add §10.4 Research Checkpoints (6 checkpoints including Final Research Gate).
- [x] Replace §10.3 with Kill Criteria (9 specific stop conditions).
- [x] Add §14 Research Priority Order (P0–P3).
- [x] Add Appendices A–F (Source Register, Reliability Classification, Candidate Selection, Search Log, Core Project Analysis, Final Research Gate).
- [x] Update Table of Contents to reflect §14 and Appendix A–F.
- [x] Distinguish A–E source reliability from Strong / Moderate / Weak note quality in §7.
- [x] Replace `tasks/sprint-01-ecosystem-research-plan.md` Git-status language with "no mutating Git operation" and document the four read-only operations that remain permitted.
- [x] Add a `Sprint 1.1` entry to `CHANGELOG.md`.
- [x] Ensure `research/README.md` references the refined plan and ends with a trailing newline.
- [x] Create this task file.
- [x] Run final verification: `git status`, `git diff --stat`, `git diff --check`, and the 15-point acceptance check.

## Acceptance Criteria

- `research/research-plan.md` is non-empty and contains the 14 numbered sections plus six Appendices.
- The plan encodes a Source Register Schema with 15 fields, a Search Log Schema with 9 fields, and a Core Project Analysis Schema with 28 fields.
- The plan defines a Reliability Classification (A–E) and explicitly distinguishes it from Strong / Moderate / Weak note quality.
- The plan defines Candidate Selection Criteria with both inclusion and exclusion lists.
- The plan defines six Research Checkpoints, including a Final Research Gate with GO / PIVOT / STOP / RESEARCH AGAIN outputs.
- The plan defines Kill Criteria with at least nine explicit stop conditions.
- The plan defines a Research Priority Order P0–P3 covering adjacent standards, product discovery methods, engineering / governance / security standards, and supplementary material.
- The plan forbids public mirrors of paywalled sources; it requires metadata, short quotes, and page numbers; and where possible it prefers legal open versions.
- `tasks/sprint-01-ecosystem-research-plan.md` Status language clarifies "Completed" applies to the planning task only, not the research itself.
- The same task file replaces "No git operation of any kind" with "No mutating Git operation" and enumerates the allowed read-only operations.
- The same task file documents that the working tree is intentionally not clean after Sprint 1 (two new files plus two additive modifications).
- `CHANGELOG.md` contains a `Sprint 1.1` entry that summarizes the refinement without claiming research results.
- `research/README.md` references the refined plan and ends with a trailing newline.
- No file outside the allowed list (`research/research-plan.md`, `tasks/sprint-01-ecosystem-research-plan.md`, `research/README.md`, `CHANGELOG.md`, `tasks/sprint-01-1-research-plan-review-fix.md`) was modified.
- No git commit, push, tag, or branch creation was performed.

## Verification

- `git status` — confirms the five files listed in Tasks are the only modifications and additions.
- `git diff --stat` — confirms scope of changes (additions and edits, no deletions).
- `git diff --check` — confirms no whitespace errors are introduced.
- Spot-read on the new research-plan sections to confirm UTF-8 / no BOM and that the markers reported as "mojibake" do not appear in the file bytes.
- Acceptance check against the 15-point list above.

Verification details are summarized in the agent's completion report.

## Notes

- The encoding-anomaly markers reported in the brief (`鈫?`, `搂`, `脳`, `鈥?`, `鈹`) were not present in the file bytes; they were terminal display artifacts. No character replacement was performed.
- This sprint remains planning-only. No formal research was begun and no Claim about APES's value gap was produced.
- The Final Research Gate default is **not** GO; PIVOT, STOP, or RESEARCH AGAIN take precedence whenever evidence does not unambiguously support GO.

## Final Status

**Completed** for the items listed in [Tasks](#tasks) above. Items left intentionally open (Phase A–D execution, license, code of conduct, MD lint action choice, and any subsequent sprint planning) are tracked in the agent's "Open Decisions" report.
