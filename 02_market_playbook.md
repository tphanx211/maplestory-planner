# Market Playbook: Founder's Access to Free-to-Play

Version 0.6 · 2026-10-02. Risk profile: **balanced**. Tags and source keys are as in `00_classic_world_verified_intel.md`.

**Changed in 0.6:** the farmer is now an **I/L Wizard** and the launch character an **Assassin** (your decision). What changed here: the farming income figure (§2.2), the merchant role (§2.3: offline Hired Merchant only), the quest Greater scrolls a mage can get (§3, W10), the farmer's own gear buys (§4.1, W27), and the Hunter fallback (§5, retired). Equipment drops are vendored to NPCs at 25–50% of the NPC buy price; scrolls sell to NPCs for 1 meso, so scroll income only exists as player sales [V-dm].

**No prices exist yet, and none are invented here.** Every rule is relative to prices **you observe** (logged in the dashboard's price log in Phase 4, or the template in §8), or to datamined NPC prices [V-dm].

**Assumptions to verify first** (`05_launch_day_verification.md`):
- Trade tax and gates (V-11).
- Hired Merchant availability (V-8).
- Store Permit price (V-7).
- Quest-item tradability (V-21).
- Citizenship rules (V-9).

If any of these come back different, the affected section says what changes.

---

## 1. Price rules (used in every period)

### 1.1 What to log
For each watched item, log the **lowest asking price you see** (and the sale price when you know it), with date, time and channel.

The dashboard computes:
- **M3**: median of your observations over the last 3 days.
- **M7**: median over the last 7 days.
- **n**: the number of observations in the window.

**Signals need n ≥ 5 in the window.** Below that, the item shows "not enough data".

### 1.2 Anchors from NPCs [V-dm, COT2 prices; re-check V-12/V-13]

| Anchor | Meaning | Examples |
|---|---|---|
| **NPC floor** | NPC sell-back price. Never sell to a player below it | Mokbi 1,000 · Kumbi 1,500 · Tobi 2,500 · Steely 10,000 · Ilbi 20,000 · Hwabi 25,000 · Black Crystal Ore 500 · Mushmom Spore 400 · Dragon Skin 200 · Sauna Robe 5,400 |
| **NPC ceiling** | NPC buy price. Never pay a player more than it | Subi 500/set · Wolbi 1,000/set (Kerning grade 3) · all potions · arrows · NPC weapons up to Lv 30 (16,500–27,600) |
| **Lesser ceiling** | Price of the 100% scroll from an NPC | Weapon ATT Lesser: 25,000 (1H, dagger, wand, staff) or 50,000 (2H, spear, polearm, bow, crossbow, claw) at El Moth · Armor/DEF/ACC Lessers 15,000 at Tulcus · **Overall stat Lesser 35,000 (citizenship grade 7)** · **GFA/GFMA Lesser 50,000 (grade 9)** |

### 1.3 Signals

| # | Signal | Rule | Notes |
|---|---|---|---|
| R1 | **Floor arbitrage (BUY)** | Ask < 0.9 × NPC floor | Risk-free: buy, then NPC-sell or hold. Valid in every period |
| R2 | **Value buy** | Ask ≤ **0.70 × M3** for liquid items (n ≥ 5/day), or ≤ **0.60 × M3** for thin or hold items, **and** ask ≤ every applicable ceiling (R6) | The default buy rule |
| R3 | **Premium sell** | List at **1.15–1.30 × M7**; take any offer ≥ **1.20 × M7** right away | The default sell rule |
| R4 | **Cap-event sell** | Sell regardless of R3 when a cheaper substitute is about to unlock: you see players advertising grade-9 or grade-7 citizenship, or Nexon announces Orbis/El Nath | For GFA scrolls and gloves, and Overall stat scrolls and robes (§3) |
| R5 | **Stop-loss** | M3 < **0.80 × your buy price** for 3 days in a row **and** the thesis invalidator for that item has happened (§3) → sell at market | Without an invalidator, hold. Thin markets are noisy |
| R6 | **Substitute ceilings for scrolls** | Intermediate (60%, +2): pay ≤ **1.5 × Lesser price**. Greater (10%, +3): pay ≤ **0.5 × Lesser price**. Chaos: never buy for use | Expected stat per slot: Lesser 1.0, Intermediate 1.2, Greater 0.3, Chaos 0.4 with a 45% chance of destroying the item [calc]. Where a Lesser isn't buyable yet (GFA before grade 9), R6 doesn't apply; use R2 |
| R7 | **Never** | Pay above an NPC ceiling. Sell below an NPC floor. Trade with anyone offering real money or "cross-game" deals | RMT is bannable, and bans apply in both games [V-off N9, N8] |

### 1.4 Position sizing (balanced)

| Bucket | Share of liquid mesos | Use |
|---|---|---|
| Progression reserve | **≥ 40%** | Next weapon tier, Lesser scrolls, potions, Cash Shop convenience, and the launch character's funding |
| Hold-thesis inventory | **≤ 35%** | Items in §3 "Hold" |
| Active flips | **≤ 25%** | R1/R2 buys you plan to resell within 7 days |
| Any single item | **≤ 10%** | Concentration limit, because dupes and rollbacks happened in COT2 [V-off N6] |

---

## 2. Where and how to sell

### 2.1 Shop setup [V-dm unless tagged]
- **Free Market:** the FM Entrance has Fredrick (store banker) and Scrooge (storage) and leads to **11 rooms** (Free Market <1>–<11>). Teleport Rocks don't work there [V-dm].
- **Store Permit** (Cash Shop, untradeable; price [?] V-7): 16 items, 24 for seasonal permits. It works **in fields or the FM** and closes if a monster hits you [V-dm].
- **Placement:**
  - Use **FM room <1> or <2>** on the **highest-population channel** at your play time (V-27). Players walk in from the entrance, so the first rooms get the most traffic [B?].
  - Shops in town maps (Henesys, Kerning) are untested. The datamine says "fields", and whether towns count is [?]. Try one session and compare sales per hour.
  - **Avoid Channel 1** for shopping: it's where KPQ parties form [V-cbt], so it's crowded but not with buyers.
- **Shop title:** lead with the item class plus a price hint, e.g. `Mokbi/Kumbi • GFA60 • Sauna Robe`. Update it when stock changes.
- **Megaphones** (Cash Shop): only for single items worth more than about 2× the megaphone price.

### 2.2 The one-client constraint
You can run **one game at a time** [V-off N1], and two Classic clients aren't confirmed (V-16). **Shop time is farming time lost.**
- At the I/L farming estimate (~40–60k mesos/h net at Lv 30–38, ~75–100k at Lv 41–50, ~110–130k at Lv 51–60, mid case, `01` §0), a shop session must beat that to be worth staying in.
- **Shop while you're away from the keyboard**: meals and breaks. That's manual play, not automation.
- **Batch your selling**: one 20–30 min session per play day. List, adjust prices, close.
- Leaving the shop open while you're logged in and idle is not botting. Whether Classic has an **idle disconnect** is [?]; test it once.

### 2.3 Overnight selling: **only if offline vending exists**
- **If the Hired Merchant is sold at launch (V-8):**
  - Place it in an FM room before you log off. It's **removed 24 h after setup** [V-dm], so re-place it daily.
  - Collect unsold items and mesos from **Fredrick** or the mailbox [V-off N6].
  - Stock it with your R3 list (premium prices). Overnight buyers are price-takers.
  - **Risk:** COT2 had a bug that stripped equipment stats when collected from a closed merchant [V-off N6]. For the first week, sell **only scrolls, stars and ETCs** through it, not scrolled equipment.
- **If it isn't sold:** there's no overnight selling. Skip this section. Don't use workarounds.
- **The farmer as "FM merchant":** your farmer and Assassin share one account, and one account can only have one character logged in at a time [B legacy behaviour; not addressed by Nexon]. So the farmer can't sit in a shop while you play the Assassin. Its merchant role is **the offline Hired Merchant (if sold), or Store Permit sessions while the Assassin is logged off**. A shop on a second account with a second client is a gray area: don't do it without a written OK from Nexon (V-16, V-29).

---

## 3. What to sell, hold and buy (summary of the thesis test in `00` §4.7)

| Item group | Call | Why | Invalidator (what would trigger R5 or a re-think) |
|---|---|---|---|
| **Greater (10%) weapon scrolls** (3 per character from Hollow/Blackbull/Alligators; **class-gated**: your I/L gets Wand/Staff MATK Greater, the Assassin gets Claw ATT Greater) | **Sell the I/L's copies during Founder's Access** (keep one only if you'll gamble a slot on your own wand); the Assassin's Claw Greaters go to its claw | Quest supply keeps growing as more characters reach Lv 39–48, and they're worth 0.3 stat per slot in expectation | Quest rewards turn out untradeable (V-21) |
| **Intermediate defensive scrolls** (hat, top/bottom DEF, shoes evasion, shield, cape DEF) | **Sell any time; don't hold** | The Tulcus Lesser at 15k caps them | — |
| **Mokbi, Kumbi** | **Sell the surplus during Founder's Access**; keep 2–3 sets of each for the Assassin | Founder thieves need them while leveling; resale supply grows once founders upgrade | Prices keep rising after Oct 21 (F2P thief demand plus meso growth) → hold the rest |
| **Ilbi, Hwabi, Steely, Tobi** | **Hold** (or feed to the Assassin) | Boss- or rare-sourced; the whole thief population is the market. Hwabi has no confirmed launch-scope source [V-cbt 0 up/1 down] | Ilbi: many founders camp Mushmom. Steely/Tobi: M7 falls for 2+ weeks while Red Drake / Golem maps are crowded. Any: an Ossyria patch adds sources |
| **GFA/GFMA 60/10 scrolls and GFA'd gloves** | **Hold, then sell before the grade-9 cap event** | Unbuyable until citizenship grade 9 (Lv 52) | Contribution is cumulative and fast (V-9) → sell earlier; Nexon moves GFA Lesser to a lower grade |
| **Overall stat scrolls (Intermediate/Greater) and stat-scrolled Sauna Robes** | **Hold, then sell before the grade-7 cap event** | 10-slot all-class base, one per character | Same as GFA; robes turn out untradeable |
| **Earring stat and Cape stat Intermediate/Greater; Gloves Crit; Earring Crit Damage** | **Hold** | No NPC source until Arcforge Lv 8–10 crafters scale up | Arcforge becomes common |
| **Chaos scrolls** | **Hold** | No identified source; demand grows with population and mesos | Found to drop commonly |
| **Jane/Blackbull/Secret Book/Cursed Doll materials** | **Sell in week 2** (Oct 12–19) | Founders hit Lv 44–48 together | See §6 |
| **Crafting inputs** (Leather, Garnet, Black Crystal, Jr. Necki Skin, Pig's Ribbon, Animal Fur) | **Buy right after Oct 21** (R1/R2) | Cash-starved F2P sell low; founders' crafters need bulk | F2P keep their materials |
| Potions, Subi, Wolbi, arrows | **No trade** | NPC-pinned | — |

---

## 4. Period plans

### 4.1 Oct 6–10: founders only, mostly Lv 1–35
**Context:** few mesos per player, so mesos have high purchasing power. Everyone is leveling. NPC Lessers are available from day 1.

| Do | Rule |
|---|---|
| **Observe first.** Log asks for every watchlist item (§8) at least twice a day. No R2/R3 trades until n ≥ 5 | — |
| **Floor arbitrage** whenever you see it | R1 |
| **Sell:** surplus early equips (Lv 15–30 weapons and armor) to founders, but never above the NPC ceiling for NPC-sold gear, and vendor them when nobody pays more than the NPC (`01` §12). Also Intermediate defensive scrolls. **Keep** Claw ATT Intermediate for the Assassin | R3, R6 |
| **Keep:** Work Gloves (the farmer's GFMA base; a second pair for the Assassin's GFA), quest ETCs you'll need (`01` §12), and every star | — |
| **Don't buy** speculative stock yet. Your mesos go to the **Mithril Wand (22,000 at Flora)** and Wand MATK Lessers (25,000 at El Moth) first (progression reserve) | §1.4 |
| **Watch:** does the founder population keep growing? (Packages are sold until **Oct 14** [V-off N10].) Do trade tax and gates exist? (V-11) | — |

### 4.2 Oct 11–19: founders Lv 30–60, peak founder demand
**Context:**
- Founders hit 2nd job, Forgotten Hollow and the Lv 44–48 quest wall.
- First citizenship grades: 2–4, maybe 6.
- Quest scroll payouts begin.
- Mushmom and Zombie Mushmom farming starts.

| Do | Rule |
|---|---|
| **Sell the I/L's Wand/Staff MATK Greater scrolls** as soon as you get them, except one if you choose to gamble on your own wand | R3; take ≥ 1.2 × M7 immediately |
| **Sell quest materials into the Lv 44–48 wall**: Mushmom Spore, Medicine With Weird Vibes, Drake Skull, Dragon Skin, Sap of Ancient Tree, Stone Golem Rubble, Jr. Necki Skin, Malady's Frog | §6 rules |
| **Sell Mokbi/Kumbi surplus.** Keep **2–3 sets of each** for the Assassin | R3 |
| **Hold:** Ilbi/Hwabi/Steely/Tobi, GFA scrolls and GFA'd gloves, Overall stat scrolls, Earring/Cape stat scrolls, Chaos | §3 |
| **Value-buy** hold items only below 0.60 × M3, within the 35% hold bucket | R2, §1.4 |
| **Watch:** players advertising citizenship grade 7+, which is the cap-event warning (R4). Also any Nexon notice about trade rules, maintenance, or rollbacks | — |

### 4.3 Transition, Oct 20–22 (Grand Launch Wed Oct 21, 1:00 PM CDT)
**Context:**
- Founders hold the meso stock.
- **Many founders start alts with friends on Oct 21**, so founder mesos chase low-level gear for alts. That's a hypothesis to test: watch listing volume for Lv 10–30 gear and mid stars on Oct 21–22.
- F2P players arrive with 0 mesos and sell Lv 1–30 drops to raise cash.

| When | Do | Rule |
|---|---|---|
| **Oct 20** (last FA day) | Restock the shop with alt-friendly items: scrolled Work Gloves, Squishy Shoes, Lv 20–30 weapons, Mokbi/Kumbi, clean Sauna Robes. Price at R3 against your Founder's Access M7. Hold back the GFA/robe/Earring/Chaos inventory | R3 |
| **Oct 21, first 3 h** | Launch-day maintenance or queues are likely. **Don't panic-sell.** Log asks for the watchlist at least once. Check whether F2P share your world (V-3) | — |
| **Oct 21–22** | **Buy crafting inputs and lucky low-mob scrolls** from F2P below 0.70 × M3 or under the floor. **Sell to founder alts** at R3 | R1, R2, R3 |
| **Oct 22** | Compare M3 (Oct 20–22) with M7 (Founder's Access). If an item's M3 > 1.3 × M7, sell half of that hold | R3 |

### 4.4 After launch (Oct 23 onward)
**Context:**
- The meso stock grows fastest now, with the larger farming population. Expect **mild inflation in prices of scarce durables**.
- Citizenship cap events arrive: best case late Oct to early Nov; worst case months away.
- Orbis, El Nath and 3rd job come "gradually" [V-off N3].

| Do | Rule |
|---|---|
| **Hold scarce durables** (Ilbi/Hwabi/Steely/Tobi, Chaos, Earring/Cape stat scrolls) while M7 rises week over week | §3 |
| **GFA and Overall stat stock: sell into the first sign of grade-7/9 citizens**, or by **Nov 15** at the latest if contribution is cumulative (V-9) | R4 |
| **Weekly-donation ETCs from Lv 40+ mobs** (Drake Skull, Tortie Shell, Cold Eye Tail, Lorang Claw): F2P citizens need 100 a week and can't farm them yet | R3 |
| **Every patch note:** re-run the thesis. Ossyria content means re-pricing stars, GFA and Lv 50–70 weapons. The updater flags these in `reviewQueue` | Phase 5 |

---

## 5. Launch-character funding (cross-reference)
- `03_assassin_funding_checklist.csv` is the plan.
- `03_hunter_funding_checklist.csv` is archived (0.5 fallback, no longer used).

The farmer supplies stars and scrolls **internally first**, then market-buys at R2. Internal transfers go through shared storage (`04`). What an I/L farmer can and can't supply: Mokbi (Jr. Wraith), Claw ATT Intermediate (Zombie Mushroom), Kumbi (Lupin), Wolbi (Fire Boar), Steely (Red Drake, ice weak) and Ilbi (Mushmom, with the Cold Beam boss variant) — yes. Claw ATT Greater (class-gated quest reward) and Hwabi (no confirmed source) — no; buy those at R2.

---

## 6. Quest-material arbitrage (datamine-confirmed Classic quests only)

All quests below exist in the COT2 Classic data [V-dm M-Q]. **Check tradability on day 1 (V-21)**: an untradeable item has no market. Buyers are other players who would rather pay than farm.

| Item | Quests that need it (per character) | Buyer level band | Source (votes) [V-cbt] | NPC floor | Buy rule | Sell rule |
|---|---|---|---|---|---|---|
| **Mushmom Spore** | Jane's Second Challenge ×1 (Lv 44; gate to 15 Power Elixirs) | 44+ | Mushmom only (5); 1–1.5 h respawn | 400 | R2 | R3; it's the bottleneck, so list high (1.3 × M7) during Oct 12–19 |
| **Medicine With Weird Vibes** | Jane's First ×25, Second ×25; Flying Medicine ×50; What Pia Borrowed ×30; Kerning grade-9 weekly ×100 | 42+ | Wraith (1) | 48 | R2 | R3 in stacks of 25 |
| **Drake Skull** | Jane's First ×25; Third Material ×30; Luke ×30; Henesys grade-9 weekly ×100 | 41+ | Drake (5), Red Drake (4), Copper Drake (1) | 45 | R2 | R3 in stacks of 25–30 |
| **Dragon Skin** | Jane's Final ×20; Last Material ×10; Luke ×20; Pia's Present ×30; 23 crafting recipes | 41+ | Drake (4) | 200 | R2 | R3 |
| **Stone Golem Rubble** | Blackbull ×100 (Lv 48; Greater ATT scroll); Maya's Last Collection ×50 | 47+ | Stone Golem (1) | 56 | R2 | R3 in stacks of 50/100 |
| **Jr. Necki Skin** | Alligators 1 ×20 (Greater ATT scroll); Luke ×10; Dr. Faymus ×20; Leatherworking | 22+ | Jr. Necki (9) | 21 | R1/R2 | R3 in stacks of 20 |
| **Cursed Doll** | Rowen 50→200 (570 total; GFA60 at 150); Heart of Stillness ×30 | 36+ | Zombie Lupin (5) | 40 | R2 | R3 in stacks of 50 |
| **Sap of Ancient Tree** | Jane's Final ×10 | 44+ | Dark Axe Stump (6) | — | R2 | R3 |
| **Arwen's Glass Shoe** | Arwen (repeatable; Piece of Ice or Fairy Wing → wand crafting) | 29+ | Fire Boar (7); "worst drop rate" per community | 250 | R2 | R3 |
| **Lupin's Banana / Curse Eye Tail / Tablecloth** | Secret Book chain ×30 / ×50; Building a New House ×30; weeklies | 32–41 | Lupin (9) / Curse Eye (2) / Jr. Wraith (9) | — | R2 | R3 |

**Margin rule:** don't hold more than **2× the quantity you can sell in a week** at R3, based on your observed sales. Thin markets punish over-stocking.

---

## 7. Risks and what to do

| Risk | Signal | Response |
|---|---|---|
| Trade tax or gates announced (as China did, then reversed) | Nexon notice; first trade prompt (V-11) | Re-compute R1 margins net of tax. Prefer the Hired Merchant if its commission is lower |
| Dupe or rollback | Maintenance notice mentioning items or rollback | Freeze buying of affected items for 72 h. Don't hold > 10% in any item (§1.4) |
| Hired Merchant stat-loss bug returns | Patch notes or community reports | Sell equipment only face to face or through the Store Permit |
| Bots flood drop-only items | M7 falling for 2+ weeks with very high listing counts | Sell holds of that item (R5 with the invalidator met) |
| Datamine drift at launch (prices, scroll odds, quest rewards) | meowdb changelog date changes (V-30) | Updater adds it to the review queue; re-check §1.2 anchors |
| Citizenship turns out faster or slower | V-9 | Move the R4 cap-event dates in §4.4 |

---

## 8. Watchlist (seed for the dashboard; prices left blank)

Log columns: `datetime, channel, item, ask_or_sale, price, qty, note`.

| ID | Item | Group | NPC floor | NPC/Lesser ceiling | Call |
|---|---|---|---|---|---|
| W01 | Mokbi | star | 1,000 | — | Sell surplus in Founder's Access |
| W02 | Kumbi | star | 1,500 | — | Sell surplus in Founder's Access |
| W03 | Tobi | star | 2,500 | — | Hold |
| W04 | Steely | star | 10,000 | — | Hold |
| W05 | Ilbi | star | 20,000 | — | Hold |
| W06 | Hwabi | star | 25,000 | — | Hold |
| W07 | Gloves ATT Intermediate (GFA60) | scroll | 1 | grade 9: 50k Lesser | Hold → R4 |
| W08 | Gloves ATT Greater (GFA10) | scroll | 1 | — | Hold → R4 |
| W09 | Claw ATT Intermediate | scroll | 1 | 1.5 × 50k Lesser | Sell or keep for the Assassin |
| W10 | Wand/Staff MATK Greater | scroll | 1 | 0.5 × 25k | Sell (keep one only to gamble on your wand) |
| W11 | Overall DEX/STR/LUK/INT Intermediate | scroll | 1 | grade 7: 35k Lesser | Hold → R4 |
| W12 | Earring INT/LUK Intermediate | scroll | 1 | — | Hold |
| W13 | Any Chaos scroll | scroll | 1 | — | Hold |
| W14 | Sauna Robe (clean) | equip | 5,400 | — | Sell to founder alts on Oct 20–22 |
| W15 | Work Gloves (clean / scrolled) | equip | 1,200 | — | Keep 1; sell scrolled ones to alts |
| W16 | Squishy Shoes | equip | 1,590 | — | Sell to alts |
| W17 | Mushmom Spore | quest | 400 | — | Sell Oct 12–19 |
| W18 | Medicine With Weird Vibes | quest | 48 | — | Sell in stacks |
| W19 | Drake Skull | quest | 45 | — | Sell in stacks |
| W20 | Dragon Skin | quest | 200 | — | Sell in stacks |
| W21 | Stone Golem Rubble | quest | 56 | — | Sell in stacks |
| W22 | Jr. Necki Skin | quest | 21 | — | Buy low, sell in stacks |
| W23 | Cursed Doll | quest | 40 | — | Sell in stacks |
| W24 | Garnet Ore | ore | 40 | — | Buy after Oct 21 |
| W25 | Black Crystal Ore | ore | 500 | — | Buy after Oct 21 |
| W26 | Leather | material | — | — | Buy after Oct 21 |
| W27 | Lv 35–50 wands and staves (Fairy Wand, Cromi, Arc Staff) | equip | — | — | Buy for the I/L at R2 (check the LUK requirement, `01` §7) |
