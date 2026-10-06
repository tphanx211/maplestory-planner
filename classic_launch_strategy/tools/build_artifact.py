"""Build the claude.ai Artifact copy of the dashboard from index.html.

The Artifact platform wraps the page in its own <!doctype html><html><head>...<body>
skeleton, so this strips those tags and keeps <title>, <style>, the body content and
the scripts. data/plan_data.js is published alongside it as a supporting file.

Usage: python tools/build_artifact.py <output.html>
"""
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent


def main() -> int:
    if len(sys.argv) != 2:
        print(__doc__)
        return 1
    html = (ROOT / "index.html").read_text(encoding="utf-8")
    for pattern in (r"<!doctype html>\s*", r"<html[^>]*>\s*", r"</html>\s*", r"<head>\s*", r"</head>\s*",
                    r"<body>\s*", r"</body>\s*", r'<meta charset="utf-8">\s*', r'<meta name="viewport"[^>]*>\s*'):
        html = re.sub(pattern, "", html, flags=re.IGNORECASE)
    if not html.lstrip().startswith("<title>"):
        print("FAIL: expected <title> to lead the artifact file")
        return 1
    out = pathlib.Path(sys.argv[1])
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(html.strip() + "\n", encoding="utf-8")
    print(f"OK: wrote {out} ({len(html):,} chars)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
