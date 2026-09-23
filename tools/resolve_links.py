#!/usr/bin/env python3
"""Find [[links]] in content/ that don't match a page title or alias, and ask the wiki where they redirect.
Writes data/redirects.json  {"Link target": "Actual page title"} used by the site build."""
import glob, json, os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fetch import api
import yaml

ROOT = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
known, targets = set(), set()
for f in glob.glob(os.path.join(ROOT, "content", "**", "*.md"), recursive=True):
    txt = open(f).read()
    fm = yaml.safe_load(txt.split("---\n", 2)[1])
    known.add(fm["title"]); known.update(fm.get("aliases", []))
    for m in re.finditer(r"\[\[([^\]|#]+)", txt):
        targets.add(m.group(1).strip())
path = os.path.join(ROOT, "data", "redirects.json")
os.makedirs(os.path.dirname(path), exist_ok=True)
redirects = json.load(open(path)) if os.path.exists(path) else {}
todo = sorted(t for t in targets if t not in known and t not in redirects)
print(f"{len(targets)} link targets, {len(todo)} to look up", file=sys.stderr)
for i in range(0, len(todo), 50):
    d = api({"action": "query", "redirects": "1", "titles": "|".join(todo[i:i + 50])})["query"]
    norm = {n["from"]: n["to"] for n in d.get("normalized", [])}
    red = {r["from"]: r["to"] for r in d.get("redirects", [])}
    exists = {p["title"] for p in d["pages"] if not p.get("missing") and not p.get("invalid")}
    for t in todo[i:i + 50]:
        n = norm.get(t, t); n = red.get(n, n)
        redirects[t] = n if n in exists else None     # None = page doesn't exist on the wiki (red link)
json.dump(redirects, open(path, "w"), indent=1, ensure_ascii=False, sort_keys=True)
print("red links:", sum(v is None for v in redirects.values()), "| redirects:", sum(1 for k, v in redirects.items() if v and v != k), file=sys.stderr)
