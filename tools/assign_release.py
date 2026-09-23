#!/usr/bin/env python3
"""File each quest under the release that added it, not the release of the zone it starts in.

The wiki's "<Release> Quests" category follows the starting zone when a quest page has no patch field, so
quests added later to old zones (epic weapons, later questlines, level-90+ quests in Antonica...) end up
under The Shattered Lands. Evidence, strongest first:
  1. questline   epic weapon quests (Epic 1.0 arrived in Rise of Kunark, Epic 2.0 in Kunark Ascending)
  2. patch       the infobox patch field ("Rise of Kunark", "LU42")
  3. timeline    a timeline named after a release, or one whose dated quests agree on a release
  4. chain       the prerequisite / next-quest chain the quest belongs to, when its dated quests agree
  5. level       a quest above everything the category release offers moves to the first release reaching that level
  6. category    the wiki's category (unchanged)
Rewrites the `expansion:` line in content/quests/*.md and adds `expansion_source:`; prints a summary of moves.
Run after convert.py and before build_preview.py.
"""
import collections, glob, os, re, sys
import yaml

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from convert import EXPANSIONS, CONTENT, norm_title
CONTENT = os.environ.get("EQ2_CONTENT", CONTENT)

POS = {x: i for i, x in enumerate(EXPANSIONS)}
ABBR = {"sl": "Shattered Lands", "dof": "Desert of Flames", "kos": "Kingdom of Sky", "eof": "Echoes of Faydwer",
        "rok": "Rise of Kunark", "tso": "The Shadow Odyssey", "sf": "Sentinel's Fate", "dov": "Destiny of Velious",
        "aod": "Age of Discovery", "coe": "Chains of Eternity", "tov": "Tears of Veeshan", "aom": "Altar of Malice",
        "tot": "Terrors of Thalumbra", "ka": "Kunark Ascending", "pop": "Planes of Prophecy", "cd": "Chaos Descending",
        "bol": "Blood of Luclin", "ros": "Reign of Shadows", "vov": "Visions of Vetrovia", "ror": "Renewal of Ro",
        "boz": "Ballads of Zimara", "sod": "Scars of Destruction", "roc": "Rage of Cthurath"}
# First game update (LU/GU number) of each release's era, from the game's release history.
LU_START = [(1, "Shattered Lands"), (13, "Desert of Flames"), (20, "Kingdom of Sky"), (29, "Echoes of Faydwer"),
            (40, "Rise of Kunark"), (49, "The Shadow Odyssey"), (55, "Sentinel's Fate"), (59, "Destiny of Velious"),
            (62, "Age of Discovery"), (65, "Chains of Eternity"), (68, "Tears of Veeshan")]
# Adventure level cap each release brought (a quest up to this level can belong to it).
CAP = dict(zip(EXPANSIONS, [50, 50, 60, 70, 80, 80, 90, 90, 90, 95, 95, 100, 100, 100, 110, 110, 120, 120, 125, 125, 130, 130, 135]))
AGREE = 0.6   # share of dated quests that must agree before a timeline or chain passes its release on

def from_patch(v):
    v = re.sub(r"\[\[(?:[^\]|]*\|)?([^\]]*)\]\]", r"\1", str(v or "")).strip()
    if not v: return ""
    for x in EXPANSIONS:
        if x.lower() in v.lower() or v.lower() == x.lower().replace("the ", ""): return x
    if v.lower() in ABBR: return ABBR[v.lower()]
    m = re.match(r"(?:LU|GU|Live Update|Game Update)\s*0*(\d+)$", v, re.I)
    if m:
        n = int(m.group(1))
        if n > 71: return ""          # later updates aren't numbered consistently; don't guess
        return [x for start, x in LU_START if n >= start][-1]
    return ""

def titles(v):
    return [norm_title(m.group(1)) for m in re.finditer(r"\[\[([^\]|#]+)", str(v or ""))]

def level_of(fm):
    m = re.match(r"\s*(\d+)", str(fm.get("level", "")))
    return int(m.group(1)) if m else None

def vote(xs):
    xs = [x for x in xs if x]
    if not xs: return ""
    x, n = collections.Counter(xs).most_common(1)[0]
    return x if n / len(xs) >= AGREE else ""

def set_release(q, rel, why):
    head, rest = q["txt"].split("---", 2)[1:]
    head = re.sub(r"^expansion_source: .*\n", "", head, flags=re.M)
    line = "expansion: %s\nexpansion_source: %s\n" % (yaml.safe_dump(rel, default_style=None).split("\n")[0], why)
    if re.search(r"^expansion: .*\n", head, re.M): head = re.sub(r"^expansion: .*\n", line, head, count=1, flags=re.M)
    else: head = head.rstrip("\n") + "\n" + line
    open(q["file"], "w").write("---" + head + "---" + rest)

def load(pattern):
    out = {}
    for f in sorted(glob.glob(os.path.join(CONTENT, pattern))):
        txt = open(f).read()
        fm = yaml.safe_load(txt.split("---", 2)[1])
        out[fm["title"]] = {"file": f, "fm": fm, "txt": txt}
    return out

REFERRERS = {"quests", "named", "monsters", "npcs", "zones", "pois", "timelines"}

def items(write=True):
    """Items take the earliest release among the quests, zones and creatures they come from (or the quest they
    start, or the recipe book that makes them); then the earliest release of a quest, creature or zone page that
    links to them (rewards, drops); failing that, the first release whose level cap reaches them."""
    known, alias, bodies = {}, {}, []
    for f in glob.glob(os.path.join(CONTENT, "*", "*.md")):
        if os.sep + "items" + os.sep in f: continue
        txt = open(f).read()
        head = txt.split("---", 2)[1]
        t = re.search(r"^title: (.*)$", head, re.M); x = re.search(r"^expansion: (.*)$", head, re.M)
        if not (t and x): continue
        t, x = yaml.safe_load(t.group(1)), yaml.safe_load(x.group(1))
        if x in POS and f.split(os.sep)[-2] in REFERRERS: bodies.append((x, txt))
        if x in POS:
            known[norm_title(str(t))] = x
            for a in re.findall(r"^- (.*)$", head.split("aliases:", 1)[1].split("\n\S", 1)[0], re.M) if "aliases:" in head else []:
                alias.setdefault(norm_title(str(yaml.safe_load(a))), x)
    I = load(os.path.join("items", "*.md"))
    for t, q in I.items(): q["rel"], q["why"] = "", ""
    src_of = lambda v: [known.get(s) or alias.get(s) or (I[s]["rel"] if s in I else "") for s in titles(v)]
    # pages that link to an item: quest rewards, named-monster drops, zone loot lists
    cited = collections.defaultdict(set)
    for x, txt in bodies:
        for m in re.finditer(r"\[\[([^\]|#]+)", txt):
            t = norm_title(m.group(1))
            if t in I: cited[t].add(x)
    for rnd in range(3):                          # a few rounds so recipe books pass their release on
        for t, q in I.items():
            if q["why"] not in ("", "linked", "category"): continue
            fm = q["fm"]
            rs = [r for r in src_of(fm.get("obtained_from")) + src_of(fm.get("starts_quest")) if r]
            cats = [m.group(1) for c in fm.get("categories", []) or [] for m in [re.match(r"(.+?) (?:Dropped Items|Recipes|Bounty Items)$", c)] if m and m.group(1) in POS]
            if rs: q["rel"], q["why"] = min(rs, key=POS.get), "source"
            elif cited.get(t): q["rel"], q["why"] = min(cited[t], key=POS.get), "linked"
            elif cats: q["rel"], q["why"] = min(cats, key=POS.get), "category"
    for t, q in I.items():
        if q["rel"]: continue
        m = re.match(r"\s*(\d+)", str(q["fm"].get("level") or q["fm"].get("item_level") or ""))
        if m and int(m.group(1)) > 0:
            lv = int(m.group(1)); q["rel"] = next((x for x in EXPANSIONS if CAP[x] >= lv), EXPANSIONS[-1]); q["why"] = "level"
    n = collections.Counter(q["why"] or "none" for q in I.values())
    if write:
        for q in I.values():
            if q["rel"] and (q["rel"] != q["fm"].get("expansion") or "expansion_source:" not in q["txt"]): set_release(q, q["rel"], q["why"])
    print("items:", len(I), "| by evidence:", dict(n), "| by release:", dict(collections.Counter(q["rel"] or "-" for q in I.values()).most_common(8)))

def main(write=True):
    files = sorted(glob.glob(os.path.join(CONTENT, "quests", "*.md")))
    Q = {}
    for f in files:
        txt = open(f).read()
        head = txt.split("---", 2)[1]
        fm = yaml.safe_load(head)
        Q[fm["title"]] = {"file": f, "fm": fm, "txt": txt}
    alias = {}
    for t, q in Q.items():
        for a in q["fm"].get("aliases", []) or []: alias.setdefault(norm_title(a), t)
    look = lambda t: t if t in Q else alias.get(t)

    # 1-2: direct evidence
    for t, q in Q.items():
        fm, cats = q["fm"], q["fm"].get("categories", []) or []
        patch = from_patch(fm.get("added_in"))
        q["cat"] = fm.get("expansion", "")
        q["rel"], q["why"] = "", ""
        if "Epic Weapon 2.0 Quests" in cats:
            q["rel"], q["why"] = "Kunark Ascending", "questline"
        elif any(re.match(r".+ Epic Weapon Quests$", c) for c in cats):
            base = "Rise of Kunark"          # later classes (Beastlord, Channeler) got theirs with their release
            q["rel"], q["why"] = (patch if patch and POS[patch] > POS[base] else base), "questline"
        elif patch:
            q["rel"], q["why"] = patch, "patch"

    # 3: timelines
    by_tl = collections.defaultdict(list)
    for t, q in Q.items():
        for tl in titles(q["fm"].get("timeline")): by_tl[tl].append(t)
    tl_rel = {}
    for tl, ts in by_tl.items():
        named = next((x for x in sorted(EXPANSIONS, key=len, reverse=True) if tl.lower().startswith(x.lower())), "")
        tl_rel[tl] = named or vote(Q[t]["rel"] for t in ts)
    for t, q in Q.items():
        if q["rel"]: continue
        r = vote(tl_rel.get(tl, "") for tl in titles(q["fm"].get("timeline")))
        if r: q["rel"], q["why"] = r, "timeline"

    # 4: prerequisite / next-quest chains
    parent = {t: t for t in Q}
    def find(t):
        while parent[t] != t: parent[t] = parent[parent[t]]; t = parent[t]
        return t
    for t, q in Q.items():
        for k in ("prerequisite", "next_quest"):
            for o in titles(q["fm"].get(k)):
                o = look(o)
                if o: parent[find(o)] = find(t)
    comp = collections.defaultdict(list)
    for t in Q: comp[find(t)].append(t)
    for ts in comp.values():
        if len(ts) < 2: continue
        r = vote(Q[t]["rel"] for t in ts if Q[t]["why"] in ("patch", "questline", "timeline"))
        if not r: continue
        for t in ts:
            if not Q[t]["rel"]: Q[t]["rel"], Q[t]["why"] = r, "chain"

    # 5: level above what the category release offers (levels from quests dated by their patch field)
    top = collections.defaultdict(list)
    for q in Q.values():
        if q["why"] == "patch" and level_of(q["fm"]) is not None: top[q["rel"]].append(level_of(q["fm"]))
    reach, best = {}, 0
    for x in EXPANSIONS:                   # highest level seen so far, by release (95th percentile, cumulative, never below the level cap)
        ls = sorted(top.get(x, []))
        if ls: best = max(best, ls[int(len(ls) * .95) - 1 if len(ls) > 1 else 0])
        reach[x] = max(best, CAP[x])
    for t, q in Q.items():
        if q["rel"]: continue
        lv, cat = level_of(q["fm"]), q["cat"]
        if lv is not None and cat in reach and lv > reach[cat]:
            later = next((x for x in EXPANSIONS[POS[cat] + 1:] if reach[x] >= lv), "")
            if later: q["rel"], q["why"] = later, "level"

    # 6: keep the category
    moves = collections.Counter(); samples = collections.defaultdict(list)
    for t, q in Q.items():
        if not q["rel"]: q["rel"], q["why"] = q["cat"], "category"
        if q["rel"] != q["cat"]:
            moves[(q["cat"] or "(none)", q["rel"], q["why"])] += 1
            samples[(q["cat"] or "(none)", q["rel"], q["why"])].append(t)
        if write and q["rel"] and (q["rel"] != q["cat"] or "expansion_source:" not in q["txt"]):
            set_release(q, q["rel"], q["why"])
    print("quests:", len(Q), "| moved:", sum(moves.values()),
          "| by evidence:", dict(collections.Counter(q["why"] for q in Q.values())))
    for (a, b, why), n in sorted(moves.items(), key=lambda kv: -kv[1]):
        print("  %4d  %s -> %s (%s): %s" % (n, a, b, why, "; ".join(samples[(a, b, why)][:3])))

if __name__ == "__main__":
    main(write="--dry-run" not in sys.argv)
    items(write="--dry-run" not in sys.argv)
