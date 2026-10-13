# run-apes-stage

- Status: Active
- Version: v0.2
- Owner: APES Maintainers
- Last Updated: 2026-08-19
- Purpose: Tool-neutral instruction for producing one project-owned APES stage artifact and preparing its manual exit gate.

## Table of Contents

- [Purpose](#purpose)
- [Required Inputs](#required-inputs)
- [Preflight](#preflight)
- [The Canonical Prompt](#the-canonical-prompt)
- [Stage Reference](#stage-reference)
- [Agent Obligations](#agent-obligations)
- [Anti-Patterns](#anti-patterns)
- [Tool Adaptation](#tool-adaptation)
- [Status](#status)

## Purpose

Use this command to delegate exactly one APES lifecycle stage. It connects a canonical template to a project-owned artifact, a canonical exit-gate checklist to a project-owned gate record, and evidence preparation to a named human decision owner. It names no required vendor, model, IDE, or project-memory file.

## Required Inputs

- `STAGE` — one of Idea, Discovery, Research, Validation, Product, Business, Engineering, Growth, or Knowledge.
- `APES_SOURCE_ROOT` — existing directory containing the read-only APES source installation.
- `PROJECT_WORK_ROOT` — existing directory reserved for project-owned artifacts and gate records; it must contain no canonical APES source file.
- `TEMPLATE_PATH` — canonical APES template for `STAGE`; read-only.
- `OUTPUT_PATH` — project-owned working copy to create or update under `PROJECT_WORK_ROOT`.
- `EXIT_GATE_CHECKLIST_PATH` — canonical APES checklist for the selected stage; read-only.
- `GATE_RECORD_PATH` — project-owned checklist and Gate Record working copy to create or update under `PROJECT_WORK_ROOT`.
- `GATE_DECISION_OWNER` — named human who alone records the final gate result.
- `STANDARDS_CONTEXT_PATHS` — optional list of relevant context; a Standard module never defines or overrides the output in this alpha, whether its body is `Draft` or still a placeholder.

Use the exact stage mappings in [`Getting Started`](../docs/getting-started.md#choose-one-stage) or [`Stage Gates`](../docs/stage-gates.md#gate-outputs).

## Preflight

Complete this preflight before creating or updating any file:

1. Confirm that `APES_SOURCE_ROOT` and `PROJECT_WORK_ROOT` already exist as directories. Resolve both actual targets. `PROJECT_WORK_ROOT` must be a dedicated project-owned record tree: it must not contain canonical APES source files and must not be an ancestor of `APES_SOURCE_ROOT`.
2. Confirm that `STAGE` exactly matches one of the nine Stage Reference values.
3. Confirm that `TEMPLATE_PATH` and `EXIT_GATE_CHECKLIST_PATH` identify the canonical template and checklist from the same Stage Reference row as `STAGE`, and that both resolve under `APES_SOURCE_ROOT` but outside `PROJECT_WORK_ROOT`.
4. Lexically normalize `TEMPLATE_PATH`, `OUTPUT_PATH`, `EXIT_GATE_CHECKLIST_PATH`, and `GATE_RECORD_PATH`. Walk every path component using link-aware metadata that does not follow the component first (for example, `lstat` or the platform's reparse-point equivalent). Resolve every symbolic link, junction, or reparse point, including a link at the final leaf. A dangling link is a hard stop, not a nonexistent output. For a genuinely absent target with no link entry, resolve its nearest existing ancestor and append the remaining lexical components; this prevents a missing leaf below a symbolic-link or junction parent from escaping the resolved boundary.
5. Confirm that both project-owned targets remain descendants of the resolved `PROJECT_WORK_ROOT`. Reject a target that resolves outside it, including through a relative path, symbolic link, junction, or equivalent alias.
6. Treat every existing file under `APES_SOURCE_ROOT` but outside `PROJECT_WORK_ROOT` as protected APES source. Confirm that neither project-owned target equals, resolves to, or shares file identity with any protected source file. For existing targets, compare filesystem identity (for example, device/inode or volume/file ID), not only path text, so a hard link cannot bypass protection.
7. Confirm that the four main paths identify four distinct targets and that `OUTPUT_PATH` and `GATE_RECORD_PATH` do not share filesystem identity.
8. If `GATE_RECORD_PATH` exists, inspect the Decision cell in its Gate Record table. If it already records final `Pass`, `Failed`, or `Deferred`, stop before changing the artifact or gate record. Preserve that human decision; require a new `GATE_RECORD_PATH`, or a human-owned archive/reopen action that supplies a fresh undecided record. The agent must never clear or carry forward a stale final decision.
9. If any root, stage, mapping, containment, collision, alias, file-identity, or prior-decision check fails, do not create or modify any file. Report the invalid input and expected contract, then stop without guessing a replacement.

## The Canonical Prompt

Copy this block, replace every required placeholder, and give it to the selected agent together with any instructions owned by the adopting project.

```text
You are working in a project that is applying APES (AI Product Engineering Standard).

Run exactly ONE lifecycle stage.

Inputs:
- STAGE: {STAGE}
- APES_SOURCE_ROOT: {APES_SOURCE_ROOT}
- PROJECT_WORK_ROOT: {PROJECT_WORK_ROOT}
- TEMPLATE_PATH: {TEMPLATE_PATH}
- OUTPUT_PATH: {OUTPUT_PATH}
- EXIT_GATE_CHECKLIST_PATH: {EXIT_GATE_CHECKLIST_PATH}
- GATE_RECORD_PATH: {GATE_RECORD_PATH}
- GATE_DECISION_OWNER: {GATE_DECISION_OWNER}
- STANDARDS_CONTEXT_PATHS: {OPTIONAL_PATHS_OR_NONE}

Preflight — complete before any file creation or update:
1. Require APES_SOURCE_ROOT and PROJECT_WORK_ROOT to exist as directories; resolve both. PROJECT_WORK_ROOT must contain no canonical APES source and must not be an ancestor of APES_SOURCE_ROOT.
2. Confirm STAGE exactly matches one of the nine Stage Reference values.
3. Confirm TEMPLATE_PATH and EXIT_GATE_CHECKLIST_PATH match the same Stage Reference row as STAGE and resolve under APES_SOURCE_ROOT but outside PROJECT_WORK_ROOT.
4. Lexically normalize all four main paths. Inspect every component with link-aware metadata before following it; resolve final-leaf links as well as parent links, and treat any dangling link as a hard stop. For a genuinely absent target with no link entry, resolve its nearest existing ancestor and append the remaining components.
5. Confirm OUTPUT_PATH and GATE_RECORD_PATH remain under the resolved PROJECT_WORK_ROOT, including after symbolic-link, junction, or equivalent alias resolution.
6. Protect every existing file under APES_SOURCE_ROOT but outside PROJECT_WORK_ROOT. Reject either project-owned target if it equals, resolves to, or shares filesystem identity with a protected source file; use file identity to detect hard links.
7. Confirm all four main targets are distinct and OUTPUT_PATH and GATE_RECORD_PATH do not share filesystem identity.
8. If an existing GATE_RECORD_PATH has a Gate Record Decision cell of Pass, Failed, or Deferred, stop before changing either project-owned file. Preserve the human result and require a new gate-record path or a human-owned archive/reopen action that supplies a fresh undecided record.
9. If any root, stage, mapping, containment, collision, alias, file-identity, or prior-decision check fails, do not create or modify any file. Report the invalid input and expected contract, then stop without guessing a replacement.

Execution contract — continue only after preflight passes:
1. Read TEMPLATE_PATH and EXIT_GATE_CHECKLIST_PATH. Treat both canonical APES files as read-only.
2. Read project-owned OUTPUT_PATH and GATE_RECORD_PATH if they already exist. Otherwise create working copies at those paths from the canonical inputs.
3. Work only inside STAGE. Do not start, simulate, or approve a later lifecycle stage.
4. Produce the smallest complete stage artifact at OUTPUT_PATH. Preserve the template structure, APES version/source provenance, explicit unknowns, Out of Scope, and boundary statement.
5. For every material product, market, user, or technical claim, cite the source and access date. Label unsupported statements Hypothesis or Unverified; never invent evidence or dates.
6. Prepare GATE_RECORD_PATH from the canonical checklist. Link evidence, mark criteria supported or unmet, and record gaps, compensating evidence, owners, and review dates where applicable.
7. Do not choose or write the final Pass, Failed, or Deferred result. Only the named human GATE_DECISION_OWNER may record that decision.
8. Do not edit TEMPLATE_PATH or EXIT_GATE_CHECKLIST_PATH. Do not silently waive a gate. "We will add it later" is not evidence.
9. Treat STANDARDS_CONTEXT_PATHS as optional context only. If a context file is a placeholder or conflicts with the selected template/checklist contract, report the gap and follow the explicit inputs above.

Handoff report:
- OUTPUT_PATH created or updated.
- GATE_RECORD_PATH created or updated.
- Evidence used, with source and access date.
- Supported and unmet gate criteria.
- Remaining hypotheses, gaps, risks, and compensating evidence.
- The next action required from GATE_DECISION_OWNER.
- Any place APES failed to handle the work.

Stop after the handoff. Do not begin the next stage.
```

## Stage Reference

| Stage | Canonical Template | Exit-Gate Checklist |
| --- | --- | --- |
| Idea | [`idea-brief.md`](../templates/idea-brief.md) | [`gate-1-idea-to-discovery.md`](../checklists/gate-1-idea-to-discovery.md) |
| Discovery | [`discovery-interview-notes.md`](../templates/discovery-interview-notes.md) | [`gate-2-discovery-to-research.md`](../checklists/gate-2-discovery-to-research.md) |
| Research | [`research-note.md`](../templates/research-note.md) | [`gate-3-research-to-validation.md`](../checklists/gate-3-research-to-validation.md) |
| Validation | [`validation-experiment-plan.md`](../templates/validation-experiment-plan.md) | [`gate-4-validation-to-product.md`](../checklists/gate-4-validation-to-product.md) |
| Product | [`product-scope-spec.md`](../templates/product-scope-spec.md) | [`gate-5-product-to-business.md`](../checklists/gate-5-product-to-business.md) |
| Business | [`business-viability-brief.md`](../templates/business-viability-brief.md) | [`gate-6-business-to-engineering.md`](../checklists/gate-6-business-to-engineering.md) |
| Engineering | [`engineering-change-record.md`](../templates/engineering-change-record.md) | [`gate-7-engineering-to-growth.md`](../checklists/gate-7-engineering-to-growth.md) |
| Growth | [`growth-experiment-record.md`](../templates/growth-experiment-record.md) | [`gate-8-growth-to-knowledge.md`](../checklists/gate-8-growth-to-knowledge.md) |
| Knowledge | [`retrospective-and-learning-record.md`](../templates/retrospective-and-learning-record.md) | [`gate-9-knowledge-to-discovery.md`](../checklists/gate-9-knowledge-to-discovery.md) |

## Agent Obligations

- Protect canonical inputs and write only to project-owned paths.
- Keep observations, inferences, and unsupported hypotheses distinguishable.
- Prefer existing project evidence and artifacts before creating new claims.
- Prepare an auditable gate record without impersonating the human owner.
- Surface uncertainty and APES workflow gaps in the handoff.

## Anti-Patterns

- Editing the APES source template or checklist during project execution.
- Treating any Standard module, placeholder or `Draft`, as the artifact definition.
- Importing APES's repository-maintainer `AGENTS.md` as adopter policy.
- Fabricating a citation, access date, interview, test result, or user observation.
- Recording a final gate decision on behalf of the human owner.
- Drifting into a later stage or continuing after handoff.

## Tool Adaptation

Tool-specific examples may explain how to supply this prompt and the adopting repository's own instructions. They must preserve every required input, the canonical-file boundary, the human gate decision, and the final stop. See [`examples/`](../examples/README.md).

## Status

Active for `v0.2.0-alpha.1`. It has bounded internal maintainer dogfood only and has not been validated by an external real-project case.
