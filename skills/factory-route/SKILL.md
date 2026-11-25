---
name: factory-route
description: Route GitHub backlog work, coordinate production incidents, and resume factory jobs with durable ownership and handoffs.
---

# Factory Route

Start each factory invocation in the current chat. Establish its scope and own its
coordination here; delegate bounded supporting work only after that. Consult repository
instructions and factory records for context. Contact another chat only when the user
explicitly requests it; an existing factory chat is not the default entry point.

Before routing or editing, run the preflight (`factory-manager` step 1) from the selected checkout.
Resolve the reported readiness failures while preserving unrelated work. If the local
factory entry point is absent, inspect Git status and current main before searching
other installations; update safely or read the instructions from that revision.

Use `sync`, `board` and `dispatch` for routing and assigned contracts. Read the
configuration only when changing routing rules; use `docs/factory.md` for commands.
Inspect each candidate's current
issue, native dependencies, readiness and acceptance before routing.

Use one integration owner and the existing checkout; configure `workspace` before
engineering claims. Before starting workers, use the `factory-plan` delivery plan
to reserve capacity for integration, independent acceptance/review, and a bounded repair pass.
Reduce the implementation slice when capacity is tight; retain the verification
reserve. Record unavailable capacity explicitly and checkpoint when it prevents
independent verification.
Before starting any worker, apply the assignment rubric in `docs/factory.md`.
Record the class and deciding evidence for each new assignment, including handoffs
and supporting delegations. Claim factory jobs with a stable session identity. Include actual host
token telemetry when exposed; otherwise omit token fields and retain the explicit
unavailable-enforcement record. A checkpoint cites the commit SHA that holds the work so far; commit first, per the
`factory-build` cadence. Checkpoint proactively without inventing usage or
sign-off. Provide the leased dispatch packet and assigned skill to a fresh worker
context.
Pass its exact resolved model/effort (provider from `FACTORY_PROVIDER` or direction.json); stop for a resource decision if unavailable. Delegate
independent work and verification when available; otherwise report missing
independence. Coordinate shared files and freeze candidates during validation.

Honor dependency, lease, retry, incident and context gates. Checkpoint before the
context ceiling; continue in a fresh session with `fork_turns='none'`, preserving
attempts and budgets. Keep packets to bounded tasks and evidence pointers.

Require evidence and a next owner/action at handoff. Publish complete prepared PRs
with diagrams only within session authorization; confirm saved content. Report
material results, blockers and decisions. Factory records grant no external access.
