# Why the repository is about 760 MB, and what could change

Nothing in this document has been run. The commands in "Options" are proposals for the owner to approve.
The numbers were measured on 2026-10-03.

## Where the 760 MB comes from

GitHub reports the repository as 760,034 KB. That is two things:

| Part | Size | Notes |
| --- | --- | --- |
| `main` history | about 203 MB packed (180 MB of file contents, 23 MB of directory listings) | 452,827 objects. Unpacked that is 663 MB of files and 194 MB of directory listings. |
| `gh-pages` branch | about 555 MB packed, 578.0 MB in 43,096 files | Rebuilt from scratch and force-pushed on every build. |
| Releases (not counted) | 8.8 GB | eight `eq2-images-*.tar` (7.3 GB), six `web-pictures-*.tar` (0.46 GB), `images-release.json`. |

### `main`

| Path | Packed | Raw |
| --- | ---: | ---: |
| `content/items` (305,943 files) | 110 MB | 479 MB |
| `content/quests` | 16 MB | 39 MB |
| `images/` (7,159 item and spell icons) | 16 MB | 16 MB |
| `content/pages` | 12 MB | 45 MB |
| `content/spells` | 6 MB | 11 MB |
| everything else under `content/` and `data/` | about 17 MB | |
| `images-release.json` (13 MB, two versions in history) and `data/pictures.json` (3.6 MB) | about 3 MB + small | 26 MB |

Most of the history is the item pages. They are generated from the wiki, so they compress well and are not the problem
that needs solving. The checkout is 410k small files, which is slow to clone, to check out and to scan (about 1.6 GB on
disk because of block size).

### `gh-pages`

| Path | Size | Files |
| --- | ---: | ---: |
| `images/w/` 640 px WebP pictures | 429.1 MB | 34,523 |
| `data/p/` page chunks (gzip JSON) | 110.5 MB | 1,344 |
| `images/*.png` item and spell icons (the same files as on `main`) | 16.1 MB | 7,158 |
| `data/i/` type indexes | 9.5 MB | 14 |
| `data/g/` gear shards | 6.4 MB | 48 |
| `data/search.json.gz` | 5.6 MB | 1 |
| everything else | under 1 MB | |

WebP and gzip do not compress further inside git, so the 578 MB working tree is about 555 MB on the server.

The two parts add up to the 760 MB GitHub shows. Because the branch is an orphan commit that is force-pushed, old builds
become unreachable and GitHub removes them later, so builds do not pile up for ever. One thing made it worse than it
needed to be: `gzip.compress()` stamped the current time into every `.json.gz` file, so every build produced about 132 MB
of "new" files even when no page had changed (the live files carry the 2026-09-27 build time). This pull request sets
`mtime=0`, so an unchanged chunk is now byte-identical from build to build.

GitHub Pages also has a 1 GB limit on the published site; at 578 MB the site is using more than half of it.

## Options (proposed, not done)

Ordered from least to most disruptive. Sizes are estimates.

### 1. Deploy with GitHub Actions instead of a `gh-pages` branch (saves up to about 555 MB on the server)

`actions/upload-pages-artifact` plus `actions/deploy-pages` publish the same `build/site` without committing it. The
workflow needs `pages: write` and `id-token: write` instead of `contents: write`, and drops the token-in-URL push.

1. Change `.github/workflows/pages.yml` (a separate pull request; needs the `workflow` scope, which `gh` has).
2. Switch the Pages source once the new workflow has run green:

       gh api -X PUT repos/starfleetsignal-hub/EVERTHINGEQ2/pages -f build_type=workflow

3. Check the site, then (owner decision, destructive) remove the old branch. GitHub frees the space on its next cleanup,
   or on request to GitHub Support:

       git push origin --delete gh-pages

Rollback before step 3 is switching the source back: `gh api -X PUT repos/starfleetsignal-hub/EVERTHINGEQ2/pages -f build_type=legacy -f 'source[branch]=gh-pages' -f 'source[path]=/'`.

### 2. Shrink the pictures (saves about 100 to 190 MB of the 429 MB)

Re-encoding a random sample of 300 of the existing WebP files from `web-pictures-00.tar` (3.9 MB in total):

| Setting | Size | Saving |
| --- | ---: | ---: |
| WebP quality 60 | 2.9 MB | 26% |
| quality 50, at most 480 px wide | 2.3 MB | 40% |
| quality 40, at most 480 px wide | 2.0 MB | 48% |

The pictures are already small (average width 309 px, about 12 KB each), so most of the saving is quality, and
re-compressing lossy files adds visible artefacts. Doing it from the originals in the `eq2-images-*.tar` assets with
`tools/web_pictures.py` (change its quality and width constants) and re-running the "Web pictures" workflow gives better
results than re-compressing the WebP files. AVIF would save more but needs a fallback for older browsers.

### 3. Serve the pictures from somewhere else (removes 429 MB from the Pages site)

- A second static host, for example a separate Pages repository or a Cloudflare R2 / Pages bucket on
  `images.everythingeq2.com`, with `images/w/` uploaded from the `web-pictures-*.tar` assets. The site would use a base
  URL for pictures (a small change in `build_preview.img()` and the CSS background, not made here).
- GitHub release assets are not suitable as an image CDN: the URLs redirect, have no cache or CORS guarantees and are
  not meant for page assets.

### 4. History cleanup of `main`: not recommended

Rewriting history would remove only the two copies of `images-release.json` (3 MB packed) and `data/pictures.json`, plus
the 7,159 icons if they were moved out (16 MB). That is under 20 MB of 203 MB, and it would change every commit ID,
break open pull requests #4 and #11, and the 11 `claude/*` branches, and need a force-push to `main`. If the owner wants it
anyway, on a fresh mirror clone and after all branches are merged or closed:

    pip install git-filter-repo
    git clone --mirror https://github.com/starfleetsignal-hub/EVERTHINGEQ2.git eq2-clean.git
    cd eq2-clean.git
    git filter-repo --invert-paths --path images-release.json --path data/pictures.json
    # inspect with: git count-objects -vH
    # then, only with the owner's explicit approval:
    git push --force --mirror

Afterwards GitHub still keeps the old objects until its cleanup; ask GitHub Support to run a garbage collection.

### 5. Make clones smaller for contributors (no server change)

    git clone --filter=blob:none --sparse https://github.com/starfleetsignal-hub/EVERTHINGEQ2.git
    cd EVERTHINGEQ2 && git sparse-checkout set tools docs data content/quests content/zones

### 6. Generate instead of store

`images-release.json` (13 MB) is already on the `images` release, and `content/items` (306k pages, 110 MB packed) is
regenerated by the wiki sync. Either could be built in CI and left out of git. That is a larger pipeline change and is
out of scope here.

## What this pull request adds for size

- `.gitignore`: scratch folders (`content.new/`, `content.old/`), image bundles (`*.tar`, `*.tgz`, `*.zip`), local
  environments. Nothing tracked matches them.
- `.gitattributes`: binary markers for images and gzip, and `linguist-generated` for `content/items/**` and the large
  generated JSON files so their diffs are collapsed in pull requests.
- The deterministic `.json.gz` change described above.
