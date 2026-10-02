# Founder's Access Route: Ice/Lightning Wizard (farmer), plus the Assassin plan

Version 0.6 · 2026-10-02. Tags and source keys are as in `00_classic_world_verified_intel.md`.
- **[V-dm]**: COT2 client datamine (meowdb, cross-checked with maplestory.io `MCW/CBT2` where noted). It may change at launch.
- **[V-cbt]**: community test reports (meso reports, voted drops).
- **[model]**: a community model (meowdb's Training Advisor, hit formula, damage formula), or the review's I/L break-even model.
- **[calc]**: my arithmetic, with inputs shown.

**Changed in 0.6 (read first).** You chose the **I/L Wizard** as the farmer (Oct 2). This file was rewritten for it; the Fighter route is in git history (commit 94f4082). The Oct 2 review (`review/REVIEW_2026-10-02.md` in the parent folder) tested the four reasons you gave. Three of them don't hold in Classic data, so this route is built on the one that does:

| Your reason | Verdict | What it changes here |
|---|---|---|
| 1. Mages bypass accuracy | **Doesn't hold.** Every offensive spell uses the same hit check as physical attacks; a miss still costs the MP and the cast [model M-ACC; M-DMG guide 2026-09-24]. Mob levels were also off: Evil Eye is Lv 27, Jr. Wraith 34 (Wraith is the Lv 48 mob) [V-dm]. | §7 has an accuracy table. Never farm more than 1–2 levels above a mob without a Sniper Potion. |
| 2. Vendor equips at 15k–45k each | **Partly.** More kills do mean more drop rolls. But the datamine's top equip sell price is 38,000 (a Lv 70 shield). Equips that Lv 20–50 mobs drop sell for **3k–9k typically**; the best voted drop on your farm mobs is Black Napoleon at 13,200 [V-dm item-db; V-cbt votes]. Scrolls sell to NPCs for 1 meso, so they're income only when sold to players. Equipment drop **rates** aren't published. | §0 shows equipment as a separate sensitivity row. Measure it on day 1 (V-39). |
| 3. Vertical maps avoid congestion | **Doesn't hold.** Thunder Bolt can't be cast mid-jump (only Heal can, among mage skills) and hits a 340×140 px band around you, about one platform; mobs on a higher platform are out of range [V-dm skill page; M-JUMP guide]. Across 111 maps, platform count doesn't predict Thunder Bolt targets; horizontal density does [model, review T12]. Ant Tunnel III and the subway are layered, not flat. | Maps are picked by **mobs per cast, magic DEF and accuracy**, with low-congestion alternates in every bracket. |
| 4. I/L pulls ahead at Lv 48–65 | **Holds in meowdb's model.** The Training Advisor gives I/L about 1.8–2.2× the Fighter's EXP/min at Lv 50–70 [model]. Two conditions: it assumes every cast hits all 6 mobs, and it needs a level cap of 60+ (unconfirmed, V-10). | Day-1 checks count Thunder Bolt targets per cast (V-40). |

**The cost of the switch, stated once** [calc, review T5/T6/T11]: a Fighter reaches efficient AoE earlier and pays less for MP. On the same corrected EXP table the Fighter baseline ends Founder's Access around **Lv 57 with ~6.7M** net coin mesos (mid), against **Lv ~51 and ~3.9M** for this I/L route (mid, coin only). Equipment vendoring adds the same per kill to either class. You accepted this for the post-launch years; the route below is built to shrink the gap.

---

## 0. The model behind every number

| Input | Value used | Source / tier |
|---|---|---|
| Play budget | 76 h gross (Oct 6–20); **66 / 69 / 72 h** of grinding after shop sessions, quest turn-ins and the day-1 queue | kickoff profile; review T5-10 |
| Pace Lv 1–30 | Lv 30 at **14–20 h** (mid 17) | COT testers via meowdb EXP table [V-cbt M-EXP] |
| Pace Lv 30+ | The review's I/L model, SP order R (§8): 810 ms casts, 4 targets per Thunder Bolt (×0.85 below TB 16), 2 s walk between packs, real-play factor 0.65, hit chance from the hit formula. Low ×0.8, high ×1.25 EXP/h | [model]; it's 2.5–5× below meowdb's Advisor, which assumes nonstop casting |
| EXP table | Lv 1–49 matches pre-BB and was verified in COT; Lv 50+ is a legacy reference. **The EXP to reach Lv L is the cumulative row L−1** (the 0.5 scripts were one level off) | [V-cbt M-EXP]/[B] |
| Mesos per kill | **2.0 × mob level × drop chance** (spread of single drops 1.7–2.3×) | 22 community reports on 20 mobs, median 2.0× [V-cbt M-MESO] |
| Meso drop chance | low 0.6 / mid 0.8 / high 1.0. Every report says 100%, which looks like a form default | [assumption]; measure it (V-1) |
| MP cost | **1 meso per MP**: Orange **50 mesos for 50 MP** or Lemon 150 for 150. Never Blue Potions (220 for 200 MP). The 150-meso "Orange Potion" restores HP, not MP | [V-dm M-SHOPS] |
| Equipment vendoring | E = p × median NPC sell value of the mob's equip list (Lv 20–30 mobs 4,200; 31–40 4,900; 41–50 6,600). **p is unknown**; 0 / 0.5% / 1% are shown | [V-dm item-db]; p [?] V-39 |

### 0.1 Founder's Access projection [calc: `python calc/il_projection.py`]

| Scenario | Assumptions | Level on Oct 20 | **Net coin mesos** | +0.5% equip drops | +1% equip drops |
|---|---|---|---|---|---|
| Low | Lv 30 at 20 h, 66 grind h, EXP ×0.8, mesos ×0.5 | ~47 | **~1.4M** | 3.2M | 5.1M |
| Mid | Lv 30 at 17 h, 69 grind h | ~51 | **~3.9M** | 7.2M | 10.5M |
| High | Lv 30 at 14 h, 72 grind h, EXP ×1.25, mesos ×1.6 | ~57 | **~8.0M** | 13.0M | 18.0M |

These totals **exclude** item resale (stars, scrolls, ores, quest ETCs; §12) and boss drops (§11). The equipment columns assume you can carry and vendor every drop; at 1% that's 25–35 equips an hour, so it costs town trips and Equip-tab space. **Fighter baseline for comparison** (same corrections): ~Lv 52.5 / 57 / 62 and ~2.1M / 6.7M / 12.2M coin [calc, review T5].

Net mesos per hour ramp like this in the mid case [model]: ~39k/h at Lv 30 (Energy Bolt on Horny Mushrooms), ~60k at Lv 37–38 (Thunder Bolt 2-shots), ~75k at Lv 41–43, ~99k at Lv 46–50, ~112–122k at Lv 51–57.

### 0.2 Day-by-day level target [calc: `il_projection.py`]

| Day | Hours (cum.) | Level: low / mid / high | Milestone |
|---|---|---|---|
| Tue Oct 6 (opens 1 PM CDT) | 4 (4) | 10 / 12 / 14 | 1st job (Ellinia); **Kerning** citizenship at 12; claim and **open** the package |
| Wed Oct 7 | 4 (8) | 17 / 20 / 22 | Jane and the Mushroom; KPQ once at 21 |
| Thu Oct 8 | 4 (12) | 22 / 24 / 26 | Ant Tunnel IV or Dark Cave |
| Fri Oct 9 | 4 (16) | 24 / 27 / 30 | Arwen's Glass Shoe at 29 |
| Sat Oct 10 | 8 (24) | 30 / 32 / 35 | **2nd job (I/L)**; Mithril Wand; start the Secret Book chain |
| Sun Oct 11 | 8 (32) | 33 / 36 / 40 | Thunder Bolt 15–18; Shumi's quests at 35 |
| Mon–Fri Oct 12–16 | 20 (52) | 40 / 44 / 49 | TB 30 at 40; Jr. Wraith 3-shot at 42; Hollow quests |
| Sat–Sun Oct 17–18 | 16 (68) | 44 / 49 / 54 | Sleepy Dungeon IV; Med 20 at 48 |
| Mon–Tue Oct 19–20 | 8 (76) | 46 / 51 / 56 | Farm; sell or hold per `02_market_playbook.md` |

If you're below the "low" column on Sun Oct 11, recheck the real-play factor with the V-36 log and the Thunder Bolt target count (V-40). Don't add hours you don't have.

---

## 1. Lv 1–10: Maple Island, then Lith Harbor (≈2–3 h)

**Goal:** finish the quests fast, keep the AP plan, leave by about Lv 8.

| Map (id) | Mobs: Lv / HP / EXP [V-dm] | Spawns | Max EXP/h (ceiling) |
|---|---|---|---|
| Hunting Ground Middle of the Forest II (000001006) | Snail 1/45/2, Blue Snail 2/51/4, Shroom 3/62/6, Red Snail 4/68/8, Orange Mushroom 8/142/15 | 45 | 94k |
| Dangerous Forest (000001002) | Snail, Blue/Red Snail, **Orange Mushroom ×12** | 34 | 93k |
| Mushroom Garden (000001003) | Shroom ×23, Snail, Orange Mushroom | 35 | 81k |

- **Weaknesses:** none relevant yet; you have no spells before Lv 10.
- **Quests** [V-dm]: Sam's Suggestion (30 EXP, potions); Lucas's letter (hat); **Mai's Training** (170 EXP, 150 mesos); **Biggs's Collection** (a beginner weapon); **Pio's Recycled Goods** (Green Relaxer chair); Rain's Maple Quiz (245 EXP). Quests take you to about **Lv 8**. Then take the boat at **Shanks, Southperry** to Lith Harbor (fare [?] V-31).
- **Lith Harbor to Lv 10:** Lith beginner quests and **Phil's Call** (Lv 8, prerequisite for Jane). Grind **L Forest I** (010003020): Ribbon Pig Lv 10 ×21. Avoid its single Iron Hog (Lv 28).
- **1st job: Magician at Lv 10**, with Grendel the Really Old in **Ellinia**. No INT requirement [V-dm M-Q1017].
- **Then claim the Founder package from the mailbox and open it right away.** It can't be opened on Maple Island, and **once claimed you have 30 days to open it** [V-off N10, CMS 44134].
- **Mesos [calc]:** EXP to Lv 10 is 3,347; expect 2–5k mesos from kills plus ~300 from quests.
- **Pick up:** Orange Mushroom Cap, Red/Blue Snail Shell, Mushroom Spore (citizenship weekly at grade 1).

---

## 2. Lv 10–20: Magician (≈3–4 h)

**Goal:** Energy Bolt to 20, Improved MP Recovery 1 early, **Kerning** citizenship at 12, Work Gloves.

| Map (id) | Mobs: Lv / HP / EXP / M.DEF / weak [V-dm] | Spawns | Ceiling EXP/h | Notes |
|---|---|---|---|---|
| L Forest I (010003020) | Ribbon Pig 10/172/19/0 (0 MP) | 73 (21 pigs) | 334k | Safe; avoid the Iron Hog |
| **Line 1 <Area 1> (010003061)** | **Bubbling 15/259/28/M.DEF 10, lightning weak** | 64 | 640k | Kerning subway; touch 67–91 is risky at Lv 11–15 |
| Tree Dungeon, Forest Up North IV (010002075) | Green Mushroom ×31 (14/233/26), Slime ×13 | 44 | 344k | Close to Ellinia |
| Subway Transfer Area / Dangerous Steam | Stirge 20/296/37 (flying) | — | — | meowdb's I/L pick around Lv 20 [model] |

- **Estimate [model]:** Energy Bolt is single target, 1 cast per kill on these mobs once EB is ~10+. Magician Advisor: 811 EXP/min at Lv 15 and 1,370 at Lv 20 (nonstop) [model]. At r 0.55–0.80 that's **27k–66k EXP/h**, about 1,000–2,300 kills/h; mesos/kill = 2.0 × 15 × (0.6–1.0) = **18–30**; **gross ~20k–70k/h**. MP use 15–27k MP/h, roughly what the kills pay [calc, review T11]. Treat Lv 10–30 as break-even.
- **Energy Bolt beats Magic Claw.** Same expected damage at every level (90 + 2/lv vs 2 × (45 + 1/lv)); Magic Claw costs 20–25% more MP and an extra SP [V-dm, calc].
- **Quests** [V-dm]:
  - **Nella chain (Kerning, Lv 10):** Don Hwang's Request (costs 1,000 mesos; 10 Orange Mushroom Caps + 10 Pig's Ribbons) → Shumi's Request → **Andre's Request** (30 Octopus, 20 Octopus Legs + 1 Pure Water at 1,120). Reward: **Work Gloves** (5 slots, tradeable). Keep them: your GFMA base.
  - **Fixing Blackbull's House** (Lv 11): prerequisite for the Lv 48 Blackbull scroll quest.
  - **I Need to Find My Daughter 1/2** (Lv 11): prerequisite for Arwen and the Alligators quests.
  - **Kerning citizenship** (Lv 12, Roxy): do the daily every play day (§13).
  - **Pia and the Blue Mushroom** (Lv 16): random Hat Accuracy scroll. **Use it** (+ACC helps a mage, §7).
  - **Mother's Gold Watch** (Lv 18): earrings. **Talking to Stan** (Lv 18).
  - **Jane and the Mushroom** (Lv 20, Lith; needs Phil's Call): 30 Blue + 30 Horny kills, 15 + 15 caps → 2,021 EXP, 585 mesos and **1 of 14 Intermediate weapon scrolls (7.1% each, includes Wand and Staff MATK)** [V-dm].
- **Pick up:** Octopus Leg, Mithril Ore (Bubbling), Bubbling's Huge Bubble, Blue Mushroom Cap, **any scroll, ever**.

---

## 3. Lv 21–30: Magician, Energy Bolt (≈8 h; testers took 8–9 h for Lv 20–30)

**Goal:** Energy Bolt farming on low-M.DEF mushrooms, KPQ once, scroll and cape quests, **2nd job at 30**. You have no Thunder Bolt or Teleport yet.

| Map (id) | Mobs: Lv / HP / EXP / M.DEF [V-dm] | Spawns | Congestion | Why |
|---|---|---|---|---|
| **Dark Cave (010005064)** | Stirge 20 ×35, Horny Mushroom 22/403/41/0 ×9, Zombie Mushroom 24/436/45/15 ×7 | 51 | **low** | Best low-traffic EB map in the review's ranking [model] |
| **Ant Tunnel IV (010005063)** | Horny ×41, Zombie ×23 | 64 | medium | Same mobs as Ant Tunnel III with fewer players |
| Ant Tunnel I (010005060) | Horny ×15, Zombie ×11 | 26 | low | Overflow |
| Land of Wild Boar II (010004091) | Wild Boar 25/510/46/M.DEF 15 ×23 (0 MP) | 23 | low | Perion side |
| (Ant Tunnel III, 010005062) | Zombie ×61, Horny ×38 | 99 | **very high** | Best density, but every founder will be here |

- **Accuracy:** Horny/Zombie Mushrooms need 44–47 ACC, which you pass from about Lv 22. Evil Eye (Lv 27) needs 54 [model M-ACC].
- **Estimate [model, review T11]:** at Lv 25–30, Energy Bolt 20 kills a Horny Mushroom in 1–2 casts (at Lv 30 its minimum hit 405 beats 403 HP). About 1,450 kills/h mid; gross ≈ 51k/h, MP ≈ 15k/h → **net ≈ 36–39k/h**; low/high 18k–59k.
- **Quests** [V-dm]:
  - **Proof of Companionship** (Lv 21, Lakelis, Kerning; one KPQ clear): 2,193 EXP, 614 mesos, random Intermediate Earring stat scroll.
  - **Arcon's Blood** (Lv 21, Manji, Henesys): 75 Zombie Mushrooms → 2 × 2,193 EXP.
  - **Cutthroat Manny's Request** (Lv 22): 50 Evil Eyes → Mithril War Boots (warrior boots; sell or keep for a friend).
  - **Dr. Faymus's Request** (Lv 22): 40 Horny + 40 Jr. Necki → 30 White Potions.
  - **Stranger's Identity** (Lv 23, Jane Doe, Kerning): 50 Zombie Mushrooms → Old Raggedy Cape.
  - **Sabitrama and the Diet Medicine** (Lv 25) → Overall DEF scroll (Intermediate or Greater). **Sabitrama's Anti-Aging Medicine** (Lv 25) → Star Rock (keep for Hero's Gladius at 50; NPC sell 4,000).
  - **Arwen and the Glass Shoe** (Lv 29, Ellinia; repeatable): 1 Glass Shoe (Fire Boar) → 3,037 EXP, 848 mesos, **Piece of Ice or Fairy Wing** (wand-crafting inputs).
- **2nd job:** **Ice/Lightning Wizard at Lv 30** (Grendel, Ellinia) [V-dm].
- **Wand at 30: Mithril Wand** (Flora, Ellinia; 22,000; 55 M.ATK; needs 20 LUK) [V-dm]. Budget it from your Lv 20–30 kills.
- **Pick up:** **Claw ATT Intermediate** (Zombie Mushroom, 7 up / 1 down votes; keep for the Assassin), Spear ATT Greater (Zombie), Charm of the Undead, Horny Mushroom Cap, Evil Eye Tail, ores, and the equips in §12.

---

## 4. Lv 31–40: I/L, Thunder Bolt rush (≈20–22 h of play)

**Goal:** Thunder Bolt to 30 by Lv 40 (3 SP a level), MP Eater 1 from Lv 30, the Sauna Robe chain, Shumi's 10k mesos.

**How Thunder Bolt grows** [V-dm skill page]: Basic Atk 40 at skill Lv 1 → 70 at 30 (+1 per level); MP 20 → 40; 6 targets at every level; hit box **300×100 px to skill Lv 15, 340×140 from Lv 16**; 810 ms cast, ground only. Below about 2 mobs per cast it loses to Energy Bolt, so keep EB 20 on single mobs.

**Break-even points [model, review T11; Mithril Wand, no Meditation, 90% kill chance]:**

| Mob (Lv / HP / M.DEF) | 3-shot with TB | **2-shot with TB** | 1-shot |
|---|---|---|---|
| Horny Mushroom (22 / 403 / 0) | Lv 34 (TB 13) | **Lv 37 (TB 22)** | Lv 46 (TB 30 + Med 15) |
| Zombie Mushroom (24 / 436 / 15) | Lv 35 (TB 16) | **Lv 39 (TB 28)** | Lv 52 |
| Evil Eye (27 / 606 / 20) | Lv 38 (TB 25) | Lv 43 (TB 30 + Med 6) | — |
| Jr. Wraith (34 / 982 / 0) | **Lv 42** | Lv 51 (Med 20) | — |
| Curse Eye (33 / 1,001 / 0) | Lv 42 | Lv 52 | — |
| Lupin, Lorang, Glowshroom, Raffle | Lv 52–59 | — | — |
| Wraith, Clang, Drakes, Malady, Dark Stone Golem | none by Lv 60 | — | — |

So the I/L farms **low-HP, low-M.DEF mobs below its level** for all of Founder's Access. Thunder Bolt never one-shots anything above Lv 27 before Lv 60 with NPC wands.

| Map (id) | Mobs | TB targets (best spots) | Congestion | When |
|---|---|---|---|---|
| **Ant Tunnel IV / Dark Cave** (above) | Horny, Zombie | 2.6 | medium / low | Lv 31–39: EB until TB ~16–19, then TB |
| West Rocky Mountain IV (010004023) | Wild Boar and others | 3.2 | low | Lv 35–40 alternate |
| East Rocky Mountain VI (010004055) | — | 3.7 | low | Lv 35–40 alternate |
| The Cave of Evil Eye III (010005073) | Evil Eye 27/606/50/M.DEF 20 ×38 | 3.0 | high | From Lv 38 (3-shot) |
| Line 1 <Area 2> (010003063) / Line 2 <Area 1> (010003066) | **Jr. Wraith 34/982/70/M.DEF 0** | 3.5 / 2.6 | very high | From Lv 38–42; 100% hit from Lv 35 |
| The Burnt Land (010004111–114) | **Fire Boar 32/842/62/0, ice weak, 0 MP** | 2.7 | low | Fallback; MP Eater gets nothing |

- **Estimate [model, review T11]:** mid net **47k/h at Lv 36 → 61k at 38 → 65k at 40**, about 2,100–2,600 kills/h. MP use with Thunder Bolt is 44k–52k MP/h at r 0.65 (35–40k/h of potions after regen and MP Eater). Low/high: 15k–108k/h.
- **Accuracy (§7):** Jr. Wraith 96% at Lv 35 and 100% from 36; Lupin and Lorang 100% from about Lv 38–40; Zombie Lupin only 77% at Lv 40.
- **Quests** [V-dm]:
  - **Mr. Wetbottom's Secret Book chain** (Lv 32, 9 steps): 30 Lupin's Bananas, 50 Curse Eye Tails, 10 Pig's Heads (source [?] V-33), 1 refined Diamond. Rewards: 29,289 EXP, 7,862 mesos, 40 Blue Potions, **Sauna Robe** (10 slots, +1 all stats, tradeable; NPC sell 5,400).
  - **Shumi's Lost Coin / Roll / Sack of Cash** (Lv 35; needs Proof of Companionship): 3 × 4,162 EXP, then 1,023 + 1,023 + **10,000 mesos**, 30 Blue Potions, **30 Mana Elixirs**.
  - **Collecting 50 → 200 Cursed Dolls** (Lv 36, Rowen, Ellinia): Zombie Lupin (M.DEF 30). **Start it at Lv 42+**, when you hit Zombie Lupin reliably. 150 dolls: GFA60 or GFMA60 (50/50).
  - **Forgotten Hollow opening** (Lv 39): Tracing the Resonance (Hat ACC scroll; use it) and **Welcome to the Hollow: a pick-one Greater scroll for your class's weapon, so Wand or Staff MATK Greater** [V-dm M-Q].
- **Pick up:** Mokbi (Jr. Wraith), Kumbi (Lupin), Lupin's Banana, Curse Eye Tail, Tablecloth, Hat ACC Greater (Jr. Wraith), Topwear MP Greater (Curse Eye).

---

## 5. Lv 41–50: I/L, Meditation and MP Eater (≈25–30 h of play)

**Goal:** Meditation 20 by Lv 48 (+25 M.ATK; needs MP Eater 3), the scroll and Elixir quests, the first Teleport points from 48. If the cap is 50 (V-10), this bracket is the endgame.

| Map (id) | Mobs / casts to kill | TB targets | Congestion | Why |
|---|---|---|---|---|
| **Sleepy Dungeon IV (010005053)** | **Curse Eye 3 casts**, Jr. Necki 1; Dark Stone Golem 33 casts at 8% hit | 4.4 | **low** | Best low-traffic I/L map. **Skip the Golems** (M.DEF 30, 150 MP, touch ~48% of your HP) |
| Sleepy Dungeon III / V (010005052 / 054) | same mix | 4.2 / 5.9 | high / very high | Denser; contested |
| Line 1 <Area 2> / Line 2 <Area 1> | Jr. Wraith 3 casts from Lv 42 | 3.5 / 2.6 | very high | 0 M.DEF; Mokbi |
| Tree Dungeon, Forest Up North VI (010002080) | Curse Eye ×17 | 2.6 | low | Quiet alternate |
| The Burnt Land IV (010004114) | Fire Boar 3 casts | 2.7 | low | Glass Shoes; Wolbi |
| The Cave of Evil Eye III | Evil Eye 2 casts from Lv 43 | 3.0 | high | Evil Eye Tails |
| Ant Tunnel IV (late 40s) | Horny 1-shot from Lv 46 | 2.6 | medium | Highest net/h in the model at Lv 46–50 (~99k) |

- **Estimate [model, review T11]:** mid net **75k/h at Lv 41–43 → 80k at 45 → 99k at 46–50**, 2,600–3,300 kills/h. Potions ~18–40k/h. Low/high: 34k–151k/h.
- **Accuracy:** Wraith needs 113 ACC at Lv 45 and 101 from Lv 48; Clang 110 → 95. A pure-INT I/L has ~92 ACC at 45 and ~100 at 50, so **Wraith and Clang wait until Lv 48–50** (a Supreme Sniper Potion, +7 ACC, closes the last gap) [model M-ACC].
- **Quests** [V-dm]:
  - **Forgotten Hollow chains** (Lv 39–50; 84,249 EXP and 19,573 mesos in total): The Road Back Home (43, Earring scroll), Matters of the Heart (45, Cape ACC scroll), A Heart of Stillness & Wood (50; 30 Cursed Dolls + 20 Duskmander Tails), The Sage's Burden (50), Myra's Old Friend (49, 15 Mana Elixirs).
  - **Jane's First / Second / Final** (Lv 44): 10 Elixirs; 15 Power Elixirs (needs 1 Mushmom Spore); then **one random gloves scroll: ATT Int / ATT Greater / MATK Int / MATK Greater (25% each)**. Jane's Final is the **only** source of Gloves MATK scrolls; no mob drops one [V-dm, review T12].
  - **John's Present** (Lv 45) → Dark Knuckle (warrior gloves; sell). **Luke's Wish to Travel** (Lv 46).
  - **Building a New House For Blackbull** (Lv 48) and **Taking Out the Alligators 1** (Lv 48) → each a **pick-one Wand/Staff MATK Greater** for a Magician. Claw ATT Greater is not available to you; the Assassin gets its own copies.
  - **Citizenship weeklies** (Kerning list, §13).
- **Pick up:** Medicine With Weird Vibes (Wraith), Drake Skull, Dragon Skin, Black Crystal Ore, Cursed Doll, Earring LUK Intermediate (Rafflesia), Tortie Shell.

---

## 6. Lv 51–70: I/L (only partly reachable before Oct 20; cap unconfirmed)

From Lv 51 you add MP Eater to 20 and Teleport to 20 (§8). Teleport costs **55 MP at skill Lv 1** and 15 MP only at 20, and it's ground-only [V-dm], so it's a mobility tool from about TP 10, not before.

| Map (id) | Mobs | Congestion | Why |
|---|---|---|---|
| **Sleepy Dungeon IV / III / V** | Curse Eye 2 casts at 51+; Tobi from Dark Stone Golem (1 vote) | low / high / very high | Still the best I/L earners to Lv 70 in the review's model (576k–781k gross at 1% equip drops) |
| **Lorang and Clang (010007030/031)** | **Clang 49/2,899/137/M.DEF 15, lightning weak**; Lorang 38, lightning weak | medium | 4.6 targets per cast; equip list averages 9.7k [model, V-dm] |
| Line 1 <Area 3> (010003064), Line 2 <Area 2/3> (010003067/068) | Wraith 48/2,350/132/**M.DEF 0** | high | 100% hit from Lv 48–50; Medicine With Weird Vibes |
| The Valley of Death (010006031) | Rafflesia etc. | medium | Earring LUK Intermediate |
| Golem's Temple III (010001105) | — | low | Quiet alternate |
| Lv 61–70: Hot Sand (010007040), Line 1 <Area 4> (010003065), Perilous Descent III (010006110), Drake's Meal Table (010005090) | — | medium–high | On-level alternates; meowdb's Lv 70 I/L pick is Line 1 <Area 2> [model] |

- **Avoid as an I/L:** Dark Stone Golem (M.DEF 30, 5,428 HP, fire and poison resist; net negative), Malady (M.DEF 50, ice resist), Drakes and Cold Eye (ice resist; and Drakes 15 M.DEF with 3,218 HP) [V-dm; model].
- **Estimate [model, review T11]:** mid net **~112–122k/h at Lv 51–57**, ~126–132k at 58–59. Equipment at 1% per kill roughly doubles gross on the Sleepy Dungeon maps [model, review T12].
- **Quests:** A Heart of Stillness & Wood and The Sage's Burden (50); **Hero's Gladius chain** (50; Star Rock, Piece of Ice, Ancient Scroll from Dark Stone Golem, Flaming Feather from Red Drake): rewards EXP and Hero's Gladius or Skull Earrings. Citizenship Lv 52 weekly.
- **Pick up:** Steely (Red Drake, ice weak: take Cold Beam first if you farm it), Tobi, Black Crystal, Drake Skull, Dragon Skin, Ancient Scroll, Aquamarine Ore (Clang).

---

## 7. I/L AP plan and accuracy [V-dm wand requirements; model M-ACC, M-DMG]

**Rule:** all AP into **INT**, plus **base LUK only up to your next wand's requirement**. LUK gives half the accuracy of INT (0.118 vs 0.235 ACC per point) and no spell damage, so never add LUK for accuracy. There's no AP into HP or MP in Classic.

| Level | AP | Base INT / LUK at the end | Why |
|---|---|---|---|
| Creation | 4 base + 9 free | **13 INT / 4 LUK** (STR 4, DEX 4) | Put all 9 free points in INT |
| 2–19 | 5 INT (one point a level into LUK from 14–19 until LUK 10) | ~97 / 10 | Lv 20 wands need ~10 LUK [V-dm, review T11] |
| 20 | 5 INT | 102 / 10 | |
| 21–25 | 4 INT, 1 LUK | 122 / 15 | 15 LUK by 25 |
| 26–30 | 4 INT, 1 LUK | **142 / 20** | **Mithril Wand** (Lv 30, 55 M.ATK) needs 20 LUK and 60 INT |
| 31–70 | 5 INT | 342 / 20 at Lv 70 | Stay at 20 LUK unless you get a better wand: **Fairy Wand** (69 M.ATK) needs 30 LUK, **Cromi** (83) 40, Arc Staff 40 (crafted or market [?]) |

Check [calc]: base INT = 12 + 5 × Lv − LUK (all stats start at 4; 9 free points plus 5 a level). Lv 30 with 20 LUK: 12 + 150 − 20 = 142 ✓.

**NPC wands** (Flora, Ellinia) [V-dm]: Wooden 27 M.ATK (3,000), Hardwood 34 (5,000), Metal 41 (10,500), Ice 48 (13,500), **Mithril 55 (22,000)**. Wand Lesser scrolls (+1) cost 25,000 at El Moth.

**Accuracy** [model M-ACC; meowdb formulas and accuracy sim, 2026-10-02]: Magician ACC = floor((1.2 × INT + 2 × Lv + 0.6 × LUK) / 5.1 + 20). Mobs above your level get harder fast (each level adds roughly 3–4 to the ACC you need); being above a mob gives no bonus.

| Your Lv (≈ACC) | Mushrooms, Evil Eye | Fire Boar | Curse Eye | Jr. Wraith | Lupin | Lorang | Zombie Lupin | Wraith | Clang |
|---|---|---|---|---|---|---|---|---|---|
| 30 (69) | 100% | 94% | 78% | 45% | 8% | 28% | 0% | 0% | 0% |
| 35 (77) | 100% | 100% | 100% | 96% | 65% | 82% | 23% | 0% | 0% |
| 40 (85) | 100% | 100% | 100% | 100% | 100% | 100% | 77% | 9% | 17% |
| 45 (92) | 100% | 100% | 100% | 100% | 100% | 100% | 100% | 58% | 65% |
| 50 (100) | 100% | 100% | 100% | 100% | 100% | 100% | 100% | 98% | 100% |

ACC for a pure-INT build with 4 LUK [model, review verifier]; your 20 LUK and gear INT add 1–4 ACC. **Close small gaps** (≤7 ACC) with Henesys's **Supreme Sniper Potion** (+7 ACC, 600 mesos, 15 min; Henesys citizens only [?] V-9) or Hat ACC scrolls from Pia, Tracing the Resonance and Jr. Wraith drops.

**Durability** [V-cbt M-TIER, model]: I/L physical EHP ~5,140 and magic EHP ~5,300 (the Fighter's was ~4,010). Magic Guard (80% to MP) spends MP instead of HP, about 90 mesos per 100 damage taken against 50 on HP. Keep it on; it's the reason boss touches (79–96% of your HP) are survivable.

---

## 8. I/L SP plan [V-dm skill values; model: review T11 break-even, order "R"]

Totals: beginner 9 + 1st job 61 + 2nd job 121 = **191 SP by Lv 70**.

**Beginner (Lv 2–10, 9 SP):** Nimble Feet 3, then Three Snails 3, then Recovery 3.

**Magician (Lv 10–30, 61 SP)** — Energy Bolt 20 / Magic Guard 3 / Magic Armor 8 / Improved MP Recovery 15 / Max MP Increase 15:

| Level | Spend | Running total | Reason |
|---|---|---|---|
| 10 | EB +1 | EB 1 | |
| 11 | EB +2, IMR +1 | EB 3, IMR 1 | IMR 1 already gives the full 1% Max MP per 10 s regen |
| 12–16 | EB +3 each | EB 18 | |
| 17 | EB +2, MG +1 | **EB 20**, MG 1 | 130 Basic Atk, 16 MP |
| 18 | MG +2, IMR +1 | MG 3, IMR 2 | MG 3 opens Magic Armor |
| 19 | IMR +1, MMI +2 | IMR 3, MMI 2 | IMR 3 opens Max MP Increase |
| 20–21 | MA +3 each | MA 6 | |
| 22 | MA +2, IMR +1 | MA 8, IMR 4 | |
| 23–25 | IMR +3 each | IMR 13 | |
| 26 | IMR +2, MMI +1 | **IMR 15**, MMI 3 | +20% MP from potions (permanent saving) |
| 27–30 | MMI +3 each | **MMI 15** | |

Check: 20 + 3 + 8 + 15 + 15 = 61 ✓. Safer variant: IMR 8 / MA 15 (more W.DEF and M.DEF).

**I/L (Lv 30–70, 121 SP):**

| Level | Spend | Running total | Reason |
|---|---|---|---|
| 30 | MP Eater +1 | ME 1 | The best single point: absorbs 3–9k MP an hour, 10–25% of the potion bill |
| 31–40 | TB +3 each | **TB 30** at 40 | Reaches the 2-shot brackets above; 50k/h net at Lv 37 (mid) vs Lv 40–42 for other orders |
| 41 | ME +2, Med +1 | ME 3, Med 1 | ME 3 opens Meditation |
| 42–47 | Med +3 each | Med 19 | +25 M.ATK at max |
| 48 | Med +1, TP +2 | **Med 20**, TP 2 | |
| 49–50 | TP +3 each | TP 8 | |
| 51 | ME +1, TP +2 | ME 4, **TP 10** | Teleport 37 MP / 128 px: now worth using |
| 52–56 | ME +3 each | ME 19 | |
| 57 | ME +1, TP +2 | **ME 20**, TP 12 | |
| 58–59 | TP +3 each | TP 18 | |
| 60 | TP +2, CB +1 | **TP 20**, CB 1 | 15 MP / 150 px |
| 61–69 | CB +3 each | CB 28 | |
| 70 | CB +2, Slow +1 | **CB 30**, Slow 1 | |

Check: ME 20 + TB 30 + Med 20 + TP 20 + CB 30 + Slow 1 = 121 ✓.

**Why not meowdb's order (Cold Beam first)?** Cold Beam first only wins if you can't hold about 2+ mobs per Thunder Bolt. In the review's model the TB-first order reaches Lv 45 after ~35 farming hours (Cold Beam first: ~47) and makes ~1.55M by 30 hours after Lv 30 (CB-first: ~1.23M) [model]. **If V-40 shows fewer than ~2 targets per cast on your maps, switch to meowdb's order: Cold Beam 30 at Lv 31–40, then TB** (SP Reset is a Cash Shop item [?]).

**Variants:**
- **Boss variant (Ilbi from Mushmom):** after Med 20 at 48, put the next points into **Cold Beam** instead of Teleport. Thunder Bolt is weak on a single 34,440-HP boss.
- **Ice-weak farming** (Fire Boar, Copper Drake, Red Drake/Steely): Cold Beam earlier, after Med.
- **Mobility first:** TP 10 straight after Med costs almost nothing in the model (Lv 30→60 in ~99 h instead of ~104).

---

## 9. Launch character: Assassin [V-dm meowdb thief and assassin guides]

**Your decision: Assassin**, levelled with friends from Oct 21. Keep one tripwire: **if both friends pick single-target classes** (Bandit, Assassin, Cleric), the party has no AoE at all until 3rd job. Revisit before Oct 21 (Cleric for support, or a 2nd-job AoE class). Get their picks this week.

- **Creation:** 4 STR / 5 DEX / 4 INT / **12 LUK**. All AP to LUK until Lv 10.
- **Lv 11–15:** 2 DEX + 3 LUK per level. **Lv 16–70:** 1 DEX + 4 LUK per level. DEX tracks claw level.
- **Citizenship:** **Kerning** (Wolbi at grade 3, Overall LUK Lesser at grade 7). Same town as the farmer, so the storage discount works for both at Mr. Hong.

| Lv | Base DEX / LUK | Claw | Skills (running) |
|---|---|---|---|
| 10 | 5 / 57 | Garnier (Manny, 5,000), Subi | Beginner 3/3/3; Lucky Seven 1 |
| 30 | 30 / 132 | **Adamantium Guards** (Manny, 27,600), Wolbi | L7 20 (Lv 18), Keen Eyes 15 (Lv 23), Nimble Body 15 (Lv 27), Disorder 3, Dark Sight 8 = 61 ✓ |
| 40 | 40 / 172 | **Steel Igor** (Manny, 14,100) or Meba (16,500), then Dark Guardian (crafted) | Haste 1, **Claw Mastery 20 (Lv 37)**, Booster 1, Critical Throw 9 |
| 50 | 50 / 212 | Dark Slain (crafted) | **Critical Throw 30 (Lv 47)**, Haste 10 |
| 70 | 70 / 292 | Black Scarab, Tobi/Ilbi | Haste 20, Booster 20, Critical Recovery 20, Drain 11 = 121 ✓ |

**Assassin maps** [V-dm; model]: Lv 13–30 Subway Transfer Area and Dangerous Steam (Stirge, flying); Lv 30–40 Ant Tunnel II/IV; Lv 41–45 Forgotten Entrance III or Monkey Swamp III; Lv 46–55 Line 2 Wraiths; Lv 55+ Monkey Forest II / Forgotten Entrance II.

Party EXP split rules are undocumented (V-18). With one client, the I/L can't be in the party at the same time as the Assassin.

The Hunter plan (0.5 fallback) is retired; `03_hunter_funding_checklist.csv` stays only as an archive.

---

## 10. Kerning PQ vs solo grinding (Lv 21–30)

| | **Kerning PQ** | **Solo (Magician, Energy Bolt, Dark Cave / Ant Tunnel IV)** |
|---|---|---|
| Entry | Exactly **4 players**, Lv 21+, **Channel 1 only**, 30-min timer [V-off N4, N7; V-cbt M-KPQ] | Any channel |
| EXP | Mob EXP in a run is **2,506 for the whole party** (22 Ligators × 68 + 6 Jr. Necki × 80 + 3 Curse Eyes × 94 + King Slime 248) [V-cbt; calc]. Per member: 2,506 ÷ 4 × 2–6 runs/h = **0.6k–3.8k EXP/h** (up to 4.9k with the +30% party bonus). Stage-clear EXP is unknown [?] | **≈40k–60k EXP/h** at Lv 25–30 [model, review T11] |
| Mesos | Whether PQ mobs drop mesos is [?] | ≈36–39k/h net (mid) |
| Items | 1 Companion's Magic Box per clear (untradeable; odds unknown); **Squishy Shoes** (Lv 28, +1 all stats, 5 slots, tradeable) from King Slime | Normal drops |
| Break-even | Stage-clear EXP would need to be about **10k–20k per member per run** for KPQ to match solo [calc: (40k − 3.8k) ÷ 2–4 runs] | — |

**Verdict:** **run KPQ once** for Proof of Companionship (2,193 EXP, 614 mesos, an Intermediate Earring stat scroll, and the prerequisite for Shumi's 10k-meso quest). Re-run only if V-19 shows big stage-clear EXP or to hunt Squishy Shoes.

---

## 11. Bosses as farming targets (I/L)

| Boss | Lv / HP / M.DEF / weak [V-dm] | Where | Respawn | I/L readiness [model, review T12] | Drops worth it [V-cbt votes] |
|---|---|---|---|---|---|
| **Mushmom** | 40 / 34,440 / 15 / none; touch ~630 | Someone Else's House (010001005), via Pig Park II | 1–1.5 h | From **Lv 45 with Cold Beam** (~45 casts, ~1 min, 850–1,000 MP). Touch is 79–89% of your HP: **Magic Guard on**. With order R (no Cold Beam until 60) it's slow; use the boss variant (§8) if you want Ilbi | **Ilbi (+9)**, Mushmom Spore, Elixir, GFA Intermediate (+1), Shield DEF Intermediate (+4) |
| **Zombie Mushmom** | 50 / 53,640 / 20 / holy weak, undead; touch ~770 | The Grave of Mushmom (010005078) | 1–1.5 h | From **Lv 50** (62 Cold Beam casts, 100% hit; only 49% hit at Lv 45). Touch is ~96% of HP: Magic Guard and mana potions | Ilbi (+3), Scroll Crafting Catalyst, Earring Crit Damage Int/Greater (+2). **Hwabi: 0 up / 1 down, unconfirmed** |
| **Rotten Mushmom** | 60 / 86,400 / 10 / holy and fire weak | Someone Else's Grave (Forgotten Hollow) | 1–1.5 h | Lv 60+ only (8% hit at Lv 50); its magic hits reach 106% of your HP. **Not in Founder's Access** | Catalysts, Overall INT Intermediate (+1) |

**Boss loop:** note the channel and time after each kill and check back 60–90 min later while farming nearby. A phone timer you set by hand is fine; **never** a script or a tool that automates anything.

---

## 12. Loot rules (I/L)

| Category | Rule | Why |
|---|---|---|
| **Any scroll** | Always loot. **Never** NPC-sell (1 meso) | `02` decides sell vs hold. Wand/Staff MATK and Gloves MATK: keep for yourself first |
| **Throwing stars** (Mokbi, Kumbi, Tobi, Steely, Ilbi) | Always loot; keep for the Assassin or sell per `02` | NPC sell 1,000 / 1,500 / 2,500 / 10,000 / 20,000 per set [V-dm] |
| **Equipment** | Loot everything while the Equip tab has room. **Vendor** it unless it's a scroll base (Work Gloves, Sauna Robe, Squishy Shoes), a mage item you'll wear, or an item `02` lists. **Log equips per 1,000 kills (V-39)** | NPC sell is 25–50% of NPC buy; typical drops sell for 3k–9k, the best voted farm-mob drop 13,200 [V-dm, V-cbt] |
| **Quest-demand ETCs**: Cursed Doll, Medicine With Weird Vibes, Drake Skull, Dragon Skin, Stone Golem Rubble, Jr. Necki Skin, Glass Shoe, Mushmom Spore, Sap | Keep enough for your own quests, then sell the surplus to players | Quest demand runs 80–600 per character; NPC values are 21–400 [V-dm] |
| **Ores**: Garnet, Black Crystal, Diamond, gem ores | Keep Garnet and Black Crystal (Arcforge scroll inputs) | Demand reported in COT2 [V-cbt, unsourced quote] |
| Potions | Use them; buy **Orange (50 mesos / 50 MP) or Lemon** | 1 meso per MP [V-dm] |

Notable voted equip drops on your maps [V-cbt votes; NPC sell V-dm]: Zombie Mushroom: White/Blue Chaos Robe 9,000, Nakamaki 9,000 · Curse Eye: Battle Shield 10,000, Axe Pole Arm 9,000 · Fire Boar: Red Viper 9,000, Blood Fitted Mail 9,000 · Jr. Wraith: Dankke 7,500, Yellow Jangoon Armor 7,000 · Lorang: Korean Fan 9,500 (+20) · Zombie Lupin: Black Napoleon 13,200, Blue Moonlight 12,600 · Wraith: Red China 11,000 · Echopus: Blue Calas/Calaf (Lv 50 mage overall) 19,800.

---

## 13. Kerning citizenship routine (I/L) [V-dm M-CIT, "work in progress"]

**Why Kerning:** Ben (Kerning) sells the **Overall INT Lesser** (35k, grade 7) and Max sells **Wolbi** (grade 3) for the Assassin; meowdb's I/L guide says to keep Kerning [V-dm, guide]. Henesys's Flint sells the Earring Crit Damage Lesser (grade 3); with both characters in Kerning, buy those from players (≤ 1.1 × 50k).

- **Daily** (2–5 min): one Community Board task. **100 contribution at grade 1, +50 per grade**, plus EXP and mesos. VIP dailies from grade 5 (Lv 32).
- **Weekly donation:** 100 of one ETC from your grade's list (Kerning's list: read it on the board, V-9). Contribution is 500 at grade 1, +250 per grade, whichever listed item you donate.
- **Grade thresholds** (level + contribution): 2 (17, 1,000), **3 (22, 2,000)**, 4 (27, 3,000), 5 (32, 4,000), 6 (37, 5,000), **7 (42, 6,000)**, 8 (47, 7,000), **9 (52, 8,000)**, 10 (57, 10,000).
- **Grade timeline** [calc]: if contribution is cumulative, grade 3 ≈ day 8, 5 ≈ day 15, 7 ≈ day 18. If it resets per grade, grade 3 ≈ day 14 and 7 ≈ day 56. **Expect grade 3–6 by Oct 20** (V-9 decides).
- Per character or per account is [?] (V-32). The first town choice is free; later switches cost about 50,000 mesos per reactivation in COT2 [V-cbt, unconfirmed].

---

## 14. Open items that change this file

V-1 (mesos per kill), V-10 (level cap), V-9 (citizenship), V-14/V-15 (skill or mob changes), V-19 (KPQ), V-26 (MP regen), and the new I/L checks **V-38 (magic misses), V-39 (equips per 1,000 kills), V-40 (Thunder Bolt targets per cast), V-41 (level-gap EXP penalty)**. All are in `05_launch_day_verification.md`.
