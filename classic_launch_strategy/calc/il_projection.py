# I/L Wizard Founder's Access projection (v0.6.0). Replaces the Fighter scripts as the plan's projection;
# route_projection.py / bracket_rates.py / day_plan.py are kept only as the Fighter baseline for comparison.
#
# Inputs (tags as in 00_classic_world_verified_intel.md):
#  - EXP to next level: meowdb EXP table (Lv 1-49 [V-cbt M-EXP], Lv 50+ legacy reference [B]).
#    Fixed off-by-one: the EXP to REACH level L is the cumulative value of row L-1 (review T5-07).
#  - Lv 30+ EXP/h and net mesos/h per level: the review's I/L break-even model (review/REVIEW_2026-10-02.md,
#    scratch il_breakeven.py, SP order "R"): mid case = 810 ms casts, 4 targets per Thunder Bolt (x0.85 below TB 16),
#    2.0 s walk between packs, real-play factor 0.65, Lemon/Orange at 1 meso per MP, mesos = 2.0 x mob Lv x 0.8
#    drop chance, accuracy from meowdb's hit formula [model]. It is 2.5-5x BELOW meowdb's Training Advisor EXP/min,
#    which assumes continuous casting, so treat it as conservative.
#  - Lv 1-30: COT tester pace, Lv 30 after 14-20 h [V-cbt M-EXP]. 1st-job mesos are roughly break-even [calc, T11].
#  - Equipment vendoring: E = p_equip x median NPC sell value of the mob band [V-dm item-db; review T12]. p_equip is
#    NOT published anywhere; the 0 / 0.5% / 1% rows are assumptions to replace with your V-39 tally.
#  - Grind hours = 76 h budget minus shop, quest turn-in and day-1 queue time (review T5-10).

def exp_tnl(L):
    # meowdb EXP table formula, checked against two published rows below
    t = {}
    for l in range(1, 100):
        if l <= 5:
            e = (l * l // 2 + 15) * l
        elif l <= 50:
            q = l * l // 3
            e = (q + 19) * q
        else:
            e = int(t[l - 1] * 1.0548)
        t[l] = e
    return t[L]

assert exp_tnl(49) == 655200 and exp_tnl(29) == 83720
assert sum(exp_tnl(l) for l in range(1, 30)) == 548637            # EXP to reach Lv 30
assert sum(exp_tnl(l) for l in range(30, 35)) == 621146           # 30 -> 35 (the Fighter script used 699,662)

# (level, training mob, mob EXP, EXP/h mid, net mesos/h mid) from the break-even model, SP order R
SIM = [
    (30, "Horny Mushroom", 41, 59590, 38885), (31, "Horny Mushroom", 41, 59937, 38966),
    (32, "Horny Mushroom", 41, 61798, 39050), (33, "Zombie Mushroom", 45, 66285, 39131),
    (34, "Horny Mushroom", 41, 73096, 39215), (35, "Fire Boar", 62, 79700, 39296),
    (36, "Zombie Mushroom", 45, 101721, 47170), (37, "Horny Mushroom", 41, 109947, 62038),
    (38, "Jr. Wraith", 70, 120389, 60688), (39, "Jr. Wraith", 70, 125038, 66888),
    (40, "Zombie Mushroom", 45, 139240, 64818), (41, "Jr. Wraith", 70, 147901, 75037),
    (42, "Jr. Wraith", 70, 147901, 75202), (43, "Jr. Wraith", 70, 147901, 78161),
    (44, "Evil Eye", 50, 160763, 79705), (45, "Evil Eye", 50, 167088, 79813),
    (46, "Horny Mushroom", 41, 181012, 98574), (47, "Horny Mushroom", 41, 181012, 98672),
    (48, "Horny Mushroom", 41, 184688, 98753), (49, "Horny Mushroom", 41, 194507, 98834),
    (50, "Horny Mushroom", 41, 204218, 98918), (51, "Jr. Wraith", 70, 230420, 112247),
    (52, "Jr. Wraith", 70, 232340, 114745), (53, "Jr. Wraith", 70, 232340, 115619),
    (54, "Jr. Wraith", 70, 232340, 116493), (55, "Jr. Wraith", 70, 232340, 117362),
    (56, "Jr. Wraith", 70, 232340, 118231), (57, "Jr. Wraith", 70, 232340, 121600),
    (58, "Zombie Mushroom", 45, 276155, 125934), (59, "Zombie Mushroom", 45, 278270, 131836),
]
# EXP/h uses the best-EXP map; net uses the best-meso map of that level (they differ by under 1 level of pace).
# Median NPC sell value of equips on the drop lists, by mob level band [V-dm item-db via review T12]
EQUIP_V = {(20, 30): 4200, (31, 40): 4900, (41, 50): 6600}
mob_lv = {"Horny Mushroom": 22, "Zombie Mushroom": 24, "Evil Eye": 27, "Fire Boar": 32, "Jr. Wraith": 34}

def vbar(mob):
    lv = mob_lv[mob]
    for (a, b), v in EQUIP_V.items():
        if a <= lv <= b:
            return v
    return 4200

SCEN = {
    #        hours to Lv 30, grind budget, EXP mult, net mult, pre-30 net/h
    "low":  dict(pre30=20.0, budget=66.0, xm=0.80, nm=0.50, pre_net=-3000),
    "mid":  dict(pre30=17.0, budget=69.0, xm=1.00, nm=1.00, pre_net=3000),
    "high": dict(pre30=14.0, budget=72.0, xm=1.25, nm=1.60, pre_net=8000),
}
P_EQUIP = (0.0, 0.005, 0.01)

def run(s, p_equip):
    t = s["pre30"]; lv = 30.0
    mesos = s["pre_net"] * t
    curve = [(0.0, 1.0), (t, 30.0)]
    for L, mob, mexp, exph, neth in SIM:
        need = exp_tnl(L)
        rate = exph * s["xm"]
        hrs = need / rate
        kills_h = rate / mexp
        per_h = neth * s["nm"] + kills_h * p_equip * vbar(mob)
        if t + hrs >= s["budget"]:
            frac = (s["budget"] - t) / hrs
            mesos += per_h * hrs * frac
            lv = L + frac
            t = s["budget"]
            curve.append((t, lv))
            break
        t += hrs; mesos += per_h * hrs; lv = L + 1
        curve.append((t, float(lv)))
    return lv, mesos, curve

def interp(x, pts):
    for (x0, y0), (x1, y1) in zip(pts, pts[1:]):
        if x <= x1:
            return y0 + (y1 - y0) * (x - x0) / (x1 - x0) if x1 > x0 else y1
    return pts[-1][1]

if __name__ == "__main__":
    print("I/L Founder's Access projection (grind hours = 76 h minus non-grind time)")
    print(f"{'scenario':8s} {'p_equip':>8s} {'Lv Oct 20':>9s} {'net mesos':>10s}")
    for name, s in SCEN.items():
        for p in P_EQUIP:
            lv, m, _ = run(s, p)
            print(f"{name:8s} {p:8.3%} {lv:9.1f} {m/1e6:9.2f}M")
    # Day-by-day level targets. Each day's grind hours are scaled from its play hours by budget/76.
    days = [("Oct 6", 4), ("Oct 7", 4), ("Oct 8", 4), ("Oct 9", 4), ("Oct 10", 8), ("Oct 11", 8), ("Oct 12", 4),
            ("Oct 13", 4), ("Oct 14", 4), ("Oct 15", 4), ("Oct 16", 4), ("Oct 17", 8), ("Oct 18", 8),
            ("Oct 19", 4), ("Oct 20", 4)]
    curves = {k: run(s, 0.0)[2] for k, s in SCEN.items()}
    print("\nDay       cum h   low  mid  high   (level, floor)")
    cum = 0
    out = []
    for d, h in days:
        cum += h
        lv = []
        for k, s in SCEN.items():
            g = cum * s["budget"] / 76.0
            pts = curves[k]
            # Lv 1-30 grows roughly with cumulative EXP; approximate with the tester milestones (Lv 10 at ~15%, 20 at ~40% of pre-30 time)
            if g <= s["pre30"]:
                f = g / s["pre30"]
                lvl = 1 + 9 * min(f / 0.15, 1) if f <= 0.15 else (10 + 10 * (f - 0.15) / 0.25 if f <= 0.40 else 20 + 10 * (f - 0.40) / 0.60)
            else:
                lvl = interp(g, pts)
            lv.append(int(lvl))
        out.append([d, cum] + lv)
        print(f"{d:8s} {cum:5d}  {lv[0]:4d} {lv[1]:4d} {lv[2]:4d}")
    print("\nDAYPLAN =", out)
