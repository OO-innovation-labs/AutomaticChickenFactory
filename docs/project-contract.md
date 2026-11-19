# Proposed project contract v1

This is a design contract. A runtime JSON Schema and configuration loader are deliverables of milestone M3; example checks today do not replace that validator.

## Resolution and precedence

1. Factory safety invariants are mandatory and immutable from project configuration.
2. Release defaults supply generic roles, resource limits and baseline policies.
3. Project definitions add areas, specialists, local checks and approved adapters.
4. Explicit invocation options select project/workspace/base and may tighten limits; they cannot weaken gates or grant authority.

Reject unknown keys and unsupported major versions. Merge named maps by identifier; reject duplicate/conflicting definitions. Command/check arrays replace by named entry only through explicit policy, never positional merging. Reject removal of required factory checks, self-acceptance, evidence bypass, enlarged authority or lock disabling. Show effective values, provenance and a policy digest before dispatch.

## Fields

| Field | Contract |
| --- | --- |
| `schemaVersion` | Integer 1; future incompatible versions fail before state mutation |
| `projectId` | Stable nonempty namespace identifier; renames require explicit migration |
| `repository` | Provider plus canonical owner/name identity; checked against selected checkout |
| `base` | Remote and branch, independently configurable; no implicit `main` |
| `factory` | Source repository and immutable revision; resolve and record actual SHA |
| `toolchain` | Prerequisite executable/version probes and optional install command |
| `areas` | Named routing patterns, project-relative paths and one owner role |
| `roles` | Local role inherits a generic role, adds mission, skills and bounded ownership |
| `checks` | Unique names, argv arrays, phase, required flag and optional service prerequisites |
| `knowledge` | Project-relative glossary, ADR, skills and runbook paths |
| `adapters` | Named versioned Git/issue/CI/release interfaces and non-secret configuration |

Commands use argv arrays, an explicit cwd and bounded output/time handling. Credentials are referenced by environment/provider names, never stored in tracked JSON. Normalize paths and reject escape outside the declared roots. Validate owners, inheritance cycles, role handoffs, executable availability and required knowledge paths before dispatch. Errors must name the field, invalid value and corrective action without exposing secrets.

## Extensions

| Addition | Project-local extension | Factory change |
| --- | --- | --- |
| Specialist | Inherit `engineer`, add domain skill and paths | Change generic role/evidence semantics |
| Area | Map source paths/patterns to a known role | Change routing algorithm or ambiguity handling |
| Workflow | Compose existing guarded stages | Add stage/state transitions or recovery semantics |
| Gate | Add stricter project validation | Change shared required gate enforcement |
| Adapter/provider | Select installed compatible adapter and config | Implement versioned adapter behavior and conformance tests |

Adapter contracts must define inputs, outputs, errors, retries, idempotency and read/write classification. Git exposes identity/base/candidate checks; issue providers expose intake/dependencies; CI exposes exact-revision runs and terminal outcomes; release adapters expose artifact identity, authorized action and rollback references. Capability absence blocks the affected stage. Secrets and external writes remain controlled by session authority.

## Compatibility

Factory releases declare supported project and state schema majors. Additive minor changes retain defaults; removals and changed meaning require a major version and migration guide. Pin immutable refs and upgrade one project/coordinator at a time after fixture compatibility checks. See [migration](migration.md).
