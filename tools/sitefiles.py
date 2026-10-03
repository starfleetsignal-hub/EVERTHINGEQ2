"""Static files that sit next to the single-page app in build/site: robots.txt, sitemap.xml (or an index), 404.html and the
small crawlable "landing" pages for a few page types. Kept apart from build_preview.py so each piece can be tested alone.

The app itself routes with #hash URLs, which search engines treat as one URL, so only these static pages (and the home page)
can appear in a sitemap.
"""
import datetime, html, os, urllib.parse

MAX_URLS = 50000          # sitemap protocol limit per file


def site_url(root, repo=""):
    """Absolute site address without a trailing slash: EQ2_SITE_URL, else the CNAME file, else the github.io address, else ''."""
    explicit = os.environ.get("EQ2_SITE_URL", "").strip()
    if explicit: return explicit.rstrip("/")
    cname = os.path.join(root, "CNAME")
    if os.path.exists(cname):
        for line in open(cname, encoding="utf-8"):
            if line.strip(): return "https://" + line.strip()
    if "/" in repo:
        owner, name = repo.split("/")[:2]
        return "https://%s.github.io/%s" % (owner.lower(), name)
    return ""


def write_robots(site_dir, base):
    lines = ["User-agent: *", "Allow: /", ""]
    if base: lines.append("Sitemap: %s/sitemap.xml" % base)
    open(os.path.join(site_dir, "robots.txt"), "w", encoding="utf-8").write("\n".join(lines) + "\n")


def write_sitemaps(site_dir, base, urls):
    """urls: [(path, 'YYYY-MM-DD' or '')]. Writes sitemap.xml, or a sitemap index plus sitemap-N.xml when over the 50,000 limit."""
    if not base: return []
    def body(chunk):
        rows = "".join("<url><loc>%s</loc>%s</url>\n" % (html.escape(base + urllib.parse.quote(p, safe="/")),
                                                          "<lastmod>%s</lastmod>" % d if d else "") for p, d in chunk)
        return '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + rows + "</urlset>\n"
    parts = [urls[i:i + MAX_URLS] for i in range(0, len(urls), MAX_URLS)] or [[]]
    if len(parts) == 1:
        open(os.path.join(site_dir, "sitemap.xml"), "w", encoding="utf-8").write(body(parts[0]))
        return ["sitemap.xml"]
    names = []
    for n, chunk in enumerate(parts, 1):
        names.append("sitemap-%d.xml" % n)
        open(os.path.join(site_dir, names[-1]), "w", encoding="utf-8").write(body(chunk))
    today = datetime.date.today().isoformat()
    idx = "".join("<sitemap><loc>%s/%s</loc><lastmod>%s</lastmod></sitemap>\n" % (base, n, today) for n in names)
    open(os.path.join(site_dir, "sitemap.xml"), "w", encoding="utf-8").write(
        '<?xml version="1.0" encoding="UTF-8"?>\n<sitemapindex xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + idx + "</sitemapindex>\n")
    return ["sitemap.xml"] + names


STYLE = """<style>
:root{color-scheme:light dark;--bg:#f1e8dc;--panel:#fbf6ef;--text:#2a1c13;--muted:#6d5543;--link:#a3301f;--line:#d4c0a8;--btn:#a3301f;--btn-ink:#fff6f0}
@media (prefers-color-scheme:dark){:root{--bg:#1d1510;--panel:#281d16;--text:#ecdfcb;--muted:#b39c83;--link:#e57d69;--line:#4a3527;--btn:#c2412f;--btn-ink:#fff4ee}}
*{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--text);font:17px/1.55 "Alegreya Sans","Gill Sans","Segoe UI",system-ui,sans-serif}
header{background:var(--btn);color:var(--btn-ink);padding:10px 16px;border-bottom:3px solid #8a5a36}header a{color:inherit;font-weight:700;font-size:1.3rem;text-decoration:none}
main{max-width:760px;margin:0 auto;padding:24px 16px 48px}a{color:var(--link)}a:focus-visible,button:focus-visible,input:focus-visible{outline:2px solid #d2a85a;outline-offset:2px}
h1{font-family:"Alegreya SC",Palatino,Georgia,serif;font-size:clamp(1.8rem,5vw,2.4rem);line-height:1.1;margin:0 0 4px}.kind{color:var(--muted);margin:0 0 18px}
dl{display:grid;grid-template-columns:auto 1fr;gap:0;border:1px solid var(--line);border-radius:8px;background:var(--panel);margin:0 0 18px}dt,dd{margin:0;padding:6px 12px;border-top:1px solid var(--line)}dt:first-of-type,dt:first-of-type+dd{border-top:0}dt{color:var(--muted)}
.open{display:inline-block;background:var(--btn);color:var(--btn-ink);text-decoration:none;font-weight:700;border-radius:6px;padding:10px 18px;margin:6px 0 20px}
.credit{font-size:.85rem;color:var(--muted);border-top:1px solid var(--line);padding-top:10px;margin-top:28px}
form{display:flex;gap:8px;margin:18px 0}input[type=search]{flex:1;font:inherit;padding:8px 10px;border:1px solid var(--line);border-radius:6px;background:var(--panel);color:var(--text)}button{font:inherit;font-weight:700;padding:8px 16px;border:0;border-radius:6px;background:var(--btn);color:var(--btn-ink);cursor:pointer}
</style>"""


def head(title, desc, canonical="", extra=""):
    return ('<!doctype html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n'
            '<meta name="viewport" content="width=device-width,initial-scale=1">\n<title>%s</title>\n'
            '<meta name="description" content="%s">\n%s%s%s</head>\n<body>\n'
            '<header><a href="/">Norrath Ledger</a></header>\n') % (
        html.escape(title), html.escape(desc, quote=True),
        '<link rel="canonical" href="%s">\n' % html.escape(canonical) if canonical else "", extra, STYLE + "\n")


def not_found_html():
    return head("Page not found | Norrath Ledger", "This page does not exist on Norrath Ledger, the EverQuest II reference.", extra='<meta name="robots" content="noindex">\n') + (
        '<main>\n<h1>Page not found</h1>\n<p class="kind">There is nothing at this address.</p>\n'
        '<p>The pages on this site open from the <a href="/">start page</a>. Try a search:</p>\n'
        '<form id="f" role="search"><input type="search" id="q" name="q" aria-label="Search the wiki" placeholder="Search quests, items, zones, NPCs" autocomplete="off">'
        '<button type="submit">Search</button></form>\n'
        '<p><a href="/">Go to the start page</a></p>\n</main>\n'
        '<script>document.getElementById("f").addEventListener("submit",function(e){e.preventDefault();var v=document.getElementById("q").value.trim();'
        'location.href="/#"+(v?"search?q="+encodeURIComponent(v):"home");});</script>\n</body>\n</html>\n')


def landing_html(title, kind, desc, facts, paras, route, canonical, source):
    """A short static page for one wiki page: the facts and opening text a crawler can read, and a link into the app."""
    dl = "".join("<dt>%s</dt><dd>%s</dd>\n" % (html.escape(k), html.escape(v)) for k, v in facts)
    credit = ""
    if source:
        credit = ('<p class="credit">Adapted from <a href="%s" rel="nofollow noopener">%s</a> on the EverQuest II Wiki (Fandom), by '
                  '<a href="%s" rel="nofollow noopener">its contributors</a>. Licensed '
                  '<a href="https://creativecommons.org/licenses/by-sa/3.0/" rel="noopener">CC BY-SA 3.0</a>.</p>\n') % (
            html.escape(source["url"]), html.escape(source["title"]), html.escape(source["history"]))
    og = ('<meta property="og:type" content="article">\n<meta property="og:site_name" content="Norrath Ledger">\n'
          '<meta property="og:title" content="%s">\n<meta property="og:description" content="%s">\n%s') % (
        html.escape(title + " | Norrath Ledger", quote=True), html.escape(desc, quote=True),
        '<meta property="og:url" content="%s">\n' % html.escape(canonical, quote=True) if canonical else "")
    return head(title + " | Norrath Ledger", desc, canonical, og) + (
        '<main>\n<h1>%s</h1>\n<p class="kind">%s</p>\n%s%s<p><a class="open" href="/#%s">Open the full page</a></p>\n%s</main>\n</body>\n</html>\n') % (
        html.escape(title), html.escape(kind), "<dl>\n%s</dl>\n" % dl if dl else "",
        "".join("<p>%s</p>\n" % html.escape(p) for p in paras), urllib.parse.quote(route, safe=".-_"), credit)
