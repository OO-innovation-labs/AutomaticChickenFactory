# AutomaticChickenFactory

Specification and roadmap for a reusable, evidence-driven software factory.

**Status: specification only.** The factory engine has not been extracted or released. Examples and commands describe the proposed contract; they are not executable installation instructions today.

Origin: [OOlivetranslator issue #208](https://github.com/OO-innovation-labs/OOlivetranslator/issues/208). The initial consumer is Cepstrum; the factory must also support unrelated projects without copying engine files or changing shared source.

## Read the specification

- [Requirements and acceptance](docs/specification.md)
- [Architecture and boundaries](docs/architecture.md)
- [Project extension contract](docs/project-contract.md)
- [Implementation roadmap](docs/roadmap.md)
- [Onboarding plan](docs/getting-started.md)
- [Migration and recovery](docs/migration.md)
- [Operations and release design](docs/operations.md)
- [Source inventory](docs/inventory.md)
- [Repository and precedence decision](docs/adr/0001-factory-home-and-project-boundary.md)

## Review this repository

Run `python3 scripts/check-specs.py` to check local document links and example structure. CI runs the same check. This validates the specification artifacts, not factory functionality.

Contributions should identify the requirement and acceptance scenario they affect. Implementation begins with the baseline milestone in the roadmap. This publication does not mark issue #208 complete or authorize application merges, production changes, or migration cutover.
