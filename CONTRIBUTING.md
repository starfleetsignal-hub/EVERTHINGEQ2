# Contributing

## Editing a page

1. On the site, open the page and press **Edit this page**, then **Edit on GitHub**. Or find the file under
   `content/<type>/` on GitHub and press the pencil icon.
2. Change the text. Keep the front matter (between the `---` lines) valid YAML, and keep the `source:` block.
3. Commit to `main` (or open a pull request if you'd like a review). The **Build site** workflow rebuilds the
   site and publishes it within a few minutes.

Links use `[[Page title]]` or `[[Page title|shown text]]`. Waypoints use `{{waypoint x, y, z}}`.

New editors need to be added as collaborators under **Settings → Collaborators** on GitHub.

## Adding more converted content (pipeline)

The full-wiki conversion runs outside this repository and adds pages in batches. Work in a clone of this
repository so the tools write straight into it:

    git clone https://github.com/starfleetsignal-hub/everythingeq2.git && cd everythingeq2
    pip install pyyaml
    # raw/ (downloaded wikitext) is not committed; unpack an existing raw bundle here or fetch again
    python3 tools/fetch.py --all            # or --title / --category for a subset; 1 request/s
    python3 tools/convert.py
    python3 tools/assign_release.py
    python3 tools/resolve_links.py
    python3 tools/build_preview.py          # optional local check; CI builds the published site
    git add content data images-needed.json tools
    git commit -m "Add converted pages: <what>"
    git push origin main

`tools/build_all.sh [owner/repo]` does the convert, release and site steps in one go (it keeps `content/guides`).

Notes:

- Commit in batches of a few thousand pages per push rather than one huge push; very large pushes are slow and
  can time out.
- `convert.py` rewrites every file under `content/` it produces. Hand edits made on GitHub will be overwritten
  if that page is converted again, so after the site opens for editing, reconvert only new pages
  (`convert.py` accepts the raw files to convert) or check `git diff` before committing.
- `raw/`, `build/`, `images/` and `data/allimages.json` are ignored by git (see `.gitignore`).
- Images are not committed yet. See the README.

More detail on each step is in [docs/PIPELINE.md](docs/PIPELINE.md).
