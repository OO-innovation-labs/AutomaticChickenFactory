# Operations and release design

## Permissions and evidence

Configuration is never an authorization source. Preflight verifies repository access and required services without leaking credentials. Production access requires an explicit target/action in the session. The factory must preserve read-only preparation and distinguish publication, merge, release and deployed verification.

## Recovery cookbook requirements

| Symptom | Required response |
| --- | --- |
| Missing config/tool/base | Field-specific error and remedy; keep dispatch blocked |
| Fetch failed | Report freshness unknown; retry safely and retain selected checkout |
| Lease expired | Inspect workspace and external actions before recovery; fence old writer |
| Context unavailable/exhausted | Persist checkpoint and evidence pointers; resume with preserved budget/history |
| Candidate/base moved | Invalidate matching assessment/evidence; freeze and revalidate |
| CI missing/pending/failed | Observe exact SHA; empty checks are unresolved; repair or report blocker |
| State incompatible | Refuse mutation; restore compatible pin or perform reviewed migration |
| Provider partial write | Reconcile remote identity and saved result before retry; use idempotency |

Before the first implementation release, replace proposed command shapes in the onboarding guide with verified help output and a fixture command cookbook. Documents must describe prerequisites, output/report locations, safe retries and terminal success for each stage.

## Versioning and release process

Use semantic versions for runtime compatibility; record immutable commit SHAs even when a tag is supplied. A specification tag must be clearly labeled as documentation only. Factory CI covers core tests, adapter conformance, configuration failures and both consumer fixtures. Publish release notes with supported schema/state majors, migration/rollback instructions and known limitations. Release owners verify the frozen commit, independent acceptance and required CI before an authorized runtime release.

## Upgrade procedure

Read compatibility notes, snapshot state/evidence, stop the current coordinator, validate the new ref against isolated fixtures and migrate only when required. Update the consumer pin through a reviewed change. Keep the old pin and snapshot until rollback has been rehearsed and the observation window ends. Record factory/project/base revisions in all subsequent evidence.

## Contribution rules

Project business rules and environment runbooks belong with the project. Shared orchestration, generic roles and provider semantics belong here. Every factory change names affected invariants, failure cases and downstream consumers; behavior changes require focused regression and integration tests. Broader state/configuration changes require the full compatibility matrix. Changes to a frozen candidate invalidate prior acceptance.
