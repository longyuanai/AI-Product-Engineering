# ADR-0001 — Project Positioning

- **Title:** Project and standard name, positioning, and scope boundaries
- **Status:** Accepted
- **Date:** 2026-08-03

## Table of Contents

- [Context](#context)
- [Decision](#decision)
- [Consequences](#consequences)
- [Alternatives Considered](#alternatives-considered)

## Context

The team is starting a vendor-neutral, evidence-driven standard for AI-assisted product engineering. Several positioning choices — the project's name, the standard's name, what it claims to be, and what it explicitly does not do — need to be settled before any standard module is drafted. Without these decisions, contributing teams cannot align on identity, scope, or handoff boundaries with adjacent standards and tools.

## Decision

1. The repository will be named **`AI-Product-Engineering`**.
2. The standard will be named **`AI Product Engineering Standard (APES)`**.
3. APES will be positioned as a **vendor-neutral, evidence-driven** AI product engineering standard.
4. APES will **not** replace, compete with, or be wrapped inside:
   - `AGENTS.md`-style agent guidance documents.
   - The Model Context Protocol (MCP).
   - Specific coding agents or IDEs (Claude Code, Codex, Cursor, etc.).
5. APES will focus, at this stage, on **documentation and standards validated by real cases**, not on building a large tool ecosystem (CLI, MCP server, IDE extension, website).

## Consequences

Positive:

- A clear, memorable identity that distinguishes the repository from any single AI tool.
- A strong evidence-first framing for every later module.
- A defensible scope boundary makes it easier to say "no" to scope creep.
- Compatible with, not competitive against, common agent and IDE conventions.

Negative and risks:

- The acronym "APES" may be confused with other projects; a longer name must always be available.
- The vendor-neutral claim requires discipline: any example that reads as endorsement must be reframed as illustration.
- Deferring tooling means adopters have to bridge to their own tools; this is acceptable but must be communicated.

Operational consequences:

- All root-level documents (README, VISION, MANIFESTO) must avoid claims of industry-standard status or market position.
- `AGENTS.md` rules bind AI agents operating in this repository.
- Future ADRs must reference this one when extending scope.

## Alternatives Considered

### Alternative A — "AI Engineering Operating System"

Pros:

- Conveys a holistic toolset framing.

Cons:

- Implies building an operating system and tool platform.
- Conflicts with the decision to defer tooling.
- Conflates standard with implementation.
- Vendor neutrality is harder to maintain when an "OS" implies bundling.

Decision: rejected.

### Alternative B — "AI Product Engineering Protocol"

Pros:

- "Protocol" suggests a simpler, lighter artifact than a "standard".
- Avoids market-positioning pressure.

Cons:

- Ambiguous in product/engineering circles (HTTP protocol? Internal protocol?).
- Understates the lifecycle and governance scope we intend.
- Less useful as a recognizable project identity.

Decision: rejected for now. Kept as a candidate sub-brand for any future interoperability layer.

### Alternative C — "AI Coding Workflow"

Pros:

- Specific and easy to grasp.
- Aligns with day-to-day vocabulary of practitioners.

Cons:

- Reduces scope to coding, excluding discovery, validation, business, growth, and knowledge stages.
- Reopens "we are just a coding guide" framings we explicitly want to avoid.
- Hard to extend without renaming.

Decision: rejected.
