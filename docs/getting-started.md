# Getting Started

- Status: Active
- Version: v0.2
- Owner: APES Maintainers
- Last Updated: 2026-08-19
- Purpose: Guide a first-time user through one bounded APES lifecycle stage and its manual exit gate.

## Table of Contents

- [Alpha Promise](#alpha-promise)
- [Before You Start](#before-you-start)
- [Choose One Stage](#choose-one-stage)
- [Create Working Copies](#create-working-copies)
- [Run One Stage](#run-one-stage)
- [Record the Manual Gate Decision](#record-the-manual-gate-decision)
- [Stop](#stop)
- [Alpha Boundary](#alpha-boundary)

## Alpha Promise

> `v0.2.0-alpha.1` provides documented and repository-contract-tested mappings for all nine APES lifecycle stages from canonical template/checklist inputs to project-owned artifact/gate-record paths. Internal maintainer dogfood has exercised only the Idea path; the other eight paths and unaffiliated first-time-user usability remain unverified. A named human alone records the final gate decision.

## Before You Start

You need a project-owned repository or workspace, a current lifecycle stage, one named human gate owner, and any evidence already available. Read the short [`lifecycle`](lifecycle.md) and [`stage-gate`](stage-gates.md) definitions if the current stage is uncertain.

APES source templates and checklists are canonical references. Do not fill them in place. Your completed artifact and gate record belong in project-owned paths so APES can be upgraded or compared without overwriting project evidence.

## Choose One Stage

Choose exactly one row. The stage artifact is produced from the template; the transition is assessed with the matching exit-gate checklist.

| Stage | Canonical Template | Exit Gate | Canonical Checklist |
| --- | --- | --- | --- |
| Idea | [`idea-brief.md`](../templates/idea-brief.md) | Idea → Discovery | [`gate-1-idea-to-discovery.md`](../checklists/gate-1-idea-to-discovery.md) |
| Discovery | [`discovery-interview-notes.md`](../templates/discovery-interview-notes.md) | Discovery → Research | [`gate-2-discovery-to-research.md`](../checklists/gate-2-discovery-to-research.md) |
| Research | [`research-note.md`](../templates/research-note.md) | Research → Validation | [`gate-3-research-to-validation.md`](../checklists/gate-3-research-to-validation.md) |
| Validation | [`validation-experiment-plan.md`](../templates/validation-experiment-plan.md) | Validation → Product | [`gate-4-validation-to-product.md`](../checklists/gate-4-validation-to-product.md) |
| Product | [`product-scope-spec.md`](../templates/product-scope-spec.md) | Product → Business | [`gate-5-product-to-business.md`](../checklists/gate-5-product-to-business.md) |
| Business | [`business-viability-brief.md`](../templates/business-viability-brief.md) | Business → Engineering | [`gate-6-business-to-engineering.md`](../checklists/gate-6-business-to-engineering.md) |
| Engineering | [`engineering-change-record.md`](../templates/engineering-change-record.md) | Engineering → Growth | [`gate-7-engineering-to-growth.md`](../checklists/gate-7-engineering-to-growth.md) |
| Growth | [`growth-experiment-record.md`](../templates/growth-experiment-record.md) | Growth → Knowledge | [`gate-8-growth-to-knowledge.md`](../checklists/gate-8-growth-to-knowledge.md) |
| Knowledge | [`retrospective-and-learning-record.md`](../templates/retrospective-and-learning-record.md) | Knowledge → Discovery | [`gate-9-knowledge-to-discovery.md`](../checklists/gate-9-knowledge-to-discovery.md) |

## Create Working Copies

Create a directory reserved for artifacts and gate records owned by the adopting project. A simple layout is:

```text
project-artifacts/                 # PROJECT_WORK_ROOT
  {stage}-artifact.md              # OUTPUT_PATH
  gates/
    {stage}-exit-gate.md           # GATE_RECORD_PATH
```

Keep these paths ready:

- `APES_SOURCE_ROOT` — existing directory containing the read-only APES source installation.
- `PROJECT_WORK_ROOT` — existing project-owned record directory; it must contain no canonical APES source file.
- `TEMPLATE_PATH` — canonical APES template; read-only and under `APES_SOURCE_ROOT`.
- `OUTPUT_PATH` — project-owned stage artifact under `PROJECT_WORK_ROOT`.
- `EXIT_GATE_CHECKLIST_PATH` — canonical APES checklist; read-only and under `APES_SOURCE_ROOT`.
- `GATE_RECORD_PATH` — project-owned gate working copy under `PROJECT_WORK_ROOT`.
- `GATE_DECISION_OWNER` — named human accountable for the final decision.

Before any write, the command resolves the roots, inspects every path component without first following links, resolves final-leaf and parent links, and distinguishes a genuinely missing leaf from a dangling link. It rejects dangling links, output outside `PROJECT_WORK_ROOT`, any alias or hard link to protected APES source, and any existing gate record whose Decision cell is already `Pass`, `Failed`, or `Deferred`. A later run uses a fresh undecided gate record; an agent never clears or carries forward an earlier human result.

Retain the APES candidate version and canonical source path in each working copy so provenance remains visible.

## Run One Stage

Use the canonical [`run-apes-stage`](../commands/run-apes-stage.md) instruction. Supply all required inputs and optionally list relevant Standard modules as context. Standard modules are placeholders in this alpha: they may provide orientation but do not define the artifact or override the selected template.

You may pass the command to any capable coding agent, or use the [`Claude Code`](../examples/claude-code-apes.md) or [`Codex CLI`](../examples/codex-cli-apes.md) adaptation. Follow the adopting repository's own project instructions; APES's root `AGENTS.md` is maintainer policy for this repository, not a portable adopter requirement.

The agent should produce one artifact, prepare evidence references and checklist state, identify unmet criteria, and report the next human action. Unsupported statements remain `Hypothesis` or `Unverified`.

## Record the Manual Gate Decision

The agent may prepare evidence and mark which criteria appear satisfied or unmet. It must not choose the final gate result.

The human named by `GATE_DECISION_OWNER` reviews the working gate record and records exactly one result:

- `Pass` — the evidence supports entering the next stage.
- `Failed` — the gate is not met and the unmet criteria are recorded.
- `Deferred` — a time-bounded decision is postponed with an owner and review date.

No gate is silently waived. “We will add it later” is not evidence.

## Stop

After the human decision is recorded, stop. Do not begin the next lifecycle stage automatically. A new stage requires a new explicit invocation, fresh inputs, and the applicable template and exit gate.

## Alpha Boundary

This path is a provisional Project Layer workflow. It is not final v0.2, F5, a deterministic Release Layer bundle, an externally validated methodology, adoption evidence, or an industry standard. No external real-project case exists yet, and internal maintainer dogfood does not satisfy the roadmap real-case requirement.
