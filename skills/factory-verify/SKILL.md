---
name: factory-verify
description: Independently verify acceptance, review a candidate, coordinate an authorized release, and confirm deployed behavior.
---

# Factory Verify

Use the assigned contract in dispatch; if absent, use this skill and the project's `AGENTS.md`.
Read issue acceptance and candidate full SHA.
Use a separate context from implementation; verify source/artifact identity and
run your own checks. Record missing independence rather than inventing sign-off.
Use the evidence and publication commands in `docs/factory.md`.

Acceptance: compare the candidate with the customer's intended product outcome and
explicit constraints, using the recorded assumptions and representative cases beyond
their examples. Report unresolved scope assumptions rather than treating a mechanism
or example-specific passing test as product acceptance. Exercise criteria and material
failure/retry cases; distinguish mocks
from provider/production observations. Record a separate validation manifest and
return failures with reproduction, impact and revision; pass to code review.

On a new revision, rerun every required check on its exact SHA. Scope repeated manual
probes to the change and the regressions it can reach, and say which earlier revision
each reused result covers; a change to shared state repeats all probes. After three rounds on one candidate, hand the open findings and probe scripts to
a fresh verifier and report the count to the manager, who reconsiders the split.

Review: inspect the complete diff, scope, invariant groups, cross-group assumptions,
safe split alternatives and diagram accuracy. Small file counts do not prove a
simple review. Keep-together exceptions need a separate architecture decision.
Read the branch commit by commit as well as whole: return a commit that mixes ideas,
or a commit that serves no acceptance criterion, as a split finding.
Record actionable findings or revision-bound review evidence.

Release: confirm matching acceptance/review, artifact identity, migration and rollback
readiness. Use the project's build/deploy skill and the target runbook; execute only the authorized
action. Production verification checks serving identity, health and acceptance.
Complete only with matching implementation, quality, release and production evidence.
Preparation, saved descriptions and parsed diagrams are distinct from deployed or
visually observed behavior.

Apply `delivery.testing` in `.factory/direction.json` for test selection, evidence
reuse and escalation. During iteration use focused files or `pnpm test:affected`;
formal `validate` still runs every required check on the frozen candidate.
