---
name: windows-tool-gotchas
description: "Tool quirks on the user's Windows PC (python3 Store stub, curl alias, claude CLI path)"
metadata:
  node_type: memory
  type: project
  originSessionId: 5ec692d5-1d7b-495c-b174-f1e7f285b1bb
  modified: 2026-10-02T06:37:47.111Z
---

On this PC (checked 2026-10-02):
- `python3` points to the Microsoft Store stub in WindowsApps. Real Python 3.11 is `python` (`C:\Users\TonyH\AppData\Local\Programs\Python\Python311\python.exe`), and `py` also works.
- In PowerShell 5.1, `curl` is an alias for Invoke-WebRequest. Use `curl.exe` or Git Bash for real curl.
- The user's own terminal is Windows PowerShell 5.1, which rejects `&&`/`||`. Any command meant for the user to run should be one per line or code block, never chained with `&&`. (On 2026-10-02 a chained `git add . && git commit && git push` failed with a parser error.)
- The `claude` CLI is installed at `C:\Users\TonyH\.local\bin\claude.exe` and is on PATH, so headless `claude -p` runs are possible.

**Why:** scripts that call `python3` or PowerShell `curl` fail or behave unexpectedly here.

**How to apply:** use `python`/`py` and `curl.exe` (or Git Bash) in commands and generated scripts. Related: [[maplestory-classic-launch-plan]].
