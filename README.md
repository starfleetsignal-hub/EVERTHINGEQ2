# Norrath Ledger

A clean, ad-free reference for **EverQuest II**, from The Shattered Lands through Rage of Cthurath.
Every page is a Markdown file in this repository, and the site is rebuilt and published to GitHub Pages
whenever a page changes.

**Site:** https://everythingeq2.com/

The page text is adapted from the [EverQuest II Wiki](https://eq2.fandom.com/) on Fandom (EQ2i) and is shared
under [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/). Each page names its source article,
revision and edit history. See [LICENSE.md](LICENSE.md).

## What's here

| Folder | Contents |
| --- | --- |
| `content/<type>/<slug>.md` | The pages: items, spells, achievements, quests, NPCs, zones, monsters, named, places, housing, lore, timelines, guides, other wiki pages |
| `tools/` | The pipeline: fetch from the wiki, convert to Markdown, assign releases, resolve links, build the site |
| `tools/preview_template.html` | The site template (red, brown and green theme) |
| `data/redirects.json` | Wiki redirects, used to resolve links between pages |
| `guides/` | Index of player guides from the EverQuest II forums (our summaries, with credit and a link) |
| `images-needed.json` | Image files the pages reference |
| `docs/PIPELINE.md` | How the conversion works, step by step |

<!-- counts:start -->
Current snapshot: **402,945 pages** (counted from `content/`; run `python3 tools/update_counts.py` after a bulk change).

| Type | Pages |
| --- | ---: |
| Items | 305,943 |
| Other pages | 33,749 |
| Quests | 13,763 |
| Achievements | 10,776 |
| Spells | 9,845 |
| Monsters | 9,058 |
| NPCs | 8,209 |
| Named monsters | 5,770 |
| Places | 3,964 |
| Zones and instances | 1,418 |
| Timelines | 283 |
| Housing | 98 |
| Lore | 66 |
| Player guides | 3 |
<!-- counts:end -->

Images: the small icons (`images/Item_N.png`, `images/Spell_N.png`) and the page background are in the repository. The
wiki's own pictures are far too large for it (the full set is about 8 GB), so they live as `eq2-images-*.tar` and
`web-pictures-*.tar` assets on the `images` release; the build downloads the 640 px WebP set (`web-pictures-*.tar`) and
publishes it with the site. Pages point at `images/<File_name>` and show a picture once it exists. See
[docs/REPO-SIZE.md](docs/REPO-SIZE.md) for where the repository's size comes from.

## Page format

Each page has YAML front matter (the infobox fields, `expansion:` and a `source:` block for attribution),
then a Markdown body with two extras:

- `[[Page title]]` or `[[Page title|shown text]]` links to another page (write `\|` for the pipe inside tables)
- `{{waypoint x, y, z}}` shows a chip that copies `/waypoint x, y, z` for the in-game chat

Keep the `source:` block when you edit a page: it is how the site credits the original wiki authors.

## Editing

Collaborators can press **Edit this page** on the site, or open the file under `content/` on GitHub and edit it
there. Saving to `main` rebuilds the site. See [CONTRIBUTING.md](CONTRIBUTING.md).

## Building locally

    pip install pyyaml
    python3 tools/build_preview.py      # writes build/site/ (all ~400k pages: several minutes and a few GB of memory)
    python3 -m http.server -d build/site 8000

For a quick try-out, point the build at a few pages: copy some `content/<type>/*.md` files into a folder and run
`EQ2_CONTENT=/that/folder EQ2_OUT=/tmp/out python3 tools/build_preview.py`. Tests for the converter fixes:
`python3 -m unittest discover -s tools -p "test_*.py"`. SEO files and the static landing pages are described in
[docs/SEO.md](docs/SEO.md).

EverQuest II is a trademark of Daybreak Game Company. This is a fan-made reference and is not affiliated with Daybreak or Fandom.
