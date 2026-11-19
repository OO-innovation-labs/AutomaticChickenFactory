# ADR 0001: Factory home and project boundary

Status: proposed; requires architecture review before implementation cutover.

## Context

Cepstrum embeds reusable factory orchestration together with product-specific ownership, checks and skills. Copying this engine to each consumer would create divergent safety gates and make upgrades difficult.

## Decision proposal

Use `OO-innovation-labs/AutomaticChickenFactory` as the standalone home. Consumers select an immutable factory revision and declare project-local configuration. Explicit project resolution replaces installation-relative project discovery. Safety invariants remain in the factory; project policies can add requirements but cannot weaken those gates. The precedence and extension rules are specified in [the project contract](../project-contract.md).

## Alternatives

- Keep everything in Cepstrum: low initial migration cost, continued application/toolchain coupling.
- Copy the engine per project: simple bootstrap, divergent orchestration and duplicated maintenance.
- Standalone versioned home: explicit compatibility and migration work, one maintained engine and independently testable consumers.

## Consequences

The factory needs its own CI, schema/version policy, fixtures and adapter contracts. Cepstrum needs a pinned launcher and migration rehearsal. Runtime state must stay project-namespaced and outside the installation. Publication of this ADR is a reviewable proposal, not authorization for irreversible cutover.
