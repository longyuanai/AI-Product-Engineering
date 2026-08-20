# Claude Code — APES Adaptation Example

- Status: Draft
- Version: v0.2
- Owner: APES Maintainers
- Last Updated: 2026-08-19
- Purpose: Show how to supply the tool-neutral APES one-stage contract to Claude Code without importing APES maintainer policy.

## Table of Contents

- [What This Is](#what-this-is)
- [Evidence-Bounded Tool Fact](#evidence-bounded-tool-fact)
- [Project Instruction Boundary](#project-instruction-boundary)
- [Validation Example](#validation-example)
- [Expected Handoff](#expected-handoff)
- [Status](#status)

## What This Is

This adapter instantiates the canonical [`run-apes-stage`](../commands/run-apes-stage.md) command for Validation. The command contract, template, checklist, human decision, and stop rule remain identical to every other tool path. This is not an endorsement of one vendor over another.

## Evidence-Bounded Tool Fact

The repository's current evidence says Claude Code reads `CLAUDE.md` by default, not `AGENTS.md`; import, copy, or symlink workflows can expose other instructions (SRC-014, VR-033, access date 2026-08-15). Reverify current product behavior before relying on details beyond that recorded claim.

## Project Instruction Boundary

Use the adopting project's own `CLAUDE.md` and repository policies. Do not copy or import APES's root `AGENTS.md`: that file governs maintenance of the APES repository and may block legitimate adopter work.

Provide the APES command by pasting it into the session or referencing a project-local copy. The explicit input paths are the portable contract.

## Validation Example

Ensure the read-only APES source is available and create the project-owned record directory. Then give Claude Code the canonical prompt with these values:

```text
STAGE: Validation
APES_SOURCE_ROOT: vendor/apes
PROJECT_WORK_ROOT: project-artifacts
TEMPLATE_PATH: vendor/apes/templates/validation-experiment-plan.md
OUTPUT_PATH: project-artifacts/validation/experiment-plan.md
EXIT_GATE_CHECKLIST_PATH: vendor/apes/checklists/gate-4-validation-to-product.md
GATE_RECORD_PATH: project-artifacts/gates/validation-to-product.md
GATE_DECISION_OWNER: Casey Maintainer
STANDARDS_CONTEXT_PATHS: vendor/apes/standards/validation/README.md (optional placeholder context)
```

Required instruction:

```text
Follow commands/run-apes-stage.md with the supplied values. Treat TEMPLATE_PATH and EXIT_GATE_CHECKLIST_PATH as read-only. Create or update only the project-owned OUTPUT_PATH and GATE_RECORD_PATH. Cite source and access date, leave unsupported claims as Hypothesis or Unverified, and prepare the Gate 4 evidence without selecting Pass, Failed, or Deferred. Casey Maintainer owns the final gate decision. Stop after the handoff and do not begin Product.
```

The paths are illustrative; use paths that clearly separate vendored or upstream APES sources from project-owned evidence.

## Expected Handoff

Claude Code should report:

- the Validation artifact and Gate 4 working-record paths;
- evidence used with source and access date;
- supported and unmet criteria, risks, and remaining hypotheses;
- the exact next action for `Casey Maintainer`; and
- any workflow gap found in APES.

The human owner reviews the record and enters the final decision. A filled template, generated answer, or future experiment promise is not evidence by itself.

## Status

Draft adapter for `v0.2.0-alpha.1`. The command path has internal maintainer dogfood only and no external real-project validation.
