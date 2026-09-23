#!/usr/bin/env bash
# Full rebuild: raw/*.json -> content/ -> releases -> site for GitHub Pages (build/site) -> bundles in the shared folder.
# Usage: tools/build_all.sh [owner/repo[/branch]]   (the repo makes "Edit this page" open GitHub's editor)
set -euo pipefail
cd "$(dirname "$0")/.."
SHARED=/mnt/project-files/eq2-wiki
rm -rf content.new; mkdir -p build
EQ2_CONTENT=content.new python3 tools/convert.py | cut -c1-2000
EQ2_CONTENT=content.new python3 tools/assign_release.py > build/releases.log; grep -E "^(quests|items)" build/releases.log
if [ -d content/guides ]; then cp -r content/guides content.new/; fi    # forum guide pages are written by hand, not converted
rm -rf content.old; [ -d content ] && mv content content.old; mv content.new content
# item and spell icons (Item_N.png / Spell_N.png) from the image bundles, when they are there
mkdir -p build/site/images
for t in "$SHARED"/images/*.tar; do
  [ -e "$t" ] || continue
  tar -xf "$t" -C build/site/images --wildcards --no-anchored 'Item_*.png' 'Spell_*.png' 2>/dev/null || true
done
find build/site/images -mindepth 2 -type f -exec mv -t build/site/images {} + 2>/dev/null || true
echo "icons: $(find build/site/images -maxdepth 1 -type f | wc -l)"
EQ2_TARGET=github EQ2_REPO="${1:-}" python3 tools/build_preview.py
# the shared store loses very large files, so bundles go up in 150 MB pieces and are checked after copying
# restore: cat content-full.tgz.part-* | tar -xzf -
saved() {  # full size in the shared folder, and rclone no longer marks it Dirty (not yet uploaded)
  local b; b=$(basename "$1")
  [ "$(stat -c %s "$SHARED/bundles/$b" 2>/dev/null)" = "$(stat -c %s "$1")" ] || return 1
  python3 - "$b" <<'PY'
import glob, json, sys
for m in glob.glob("/dev/shm/rclone-vfscache/vfsMeta/*/eq2-wiki/bundles/" + sys.argv[1]):
    sys.exit(0 if json.load(open(m)).get("Dirty") is False else 1)
PY
}
save() {   # save <name> <tar args...>
  local name=$1; shift
  rm -rf "/tmp/$name.parts"; mkdir -p "/tmp/$name.parts" "$SHARED/bundles"
  tar -czf - "$@" | split -b 150m - "/tmp/$name.parts/$name.part-"
  rm -f "$SHARED/bundles/$name".part-*
  for f in "/tmp/$name.parts"/*; do
    cp "$f" "$SHARED/bundles/"
    for _ in $(seq 90); do saved "$f" && break; sleep 10; done
    saved "$f" || { echo "not saved: $f (is the shared folder full? it holds about 10 GB)"; exit 1; }
  done
  echo "saved $name: $(ls "/tmp/$name.parts" | wc -l) part(s), $(du -sh "/tmp/$name.parts" | cut -f1)"
  rm -rf "/tmp/$name.parts"
}
save content-full.tgz content
save site-github-pages.tgz -C build site
echo "site: $(du -sh build/site | cut -f1), files: $(find build/site -type f | wc -l)"
