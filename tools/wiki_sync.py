#!/usr/bin/env python3
"""Bring content/ up to date with the wiki: every article created, edited, moved or deleted since the last sync.

  wiki_sync.py [--since 2026-09-22T00:00:00Z] [--dry-run]

Reads the wiki's recent changes (articles and file uploads) from data/wiki-sync.json's `until` (or --since) to now,
re-downloads the articles that changed (tools/fetch.py), converts them (tools/convert.py) and writes them over their
old files, removes pages that were deleted or turned into redirects, adds new pictures to data/pictures.json (the
"Web pictures" workflow shrinks them) and new Item_N/Spell_N icons to images/. Run assign_release.py and
resolve_links.py after it (the workflow does). Writes what changed to data/wiki-sync.json.
Needs eq2.fandom.com and static.wikia.nocookie.net, so it runs on GitHub's runners (.github/workflows/wiki-sync.yml).
"""
import argparse, datetime, glob, json, os, re, shutil, sys, tempfile, urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import fetch, convert
import yaml
from web_pictures import REF, ICON, picture_name

ROOT = os.path.normpath(os.path.join(HERE, ".."))
CONTENT = os.path.join(ROOT, "content")
STATE = os.path.join(ROOT, "data", "wiki-sync.json")
PICTURES = os.path.join(ROOT, "data", "pictures.json")
FIRST = "2026-09-22T00:00:00Z"       # the full download started 2026-09-23; one day of overlap
HAND_WRITTEN = {"guides"}            # folders written by hand, never touched here
# Pages whose dates are typed into build_preview.EVENTS; a change to one means checking those dates by hand
EVENT_PAGES = {"Erollisi Day", "Chronoportal Phenomenon", "Brew Day", "Bristlebane Day", "Beast'r Eggstravaganza",
               "Tinkerfest", "Scorched Sky", "Oceansfull Festival", "Nights of the Dead", "Heroes' Festival",
               "Heroes' Festival Timeline", "Frostfell", "City Festival", "Moonlight Enchantments", "Live Events"}

def recent_changes(since, until):
    """Article titles touched since `since`: (changed, gone, uploads), following moves and deletions in order."""
    changed, gone, uploads, cont = set(), set(), set(), {}
    while True:
        d = fetch.api({"action": "query", "list": "recentchanges", "rcnamespace": "0|6", "rctype": "edit|new|log",
                       "rcprop": "title|timestamp|loginfo", "rcdir": "newer", "rcstart": since, "rcend": until,
                       "rclimit": "500", **cont})
        for c in d["query"]["recentchanges"]:
            t, ns = c["title"], c["ns"]
            if ns == 6:
                if c["type"] == "new" or c.get("logtype") == "upload": uploads.add(t.split(":", 1)[1])
                continue
            lt, la = c.get("logtype"), c.get("logaction")
            if c["type"] in ("edit", "new") or (lt == "delete" and la == "restore"):
                changed.add(t); gone.discard(t)
            elif lt == "delete" and la in ("delete", "delete_redir"):
                gone.add(t); changed.discard(t)
            elif lt == "move":
                new = (c.get("logparams") or {}).get("target_title", "")
                gone.add(t); changed.discard(t)
                if new and (c.get("logparams") or {}).get("target_ns", 0) == 0: changed.add(new); gone.discard(new)
        if "continue" not in d: return changed, gone, uploads
        cont = d["continue"]

def page_states(titles):
    """title -> 'article' | 'missing' | ('redirect', target), as the wiki has it now."""
    out, titles = {}, sorted(titles)
    for i in range(0, len(titles), 50):
        batch = titles[i:i + 50]
        d = fetch.api({"action": "query", "prop": "info", "titles": "|".join(batch), "redirects": "1"})["query"]
        norm = {n["from"]: n["to"] for n in d.get("normalized", [])}
        red = {r["from"]: r["to"] for r in d.get("redirects", [])}
        pages = {p["title"]: p for p in d["pages"]}
        for t in batch:
            n = norm.get(t, t)
            if n in red:
                tgt = red[n]; p = pages.get(tgt, {})
                out[t] = ("redirect", tgt) if p and not p.get("missing") and not p.get("invalid") and p.get("ns") == 0 else "missing"
            else:
                p = pages.get(n, {})
                out[t] = "article" if p and not p.get("missing") and not p.get("invalid") else "missing"
    return out

def front(path):
    """(title, source title) from a page's front matter, read without parsing the whole file."""
    head = open(path, encoding="utf-8").read(20000).split("\n---", 1)[0]
    t = re.search(r"^title: (.*)$", head, re.M)
    s = re.search(r"^source:\n  title: (.*)$", head, re.M)
    val = lambda m: str(yaml.safe_load(m.group(1))) if m else ""
    return val(t), val(s)

def index():
    """Source title -> content files converted from it."""
    out = {}
    for f in glob.glob(os.path.join(CONTENT, "*", "*.md")):
        if f.split(os.sep)[-2] in HAND_WRITTEN: continue
        t, s = front(f)
        out.setdefault(s or t, []).append(f)
    return out

def new_pictures(files, have):
    """Picture and icon file names the given pages link to that the site doesn't host yet."""
    pics, icons = set(), set()
    for f in files:
        text = open(f, encoding="utf-8").read()
        t = front(f)[0]
        for ref in REF.findall(text):
            n = picture_name(ref, t)
            if ICON.match(n):
                if not os.path.exists(os.path.join(ROOT, "images", n)): icons.add(n)
            elif n not in have and n.lower() not in have: pics.add(n)
    return pics, icons

def file_urls(names):
    """Wiki file name -> original file URL, for the names that exist on the wiki."""
    out, names = {}, sorted(names)
    for i in range(0, len(names), 50):
        batch = names[i:i + 50]
        d = fetch.api({"action": "query", "prop": "imageinfo", "iiprop": "url",
                       "titles": "|".join("File:" + n for n in batch)})["query"]
        back = {n["to"]: n["from"] for n in d.get("normalized", [])}
        for p in d["pages"]:
            if p.get("imageinfo"):
                asked = back.get(p["title"], p["title"]).split(":", 1)[1]
                out[asked.replace(" ", "_")] = p["imageinfo"][0]["url"].split("?")[0]
    return out

def download(url, path):
    req = urllib.request.Request(url, headers={"User-Agent": fetch.UA})
    for attempt in range(4):
        try:
            with urllib.request.urlopen(req, timeout=60) as r: data = r.read()
            open(path, "wb").write(data); return True
        except Exception as e:
            print("  retry", url, e, file=sys.stderr)
    return False

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--since")
    ap.add_argument("--dry-run", action="store_true", help="list the changes, write nothing")
    a = ap.parse_args()
    state = json.load(open(STATE)) if os.path.exists(STATE) else {}
    since = a.since or state.get("until") or FIRST
    until = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    changed, gone, uploads = recent_changes(since, until)
    print(f"since {since}: {len(changed)} articles changed, {len(gone)} moved or deleted, {len(uploads)} files uploaded", file=sys.stderr)
    states = page_states(changed | gone)
    fetch_titles, remove = set(), set()
    for t, s in states.items():
        if s == "article": fetch_titles.add(t)
        elif s == "missing": remove.add(t)
        else: remove.add(t); fetch_titles.add(s[1])     # now a redirect: drop its page, refresh the target's aliases
    if a.dry_run:
        print(json.dumps({"fetch": sorted(fetch_titles), "remove": sorted(remove)}, indent=1, ensure_ascii=False)); return

    idx = index()
    tmp = tempfile.mkdtemp()
    fetch.RAW = os.path.join(tmp, "raw"); os.makedirs(fetch.RAW)
    convert.CONTENT = os.path.join(tmp, "content")
    got = fetch.fetch_pages(sorted(fetch_titles))
    if got: convert.main(sorted(glob.glob(os.path.join(fetch.RAW, "*.json"))))

    report = {"since": since, "until": until, "new": [], "updated": [], "removed": [], "unchanged": 0}
    written = []
    for f in sorted(glob.glob(os.path.join(convert.CONTENT, "*", "*.md"))):
        title, _ = front(f)
        kind_dir = f.split(os.sep)[-2]
        old = idx.get(title, [])
        same = [o for o in old if o.split(os.sep)[-2] == kind_dir]
        if same:
            dest = same[0]
        else:
            dest = os.path.join(CONTENT, kind_dir, os.path.basename(f))
            if os.path.exists(dest) and (front(dest)[1] or front(dest)[0]) != title:   # another page has this slug
                dest = dest[:-3] + "-%s.md" % json.load(open(os.path.join(fetch.RAW, fetch.safe_name(title))))["pageid"]
        new_text = open(f, encoding="utf-8").read()
        if os.path.exists(dest):
            old_text = open(dest, encoding="utf-8").read()
            # assign_release.py adds expansion_source and may move expansion; compare without them
            strip = lambda s: re.sub(r"^expansion(_source)?: .*\n", "", s, flags=re.M)
            if strip(old_text) == strip(new_text): report["unchanged"] += 1; continue
        os.makedirs(os.path.dirname(dest), exist_ok=True)
        open(dest, "w", encoding="utf-8").write(new_text)
        written.append(dest)
        report["updated" if old else "new"].append(title)
        for o in old:                                # the page changed type: drop the copy in the old folder
            if o != dest and os.path.exists(o): os.remove(o)
    for t in sorted(remove):
        for o in idx.get(t, []):
            if o not in written and os.path.exists(o): os.remove(o); report["removed"].append(t)

    have = json.load(open(PICTURES)) if os.path.exists(PICTURES) else {}
    have_lower = set(have) | {k.lower() for k in have}
    pics, icons = new_pictures(written, have_lower)
    urls = file_urls(pics | icons) if pics | icons else {}
    added = {n: u for n, u in urls.items() if n in pics or n.replace(" ", "_") in pics}
    if added:
        have.update(added)
        json.dump(dict(sorted(have.items())), open(PICTURES, "w"), ensure_ascii=False, indent=0)
    got_icons = [n for n in icons if n in urls and download(urls[n], os.path.join(ROOT, "images", n))]
    report["pictures_added"] = sorted(added)
    report["icons_added"] = sorted(got_icons)
    report["reuploaded_pictures"] = sorted(u.replace(" ", "_") for u in uploads if u.replace(" ", "_") in have)
    report["event_pages_changed"] = sorted(t for t in fetch_titles if t in EVENT_PAGES)
    json.dump(report, open(STATE, "w"), indent=1, ensure_ascii=False)
    shutil.rmtree(tmp, ignore_errors=True)
    print(f"new {len(report['new'])}, updated {len(report['updated'])}, unchanged {report['unchanged']}, "
          f"removed {len(report['removed'])}, pictures {len(added)}, icons {len(got_icons)}, "
          f"event pages {report['event_pages_changed']}", file=sys.stderr)

if __name__ == "__main__":
    main()
