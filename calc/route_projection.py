# Fighter Founder's Access projection.
# Inputs: meowdb EXP table (cumulative-including-row values from the warrior notes, used as 5-level segment sizes),
# meowdb Fighter Advisor modeled EXP/min, community meso reports (~2x mob level per kill).
segs = [
 # (label, EXP in segment, model EXP/min, mob lv, mob exp, upkeep k/h low, high)
 ("30-35", 699662, 1770, 15, 28, 10, 20),   # Line 1 Area 1 Bubbling
 ("35-40", 1212830, 3857, 23, 43, 15, 30),  # Ant Tunnel II Zombie/Horny
 ("40-45", 1969046, 4309, 26, 48, 20, 35),  # Ant Tunnel Park Evil Eye/Zombie
 ("45-50", 3035432, 5153, 32, 62, 20, 35),  # Burnt Land Fire Boar
 ("50-55", 4176375, 7883, 41, 99, 25, 40),  # Monkey Forest II Zombie Lupin
 ("55-60", 5453169, 7939, 50, 150, 25, 40), # Forest of Evil II Malady/Zombie Lupin mix
 ("60-65", 7120304, 10557, 50, 150, 25, 40),
 ("65-70", 9297125, 9743, 48, 132, 25, 40), # Perilous Descent III Duskmander/Echopus
]
# Lv 1-30: tester data 14 h (fast) to 20 h (slow); EXP to reach 30 = 548,637; mobs ~Lv 15-24, mesos/EXP ~1.07
pre30 = {"fast": 14.0, "slow": 20.0}
pre30_exp = 548637
budget = 76.0
scen = {
 "low":  dict(r=0.55, p=0.6, mult=1.7, up="high", pre="slow"),
 "mid":  dict(r=0.70, p=0.8, mult=2.0, up="mid",  pre="slow"),
 "high": dict(r=0.80, p=1.0, mult=2.0, up="low",  pre="fast"),
}
for name, s in scen.items():
    t = pre30[s["pre"]]
    # pre-30 mesos: EXP x (mesos/EXP ~ mult*lv/exp, ~1.07 at mult 2) x p ; upkeep ~5-15k/h
    ratio_pre = s["mult"] * 20 / 40   # Lv20-ish mobs, ~40 EXP
    gross = pre30_exp * ratio_pre * s["p"]
    up_pre = {"low": 5, "mid": 10, "high": 15}[s["up"]] * 1000 * t
    net = gross - up_pre
    lv_end = 30
    rows = [("1-30", t, gross, up_pre)]
    for label, exp, model, mlv, mexp, ulo, uhi in segs:
        rate = model * 60 * s["r"]           # EXP/h
        hrs = exp / rate
        up = {"low": ulo, "mid": (ulo + uhi) / 2, "high": uhi}[s["up"]] * 1000
        frac = 1.0
        if t + hrs > budget:
            frac = (budget - t) / hrs
        g = exp * frac * (s["mult"] * mlv / mexp) * s["p"]
        u = up * hrs * frac
        rows.append((label, hrs * frac, g, u))
        gross += g; net += g - u; t += hrs * frac
        if frac < 1.0:
            lv_end = int(label.split("-")[0]) + 5 * frac
            break
        lv_end = int(label.split("-")[1])
    print(f"== {name}: r={s['r']} p={s['p']} mesos/kill={s['mult']}xLv  -> level at 76 h ~ {lv_end:.1f}")
    for lab, h, g, u in rows:
        print(f"  {lab:6s} {h:5.1f} h  gross {g/1e6:5.2f}M  upkeep {u/1e6:4.2f}M  net/h {(g-u)/max(h,0.01)/1e3:6.0f}k")
    print(f"  TOTAL gross {gross/1e6:.2f}M  net {net/1e6:.2f}M  hours {t:.1f}")
