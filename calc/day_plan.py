# Level per day for the 76 h Founder's Access budget. Milestones come from route_projection.py output
# (pre-30 pace from COT tester reports: Lv10 ~2-3h, Lv20 ~6-7h, Lv30 14-20h).
sc = {
 "low":  [(0,1),(3,10),(7,20),(20,30),(32,35),(41.5,40),(55.3,45),(73.2,50),(76,50.9)],
 "mid":  [(0,1),(2.5,10),(6.5,20),(20,30),(29.4,35),(36.9,40),(47.8,45),(61.8,50),(74.4,55),(76,55.5)],
 "high": [(0,1),(2,10),(6,20),(14,30),(22.2,35),(28.8,40),(38.3,45),(50.6,50),(61.6,55),(75.9,60)],
}
days = [("Tue Oct 6",4),("Wed Oct 7",4),("Thu Oct 8",4),("Fri Oct 9",4),("Sat Oct 10",8),("Sun Oct 11",8),
        ("Mon Oct 12",4),("Tue Oct 13",4),("Wed Oct 14",4),("Thu Oct 15",4),("Fri Oct 16",4),("Sat Oct 17",8),
        ("Sun Oct 18",8),("Mon Oct 19",4),("Tue Oct 20",4)]

def interp(x, pts):
    for (x0, y0), (x1, y1) in zip(pts, pts[1:]):
        if x <= x1:
            return y0 + (y1 - y0) * (x - x0) / (x1 - x0)
    return pts[-1][1]

cum = 0
for d, h in days:
    cum += h
    lv = [interp(cum, sc[k]) for k in ("low", "mid", "high")]
    print(f"{d:11s} +{h}h cum {cum:3d}h  Lv low {lv[0]:4.1f} mid {lv[1]:4.1f} high {lv[2]:4.1f}")
