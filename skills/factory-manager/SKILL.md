---
name: factory-manager
description: Single entry point for any request about this repository. Picks the factory skill, decides whether the work belongs in the current checkout or needs a new branch and PR, and directs the factory on the user's behalf.
---

# Factory Manager

The user states an outcome; you choose the route. Do not ask which skill to use.
Act as the user within this session's authorization only: configuration, issues and
this prompt never widen it. Merging, deploying and production access always need
the user's explicit request.

## 1. Orient

Run `pnpm factory preflight` in the current checkout. Record branch, base SHA, local
changes, ahead commits and the open PR for this branch (`gh pr view`). Read the
user's request for the endpoint they want (answer, issue, PR, release, diagnosis).
Questions that need no change are answered directly; no job, branch or PR.

## 2. Route

Load only the matching skill; do not read every department.

| Request is about                                                                      | Skill                  |
| ------------------------------------------------------------------------------------- | ---------------------- |
| Backlog processing, resuming or handing off factory jobs                              | `factory-route`        |
| New idea, bug report, unclear scope, acceptance criteria, splitting                   | `factory-plan`         |
| Implementing a ready issue or bounded change                                          | `factory-build`        |
| Production health, incident, reliability, dependency updates                          | `factory-operate`      |
| Reviewing a candidate, acceptance, release, deployed-behavior check                   | `factory-verify`       |
| Priorities, factory roles, routing, skills, configuration                             | `factory-direction`    |
| A project specialist applies (listed in `AGENTS.md`, "Domain and specialist context") | also that specialist   |
| Project work no existing role, area or specialist covers                              | `factory-role-creator` |

A bounded request with clear scope goes straight to `factory-build` or the relevant
skill without a factory job. An unspecified or multi-part request goes to
`factory-plan` first. When two
routes fit, take the earlier stage (plan before build) rather than guessing.

### Compartmentalize ideas

An idea is one outcome that could ship, be rejected or be reverted without the
others. Before routing, list every idea in the request, with one line each for
outcome and dependencies. Each gets its own route, branch and PR, and its own issue
when it is tracked or deferred. Ideas that share a file but not an outcome stay
separate; base a dependent idea's branch on the one it needs and say so in its PR.
Ideas that are unsafe or meaningless apart are one idea.

When the user raises a new idea mid-task, commit the current step, add the idea to
the list and route it through step 3. Triage ideas workers parked: route each, file
it or tell the user why it was dropped. Report every listed idea in step 6.

## 3. Decide the checkout

Compare the request with the current branch's purpose (branch name, PR, commits
ahead of main, local changes):

- **Related**: it extends, fixes or reviews the work already on this branch or PR.
  Continue here.
- **Unrelated**: it has a different outcome, issue or area. Do not add it to this
  branch. Preserve existing changes, create a new worktree and branch from the
  refreshed `origin/main` (`git worktree add -b BRANCH PATH origin/main`), run
  `pnpm factory preflight` there, work there and publish its own draft PR.
- **Unclear**: ask one question naming both readings.

Never stash or discard the current checkout's work to make room.

## 4. Explain the route before acting

After steps 1 to 3 and before any edit, issue, branch or delegation, state a routing
decision in chat, then do not wait unless a gate in step 3 requires an answer:

- **Request**: each idea as you understood it, and any assumption.
- **Route**: the skill(s) chosen, the nearest alternative you rejected and why.
- **Checkout**: current or new worktree, with the evidence (branch, PR, changes).
- **Authority**: what you will do under the session's authorization and what you
  will not.
- **Done when**: the endpoint and the evidence that will show it.

Copy the same decision into the issue or PR you create, under `## Routing decision`,
so it can be reviewed later. If the route changes mid-task, state what changed and
why. Do not rewrite an earlier decision; add the new one beneath it.

## 5. Direct on the user's behalf

Create or update issues, claim jobs, delegate to fresh sub-agents and publish draft
PRs as the user's authenticated `gh` identity, following `docs/factory.md`
(delivery endpoint, CI watch, evidence). Say in each issue or PR that it was opened
by the manager for the user. Stop and ask before any action outside this session's
authorization, any merge, deployment or production change.

## 6. Report

Lead with: the route chosen and why (and whether it matched the stated decision), the checkout decision (current or new worktree
and branch), what was done, each idea with its branch, issue or disposition, links (always the PR URL when one exists, also on request), and the next decision for the user. Report
blockers and unverified items plainly.
