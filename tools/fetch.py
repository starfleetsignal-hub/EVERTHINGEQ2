#!/usr/bin/env python3
"""Download page wikitext from the EverQuest II Fandom wiki via the MediaWiki API.

Usage:
  fetch.py --category "Antonica Quests" --title Antonica ...
Saves one JSON file per page in raw/ (title, pageid, revid, timestamp, categories, wikitext).
Polite: one request at a time, >=1s apart, maxlag honoured, identifying User-Agent.
"""
import argparse, json, os, re, sys, time, urllib.parse, urllib.request

API = "https://eq2.fandom.com/api.php"
UA = "NorrathLedgerImporter/0.1 (fan wiki conversion; contact via github.com/starfleetsignal-hub)"
HERE = os.path.dirname(os.path.abspath(__file__))
RAW = os.path.join(HERE, "..", "raw")
_last = [0.0]

def api(params):
    params = {**params, "format": "json", "formatversion": "2", "maxlag": "5"}
    url = API + "?" + urllib.parse.urlencode(params)
    for attempt in range(5):
        wait = 1.0 - (time.time() - _last[0])
        if wait > 0: time.sleep(wait)
        _last[0] = time.time()
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA})
            with urllib.request.urlopen(req, timeout=60) as r:
                data = json.load(r)
        except Exception as e:
            print("  retry after error:", e, file=sys.stderr); time.sleep(2 ** attempt * 2); continue
        if data.get("error", {}).get("code") == "maxlag":
            time.sleep(5); continue
        if "error" in data: raise RuntimeError(data["error"])
        return data
    raise RuntimeError("giving up on " + url)

def category_members(cat):
    out, cont = [], {}
    while True:
        d = api({"action": "query", "list": "categorymembers", "cmtitle": "Category:" + cat,
                 "cmlimit": "500", "cmnamespace": "0", **cont})
        out += [m["title"] for m in d["query"]["categorymembers"]]
        if "continue" not in d: return out
        cont = d["continue"]

def safe_name(title):
    return re.sub(r"[^A-Za-z0-9._-]+", "_", title)[:150] + ".json"

def fetch_pages(titles):
    """Fetch wikitext, categories and redirect aliases, following API continuation so nothing is cut short."""
    saved = []
    for i in range(0, len(titles), 50):
        batch = titles[i:i + 50]; acc, cont = {}, {}
        while True:
            d = api({"action": "query", "prop": "revisions|categories|redirects", "rvprop": "ids|timestamp|content",
                     "rvslots": "main", "cllimit": "max", "rdlimit": "max", "rdnamespace": "0", "redirects": "1",
                     "titles": "|".join(batch), **cont})
            for p in d["query"]["pages"]:
                a = acc.setdefault(p["title"], {"page": p, "cats": [], "reds": [], "rev": None})
                a["cats"] += [c["title"].split(":", 1)[1] for c in p.get("categories", [])]
                a["reds"] += [r["title"] for r in p.get("redirects", [])]
                if p.get("revisions"): a["rev"] = p["revisions"][0]
            if "continue" not in d: break
            cont = d["continue"]
        for t, a in acc.items():
            p, rev = a["page"], a["rev"]
            if p.get("missing") or p.get("invalid") or not rev:
                print("  missing:", t, file=sys.stderr); continue
            rec = {"title": t, "pageid": p["pageid"], "revid": rev["revid"], "timestamp": rev["timestamp"],
                   "categories": sorted(set(a["cats"])), "redirects": sorted(set(a["reds"])),
                   "wikitext": rev["slots"]["main"]["content"]}
            with open(os.path.join(RAW, safe_name(t)), "w") as f:
                json.dump(rec, f, ensure_ascii=False)
            saved.append(t)
        if (i // 50) % 20 == 0 or i + 50 >= len(titles):
            print(f"  fetched {min(i + 50, len(titles))}/{len(titles)}", file=sys.stderr)
    return saved

def all_titles():
    """Every non-redirect article title (namespace 0); cached in data/allpages.json."""
    path = os.path.join(HERE, "..", "data", "allpages.json")
    if os.path.exists(path): return json.load(open(path))
    out, cont = [], {}
    while True:
        d = api({"action": "query", "list": "allpages", "apnamespace": "0", "apfilterredir": "nonredirects",
                 "aplimit": "500", **cont})
        out += [p["title"] for p in d["query"]["allpages"]]
        if len(out) % 20000 < 500: print(f"  listed {len(out)} titles", file=sys.stderr)
        if "continue" not in d: break
        cont = d["continue"]
    os.makedirs(os.path.dirname(path), exist_ok=True)
    json.dump(out, open(path, "w"), ensure_ascii=False)
    return out

def refresh_meta():
    """Re-read categories and redirect aliases for every saved page, following API continuation."""
    recs = {}
    for f in os.listdir(RAW):
        if f.endswith(".json") and not f.startswith("_"):
            r = json.load(open(os.path.join(RAW, f))); recs[r["title"]] = (f, r)
    titles = sorted(recs)
    for i in range(0, len(titles), 50):
        batch = titles[i:i + 50]; cats, reds, cont = {}, {}, {}
        while True:
            d = api({"action": "query", "prop": "categories|redirects", "cllimit": "max", "rdlimit": "max",
                     "rdnamespace": "0", "titles": "|".join(batch), **cont})
            for p in d["query"]["pages"]:
                cats.setdefault(p["title"], []).extend(c["title"].split(":", 1)[1] for c in p.get("categories", []))
                reds.setdefault(p["title"], []).extend(r["title"] for r in p.get("redirects", []))
            if "continue" not in d: break
            cont = d["continue"]
        for t in batch:
            f, r = recs[t]
            r["categories"] = sorted(set(cats.get(t, r["categories"])))
            r["redirects"] = sorted(set(reds.get(t, r.get("redirects", []))))
            json.dump(r, open(os.path.join(RAW, f), "w"), ensure_ascii=False, indent=1)
        print(f"  metadata {min(i + 50, len(titles))}/{len(titles)}", file=sys.stderr)

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--category", action="append", default=[])
    ap.add_argument("--title", action="append", default=[])
    ap.add_argument("--refresh-meta", action="store_true", help="re-read categories/redirects for all saved pages")
    ap.add_argument("--all", action="store_true", help="every article on the wiki not already saved")
    a = ap.parse_args()
    if a.refresh_meta:
        refresh_meta(); sys.exit()
    os.makedirs(RAW, exist_ok=True)
    titles = list(a.title)
    for c in a.category:
        m = category_members(c); print(f"Category:{c}: {len(m)} pages", file=sys.stderr); titles += m
    if a.all:
        have = set(os.listdir(RAW))
        titles += [t for t in all_titles() if safe_name(t) not in have]
        print(f"{len(titles)} articles still to fetch", file=sys.stderr)
    titles = list(dict.fromkeys(titles))
    fetch_pages(titles)
