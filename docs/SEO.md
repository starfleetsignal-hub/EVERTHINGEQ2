# Search, sharing and the static pages

## What a search engine sees

The site is a single-page app: `index.html` plus gzip-JSON data that the browser fetches and renders. Its routes are
`#hash` URLs (`/#zones.antonica`). Everything after `#` is never sent to a server and search engines treat all of
them as the one URL `/`. So the 400k pages cannot be crawled one by one, whatever is put in a sitemap.

## What the build writes (tools/build_preview.py, tools/sitefiles.py)

| File | Purpose |
| --- | --- |
| `index.html` | Now has `<!doctype html>`, `<html lang="en">`, a viewport tag, a description, a canonical link and Open Graph / Twitter tags. The tab title and meta description follow the current route in the browser (`syncTitle()` in the template). |
| `robots.txt` | Allows everything and points to the sitemap. |
| `sitemap.xml` | The home page plus the static landing pages below (a sitemap index plus `sitemap-N.xml` files if it ever passes 50,000 URLs). |
| `404.html` | GitHub Pages serves it for unknown paths. It is `noindex` and has a small search box. |
| `<type>/<slug>/index.html` | Static landing pages, see below. |

The absolute address comes from `EQ2_SITE_URL`, else the `CNAME` file, else `https://<owner>.github.io/<repo>`.
If none is known the canonical and Open Graph URL tags and the sitemap are left out rather than written empty.

## Static landing pages

Zones, timelines, lore, housing and guides (about 1,870 pages) also get a small plain-HTML page at
`/<type>/<slug>/`, for example `/zones/antonica/`. It carries the page's facts, its opening paragraphs, its own title,
description and canonical link, the CC BY-SA credit, and an "Open the full page" button into the app. Nothing
redirects: a visitor from a search result sees the summary and can open the full page. They are 3 to 10 KB each
(13 MB for the 1,418 zone pages in a full build, 1,868 pages in all).

- Change the set with `EQ2_STATIC_TYPES` (comma list of content folders). Set it to an empty string to switch the pages,
  and with them the sitemap entries, off. Nothing else depends on them.
- Items, spells, quests, NPCs and the other ~400,000 pages are not included. Adding them would need the History API
  instead of `#` routes plus real per-page HTML, and 400k files do not fit the 1 GB Pages limit (the site is already
  578 MB). Adding quests (13,763) and achievements would be the next step if the zone pages show results.

## Checking after deploy

1. `https://everythingeq2.com/robots.txt`, `/sitemap.xml` and a bogus path (404 page) should answer.
2. Submit `https://everythingeq2.com/sitemap.xml` in Google Search Console and Bing Webmaster Tools.
3. View a landing page's source and the Open Graph preview of `/` in a link debugger.
