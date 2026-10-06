---
name: mscw-updater-ops
description: "How the Classic World plan's scheduled updater, allowlists, and phone dashboard copy are wired, and their known blockers"
metadata:
  node_type: memory
  type: project
  originSessionId: 95523bc9-8083-4f68-a97d-391bd20fc11d
  modified: 2026-10-06T19:19:57.252Z
---

Set up 2026-10-02 (Phase 5 of [[maplestory-classic-launch-plan]]):

- Scheduled tasks (desktop app): `mscw-plan-updater` (daily 2:30 PM CT), `mscw-plan-updater-evening` (daily 9 PM CT), one-offs `mscw-updater-founders-access-open` (2026-10-06 1:30 PM CT) and `mscw-updater-grand-launch` (2026-10-21 1:30 PM CT). All follow `classic_launch_strategy/updater/UPDATER_RULES.md`.
- Scheduled runs start with cwd = the PARENT folder (`maplestory-plan`), not `classic_launch_strategy`, so their prompts use `git -C <abs path>` and an absolute validator path. The rules file still shows short forms because it couldn't be edited (next point).
- `tools/write_allowlists.py` writes the same allowlist to both `maplestory-plan/.claude/settings.json` and `classic_launch_strategy/.claude/settings.json`. Its deny rules also block Claude's own Edit/Write on `index.html`, `updater/UPDATER_RULES.md`, `updater/validate_plan_data.py`, `tools/**`, `.claude/**`. The user was asked whether to drop those file denies; until they answer, don't work around them via Bash.
- `update_now.bat` was built and removed (commit d9f9d5e): the standalone `claude` CLI's OAuth session was expired and the folder wasn't trusted for the CLI. Restore with `git revert d9f9d5e` once the user logs in and trusts the folder, then re-test.
- 2026-10-06: **one repo now.** The nested `classic_launch_strategy` repo was folded into the parent repo (GitHub `tphanx211/maplestory-planner`, history kept; merge commit a37ed2c). The old nested `.git` is backed up at `C:\Users\TonyH\maplestory-plan-classic-git-backup`. The updater's `git -C .../classic_launch_strategy` commands now act on the parent repo, so its `add -A` stages the WHOLE repo (review/, claude/, CLAUDE.md too). `git push` is still denied; the user pushes by hand. Only one machine should run the scheduled tasks.
- 2026-10-02: the user removed the `index.html` deny lines from BOTH settings files (the parent's are separate from the inner one, and both apply). The inner file's change was uncommitted at the time. `write_allowlists.py` still writes them back if run.
- Scheduled runs use auto permission mode (user-level defaultMode), and their `git add -A` sweeps any uncommitted edits. Rebuild big changes in scratch and copy them in plus commit in one step, away from the ~2:39 PM / ~9:07 PM CT runs.
- Phone copy: private artifact https://claude.ai/artifact/WGdkJ7HCh93qLxcYKU4Zrk built by `python tools/build_artifact.py <out.html>` and published with `data/plan_data.js` as a supporting file. It doesn't auto-update; republish to the same URL after plan changes. Prices/checks/notes sync to its owner-only db (`prices/*`, `mscw/state`), which Claude can read with ArtifactData.

**Why:** these are not obvious from the repo and each one caused a failure or detour on setup day.
**How to apply:** check these before debugging an updater run, the dashboard sync, or a permission denial in this project.
