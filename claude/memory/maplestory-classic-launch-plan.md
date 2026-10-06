---
name: maplestory-classic-launch-plan
description: "Project goal, timeline, and where the spec lives for the MapleStory Classic World launch plan"
metadata:
  node_type: memory
  type: project
  originSessionId: 5ec692d5-1d7b-495c-b174-f1e7f285b1bb
  modified: 2026-10-02T18:53:37.596Z
---

User is building a launch plan for MapleStory Classic World: Founder's Access Oct 6–20, 2026; free-to-play Grand Launch Oct 21, 2026. Founder's Access characters, mesos, and items carry into launch (confirmed 2026-10-02 via MassivelyOP and meowdb). Plan shape: a farming character built during Founder's Access that becomes a bank and solo farmer, a second character (Assassin is a hypothesis) leveled with friends from Oct 21, and manual Free Market trading.

The agreed spec is `kickoff_prompt.md` in the project root; outputs go in `classic_launch_strategy/`. The user filled in "About me" on 2026-10-02 (recorded in the spec): NA, US Central; 4h weekdays / 8h weekends both before and after Oct 21; Zakum Founder's Package; Cash Shop spend "whatever pays off"; 1–2 friends with classes undecided; dashboard on a second monitor (phone later); balanced market risk.

Status 2026-10-02: Phases 1–5 done (plan files, dashboard, scheduled updater, phone artifact; see [[mscw-updater-ops]]). The user's price log on the phone copy can be read directly with ArtifactData instead of asking for exports.

**v0.6.0 (2026-10-02, commit 1cf3ad5): the user overrode the plan's Fighter pick and chose an I/L Wizard farmer + Assassin launch character** (Hunter retired; tripwire: revisit only if both friends pick single-target classes). Don't relitigate it. A review that same day (`review/REVIEW_2026-10-02.md` in the parent folder) found the user's reasons "mages never miss" and "vertical maps avoid congestion" false in Classic data, "15k–45k vendor equips" wrong (typical 3–9k), and the Lv 48–65 advantage real only if Thunder Bolt hits most of 6 targets and the cap is ≥60. The user said not to apply review fixes beyond the class switch until they decide; the report lists those as Open.

**Why:** the user wanted research held to Classic World data, not legacy or private-server assumptions, and accepted a review that added source tiers ([V] verified / [B] legacy baseline / [?] unknown), no invented market prices, and a research checkpoint before building.

**How to apply:** read `kickoff_prompt.md` before changing the plan. Keep the source tiers, never fabricate prices, and keep tactics within the Terms of Service (no macros or bots). See [[windows-tool-gotchas]] for environment quirks.
