# Claude context for this project

Copies of what Claude Code keeps outside the repo on the original PC, so a session on another machine has the same background. `CLAUDE.md` in the repo root loads automatically; these files are the detail behind it.

## memory/

Claude's memory notes for this project (snapshot from Oct 6, 2026). The live copies on the original PC are in `C:\Users\TonyH\.claude\projects\C--Users-TonyH-maplestory-plan\memory\`.

To use them on another PC, copy the files into that PC's project memory folder: `~/.claude/projects/<project-slug>/memory/`. The slug is the clone's full path with `:` and `\` replaced by `-` (for example `C--Users-<you>-maplestory-plan`). Open a Claude Code session in the clone once first so the folder exists.

These are snapshots: the live notes on the original PC keep changing, so re-copy them when you push if you want the desktop to stay current.

## scheduled-tasks/

The prompts of the four updater tasks (daily 2:30 PM and 9 PM CT, plus one-offs on Oct 6 and Oct 21). Each task's prompt contains absolute paths for the original PC (`C:\Users\TonyH\maplestory-plan\...`).

**Run these on one machine only.** Two machines running the updater would each commit to their own clone and the histories would diverge. If you move the updater to the desktop, disable the tasks on the original PC first, then recreate them in the desktop app with the paths changed.
