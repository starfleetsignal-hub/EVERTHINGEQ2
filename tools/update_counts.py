#!/usr/bin/env python3
"""Count the pages in content/ and write the numbers into README.md (between the <!-- counts --> markers).

    python3 tools/update_counts.py           # rewrite README.md
    python3 tools/update_counts.py --check   # exit 1 when README.md is out of date (for CI or a pre-commit hook)

The site's own sidebar and home page already count the pages while building (META.counts in build_preview.py), so only the
README needs this.
"""
import os, re, sys

ROOT = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
README = os.path.join(ROOT, "README.md")
LABELS = [("items", "Items"), ("pages", "Other pages"), ("quests", "Quests"), ("achievements", "Achievements"), ("spells", "Spells"),
          ("monsters", "Monsters"), ("npcs", "NPCs"), ("named", "Named monsters"), ("pois", "Places"), ("zones", "Zones and instances"),
          ("timelines", "Timelines"), ("housing", "Housing"), ("lore", "Lore"), ("guides", "Player guides")]
START, END = "<!-- counts:start -->", "<!-- counts:end -->"


def count():
    out = {}
    base = os.path.join(ROOT, "content")
    for d in sorted(os.listdir(base)):
        p = os.path.join(base, d)
        if os.path.isdir(p): out[d] = sum(1 for f in os.listdir(p) if f.endswith(".md"))
    return out


def block(c):
    known = {k for k, _ in LABELS}
    rows = [(l, c[k]) for k, l in LABELS if c.get(k)] + [(k.capitalize(), n) for k, n in sorted(c.items()) if k not in known and n]
    total = sum(c.values())
    return "%s\nCurrent snapshot: **%s pages** (counted from `content/`; run `python3 tools/update_counts.py` after a bulk change).\n\n| Type | Pages |\n| --- | ---: |\n%s\n%s" % (
        START, format(total, ","), "\n".join("| %s | %s |" % (l, format(n, ",")) for l, n in rows), END)


def main():
    text = open(README, encoding="utf-8").read()
    if START not in text or END not in text: sys.exit("README.md has no %s ... %s block" % (START, END))
    new = re.sub(re.escape(START) + ".*?" + re.escape(END), lambda m: block(count()), text, flags=re.S)
    if "--check" in sys.argv:
        if new != text: sys.exit("README.md page counts are out of date: run python3 tools/update_counts.py")
        print("README.md page counts are current"); return
    open(README, "w", encoding="utf-8").write(new)
    print("README.md updated:", format(sum(count().values()), ","), "pages")


if __name__ == "__main__":
    main()
