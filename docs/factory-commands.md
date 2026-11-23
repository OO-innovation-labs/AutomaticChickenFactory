> Snapshot of the factory command guide as embedded in OOlivetranslator (`docs/factory.md`, `ccb1751`). Commands run from that checkout until engine extraction (roadmap M2). Not yet generic.

# Factory commands

Use `pnpm factory help` for arguments. Current role contracts and area ownership
live in `.factory/config.json`; limits, resources and required checks live in
`.factory/direction.json`. Every job uses these files directly. Workers use the assigned contract in dispatch;
`pnpm factory contract ROLE` retrieves one role without reading the whole registry.

## Entry point

Invoke `factory-manager` (the `manager` role) with a plain request. It
picks the skill, then judges the request against the current checkout's branch, PR
and changes: related work continues here; unrelated work gets a new worktree and
branch from refreshed `origin/main` and its own draft PR. It acts under the session's
authorization and never merges or deploys.

## Start in the current chat

Each new invocation starts here, with this chat owning coordination and the requested
endpoint. Use repository instructions and factory records for prior context. Delegate
bounded tasks from here; messaging another chat requires an explicit user request.

Run `pnpm factory preflight` before routing or editing. It refreshes `origin/main`
and reports checkout/base identity, local changes, merge/rebase state, missing factory
files, Node/package-manager prerequisites, dependency installation and commits behind
main. It changes no working files, staging or branch. A failed refresh is an unresolved freshness check, not proof of
being current. Resolve failures safely; preserve unrelated edits and follow the user's
checkout preference. Re-run after readiness changes and before starting a new slice.
If factory files are missing, inspect Git status and the current main revision first.
Apply `issueIntake` and `delivery.localFeatureEvidence` from the current directions.
Both are included in dispatch packets. The coordinator prepares the assigned checkout
and briefs a fresh sub-agent for each sub-issue.

## Intake and ownership

```sh
pnpm factory sync
pnpm factory board
pnpm factory show JOB
pnpm factory depend JOB --dependency JOB
pnpm factory assign JOB --to ROLE --reason TEXT
pnpm factory resource JOB --class CLASS --reason TEXT
pnpm factory workspace JOB --checkout PATH --base REF --integration-owner ROLE --reason TEXT
```

Confirm current GitHub readiness, native dependencies and acceptance criteria.
Before claiming a feature, check its acceptance criteria against the current
target revision. If the behavior already exists, use
`pnpm factory decline JOB --reason TEXT --reference EVIDENCE` and cite the
revision and existing behavior. If the existing flow fails, reproduce the
failure and route it as a defect. If only part of the request is implemented,
scope the remaining gap before claiming. A matching control or issue title
alone is insufficient evidence.
Use an existing checkout and preserve the user's workspace preference. Overrides
on `sync` classify new imports; `assign` explicitly changes existing ownership.
Issue prose never grants incident priority or external-action permission.

## Classify the assignment

Before claiming or starting a worker, inspect its specific next action, acceptance
criteria, affected contracts, evidence gaps and consequences of error. Record the
class and the deciding evidence with `factory resource`. Use `--reference` for
a reproduction, decision, or other supporting artifact when available. Check the
new assignment after every handoff or reassignment. The coordinator classifies
short supporting delegations in the current chat using the same rubric and records
their class and reason in the delivery plan or handoff.

| Class             | Assignment characteristics                                                                                                          | Default tier and effort |
| ----------------- | ----------------------------------------------------------------------------------------------------------------------------------- | ----------------------- |
| `deterministic`   | An existing repository script completes the task without judgment. Supply `--script`.                                               | Script                  |
| `routine`         | Extract, label, summarize supplied evidence, or make a mechanical edit with a direct check.                                         | fast · low              |
| `bounded`         | Clear outcome, narrow scope, and a known verification path.                                                                         | fast · medium           |
| `complex`         | Clear goal with substantial implementation, diagnosis, or multi-step reasoning.                                                     | balanced · medium       |
| `ambiguous`       | Bounded discovery to reconcile conflicting evidence or resolve uncertain requirements.                                              | balanced · high         |
| `cross-area`      | Multiple coupled contracts or invariants must be reasoned about together.                                                           | balanced · high         |
| `demanding`       | Deep investigation, unresolved tradeoffs across coupled systems, or architecture decisions whose errors would be costly to reverse. | balanced · high         |
| `high-risk`       | Incident or production responsibility, or work with substantial consequences for users, data, or recoverability.                    | balanced · high         |
| `hyper-high-risk` | An error could cause severe, irreversible harm, such as widespread data loss, and the assignment needs expert judgment.             | deep · high             |

Incident and production assignments start as `high-risk`. Select
`hyper-high-risk` explicitly and record the specific consequence that justifies
the `deep` tier. Retry escalation stays within `fast` and `balanced`. For missing acceptance,
dependencies, or authority, route a bounded assessment or keep implementation
blocked as appropriate. Evaluate coupling and consequences even for small diffs.
Use the class that covers the most demanding part of the assignment. Settings
live in `.factory/direction.json`.

Tiers are provider-neutral. `resources.providers` in `.factory/direction.json` maps
each tier to a concrete model and each effort level to the provider's setting; the
active provider is `resources.provider`, overridden by the `FACTORY_PROVIDER`
environment variable. `dispatch` returns the resolved `provider`, `tier`, `model` and
`reasoningEffort`. A missing mapping yields a resource decision, never a silent fallback.
To add a provider, add an entry with `tiers` (`fast`, `balanced`, `deep`) and `efforts`.
The rubric follows each provider's own model-selection and reasoning-effort guidance.
Evaluate quality, time, and total usage including rework before increasing effort
beyond high.

## Execution and continuation

```sh
pnpm factory claim JOB --actor ROLE --session ID [--used-tokens N --window-tokens N --next-turn-tokens N]
pnpm factory dispatch JOB
pnpm factory context JOB --actor ROLE --token TOKEN --session ID [--used-tokens N --window-tokens N --next-turn-tokens N]
pnpm factory checkpoint JOB --actor ROLE --token TOKEN --summary TEXT --next TEXT --reference PATH
pnpm factory resume JOB --actor ROLE --session NEW_ID [--used-tokens N --window-tokens N --next-turn-tokens N]
```

Pass the dispatched model/effort to the worker exactly, on the host that serves the dispatched provider. Missing model availability
blocks execution. Session identity is required for ownership and independent
evidence; use a stable session label when no host ID is exposed.
Token telemetry is optional: omit all three token flags when unavailable; the record
marks enforcement unavailable rather than inventing usage. When available, report
actual usage plus a proactive reserve to enforce the configured context ceiling.
Checkpoint proactively, and before reaching a measured ceiling; resume in a fresh
session with `fork_turns='none'` and preserve attempts/budgets. Requested time/output limits are cooperative, not spending caps.
Use `renew` for leases, `usage` for observed cost/tokens, and `metrics` for coverage.

## Candidate validation and review

```sh
pnpm factory assess-diff JOB --actor ROLE --token TOKEN --revision SHA
pnpm factory assess-diff JOB --actor ROLE --token TOKEN --revision SHA --review-file PATH
pnpm factory validate JOB --actor ROLE --token TOKEN --revision SHA
pnpm factory evidence JOB --actor ROLE --token TOKEN --type TYPE --revision SHA --reference REPORT --summary TEXT
pnpm factory handoff JOB --actor ROLE --token TOKEN --to ROLE --summary TEXT --next TEXT
```

Freeze the committed candidate while checks execute. `validate` retains individual
results under ignored `.factory/state/evidence/`; failed reports remain available.
Engineering and acceptance produce separate manifests from separate contexts.
Run affected integration/browser checks in addition to required baseline commands.
Source/base changes invalidate matching evidence and assessments.

Review JSON fields: `assessmentFingerprint`, `outcome`, `coupling`, `invariants`,
`groups`, optional `mechanicalPaths`, `requiresSplitDecision` and `decision`.
Each invariant has `id`, `statement`, `status` (`new|preserved`), `paths`, `evidence`
and `dependsOn`. Each ordered group has invariant identifiers and `reasoning`.
Mechanical exclusions have `path` and `reason`. Cover changed handwritten files.
Explain what must be understood together; counts cannot establish simple review.
A triggered keep decision needs `actor: architecture-steward`, a separate `session`,
`reason` and `alternatives`. A split decision blocks handoff until slices exist.

## PR publication

```sh
pnpm factory prepare-pr JOB --actor ROLE --token TOKEN --revision SHA --reference REPORT --body-file PATH --head BRANCH --title TEXT
pnpm factory publish-pr JOB --actor ROLE --token TOKEN --revision SHA --reference REPORT --body-file PATH --head BRANCH --title TEXT
```

Preparation is read-only. Completed implementation work must be pushed and published
as a draft PR unless the user explicitly says not to push or publish. This default
also applies to direct bounded requests. Do not stop at a local commit or prepared
body. Session access restrictions still apply; report blockers. Publication checks remote head/base
and saved-body readback. Bodies need Summary, Evidence, Reviewer path, Invariants
and Merge Danger, issue reference, `Revision: SHA`, `Verification: pending|accepted`
and `Validation: REPORT`. Fixes include Before/After Mermaid diagrams; use
`--pr-kind feature|structural` for a new-flow/dependency diagram. Parsing and saving
are distinct from observed rendering. Accepted status requires independent evidence.

Always give the user the PR link (full URL) when the work ends and whenever they ask.
If no PR exists yet, say so and name the blocker.

### Screenshot evidence

After the browser assertions pass, save a JSON manifest with the full candidate
`revision` and an `images` array. Each entry has a PNG or JPEG `path` relative to
the manifest and descriptive `alt` text. Pass `--screenshots MANIFEST` when recording
implementation evidence with `pnpm factory evidence`. The factory records the
image hashes with the validation reference. Keep the local files through publication.

`prepare-pr` checks the local images without uploading. `publish-pr` stores them
as native GitHub PR attachments using GitHub CLI 2.99.0 or newer and verifies
that the saved Evidence section contains every expected image. On drafts with managed
screenshots, publication preserves the saved prose and refreshes the evidence block
and candidate metadata. Edit the PR itself to change its prose. Use `--update-ready` when explicitly updating
an existing ready-for-review PR.

### Follow every push through CI

After every push, including repair pushes, record the remote head SHA and inspect
Actions runs and PR checks for that exact revision. Wait for checks to appear and
for queued, pending and running jobs to finish. An empty check list is not success.
Use `gh pr checks NUMBER --watch --interval 10`, `gh run list --commit SHA` and
`gh run view RUN_ID --log-failed` as needed. Recheck the remote head before reporting;
a newer push requires a new watch.

Inspect failed, cancelled, timed-out and action-required jobs. Repair failures within
scope, push and repeat. Never report passing CI while checks are pending or failed.
If access, approval, runner availability or an external service blocks completion,
report the revision, run/check links, outstanding status and next action. Include
the final CI result and revision in the handoff. Draft publication and passing CI
do not authorize merging or deployment.

## Recovery and checks

Use `block` for missing scope/access, `unblock` for an evidenced decision, and
`recover` only after inspecting an expired worker's checkout and external actions.
Held-context recovery also needs checkpoint summary/next/reference. Completion
requires same-revision implementation, acceptance, review, release and production
evidence. A draft PR does not complete a production job.

`pnpm test:factory` exercises routing, gates and persistence. `pnpm lint` checks
source and scripts. Specs belong in GitHub Issues, change explanations in PRs.
Only authorized `publish-pr` writes GitHub; no command merges or deploys. Runtime
records coordinate work; they do not authenticate identity or grant permissions.
For deployment use the project's environment runbook.

## Local PR description check

Run `pnpm hooks:install` once per checkout to enable the tracked pre-push hook.
It validates the current branch's open PR description using the same validator as
CI and blocks pushes when validation or GitHub access fails. Branches without an
open PR are skipped. Other refs pushed from this checkout still require CI checks.
Run `pnpm check:pr-body` manually, or `pnpm check:pr-body PATH` to validate a prepared
body file before creating a PR. GitHub lookup requires an authenticated `gh` CLI.

This runs before pushing, because the required full `Revision:` SHA exists only
after committing. Update the description's revision after each new commit before
pushing. Validation includes sections, evidence fields and Mermaid parsing.

On failure, the command prints agent next steps with the actual candidate SHA:
repair the reported error, validate a prepared body, update the PR, verify the saved
description and retry the push. An agent running the push can read these steps in
the command output. The hook does not start an agent or automatically edit GitHub.

## Focused testing

Test policy lives in `delivery.testing` in `.factory/direction.json`.
Use `pnpm --filter PACKAGE test PATH -t "test name"` during a fix, then run
that complete file. `pnpm test:affected [BASE]` runs changed workspace packages
and downstream consumers against the merge base (default `origin/main`). It
includes working-tree changes and untracked files. Root/tooling changes or an
unknown package fall back to the full suite; missing Git bases fail closed.
This command does not replace database/browser checks or formal validation.
Required checks and independent acceptance remain unchanged.

Markdown-only changes run Prettier checks on existing changed documents. Agent
instructions (`AGENTS.md`, `CLAUDE.md`, `.agents/`, `.claude/skills`, `.codex/`) and
`docs/factory.md` additionally run factory tests. Deleted documents are excluded
from formatting. Markdown under source, test or fixture directories retains
application checks because it may be an executable input. Mixed changes retain
all checks selected for code. These shortcuts apply to `test:affected`, not CI or
formal validation.

When every changed file belongs to the factory, CI keeps the required check active
and runs lint and factory tests. Local `test:affected` runs factory tests and
checks the formatting of changed documentation. Mixed changes, workflow edits,
empty diffs, and unavailable comparison bases do not qualify for the CI shortcut.
