# Factory specification

## Purpose and scope

AutomaticChickenFactory will own reusable orchestration. Consuming projects will own their business context, checks, skills and delivery environments. A developer must be able to clone a pinned factory revision, connect a project and complete a workflow without editing factory source.

This repository currently delivers a specification and roadmap only. Requirements below are implementation acceptance conditions, not claims of current capability.

## Required capabilities

| ID | Requirement | Acceptance evidence |
| --- | --- | --- |
| R1 | Independent factory home, CI and versioned release/ref | Run engine tests in a clean clone with no Cepstrum files available |
| R2 | Explicit project resolution and pinned consumption | Execute from outside both repositories using `--project`; Cepstrum contains no generic engine copies |
| R3 | Versioned configuration validated before dispatch | Unknown fields, missing commands, unresolved roles and unsafe overrides fail with field paths and remedies |
| R4 | Project-local extension without engine edits | Add a specialist, area and non-pnpm check entirely in a fixture project |
| R5 | Preserve routing, leases, checkpoints, budgets and independent acceptance | Baseline fixtures pass before and after extraction, including stale and forged evidence rejection |
| R6 | Namespaced durable state and revision-bound evidence | Two projects operate independently; second coordinator for the same namespace is rejected; archive and recovery round trip |
| R7 | Toolchain and base independence | Python fixture on `trunk` completes preflight, intake, dispatch, validation, independent acceptance, PR preparation and recovery |
| R8 | Explicit external authority | Tests prove configuration cannot grant merge or production authorization |

## Invariants

- Every active job has one accountable owner, lease token and stable session identity. Expired ownership requires inspected recovery.
- Dependencies and readiness gate dispatch. Missing model/resources or acceptance criteria produce explicit blockers.
- Checkpoint/resume preserves attempts, budgets and evidence pointers. Telemetry that is unavailable stays marked unavailable.
- Implementation, acceptance and review bind to the same candidate, base, effective policy and environment. Factory revision is also recorded. Changed inputs invalidate matching evidence.
- Acceptance runs in an independent context and produces its own manifest; relabeling engineering results is rejected.
- Required checks fail closed on missing tools, zero discovered tests, skipped required checks or unavailable required services.
- Diff review explains invariant groups and safe split boundaries. Large or coupled changes require independent architecture disposition.
- PR preparation is read-only. Authorized publication verifies remote head/base, evidence and saved description; all pushed revisions are followed through CI.
- Release identity and deployed verification remain separate evidence stages. A draft PR does not complete a production delivery.
- No merge, deployment or live cutover follows implicitly from publication, configuration or a passing test.

## Definition of done for the future implementation

All R1–R8 acceptance artifacts exist for Cepstrum and the unrelated fixture; onboarding works from a clean environment; release and project pins are immutable; rollback has been rehearsed. Reviewers can trace every requirement to CI and revision-bound evidence. The original migration issue stays open until these conditions are met.
