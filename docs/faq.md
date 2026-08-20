# Frequently Asked Questions

- Status: Active
- Version: v0.2
- Owner: APES Maintainers
- Last Updated: 2026-08-19
- Purpose: Answer common questions about the APES alpha and its one-stage workflow.

## Table of Contents

- [Alpha](#alpha)
- [Using One Stage](#using-one-stage)
- [Tools and Standards](#tools-and-standards)
- [Governance and License](#governance-and-license)

## Alpha

### What does v0.2.0-alpha.1 promise?

`v0.2.0-alpha.1` provides documented and repository-contract-tested mappings for all nine APES lifecycle stages from canonical template/checklist inputs to project-owned artifact/gate-record paths. Internal maintainer dogfood has exercised only the Idea path; the other eight paths and unaffiliated first-time-user usability remain unverified. A named human alone records the final gate decision.

### Is this final v0.2 or an industry standard?

No. It is a provisional APES Project Layer snapshot. It is not final v0.2, a Foundation or Research OS version assignment, F5, a deterministic Release Layer bundle, a mature or externally validated methodology, or an industry standard.

### Has APES been validated by real projects?

No external real-project case exists yet. Maintainer dogfood tests the repository's usability, but it is not adoption evidence, external validation, or satisfaction of the roadmap real-case requirement.

## Using One Stage

### What is the fastest way to start?

Open [`Getting Started`](getting-started.md), choose exactly one stage row, copy its canonical template and exit-gate checklist to project-owned paths, and supply the required inputs to [`run-apes-stage`](../commands/run-apes-stage.md).

### Why must I copy the template and checklist?

Canonical APES files are read-only references. A working copy protects upstream structure, preserves project evidence separately, and makes later APES upgrades or comparisons possible.

### Can the agent pass the gate?

No. The agent may prepare evidence, mark criteria supported or unmet, and identify gaps. Only the named human `GATE_DECISION_OWNER` records `Pass`, `Failed`, or `Deferred` in the project-owned gate record.

### Does Pass automatically start the next stage?

No. Every run stops after the human decision. The next lifecycle stage requires a new explicit invocation.

## Tools and Standards

### Does APES require Claude Code, Codex, or another vendor?

No. The canonical command is tool-neutral. Tool-specific examples are optional adapters and do not change the workflow contract.

### Should an adopting project copy APES's AGENTS.md?

No. APES's root `AGENTS.md` is maintainer policy for this repository. Adopters use their own repository instructions and pass the APES command and canonical input paths explicitly.

### What role do Standard modules play in the alpha?

The current module bodies are placeholders. They may be supplied as optional context, but the selected template and exit-gate checklist define the alpha artifact path. Placeholder text never overrides explicit command inputs.

## Governance and License

### What is the license?

Repository-authored APES content uses the Apache License 2.0, SPDX identifier `Apache-2.0`. See [`LICENSE`](../LICENSE) and [`ADR-0004`](../governance/adr/ADR-0004-apache-2-0-repository-license.md). Third-party material retains its original rights and notices.

### Does this alpha approve F2 or start F3?

No. F2 remains `In Review / Request changes` pending eligible independent re-review, and F3 is unstarted. Sprint 2 remains `In Review`; current Research Gate authority remains `RESEARCH AGAIN`.

### Did the alpha resolve the template/checklist Schema type?

No. OQ-11 remains unresolved. Templates and checklists retain the Schema v0.2.0 `Workflow` type and `WORKFLOW-` prefix.
