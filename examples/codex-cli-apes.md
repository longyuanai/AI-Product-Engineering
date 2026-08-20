# Codex CLI — APES Adaptation Example

- Status: Draft
- Version: v0.2
- Owner: APES Maintainers
- Last Updated: 2026-08-19
- Purpose: Show how to supply the tool-neutral APES one-stage contract to Codex CLI without depending on unverified project-memory behavior.

## Table of Contents

- [What This Is](#what-this-is)
- [Evidence-Bounded Tool Facts](#evidence-bounded-tool-facts)
- [Project Instruction Boundary](#project-instruction-boundary)
- [Research Example](#research-example)
- [Expected Handoff](#expected-handoff)
- [Open Question](#open-question)
- [Status](#status)

## What This Is

This adapter instantiates the canonical [`run-apes-stage`](../commands/run-apes-stage.md) command for Research. The command contract, template, checklist, human decision, and stop rule remain identical to every other tool path. This is not an endorsement of one vendor over another.

## Evidence-Bounded Tool Facts

The repository's current evidence confirms that OpenAI Codex CLI exists at `openai/codex`, describes itself as a coding agent that runs in a local terminal, and uses Apache-2.0 (SRC-015, EV-002, access date 2026-08-03). The source register does not verify whether it automatically loads `AGENTS.md`.

## Project Instruction Boundary

Use the adopting project's own repository instructions and the tool's currently documented context mechanism. Do not depend on automatic `AGENTS.md` loading, and do not import APES's root `AGENTS.md`: that file is maintainer policy for this repository.

Provide the APES command by pasting it into the session or referencing a project-local copy. The explicit input paths are the portable contract.

## Research Example

Ensure the read-only APES source is available and create the project-owned record directory. Then give Codex CLI the canonical prompt with these values:

```text
STAGE: Research
APES_SOURCE_ROOT: vendor/apes
PROJECT_WORK_ROOT: project-artifacts
TEMPLATE_PATH: vendor/apes/templates/research-note.md
OUTPUT_PATH: project-artifacts/research/feature-evidence.md
EXIT_GATE_CHECKLIST_PATH: vendor/apes/checklists/gate-3-research-to-validation.md
GATE_RECORD_PATH: project-artifacts/gates/research-to-validation.md
GATE_DECISION_OWNER: Casey Maintainer
STANDARDS_CONTEXT_PATHS: vendor/apes/standards/research/README.md (optional placeholder context)
```

Required instruction:

```text
Follow commands/run-apes-stage.md with the supplied values. Treat TEMPLATE_PATH and EXIT_GATE_CHECKLIST_PATH as read-only. Create or update only the project-owned OUTPUT_PATH and GATE_RECORD_PATH. Cite source and access date, distinguish observation from inference, retain counter-evidence, and prepare the Gate 3 evidence without selecting Pass, Failed, or Deferred. Casey Maintainer owns the final gate decision. Stop after the handoff and do not begin Validation.
```

The paths are illustrative; use paths that clearly separate vendored or upstream APES sources from project-owned evidence.

## Expected Handoff

Codex CLI should report:

- the Research artifact and Gate 3 working-record paths;
- search and verification evidence with source and access date;
- contradictions, supported and unmet criteria, and remaining hypotheses;
- the exact next action for `Casey Maintainer`; and
- any workflow gap found in APES.

The human owner reviews the record and enters the final decision. An uncited summary, planned search, or generated conclusion is not evidence by itself.

## Open Question

Whether Codex CLI automatically loads `AGENTS.md` remains unverified in the APES source register. This adapter does not rely on that behavior.

## Status

Draft adapter for `v0.2.0-alpha.1`. The command path has internal maintainer dogfood only and no external real-project validation.
