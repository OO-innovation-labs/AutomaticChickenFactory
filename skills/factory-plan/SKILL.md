---
name: factory-plan
description: Curate GitHub issues, reproduce reports, define acceptance criteria, and split cross-area work before implementation.
---

# Factory Plan

Use the assigned contract in dispatch; if absent, run `pnpm factory contract ROLE`.
Read current GitHub issue, root
glossary and relevant ADRs. Inspect native dependencies and related/child issues.
Use the configured triage labels; readiness and execution status are separate.

Treat the customer as knowing the desired outcome while leaving its specification
incomplete. Infer the product need behind examples and proposed mechanisms; explore
whether the same need applies to other supported users, languages, engines or flows.
Separate explicit constraints from examples and inferred requirements. Preserve the
requested outcome and scope; broader interpretation does not authorize unrelated
features. Inspect product evidence, state useful assumptions, and resolve routine
details autonomously. Ask only when competing interpretations materially change
behavior, scope, cost or risk and the available evidence cannot settle them.

Before readiness, express the intended experience as acceptance scenarios, including
representative cases beyond the customer's examples, legitimate exceptions and failure
recovery. Select an implementation approach only after those scenarios are clear.

Curate duplicates/stale requests from evidence. Reproduce reports and define expected
behavior, scope, meaningful checks and one accountable owner. Product uncertainty
needs a bounded decision; domain behavior uses the project's specialist skills.

For work planning, group invariants the reviewer must understand together. Split
independent outcomes at safe behavior/module boundaries, preserving intermediate
compatibility and integrated regressions. Use the diff assessment in `docs/factory.md`;
size signals a judgment call, not an automatic split. Link children/dependencies
natively and identify the integration owner. Give each idea (as `factory-manager`
defines it) its own issue; within an issue, order the slices so each is one or more
atomic commits that leave the branch working.

Before implementation, plan through the requested delivery endpoint: ordered slices,
dependencies, accountable integration owner, checks and evidence, independent review,
and release/rollback when authorized. Allocate available time, context and worker
capacity across implementation, integration, verification and a bounded repair pass.
Identify unavailable access, telemetry or provider evaluation before promising delivery;
record the next action and distinguish local tests from live product evidence. Replan
remaining work and preserve verification capacity when assumptions or limits change.

A decision is settled when it is in the issue or an ADR. After any discussion that
settles one, update the issue (or prepare the exact text when issue edits are outside
session authorization) and correct wording it contradicts. Mark open points as open.

Keep specs in GitHub Issues with `--body-file` for multiline changes. Hand off only
when acceptance, dependencies, ownership and verification are clear; route an already
ready issue directly. Analysis is not implementation completion.
