# Dual-Character Operations (from Oct 21)

Version 0.1 · 2026-10-02. Tags and source keys are as in `00_classic_world_verified_intel.md`.

Two characters:
- **Fighter**: farmer and bank, Henesys citizen.
- **Launch character**: Assassin (Kerning citizen), or Hunter (Henesys citizen) if no friend plays an AoE class.

**Baseline: one client at a time.** Running MapleStory and Classic together is not allowed, and two Classic clients aren't addressed anywhere [V-off N1; ? V-16].

---

## 1. Character slots (tests: 3 per account [V-off N7, N4]; launch [?] V-2)

| Slot | Character | Role |
|---|---|---|
| 1 | Fighter | Farmer, bank, boss runs, shop |
| 2 | Launch character | Levels with friends; funded by slot 1 |
| 3 | Empty at first | Becomes a **storage mule** only if shared storage (50 slots, or 150 with coupons) runs out. Each mule adds 4 inventory tabs (size [?] V-6). If launch allows more than 3 slots, use the extra for the mule and keep slot 3 free |

---

## 2. Moving mesos and items between your characters

### 2.1 Confirmed rules
- **Shared account storage** holds items and mesos for every character on the account [V-dm M-NPC].
  - Storage NPCs: Mr. Lee (Henesys Park), Mr. Hong (Kerning), Mr. Kim (Lith), Mr. Park (Ellinia), Mr. Wang (Perion), Mr. Oh (Sleepywood), Scrooge (FM Entrance), Cave Fairy (Forgotten Hollow).
- **Deposit fee: 100 mesos per item** [V-dm].
  - A citizenship grade cuts it 5% per grade (down to 50 at grade 10), but **only at your own town's storage**. For the Fighter that's Henesys, Mr. Lee.
  - Unknown [?] (V-5): the withdrawal fee, the meso deposit/withdraw fee, and whether a stack counts as one item.
- **Cash and cosmetic items** move through the **Cash Inventory**, same account and same world only [V-off N10].
- **With one client you can't trade your own characters face to face.** Storage is the only route.

### 2.2 Transfer run (about 3 min)
1. On the Fighter, go to **Henesys storage (Mr. Lee)** for the citizenship discount.
2. Deposit the items in order: **stars and scrolls the launch character needs this week** → **hold-inventory overflow** → **quest ETC stock**.
3. Stack items before depositing.
4. **Deposit mesos** for the launch character's weekly allowance (§4).
5. Log out and switch to the launch character. Withdraw at its nearest storage: Kerning (Mr. Hong) for the Assassin, Henesys for the Hunter.

Do **one transfer run per play day at most**. Batching keeps fees and switching time down.

### 2.3 Storage slot budget (assumes 50 slots until V-4 says otherwise)

| Use | Slots | Notes |
|---|---|---|
| Launch-character funding queue (stars, scrolls, next weapon) | 12 | Refill from the Fighter weekly |
| Hold-thesis inventory (Ilbi/Hwabi/Steely/Tobi, GFA, Overall stat, Earring/Cape stat, Chaos) | 20 | `02` §3 |
| Quest-ETC stock for sale (Mushmom Spore, Medicine, Skulls, Skins, Rubble, Necki Skins, Dolls) | 10 | Sell in stacks (`02` §6) |
| Buffer | 8 | Drops waiting for a decision |

Buy the **Storage Room 5-slot Coupon** (Cash Shop) when the buffer stays full for 3+ days. "Whatever pays off" applies: each coupon must hold items worth more than its price.

---

## 3. Bank rules (Fighter)
- The Fighter holds the account's meso stock and its hold inventory. It follows the buckets in `02` §1.4: ≥40% progression reserve, ≤35% holds, ≤25% flips, ≤10% in any one item.
- The **progression reserve covers both characters**. The launch character's funding is a line item, not a separate pile.
- **Internal supply first:** the Fighter's own drops cover the launch character's needs before any market purchase. Stars from Jr. Wraith, Lupin, Dark Stone Golem and the Mushmoms; Claw/Bow ATT Intermediate; GFA from the Cursed Dolls and Jane quests; Henesys-only NPC scrolls such as Earring Crit Damage Lesser.

---

## 4. Funding the launch character [calc; prices are NPC values, V-dm]

| Launch-character level | Assassin needs | Source |
|---|---|---|
| 10–30 | Subi (500/set), Garnier → Steel Titans (5,000 / 7,000), Lemons | NPC; the launch character can pay its own way |
| 22+ | **Wolbi** (1,000/set at Kerning grade 3) | NPC (Kerning citizen) |
| 30 | **Adamantium Guards** (27,600), Mokbi/Kumbi | NPC; Fighter stash |
| 35–50 | Dark Guardian → Dark Slain (craft or market), **Claw ATT Lesser ×7 = 350,000**, Work Gloves + GFA, Tobi/Ilbi | El Moth; Fighter quest copies and boss drops; market at R2 |
| Ongoing | **MP potions: ~29k–48k mesos per hour** of Lucky Seven play [calc, thief notes] | The Fighter's farming |

- **Rule of thumb** [calc]: the Fighter nets ~40k–290k mesos/h at Lv 35+ (`01` §0). So **1 Fighter hour funds about 1–10 launch-character hours** of potion upkeep before gear (mid ≈ 4): 40k ÷ 48k ≈ 0.8 at worst, 290k ÷ 29k ≈ 10 at best.
- **Weekly allowance:** the potion cost of the launch character's expected weekly hours (§5) plus the next gear milestone in the table. Deposit it in one transfer run.

The Hunter needs less: arrows cost 1 meso and Soul Arrow arrives at Lv 34. See `03_hunter_funding_checklist.csv`.

---

## 5. Daily schedule (from Oct 21; one character at a time)

Your friends' play times are unknown, so these are templates. Put the **"with friends"** block wherever they play, and the Fighter blocks around it. **Limit yourself to 2–3 character switches per session**; each logout and login costs a minute or two [?].

### Weekday (4 h)
| Block | Character | What |
|---|---|---|
| 0:00–0:20 | Fighter | Citizenship daily (and VIP daily from grade 5) · boss check (Mushmom/Zombie Mushmom channel and time log) · log watchlist prices · **transfer run** (§2.2) |
| 0:20–3:20 | Launch character | Citizenship daily · level with friends. When they're offline, solo on the class map (`01` §9) |
| 3:20–4:00 | Fighter | Farm block, **or** a 20–30 min shop session if you have stock to clear (`02` §2) |

### Weekend day (8 h)
| Block | Character | What |
|---|---|---|
| 0:00–2:00 | Fighter | Farm block (best map for its level) + boss loop |
| 2:00–2:30 | Fighter | Shop session or listing round; weekly citizenship donation; **transfer run** |
| 2:30–7:30 | Launch character | With friends; weekly donation; KPQ if the friend group has 4 players and V-19 showed it's worth it |
| 7:30–8:00 | Fighter | Restock, log prices, export the dashboard data (Phase 4) |

### Overnight
- **If the Hired Merchant is sold (V-8):** before logging off, place it with the Fighter in an FM room, stocked with `02` R3 listings. It runs 24 h. Collect at Fredrick the next day.
- **If it isn't sold:** nothing runs overnight. Don't use any automation; it's bannable [V-off N9].

### If two Classic clients turn out to be allowed (V-16, explicit confirmation only)
- The Fighter can sit in an FM shop while you play the launch character.
- Direct trades between your own characters replace storage runs, which saves the 100-meso fees.
- Don't do this on a guess. Get a written answer from Nexon support or the FAQ first.

---

## 6. Weekly checklist
- [ ] Citizenship weekly donation for **both** characters. Each needs 100 of its grade's ETC; the Fighter farms Henesys-list ETCs, and the launch character farms or buys its own.
- [ ] Mushmom / Zombie Mushmom kills logged (channel, time, drops).
- [ ] Sell quest-ETC stacks (`02` §6).
- [ ] Review the hold list against R4 (cap events) and R5 (stop-loss).
- [ ] Export the dashboard price log (JSON/CSV) and share it if you want the plan re-tuned.
- [ ] Check the dashboard's Updates tab (Phase 5) for new patch notes.
