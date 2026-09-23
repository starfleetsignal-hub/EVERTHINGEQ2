#!/usr/bin/env python3
"""Pack downloaded images into ~150 MB tars in the shared folder.

  pack_images.py [--out DIR] [--max-mb 150] [--final]
The shared folder does not keep files much over 200 MB, so bundles are capped by size. Each run packs files in images/
that no bundle holds yet (sorted by name) into images-NNN.tar (members images/<File_name>, the path pages link to),
copies it to --out, waits for the upload to finish, and records it in --out/index.json (file -> bundle). Without --final the last, partly
filled bundle is left for a later run, so the command can run while downloads continue.
--out/image-sources.json maps every packed file to its source URL, file page, uploader and upload time (CC BY-SA).
Local copies are kept; delete images/ yourself once the bundles are confirmed.
"""
import argparse, json, os, subprocess, sys, tarfile, time, urllib.parse

ROOT = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
LIST, IMAGES = os.path.join(ROOT, "data", "allimages.json"), os.path.join(ROOT, "images")
VFS_META = "/dev/shm/rclone-vfscache/vfsMeta"

def wait_uploaded(dest, timeout=1800):
    """Wait until rclone's cache marks dest as uploaded (Dirty false); True if confirmed, None if no cache metadata."""
    rel = os.path.relpath(os.path.realpath(dest), "/mnt/attach/project-files")
    metas = [os.path.join(VFS_META, d, rel) for d in (os.listdir(VFS_META) if os.path.isdir(VFS_META) else [])]
    t0 = time.time()
    while time.time() - t0 < timeout:
        found = [m for m in metas if os.path.exists(m)]
        if not found: return None
        try:
            if not any(json.load(open(m)).get("Dirty") for m in found): return True
        except ValueError: pass
        time.sleep(3)
    return False

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default="/mnt/project-files/eq2-wiki/images")
    ap.add_argument("--max-mb", type=int, default=150); ap.add_argument("--final", action="store_true")
    a = ap.parse_args()
    meta = {i["name"]: i for i in json.load(open(LIST))}
    index_path, sources_path = os.path.join(a.out, "index.json"), os.path.join(a.out, "image-sources.json")
    index = json.load(open(index_path)) if os.path.exists(index_path) else {}
    sources = json.load(open(sources_path)) if os.path.exists(sources_path) else {}
    # drop entries left by the earlier 2 GB bundles, which never reached the shared store
    index = {k: v for k, v in index.items() if os.path.exists(os.path.join(a.out, v))}
    sources = {k: v for k, v in sources.items() if k in index}
    n = max([int(v[7:10]) + 1 for v in index.values()] or [0])
    todo = sorted(f for f in os.listdir(IMAGES) if f in meta and f not in index)
    limit = a.max_mb * 1_000_000
    while todo:
        batch, size = [], 0
        while todo and (not batch or size + os.path.getsize(os.path.join(IMAGES, todo[0])) <= limit):
            f = todo.pop(0); batch.append(f); size += os.path.getsize(os.path.join(IMAGES, f))
        if not todo and size < limit * 0.9 and not a.final: break
        name = f"images-{n:03d}.tar"; local = os.path.join(ROOT, name); dest = os.path.join(a.out, name)
        with tarfile.open(local, "w") as tf:
            for f in batch: tf.add(os.path.join(IMAGES, f), arcname="images/" + f)
        subprocess.run(["cp", local, dest], check=True)
        if os.path.getsize(dest) != os.path.getsize(local): sys.exit(f"{name}: size mismatch after copy")
        os.remove(local)
        if wait_uploaded(dest) is False: sys.exit(f"{name}: not uploaded to the shared store after 30 min")
        for f in batch:
            i = meta[f]; index[f] = name
            sources[f] = {"source": i["url"], "file_page": "https://eq2.fandom.com/wiki/File:" + urllib.parse.quote(f),
                          "uploader": i.get("user"), "uploaded": i.get("uploaded") or i.get("timestamp"), "sha1": i["sha1"]}
        json.dump(index, open(index_path, "w"), ensure_ascii=False)
        json.dump(sources, open(sources_path, "w"), ensure_ascii=False, sort_keys=True)
        print(f"{name}: {len(batch)} files, {size / 1e6:.0f} MB; {len(index)} packed", flush=True)
        n += 1

if __name__ == "__main__":
    main()
