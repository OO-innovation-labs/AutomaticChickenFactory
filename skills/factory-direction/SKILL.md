---
name: factory-direction
description: Set factory priorities, resolve architecture decisions, and improve agent roles, routing or skills from delivery evidence.
---

# Factory Direction

Use the assigned contract in dispatch or `pnpm factory contract ROLE`.
Read current `.factory/direction.json` and `board`. Base improvements on job histories and evidence.

Set priorities from owner goals; resolve cross-area architecture using the root
glossary and ADRs. Evaluate recurring rework, blocked handoffs, escaped defects and
observed execution cost. Propose bounded changes with expected results and meaningful
successful/failing cases; obtain the owner's decision unless already authorized.

Apply approved changes to their single authoritative configuration or skill. Use
`skill-creator` and `writing-for-agents` for skill edits. Keep documentation to minimal
functional references; put specifications and decisions in GitHub Issues. All jobs
use current configuration directly; retain outcomes and evidence rather than policy
copies or parallel legacy workflows.

Run `pnpm test:factory`, validate changed skills and forward-test ready, ambiguous,
blocked and incident work. Check invariant load and safe split choices, not only size.
Return evidence, remaining limits and the next observation condition. Read resource,
context and command settings from configuration and `docs/factory.md`; record observed
usage honestly. Factory changes do not authorize paid runs, merges or production.
