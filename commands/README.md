# commands/

- Status: Active
- Version: v0.2
- Owner: APES Maintainers
- Last Updated: 2026-08-19
- Purpose: Hold standardized, tool-neutral instructions for agents and humans.

## Table of Contents

- [Purpose](#purpose)
- [Relationship to Project Instructions](#relationship-to-project-instructions)
- [Available Commands](#available-commands)
- [Status](#status)

## Purpose

This directory holds command-style instructions: short, structured prompts that are reproducible across tools. Commands are written workflow contracts, not application code.

## Relationship to Project Instructions

The adopting project's own instructions govern its repository. APES commands add one bounded lifecycle task and must not override those instructions.

APES's root [`AGENTS.md`](../AGENTS.md) governs maintenance of this repository. It is not a portable adopter requirement and must not be imported automatically into another project. Portable APES behavior is defined by explicit command inputs, canonical template and checklist paths, project-owned output paths, and the named human gate owner.

## Available Commands

- [`run-apes-stage.md`](run-apes-stage.md) — Produce one stage artifact, prepare its exit-gate evidence, hand the final decision to a named human, and stop.

## Status

Active for `v0.2.0-alpha.1`. No other command file exists yet.
