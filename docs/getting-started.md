# Onboarding plan

The engine is not available in this repository yet. The steps and command shape below specify the onboarding experience that M3–M7 must implement and verify.

1. Choose an existing repository or initialize a greenfield repository with a real base commit and remote. Record canonical repository identity and its actual default branch.
2. Install the factory runtime prerequisites and Git/GitHub tooling. Clone a reviewed immutable factory ref in a separate directory. Record the resolved factory SHA.
3. Add `.factory/project.json` using the [minimal](../examples/minimal.project.json) or [advanced](../examples/advanced.project.json) example. Replace illustrative identities and the zero SHA with the real repository and factory revision.
4. Configure language/toolchain probes, install/check commands, areas and specialist ownership. Keep business skills, glossary, ADRs and environment runbooks in the project.
5. Configure provider access through environment/credential stores. Start with read-only access; confirm write permission only for authorized publication. Keep secrets outside tracked files.
6. Select the durable project namespace and verify no other coordinator owns it. Run configuration validation and preflight from outside the project directory.
7. Import one bounded ready issue, inspect dependencies and acceptance, assign checkout/base/integration owner, dispatch the inherited specialist contract and claim a lease.
8. Implement, checkpoint and freeze a candidate. Run required checks and independent acceptance/review using distinct contexts and manifests. Prepare a PR without writes.
9. If publication is authorized, publish a draft, verify the saved description and watch CI for that exact remote revision. Request separate authorization for any merge or environment action.

Proposed invocation:

```sh
node /path/to/pinned-factory/bin/factory.mjs --project /path/to/project preflight
```

The exact CLI entry point is to be finalized in M2. The complete cookbook must include intake/sync, board, contract, workspace, claim, dispatch, checkpoint/resume, validate, assess-diff, handoff, prepare-pr and recover with runnable fixture examples before release.

## Extending a connected project

Add a role inheriting `engineer`, place its skill under the project's local skills directory, and map an area to that role. Add local check argv entries for its acceptance requirements. Configuration validation must confirm inheritance and ownership before dispatch. A different toolchain or base branch must be configured here rather than patched into the engine. Changes to state transitions or generic evidence gates instead require a factory PR and adapter/fixture compatibility tests.
