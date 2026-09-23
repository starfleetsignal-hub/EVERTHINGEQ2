#!/usr/bin/env python3
"""Put the wiki images that are not in the shared image tars on a GitHub Release, in ~1.9 GB tars.

  release_images.py --plan           write images-release.json from data/allimages.json and images/index.json
  release_images.py --shard N        download shard N from Fandom's image host into eq2-images-NN.tar (run by CI)
images-release.json lists every file with its shard, source URL, uploader and upload time (CC BY-SA credit).
Tar members are images/<File_name>, the path pages link to, like the shared tars.
"""
import argparse, http.client, io, json, os, socket, sys, tarfile, threading, time, urllib.error, urllib.parse, urllib.request
from concurrent.futures import ThreadPoolExecutor

ROOT = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
PLAN = os.path.join(ROOT, "images-release.json")
UA = "NorrathLedgerImporter/0.1 (fan wiki conversion; contact via github.com/starfleetsignal-hub)"
SHARD_BYTES = 1_900_000_000          # release assets must stay under 2 GiB
SHARD_FILES = 5_000                  # download time goes by file count, so keep shards even for parallel jobs

_getaddrinfo = socket.getaddrinfo      # runners have no IPv6 route; an IPv6 address stalls each connect ~2 minutes
socket.getaddrinfo = lambda host, port, family=0, *a, **k: _getaddrinfo(host, port, socket.AF_INET, *a, **k)

def plan(allimages, index):
    al = json.load(open(allimages)); have = json.load(open(index))
    rest = sorted((i for i in al if i["name"] not in have and not i["mime"].startswith("video/youtube")), key=lambda i: i["name"])
    shard, used, count, out = 0, 0, 0, []
    for i in rest:
        if (used + i["size"] > SHARD_BYTES or count == SHARD_FILES) and used: shard, used, count = shard + 1, 0, 0
        used += i["size"]; count += 1
        out.append({"name": i["name"], "shard": shard, "url": i["url"], "size": i["size"], "sha1": i["sha1"],
                    "file_page": "https://eq2.fandom.com/wiki/File:" + urllib.request.quote(i["name"]),
                    "uploader": i.get("user", ""), "uploaded": i.get("uploaded", "")})
    json.dump(out, open(PLAN, "w"), ensure_ascii=False, indent=0)
    print(f"{len(out)} files, {sum(i['size'] for i in out) / 1e9:.2f} GB in {shard + 1} shards", file=sys.stderr)

_local = threading.local()

def get(url):
    """GET over a kept-alive connection per thread: the image host sometimes takes 20 s to accept a new connection."""
    u = urllib.parse.urlsplit(url)
    conn = getattr(_local, "conn", None)
    if conn is None or (conn.host, conn.port) != (u.hostname, u.port or (443 if u.scheme == "https" else 80)):
        cls = http.client.HTTPSConnection if u.scheme == "https" else http.client.HTTPConnection
        conn = _local.conn = cls(u.hostname, u.port, timeout=60)
    try:
        conn.request("GET", u.path + "?" + u.query, headers={"User-Agent": UA})
        r = conn.getresponse()
        parts, deadline = [], time.time() + 300    # a server that trickles bytes would otherwise hold the job for hours
        while chunk := r.read1(1 << 16):
            parts.append(chunk)
            if time.time() > deadline: raise TimeoutError("download took over 5 minutes")
        if r.status in (301, 302, 303, 307, 308): return get(urllib.parse.urljoin(url, r.getheader("Location")))
        if r.status != 200: raise urllib.error.HTTPError(url, r.status, r.reason, r.headers, None)
        return b"".join(parts)
    except Exception:
        conn.close(); _local.conn = None
        raise

def fetch(i):
    """The file's bytes, or an error string. Without ?format=original Fandom serves a re-encoded copy."""
    for attempt in range(4):
        try:
            return get(i["url"] + "?format=original")
        except Exception as e:
            err = str(e)
            if getattr(e, "code", None) in (404, 410): break
            time.sleep(2 ** attempt)
    return err

def shard(n, workers=16, limit=None):
    items = [i for i in json.load(open(PLAN)) if i["shard"] == n][:limit]
    t0 = time.time()
    name, failed = f"eq2-images-{n:02d}.tar", []
    with tarfile.open(name, "w") as tar, ThreadPoolExecutor(workers) as ex:
        for k, (i, data) in enumerate(zip(items, ex.map(fetch, items)), 1):
            if isinstance(data, str): failed.append({"name": i["name"], "error": data}); continue
            ti = tarfile.TarInfo("images/" + i["name"]); ti.size = len(data); ti.mtime = int(time.time())
            tar.addfile(ti, io.BytesIO(data))
            if k % 1000 == 0: print(f"  {k}/{len(items)} in {time.time() - t0:.0f}s, {len(failed)} failed", file=sys.stderr, flush=True)
            if k == 200 and len(failed) > 100: sys.exit(f"stopping: {len(failed)} of the first 200 failed, e.g. {failed[0]}")
    json.dump(failed, open(f"eq2-images-{n:02d}-failed.json", "w"), indent=1)
    if os.environ.get("GITHUB_OUTPUT"): open(os.environ["GITHUB_OUTPUT"], "a").write(f"failed={len(failed)}\n")
    print(f"{name}: {len(items) - len(failed)} of {len(items)} files, {len(failed)} failed, {time.time() - t0:.0f}s", file=sys.stderr)

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--plan", action="store_true"); ap.add_argument("--shard", type=int)
    ap.add_argument("--limit", type=int, help="only the first N files of the shard (a quick test)")
    ap.add_argument("--list-shards", action="store_true", help="print the shard numbers as a JSON list (for the CI matrix)")
    ap.add_argument("--allimages", default=os.path.join(ROOT, "data", "allimages.json"))
    ap.add_argument("--index", default=os.path.join(ROOT, "images", "index.json"))
    a = ap.parse_args()
    if a.plan: plan(a.allimages, a.index)
    if a.list_shards: print(json.dumps(sorted({i["shard"] for i in json.load(open(PLAN))})))
    if a.shard is not None: shard(a.shard, limit=a.limit)
