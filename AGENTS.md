# AutomaticChickenFactory — Home Repo

This repository is the Home Repo for the factory: run factory sessions from here,
not from inside a product repo. It holds the shared factory skills, the factory
specification and (once extracted) the engine. Product repos keep their own code,
history, issues, glossary, ADRs and product skills.

## Working from here

Start with `skills/factory-manager/SKILL.md`; it routes the request. Load the
assigned role's skill only. The specification lives in `docs/`; read
`docs/project-contract.md` before changing what a project may configure.
`docs/factory-commands.md` documents the current command surface, which still runs
from the product checkout until engine extraction (roadmap M2).
Factory configuration never expands session authorization or grants production access.

## Other Repos

- OOlivetranslator (OOlive Live and Studio product, first factory consumer; also referred to as Cepstrum in the specification): ~/Documents/Repos/OOlivetranslator. Clone from https://github.com/OO-innovation-labs/OOlivetranslator if missing. Read its AGENTS.md before changing it. Work in a worktree per change; its `.factory/` config, glossary, ADRs, `event-production-ui` and `oolive-build-deploy` stay there.

## Rules

- One copy of each shared skill, here. Product-specific skills stay in the product repo.
- Safety invariants live in the factory; projects can add requirements, never weaken them (ADR 0002 and the project contract).
- Never push, merge or deploy without the user's explicit request.
