# MapleStory Classic World: Verified Intel (Phase 1)

Version 0.1 · last checked 2026-10-02 · Founder's Access opens **Tue Oct 6, 11:00 AM PDT (1:00 PM CDT)**; Grand Launch **Wed Oct 21, 11:00 AM PDT (1:00 PM CDT)** [V-off N1].

## How to read this file

| Tag | Meaning |
|---|---|
| **[V-off]** | Official Nexon post, patch/maintenance notes, or support article. |
| **[V-dm]** | Datamine of the **COT2 test client (Aug 2026)**, mostly via meowdb.com/msclassic, cross-checked against maplestory.io `MCW/CBT2` where noted. Classic-specific, but from a test build: **values may change at launch**. |
| **[V-cbt]** | First-hand test reports or community measurements from COT1 (Apr 2026) / COT2 (Aug 2026). A single report is low confidence. |
| **[B]** | Legacy pre-Big Bang GMS baseline (maplestory.io GMS v83 client data, Wikibooks, ayumilove). Assumption only, never Classic fact. **[B?]** = recalled, not re-fetched (hidden-street, StrategyWiki, the fandom wiki and archive.org were blocked during research). |
| **[?]** | Unknown or unsourced. Goes on the launch-day verification list (§7). |
| **[calc]** | My arithmetic; inputs shown inline. |

Source keys (N1, M-DPS, …) resolve to URLs and dates in §8. `updater/sources.json` holds the monitoring list.

**Player profile** (from kickoff_prompt.md): NA, US Central. 4 h weekdays / 8 h weekend days, before and after Oct 21. **Founder's Access budget = 76 h** (11 weekdays × 4 h + 4 weekend days × 8 h, Oct 6–20). The research agents were briefed with 88 h by mistake; every "hours left" figure below is corrected to 76 h. Zakum package (cosmetic only). Cash Shop: "whatever pays off". 1–2 friends, classes undecided. Balanced risk.

---

## 0. Read first: assumptions that broke or changed

| # | Spec assumption | Status | What's actually true | Affects |
|---|---|---|---|---|
| A1 | Level cap 70 | **Unconfirmed** | Nexon has published no launch cap [V-off N1, N3]. COT1 stopped at 50; COT2 opened 3rd job at 70 and gave testers a Lv 100 test boost [V-off N4]. meowdb's EXP-table page (Sep 18) says "Current Launch Cap: Level 50"; its newer pages (Sep 29–30) say "not published" [V-cbt M-EXP, M-REL]. Confirmed: **3rd job (Lv 70) is not at launch** [V-off N3], so 2nd job is the ceiling. | Farming at cap, citizenship grade 9 (needs Lv 52), route 51–70 |
| A2 | Magicians advance at 8; stat dice at creation | **Broken** | All classes take 1st job at **Lv 10 with no stat requirement** [V-off N7; V-dm M-Q1017]. **No dice**: every stat starts at 4 plus 9 free points [V-cbt W-CC]. | Route 1–10, AP plans |
| A3 | I/L is the best farmer (Thunderbolt) | **Broken** | I/L only mobs well from ~Lv 45–50, Thunder Bolt is weak per target (Basic Atk 70), costs 40 MP/cast, and there's no Spell Booster before 3rd job. Elemental weakness is only **1.25×** (legacy 1.5×) [V-dm M-SKILL, M-DMG]. See §2. | Farming pick |
| A4 | Pirates may be in scope | **Broken** | **No Pirates**, Cygnus or Aran. Only 4 Explorer classes, 10 2nd jobs [V-off N3 class split; V-dm M-CLASS]. | Census |
| A5 | Meso Up, Meso Guard, Rush, Flash Jump are legacy 3rd-job previews | **Changed** | **Rush is now a 2nd-job skill for all three warriors**, cooldown 1 s [V-dm; V-off N5]. **Power Guard and Hyper Body moved to 3rd job** (not at launch) [V-dm M-CLASS]. **Meso Up doesn't exist** in Classic's Hermit list. Flash Jump, Meso Guard, Pickpocket and Avenger are 3rd job (not at launch) [V-dm]. | Class census |
| A6 | GFA 60%/10%, Claw ATT 60%/10%, DEX/LUK scrolls | **Changed** | New tiers: **Lesser 100% (+1)**, Intermediate 60% (+2), Greater 10% (+3), Chaos 10% (+4, **50% destroy**). **NPCs sell Lesser scrolls**: weapon Lessers 25k–50k to anyone; GFA Lesser 50k only at citizenship grade 9. **No** Gloves DEX, Helmet DEX/INT, Top/Bottom stat, Shoes DEX, or 30%/70% scrolls [V-dm M-ITEM]. | Market playbook, funding CSV |
| A7 | 4-slot starting storage | **Unknown** | Storage is **account-shared** (items and mesos), **100 mesos per item deposited** (50 with a citizenship discount), cap 50 per the NPC pages, or up to 150 via +5 coupons. **Starting slots [?]** [V-dm M-NPC]. | Dual-character ops |
| A8 | FM rooms, offline vending (Hired Merchant) | **Partly holds** | FM Entrance with **11 rooms** [V-dm]. **Store Permit** (Cash Shop, 16 items) works **in fields or the FM** and closes if a mob hits you [V-dm]. **Hired Merchant** (offline, FM only, 24 h) **ran in COT2** [V-off N6] but the datamine marks it "not currently sold" → launch availability **[?]**. Both need Cash Shop items. | Market playbook |
| A9 | Kerning PQ, Jane and Maya quests | **Exist, changed** | KPQ: Lv 21+ with no upper limit, 4 players, **Channel 1 only**, 30 min [V-cbt M-KPQ]. Jane is a **4-step quest line** (scrolls, Elixirs, GFA chance), **not a potion shop** [V-dm]. Maya exists (5 collection quests); "Sparkling Rock" not found [V-dm]. Shumi exists but is **not repeatable** [V-dm, conflicting list view]. | Route, quests |
| A10 | Tobis, Steelies, Meba, Slain | **Exist, scarce** | All exist [V-dm]. Only Subi (500/set) and Wolbi (1,000/set, citizenship-gated) are NPC-sold; **no star crafting** in 348 recipes. In launch areas, Tobi comes only from Dark Stone Golem; Steely's source is unclear (community reports point to Red Drake) [V-dm; V-cbt M-DROPS]. Claws were cut ~40–50% in W.ATK from COT1 to COT2 [V-dm]. | Funding CSV |
| A11 | Character count / mules | **New limit** | Both tests: **3 characters per account** [V-off N7, N4]. No slot-expansion item in the datamine. Launch count [?]. Plan: farmer + launch character + 1 mule at most. | Dual-character ops |
| A12 | Two clients | **Plan on one** | Official: only one of MapleStory / Classic open at a time [V-off N1]. Two **Classic** clients: not addressed [?]. | Daily schedule |

New systems that legacy didn't have (all [V-dm] unless noted):
- **Citizenship** (Henesys or Kerning, from Lv 12). Grades unlock NPC stock (Wolbi, GFA Lesser, stat scrolls, Elixirs) and storage discounts.
- **Six crafting professions** (348 recipes).
- **Forgotten Hollow**: a new Lv 39–60 area with 10 new mobs and the Rotten Mushmom boss.
- **Pet auto-pot and auto-loot skills** (Cash Shop).
- **Full AP/SP resets** (Cash Shop).
- **Crit stats** replace Hands.
- **Fixed HP/MP per level**: no HP washing [V-cbt M-HPMP; interview C2].

---

## 1. Recommendations

### 1.1 Farming character: **Fighter (2H Axe)**

Measured against the spec's definitions:

**Priority 1: most mesos plus resale value by Oct 21, counting leveling time.**
- **Fighter farms earliest.** Its 1st-job Slash Blast already hits 4 targets: 130%, 150 px, no cooldown, maxed around Lv 25 [V-dm M-SKILL]. No other class has multi-target damage before 2nd job except the Archer's melee-range Power Knockback. Efficient 2nd-job farming starts around **Lv 35, after ~21–30 h** [calc, warrior notes], leaving **~46–55 of 76 h** for efficient farming. Hunter, I/L and F/P only become efficient around Lv 45–50, after 27–60 h.
- **Lowest upkeep per unit of damage.** Damage/MP is #1 of all classes (Fighter 264.5; Page 236.3; Spearman 224.2; Crossbowman 174.2; Hunter 166.5; Assassin 160.0; Bandit 147.6; I/L 114.5; F/P 95.2; Cleric 88.2) [V-cbt M-TIER model].
- **Mesos appear to scale with mob level**: ~2× mob level per kill in 13 single COT2 reports [V-cbt M-MESO, low confidence]. Mesos per HP are best on dense low-HP mobs (Jr. Wraith: ~67 mesos for 982 HP). AoE classes win that trade.
- **Resale value**: farming maps decide drops, not class. A Fighter can farm Jr. Wraith (Mokbi stars), Lupin (Kumbi) and Zombie Mushroom (Claw ATT Intermediate), and can solo Mushmom (Lv 40, 34,440 HP; Ilbi stars) and Zombie Mushmom (Lv 50, 53,640 HP; Ilbi/Hwabi). Fighter is #2 in single-target DPS [V-dm/V-cbt M-DROPS, M-DPS].
- **Highest durability** of the damage classes (2H physical EHP ≈4,010; ≈6,500 with 1H + shield) means fewer deaths. Death costs up to 10% of the EXP bar [V-cbt W-DEATH].

**Priority 2: solo mesos/hour after Oct 21 and at the cap.**
- **#1 AoE DPS at Lv 70** (9,235/s with Slash Blast plus FA Axe on 3 targets) and **#2 single-target** (4,390/s) [V-cbt M-DPS model: stationary 0-DEF target, all hits land].
- Rage (+40 Attack Power) and Axe Bleed are self-sufficient. There's no ammo cost.
- Rush (1 s cooldown) gives some mobility [V-off N5].

**Risks to this call:**
- Mesos per kill are unmeasured [?]. If high-level single mobs drop far more than ~2× level, **Bandit** (#1 single-target, MGI 5.7) closes the gap.
- Lv 35–70 axes are drop/FM/craft only [V-dm], so expect to spend on the weapon around Lv 40.
- Short reach and a 4-target cap. **Hunter** (#2 AoE, best range) is the runner-up farmer if melee feels bad in play.

**Expected state on Oct 20** [calc, `01_early_access_route.md` §0]: **Lv ~51–60 (mid ~55)** and **~2.3M–13.7M net mesos from mob drops (mid ~7.7M)**, before any item sales. The range comes from the unmeasured meso drop chance and real-play pace. **Lv 70 is not reachable in Founder's Access.**

### 1.2 Launch character: **Assassin, but only if a friend brings AoE; otherwise Hunter**

Measured against "best fit for group play alongside my friends' classes, with funding needs the farmer can cover":

**For the Assassin:**
- **Farmer synergy.** The Fighter's natural farming maps drop the Assassin's ammo: Jr. Wraith gives Mokbi, Lupin and Fire Boar give Kumbi, Dark Stone Golem gives Tobi, Mushmom and Zombie Mushmom give Ilbi and Hwabi [V-cbt M-DROPS; B MSEA lists]. That supply is internal and costs no market purchases.
- **Funding is the Assassin's biggest lever.** It gains +71.9% DPS from realistic to max-scrolled gear, the most of any class [V-cbt M-DPS].
- It's ranged and safe (400 px with Keen Eyes).
- It's #3 in single-target damage.
- **Haste** is a party buff: +30 Speed and +10 Jump for 300 s.

**Against the Assassin:**
- **No multi-target attack at all until Avenger, which is 3rd job with no date** [V-dm]. In a 2–3 person leveling party, that hurts unless a friend clears mobs.
- Heavy MP use (Lucky Seven costs 16 MP per cast; about 29k–48k mesos/h of potions). Star recharge is cheap at about 1k–4k/h [calc, thief notes].
- Claw scrolls cost twice as much as dagger scrolls (50k Lesser).
- Wolbi needs about 1–2 weeks of Kerning citizenship dailies.

**Rule:** if at least one friend plays Fighter, Hunter, I/L or F/P, take **Assassin**. If both friends pick single-target classes, take **Hunter** instead: #2 AoE, a 60% stun, cheap to fund, and good next to a melee friend. If the friends want a support, a **Cleric** (Heal, Bless +20 ACC/EVA) adds the most to a physical group but has the lowest damage in the game.

**Action:** get your friends' class picks before Oct 21. This call is the one most likely to change.

### 1.3 What would change these calls
- **Meso drops per kill** (measure in the first hour): if mesos don't scale with mob level, AoE's advantage shrinks.
- **Level cap 50 instead of 70**: Fighter still leads (it's efficient early), but Lv 51–70 route sections and grade-9 citizenship (Lv 52) disappear.
- **Launch patch values** differ from the COT2 datamine (Nexon called the Aug 11 mobility changes "an experiment" [V-off N5]).
- **Friends' classes** (§1.2).

---

## 2. Class census

### 2.1 Side-by-side (10 second jobs; Lv 70 figures are meowdb's model on a stationary 0-DEF target with every hit landing [V-cbt M-DPS, M-TIER])

| Class | Efficient farming from | FA hours used before efficient (of 76) | Main multi-target | Lv 70 single-target DPS (rank) | Lv 70 AoE DPS (rank) | Damage/MP (rank) | Phys. EHP | Funding | Solo (1–10) | Party (0–10)† | **MGI** |
|---|---|---|---|---|---|---|---|---|---|---|---|
| **Fighter** | ~Lv 35 (SB from ~Lv 20) | 21–30 | Slash Blast 4 + FA Axe 3 | 4,390 (#2) | **9,235 (#1)** | **264.5 (#1)** | 4,010 | Medium | 8 | 7 | **6.7** |
| Page | Lv 38–40 | 26–37 | Slash Blast 4 | 3,953 (#5) | 7,563 (#5) | 236.3 (#2) | 4,190 (6,760 w/ shield) | Med-Low | 7 | 6 | 6.0 |
| Spearman | Lv 38–40 | 26–37 | Slash Blast 4, Rush 4 | 3,745 (#6) | 7,262 (#7) | 224.2 (#3) | 4,330 | Medium | 7 | 3 | 5.8 |
| Bandit | Lv 43–47 | 28–44 | Steal 2 | **5,696 (#1)** | 3,553 (#8) | 172.9 | [?] | Medium | 7 | 4 | 5.7 |
| Hunter | Lv 45–50 | 27–46 | Arrow Bomb 4 + 60% stun | 3,982 (#4) | 8,600 (#2) | 166.5 | 2,620 (lowest) | Low-Med | 7 | 5 | 5.6 |
| Crossbowman | Lv 50–60 | 35–55 | Iron Arrow 4 (pierce, falloff) | 3,530 (#7) | 7,412 (#6) | 174.2 | 2,620 | Low-Med | 6 | 4 | 5.1 |
| I/L Wizard | Lv 45–50 | 35–60 | Thunder Bolt 6 + 25% stun | 3,107 (#9) | 7,675 (#4) | 114.5 | [?] | Medium | 7 | 5 | 4.9 |
| F/P Wizard | Lv 41–50 | 35–60 | Poison Breath 4 | 3,289 (#8) | 7,944 (#3) | 95.2 | [?] | Medium | 7 | 4 | 4.8 |
| Cleric | Lv 37–41 | 25–40 | Holy Arrow 3 | 3,044 (#10) | 3,044 (#9) | 88.2 | **7,610 (#1)** | Low-Med | 5 | **8** | 4.5 |
| Assassin | Lv 37–47 | 20–40 | **none** | 4,266 (#3) | — (no AoE) | 160.0 | 3,850 | High-Med | 6 | 5 | 4.4 |

† Party scores are my judgement from the skill kits: Fighter 7, Page 6 and Spearman 3 came from the warrior notes, Hunter 5 and Crossbowman 4 from the bowman notes, the rest are mine.
Hours columns are [calc] from meowdb's modeled EXP/min with a 1.5–2.5× real-play factor. They are estimates, not measurements.

### 2.2 Meso Generation Index (MGI): method

MGI = 0.20·A + 0.20·B + 0.25·C + 0.15·D + 0.10·E + 0.10·F, with sub-scores from 0 to 10:
- A: time to efficiency
- B: mobbing/AoE
- C: kill speed against meso-rich mobs
- D: upkeep (10 = cheap)
- E: funding needed (10 = little)
- F: meso-specific skills

Each research agent scored its own class family. I normalized across families: F = 0 for every class without a meso skill (the magician notes had given 2), and Bandit F = 3 (Steal's item roll, yield [?]). Warriors' A gets +1 because Slash Blast farms from 1st job. Assassin's A goes from 7 to 6.5 because efficiency spans Lv 37–47.

| Class | A | B | C | D | E | F | MGI |
|---|---|---|---|---|---|---|---|
| Fighter | 8 | 8 | 8 | 6.5 | 5 | 0 | 1.6+1.6+2.0+0.975+0.5 = **6.7** |
| Page | 7 | 7 | 7 | 6 | 5.5 | 0 | 1.4+1.4+1.75+0.9+0.55 = **6.0** |
| Spearman | 7 | 7 | 6.5 | 6 | 5 | 0 | 1.4+1.4+1.625+0.9+0.5 = **5.8** |
| Bandit | 6 | 4 | 8 | 5 | 6 | 3 | 1.2+0.8+2.0+0.75+0.6+0.3 = **5.7** |
| Hunter | 5 | 7 | 7 | 5 | 7 | 0 | 1.0+1.4+1.75+0.75+0.7 = **5.6** |
| Crossbowman | 4 | 6 | 6 | 6 | 7 | 0 | 0.8+1.2+1.5+0.9+0.7 = **5.1** |
| I/L | 4 | 9 | 5 | 3 | 6 | 0 | 0.8+1.8+1.25+0.45+0.6 = **4.9** |
| F/P | 4 | 7 | 6 | 3 | 6 | 0 | 0.8+1.4+1.5+0.45+0.6 = **4.8** (4.75) |
| Cleric | 5 | 4 | 5 | 5 | 7 | 0 | 1.0+0.8+1.25+0.75+0.7 = **4.5** |
| Assassin | 6.5 | 2 | 6 | 5 | 4 | 0 | 1.3+0.4+1.5+0.75+0.4 = **4.4** (4.35) |

**C and D could each move by about ±2 once mesos per kill is measured.** The gaps below about 0.5 MGI are noise.

### 2.3 Shared mechanics (all classes)

- **Damage formula** [V-dm M-DMG]: MAX = S × TotalATK × (1 + (Primary × WeaponMult + Secondary)/100 + AttackPower/50).
  - Defense: × 100/(DEF+100).
  - Crit: base 5% for +20% damage. "Hands" is removed.
  - Elements: weak 1.25×, "enhanced weak" 1.5×, resist 0.75×. Legacy weakness was 1.5× [B v83 skill text].
  - Weapon multipliers are about half of legacy [B L-AYU], with a new +1 base term and Attack Power. Two-handed weapons now beat one-handed by about 44% in the stat term, versus about 6% in legacy [calc].
- **Spell cast time**: all 2nd-job spells take 810 ms (Heal 600 ms). No Spell Booster before 3rd job [V-dm].
- **Booster speeds**: +2 stages, 300 s for every class [V-dm].
- **COT2 mobility pass (Aug 11)** [V-off N5]: Rush cooldown 3→1 s (MP 40→20 by level). Flash Jump lost its cooldown. Ranger/Sniper steps changed. Invincibility after a hit went from 1.0 to **1.5 s**. **Only Rush is in launch scope**; the rest are 3rd job.
- **Base movement**: Speed 100 now moves like legacy 120 (150 px/s); speed cap 140 [V-cbt M-MOV].

### 2.4 Warriors (Swordman → Fighter / Page / Spearman)

All values [V-dm M-SKILL, M-CLASS] unless tagged.

**Changes vs legacy:**
- Endure is removed; Improved HP Recovery now regenerates while moving and adds +20% to potion HP.
- New 1st-job **Precise Strikes** (+20 ACC, +5% crit).
- **Max HP Increase** gives +25% immediately.
- Slash Blast hits **4** targets (legacy 6 [B L-AYU]).
- Iron Body is **+25% WDEF for 600 s** (legacy +40 flat for 300 s).
- **Rush** is in 2nd job for all three branches (legacy 4th job [B]).
- **Power Guard and Hyper Body are 3rd job**, not at launch.
- Final Attack procs **50%**; Fighter's FA hits up to 3 targets at 140%.
- Rage gives **+40 Attack Power** to the party but −40 WDEF to every member, for 300 s.
- Axe Mastery adds a 25% **Bleed** (100% damage over 3 s).
- Blunt Mastery gives a 20% chance to ignore WDEF.
- Spear Mastery gives +20% crit; Polearm Mastery gives +20 speed.
- Spear/Polearm FA heals 10% of damage dealt.
- Iron Will is +50 WDEF and 35% knockback resistance, self only, with no MDEF.
- Threaten: 4 mobs, −10 WDEF and −35 speed.

**Weapons:** NPC weapons stop at Lv 30. River (Perion) sells Blue Axe and Mithril Maul for 26,000 and the Two-Handed Axe for 16,500. **Everything from Lv 35 to 70 is drop, market or craft only.**

**Job advancement:** 1st job at Lv 10 with no STR requirement (legacy 35 STR [B L-AYU]); 2nd job at 30 with Proof of a Hero.

**Upkeep:** about 12 mesos of MP per Power Strike or Slash Blast cast (Lemon at 1 meso/MP), so roughly **25k–40k mesos/h (Fighter)** or 18k–28k (Page, Spearman) at 40–60% attack uptime [calc, warrior notes].

| | Pros | Cons | Solo | Funding | MGI reasoning |
|---|---|---|---|---|---|
| **Fighter** | #1 AoE, #2 single target, #1 damage/MP, Rage, Bleed, FA hits 3, AoE from 1st job | Highest absolute MP spend (fast casts), Rage lowers own WDEF, short reach, no Power Guard | 8 | Medium | Earliest efficiency, best AoE, cheapest damage |
| **Page** | FA 270% single target, best shield tank (Guard passive), WDEF ignore, Threaten | FA useless for AoE, slow blunts, Booster maxed late | 7 | Med-Low (craftable blunts) | Solid but its AoE is just Slash Blast |
| **Spearman** | Best reach (122 px), FA lifesteal, highest 2H EHP, Rush plus Slash Blast | **No party buff until 3rd job (Hyper Body moved)**, lowest warrior DPS | 7 | Medium | Comfortable solo, little else |

### 2.5 Thieves (Rogue → Assassin / Bandit)

All values [V-dm] unless tagged.

**Changes vs legacy:**
- **Lucky Seven**: 140% × 2 stars, 16 MP (COT1 was 120%). Keen Eyes max 15 gives **400 px** star range; Nimble Body max 15.
- **Dark Sight** is a toggle with no speed penalty at max.
- **Critical Throw**: only +15% rate and +35% crit damage (legacy up to 50% rate and +100% [B Wikibooks]).
- **Claw Mastery**: +20 Attack Power and a 25% chance to recover thrown stars; it no longer raises stack size.
- **Drain**: 240%, with a 12% chance to absorb 15% of damage.
- **Endure removed**: Assassin gets Critical Recovery (10% HP/MP on crit, once per 30 s) and Bandit gets Nimble Recovery (on evade).
- **Savage Blow**: 75% × 6 hits.
- **Steal**: 2 targets at 180%, 90% steal chance, stun 1.5 s, and **+35 Attack Power for 30 s**. Its loot pool is [?].
- **Dagger Mastery**: +20% crit and 20% knockback ignore.
- Haste: +30 Speed and +10 Jump to the party. The Assassin and Bandit versions don't stack.
- **Meso Up doesn't exist.** Pickpocket, Meso Guard, Flash Jump and Avenger are 3rd job, not at launch.

**Stars and claws:** see §4.3.
- Claws from Lv 35 up are craft or market only. Adamantium Guards (Lv 30) cost 27,600 from Manny, Kerning.
- Claw ATT Lesser costs 50k each (El Moth); Dagger ATT Lesser costs 25k.
- The Bandit's best path wants an SP Reset Scroll (Cash Shop, price [?]).

| | Pros | Cons | Solo | Funding | MGI reasoning |
|---|---|---|---|---|---|
| **Assassin** | Ranged and safe, #3 single target, scales most with scrolls (+72%), Haste | **No multi-target until 3rd job**, MP-hungry, drop-only stars above Wolbi, claw scrolls cost 2× | 6 | High-Med | Single target with real ammo logistics |
| **Bandit** | **#1 single target**, 1-hit kills at 70, no ammo, Steal buff, stun and item roll | Melee face-tanking, 2-target cap, best build needs an SP reset | 7 | Medium | Fastest single-target farmer; ~1.3–1.7× the Assassin's kills/h [calc] |

### 2.6 Bowmen (Archer → Hunter / Crossbowman)

All values [V-dm] unless tagged.

**Changes vs legacy:**
- **Blessing of Amazon removed.**
- **Power Knockback moves to 1st job**: max 15, 4 mobs, always crits.
- **Critical Shot**: only +20% rate and +15% crit damage (legacy 40% for 200% [B Wikibooks]).
- **Arrow Bomb**: 140%, **4** mobs (legacy 6), 60% stun for 3 s, 28 MP.
- **Iron Arrow**: 180%, pierces 4 with damage falling 100/80/60/40%.
- **Final Attack: Bow** fires 3 arrows at 90%.
- **Soul Arrow** lasts 300 s (legacy 600).
- New 2nd-job passive **Amazon's Judgement**: crits slow by 35 for 5 s.
- Crossbows **whack inside 65 px**; the bow's dead-zone distance is [?].
- Bowmen get **no movement skill** before 3rd job and nothing from the Aug 11 mobility pass.

**Ammo:** arrows cost 1 meso each (Bronze is 2 mesos and gated by citizenship). Soul Arrow (Lv 34+) removes arrow cost, so **MP is the real cost: about 7–14 mesos per kill** for a Hunter [calc].

| | Pros | Cons | Solo | Funding | MGI reasoning |
|---|---|---|---|---|---|
| **Hunter** | #2 AoE, 60% stun on 4, longest range, cheap gear | **Lowest EHP**, no mobility, efficient only around Lv 45–50, weaker crit | 7 | Low-Med | Strong ceiling, late start |
| **Crossbowman** | #4 damage/MP, 20% DEF ignore, highest-ATT weapons | Needs lined-up mobs, slow weapons, no stun, point-blank whack | 6 | Low-Med | Map-dependent AoE |

### 2.7 Magicians (Magician → Cleric / I/L / F/P)

All values [V-dm], cross-checked against maplestory.io `MCW/CBT2`; legacy values from `GMS/83` [B].

**1st job:**
- **Energy Bolt 130** (legacy 55); Magic Claw 65 × 2.
- **Magic Guard is a toggle** (80%).
- **Magic Armor** gives +120 W.Def and +120 M.Def for 600 s (legacy +40 W.Def).
- Improved MP Recovery: 1% of Max MP per 10 s, plus +20% MP from items.
- Max MP Increase: +25%. **INT gives no extra MP** [V-cbt M-HPMP].

**Cleric:**
- **Holy Arrow** fires 3 × 60 and can split over 3 targets (legacy 80, single target).
- **Heal**'s undead damage is small: about 204 per mob on 5 undead at Lv 70, and it is not Holy element [calc]. Heal is **not a farming tool**.
- Bless: party +20 ACC and +20 EVA. Invincible cuts touch damage by 30%.

**I/L:**
- **Thunder Bolt**: 6 targets, Basic Atk 70, 40 MP, 25% stun.
- **Cold Beam**: 170 (legacy 100). The skill text says "frozen"; meowdb reads it as a slow [?].

**F/P:**
- **Fire Arrow**: 180 plus a burn (legacy 120).
- **Poison Breath**: now hits **4** targets at Basic Atk 80 for 40 MP (legacy single target).

**Shared 2nd job:**
- MP Eater: 50% chance to absorb 50% of the mob's MP, at most once per 5 s.
- Teleport: 15 MP, no cooldown, unchanged by the mobility patch.
- Meditation: party +25 M.ATK.
- 3rd-job previews (not at launch): I/L Thunder Spear; F/P Explosion and Poison Mist; Priest Doom and Mystic Door. Holy Symbol is reworked into self-resurrection. **There is no Chain Lightning in Classic.**

**Wands:** Flora (Ellinia) sells wands up to Mithril (Lv 30, 22,000). The Wizard Wand is El Nath only, so not at launch. Fairy Wand and Cromi are crafted (Arcforge). Wand Lesser scrolls cost 25k each.

**Upkeep:** **about 40k–90k mesos/h** [calc, magician notes]. Elixir and Mana Elixir now have a **30 s cooldown** [V-dm].

| | Pros | Cons | Solo | Funding | MGI reasoning |
|---|---|---|---|---|---|
| **I/L** | 6 targets plus stun, Slow, best mage damage/MP | Weak per-target Thunder Bolt, no AoE before Lv 41, 40 MP per cast, single-target rank #9 | 7 | Medium | Late efficiency, high upkeep |
| **F/P** | Best mage single target (Fire Arrow plus burn), 4-target Poison Breath | Many high-level Victoria mobs resist fire or poison (Drakes, Golems, Malady) | 7 | Medium | Map-dependent |
| **Cleric** | Highest EHP, Heal and Bless (best support), cheapest mage upkeep | **Lowest DPS in the game**, Holy Arrow caps at 3 | 5 | Low-Med | Support, not a farmer |

### 2.8 Pirates
**Not in the Classic launch** [V-off N3: the COT2 class split lists only 4 classes; V-dm: no Pirate jobs, knuckles, guns or bullets]. China's separate Classic service has Pirates; that doesn't apply to Global.

---

## 3. Systems

### 3.1 Launch scope and dates
- **Dates:** Founder's Access opens Oct 6 at 11:00 AM PDT; Grand Launch is Oct 21 at 11:00 AM PDT. Founder characters, mesos and items carry over [V-off N1, N3]. Package purchase or upgrade deadline: **Oct 14, 11:59 PM PDT** [V-off N10], so the founder population can still grow until then.
- **Client:** the Nexon Launcher Classic client is downloadable only on launch day. Steam players should install base MapleStory now [V-off N2].
- **Areas:** Maple Island and Victoria Island: Henesys, Ellinia, Perion, Kerning, Lith Harbor, Sleepywood with its dungeons, the Kerning subway, Florina Road and beach, Swamp, Monkey Forest, Forest of Evil, Burnt Land and Golem's Temple. Plus **Forgotten Hollow** (Lv 39–60) and KPQ [V-dm M-MAPS].
- **Not at launch:** Orbis, El Nath and 3rd job [V-off N3]; Ludibrium, Aquarium, Leafre, Mu Lung, Nautilus and Zakum are absent from the data. Nexon promised "brand-new content" for Grand Launch without naming it [V-off N3].
- **Roadmap:** Ossyria and 3rd job will come "gradually", with no dates [V-off N3].
- **Jobs:** 1st job at Lv 10, 2nd at Lv 30 (10 branches), 3rd at Lv 70 (not at launch) [V-off N4, N7].

### 3.2 Accounts and worlds
- Classic uses the regular Nexon account. NX is shared with MapleStory; IGNs, Maple Points and MVP are not [V-off N1].
- **Only one game (MapleStory or Classic) can be open at a time.** Sanctions apply across both [V-off N1, N8].
- **3 characters per account** in both tests [V-off N7, N4]. Launch count [?]. No character-slot item in the datamine.
- The number of worlds is unannounced, and every source says "Classic World", singular [?]. Founders and F2P **likely share the world(s)**: progress "carries into Grand Launch" [V-off]. Explicit "same world" wording appears only on finalboss.io [?].
- Founder cosmetics move between your own characters through the Cash Inventory (same account, same world) [V-off N10]. Claim from the mailbox by **Nov 30, 2026, 23:59 UTC**, and leave Maple Island before opening.

### 3.3 Storage and inventory
- Storage is **shared across your account** for items and mesos [V-dm M-NPC].
- Storage NPCs: Lith, Henesys, Ellinia, Kerning, Perion, Sleepywood, the FM Entrance (Scrooge), and **Cave Fairy in Forgotten Hollow** [V-dm].
- **Fee:** 100 mesos per item deposited, at every NPC including Scrooge. A Henesys or Kerning citizenship grade cuts this 5% per grade, down to 50, at that town's storage only [V-dm M-CIT]. Withdrawal fees and meso-deposit fees are [?]. The flat 100 may be a meowdb template value [?].
- **Capacity:** the NPC pages say "capped at 50 slots". The Storage Room 5-slot Coupon says "+5, up to 150". **Starting slots [?].**
- **Inventory:** starting slots per tab [?]. +5 coupons per tab, up to 150 (Cash Shop, untradeable).
- **Mules:** with 3 characters per account, at most 1 dedicated mule next to the farmer and the launch character.

### 3.4 Trading and shops
- Face-to-face trading exists [V-off N7].
- **Trade tax, trade level gates and meso cap: unknown** [?]. meowdb's glossary claims "trade taxes apply to mesos" without a source. China Classic's 5% fee does not apply to Global.
- **Free Market:** Entrance with Fredrick (store banker), Scrooge (storage), and **11 rooms**. Teleport rocks are blocked there [V-dm M-MAPS].
- **Store Permit** (Cash Shop, untradeable): 16 items (24 for seasonal versions). Usable **in fields or the FM**; it closes if a monster hits you [V-dm].
- **Hired Merchant**: offline, FM only, removed **24 h** after setup; unsold items come back through Fredrick or the mailbox [V-off N6; V-dm]. Live in COT2, but marked "not currently sold" in the datamine. **Launch availability and price [?].**
- **Auction house:** none found [?].
- **Untradeable:** every Cash Shop item, opened Founder cosmetics, and Signature Style items [V-dm; V-off N1].
- COT2 had a **Hired Merchant stat-loss bug** and an **item dupe** (fixed Aug 7 and Aug 10) [V-off N6]. Rollback risk exists at launch.
- **Market prices:** none exist yet. Never assume any. meowdb's community price board is empty.

### 3.5 Rates and core systems

| Topic | Classic | Tag |
|---|---|---|
| EXP / drop / meso rates | **No multiplier stated.** EXP table matches pre-BB GMS for Lv 1–49; Lv 50+ is a legacy reference. EXP to reach Lv 30 is 548,637; Lv 50 is 6,851,591; Lv 70 is 31,545,355. 78% of the EXP to 70 is in levels 50–69, which are unverified | [V-dm/cbt M-EXP]; [?] rates |
| Mob EXP | Looks set by level alone (every Lv 34 mob gives 70 EXP), so low-HP mobs are EXP-efficient. Many HPs changed vs v83: Jr. Wraith −18%, Wraith −16%, Stone Golem +28%, Tauromacis −38%. Bosses re-levelled: Mushmom 60→40, Zombie Mushmom 65→50 | [V-dm M-MOB] vs [B L-v83] |
| **Mesos per kill** | **No datamine.** 13 single community reports from COT2, all self-reporting a 100% drop chance, cluster at **~2× mob level**: Green Mushroom (Lv 14) 25–30, Jr. Wraith (34) 61–74, Lupin (37) 68–81, Zombie Lupin (41) 74–92, Rotten Mushroom (56) 100–120, Sporewood (59) 110–130, Mushmom 1,800–2,200, Zombie Mushmom 2,250–2,750 | [V-cbt M-MESO], low confidence |
| Item drop rates | **Not published or datamined.** meowdb's "MSEA reference drops" are legacy MapleSEA tables. Community-confirmed drops have votes but no rates | [?] |
| Pets | Cash Shop only (Brown Kitty, Pink Bunny, Husky and Snail were sold in COT2). Paid pet skills: **Auto HP Potion, Auto MP Potion** (threshold you set), **Auto Move** ("pick up nearby items and mesos without you having to move"). Plain pets pick up loot per a COT1 hands-on. Lifespan and launch prices [?]. Pet food 35 mesos | [V-dm]; [V-cbt C1] |
| NPC potions | Red 50 (100 HP), Orange 150, White 350, Blue 220 (200 MP), Lemon 150 (150 MP, best MP per meso), Meat 80 (160 HP), Pure Water 1,120 (800 MP), Unagi 1,000. **Elixir 3,000 at citizenship grade 10 only, restores 35% with a 30 s cooldown.** Power and Mana Elixirs are not NPC-sold. NPC sell-back is ~10% | [V-dm M-SHOPS] |
| Job advancement | 10 / 30 / 70, no stat requirements, Magicians included | [V-off N7; V-dm] |
| Stats | No dice: 4/4/4/4 plus 9 free points. 5 AP per level, all placed by hand. 3 SP per level (+1 at 1st job). **Fixed HP/MP per level** (Warrior +28/+12; Bowman and Thief +22/+17; Magician +16/+22). No HP washing. INT gives no MP | [V-cbt W-CC, M-HPMP] |
| AP/SP reset | Cash Shop. **AP Reset resets ALL stats** (including HP/MP); SP Reset resets all non-beginner skills. Prices [?] | [V-dm] |
| Party EXP | Bonus **+10% for 2, +20% for 3, +30% for 4 or more** (COT2 measurement; COT1 claims were higher). Split formula and level range [?]. Party pickup rights can be set | [V-cbt M-EXP]; [V-cbt W-MSW] |
| Kerning PQ | **Lv 21+, no upper limit**, party of 4, **Channel 1 only**, 30 min, 5 stages plus a bonus (King Slime). Rewards: Companion's Magic Box, rare Squishy Shoes, one-time "Proof of Companionship" (EXP, 614 mesos, Intermediate earring scroll). Daily limits [?] | [V-cbt M-KPQ] |
| Other PQs | Ludibrium PQ not at launch; Henesys/Ellinia PQ not found | [?] |
| Level cap | **Unconfirmed** (see A1). What happens at the cap [?] | [?] |
| Death | Lose up to 10% of the EXP bar; you can't lose a level; LUK reduces the loss. Safety Charm appears in COT2 notes, but a launch sale is [?] | [V-cbt W-DEATH]; [V-off N6] |
| Spawns | Global respawn check every 7.56 s. Map capacity is 75% of spawn points solo, +5% per extra player, 100% at 6+ | [V-cbt M-SPAWN] (community model) |
| Channels and worlds | Unknown | [?] |
| QoL | Fully rebindable keys (WASD), 3 key presets, 12 quick slots, controller support, enemy info UI, HP/MP warning thresholds, potion-use animation (small time cost) | [V-cbt M-CTRL; V-off N7] |

### 3.6 Cash Shop
- **Policy:** "cosmetics and convenience", with no items that directly raise EXP or strength [V-off N3]. EXP coupons exist only as tradeable **drops** [V-dm].
- **Currencies:** NX is shared with MapleStory. **Leaf Points** are a Classic-only cash currency. In COT1 they came from **tradeable** letter drops, a possible mesos-to-cash route; launch method [?] [V-off N1, N7].
- **Prices: none published.** Every datamined price (100 NX) is a test placeholder [V-off N7: "not final"].

| Convenience item | Effect | Worth it for this plan? (rule, not price) |
|---|---|---|
| Pet + **Auto Move** + **Auto HP/MP** skills | Auto-loot and auto-potion | **Highest value for the farmer.** Cuts looting walk time and potion downtime. Buy on day 1 if priced under roughly 1 hour of farming income (measure first). |
| Storage Room 5-slot Coupon | +5 shared storage | Buy when storage is the bottleneck for the bank role |
| Equip/Use/Etc/Set-Up tab coupons | +5 per tab | Etc tab first (drops), then Use (potions, scrolls) |
| Regular Store Permit | 16-item shop (field or FM) | Needed to sell at all without trading face to face |
| Hired Merchant | Offline FM shop, 24 h | **Best value if sold**: sells while you sleep or play the other character |
| AP / SP Reset Scroll | Full reset | Only for a build mistake or the Bandit "Sindit" path |
| Safety Charm | No EXP loss on death | Optional: cheaper to avoid deaths |

### 3.7 Rules (Terms of Service)
[V-off N9, N8, N1] (official, Oct 2026). This is a summary; the full text is at the linked pages.
- **Banned:** botting (a macro, third-party program or physical method that plays repetitively), hacking tools, **gold trading (RMT)**, account trading and account sharing. Penalties go up to a permanent ban. Bans apply to both MapleStory and Classic.
- **Pet auto-pot and auto-move are in-game features, not macros.** Using them is fine.
- **Running two Classic clients:** not addressed in any Global source [?]. **Plan for one client** until confirmed in game or by support. Gray area: don't run two without an explicit OK.
- **Multiple accounts per person:** not addressed [?]. Account sharing is banned.
- **No Classic-specific Code of Conduct.** Nexon points players to the standard ToS. Private servers are prohibited (Maple Memo, Sep 11).

### 3.8 New systems: citizenship and crafting
- **Citizenship** (Henesys via Arthur, or Kerning via Roxy; from **Lv 12**) [V-dm M-CIT]:
  - Grades need character level plus contribution: 2 Visitor (Lv 17, 1,000), **3 Helpful Stranger (22, 2,000)**, 4 (27, 3,000), 5 (32, 4,000), 6 (37, 5,000), **7 Distinguished Citizen (42, 6,000)**, 8 (47, 7,000), **9 Guardian of the Village (52, 8,000)**, **10 Citizen of Honor (57, 10,000)**.
  - Contribution comes from **one daily** (100 at grade 1, +50 per grade) and a **weekly donation of 100 of one ETC** (500 at grade 1, +250 per grade).
  - Unlocks:
    - Grade 3: **Wolbi** (Kerning, Max) and Earring scrolls.
    - Grade 7: **Overall stat Lesser** scrolls (35k): DEX/STR at Flint in Henesys, LUK/INT at Ben in Kerning.
    - Grade 9: **GFA/GFMA Lesser** (50k).
    - Grade 10: Elixir.
    - Also shop discounts up to 25% on tagged items and storage discounts up to 50%.
  - **Whether contribution resets after each promotion is unknown** [?]. That decides whether GFA Lesser opens around late Oct (cumulative) or months later (resets).
- **Crafting**: Smithing, Weaponcrafting, Tailoring, Woodcrafting, Leatherworking and **Arcforge** (gems, wands, and **Lesser scrolls** for Earring stat, Cape stat, Gloves ACC and Gloves Crit). Each unlocks at Lv 10 with a quest. **Only 11 of 348 recipes are profitable against NPC value** (mostly a meso sink). Black Crystal refining is net positive [V-dm M-CRAFT; V-cbt meowdb study].

---

## 4. Economy

### 4.1 Scroll system [V-dm M-ITEM]

| Tier | Success | Weapon ATT | On failure |
|---|---|---|---|
| Lesser | 100% | +1 | — |
| Intermediate | 60% | +2 | slot used [B assumption] |
| Greater | 10% | +3 | slot used [B assumption] |
| Chaos | 10% | +4 (gloves) | **50% destroy** (COT1: +5 with 100% destroy) |

- **Expected stat per slot** [calc]: Lesser 1.0, Intermediate 1.2, Greater 0.3, Chaos 0.4. Greater and Chaos are lottery tickets for "perfect" items.
- Scrolls sell to NPCs for 1 meso, so there's no price floor.
- **Scroll types that exist:**
  - Weapon ATT/MATK for every type.
  - **Gloves: ATT, MATK, ACC, Crit Rate.**
  - Hat: ACC, HP, MP.
  - Top/Bottom: DEF, HP, MP.
  - **Overall: DEX, STR, LUK, INT, DEF.**
  - Shoes: Evasion, Jump, Speed.
  - Cape: STR, DEX, INT, LUK, ACC, W.DEF, M.DEF.
  - Earring: STR, DEX, INT, LUK, Evasion, Crit Damage.
  - Shield: ACC, DEF.
  - Pet: Jump, Speed.

**NPC scroll shops (all Lesser 100%)** [V-dm]:
- **El Moth** (The Tree That Grew III): 1H weapon, dagger, wand and staff Lessers 25,000; 2H weapon, spear, polearm, bow, crossbow and **claw** Lessers 50,000. No requirement [?: whether reaching him needs Forgotten Hollow access].
- **Tulcus** (Swamp of Despair II): hat, top/overall/bottom DEF, shoes evasion, shield and cape DEF/ACC Lessers 15,000.
- **Flint (Henesys)** and **Ben (Kerning)**: citizenship-gated Lessers (see 3.8).
- COT1 to COT2 tightened this: Claw Lesser 20k→50k, and Overall DEX moved off Tulcus behind citizenship. **It may tighten again at launch.**

**Quest scroll supply** [V-dm M-Q]:
- Every character gets **3 guaranteed pick-one Greater scrolls for its own class's weapon**: Welcome to the Hollow (Lv 39), Blackbull (Lv 48), Alligators 1 (Lv 48).
- About **0.75 GFA/GFMA 60%** on average, from Collecting 150 Cursed Dolls (Lv 36, GFA60 or GFMA60) and Jane's Final Challenge (Lv 44, GFA60/GFA10/GFMA60/GFMA10 at 25% each).
- Whether quest rewards are tradeable is [?].

### 4.2 GFA and Claw ATT sources (launch scope)

| Scroll | NPC | Quests | Drops (B-MSEA reference unless marked) |
|---|---|---|---|
| GFA Lesser 100% | Flint/Ben 50k, **grade 9 only** | — | — |
| GFA Intermediate 60% | — | Cursed Dolls 150; Jane Final (25%) | Mushmom (Lv 40, in scope); others out of scope |
| GFA Greater 10% | — | Jane Final (25%) | Tortie (Lv 46, Florina) |
| Claw ATT Lesser | El Moth 50k | — | — |
| Claw ATT Intermediate | — | Jane and the Mushroom (Lv 20, 1 of 14 weapon scrolls) | Green Mushroom, Zombie Mushmom [V-cbt], Jr. Balrog; **Zombie Mushroom (community, 6 votes) [V-cbt]** |
| Claw ATT Greater | — | Hollow, Blackbull, Alligators (pick one) | Copper Drake (Lv 45) |
| Overall DEX/LUK | Flint/Ben 35k, grade 7 | — | DEX Intermediate: Mano, Mushmom; DEX Greater: Red Snail |

### 4.3 Throwing stars [V-dm M-ITEM; drops V-cbt M-DROPS or B-MSEA]

| Star | ATT | NPC | Stack | Recharge/unit | NPC sell | Launch-scope sources |
|---|---|---|---|---|---|---|
| Subi | 15 | **500 per set** at 12 grocers | 500 | 0.3 | 250 | NPC |
| Wolbi | 17 | **1,000 per set**, Max (Kerning), Helpful Stranger+ (item page says no requirement: conflict) | 500 | 0.4 | 500 | NPC; Fire Boar [V-cbt] |
| Mokbi | 19 | no | 700 | 0.5 | 1,000 | **Jr. Wraith** [V-cbt, 12 votes], Cold Eye, Stone Golem |
| Kumbi | 21 | no | 700 | 0.6 | 1,500 | **Lupin** [V-cbt], Fire Boar, Drake, Stone Golem |
| Tobi | 23 | no | 1,000 | 0.7 | 2,500 | Stone Golem [V-cbt], **Dark Stone Golem** (only in-scope MSEA source) |
| Steely | 25 | no | 1,000 | 0.8 | 10,000 | **Red Drake** [V-cbt, 9 votes]; no MSEA source listed |
| Ilbi | 27 | no | 800 | 0.9 | 20,000 | **Mushmom** [V-cbt, 9 votes], Zombie Mushmom [V-cbt] |
| Hwabi | 29 | no | 800 | 1.0 | 25,000 | **Zombie Mushmom** [V-cbt] |

- **No star crafting recipe exists** [V-dm].
- Demand signal: the five most-viewed items on meowdb during COT2 were all stars (Ilbi, Steely, Tobi, Kumbi, Hwabi) [V-cbt M-REPORT].

### 4.4 Key equips and materials [V-dm]
- **Work Gloves:** 5 slots (not the spec's "10-slot"). Quest rewards (Andre's Request, Lv 10) or Tailoring Lv 2. Clean bases are cheap; the value is in GFA'd gloves.
- **Sauna Robe** (Blue or Red): Lv 30, all classes, **10 slots**, +1 all stats. **One per character** from the "Returned Secret Book" chain (Lv 32). Tradeable. It's **the** base for Overall stat scrolls (the legacy Bathrobe role).
- **Boss crafting catalysts:** Mushmom, Zombie Mushmom and Rotten Mushmom drop them [V-cbt].
- **Demanded ores:** **Garnet** is "the most in-demand ore in COT2", and **Black Crystal** feeds earring and crit scrolls [V-cbt].
- **Quest bottleneck materials:** **Mushmom Spore** (1 per character, gate to Jane's chain), Drake Skull, Medicine With Weird Vibes, Dragon Skin, Stone Golem Rubble, Jr. Necki Skin.

### 4.5 Quests [V-dm M-Q]

**Repeatable or exchange:**
- **Arwen and the Glass Shoe** (Lv 29, repeatable): 1 Glass Shoe (Fire Boar drop) → 3,037 EXP, 848 mesos, and **Piece of Ice or Fairy Wing** (wand crafting inputs).
- **Citizenship daily and weekly** (see 3.8).
- **KPQ.**

**Notable one-time quests:**
- **Shumi's Lost Sack of Cash** (Lv 35, 10,000 mesos plus 30 Mana Elixirs; Coin and Roll pay 1,023 each). Not repeatable per the NPC page; the tracker list disagrees.
- **Jane** (Lv 20 and 44): Intermediate weapon scroll, 10 Elixirs, 15 Power Elixirs, and a GFA/GFMA chance.
- **Cursed Dolls** (Lv 36, Zombie Lupin): GFA60 or GFMA60, then a class hat.
- **Sauna Robe** chain (Lv 32).
- **Forgotten Hollow** chains: 84,249 EXP and 19,573 mesos in total.

Quest mesos are small. **Farming is the meso source.**

### 4.6 Top farming mobs (launch scope) [V-dm stats; V-cbt meso and drop reports]

| Mob | Lv | HP | EXP | Mesos/kill (1 report) | Weak / resist | Best map (spawn points) | Notable drops (votes) |
|---|---|---|---|---|---|---|---|
| Horny Mushroom | 22 | 403 | 41 | 40–48 | — | Ant Tunnel IV (41), III (38) | ores |
| Zombie Mushroom | 24 | 436 | 45 | — | Holy weak, undead | **Ant Tunnel III (61)** | **Claw ATT Intermediate (6)** |
| Fire Boar | 32 | 842 | 62 | — | Ice weak, fire resist | Burnt Land V (26) | **Wolbi (5)**, Arwen's Glass Shoe (7) |
| **Jr. Wraith** | 34 | 982 | 70 | **61–74** | Holy and fire weak, undead | **Line 2 Area 1 (83 of 97)**, Line 1 Area 2 (69) | **Mokbi (12)**, Hat ACC Greater (2) |
| Lupin | 37 | 1,336 | 82 | 68–81 | — | Monkey Swamp I (28) | **Kumbi (6)** |
| Lorang | 38 | 1,714 | 86 | — | Lightning weak | Look-Out Shed (36), Lorang Lorang (35) | Korean Fan (17) |
| Zombie Lupin | 41 | 1,774 | 99 | 74–92 | Holy weak, undead | Monkey Swamp III (31) | Cursed Doll (quest) |
| Rafflesia (new) | 47 | 2,285 | 127 | — | Fire weak | Decayed Tunnel (11) | **Earring LUK Intermediate (4)** |
| Wraith | 48 | 2,350 | 132 | — | Holy weak, undead | Line 2 Area 3 (68), Line 1 Area 4 (59) | — |
| Rotten Mushroom (new) | 56 | 3,520 | 190 | 100–120 | Holy weak | Dilapidated Tomb (14) | — |
| Dark Stone Golem | 58 | 5,428 | 197 | — | Holy weak; fire and poison resist | Sleepy Dungeon V (19) | Tobi (1) |
| Red Drake | 60 | 5,184 | 213 | — | Ice weak | Dangerous Valley II (17) | **Steely (9)** |
| Mushmom (boss) | 40 | 34,440 | 376 | 1,800–2,200 | — | Someone Else's House (1–1.5 h respawn) | **Ilbi (9)**, GFA Intermediate (1), catalysts |
| Zombie Mushmom (boss) | 50 | 53,640 | 568 | 2,250–2,750 | — | Grave of Mushmom (1–1.5 h) | Ilbi, **Hwabi**, Claw ATT Intermediate, catalysts |
| Rotten Mushmom (boss, new) | 60 | 86,400 | 852 | — | Holy and fire weak, undead | Someone Else's Grave (FH, 1–1.5 h) | catalysts, Overall INT Intermediate |

**Meso-rate sketch** [calc; illustration only, not a forecast]: a Lv 50+ Fighter clearing Line 2 Area 1 (about 62 Jr. Wraiths alive at 75% solo capacity) at an assumed 1,500–3,000 kills/h × 67 mesos × drop chance (reported 100%, unverified; assume 60–100%):
- gross ≈ **60k–200k mesos/h**;
- minus MP ≈ 4–12 mesos/kill (6k–36k/h);
- plus Mokbi and ore drops.

**Measure this on day 1.**

### 4.7 Market thesis: tested

| Part of the spec's thesis | Verdict | Why |
|---|---|---|
| Founders hold the meso supply on Oct 21 | **True, briefly** | The meso stock then grows fastest after Oct 21 as the larger F2P population farms, offset by heavy NPC sinks (Lesser scrolls, crafting fees, potions, storage). Expect mild inflation over weeks. |
| Common stars fall | **Mostly N/A** | **Subi and Wolbi are pinned** between NPC buy and sell-back prices (500/250 and 1,000/500). Mokbi and Kumbi probably soften after founders out-level them. |
| Common scrolls fall | **Reframe** | Weapon and armor **Lessers are capped by NPCs** for everyone from day 1, so Intermediate/Greater defensive scrolls have little upside. Greater weapon scrolls get a large quest supply (3 per character). |
| Rare items rise | **Conditional** | Ilbi, Hwabi, Steely and Tobi are boss-limited or have few in-scope sources: hold. **GFA and Overall stat scrolls face a "cap event"** when the first citizens reach grade 9 or 7 (best case late Oct to early Nov). Sell before that. |
| F2P pot demand is a trade | **No** | Potions are unlimited at fixed NPC prices. Elixirs have cooldowns. |

**Sell to founders during Founder's Access:**
- Greater (10%) weapon scrolls (quest supply keeps growing).
- Mokbi and Kumbi beyond what the launch character will use.
- Jane and Blackbull quest materials, and **Mushmom Spore** (week 2, when founders hit Lv 44–48 together).
- Intermediate/Greater defensive scrolls (Tulcus caps them at 15k).

**Hold into launch:**
- Ilbi, Hwabi, Steely and Tobi (or keep them for an Assassin launch character).
- GFA/GFMA scrolls and GFA'd gloves; Overall stat scrolls and scrolled Sauna Robes. **Sell before grade-7/9 citizens appear.**
- Earring INT, LUK, DEX and STR scrolls; Chaos scrolls.
- High-level weekly-donation ETCs: Drake Skull, Tortie Shell, Cold Eye Tail, Lorang Claw, Ligator Skin, Curse Eye Tail.

**Buy right after Oct 21:**
- Crafting inputs that F2P players dump for cash: Leather, Garnet and Black Crystal ore, Jr. Necki Skins, Pig's Ribbon, Animal Fur.
- Mis-priced low-mob scrolls.
- Mokbi and Kumbi only after a real collapse.

**Risks to every call:**
- Launch values drift from the COT2 datamine.
- Drop rates are unknown.
- The citizenship contribution rule decides when the cap events arrive.
- Nexon could add trade gates or taxes (China did, then reversed it).
- Hired Merchant availability is [?].
- Dupes or rollbacks.
- Bots.
- The founder-to-F2P population ratio is unknown.

The buy and sell rules, written relative to prices you observe, go in Phase 3 (`02_market_playbook.md`).

---

## 5. Differences from legacy GMS (consolidated)

| Area | Legacy [B] | Classic |
|---|---|---|
| Classes | Explorers, then Pirates (2007) | 4 Explorer classes only, 10 2nd jobs [V-off/V-dm] |
| Job advancement | Mage Lv 8 / 20 INT; others Lv 10 plus a stat requirement | All Lv 10, no stat requirement [V-off/V-dm] |
| Starting stats | Dice roll | Chosen: 4 each + 9 [V-cbt] |
| HP/MP growth | Random; INT adds MP; HP washing | Fixed per level; INT gives no MP; no washing [V-cbt] |
| AP/SP reset | 1 point per scroll | Full reset [V-dm] |
| Crit | Hands stat; class crit skills strong | Base 5% / +20%; class crit skills weaker [V-dm] |
| Elemental weakness | 1.5× | 1.25× (1.5× "enhanced") [V-dm] |
| Warrior | Endure; PG/HB at 2nd; Rush at 4th; SB 6 targets | No Endure; PG/HB at 3rd; **Rush at 2nd**; SB 4; Bleed; new crit passives [V-dm] |
| Thief | Meso Up (Hermit); Endure; strong Critical Throw | No Meso Up; Critical/Nimble Recovery; Steal buff; weaker Critical Throw [V-dm] |
| Bowman | Blessing of Amazon; PK at 2nd; Arrow Bomb 6 targets | No BoA; PK at 1st; Arrow Bomb 4; Amazon's Judgement [V-dm] |
| Magician | Energy Bolt 55; Holy Arrow single; Poison Breath single | Energy Bolt 130; Holy Arrow 3×; Poison Breath 4 targets; MG toggle [V-dm] |
| Scrolls | 10/30/60/70/100% sets; Gloves DEX, Helm INT, etc. | Lesser/Intermediate/Greater/Chaos; **NPC-sold 100%**; different stat set [V-dm] |
| Elixirs | 50%, no cooldown | 35%, **30 s cooldown**; Elixir sold at citizenship grade 10 [V-dm] |
| Storage | ~4 slots, +4 per coupon, fees varied by town [B?] | Start [?], +5 per coupon up to 150, flat 100 per deposit [V-dm] |
| Shops | FM-only stores; Hired Merchant | Store Permit usable in fields; HM 24 h, mailbox returns [V-dm/V-off] |
| Pets | Meso Magnet / Item Pouch equips | Paid Auto Move and Auto HP/MP skills [V-dm] |
| Party bonus | grew with size [B?] | +10/20/30%, capped at 4 members [V-cbt] |
| KPQ | Lv 21–30, one party per channel | Lv 21+, no upper limit, Channel 1, multiple parties [V-cbt] |
| Mobs | v83 stats | Many HPs changed; Mushmom Lv 40; EXP set by level [V-dm] |
| New content | — | Forgotten Hollow, citizenship, 6 crafting professions, Leaf Points [V-dm/V-off] |
| Movement | Speed 100 = 125 px/s | Speed 100 = 150 px/s; i-frames 1.5 s [V-cbt/V-off] |

---

## 6. Open questions (ranked by impact)

Each one goes on the launch-day checklist in Phase 2 (`05_launch_day_verification.md`).

| ID | Question | Why it matters | Where to update |
|---|---|---|---|
| Q1 | **Mesos per kill and meso drop chance** (Jr. Wraith, Horny/Zombie Mushroom, Lupin, Fire Boar) | Decides absolute mesos/h and the AoE-vs-single-target ranking | §1.1, §4.6, route |
| Q2 | **Level cap** (50 or 70?), and does EXP stop at the cap? | Route 51–70; citizenship grade 9 needs Lv 52 | A1, §3.5 |
| Q3 | Character slots per account and per world; number of worlds; do F2P players share founders' world? | Bank/mule plan; selling to F2P | §3.2 |
| Q4 | Starting storage and inventory slots; withdrawal and meso-deposit fees; can untradeable items be stored? | Dual-character ops | §3.3 |
| Q5 | Cash Shop launch prices: pet and pet skills, Store Permit, **Hired Merchant (sold?)**, slot coupons, AP/SP reset | Cash Shop buy rules; overnight selling | §3.6 |
| Q6 | Trade tax, trade level or account-age gates, meso cap | Market playbook | §3.4 |
| Q7 | Citizenship: does contribution reset on promotion? Do VIP dailies add contribution? Is the weekly ETC per player? | Timing of GFA and robe cap events; Wolbi | §3.8, §4.7 |
| Q8 | Two Classic clients allowed? Multiple accounts? | Daily schedule | §3.7 |
| Q9 | Did launch skill and item values change from COT2? (Check meowdb's changelog header; it's 2026-08-04 now) | Census | §2 |
| Q10 | Party EXP split rules and level range; loot ownership timer | Leveling with friends | §3.5 |
| Q11 | KPQ daily limits; is it still Channel 1 only? | Route 21–30 | §3.5 |
| Q12 | Whether quest-reward scrolls and quest items (Cursed Dolls, Mushmom Spore) are tradeable | Sell list | §4.1, §4.7 |
| Q13 | Steal's loot pool (Bandit) | Bandit MGI | §2.5 |
| Q14 | Does El Moth need Forgotten Hollow access? | Early access to weapon Lessers | §4.1 |
| Q15 | How are Leaf Points earned at launch, and are the earning items tradeable? | Meso-to-cash route | §3.6 |
| Q16 | Natural HP/MP regen; does Improved MP Recovery's +20% apply to food? | Upkeep math | §2 |
| Q17 | What's the "brand-new content" at Grand Launch? (Maple Fest is Oct 17) | Everything | §3.1 |

---

## 7. Data-quality notes

- **The datamine is a test build.** Several values changed between COT1 and COT2: claw ATT −40–50%, Claw Lesser price 20k→50k, Chaos stats, Work Gloves DEF, Rush, Final Attack. Expect some changes at launch. The updater watches meowdb's changelog for a new snapshot date.
- **Hours estimates** use the agents' "cumulative EXP including the current row" values (e.g., 644,337 for Lv 30). The EXP to *reach* level N is actually row N−1, so the hour estimates are about one level conservative.
- **meowdb's DPS rankings** assume a stationary 0-DEF target, every hit landing, no MP limit and no travel. Useful for ranking, not for absolute kill speed.
- **meowdb drop lists marked "MSEA reference"** are legacy MapleSEA tables, not a Classic datamine. Only the "community-sourced" list (with votes) is Classic evidence.

---

## 8. Source keys

| Key | Source | Type | Date |
|---|---|---|---|
| N1 | Classic World FAQ: https://www.nexon.com/maplestory/news/general/45385/classic-world-frequently-asked-questions (text: https://g.nexonstatic.com/maplestory/cms/v1/news/45385) | official | 2026-09-29 |
| N2 | Founder's Access pre-download instructions: https://www.nexon.com/maplestory/news/general/45521/founder-s-access-pre-download-instructions-steam | official | 2026-09-29 |
| N3 | Ossyria Exploration Report (image-only; read via meowdb and the image): https://www.nexon.com/maplestory/news/general/44359/ossyria-exploration-report | official | 2026-08-21 |
| N4 | COT2 release notes: https://www.nexon.com/maplestory/news/general/43432/closed-online-test-2-release-notes | official | 2026-08-03 |
| N5 | Scheduled maintenance Aug 11 (balance pass): https://www.nexon.com/maplestory/news/maintenance/43962/scheduled-maintenance-august-11-2026 | official | 2026-08-11 |
| N6 | COT2 known issues and Hired Merchant fix: https://g.nexonstatic.com/maplestory/cms/v1/news/43808, …/43846 | official | 2026-08-06/07 |
| N7 | COT1 release notes (3 characters/account, Lv 10 1st job, Leaf Points): https://g.nexonstatic.com/maplestory/cms/v1/news/39217; content update (test prices not final): …/40017 | official | 2026-04-14 / 04-21 |
| N8 | Maple Memo: sanctions across both games: https://g.nexonstatic.com/maplestory/cms/v1/news/45230 | official | 2026-09-22 |
| N9 | What activities constitute User Abuse?: https://support-maplestory.nexon.com/hc/en-us/articles/204737315-What-activities-constitute-User-Abuse | official | updated 2026-10-01 |
| N10 | Founder's Packages FAQ: https://support-maplestory.nexon.com/hc/en-us/articles/53268989017620-Founder-s-Packages-Frequently-Asked-Questions | official | updated 2026-10-01 |
| M-DPS | Second-Job DPS Rankings at Lv 70: https://meowdb.com/msclassic/guides/class-dps-rankings | community model | 2026-09-28 |
| M-TIER | Tier list (AoE, damage/MP, EHP): https://meowdb.com/msclassic/tier-list | community model | accessed 2026-10-02 |
| M-DMG | Explaining the damage formula: https://meowdb.com/msclassic/guides/explaining-the-damage-formula | community (datamine-based) | 2026-09-24 |
| M-SKILL / M-CLASS | Skill and class DB: https://meowdb.com/msclassic/skills, https://meowdb.com/msclassic/classes; COT1→COT2 diff: https://meowdb.com/msclassic/skill-changes | datamine (COT2) | 2026-08-04 snapshot |
| M-ITEM | Item DB (scrolls, stars, Cash Shop): https://meowdb.com/msclassic/item-db | datamine (COT2) | 2026-08-04 snapshot |
| M-MOB / M-MAPS | Monsters and maps: https://meowdb.com/msclassic/monsters, https://meowdb.com/msclassic/maps | datamine (COT2) | accessed 2026-10-02 |
| M-MESO / M-DROPS | Community meso and drop reports: https://meowdb.com/msclassic/api/mesos-reports?monsterId={id}, https://meowdb.com/msclassic/api/drops?monsterId={id} | community (COT2 players) | 2026-08-05 → 09-27 |
| M-SHOPS / M-NPC | NPC shops and NPCs: https://meowdb.com/msclassic/npc-shops, https://meowdb.com/msclassic/npcs/all | datamine (COT2 captures) | 2026-08-12 |
| M-CIT | Citizenship: https://meowdb.com/msclassic/citizenship | datamine (COT2) | accessed 2026-10-02 |
| M-Q / M-Q1017 | Quest tracker: https://meowdb.com/msclassic/quest-tracker/all; quiz quest 1017 (Magician at Lv 10) | datamine (COT2) | accessed 2026-10-02 |
| M-CRAFT | Crafting and efficiency: https://meowdb.com/msclassic/crafting, https://meowdb.com/msclassic/crafting/efficiency | datamine + community study | accessed 2026-10-02 |
| M-EXP | EXP table: https://meowdb.com/msclassic/guides/exp-table-level-1-to-100 | community (datamine + testing) | 2026-09-18 |
| M-REL | Release-date guide (cap unpublished, scope): https://meowdb.com/msclassic/guides/maplestory-classic-worlds-release-date | community | 2026-09-30 |
| M-KPQ | KPQ guide: https://meowdb.com/msclassic/guides/kerning-city-party-quest-kpq-guide | community (COT testing) | 2026-08-12 |
| M-SPAWN | Spawn engine: https://meowdb.com/msclassic/guides/spawn-engine-respawn-and-map-capacity | community model | 2026-08-24 |
| M-HPMP | HP/MP gain explained: https://meowdb.com/msclassic/guides/hp-mp-gain-explained | community (COT2 measurement) | 2026-09-14 |
| M-MOV | Speed, jump and movement: https://meowdb.com/msclassic/guides/speed-jump-and-movement | community (COT2) | 2026-09-25 |
| M-CTRL | Controls and settings: https://meowdb.com/msclassic/guides/controls-and-settings | community (COT2) | 2026-09-29 |
| M-REPORT | COT2 meowdb exploration report: https://meowdb.com/msclassic/news/cot2-meowdb-exploration-report | community | 2026-08-16 |
| W-CC / W-DEATH | MapleClassic Wiki, Character creation and Death: https://mapleclassic.wiki/wiki/Character_creation, https://mapleclassic.wiki/wiki/Death | community wiki | 2026-08-30 |
| W-MSW | MapleStory Wiki, Classic World: https://maplestorywiki.net/w/Classic_World | community wiki | 2026-09-05 |
| C1 | mmorpg.com COT1 hands-on: https://www.mmorpg.com/previews/maplestory-classic-world-cbt-preview-2000137829 | press, first-hand | 2026-04-16/17 |
| C2 | mmobomb interview with director Inkwell: https://www.mmobomb.com/an-exclusive-interview-inkwell-about-maplestory-classic-world-his-vision | press interview | 2025-10-27 |
| L-v83 | maplestory.io GMS v83 client data (legacy baseline), e.g. https://maplestory.io/api/GMS/83/mob/{id} | legacy datamine [B] | accessed 2026-10-02 |
| L-AYU | ayumilovemaple legacy skills and formulas: https://ayumilovemaple.wordpress.com/2009/09/06/maplestory-formula-compilation/ | legacy [B] | 2008–2009 |
| L-WB | Wikibooks MapleStory guides (pre-BB): https://en.wikibooks.org/wiki/MapleStory | legacy [B] | various |

Not used (unreliable or out of scope): mmoexp, u4gm, ssegold, ggwtb (gold sellers or SEO); finalboss.io (leads only); private-server sources; China (Shengqu) Classic rules.
