#!/usr/bin/env python3
"""Download every file in data/allimages.json in bundles and store each bundle as an uncompressed tar.

  bundle_images.py [--out DIR] [--per 10000] [--workers 8]
Files are sorted by name and split into chunks of --per files. For each chunk not yet in --out, missing files are
downloaded into images/ (?format=original), packed into images-NNN.tar (members are images/<File_name>, the path pages
link to), written to --out, checked, and the local copies deleted, so local disk only ever holds one chunk.
data/image-sources.json maps every file to its source URL, file page, uploader and upload time (CC BY-SA credit),
and --out/index.json maps every file name to its bundle. Re-running resumes after the last finished bundle.
"""
import argparse, json, os, sys, tarfile, time, urllib.parse, urllib.request
from concurrent.futures import ThreadPoolExecutor
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fetch import UA

ROOT = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
LIST, IMAGES = os.path.join(ROOT, "data", "allimages.json"), os.path.join(ROOT, "images")
SOURCES, FAILURES = os.path.join(ROOT, "data", "image-sources.json"), os.path.join(ROOT, "data", "image-failures.json")

def file_page(name):
    return "https://eq2.fandom.com/wiki/File:" + urllib.parse.quote(name)

def fetch(i):
    path = os.path.join(IMAGES, i["name"])
    if os.path.exists(path): return None
    for attempt in range(5):
        try:
            req = urllib.request.Request(i["url"] + "?format=original", headers={"User-Agent": UA})
            with urllib.request.urlopen(req, timeout=120) as r: data = r.read()
            open(path + ".part", "wb").write(data); os.replace(path + ".part", path)
            time.sleep(0.1)
            return None
        except Exception as e:
            if getattr(e, "code", None) in (404, 410) or attempt == 4: return (i["name"], str(e))
            time.sleep(2 ** attempt)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default="/mnt/project-files/eq2-wiki/images")
    ap.add_argument("--per", type=int, default=10000); ap.add_argument("--workers", type=int, default=8)
    ap.add_argument("--chunks", help="comma-separated chunk numbers to do (default all), for parallel runs")
    ap.add_argument("--tag", default="", help="suffix for this run's sources/failures/index files, for parallel runs")
    a = ap.parse_args()
    global SOURCES, FAILURES
    if a.tag: SOURCES, FAILURES = (f.replace(".json", f"-{a.tag}.json") for f in (SOURCES, FAILURES))
    items = sorted((i for i in json.load(open(LIST)) if not i["mime"].startswith("video/youtube")), key=lambda i: i["name"])
    os.makedirs(IMAGES, exist_ok=True); os.makedirs(a.out, exist_ok=True)
    sources = json.load(open(SOURCES)) if os.path.exists(SOURCES) else {}
    failed = dict(json.load(open(FAILURES))) if os.path.exists(FAILURES) else {}
    index_path = os.path.join(a.out, f"index-{a.tag}.json" if a.tag else "index.json")
    index = json.load(open(index_path)) if os.path.exists(index_path) else {}
    chunks = [items[k:k + a.per] for k in range(0, len(items), a.per)]
    for n, chunk in enumerate(chunks):
        if a.chunks and n not in {int(c) for c in a.chunks.split(",")}: continue
        tar_name = f"images-{n:03d}.tar"; dest = os.path.join(a.out, tar_name)
        if os.path.exists(dest) and all(index.get(i["name"]) == tar_name or i["name"] in failed for i in chunk):
            continue
        t0 = time.time()
        with ThreadPoolExecutor(a.workers) as ex:
            for r in ex.map(fetch, chunk):
                if r: failed[r[0]] = r[1]
        have = [i for i in chunk if os.path.exists(os.path.join(IMAGES, i["name"]))]
        local = os.path.join(ROOT, tar_name)
        with tarfile.open(local, "w") as tf:
            for i in have: tf.add(os.path.join(IMAGES, i["name"]), arcname="images/" + i["name"])
        os.replace(local, dest) if os.stat(ROOT).st_dev == os.stat(a.out).st_dev else os.system(f'cp "{local}" "{dest}" && rm "{local}"')
        with tarfile.open(dest) as tf: members = len(tf.getnames())
        if members != len(have): sys.exit(f"{tar_name}: {members} members, expected {len(have)}")
        for i in have:
            sources[i["name"]] = {"source": i["url"], "file_page": file_page(i["name"]), "uploader": i.get("user"),
                                  "uploaded": i.get("uploaded") or i.get("timestamp"), "sha1": i["sha1"]}
            index[i["name"]] = tar_name
            failed.pop(i["name"], None)
            os.remove(os.path.join(IMAGES, i["name"]))
        json.dump(sources, open(SOURCES, "w"), ensure_ascii=False, indent=0, sort_keys=True)
        json.dump(sorted(failed.items()), open(FAILURES, "w"), ensure_ascii=False, indent=1)
        json.dump(index, open(index_path, "w"), ensure_ascii=False)
        mb = sum(os.path.getsize(dest) for _ in [0]) / 1e6
        print(f"{tar_name}: {len(have)}/{len(chunk)} files, {mb:.0f} MB, {time.time() - t0:.0f}s; {len(failed)} failed so far",
              file=sys.stderr, flush=True)

if __name__ == "__main__":
    main()
