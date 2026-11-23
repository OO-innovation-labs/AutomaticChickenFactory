---
name: factory-operate
description: Assess production health or incidents, plan reliability maintenance, and evaluate dependency updates for the running product.
---

# Factory Operate

Read the assigned operations role contract and production evidence relevant to the reported environment. Inspect deployment identity and configured health signals read-only. Use the target's runbook; historical Azure records do not establish the current production topology.

Health watcher: compare timestamped health/readiness, errors and available caption-delivery signals with prior evidence. Notify only on actionable change, completion, failure or required user action. If credentials, monitoring endpoints or access are missing, report the gap; do not claim continuous monitoring is installed.

Incident responder: record impact, affected workflows, first/last observations, current release, timeline and accountable owner. Explicitly route the incident lane through the coordinator. Contain or recover only within already delegated production authority; otherwise prepare a concrete target/action and request that decision. Delegate repairs to the area engineer while retaining incident coordination. Separate restored service from permanent correction. Recovery without code requires health evidence; code changes follow independent verification and release.

Reliability maintainer: convert repeated incidents into bounded preventative issues with measurable acceptance. Dependency maintainer: inspect manifests, lockfiles and primary advisories; explain exposure and compatibility before proposing upgrades. Route implementation to the owning engineer rather than maintaining a second code ownership system.

For deployment or rollback use `oolive-build-deploy`, `docs/digitalocean-deployment.md` and `docs/database-rollback.md` as relevant. Preserve migration compatibility and recovery artifacts. Record identity, evidence, action taken, current impact and next update condition. Never include credentials in evidence. Incident updates stay in the work record; external messages require session authorization.
