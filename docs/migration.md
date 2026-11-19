# Migration and rollback design

Status: planned procedure; no cutover has occurred.

## Before cutover

Capture the pinned source revision, file/import inventory, baseline reports, serialized state versions, evidence references and active job/lease inventory. Inspect external actions and each worker checkout. Archive state and evidence together with a checksummed manifest and restricted permissions; preserve existing references. Keep a recoverable source checkout and immutable old factory ref.

Rehearse migration into a fresh isolated namespace without importing live coordinator ownership. Retain job IDs, ownership history, attempts, checkpoints and evidence identities. Preserve legacy reports as historical evidence; missing factory/policy fields must not be fabricated or retroactively treated as new accepted evidence. Require new validation where compatibility cannot be established.

## Single-coordinator cutover

1. Obtain explicit owner authorization for the concrete cutover target and rollback plan.
2. Quiesce the old coordinator and workers; verify active leases/actions and snapshot again.
3. Acquire a migration lock and fence old writers. Migrate via temporary files and atomic commit with versioned journal.
4. Point the project's pinned launcher to the reviewed factory SHA. Verify project identity, namespace, checks and state compatibility.
5. Run parity, recovery and read-only PR preparation checks before enabling dispatch.
6. Remove old generic engine/shared skills only after integration verification passes. Preserve project skills and application CI.

## Rollback

Stop and fence the new coordinator first. Preserve new records and external-action history. If no incompatible writes or external actions occurred, restore the verified snapshot and old pin, validate ownership and explicitly resume one coordinator. Otherwise reconcile job/event histories and external effects before resuming; never overwrite new facts with a blind snapshot restore. Unsupported state downgrade blocks startup with recovery instructions.

Failure tests must cover interrupted migration, lock contention, stale writer after rollback, missing evidence and changed state schema. Backups and runtime state are not committed to this public repository.
