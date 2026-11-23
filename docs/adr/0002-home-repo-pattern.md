# ADR 0002: Factory repository as Home Repo

Status: proposed; refines [ADR 0001](0001-factory-home-and-project-boundary.md).

## Context

Factory sessions currently start inside a product repo, so skills, instructions and engine are copied or embedded there. The [Home Repo pattern](https://aihero.dev/the-home-repo-pattern) keeps shared skills, `AGENTS.md` and docs in one repo, runs agents from it, and points to code repos by path.

## Decision proposal

Adopt a hybrid. AutomaticChickenFactory is the Home Repo and also the versioned engine home from ADR 0001. Shared `factory-*` skills live in `skills/` (one copy). `AGENTS.md` lists consumer repos under "Other Repos" with local path, remote and a read-first hint. Consumers keep `.factory/project.json`, glossary, ADRs and product skills, and are not submodules.

## Consequences

- Skills are copied here first; the copies in OOlivetranslator stay until engine extraction reaches parity (roadmap M2/M7), then are replaced by pointers. Until then they can drift; changes go to both.
- Skills still reference `pnpm factory` and project files; they become generic as the engine and contract land (M2–M3).
- Sessions run from this repo operate on product repos through worktrees; checkout rules in `skills/factory-manager` apply to the target repo.
