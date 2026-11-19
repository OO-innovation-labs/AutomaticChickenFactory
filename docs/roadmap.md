# Implementation roadmap

All milestones are **planned**. Publishing this specification completes no engine migration milestone. Each milestone should be a bounded PR or a set of dependency-linked issues with one integration owner.

| Milestone | Depends on | Deliverable and exit condition |
| --- | --- | --- |
| M0 Baseline | — | Complete import/file/command/state/CI inventory; install locked dependencies; green baseline or triaged reproducible failures; representative serialized fixtures |
| M1 Bootstrap | M0 | Factory source layout, independent CI, ownership/precedence ADR review, version/ref strategy; clean clone contains no application source |
| M2 Engine extraction | M1 | CLI/core/state/evidence/shared skills moved; explicit project context replaces repo-relative loading; baseline behavioral parity |
| M3 Extension contract | M2 | JSON Schema, safe precedence, role inheritance and adapter interfaces; actionable rejection tests before dispatch |
| M4 Cepstrum adapter | M3 | Project-only config/skills/checks/runbooks and pinned launcher; application CI plus factory integration passes |
| M5 Second-project proof | M3 | Python fixture on `trunk`, no pnpm assumption; complete workflow and failure/recovery proof without engine edits |
| M6 Migration rehearsal | M4, M5 | Isolated dry run, state/evidence preservation, single-coordinator fencing and rollback rehearsal; owner reviews cutover decision |
| M7 Cutover and release | M6 | Explicitly authorized cutover, immutable release/ref, clean onboarding rehearsal and complete operational docs; remove duplicate engine only after parity |

## Required test matrix

- Cepstrum and unrelated Python/trunk fixture: preflight → intake → dispatch → candidate validation → independent acceptance → review → PR preparation.
- Missing configuration, invalid inheritance and unsafe overrides fail before dispatch or state mutation.
- Competing coordinators, lease expiry, stale writer, crash during persistence, checkpoint/resume and exhausted retry budgets.
- Changed candidate/base/policy/factory revision, missing artifacts and acceptance from engineering session are rejected.
- Mock provider failures and remote base/head drift; authorized publication tests verify saved-body readback. Live publication requires task authorization.
- State migration/rollback, interrupted migration and evidence hash preservation.
- Application integration/CI remains mandatory in Cepstrum. Fixture success alone cannot establish parity.

## Review boundaries

Keep generic state/evidence invariants together during extraction. Separate configuration/schema changes from project cutover. Separate provider adapters from core state transitions. Every PR explains affected invariant groups, integration seams, selected tests and remaining evidence. Freeze each candidate before formal validation; new source requires fresh checks and independent acceptance.

## Completion tracking

For each milestone record its issue/PR, owner, factory/project/base SHAs, reports, CI URLs and acceptance disposition. Actual execution evidence belongs in ignored durable stores and linked reports; this roadmap must not invent success. Merge and production actions require separate session authorization.
