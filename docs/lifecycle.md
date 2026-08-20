# Lifecycle

- Status: Placeholder
- Version: v0.1
- Owner: APES Maintainers
- Last Updated: 2026-08-19
- Purpose: Describe the end-to-end AI product lifecycle used by APES.

## Table of Contents

- [Overview](#overview)
- [Stages](#stages)
- [Iteration](#iteration)
- [Next Steps](#next-steps)

## Overview

APES organizes product engineering into nine stages. Stages are sequential at the project level but revisited cyclically as learning accumulates.

## Stages

1. **Idea** — Capture the opportunity, problem, or hypothesis.
2. **Discovery** — Understand users, problems, and context.
3. **Research** — Investigate technical, market, and ecosystem evidence.
4. **Validation** — Test the strongest hypotheses with real users and real data.
5. **Product** — Define scope, requirements, and experience.
6. **Business** — Confirm viability, pricing, and go-to-market fit.
7. **Engineering** — Build the system with evidence-based practice.
8. **Growth** — Acquire, activate, and retain users.
9. **Knowledge** — Capture learnings and feed them back into Discovery.

Eight stages currently have matching placeholder module directories under [`../standards/`](../standards/README.md). Idea is represented at the lifecycle and template layers rather than by a standard module, while `standards/repository/` is a cross-cutting module and not a lifecycle stage.

## Iteration

The lifecycle is not strictly linear. Knowledge feeds Discovery. Validation can return work to Research. Engineering and Growth feed back into the Product and Business stages.

## Next Steps

- See [`stage-gates.md`](stage-gates.md) for what must be true to move between stages.
- See [`maturity-model.md`](maturity-model.md) for how to assess overall APES adoption.
