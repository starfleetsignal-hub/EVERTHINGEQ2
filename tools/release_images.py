#!/usr/bin/env python3
"""Put the wiki images that are not in the shared image tars on a GitHub Release, in ~1.9 GB tars.

  release_images.py --plan           write images-release.json from data/allimages.json and images/index.json
  release_images.py --shard N        download shard N from Fandom's image host into eq2-images-NN.tar (run by CI)
images-release.json lists every file with its shard, source URL, uploader and upload time (CC BY-SA credit).
Tar members are images/<File_name>, the path pages link to, like the shared tars.
"""
import argparse, hashlib, json, os, sys, tarfile, time, urllib.request
from concurrent.futures import ThreadPoolExecutor

ROOT = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
PLAN = os.path.join(ROOT, "images-release.json")
UA = "NorrathLedgerImporter/0.1 (fan wiki conversion; contact via github.com/starfleetsignal-hub)"
SHARD_BYTES = 1_900_000_000          # release assets must stay under 2 GiB

def plan(allimages, index):
    al = json.load(open(allimages)); have = json.load(open(index))
    rest = sorted((i for i in al if i["name"] not in have and not i["mime"].startswith("video/youtube")), key=lambda i: i["name"])
    shard, used, out = 0, 0, []
    for i in rest:
        if used + i["size"] > SHARD_BYTES and used: shard, used = shard + 1, 0
        used += i["size"]
        out.append({"name": i["name"], "shard": shard, "url": i["url"], "size": i["size"], "sha1": i["sha1"],
                    "file_page": "https://eq2.fandom.com/wiki/File:" + urllib.request.quote(i["name"]),
                    "uploader": i.get("user", ""), "uploaded": i.get("uploaded", "")})
    json.dump(out, open(PLAN, "w"), ensure_ascii=False, indent=0)
    print(f"{len(out)} files, {sum(i['size'] for i in out) / 1e9:.2f} GB in {shard + 1} shards", file=sys.stderr)

def fetch(i):
    for attempt in range(5):
        try:
            req = urllib.request.Request(i["url"], headers={"User-Agent": UA})
            with urllib.request.urlopen(req, timeout=120) as r: data = r.read()
            if i.get("sha1") and hashlib.sha1(data).hexdigest() != i["sha1"]: raise ValueError("sha1 mismatch")
            return data
        except Exception as e:
            err = str(e)
            if "404" in err: break
            time.sleep(2 ** attempt)
    return err

def shard(n, workers=6):
    items = [i for i in json.load(open(PLAN)) if i["shard"] == n]
    name, failed = f"eq2-images-{n:02d}.tar", []
    with tarfile.open(name, "w") as tar, ThreadPoolExecutor(workers) as ex:
        for k, (i, data) in enumerate(zip(items, ex.map(fetch, items)), 1):
            if isinstance(data, str): failed.append({"name": i["name"], "error": data}); continue
            ti = tarfile.TarInfo("images/" + i["name"]); ti.size = len(data); ti.mtime = int(time.time())
            tar.addfile(ti, __import__("io").BytesIO(data))
            if k % 1000 == 0: print(f"  {k}/{len(items)}", file=sys.stderr)
    json.dump(failed, open(f"eq2-images-{n:02d}-failed.json", "w"), indent=1)
    print(f"{name}: {len(items) - len(failed)} of {len(items)} files, {len(failed)} failed", file=sys.stderr)

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--plan", action="store_true"); ap.add_argument("--shard", type=int)
    ap.add_argument("--allimages", default=os.path.join(ROOT, "data", "allimages.json"))
    ap.add_argument("--index", default=os.path.join(ROOT, "images", "index.json"))
    a = ap.parse_args()
    if a.plan: plan(a.allimages, a.index)
    if a.shard is not None: shard(a.shard)
