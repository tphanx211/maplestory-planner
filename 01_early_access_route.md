# Founder's Access Route: Fighter (farmer), plus launch-character plans

Version 0.1 · 2026-10-02. Tags and source keys are as in `00_classic_world_verified_intel.md`.
- **[V-dm]**: COT2 client datamine (meowdb). It may change at launch.
- **[V-cbt]**: community test reports.
- **[model]**: meowdb's modeled rates (instant or 1–2-hit kills, no travel).
- **[calc]**: my arithmetic, with inputs shown.

All map, mob and quest data is from meowdb's map, monster and quest-tracker pages (COT2) and its guides: best-grind-maps 2026-09-23, warrior and fighter class guides, Forgotten Hollow guide 2026-09-26, KPQ guide 2026-08-12. Meso and drop reports come from meowdb's community endpoints, fetched 2026-10-02.

**Elements don't matter for a Fighter.** Warriors have no elemental attacks before 3rd job, so the weakness columns below only matter for the launch character or a mage friend.

---

## 0. The model behind every number (replace the inputs with your day-1 measurements)

| Input | Value used | Source / tier |
|---|---|---|
| Play budget | 76 h (Oct 6–20) | kickoff profile |
| Pace Lv 1–30 | Lv 10 at 2–3 h, Lv 20 at 6–7 h, **Lv 30 at 14–20 h** | COT testers via meowdb EXP table [V-cbt] |
| Pace Lv 30+ | meowdb Fighter Advisor EXP/min × **real-play factor r = 0.55–0.80**. COT testers ran about 75–80% of the model at Lv 20–30 | [model] × [assumption] |
| Kills/hour | EXP/h ÷ mob EXP | [calc] |
| **Mesos per kill** | **(1.7–2.3) × mob level × meso drop chance** | ~34 single community reports, all between 1.7× and 2.3× mob level [V-cbt] |
| Meso drop chance | **0.6–1.0**. Reporters entered 100%, which is unverified | [assumption]; measure it (V-1) |
| Upkeep | Power Strike and Slash Blast cost 12 MP at max, about 12 mesos at 1 meso/MP (Lemon). About 10–20k/h at Lv 30–35, rising to 25–40k/h at Lv 50+, plus HP pots | [V-dm] prices; [calc] from the warrior notes |
| EXP table | Lv 1–49 matches pre-BB and was verified in COT; **Lv 50+ is legacy reference** | [V-dm]/[B] |

A useful shortcut [calc]: **mesos per hour ≈ EXP per hour × (2 × mob Lv ÷ mob EXP) × drop chance.** That ratio is about 1.07 for Lv 15–25 mobs, 0.97 for Jr. Wraith, 0.83 for Zombie Lupin and 0.63 for Malady. Lower-level mobs pay slightly more mesos per EXP, so **the fastest-EXP map is also close to the best meso map**.

### 0.1 Founder's Access projection [calc: `calc/route_projection.py`, `calc/bracket_rates.py`, `calc/day_plan.py`; run `python calc/route_projection.py` after editing the inputs]

| Scenario | Assumptions | Level on Oct 20 | Mob mesos, gross | Upkeep | **Net mesos** |
|---|---|---|---|---|---|
| Low | r 0.55, drop 60%, 1.7× Lv, high upkeep, Lv 30 at 20 h | ~51 | 4.3M | 2.0M | **~2.3M** |
| Mid | r 0.70, drop 80%, 2.0× Lv | ~55 | 9.3M | 1.7M | **~7.7M** |
| High | r 0.80, drop 100%, 2.0× Lv, Lv 30 at 14 h | ~60 | 15.0M | 1.3M | **~13.7M** |

These totals **exclude** item value: stars, scrolls, ores and quest ETCs (§12) and boss drops (§11). Before Lv 30, mesos are roughly break-even (−1k to +34k/h). Meso income ramps after 2nd job: **~40–290k/h net from Lv 35** in this model.

### 0.2 Day-by-day level target [calc]

| Day | Hours (cum.) | Level: low / mid / high | Milestone |
|---|---|---|---|
| Tue Oct 6 (opens 1 PM CDT) | 4 (4) | 12 / 14 / 15 | 1st job; Henesys citizenship; Andre's Work Gloves |
| Wed Oct 7 | 4 (8) | 21 / 21 / 22 | Jane and the Mushroom; KPQ once |
| Thu Oct 8 | 4 (12) | 24 / 24 / 27 | Ant Tunnel III |
| Fri Oct 9 | 4 (16) | 27 / 27 / 31 | Arwen's Glass Shoe at 29 |
| Sat Oct 10 | 8 (24) | 32 / 32 / 36 | **2nd job (Fighter)**; start the Sauna Robe chain |
| Sun Oct 11 | 8 (32) | 35 / 37 / 42 | Shumi B1–B3 (10k mesos); Axe Mastery 20 by 38 |
| Mon–Fri Oct 12–16 | 20 (52) | 44 / 47 / 51 | Forgotten Hollow quests; Cursed Dolls; Jane's challenges at 44 |
| Sat–Sun Oct 17–18 | 16 (68) | 49 / 53 / 57 | Line 2 Wraiths or Monkey Forest II; Mushmom; Blackbull and Alligators at 48 |
| Mon–Tue Oct 19–20 | 8 (76) | 51 / 56 / 60 | Farm; sell or hold per `02_market_playbook.md` |

If you're behind the "low" column by Sun Oct 11, recheck the real-play factor with the V-1 tally. Don't add hours you don't have.

---

## 1. Lv 1–10: Maple Island, then Lith Harbor (≈2–3 h)

**Goal:** finish the quests fast, keep the AP plan, leave by about Lv 8.

| Map (id) | Mobs: Lv / HP / EXP [V-dm] | Spawns | Max EXP/h (ceiling) |
|---|---|---|---|
| Hunting Ground Middle of the Forest II (000001006) | Snail 1/45/2, Blue Snail 2/51/4, Shroom 3/62/6, Red Snail 4/68/8, Orange Mushroom 8/142/15 | 45 | 94k |
| Dangerous Forest (000001002) | Snail, Blue/Red Snail, **Orange Mushroom ×12** | 34 | 93k |
| Mushroom Garden (000001003) | Shroom ×23, Snail, Orange Mushroom | 35 | 81k |

- **Weaknesses:** none relevant. Stump (Lv 5) is Fire weak and Slime (Lv 6) is Lightning weak [V-dm].
- **Quests** [V-dm]:
  - Sam's Suggestion: 30 EXP, potions.
  - Lucas's letter: hat.
  - **Mai's Training**: 170 EXP, 150 mesos.
  - **Biggs's Collection**: Razor or Fruit Knife. Wield it at Lv 5.
  - **Pio's Recycled Goods**: Green Relaxer chair, "only place you can get it".
  - Rain's Maple Quiz: 245 EXP.
  - Quests take you to about **Lv 8**. Then take the boat at **Shanks, Southperry** to Lith Harbor. The fare isn't documented; legacy was 150 mesos [B?].
- **Lith Harbor to Lv 10:** Lith beginner quests. Do **Phil's Call** (Lv 8, the prerequisite for Jane). Otherwise grind **L Forest I** (010003020): Ribbon Pig Lv 10 ×21, ceiling 334k EXP/h. **Avoid its single Iron Hog** (Lv 28, 500 P.DEF).
- **1st job:** **Dances with Balrog, Perion, at Lv 10**, with no stat requirement [V-dm].
- **Then claim your Founder package from the mailbox.** It can't be opened on Maple Island [V-off N10].
- **Mesos [calc]:** EXP to Lv 10 is 3,347. Snail drops about 2 mesos and Ribbon Pig 18–23 (2 reports) [V-cbt]. Expect about 2–5k mesos from kills plus ~300 from quests. That's negligible.
- **Pick up:** Orange Mushroom Cap, Red/Blue Snail Shell and Mushroom Spore (Henesys weekly donation, grade 1). Also the **Long Sword** (Orange Mushroom) and **Metal Axe** (Slime): early weapons sell to NPCs for 1,500 and 2,500 [V-dm].

---

## 2. Lv 10–20: Swordman (≈3–4 h)

**Goal:** Work Gloves, Henesys citizenship at 12, early Slash Blast, then Bubblings.

| Map (id) | How to get there | Mobs: Lv / HP / EXP / P.DEF / weak [V-dm] | Spawns | Ceiling EXP/h | Safety |
|---|---|---|---|---|---|
| L Forest I (010003020) | East of Kerning Construction Site | Ribbon Pig 10/172/19/0 | 73 (21 Ribbon Pig) | 334k | Safe; avoid the Iron Hog |
| West Rocky Mountain III (010004022) | West of Perion | **Green Mushroom 14/233/26/0** (poison immune; flagged Undead [?]), Dark Axe Stump 23/547/43/30 (fire weak) | 67 | 573k | Dark Axe Stump hits 129–176 below Lv 15 |
| **Line 1 <Area 1> (010003061)** | Kerning → Subway Ticketing Booth → Line 1 Area 1 | **Bubbling 15/259/28/20**, lightning weak | **64 (single mob)** | **640k** | Touch 67–91: careful at Lv 11–15, safe by 20 |
| Tree Dungeon, Forest Up North IV (010002075) | North of Ellinia | Green Mushroom ×31, Slime ×13 | 44 | 344k | Safe (meowdb warrior pick for 20–25) |

- **Estimate [calc]** (Swordman model 1,000–1,367 EXP/min [model], r 0.55–0.80, Bubbling 28 EXP):
  - **33k–66k EXP/h** and **1,200–2,300 kills/h**.
  - Mesos/kill = 15 × (1.7–2.3) × (0.6–1.0) = **15–34**. Bubbling has no meso report; Green Mushroom's report is 25–30 [V-cbt].
  - **Gross 18k–81k mesos/h**. Upkeep is about 5–15k/h: use normal attacks (0 MP) on one-hit mobs.
- **Quests** [V-dm]:
  - **Nella chain (Kerning, Lv 10):** Don Hwang's Request (**costs 1,000 mesos**; 10 Orange Mushroom Caps + 10 Pig's Ribbons) → Shumi's Request → **Andre's Request**: kill 30 Octopus, bring 20 Octopus Legs + **1 Pure Water** (1,120 mesos at Sleepywood, Florina or the 24 Hr store). Reward: **Work Gloves** (5 slots, +1% crit, tradeable). Keep the gloves; they're your GFA base.
  - **Fixing Blackbull's House** (Lv 11): Wooden Buckler, or a 10% chance at a Steel Shield. Also a prerequisite for the Lv 48 Blackbull scroll quest.
  - **I Need to Find My Daughter 1/2** (Lv 11): prerequisite for Arwen and the Alligators quests.
  - **Henesys citizenship** (Lv 12, Arthur): do the daily every play day (§13).
  - **Pia and the Blue Mushroom** (Lv 16): random **Hat Accuracy scroll**.
  - **Mother's Gold Watch** (Lv 18): Weighted or Yellow Square Earrings.
  - **Talking to Stan** (Lv 18).
  - **Jane and the Mushroom** (Lv 20, Lith Harbor; needs Phil's Call): 30 Blue + 30 Horny kills, 15 + 15 caps. Rewards: 2,021 EXP, 585 mesos, and **a random Intermediate weapon ATT scroll (1 of 13)**.
- **Pick up** [V-cbt, vote counts in brackets]:
  - Octopus Leg (Andre).
  - **Mithril Ore** (Bubbling, 13).
  - Bubbling's Huge Bubble (Kerning weekly donation, Ronnie quest).
  - **Battle Axe** (Bubbling, 5): a Lv 15 warrior weapon.
  - **Pan Lid** (Green Mushroom, 16).
  - **Claw ATT scroll Intermediate** (Green Mushroom, 3).
  - 1H Axe ATT Greater (Green Mushroom, 1).
  - Blue Mushroom Cap (Jane; grade 2 weekly).
  - **Gloves Crit Rate Greater** and 2H Sword ATT Greater (Blue Mushroom).
  - **Any scroll, ever.**

---

## 3. Lv 21–30: Swordman (≈8 h; testers took 8–9 h for Lv 20–30)

**Goal:** dense mushrooms for Slash Blast, KPQ once, boots, cape and scroll quests, 2nd job at 30.

| Map (id) | How to get there | Mobs: Lv / HP / EXP / P.DEF / weak [V-dm] | Spawns | Ceiling EXP/h | Safety |
|---|---|---|---|---|---|
| **Ant Tunnel III (010005062)** | Sleepywood → Ant Tunnel I → II → III | **Zombie Mushroom 24/436/45/15** (holy weak, undead), **Horny Mushroom 22/403/41/10** | **99** (61 + 38) | **1.54M** (#32 of 279) | Touch 121–186: caution at Lv 21–25 (≈700–850 HP) |
| Deep Ant Tunnel I (010005066) | Sleepywood → Dangerous Steam → Deep Ant Tunnel I | Zombie ×29, **Evil Eye 27/606/50/10** ×21, Horny ×16 | 68 | 1.08M | Evil Eye hits 175–239 |
| Ant Tunnel Park (010005070) | After Deep Ant Tunnel II; leads to The Grave of Mushmom | Evil Eye ×31, Zombie ×23, Horny ×4 | 58 | 0.98M | Good Lv 27–30 |
| The Burnt Land II (010004112) | Perion side | **Fire Boar 32/842/62/10** (ice weak) ×19, Dark Axe Stump ×12 | 31 | 0.61M | Risky before ~Lv 28. **Arwen's Glass Shoe** and Wolbi drop here |

- **Estimate [calc]** (Swordman model 1,396–1,762 EXP/min [model], r 0.55–0.80, Zombie/Horny ~43 EXP):
  - **46k–85k EXP/h** and **1,100–2,000 kills/h**.
  - Mesos/kill = 23 × (1.7–2.3) × (0.6–1.0) = **23–53**. Horny Mushroom report: 40–48 [V-cbt].
  - **Gross 25k–104k/h**; upkeep 10–20k/h.
- **Quests** [V-dm]:
  - **Proof of Companionship** (Lv 21, Lakelis, Kerning; one KPQ clear): 2,193 EXP, 614 mesos, **random Intermediate Earring stat scroll**.
  - **Arcon's Blood** (Lv 21, Manji, Henesys): 75 Zombie Mushrooms → 2 × 2,193 EXP.
  - **Cutthroat Manny's Request** (Lv 22, Nella chain): 50 Evil Eyes → **Mithril War Boots**.
  - **Dr. Faymus's Request** (Lv 22): 40 Horny + 40 Jr. Necki → 30 White Potions.
  - **Chris's Request** (Lv 22): Bronze and Iron Ingots.
  - **Stranger's Identity** (Lv 23, Jane Doe, Kerning): 50 Zombie Mushrooms → **Old Raggedy Cape**.
  - **Sabitrama and the Diet Medicine** (Lv 25, Sleepywood; Forest of Patience jump quest via Shane, Ellinia) → **Overall DEF scroll, Intermediate or Greater**.
  - **Sabitrama's Anti-Aging Medicine** (Lv 25) → **Star Rock**. Keep it: it's needed at Lv 50 for Hero's Gladius, and it sells to NPCs for 4,000.
  - **Arwen and the Glass Shoe** (Lv 29, Ellinia; marked **repeatable**): 1 Glass Shoe (Fire Boar) → 3,037 EXP, 848 mesos, **Piece of Ice or Fairy Wing**.
- **2nd job:** **Fighter at Lv 30**, Dances with Balrog [V-dm].
- **Pick up:**
  - **Claw ATT scroll Intermediate** (Zombie Mushroom, 6).
  - **Spear ATT Greater** (Zombie, 2).
  - Charm of the Undead and Horny Mushroom Cap (grade 3 weekly; Jane).
  - Gold, Bronze and Topaz Ore.
  - Evil Eye Tail (grade 4 weekly).
  - Wild Boar Tooth and Leather.
  - **Fire Boar: Arwen's Glass Shoe (7), Garnet (6), Wolbi (5), Earring STR Greater (1).**
  - **Dark Axe Stump: Sap of Ancient Tree** (Jane's Final ×10), **Diamond Ore**, Stump's Teardrop.

---

## 4. Lv 31–40: Fighter (≈15–18 h)

**Goal:** Axe Mastery 20 by 38, the Sauna Robe chain, Shumi's 10k mesos, and start the Cursed Dolls.

| Map (id) | How to get there | Mobs: Lv / HP / EXP / P.DEF / weak [V-dm] | Spawns | Ceiling EXP/h | Why |
|---|---|---|---|---|---|
| **Line 1 <Area 1> (010003061)** | Kerning subway | Bubbling 15/259/28/20 | 64 | 640k | **Advisor pick for 30–34:** a Lv 30–34 Fighter one-shots Bubblings with Slash Blast [model] |
| **Ant Tunnel II / III (010005061/062)** | Sleepywood | Zombie / Horny (above) | 47 / 99 | 0.73M / 1.54M | **Advisor pick for 35–39** (3,857 EXP/min modeled) |
| Line 2 <Area 1> (010003066) | Kerning subway: Transfer Area → Line 2 Area 1 | **Jr. Wraith 34/982/70/30** (holy and fire weak, undead) ×83, Jr. Necki ×14 | 97 | **2.27M** (#9) | **Mokbi stars** (12 votes; NPC sell 1,000) and **Tablecloth**. Slow for a Fighter until ~Lv 38: 30 DEF means 2–3 Power Strikes or 4 Slash Blasts per kill at Lv 34 [calc] |
| A Look-Out Shed Around the Beach (010007010) | Florina Road via **Pason, Lith Harbor** (fare [?]; Return Scrolls don't work there) | **Lorang 38/1,714/86/0** (lightning weak) ×36, Lupin ×27 | 63 | 1.28M | 0 DEF; Garnet; Lorang Claw (grade 6 weekly) |
| Monkey Forest II (010002023) | Ellinia side | **Zombie Lupin 41/1,774/99/0** (holy weak, undead) ×25, Lupin 37/1,336/82/0 ×10 | 35 | 1.18M | **Cursed Doll** farm (from Lv ~39–40 for accuracy) |

- **Estimate [calc]** (Advisor models 1,770 at 30–34 and 3,857 EXP/min at 35–39, r 0.55–0.80):
  - **Lv 30–34 on Bubbling:** 58k–85k EXP/h; 2,100–3,000 kills/h; mesos/kill 15–34; **gross 32k–105k/h**.
  - **Lv 35–39 on Ant Tunnel:** 127k–185k EXP/h; 3,000–4,300 kills/h; mesos/kill 23–53; **gross 69k–228k/h**.
  - Upkeep ≈ 10–30k/h.
- **Accuracy** [calc, builds notes]: with the AP plan (§7), Jr. Wraith is 100% hit from Lv 34, Lupin from 39, and Zombie Lupin from 45 (95% at 41). Henesys's **Supreme Sniper Potion** (+7 ACC, 600 mesos, 15 min) closes the gap a level or two early.
- **Quests** [V-dm]:
  - **Mr. Wetbottom's Secret Book chain** (Lv 32, 9 steps; Ronnie at The Tree Tunnel north of Ellinia, Wetbottom in the Sleepywood VIP Sauna):
    - Needs **30 Lupin's Bananas**, **50 Curse Eye Tails**, **10 Pig's Heads** (source [?]) and **1 refined Diamond**.
    - Rewards: **29,289 EXP total**, 7,862 mesos, 40 Blue Potions, and the **Sauna Robe** (Lv 30 overall, +1 all stats, **10 slots**, tradeable, NPC sell 5,400). It's the best base for Overall stat scrolls.
  - **Shumi's Lost Coin / Roll / Sack of Cash** (Lv 35, Kerning, Construction Site B1–B3 jump quests; needs Proof of Companionship): 3 × 4,162 EXP, then 1,023 + 1,023 + **10,000 mesos**, 30 Blue Potions, **30 Mana Elixirs**, and return scrolls.
  - **Collecting 50 → 200 Cursed Dolls** (Lv 36, Rowen, Ellinia; needs Returned Secret Book):
    - 5 × 4,387 EXP and 1,053 mesos each.
    - Ores and gem ores along the way; 5 Gold or 5 Diamond Ore at 100 dolls.
    - **150 dolls: GFA60 or GFMA60** (50/50).
    - 200 dolls: **Steel Nordic Helm**.
    - 570 dolls total (Zombie Lupin). Start it here and finish it in the 40s.
  - **Forgotten Hollow opening** (Lv 39, Grendel → Arwen → Nyroth):
    - **Tracing the Resonance**: Hat ACC scroll.
    - **Welcome to the Hollow**: a **Greater (10%) ATT scroll for your class's weapon**. Pick 2H Axe, or the one that sells best (`02`).
- **Pick up:**
  - **Mokbi** (Jr. Wraith; Cold Eye).
  - **Kumbi** (Lupin, 6; NPC sell 1,500).
  - Lupin's Banana (Ronnie ×30).
  - **Curse Eye Tail** (Ronnie ×50; also Blackbull's Deed from Curse Eye).
  - Tablecloth.
  - Lorang Claw.
  - **Garnet** (Lorang).
  - Hat ACC Greater (Jr. Wraith).
  - Topwear MP Greater (Curse Eye).
  - **Cursed Doll** (Zombie Lupin).

---

## 5. Lv 41–50: Fighter (≈20–30 h)

**Goal:** the scroll and Elixir quest lines, Wraith or Fire Boar farming, and Mushmom from about Lv 45. If the cap is 50 (V-10), this bracket is the endgame.

| Map (id) | How to get there | Mobs: Lv / HP / EXP / P.DEF / weak [V-dm] | Spawns | Ceiling EXP/h | Why |
|---|---|---|---|---|---|
| **Ant Tunnel Park (010005070)** | Sleepywood dungeon | Evil Eye 27/606/50/10, Zombie Mushroom | 58 | 0.98M | **Advisor pick for 40–44** (4,309 EXP/min modeled); leads to Zombie Mushmom |
| **Monkey Swamp III (010003097)** | Monkey Swamp II (respawn point Kerning) | Zombie Lupin ×31, Jr. Necki ×14 | 45 | 1.29M | Best Cursed Doll map; 9 portals to the potion shop |
| Forgotten Entrance III (010006060) | Forgotten Hollow (Tree Tunnel north of Ellinia, or Sleepy Dungeon V) | **Glowshroom 39/1,377/90/10**, **Raffle 40/1,722/94/10** (fire weak), Curse Eye | 44 (×0.7) | 1.34M | Hollow quest items (Map Fragments, Raffle Petals) |
| **The Burnt Land I / III (010004111/113)** | Perion → Deep Valley II → Burnt Land | Fire Boar 32/842/62/10 ×18–24, Dark Axe Stump | 25–37 | 0.51–0.73M | **Advisor pick for 45–49** ("1-hit"); Glass Shoes; 100 Dark Axe Stumps for Jane's Final |
| **Line 2 <Area 2> (010003067)** | Kerning subway | **Wraith 48/2,350/132/30** (holy weak, undead, regen 50 per tick) ×57, Jr. Wraith ×32, Jr. Necki ×18 | 107 | **3.74M (#2 of 279)** | Densest map on Victoria; **Medicine With Weird Vibes** (Jane ×50). Use from Lv 46–48, when Slash Blast handles Wraiths |
| Drake Hunting Ground (010005075) | Sleepywood dungeon via Cave of Evil Eye IV | **Drake 50/3,218/142/15** (fire and ice resist) ×18 | 22 | 0.94M | **Drake Skull** (Jane ×25, grade 9 weekly) and **Dragon Skin** (Jane's Final ×20, 23 recipes) |
| Dangerous Valley (010004101) | Perion side | Fire Boar ×21, **Copper Drake 45/2,595/117/15** (ice weak) ×13 | 34 | 1.01M | Jane's First (50 Copper Drakes); Black Crystal |

- **Estimate [calc]** (Advisor models 4,309 at 40–44 and 5,153 at 45–49, r 0.55–0.80):
  - **Lv 40–44 on Ant Tunnel Park:** 142k–207k EXP/h; 3,000–4,300 kills/h; mesos/kill 27–60; **gross 79k–258k/h**.
  - **Lv 45–49 on Burnt Land:** 170k–247k EXP/h; 2,700–4,000 kills/h; mesos/kill 33–74; **gross 90k–294k/h**.
  - Upkeep 20–35k/h.
  - Line 2 Area 2 is a ceiling map: the Advisor rates it for 55–64 ("2-hit") because of Wraith's 30 DEF. Use it earlier only if your Slash Blast kills Wraiths in 2 casts.
- **Quests** [V-dm]:
  - **Forgotten Hollow chains** (Lv 39–50; 15 quests total, 84,249 EXP and 19,573 mesos [V-cbt FH guide]):
    - **The Road Back Home** (43): Earring scroll.
    - **Matters of the Heart** (45): Cape ACC scroll.
    - **A Heart of Stillness & Wood** (50; **30 Cursed Dolls** + 20 Duskmander Tails): 12,500 EXP, 2,500 mesos, Elixirs and a scroll.
    - **The Sage's Burden** (50): Elixirs.
    - **Myra's Old Friend** (49): 15 Mana Elixirs.
  - **Building a New House chain** (Lv 41, Ronnie): 4 × 5,568 EXP. The last step gives a **Shoes Speed scroll (Intermediate or Greater)**. Needs 30 Tablecloths, 30 Drake Skulls, 10 Dragon Skins and 1 Diamond.
  - **Jane's First Challenge** (Lv 44; 50 Copper Drakes + 50 Wraiths, 25 Drake Skulls + 25 Medicine With Weird Vibes + 1 Pure Water) → **10 Elixirs**.
  - **Jane's Second** (50 Wraiths + 50 Maladies; **1 Mushmom Spore**, 3 Drake's Blood, 25 Medicine, 25 Malady's Frogs) → **15 Power Elixirs**.
  - **Jane's Final** (100 Dark Axe Stumps + 50 Drakes; 1 Moon Rock, 20 Dragon Skins, 10 Sap) → **one random gloves scroll: ATT Intermediate / ATT Greater / MATK Intermediate / MATK Greater (25% each)**.
  - **John's Present** (Lv 45, Lith; Deep Forest of Patience jump quest) → **Dark Knuckle** (warrior gloves, Lv 40, 5 slots).
  - **John's Last Present** → Pansy Earrings.
  - **Luke's Wish to Travel** (Lv 46) → Bronze Crusader Helm (30 Drake Skulls, 20 Dragon Skins, 10 Orihalcon Ingots).
  - **Building a New House For Blackbull** (Lv 48; 10 fame; 100 Stone Golem Rubbles + 30 Screws + 30 Processed Wood + Blackbull's Deed) → **pick-one Greater weapon ATT scroll**.
  - **Taking Out the Alligators 1** (Lv 48; 40 Jr. Neckis + 100 Ligators, 20 Jr. Necki Skins) → **pick-one Greater weapon ATT scroll**.
  - **Alligators 2** (120 Crocos, 50 Croco Skins) → **pick-one Cape stat scroll (Intermediate)**.
  - **Citizenship weeklies:** Lv 42 Cold Eye Tail (5,793 EXP); Lv 47 Tortie Shell (7,143 EXP).
- **Pick up:**
  - **Medicine With Weird Vibes** (Wraith; 230 needed per character across quests).
  - **Drake Skull** (Drake, Red Drake, Copper Drake; 185 per character).
  - **Dragon Skin** (Drake; 80 per character plus crafting).
  - **Black Crystal Ore** (Copper Drake, Malady, Dark Stone Golem; NPC sell 500).
  - Cursed Doll.
  - **Earring LUK Intermediate** (Rafflesia, 4).
  - Bottomwear HP Intermediate (Echopus).
  - Red Whip (Wraith).
  - Tortie Shell.

---

## 6. Lv 51–70: Fighter (only partly reachable before Oct 20; cap unconfirmed)

meowdb: "Victoria Island has no strong map for the 60s." Mobs above Lv 60 use timed respawns, so **farm below your level** [V-dm].

| Map (id) | Mobs: Lv / HP / EXP / P.DEF / weak [V-dm] | Spawns | Ceiling EXP/h | Why |
|---|---|---|---|---|
| **Monkey Forest II / Tree Dungeon Monkey Forest II (010002023/024)** | Zombie Lupin 41/1,774/99/0 | 35 / 30 | 1.18M / 1.01M | **Advisor pick for 50–54** (7,883 EXP/min modeled); Cursed Dolls |
| **Line 2 <Area 2> / <Area 3> (010003067/068)** | Wraith ×57 / ×68 | 107 / 68 | 3.74M / 3.21M | Densest; Advisor pick for 60–64 (Area 3, "2-hit") |
| **Sleepy Dungeon V (010005054)** | **Dark Stone Golem 58/5,428/197/0** (holy weak; fire and poison resist; buffs itself) ×19, Curse Eye ×24, Lupin ×23, Jr. Necki, Jr. Boogie | 89 (×0.7) | **2.73M** (#6) | **Tobi**, Black Crystal, **Ancient Scroll** (Hero's Gladius); back door to Forgotten Hollow |
| The Forest of Evil II (010002026) | **Malady 55/2,998/175/0** (1-min timed respawn) ×23, Zombie Lupin ×16 | 39 | 1.21M | **Advisor pick for 55–64**; Black Crystal; Malady's Frog (Jane's Second ×25). Element data conflicts [?] |
| Drake's Meal Table (010005090) | Drake ×23, Cold Eye ×22, Wild Kargo ×10 (5-min respawn) | 55 | 1.93M (#21) | **Drake Skull and Dragon Skin farm** (quest demand) |
| Lorang and Clang (010007030) | **Clang 49/2,899/137/15** (lightning weak) ×29, Lorang ×18 | 47 | 1.97M (#19) | On-level alternative; Aquamarine |
| Dangerous Valley II (010004102) | **Red Drake 60/5,184/213/15** (ice weak, fire resist; ranged fire attack ≈420) ×17 (20 s–1 min respawn) | 30 | 0.70M | **Steely stars** (10 up / 1 down; NPC sell 10,000) |
| Perilous Descent III (010006110) | Duskmander 50/2,682/142 (ice weak), Echopus 45/2,163/117 | 14 (×0.8) | 0.67M | **Advisor pick for 65–70** (one-hit at 70). The low spawn ceiling caps the real rate |

- **Estimate [calc]:**
  - **Lv 50–54 on Monkey Forest II** (7,883/min): 260k–378k EXP/h; 2,600–3,800 kills/h; mesos/kill 42–94 (Zombie Lupin report 74–92 [V-cbt]); **gross 110k–360k/h**.
  - **Lv 55–64 on Forest of Evil II** (7,939–10,557/min): **gross 89k–388k/h**. Malady's 1-minute timed respawn makes the low end more likely [calc].
  - Upkeep 25–40k/h.
- **Quests:**
  - A Heart of Stillness & Wood and The Sage's Burden (50).
  - **Hero's Gladius chain** (50; Manji → Chrishrama): needs the **Star Rock** from Sabitrama, a **Piece of Ice** from Arwen, an **Ancient Scroll** (Dark Stone Golem) and a Flaming Feather (Red Drake). Rewards: 3 × 7,987 EXP and Hero's Gladius or Skull Earrings.
  - **Citizenship Lv 52 weekly** (Henesys): 100 **Drake Skulls** → 8,718 EXP.
  - **Grade 9 at Lv 52 unlocks GFA Lesser**, if contribution allows (V-9).
- **Pick up:** **Steely** (Red Drake), **Tobi** (Stone Golem, DSG), Black Crystal, Drake Skull, Dragon Skin, Ancient Scroll, Adamantium and Aquamarine Ore (Sporewood, Clang), Fragment of Magic (Arcforge scroll recipes).

---

## 7. Fighter AP plan (2H axe) [V-dm meowdb warrior and fighter guides; ACC calc from meowdb formulas]

**Rule:** there's no AP into HP or MP in Classic. Everything goes into STR, plus **DEX equal to your next 2H axe's level** (every 2H weapon needs DEX = weapon level).

| Level | AP per level | Base STR / DEX at the end of the range | Why |
|---|---|---|---|
| Creation | 4 base + 9 free | **12 / 5** (INT 4, LUK 4) | meowdb default |
| 2–10 | 5 STR | 57 / 5 | No 1st-job stat requirement |
| 11–12 | 4 STR, 1 DEX | 65 / 7 | Early hit rate |
| 13–14 | 3 STR, 2 DEX | 71 / 11 | Gear requirements |
| 15–19 | 4 STR, 1 DEX | 91 / 16 | Hit rate |
| 20 | 3 STR, 2 DEX | 94 / 18 | 20 total DEX with an Iron Viking Helm |
| 21–25 | 4 STR, 1 DEX | 114 / 23 | **Two-Handed Axe** (Lv 25): 25 DEX with gear |
| 26–29 | 4 STR, 1 DEX | 130 / 27 | |
| 30 | 5 STR | 135 / 27 | **Blue Axe** (Lv 30, 26,000 mesos at River): 30 DEX with a Jousting Helmet |
| 31–35 | 3 STR, 2 DEX | 150 / 37 | **Niam** (Lv 35; crafted, or El Nath, which isn't at launch); Jr. Wraith 100% hit at Lv 34 |
| 36–40 | 4 STR, 1 DEX (one level at 3/2) | 169 / 43 | **Sabretooth** (Lv 40, crafted or dropped) |
| 41–57 | 4 STR, 1 DEX | 237 / 60 | **The Rising** (Lv 50) needs 50; **The Shining** (Lv 60) needs 60 |
| 58–70 | 5 STR | 302 / 60 | **Chrono** (Lv 70) needs 70: 60 base + **10 from hat and shoes**. Without that gear, add the 10 DEX at Lv 68–70 (about −1.5% damage) |

Check [calc]: at Lv 70, total AP is 25 + 69×5 = 370 = 302 + 60 + 4 + 4 ✓.

**Accuracy:** with Precise Strikes 15 and a +3 ACC helmet, this DEX gives 100% hit on each farm mob at or within 1–3 levels of its level. **Don't farm more than 2 levels above a mob's level** without a Sniper Potion.

---

## 8. Fighter SP plan [V-dm meowdb guides; totals checked]

Totals: beginner 9 + 1st job 61 + 2nd job 121 = **191 SP by Lv 70**.

**Beginner (Lv 2–10, 9 SP):** Nimble Feet 3, then Three Snails 3, then Recovery 3.

**Swordman (Lv 10–30, 61 SP):**

| Level | Spend | Running total | Reason |
|---|---|---|---|
| 10 | PS +1 | PS 1 | Opens Slash Blast |
| 11 | PS +2, SB +1 | PS 3, SB 1 | 4-target mobbing right away |
| 12 | PS +1, SB +2 | PS 4, SB 3 | |
| 13 | SB +1, Precise +2 | SB 4, Precise 2 | |
| 14 | Precise +3 | Precise 5 | Hit rate |
| 15–19 | PS +15 | PS 19 | |
| 20 | PS +1, SB +2 | **PS 20**, SB 6 | 260%, 12 MP |
| 21–24 | SB +12 | SB 18 | |
| 25 | SB +2, Precise +1 | **SB 20**, Precise 6 | 130% × 4 mobs |
| 26–28 | Precise +9 | **Precise 15** | +20 ACC, +5% crit (stays after 2nd job) |
| 29 | Improved HP Recovery +3 | IHR 3 | Opens Max HP Increase |
| 30 | Max HP Increase +3 | MHP 3 | +12% Max HP |

Check: PS 20 + SB 20 + Precise 15 + IHR 3 + MHP 3 = 61 ✓. Iron Body stays at 0.

**Fighter (Lv 30–70, 121 SP):**

| Level | Spend | Running total | Reason |
|---|---|---|---|
| 30 | Rush +1 | Rush 1 | Mobility; knockback immunity while dashing |
| 31 | Rage +1, Axe Mastery +2 | Rage 1, AM 2 | |
| 32 | AM +3 | AM 5 | Opens Booster |
| 33 | Booster +1, Final Attack +1, AM +1 | Booster 1, FA 1, AM 6 | **Booster 1 already gives the full +2 speed** |
| 34–37 | AM +12 | AM 18 | |
| 38 | AM +2, FA +1 | **AM 20**, FA 2 | Mastery 10 + 25% Bleed |
| 39–47 | Rage +27 | Rage 28 | |
| 48 | Rage +2, FA +1 | **Rage 30**, FA 3 | +40 Attack Power (party), −40 WDEF |
| 49–57 | FA +27 | **FA 30** | 50% proc, 140%, up to 3 mobs |
| 58–63 | Booster +18 | Booster 19 | Duration and cost only |
| 64 | Booster +1, Rush +2 | **Booster 20**, Rush 3 | |
| 65–69 | Rush +15 | Rush 18 | |
| 70 | Rush +2, keep 1 | **Rush 20**, 1 spare | |

Check: 20 + 30 + 30 + 20 + 20 = 120, plus 1 spare = 121 ✓.

**Toggles** [V-dm model]: turn Final Attack **off** for single mobs and bosses (−12% damage) and **on** for packs of 2–3 (+6% / +24%). With Slash Blast on 4 targets it's about −3%. Keep Rush at 1 until 64; early levels cost 40 MP.

---

## 9. Launch character AP/SP plans (shorter)

Decide on Oct 21 (`00` §1.2): **Assassin if a friend plays an AoE class, otherwise Hunter.**

### 9A. Assassin [V-dm meowdb thief and assassin guides]
- **Creation:** 4 STR / 5 DEX / 4 INT / **12 LUK**. All AP to LUK until Lv 10.
- **Lv 11–15:** 2 DEX + 3 LUK per level. **Lv 16–70:** 1 DEX + 4 LUK per level. DEX tracks claw level.
- **Citizenship:** **Kerning** (Wolbi at grade 3, Overall LUK Lesser at grade 7, Destructive Potion).

| Lv | Base DEX / LUK | Claw | Skills (running) |
|---|---|---|---|
| 10 | 5 / 57 | Garnier (Manny, 5,000), Subi | Beginner 3/3/3; Lucky Seven 1 |
| 30 | 30 / 132 | **Adamantium Guards** (Manny, 27,600), Wolbi | L7 20 (Lv 18), Keen Eyes 15 (Lv 23), Nimble Body 15 (Lv 27), Disorder 3, Dark Sight 8 = 61 ✓ |
| 40 | 40 / 172 | Dark Guardian (crafted) | Haste 1, **Claw Mastery 20 (Lv 37)**, Booster 1, Critical Throw 9 |
| 50 | 50 / 212 | Dark Slain (crafted) | **Critical Throw 30 (Lv 47)**, Haste 10 |
| 70 | 70 / 292 | Black Scarab, Tobi/Ilbi | Haste 20, Booster 20, Critical Recovery 20, Drain 11 = 121 ✓ |

### 9B. Hunter (fallback) [V-dm meowdb bowman and hunter guides]
- **Creation:** 5 STR / **12 DEX** / 4 INT / 4 LUK. All AP to DEX until Lv 10.
- **Lv 11–15:** 2 STR + 3 DEX per level. **Lv 16–70:** 1 STR + 4 DEX per level.
- **Citizenship:** **Henesys** (Supreme Sniper Potion, Bronze Arrows, Overall DEX Lesser).

| Lv | Base STR / DEX | Bow | Skills (running) |
|---|---|---|---|
| 10 | 5 / 57 | War Bow | Arrow Blow 1 |
| 30 | 30 / 132 | Ryden (Karl, Henesys, 26,000) | Arrow Blow 20, Critical Shot 15, Eye of Amazon 15, Focus 10, Power Knockback 1 = 61 ✓ (**Double Shot 0**) |
| 40 | 40 / 172 | Vaulter 2000 (crafted) | **Bow Mastery 20 (Lv 39)**, Booster 5, Soul Arrow 1, Arrow Bomb 4, FA 1 |
| 50 | 50 / 212 | Olympus (crafted) | **Arrow Bomb 30 (Lv 49)**, FA 5 |
| 70 | 70 / 292 | Golden Hinkel | FA 30, Amazon's Judgement 20, Booster 10, Soul Arrow 11 = 121 ✓ |

**Launch-character maps** [V-dm]:
- **Lv 13–30:** Transfer Area and Dangerous Steam (Stirge 20/296/37/0, flying: good for ranged).
- **Lv 30–40:** Ant Tunnel II / Park.
- **Lv 40–50:** Ant Tunnel Park.
- **Lv 50–60:** Monkey Forest II / Forgotten Entrance II.
- **Hunter at 70:** Line 1 Area 2.

Whether the Fighter can speed up the launch character in a party (EXP from kills it didn't land) depends on Classic's party EXP split rules, which are undocumented [?] (V-18).

---

## 10. Kerning PQ vs solo grinding (Lv 21–30)

| | **Kerning PQ** | **Solo (Swordman, Ant Tunnel III)** |
|---|---|---|
| Entry | Exactly **4 players**, Lv 21+, **Channel 1 only**, 30-min timer [V-cbt M-KPQ] | Any channel |
| EXP per run / hour | Mob EXP in the run is **2,506 for the whole party** (22 Ligators × 68 + 6 Jr. Necki × 80 + 3 Curse Eyes × 94 + King Slime 248) [V-cbt; calc]. Per member: **≈1.3k–7.4k EXP/h** at 2–6 runs/h. **Stage-clear EXP is unknown [?]** | **≈49k–106k EXP/h** [model × 0.6–1.0] |
| Mesos | ≈16–102 kills per member per hour; whether PQ mobs drop mesos is [?] | ≈1,100–2,000 kills/h × 23–53 mesos = **25k–104k/h gross** |
| Items | 1 **Companion's Magic Box** per clear (untradeable; ores, potions, scrolls, gear; odds unknown); **Squishy Shoes** (Lv 28, +1 all stats, 5 slots, tradeable) can drop from King Slime | Normal drops (Claw ATT Intermediate, ores, weekly ETCs) |
| Break-even | For KPQ to match solo, stage-clear EXP would need to be about **11k–26k per member per run** [calc]. That's out of line with Classic's other quest rewards | — |

**Verdict:** **run KPQ once** for Proof of Companionship (2,193 EXP, 614 mesos and an Intermediate Earring stat scroll; it's also the prerequisite for Shumi's 10k-meso quest). Re-run only if the launch-day check (V-19) shows big stage-clear EXP, or to hunt Squishy Shoes. Grind solo otherwise.

---

## 11. Bosses as farming targets

| Boss | Lv / HP / EXP [V-dm] | Where | Respawn | Mesos (1 report) [V-cbt] | Drops worth it [V-cbt, votes] | Fighter readiness [calc] |
|---|---|---|---|---|---|---|
| **Mushmom** | 40 / 34,440 / 376; touch 585–798; regen 344 per tick | Someone Else's House (010001005), via **Pig Park II** near Henesys | 1–1.5 h | 1,800–2,200 | **Ilbi (9; NPC sell 20,000)**, **Mushmom Spore** (Jane's Second), Elixir, GFA Intermediate (1), Shield DEF Intermediate, crafting catalysts | From about **Lv 45–50**: ~20–25 Power Strikes (FA off). Touch damage is 30–40% of your HP: bring White Potions |
| **Zombie Mushmom** | 50 / 53,640 / 568; touch 706–963 | The Grave of Mushmom (010005078), via Ant Tunnel Park | 1–1.5 h | 2,250–2,750 | **Hwabi**, Ilbi, **Scroll Crafting Catalyst (9)**, Earring Crit Damage scrolls | From about Lv 52–55 |
| **Rotten Mushmom** | 60 / 86,400 / 852; poison; regen 864 per tick | Someone Else's Grave, off Decayed Tunnel I (Forgotten Hollow) | 1–1.5 h | — | Catalysts, Topwear MP Intermediate, Overall INT Intermediate | **Party only** (meowdb advises against soloing) |

**Boss loop:** after each Mushmom kill, note the channel and time. Check back about 60–90 min later while farming nearby (Henesys and Pig Park are close to Ellinia and Kerning). Other founders will contest it. **Never** use a script or timer tool that automates anything; a phone timer you set by hand is fine.

---

## 12. Loot rules (Fighter)

| Category | Rule | Why |
|---|---|---|
| **Any scroll** | Always loot. **Never** NPC-sell (it pays 1 meso) | `02` decides sell vs hold |
| **Throwing stars** (Mokbi, Kumbi, Tobi, Steely, Ilbi, Hwabi) | Always loot. Keep them for the launch-character decision or sell per `02` | NPC sell-back alone is 1,000 / 1,500 / 2,500 / 10,000 / 20,000 / 25,000 [V-dm] |
| **Quest-demand ETCs**: Cursed Doll, Medicine With Weird Vibes, Drake Skull, Dragon Skin, Stone Golem Rubble, Jr. Necki Skin, Arwen's Glass Shoe, Mushmom Spore, Sap of Ancient Tree | Keep enough for your own quests, then sell the surplus to players | Quest demand runs 80–600 per character, while NPC values are only 21–400 [V-dm] |
| **Ores**: Garnet, Black Crystal, Diamond, plus gem ores generally | Keep Garnet and Black Crystal (Arcforge scroll inputs); NPC-sell common metal ores only if storage is tight | Garnet was "the most in-demand ore in COT2" [V-cbt] |
| **Weekly-donation ETCs** for your grade (Henesys list in §13) | Keep 100 per week | Contribution plus EXP |
| Equipment | Keep **Work Gloves**, **Sauna Robe**, **Squishy Shoes**, **Dark Knuckle**, Battle Axe, Red Whip, any 2H axe ≥ Lv 35. NPC-sell the rest | Bases for scrolls; resale to warriors |
| Potions | Use them | NPC-priced; no trade value |

---

## 13. Henesys citizenship routine (Fighter) [V-dm M-CIT, "work in progress"]

- **Daily** (2–5 min): one Community Board task, i.e., talk to a named resident. It gives 224–351 EXP and mesos, and **100 contribution at grade 1, +50 per grade**. From grade 5 (Lv 32) there are also VIP dailies (2,440–3,487 EXP).
- **Weekly donation:** 100 of your grade's ETC.

| Grade (Lv) | Henesys item | Reward |
|---|---|---|
| 1 (12) | Blue/Red Snail Shell, Mushroom Spore, Squishy Liquid, Orange/Green Mushroom Cap | 321 EXP, 351 mesos |
| 2 (17) | Blue Mushroom Cap | 1,104 / 497 |
| 3 (22) | Horny Mushroom Cap, Charm of the Undead, or Wild Boar Tooth | 2,306 / 643 |
| 4 (27) | Evil Eye Tail | 2,812 / 789 |
| 5 (32) | Ligator Skin or Curse Eye Tail | 3,487 / 936 |
| 6 (37) | Lorang Claw | 4,612 / 1,082 |
| 7 (42) | Cold Eye Tail | 5,793 / 1,228 |
| 8 (47) | Tortie Shell | 7,143 / 1,374 |
| 9 (52) | Drake Skull | 8,718 / 1,521 |

Every weekly also gives 20 Blue Potions, plus 500 contribution at grade 1 and +250 per grade.

- **Grade timeline** [calc]: if contribution is cumulative, grade 3 ≈ day 8, 5 ≈ day 15, 7 ≈ day 18, 9 ≈ day 22. If it resets per grade, grade 3 ≈ day 14 and 7 ≈ day 56. **Expect grade 3–6 by Oct 20** (V-9 decides which).
- Per character or per account is [?]. If it turns out to be per account, the Assassin's Kerning choice conflicts. The first town choice is free; later switches cost about 50,000 mesos per reactivation (COT2).

---

## 14. Open items that change this file

V-1 (mesos per kill and drop chance), V-10 (level cap), V-9 (citizenship rules), V-14/V-15 (skill or mob changes at launch), V-19 (KPQ stage EXP), V-26 (natural regen), and the [?] items above: the Pason fare, the Pig's Head source, Malady's elements, and Green Mushroom's undead flag. All are tracked in `05_launch_day_verification.md`.
