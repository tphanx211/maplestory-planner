# MapleStory Classic World launch plan

Personal planning project for MapleStory Classic World (Nexon): Founder's Access Oct 6–20, 2026; free-to-play Grand Launch Oct 21, 2026. The user plays an **Ice/Lightning Wizard** as the farmer, bank and Free Market merchant, and an **Assassin** with 1–2 friends from Oct 21. These are the user's decisions (Oct 2, 2026); don't relitigate them. Report risks and let the user decide.

## Layout

- `kickoff_prompt.md`: the agreed spec, including "About me" (hours, budget, region). Read it before changing the plan.
- `classic_launch_strategy/`: the plan.
  - `00`–`05` markdown files hold the reasoning; `data/plan_data.js` (`window.PLAN_DATA`) holds the dashboard data. Keep them consistent.
  - `index.html`: the offline dashboard. Open it by double-clicking; no server needed.
  - `calc/il_projection.py`: the I/L projection. The Fighter scripts are kept only as a comparison baseline.
  - `updater/`: rules, sources, state and validator for the scheduled updater. `tools/`: phone-artifact build and allowlist writer.
- `review/REVIEW_2026-10-02.md` and `review_prompt.md`: the Oct 2 review. Findings marked Open are waiting on the user.
- `claude/`: copies of Claude's memory notes and the scheduled-task prompts (see `claude/README.md`).
- `.claude/settings.json` (here and in `classic_launch_strategy/`): permission allowlists for the updater.

## Ground rules

- Tag every fact: **[V-off]** official Nexon, **[V-dm]** COT2 datamine, **[V-cbt]** test reports, **[model]**, **[calc]** with inputs shown, **[B]** legacy pre-Big Bang GMS, **[?]** unknown (and add it to `05_launch_day_verification.md`).
- No private-server sources (MapleLegends, MapleRoyals, MapleSaga, Artale) and no gold-seller or SEO sites.
- Never invent market prices. Rules are relative to prices the user logs, or to NPC prices.
- Stay within the Terms of Service: manual play only, no macros, bots, anti-idle tools or real-money trading. One account = one character online.
- Run `python classic_launch_strategy/updater/validate_plan_data.py` after editing `plan_data.js`.
- Reading Nexon news: use `https://g.nexonstatic.com/maplestory/cms/v1/news` and `.../news/{id}`; the web pages render empty. meowdb.com started blocking automated requests (Cloudflare 403) on Oct 6.

## Operations

- **Phone copy:** private artifact https://claude.ai/artifact/WGdkJ7HCh93qLxcYKU4Zrk. It doesn't update itself: after plan changes, run `python classic_launch_strategy/tools/build_artifact.py <out.html>` and republish it with `data/plan_data.js` as a supporting file.
- **Scheduled updater:** four tasks in the desktop app on the original PC (prompts in `claude/scheduled-tasks/`). They commit with `git add -A`, which stages the whole repo, including uncommitted edits. Run them on **one machine only**, and don't edit while a run is due (about 2:39 PM and 9:07 PM CT).
- **Git:** one repo, `tphanx211/maplestory-planner` (personal account, private). `git push` is denied in the project settings on purpose; the user pushes by hand. Use the personal account `tphanx211` for anything GitHub-related here, never the work account.
- **Windows:** use `python` (`python3` opens the Microsoft Store). In PowerShell, `curl` is an alias; use `curl.exe` or Git Bash.
