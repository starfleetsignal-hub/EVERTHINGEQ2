#!/usr/bin/env python3
"""Copy newly downloaded raw/*.json into the shared folder as numbered tar.gz parts (<=20,000 pages each),
so a lost machine doesn't lose the download. A part is recorded in raw-parts/manifest.json only after it is
visible in the shared folder at full size. Restore: for f in raw-parts/raw-*.tgz; do tar -xzf "$f"; done
"""
import glob, json, os, subprocess, sys, time

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(HERE, ".."))
DEST = "/mnt/project-files/eq2-wiki/raw-parts"
PER_PART = 20000

def uploaded(name):
    """rclone marks a file Dirty until it reaches the store (a full store keeps files Dirty forever)."""
    for meta in glob.glob("/dev/shm/rclone-vfscache/vfsMeta/*/eq2-wiki/raw-parts/" + name):
        try: return json.load(open(meta)).get("Dirty") is False
        except Exception: return False
    return True

def main():
    os.makedirs(DEST, exist_ok=True)
    mpath = os.path.join(DEST, "manifest.json")
    man = json.load(open(mpath)) if os.path.exists(mpath) else {"parts": {}}
    done = {f for fs in man["parts"].values() for f in fs}
    new = sorted(f for f in os.listdir(os.path.join(ROOT, "raw")) if f.endswith(".json") and f not in done)
    n = len(man["parts"])
    for i in range(0, len(new), PER_PART):
        batch = new[i:i + PER_PART]
        if len(batch) < PER_PART and "--final" not in sys.argv: break     # wait for a full part unless finishing
        name = "raw-%03d.tgz" % n
        local = os.path.join("/tmp", name)
        lst = local + ".list"
        open(lst, "w").write("\n".join("raw/" + f for f in batch))
        subprocess.run(["tar", "-czf", local, "-C", ROOT, "-T", lst], check=True)
        size = os.path.getsize(local)
        subprocess.run(["cp", local, os.path.join(DEST, name)], check=True)
        for _ in range(60):                                   # the shared store uploads in the background
            if os.path.exists(os.path.join(DEST, name)) and os.path.getsize(os.path.join(DEST, name)) == size and uploaded(name): break
            time.sleep(10)
        else:
            print("not visible at full size yet:", name, file=sys.stderr); return 1
        man["parts"][name] = batch; n += 1
        json.dump(man, open(mpath + ".tmp", "w")); os.replace(mpath + ".tmp", mpath)
        os.remove(local); os.remove(lst)
        print("saved %s: %d pages, %.0f MB" % (name, len(batch), size / 1e6), flush=True)
    print("parts:", len(man["parts"]), "| pages saved:", sum(len(v) for v in man["parts"].values()),
          "| waiting for next part:", len(new) % PER_PART if "--final" not in sys.argv else 0)

if __name__ == "__main__":
    sys.exit(main())
