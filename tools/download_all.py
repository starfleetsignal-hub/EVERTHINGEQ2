#!/usr/bin/env python3
"""Download every file in data/allimages.json into images/ (skips files already there). Bundling is a separate step."""
import json, os, sys, time
from concurrent.futures import ThreadPoolExecutor
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bundle_images import fetch, LIST, IMAGES
items = [i for i in json.load(open(LIST)) if not i["mime"].startswith("video/youtube")]
todo = [i for i in items if not os.path.exists(os.path.join(IMAGES, i["name"]))]
print(f"{len(todo)} of {len(items)} to download", flush=True)
failed, t0 = {}, time.time()
with ThreadPoolExecutor(int(sys.argv[1]) if len(sys.argv) > 1 else 12) as ex:
    for n, r in enumerate(ex.map(fetch, todo), 1):
        if r: failed[r[0]] = r[1]
        if n % 5000 == 0: print(f"downloaded {n}/{len(todo)} ({time.time()-t0:.0f}s, {len(failed)} failed)", flush=True)
json.dump(sorted(failed.items()), open(os.path.join(os.path.dirname(LIST), "image-failures.json"), "w"), ensure_ascii=False, indent=1)
print(f"done: {len(failed)} failed", flush=True)
