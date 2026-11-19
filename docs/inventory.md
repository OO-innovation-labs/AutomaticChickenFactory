# Source inventory and baseline

Inspected source: `OO-innovation-labs/OOlivetranslator` at `7b53a559cf5417d4a2f320e8ef1f7483a32891bb` on 2026-11-19. This is an initial inventory, not the complete M0 dependency baseline.

## Couplings confirmed by inspection

| Location | Existing coupling | Extraction requirement |
| --- | --- | --- |
| `scripts/factory-policy.mjs` | Loads config/direction relative to module | Inject validated project context |
| `scripts/factory-cli.mjs` | Defaults jobs to `.factory/state/jobs.json` | Namespace and coordinate durable stores |
| `scripts/factory-preflight.mjs` | `origin/main`, pnpm version, lockfile, local skills | Configurable base/toolchain/knowledge probes |
| `scripts/factory-delivery.mjs` | Project-local evidence directory and imported policy | Explicit evidence root and effective policy |
| `scripts/factory-test-scope.mjs` | Embedded factory file patterns | Separate factory and application CI classification |
| `.factory/config.json` | Generic roles mixed with caption/operator/backend paths | Shared role inheritance plus project specialists |
| `.factory/direction.json` | Generic gates mixed with pnpm checks and model settings | Defaults plus validated project checks/resources |
| `.github/workflows/ci.yml` | Application CI runs embedded factory checks | Independent factory CI plus pinned consumer integration |
| `AGENTS.md`, `docs/factory.md` | Product context and reusable instructions mixed | Thin project pointers and shared factory docs |

## Baseline observations

The source preflight reported readiness false: origin refresh was unavailable in the restricted execution context and application dependencies were not installed. The source contract for `platform-engineer` was retrieved. An initial `node --test scripts/test-factory*.mjs` run failed, including PR tests unable to import `jsdom`. This is not a green baseline or proof of a product defect. M0 must install locked dependencies and rerun the full declared `test:factory` command, including lint and PR-hook tests, then record exact counts/results and environment.

Preserve the existing command families: preflight/contract, sync/board/show/depend/assign/resource/workspace, claim/dispatch/context/checkpoint/resume/renew/usage/metrics, assess-diff/validate/evidence/handoff, prepare-pr/publish-pr, block/unblock/recover/decline/complete. M0 must capture exact help/flags, state schema, import closure, provider calls and representative fixtures.

## Candidate extraction files

- `.agents/skills/factory-build/SKILL.md`
- `.agents/skills/factory-build/references/oolive-caption-ux.md`
- `.agents/skills/factory-direction/SKILL.md`
- `.agents/skills/factory-operate/SKILL.md`
- `.agents/skills/factory-plan/SKILL.md`
- `.agents/skills/factory-route/SKILL.md`
- `.agents/skills/factory-verify/SKILL.md`
- `.factory/config.json`
- `.factory/direction.json`
- `scripts/factory-cli.mjs`
- `scripts/factory-delivery.mjs`
- `scripts/factory-diff.mjs`
- `scripts/factory-policy.mjs`
- `scripts/factory-pr-images.mjs`
- `scripts/factory-pr.mjs`
- `scripts/factory-preflight.mjs`
- `scripts/factory-test-scope.mjs`
- `scripts/factory-validation.mjs`
- `scripts/factory.mjs`
- `scripts/test-factory-ci-browser-scope.mjs`
- `scripts/test-factory-delivery.mjs`
- `scripts/test-factory-diff.mjs`
- `scripts/test-factory-pr.mjs`
- `scripts/test-factory-preflight.mjs`
- `scripts/test-factory-testing-selection.mjs`
- `scripts/test-factory-validation.mjs`
- `scripts/test-factory.mjs`

## Supporting dependencies to inventory before extraction

Inspect `scripts/check-pr-body.mjs`, `scripts/test-affected.mjs`, lint/PR hook scripts, `.githooks/`, PR templates, all workflows and package scripts. Mermaid/jsdom dependencies used by PR validation must be independently declared. Keep `event-production-ui`, caption invariants, `oolive-build-deploy`, glossary and DigitalOcean runbooks with Cepstrum. Inspect persistence locking, atomic writes, evidence hashes and recovery behavior before changing state locations. No live state was migrated or copied into this repository.
