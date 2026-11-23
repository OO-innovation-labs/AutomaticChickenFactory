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

Freeze the committed candidate, run `validate`, and record its immutable report.
Hand off to `acceptance-verifier`; source changes require fresh checks/review.
If committing is outside scope, return the result with that blocker. Keep transient
evidence ignored and change explanations in the PR. Publishing/release needs session
authorization.

Apply `delivery.testing` in `.factory/direction.json` for test selection, evidence
reuse and escalation. During iteration use focused files or `pnpm test:affected`;
formal `validate` still runs every required check on the frozen candidate.
