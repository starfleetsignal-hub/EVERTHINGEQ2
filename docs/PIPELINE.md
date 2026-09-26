# EQ2 wiki conversion (Norrath Ledger)

Source: eq2.fandom.com via the MediaWiki API (text is CC BY-SA 3.0; every page keeps a `source:` block for attribution).

## Layout
The shared project folder can't handle thousands of small files, so page folders are stored as bundles here and
unpacked on local disk to work (`tar xzf raw-shattered-lands.tgz` / `content-shattered-lands.tgz`).
- `raw/` one JSON per downloaded article (wikitext, revision id, categories, redirect aliases)
- `content/<type>s/<slug>.md` converted pages: YAML front matter (infobox fields + source) and Markdown body
- `data/redirects.json` link targets resolved through wiki redirects (null = page does not exist on the wiki)
- `images-needed.json` image files referenced by converted pages (not downloaded yet)
- `build/site/` preview site (index.html + data/ chunks), published as an Artifact

## Markdown conventions
- `[[Page title]]` or `[[Page title|text]]` links to another page (inside tables the pipe is written `\|`)
- `{{waypoint x, y, z}}` renders a chip that copies `/waypoint x, y, z`
- Zone, instance and island pages get a **Waypoint map**: every `{{waypoint}}` in the `location` of an NPC, monster, named, place or house page (and the `starts` of a quest) that names exactly one zone, plotted with north up (in EQ2 north is -z and east is -x). Built in `build_preview.zone_map()`.

## Commands (run from this folder)
    python3 tools/fetch.py --title Antonica --category "Antonica Quests"   # polite: 1 request/s, 50 pages per request
    python3 tools/convert.py
    python3 tools/assign_release.py      # files quests and items under the release that added them
    python3 tools/resolve_links.py
    python3 tools/build_preview.py

First sample (2026-09-23): Antonica, Antonica Timeline, Category:Antonica Quests (217), Category:Antonica Quest NPCs (132).

Shattered Lands (2026-09-23): categories Shattered Lands, Shattered Lands Zones/Quests/NPCs/Monsters/Named Monsters/POIs,
8,899 pages. Preview: https://claude.ai/artifact/XcYVrwehSXffqYQzgvFT7B
Metadata pass for truncated categories/redirects: `python3 tools/fetch.py --refresh-meta`

## Image download (handoff, 2026-09-23)
The page thread's environment can't reach Fandom's image host (static.wikia.nocookie.net, proxy 403), so images run in a
separate thread started after the user allowed that host.
    python3 tools/fetch_images.py --list       # data/allimages.json: name, url, size, sha1 for ~96k files (API, 1 req/s)
    python3 tools/fetch_images.py --download   # into images/, 4 workers, resumable
Work on local disk, then store images in the shared folder as tar bundles (e.g. images-000.tar per ~10,000 files),
never as loose files: the shared folder errors out on thousands of small files. Pages link images as images/<File_name>.
