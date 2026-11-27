# Working without the engine

Use this for a project whose `package.json` has no `factory` script. Skills name engine
commands; do the manual equivalent here, and record its result in the issue or PR. The
safety rules, independence between builder and verifier, and authorization limits are
unchanged. State in handoffs that the check was manual.

| Engine command | Manual equivalent |
| --- | --- |
| `preflight` | The checks in the project's `PREFLIGHT.md`; create it per `factory-manager` step 1 when missing |
| `contract` | The assigned role's skill plus the project's `AGENTS.md` |
| `sync`, `board`, `show` | `gh issue list` and `gh issue view --comments`, read fresh |
| `depend` | Native GitHub issue dependencies |
| `assign`, `resource` | Name the role, model and effort in the brief |
| `workspace` | A worktree and branch per change |
| `claim`, `decline` | Issue comment naming the owning session, or why it was declined |
| `dispatch`, `context` | A brief from the issue: scope, base SHA, checks, authority, done-when |
| `checkpoint`, `resume` | A commit, plus a comment with its SHA and the next action |
| `validate` | Every root check from a fresh clone of the full SHA, with commands and results recorded |
| `assess-diff` | `git diff --stat BASE...HEAD` plus a written split-or-keep decision |
| `evidence`, `handoff` | Verdict, full SHA, checks run, gaps, next owner and action |
| `prepare-pr`, `publish-pr` | Draft body in a file, then `gh pr create --draft --body-file`; read it back |
| `help` | This table |

`docs/factory.md` means this document. For `.factory/config.json` and
`.factory/direction.json`, use the project's `AGENTS.md`, README commands and the user's
stated limits.
