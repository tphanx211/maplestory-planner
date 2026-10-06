---
name: personal-github-account
description: "maplestory-plan is a personal project — use GitHub account tphanx211, never the work account tphan-ambit"
metadata:
  node_type: memory
  type: user
  originSessionId: 9522b3c5-f90d-46d2-811c-c3efe9133ece
  modified: 2026-10-02T07:23:45.660Z
---

The user has two GitHub accounts: **tphan-ambit** (work, the machine-wide default for git and `gh`) and **tphanx211** (personal). This folder is personal and must use tphanx211.

Setup done 2026-10-02 in the repo's `.git/config` (local only, global config left as work), and repeated in the nested repo `classic_launch_strategy/` (its own `git init`, which defaulted to the work email until set):
- user.name "Tony Phan", user.email tonyyhphann@gmail.com
- credential.https://github.com.username = tphanx211 (so Git Credential Manager picks the personal login)

**Why:** keep personal work out of the work account and work email out of personal commits.

**How to apply:** before any `gh` command here (repo create, PR, etc.), check `gh auth status`. `gh` has one active account for the whole machine and defaults to tphan-ambit, so switch to tphanx211 first and switch back afterwards. Never edit the global ~/.gitconfig identity.
