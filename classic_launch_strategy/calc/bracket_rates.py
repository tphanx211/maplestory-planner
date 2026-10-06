# kills/h = modeled EXP/min x 60 x realism / mob EXP ; mesos/h gross = kills/h x (1.7..2.3 x mob Lv) x drop chance (0.6..1.0)
rows = [
 ("10-20 Swordman, Line 1 Area 1 (Bubbling)", 1000, 1367, 15, 28),
 ("21-30 Swordman, Ant Tunnel III (Zombie/Horny)", 1396, 1762, 23, 43),
 ("30-34 Fighter, Line 1 Area 1 (Bubbling)", 1770, 1770, 15, 28),
 ("35-39 Fighter, Ant Tunnel II (Zombie/Horny)", 3857, 3857, 23, 43),
 ("40-44 Fighter, Ant Tunnel Park (Evil Eye/Zombie)", 4309, 4309, 26, 48),
 ("45-49 Fighter, Burnt Land I/III (Fire Boar)", 5153, 5153, 32, 62),
 ("50-54 Fighter, Monkey Forest II (Zombie Lupin)", 7883, 7883, 41, 99),
 ("55-64 Fighter, Forest of Evil II (Malady/Z.Lupin)", 7939, 10557, 50, 150),
 ("65-70 Fighter, Perilous Descent III (Dusk/Echo)", 9743, 11089, 48, 132),
]
for name, lo, hi, lv, ex in rows:
    k_lo = lo * 60 * 0.55 / ex; k_hi = hi * 60 * 0.80 / ex
    m_lo = k_lo * 1.7 * lv * 0.6; m_hi = k_hi * 2.3 * lv * 1.0
    e_lo = lo * 60 * 0.55; e_hi = hi * 60 * 0.80
    print(f"{name:52s} EXP/h {e_lo/1e3:5.0f}k-{e_hi/1e3:5.0f}k  kills/h {k_lo:5.0f}-{k_hi:5.0f}  gross mesos/h {m_lo/1e3:4.0f}k-{m_hi/1e3:4.0f}k  mesos/kill {1.7*lv*0.6:.0f}-{2.3*lv:.0f}")
