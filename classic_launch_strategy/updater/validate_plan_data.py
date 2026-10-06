"""Validate data/plan_data.js after an edit. Exit code 0 = OK, 1 = problem.

Checks that the file is `window.PLAN_DATA = {...};` with valid JSON inside, that the
required top-level keys exist, that fact records carry `tier` and `source`, that IDs
are unique (checklist IDs are what users' saved checkmarks key on), and that
meta.version looks like semver.
"""
import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
PATH = ROOT / "data" / "plan_data.js"
PREFIX = "window.PLAN_DATA = "
REQUIRED = ["meta", "sources", "classes", "route", "spPlan", "farmingTargets", "watchlist",
            "checklist", "routine", "changelog", "reviewQueue", "openQuestions"]
FACT_LISTS = ["classes", "route", "farmingTargets", "watchlist", "checklist"]
TIERS = {"V", "B", "?"}


def main() -> int:
    text = PATH.read_text(encoding="utf-8").strip()
    if not text.startswith(PREFIX) or not text.endswith(";"):
        print("FAIL: file must be `window.PLAN_DATA = {...};`")
        return 1
    try:
        data = json.loads(text[len(PREFIX):-1])
    except json.JSONDecodeError as e:
        print(f"FAIL: JSON error: {e}")
        return 1

    problems = [f"missing key: {k}" for k in REQUIRED if k not in data]
    for key in FACT_LISTS:
        ids = set()
        for rec in data.get(key, []):
            rid = rec.get("id", "?")
            if rec.get("tier") not in TIERS:
                problems.append(f"{key}/{rid}: tier must be one of V, B, ?")
            if not rec.get("source"):
                problems.append(f"{key}/{rid}: missing source")
            if rid in ids:
                problems.append(f"{key}: duplicate id {rid}")
            ids.add(rid)
    if not re.fullmatch(r"\d+\.\d+\.\d+", str(data.get("meta", {}).get("version", ""))):
        problems.append("meta.version must look like 1.2.3")
    for field in ("lastChecked", "lastUpdated"):
        if not data.get("meta", {}).get(field):
            problems.append(f"meta.{field} missing")
    rq_ids = [r.get("id") for r in data.get("reviewQueue", [])]
    if len(rq_ids) != len(set(rq_ids)):
        problems.append("reviewQueue: duplicate id")

    if problems:
        print("FAIL:\n  " + "\n  ".join(problems))
        return 1
    print(f"OK: version {data['meta']['version']}, {len(data['checklist'])} checklist items, "
          f"{len(data['reviewQueue'])} review items, {len(data['changelog'])} changelog entries")
    return 0


if __name__ == "__main__":
    sys.exit(main())
