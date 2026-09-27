#!/usr/bin/env python3
"""Shrink the pictures pages show (zone, NPC, item photos; not the Item_N/Spell_N icons) so the site can host them.

  web_pictures.py --plan [--allimages PATH]  write data/pictures.json: every picture the pages link to -> its wiki URL
  web_pictures.py --shard N                  download shard N from Fandom's image host, resize to at most 640 px wide,
                                             and pack it as web-pictures-NN.tar (run by CI; needs Pillow)
Tar members are images/w/<File_name>.webp. The Pages build unpacks them, and build_preview.img() links to them.
"""
import argparse, io, json, os, re, sys, tarfile, time, urllib.parse
from concurrent.futures import ThreadPoolExecutor

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from release_images import fetch    # kept-alive connections, retries, IPv4 only

ROOT = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
PLAN = os.path.join(ROOT, "data", "pictures.json")
SHARDS = 6
WIDTH, HEIGHT = 640, 1280
REF = re.compile(r"images/([^\"'<>()\s|]+?(?:\([^()\s]*\)[^\"'<>()\s|]*?)*\.(?:png|jpe?g|gif|webp|svg|bmp))", re.I)
ICON = re.compile(r"(Item|Spell)_\d+\.png$")

def picture_name(ref, title=""):
    """The wiki file name a page's images/... link means: URL-decoded, no File:/Image: prefix, {{PAGENAME}} filled in."""
    n = urllib.parse.unquote(ref).replace(" ", "_")
    n = re.sub(r"^(?:File|Image):", "", n, flags=re.I)
    return n.replace("{{PAGENAME}}", title.replace(" ", "_"))

def plan(allimages):
    wiki = {i["name"]: i["url"] for i in json.load(open(allimages)) if not i["mime"].startswith("video/")}
    lower = {n.lower(): n for n in wiki}
    want, missing = {}, set()
    for d, _, fs in os.walk(os.path.join(ROOT, "content")):
        for f in fs:
            text = open(os.path.join(d, f), encoding="utf-8", errors="replace").read()
            m = re.search(r"^title: (.+)$", text, re.M)
            title = m.group(1).strip().strip("'\"") if m else ""
            for ref in REF.findall(text):
                n = picture_name(ref, title)
                if ICON.match(n): continue
                n = n if n in wiki else lower.get(n.lower(), "")
                if n: want[n] = wiki[n]
                else: missing.add(picture_name(ref, title))
    json.dump(dict(sorted(want.items())), open(PLAN, "w"), ensure_ascii=False, indent=0)
    print(f"{len(want)} pictures; {len(missing)} linked pictures are not on the wiki", file=sys.stderr)

def shrink(data):
    from PIL import Image
    im = Image.open(io.BytesIO(data))
    animated = getattr(im, "is_animated", False)
    s = min(1, WIDTH / im.width, HEIGHT / im.height)
    size = (max(1, round(im.width * s)), max(1, round(im.height * s)))
    out = io.BytesIO()
    if animated:
        frames, durations = [], []
        for k in range(im.n_frames):
            im.seek(k); frames.append(im.convert("RGBA").resize(size, Image.LANCZOS)); durations.append(im.info.get("duration", 100))
        frames[0].save(out, "WEBP", save_all=True, append_images=frames[1:], duration=durations, loop=0, quality=75)
    else:
        im = im.convert("RGBA" if im.mode in ("RGBA", "LA", "P") else "RGB")
        im.resize(size, Image.LANCZOS).save(out, "WEBP", quality=80, method=5)
    return out.getvalue()

def work(item):
    name, url = item
    data = fetch({"url": url})
    if isinstance(data, str): return name, data
    try: return name, shrink(data)
    except Exception as e: return name, "could not read the picture: %s" % e

def shard(n, workers=16):
    items = [kv for k, kv in enumerate(sorted(json.load(open(PLAN)).items())) if k % SHARDS == n]
    t0, failed, done = time.time(), [], 0
    with tarfile.open(f"web-pictures-{n:02d}.tar", "w") as tar, ThreadPoolExecutor(workers) as ex:
        for k, (name, data) in enumerate(ex.map(work, items), 1):
            if isinstance(data, str): failed.append({"name": name, "error": data}); continue
            ti = tarfile.TarInfo("images/w/" + name + ".webp"); ti.size = len(data); ti.mtime = int(time.time())
            tar.addfile(ti, io.BytesIO(data)); done += 1
            if k % 500 == 0: print(f"  {k}/{len(items)} in {time.time() - t0:.0f}s, {len(failed)} failed", file=sys.stderr, flush=True)
            if k == 200 and len(failed) > 100: sys.exit(f"stopping: {len(failed)} of the first 200 failed, e.g. {failed[0]}")
    json.dump(failed, open(f"web-pictures-{n:02d}-failed.json", "w"), indent=1)
    print(f"web-pictures-{n:02d}.tar: {done} of {len(items)} pictures, {len(failed)} failed, {time.time() - t0:.0f}s", file=sys.stderr)

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--plan", action="store_true"); ap.add_argument("--shard", type=int)
    ap.add_argument("--list-shards", action="store_true", help="print the shard numbers as a JSON list (for the CI matrix)")
    ap.add_argument("--allimages", default=os.path.join(ROOT, "data", "allimages.json"))
    a = ap.parse_args()
    if a.plan: plan(a.allimages)
    if a.list_shards: print(json.dumps(list(range(SHARDS))))
    if a.shard is not None: shard(a.shard)
