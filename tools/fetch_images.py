#!/usr/bin/env python3
"""List every image file on the wiki (data/allimages.json) and download them into images/.

  fetch_images.py --list        build the list through the MediaWiki API (500 per request)
  fetch_images.py --download    download files not yet in images/ from Fandom's image host
Downloads skip files already present, so the command can be re-run after an interruption.
"""
import argparse, json, os, sys, time, urllib.request
from concurrent.futures import ThreadPoolExecutor
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fetch import api, UA

ROOT = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
LIST, IMAGES = os.path.join(ROOT, "data", "allimages.json"), os.path.join(ROOT, "images")

def build_list():
    out, cont = [], {}
    while True:
        d = api({"action": "query", "list": "allimages", "ailimit": "500", "aiprop": "url|size|mime|sha1|user|timestamp", **cont})
        out += [{"name": i["name"], "url": i["url"].split("/revision/")[0], "size": i["size"], "mime": i["mime"], "sha1": i["sha1"], "user": i.get("user", ""), "uploaded": i.get("timestamp", "")}
                for i in d["query"]["allimages"]]
        if len(out) % 10000 < 500: print(f"  listed {len(out)} images", file=sys.stderr)
        if "continue" not in d: break
        cont = d["continue"]
    os.makedirs(os.path.dirname(LIST), exist_ok=True)
    json.dump(out, open(LIST, "w"), ensure_ascii=False)
    print(f"{len(out)} images, {sum(i['size'] for i in out) / 1e9:.2f} GB", file=sys.stderr)

def download(workers=4):
    items = json.load(open(LIST))
    os.makedirs(IMAGES, exist_ok=True)
    todo = [i for i in items if not os.path.exists(os.path.join(IMAGES, i["name"]))]
    print(f"{len(todo)} of {len(items)} images to download", file=sys.stderr)
    done, failed = [0], []
    def get(i):
        for attempt in range(4):
            try:
                req = urllib.request.Request(i["url"], headers={"User-Agent": UA})
                with urllib.request.urlopen(req, timeout=60) as r: data = r.read()
                tmp = os.path.join(IMAGES, i["name"] + ".part")
                open(tmp, "wb").write(data); os.replace(tmp, os.path.join(IMAGES, i["name"]))
                break
            except Exception as e:
                if attempt == 3: failed.append((i["name"], str(e)))
                time.sleep(2 ** attempt)
        time.sleep(0.25)
        done[0] += 1
        if done[0] % 2000 == 0: print(f"  downloaded {done[0]}/{len(todo)}", file=sys.stderr)
    with ThreadPoolExecutor(workers) as ex: list(ex.map(get, todo))
    json.dump(failed, open(os.path.join(ROOT, "data", "image-failures.json"), "w"), indent=1)
    print(f"done; {len(failed)} failed", file=sys.stderr)

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--list", action="store_true"); ap.add_argument("--download", action="store_true")
    a = ap.parse_args()
    if a.list: build_list()
    if a.download: download()
