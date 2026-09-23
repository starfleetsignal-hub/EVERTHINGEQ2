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
| `content/<type>/<slug>.md` | The pages: quests, NPCs, zones, monsters, named, places, housing, lore, timelines, guides |
| `tools/` | The pipeline: fetch from the wiki, convert to Markdown, assign releases, resolve links, build the site |
| `tools/preview_template.html` | The site template (red, brown and green theme) |
| `data/redirects.json` | Wiki redirects, used to resolve links between pages |
| `guides/` | Index of player guides from the EverQuest II forums (our summaries, with credit and a link) |
| `images-needed.json` | Image files the pages reference |
| `docs/PIPELINE.md` | How the conversion works, step by step |

Current snapshot: 29,402 pages (all 23 releases' zones, quests, NPCs, monsters and places, plus 3 guides).
Items, spells, achievements and the rest of the wiki are still being converted and will be added.

Images are not in the repository yet. The whole wiki's images come to about 17.7 GB, well over what GitHub Pages
allows, so image hosting will be decided separately. Pages already point at `images/<File_name>`
and show images once they are available there.

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
    python3 tools/build_preview.py      # writes build/site/
    python3 -m http.server -d build/site 8000

EverQuest II is a trademark of Daybreak Game Company. This is a fan-made reference and is not affiliated with Daybreak or Fandom.
