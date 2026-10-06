"""Write the updater's permission allowlist for both places a run can start.

Scheduled runs from the desktop app start in the parent folder (maplestory-plan);
update_now.bat starts in this folder (classic_launch_strategy). Each gets the same
narrow rules, with file paths written relative to its own project root.

Usage: python tools/write_allowlists.py
"""
import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent          # classic_launch_strategy
PARENT = ROOT.parent                                           # maplestory-plan
ROOT_POSIX = ROOT.as_posix()                                   # C:/Users/.../classic_launch_strategy

EDITABLE = ["data/plan_data.js", "00_classic_world_verified_intel.md", "01_early_access_route.md",
            "02_market_playbook.md", "04_dual_character_ops.md", "05_launch_day_verification.md",
            "03_assassin_funding_checklist.csv", "03_hunter_funding_checklist.csv", "CHANGELOG.md",
            "updater/state.json", "updater/sources.json"]
PROTECTED = ["index.html", "updater/UPDATER_RULES.md", "updater/validate_plan_data.py", "tools/**", ".claude/**"]
DOMAINS = ["g.nexonstatic.com", "www.nexon.com", "support-maplestory.nexon.com", "playersupport.nexon.com",
           "api.steampowered.com", "store.steampowered.com", "www.youtube.com", "meowdb.com", "niadb.com",
           "github.com", "mapleclassic.wiki", "maplestorywiki.net", "maplestory.io", "www.gosugamers.net"]
GIT = f"git -C {ROOT_POSIX}"
COMMANDS = [f"{GIT} status", f"{GIT} status *", f"{GIT} diff", f"{GIT} diff *", f"{GIT} add -A",
            f"{GIT} commit -m *", f"{GIT} log *",
            f"python {ROOT_POSIX}/updater/validate_plan_data.py",
            # short forms, valid when the session starts inside the plan folder (update_now.bat)
            "git status", "git diff", "git diff *", "git add -A", "git commit -m *", "git log *",
            "python updater/validate_plan_data.py"]
DENIED_COMMANDS = ["git push", "git push *", "git reset *", "git checkout *", "git config *",
                   f"{GIT} push", f"{GIT} push *", f"{GIT} reset *", f"{GIT} checkout *", f"{GIT} config *"]


def rules_for(prefix: str) -> dict:
    """prefix = path of the plan folder relative to the settings' project root ('' or 'classic_launch_strategy/')."""
    allow, deny = [], []
    for form in ("/", ""):                       # project-root-relative and cwd-relative spellings
        allow += [f"Read({form}{prefix}**)", f"Glob({form}{prefix}**)", f"Grep({form}{prefix}**)"]
        allow += [f"Edit({form}{prefix}{p})" for p in EDITABLE]
        deny += [f"Edit({form}{prefix}{p})" for p in PROTECTED]
    allow += ["WebSearch"] + [f"WebFetch(domain:{d})" for d in DOMAINS]
    for tool in ("Bash", "PowerShell"):
        allow += [f"{tool}({c})" for c in COMMANDS]
        deny += [f"{tool}({c})" for c in DENIED_COMMANDS]
    allow += ["Bash(date -Iseconds)", "PowerShell(Get-Date -Format o)"]
    return {"permissions": {"allow": allow, "deny": deny}}


def write(settings_dir: pathlib.Path, prefix: str) -> None:
    path = settings_dir / ".claude" / "settings.json"
    path.parent.mkdir(exist_ok=True)
    existing = json.loads(path.read_text(encoding="utf-8")) if path.exists() else {}
    existing["permissions"] = rules_for(prefix)["permissions"]   # this file's permissions are owned by this script
    path.write_text(json.dumps(existing, indent=2) + "\n", encoding="utf-8")
    p = existing["permissions"]
    print(f"wrote {path}: {len(p['allow'])} allow, {len(p['deny'])} deny")


if __name__ == "__main__":
    write(ROOT, "")
    write(PARENT, "classic_launch_strategy/")
