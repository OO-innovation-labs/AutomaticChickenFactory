---
name: factory-build
description: Implement a ready issue in its assigned product area and hand off a revision with meaningful verification evidence.
---

# Factory Build

Use the assigned contract in dispatch; if absent, run `pnpm factory contract ROLE`.
Read issue/dependency outcomes,
root glossary and relevant ADRs. Preserve unrelated work and the selected checkout;
one integration owner coordinates supporting changes to shared files.

For domain-specific changes, use the project's specialist skills and invariants
listed in its `AGENTS.md`. Inspect all consumers of changed state. API/data work checks isolation, concurrency and compatibility;
packaging/deployment uses the project's build/deploy skill and environment runbook.

Reproduce behavioral defects with meaningful failing regressions where practical.
Exercise affected integration seams and current CI checks. Explain invariant groups
and safe split boundaries; use `assess-diff` from `docs/factory.md` before handoff.
Keep implementation files bounded rather than concentrating a large diff in one.

## Commit cadence

Work in atomic commits: one commit holds one step a reviewer can understand and
revert alone, with its tests. Before the first edit, list the steps as intended
commit subjects. For each step:

1. Make it and run its focused check.
2. Read `git status` and `git diff`; stage only this step's paths or hunks and read
   `git diff --cached`. If the subject needs "and", split it.
3. Commit, saying why in the body when the subject does not.

Start the next step only once the previous one is committed. Keep refactors,
formatting, dependency updates and generated files in their own commits. Each commit
passes its focused check; a failing regression lands with its fix. When stopping or
handing off mid-step, commit it with a `WIP:` subject naming what is missing, and
squash it into the finished step before freezing. Rewrite only unpushed commits
that no evidence or review cites.

Cadence applies to local commits; push at handoff or when a remote copy is needed,
since every push must be followed through CI. Pre-existing uncommitted changes stay
the user's: leave them unstaged.

## New ideas while building

When work reveals something outside the issue's acceptance criteria, park it: record
the observation, evidence and paths in an issue (or in the handoff when creating
issues is outside session authorization) and return to the current step. A blocking
prerequisite gets its own commit ahead of the work that needs it, or its own PR when
it is useful alone. `factory-manager` routes parked ideas.

## Handoff

Before freezing, account for every path: `git status` shows no uncommitted work of
yours, no `WIP:` commit remains, and each commit in `git log BASE..HEAD` serves the
issue. Move any that does not to its own branch.

Freeze the committed candidate, run `validate`, and record its immutable report.
Hand off to `acceptance-verifier`; source changes require fresh checks/review.
If committing is outside scope, return the result with that blocker. Keep transient
evidence ignored and change explanations in the PR. Publishing/release needs session
authorization.

Apply `delivery.testing` in `.factory/direction.json` for test selection, evidence
reuse and escalation. During iteration use focused files or `pnpm test:affected`;
formal `validate` still runs every required check on the frozen candidate.
