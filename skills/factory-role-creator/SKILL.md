---
name: factory-role-creator
description: Create or adjust project-specific roles, areas and specialist skills when the project has work no existing role or skill owns, without changing the factory itself.
---

# Factory Role Creator

Use the assigned contract in dispatch or `pnpm factory contract ROLE`. This role
shapes the project's staffing; `factory-direction` owns the factory. Skills named
`factory-*`, factory scripts, department contracts and `.factory/direction.json`
limits are out of scope here; route those to `factory-direction`.

Start from evidence: unrouted or repeatedly misrouted jobs on `board`, rework from
missing domain context, or a request the manager could not match. Check that no
existing area, role or specialist skill already covers it; extending one is better
than adding one.

Propose the smallest project-scoped change, with the evidence behind it:

- **Area**: patterns, paths and one owner in `areas` of `.factory/config.json`.
- **Role**: an `agents` entry using an existing department skill (usually
  `factory-build`), a mission limited to the area, and only the handoffs it needs.
- **Specialist skill**: only when the area needs domain knowledge no existing skill
  holds. Name it without the `factory-` prefix, place it in `.agents/skills`, and
  write it with `skill-creator` and `writing-for-agents`. Link the project's
  glossary and ADRs rather than copying them.
- **Discovery**: list the specialist in the "Domain and specialist context" section of
  `AGENTS.md`, the one place the manager reads for project specialists.

State the expected result and a successful and a failing case. Obtain the owner's
decision before applying unless already authorized. Apply to the single
authoritative file; never copy role text elsewhere. Run `pnpm test:factory`,
validate the new skill, and forward-test with a real or representative issue through
`pnpm factory contract` and `dispatch`. Deliver it as one PR through the manager.
Return evidence, remaining limits and what to observe next.
