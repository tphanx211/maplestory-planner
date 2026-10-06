# Changelog

Newest first. The updater adds an entry for every run that changes content, with source URLs. `data/plan_data.js` → `changelog` mirrors these entries so the dashboard's Updates tab can show them.

## 0.6.2 · 2026-10-06 · Founder's Access Cash Shop prices published
- **Pets: 3,500 NX, 30 days** [V-off]. All pet skills (Auto HP/MP Potion, Auto Move, Expanded Auto Move) come only in the **Pet Booster Essentials Pack, 9,900 NX, once per account** (permanent; includes 30 pet food coupons).
- **Convenience Essentials Pack, 9,900 NX, once per account:** AP Reset, SP Reset, Selective 5-slot Coupon, Safety Charm ×10, Super Megaphone ×10.
- **Monthly Essentials, 9,900 NX, 30 days, once per world:** Special Store Permit, Portable Storage, megaphones, transparent gear. **Fall Store Permit 3,000 NX, 90 days, 18 items.**
- **Not listed:** Hired Merchant, tab/storage coupons, standalone resets or Safety Charms. Gifting needs Lv 12+. Updated `00` §3.5–3.6 and Q5, `05` V-7/V-8, `plan_data.js` Q5.
- Review queue: **RQ-6** (decide day-1 buys with real prices; supersedes the mesos-based rule), **RQ-7** (no Hired Merchant in FA: overnight-selling plan).
- Source: https://g.nexonstatic.com/maplestory/cms/v1/news/45819 (2026-10-05)

## 0.6.1 · 2026-10-05 · Founder's Access release notes: level cap 100, 3 slots, Hollow closed
- **Level cap: Lv 100** [V-off] (was "50 or 70?"). 3rd job is still not at launch; what happens at Lv 70 stays open (V-10). Resolves Q2 and V-10.
- **Up to 3 characters per account** [V-off]. Resolves V-2 (confirm on screen); worlds (V-3) still open.
- **Forgotten Hollow is closed during Founder's Access.** FA bosses: Mano, Mushmom, Shade, Zombie Mushmom, Jr. Balrog. KPQ open from Lv 21; crafting from Lv 10; citizenship from Lv 12 (Henesys, Kerning).
- Inkwell interview (Oct 2): detailed post-launch roadmap at MapleStory Fest in October; deliberately slower update pace; 3rd job and regions "may be introduced sequentially"; a new boss in development; Cash Shop to avoid stat or growth items.
- Review queue: **RQ-4** (cap 100 vs the route and SP plan that stop at 70), **RQ-5** (Hollow closed vs the Lv 39–50 route and the Oct 20 projection). Not applied.
- Note: the markdown edits in `00` and `05` were made by an earlier interrupted run (Oct 4) and were re-verified against the post in this run.
- Sources: https://g.nexonstatic.com/maplestory/cms/v1/news/45621 (2026-10-03), https://g.nexonstatic.com/maplestory/cms/v1/news/45681 (2026-10-02)

## 0.6.0 · 2026-10-02 · Farmer switched to I/L Wizard; Assassin launch character
- **Your decision:** I/L Wizard farmer and Assassin launch character. The Hunter fallback is retired; `03_hunter_funding_checklist.csv` stays as an archive.
- `01_early_access_route.md` rewritten for I/L: maps chosen by magic DEF, accuracy and congestion; AP plan (INT, LUK only for wands); SP plan with Thunder Bolt first and MP Eater 1 at Lv 30; accuracy table; bosses; Kerning citizenship.
- New `calc/il_projection.py` (fixes the one-level EXP offset): Lv ~47/51/57 and ~1.4M/3.9M/8.0M net coin mesos by Oct 20 (low/mid/high). Equipment drops shown as a sensitivity (drop rate unknown). The Fighter scripts stay as the comparison baseline.
- Facts the switch depends on, corrected in `00`: spells can miss; Teleport costs 55 MP at skill Lv 1; Thunder Bolt works from Lv 30 and scales by skill level; NPC sell-back is 21-50% for equipment and 1 meso for scrolls; Hwabi has no confirmed launch-scope source; the package must be opened within 30 days of claiming.
- `02`, `03_assassin_funding_checklist.csv`, `04`, `05`: farmer-specific lines updated; merchant role limited to the offline Hired Merchant or Store Permit sessions (one account = one character online); new checks V-38 to V-41.
- Dashboard: characters now come from `data/plan_data.js` (`meta.characters`); saved Fighter/Hunter levels are archived on first load (schema 2); magic DEF column; the projection table moved into the data.
- Review: `../review/REVIEW_2026-10-02.md` (review findings outside the switch were not applied).
- Sources: https://meowdb.com/msclassic/guides/il-wizard-class-guide, https://meowdb.com/msclassic/formulas, https://meowdb.com/msclassic/guides/attacks-you-can-use-mid-jump, https://meowdb.com/msclassic/api/items?type=Equip, https://support-maplestory.nexon.com/hc/en-us/articles/53268989017620-Founder-s-Packages-Frequently-Asked-Questions

## 0.5.0 · 2026-10-02 · Auto-updater and phone copy
- Scheduled updater: daily 2:30 PM and 9 PM CT, plus one-off runs at 1:30 PM CT on Oct 6 and Oct 21 (`updater/UPDATER_RULES.md`).
- First supervised run (commit 3e2d90d): no changes; Nexon CMS, Nexon support, meowdb sitemap and YouTube checked.
- Private claude.ai copy of the dashboard: https://claude.ai/artifact/WGdkJ7HCh93qLxcYKU4Zrk (prices, checkmarks and notes sync to the owner's account there).
- Sources: https://g.nexonstatic.com/maplestory/cms/v1/news

## 0.4.0 · 2026-10-02 · Dashboard
- Added `index.html` and `data/plan_data.js`: Updates, Class Tier Matrix, Route & SP tracker, Farming Targets, Price Log & Watchlist (signals R1–R7, JSON/CSV export and import), Launch Checklist, Dual-Character Routine.

## 0.3.0 · 2026-10-02 · Market and operations
- `02_market_playbook.md`, `03_assassin_funding_checklist.csv`, `03_hunter_funding_checklist.csv`, `04_dual_character_ops.md`.
- Sources: https://meowdb.com/msclassic/item-db, https://meowdb.com/msclassic/npc-shops, https://meowdb.com/msclassic/quest-tracker/all

## 0.2.0 · 2026-10-02 · Founder's Access route
- `01_early_access_route.md`, `05_launch_day_verification.md`, `calc/` scripts.
- Projection: Lv ~51–60 and ~2.3M–13.7M net mesos from mob drops by Oct 20.
- Sources: https://meowdb.com/msclassic/guides/fighter-class-guide, https://meowdb.com/msclassic/guides/best-grind-maps-every-level, https://meowdb.com/msclassic/api/mesos-reports?monsterId=32

## 0.1.0 · 2026-10-02 · Verified intel
- `00_classic_world_verified_intel.md`, `updater/sources.json`.
- Farming pick: Fighter. Launch: Assassin if a friend plays an AoE class, otherwise Hunter.
- Sources: https://www.nexon.com/maplestory/news/general/45385/classic-world-frequently-asked-questions, https://www.nexon.com/maplestory/news/general/44359/ossyria-exploration-report, https://meowdb.com/msclassic/guides/class-dps-rankings
