#!/usr/bin/env python3
"""Render content/**/*.md into one self-contained preview page (build/preview.html).

The preview is a single file so it can be shared as one link; the real site will be one HTML file per page.
Markdown subset: headings, paragraphs, nested lists, pipe tables, blockquotes, <details>, emphasis,
[[wiki links]], {{waypoint x, y, z}}, [text](url), ![alt](images/...).
"""
import base64, glob, gzip, html, json, os, re
import yaml

ROOT = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
CONTENT = os.environ.get("EQ2_CONTENT", os.path.join(ROOT, "content"))
OUT = os.environ.get("EQ2_OUT", os.path.join(ROOT, "build"))
REDIRECTS = json.load(open(os.path.join(ROOT, "data", "redirects.json"))) if os.path.exists(os.path.join(ROOT, "data", "redirects.json")) else {}
PIN = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 21s-7-6.3-7-11.5A7 7 0 0 1 19 9.5C19 14.7 12 21 12 21z"/><circle cx="12" cy="9.5" r="2.4"/></svg>'
TYPE_LABEL = {"quest": "Quest", "npc": "NPC", "zone": "Zone", "instance": "Instance", "timeline": "Timeline", "lore": "Lore",
              "monster": "Monster", "named": "Named", "poi": "Place", "house": "House", "island": "Island", "page": "Page",
              "item": "Item", "spell": "Spell", "achievement": "Achievement", "disambiguation": "Disambiguation"}
CHUNKS = 100
PLURAL = {"quest": "Quests", "npc": "NPCs", "zone": "Zones", "instance": "Zones", "timeline": "Timelines", "lore": "Lore",
          "monster": "Monsters", "named": "Named monsters", "poi": "Places", "house": "Housing", "island": "Zones", "page": "Pages",
          "item": "Items", "spell": "Spells", "achievement": "Achievements", "disambiguation": "Pages", "guide": "Guides"}
BROWSE = {"quest": "quests", "npc": "npcs", "zone": "zones", "instance": "zones", "timeline": "timelines", "lore": "lore",
          "monster": "monsters", "named": "named", "poi": "pois", "house": "housing", "island": "zones", "page": "pages",
          "item": "items", "spell": "spells", "achievement": "achievements", "disambiguation": "pages", "guide": "guides"}

def fnv(s):
    h = 0x811c9dc5
    for b in s.encode("utf-8"):
        h = ((h ^ b) * 0x01000193) & 0xffffffff
    return h

# ---------------------------------------------------------------- load pages
pages, by_title = {}, {}
for f in sorted(glob.glob(os.path.join(CONTENT, "**", "*.md"), recursive=True)):
    src = open(f).read()
    _, front, body = src.split("---\n", 2)
    fm = yaml.safe_load(front)
    pid = os.path.relpath(f, CONTENT)[:-3]
    pages[pid] = {"fm": fm, "body": body, "src": src, "path": "content/" + pid + ".md"}
    for t in [fm["title"]] + fm.get("aliases", []):
        by_title.setdefault(t, pid); by_title.setdefault(t.lower(), pid)

def resolve(target):
    t = target.split("#")[0].strip()
    if not t: return None, False
    t = t[:1].upper() + t[1:]
    for cand in (t, REDIRECTS.get(t) or "", t.lower(), (REDIRECTS.get(t) or "").lower()):
        if cand and cand in by_title: return by_title[cand], True
    return None, REDIRECTS.get(t, "") is not None     # (no page here, exists on the wiki?)

# ---------------------------------------------------------------- inline
def esc(s):
    s = html.escape(s, quote=False)
    s = s.replace("&lt;br&gt;", "<br>")
    return re.sub(r"&amp;(#?\w+);", r"&\1;", s)

def emph(s):
    s = re.sub(r"\*\*\*(.+?)\*\*(.+?)\*(?!\*)", r"<em><strong>\1</strong>\2</em>", s)
    s = re.sub(r"\*\*\*(.+?)\*(.+?)\*\*", r"<strong><em>\1</em>\2</strong>", s)
    s = re.sub(r"\*\*\*(.+?)\*\*\*", r"<strong><em>\1</em></strong>", s)
    s = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", s)
    s = re.sub(r"(?<![\w*])\*(?!\s)(.+?)(?<!\s)\*(?![\w*])", r"<em>\1</em>", s)
    return s

missing_links = {}
def hid(pid):
    return pid.replace("/", ".")

def wikilink(m):
    target, text = m.group(1), m.group(2)
    label = emph(text if text is not None else target)
    pid, on_wiki = resolve(html.unescape(target))
    if pid:
        return '<a href="#%s" data-peek="%s">%s</a>' % (hid(pid), pid, label)
    missing_links[target] = missing_links.get(target, 0) + 1
    if on_wiki:
        return '<span class="pending" title="Not converted yet">%s</span>' % label
    return label

def inline(s):
    s = esc(s)
    s = re.sub(r"\{\{waypoint ([-\d.]+), ([-\d.]+), ([-\d.]+)\}\}",
               lambda m: '<button type="button" class="loc" data-loc="/waypoint %s, %s, %s" title="Copy /waypoint">%s%s, %s, %s</button>'
               % (m.group(1), m.group(2), m.group(3), PIN, m.group(1), m.group(2), m.group(3)), s)
    s = re.sub(r"!\[([^\]]*)\]\(([^)]+)\)", lambda m: img(m.group(2), m.group(1)), s)
    s = re.sub(r"\[\[([^\]|]+)(?:\|([^\]]*))?\]\]", wikilink, s)
    s = re.sub(r"\[([^\]]+)\]\((https?://[^)]+)\)", r'<a href="\2" rel="nofollow noopener" target="_blank">\1</a>', s)
    return emph(s)

def img(src, alt):
    # Images are not imported yet; show nothing until they are.
    if any(os.path.exists(os.path.join(d, src)) for d in (ROOT, os.path.join(OUT, "site"))):
        return '<img src="%s" alt="%s" loading="lazy">' % (src, alt)
    return ""

# ---------------------------------------------------------------- blocks
def render_list(lines, steps=False):
    items = []
    for l in lines:
        m = re.match(r"^( *)(- |\d+\. )(.*)$", l)
        if m: items.append([len(m.group(1)), m.group(2) != "- ", m.group(3)])
        elif items: items[-1][2] += " " + l.strip()
    def build(i, indent, top):
        out = []
        while i < len(items) and items[i][0] >= indent:
            ordered = items[i][1]
            cls = ' class="steps"' if (top and steps and ordered) else ""
            out.append("<ol%s>" % cls if ordered else "<ul>")
            while i < len(items) and items[i][0] == indent and items[i][1] == ordered:
                text = inline(items[i][2]); i += 1
                child = ""
                if i < len(items) and items[i][0] > indent:
                    child, i = build(i, items[i][0], False)
                inner = text + child
                out.append("<li>%s</li>" % ("<div>%s</div>" % inner if cls else inner))
            out.append("</ol>" if ordered else "</ul>")
            if i < len(items) and items[i][0] > indent:      # stray deeper item without parent
                child, i = build(i, items[i][0], False); out.append(child)
        return "".join(out), i
    return build(0, items[0][0] if items else 0, True)[0]

def render_table(lines):
    rows = [[c.strip().replace("\\|", "|") for c in re.split(r"(?<!\\)\|", l.strip()[1:-1])] for l in lines]
    head, body = rows[0], rows[2:]
    h = "".join("<th>%s</th>" % inline(c) for c in head) if any(head) else ""
    b = "".join("<tr>%s</tr>" % "".join("<td>%s</td>" % inline(c) for c in r) for r in body)
    return '<div class="tablewrap"><table>%s<tbody>%s</tbody></table></div>' % ("<thead><tr>%s</tr></thead>" % h if h else "", b)

def render(md, quest=False):
    lines, out, i, section = md.split("\n"), [], 0, ""
    while i < len(lines):
        l = lines[i]; st = l.strip()
        if not st: i += 1; continue
        m = re.match(r"^(#{1,6}) (.*)$", st)
        if m:
            lvl = min(len(m.group(1)), 4); section = re.sub(r"<[^>]+>", "", inline(m.group(2))).strip().lower()
            out.append("<h%d>%s</h%d>" % (lvl, inline(m.group(2)), lvl)); i += 1; continue
        if st == "---": out.append("<hr>"); i += 1; continue
        if st.startswith("<details>") or st == "</details>" or st.startswith("<summary>"):
            out.append(re.sub(r"<summary>(.*)</summary>", lambda m: "<summary>%s</summary>" % inline(m.group(1)), st)); i += 1; continue
        if st.startswith("|"):
            j = i
            while j < len(lines) and lines[j].strip().startswith("|"): j += 1
            out.append(render_table(lines[i:j])); i = j; continue
        if st.startswith(">"):
            j = i; q = []
            while j < len(lines) and lines[j].strip().startswith(">"):
                q.append(re.sub(r"^\s*> ?", "", lines[j])); j += 1
            out.append("<blockquote>%s</blockquote>" % render("\n".join(q))); i = j; continue
        if re.match(r"^(- |\d+\. )", st):
            j = i
            while j < len(lines) and lines[j].strip() and (re.match(r"^ *(- |\d+\. )", lines[j]) or lines[j].startswith(" ")): j += 1
            out.append(render_list(lines[i:j], steps=quest and section == "steps")); i = j; continue
        j = i; para = []
        while j < len(lines) and lines[j].strip() and not re.match(r"^(#{1,6} |\||>|- |\d+\. |<details|</details)", lines[j].strip()):
            para.append(lines[j].strip()); j += 1
        text = inline(" ".join(para)).strip()
        if text: out.append("<p>%s</p>" % text)
        i = j
    return "\n".join(out)

# ---------------------------------------------------------------- page chrome
FIELDS = {
    "quest": [("level", "Level"), ("difficulty", "Difficulty"), ("zone", "Zone"), ("collection_type", "Collection type"), ("timeline", "Timeline"),
              ("journal_category", "Journal"), ("city_faction", "City faction"), ("repeatable", "Repeatable"),
              ("achievement_xp", "Achievement XP"), ("expansion", "Release"), ("added_in", "Added in"), ("in_game_name", "In-game name")],
    "npc": [("subtitle", "Title"), ("race", "Race"), ("class", "Class"), ("purpose", "Role"), ("zone", "Zone"),
            ("location", "Location"), ("faction", "Faction"), ("added_in", "Added in")],
    "zone": [("release", "Release"), ("levels", "Levels"), ("access", "Access"), ("harvest_tier", "Harvest tier"),
             ("adjacent_zones", "Connects to"), ("dungeons", "Dungeons"), ("instances", "Instances"), ("timelines", "Timelines")],
    "monster": [("in_game_name", "In game"), ("race", "Race"), ("class", "Class"), ("level", "Level"), ("difficulty", "Difficulty"),
                ("group", "Group"), ("zone", "Zone"), ("location", "Location"), ("aggressive", "Aggressive"), ("social", "Social"),
                ("added_in", "Added in")],
    "named": [("in_game_name", "In game"), ("race", "Race"), ("class", "Class"), ("level", "Level"), ("difficulty", "Difficulty"),
              ("zone", "Zone"), ("location", "Location"), ("health", "Health"), ("primary_damage", "Damage"), ("specials", "Specials"),
              ("respawn", "Respawn"), ("placeholder", "Placeholder"), ("drops", "Drops"), ("related_quests", "Quests"),
              ("achievement_xp", "Achievement XP"), ("aggressive", "Aggressive"), ("added_in", "Added in")],
    "poi": [("zone", "Zone"), ("location", "Location"), ("discovery_xp", "Discovery XP"), ("achievement", "Achievement"), ("added_in", "Added in")],
    "instance": [("release", "Release"), ("levels", "Levels"), ("access", "Type"), ("difficulty", "Difficulty"), ("players", "Players"),
                 ("entered_from", "Entered from"), ("entrance", "Entrance"), ("access_quest", "Access quest"),
                 ("related_quest", "Related quest"), ("success_lockout", "Lockout"), ("failure_lockout", "Failure lockout")],
    "house": [("city", "City"), ("zone", "Zone"), ("street", "Street"), ("location", "Location"), ("price", "Price"),
              ("upkeep", "Upkeep"), ("rooms", "Rooms"), ("item_slots", "Item slots"), ("guild_level", "Guild level")],
    "item": [("item_kind", "Kind"), ("item_subtype", "Type"), ("tier", "Tier"), ("level", "Level"), ("item_level", "Item level"),
             ("slot", "Slot"), ("classes", "Classes"), ("flags", "Flags"), ("description", "Description"), ("stats", "Stats"),
             ("effect_name", "Effect"), ("effects", "Effects"), ("contains", "Contains"), ("recipes", "Recipes"), ("creates", "Creates"),
             ("obtained_from", "Obtained from"), ("expansion", "Release"), ("used_in_quest", "Used in quest"), ("starts_quest", "Starts quest"),
             ("item_link", "Item link")],
    "spell": [("class", "Class"), ("spell_type", "Type"), ("category", "Category"), ("levels", "Level"), ("target", "Target"),
              ("power_cost", "Power"), ("health_cost", "Health"), ("concentration", "Concentration"), ("cast_time", "Cast time"),
              ("recast", "Recast"), ("duration", "Duration"), ("range", "Range"), ("radius", "Radius"), ("max_targets", "Max targets"),
              ("mastery", "Mastery"), ("description", "Description"), ("effects", "Effects")],
    "achievement": [("in_game_name", "In game"), ("description", "Description"), ("category", "Category"), ("subcategory", "Subcategory"),
                    ("points", "Points"), ("requirements", "Requirements"), ("quota", "Quota"), ("rewards", "Rewards"), ("hidden", "Hidden")],
    "disambiguation": [],
    "timeline": [("zone", "Zone"), ("levels", "Levels"), ("difficulty", "Difficulty"),
                 ("previous_timeline", "Previous"), ("next_timeline", "Next"), ("side_timelines", "Side timelines")],
}

STAT = {"str": "STR", "sta": "STA", "agi": "AGI", "wis": "WIS", "int": "INT", "mit": "Mitigation", "dtype": "Armor type",
        "health": "Health", "power": "Power", "crit": "Crit chance", "critbonus": "Crit bonus", "potency": "Potency",
        "resolve": "Resolve", "multi": "Multi attack", "dps": "DPS mod", "haste": "Haste", "fervor": "Fervor",
        "ability": "Ability mod", "reuse": "Reuse speed", "casting": "Casting speed", "recovery": "Recovery speed",
        "block": "Block", "dmg": "Damage", "delay": "Delay", "rating": "Rating", "range": "Range", "wtype": "Weapon type"}
def fval(v, kind=None):
    if v is True: return "Yes"
    if isinstance(v, dict):
        return '<table class="stats">%s</table>' % "".join("<tr><th>%s</th><td>%s</td></tr>" % (
            html.escape(STAT.get(k, k.replace("_", " ").capitalize())), inline(str(x))) for k, x in v.items())
    if isinstance(v, str) and "\n" in v.strip(): return render(v)
    if isinstance(v, str) and v.startswith("\\aITEM"): return '<code class="itemlink">%s</code>' % html.escape(v)
    if isinstance(v, list): return "<br>".join(inline(str(x)) for x in v)
    return inline(str(v))

def plain(s):
    return re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", "", inline(str(s))))).strip()

IN_ZONE = {}
def index_zones():
    for pid, p in pages.items():
        z = p["fm"].get("zone")
        if not isinstance(z, str): continue
        for m in re.finditer(r"\[\[([^\]|]+)", z):
            zp, _ = resolve(m.group(1))
            if zp and zp != pid: IN_ZONE.setdefault(zp, []).append(pid)

GROUPS = [("quest", "Quests that start here"), ("npc", "NPCs"), ("named", "Named monsters"), ("monster", "Monsters"),
          ("poi", "Places"), ("house", "Housing"), ("instance", "Instances")]
def zone_section(pid):
    kids = IN_ZONE.get(pid, [])
    if not kids: return ""
    out = ['<h2>In this zone</h2><p class="derived">Gathered from every page that names this zone.</p>']
    for kind, label in GROUPS:
        ps = sorted((k for k in kids if pages[k]["fm"]["type"] == kind), key=lambda k: pages[k]["fm"]["title"].lower())
        if not ps: continue
        out.append('<details%s><summary>%s <span class="count">%d</span></summary><ul class="npcgrid">%s</ul></details>' % (
            " open" if kind == "quest" else "", label, len(ps),
            "".join('<li><a href="#%s" data-peek="%s">%s</a></li>' % (hid(k), k, html.escape(pages[k]["fm"]["title"])) for k in ps)))
    return "".join(out)

def piece_rows(pieces):
    """Collection pieces as [name, icon, page id, note]; the name is the key progress is saved under."""
    out = []
    for pc in pieces:
        if not isinstance(pc, dict) or not pc.get("name"): continue
        ppid = resolve(pc.get("page") or pc["name"])[0]
        icon = pc.get("icon", "")
        out.append([str(pc["name"]), icon if icon and img(icon, "") else "", ppid or "", pc.get("note", "")])
    return out

def collection_section(pid, pieces):
    """Checklist of a collection's pieces; the template restores and saves the ticks (localStorage)."""
    rows = piece_rows(pieces)
    if not rows: return ""
    items = "".join('<li><label><input type="checkbox" data-piece="%s">%s<span>%s</span></label>%s</li>' % (
        html.escape(n), '<img src="%s" alt="" loading="lazy">' % html.escape(ic) if ic else "",
        '<a href="#%s" data-peek="%s">%s</a>' % (hid(pp), pp, html.escape(n)) if pp else html.escape(n),
        ' <small>%s</small>' % inline(note) if note else "") for n, ic, pp, note in rows)
    return ('<section class="coll" data-coll="%s"><h2>Pieces <span class="count" data-coll-count>0 / %d</span></h2>'
            '<p class="derived">Tick the pieces you have found. Your progress is saved in this browser and shows in the '
            '<a href="#collections">collections tracker</a>.</p><ul class="pieces">%s</ul></section>') % (html.escape(pid), len(rows), items)

def build_page(pid, p):
    fm, kind = p["fm"], p["fm"]["type"]
    rows = []
    for k, label in FIELDS.get(kind, [(k, k.replace("_", " ").capitalize()) for k in fm if k not in
                                      ("title", "type", "aliases", "categories", "source", "image", "image_caption")]):
        if k in fm and k != "starts": rows.append("<dt>%s</dt><dd>%s</dd>" % (label, fval(fm[k])))
    if kind == "item" and not fm.get("expansion"): rows.append("<dt>Release</dt><dd>Release unknown</dd>")
    if fm.get("expansion_source") == "level":
        rows = [r.replace("<dt>Release</dt><dd>%s</dd>" % fval(fm["expansion"]),
                          "<dt>Release</dt><dd>%s <small>(estimated from its level)</small></dd>" % fval(fm["expansion"])) for r in rows]
    icon = img(fm["icon"], "") if fm.get("icon") else ""
    box = '<aside class="infobox"><header>%s%s</header><dl>%s</dl></aside>' % (icon, TYPE_LABEL.get(kind, "Page"), "".join(rows)) if rows else ""
    top = []
    if fm.get("removed_from_game"):
        note = fm["removed_from_game"]
        top.append('<p class="callout red"><strong>Removed from the game.</strong> %s</p>' % ("" if note is True else inline(note)))
    if fm.get("events"):
        top.append('<p class="tags">%s</p>' % " ".join('<span class="tag green">%s</span>' % html.escape(e) for e in fm["events"]))
    if kind == "quest":
        chain = []
        if fm.get("prerequisite"): chain.append('<div><small>Comes after</small>%s</div>' % inline(fm["prerequisite"]))
        chain.append('<strong><small>This quest</small>%s</strong>' % html.escape(fm["title"]))
        if fm.get("next_quest"): chain.append('<div><small>Leads to</small>%s</div>' % inline(fm["next_quest"]))
        if len(chain) > 1: top.append('<div class="chain">%s</div>' % "".join(chain))
        if fm.get("starts"): top.append('<p class="starts"><span class="tag red">Start</span> %s</p>' % inline(fm["starts"]))
    body = render(p["body"], quest=(kind == "quest"))
    if kind == "quest" and fm.get("pieces"): top.append(collection_section(pid, fm["pieces"]))
    s = fm.get("source")     # forum guides carry their own credit line in the body
    credit = "" if not s else ('<p class="credit">Adapted from <a href="%s" rel="nofollow noopener" target="_blank">%s</a> on the EverQuest II Wiki (Fandom), '
              'revision %s of %s, by <a href="%s" rel="nofollow noopener" target="_blank">its contributors</a>. '
              'Licensed <a href="https://creativecommons.org/licenses/by-sa/3.0/" rel="noopener" target="_blank">CC BY-SA 3.0</a>.</p>'
              % (s["url"], html.escape(s["title"]), s["revision"], s["revised"][:10], s["history"]))
    crumb = '<a href="#home">Home</a> › %s' % (inline(fm["zone"]) + " › " if fm.get("zone") and kind != "zone" else "") + ('<a href="#browse.%s">%s</a>' % (BROWSE[kind], PLURAL[kind]) if kind in BROWSE else PLURAL.get(kind, "Pages"))
    main = "\n".join(top) + "\n" + body + (zone_section(pid) if kind in ("zone", "instance", "island") else "")
    html_ = ('<div class="crumbs">%s</div><div class="art-head"><h1>%s</h1><button type="button" class="editbtn" data-edit="%s">Edit this page</button></div>'
             '<div class="%s"><div class="article">%s</div>%s</div>%s') % (
        crumb, html.escape(fm["title"]), pid, ("with-box" if main.strip() else "box-only") if box else "", main, box, credit)
    peek = TYPE_LABEL.get(kind, "Page")
    bits = []
    if kind == "quest":
        bits = [("Level " + str(fm["level"])) if fm.get("level") else "", fm.get("difficulty", ""), plain(fm.get("zone", ""))]
        summary = plain(fm.get("starts", ""))
    elif kind == "item":
        bits = [str(fm.get("item_kind", "")), str(fm.get("tier", "")), ("Level " + str(fm["level"])) if fm.get("level") else "", str(fm.get("slot", ""))]
        summary = plain(fm.get("description", "") or fm.get("obtained_from", ""))
    elif kind == "spell":
        bits = [plain(fm.get("class", "")), ("Level " + str(fm["levels"]).split(",")[0]) if fm.get("levels") else "", str(fm.get("category", ""))]
        summary = plain(fm.get("description", ""))
    elif kind == "achievement":
        bits = [str(fm.get("category", "")), str(fm.get("subcategory", "")), ("%s points" % fm["points"]) if fm.get("points") else ""]
        summary = plain(fm.get("description", ""))
    elif kind in ("npc", "monster", "named", "poi", "house"):
        bits = [("Level " + str(fm["level"])) if fm.get("level") else "", str(fm.get("difficulty", "")), str(fm.get("race", "")), plain(fm.get("zone", ""))]
        summary = plain(fm.get("location", ""))
    else:
        bits = [("Levels " + str(fm["levels"])) if fm.get("levels") else ""]
        m = re.search(r"^[^#|>\-!\n][^\n]{20,}", p["body"], re.M); summary = plain(m.group(0))[:200] if m else ""
    return html_, {"t": fm["title"], "k": peek, "m": " · ".join(b for b in bits if b), "s": summary[:220],
                   "a": fm.get("aliases", []), "lvl": str(fm.get("level", fm.get("levels", ""))), "d": str(fm.get("difficulty", fm.get("access", ""))),
                   "z": plain(fm.get("zone", "")) if kind != "zone" else "", "x": fm.get("expansion", ""),
                   "xe": 1 if fm.get("expansion_source") == "level" else 0}

# Classic weapon questlines players look for by name; shown with the signature questlines of their release.
FEATURED = {"Claymore Timeline": "The Claymore", "Swords of Destiny Timeline": "Swords of Destiny: Soulfire",
            "Prismatic Weapon Timeline": "Prismatic weapon", "Peacock Club Timeline": "Peacock Club: Prismatic 2.0"}

def questlines():
    """Per release: signature questlines, epic weapon quests (by class), heritage quests and timelines, in play order."""
    out = {}
    def title_of(v):
        m = re.search(r"\[\[([^\]|]+)", str(v or "")); return m.group(1).strip() if m else str(v or "").strip()
    def order(pids):
        by_t = {pages[p]["fm"]["title"]: p for p in pids}
        nxt, has_prev = {}, set()
        for p in pids:
            n = resolve(title_of(pages[p]["fm"].get("next_quest")))[0]
            if n in pids: nxt[p] = n; has_prev.add(n)
            pr = resolve(title_of(pages[p]["fm"].get("prerequisite")))[0]
            if pr in pids: has_prev.add(p); nxt.setdefault(pr, p)
        lvl = lambda p: (float((re.search(r"\d+(?:\.\d+)?", str(pages[p]["fm"].get("level", ""))) or re.search(r"\d+", "999")).group()), pages[p]["fm"]["title"])
        seq, seen = [], set()
        for start in sorted((p for p in pids if p not in has_prev), key=lvl) + sorted(pids, key=lvl):
            p = start
            while p and p not in seen:
                seen.add(p); seq.append(p); p = nxt.get(p)
        return seq
    groups = {}
    featured = {}                            # quest pid -> featured timeline title
    for tl in FEATURED:
        tp = resolve(tl)[0]
        if not tp: continue
        for m in re.finditer(r"\[\[([^\]|#]+)", pages[tp]["body"]):
            q = resolve(m.group(1).strip())[0]
            if q and pages[q]["fm"]["type"] == "quest": featured.setdefault(q, tl)
    for pid, p in pages.items():
        tl = title_of(p["fm"].get("timeline"))
        if p["fm"]["type"] == "quest" and tl in FEATURED: featured[pid] = tl
        fm = p["fm"]; x = fm.get("expansion"); cats = fm.get("categories", [])
        if not x: continue
        if fm["type"] == "timeline":
            groups.setdefault((x, "tl", "Timelines"), []).append(pid); continue
        if fm["type"] != "quest": continue
        epic = [c for c in cats if "Epic Weapon" in c]
        if epic:
            cls = next((re.match(r"(.+?) Epic Weapon Quests", c).group(1) for c in epic if re.match(r".+? Epic Weapon Quests", c)), "")
            if "Epic Weapon 2.0 Quests" in cats: cls = "Epic 2.0" + (": " + cls if cls else "")
            groups.setdefault((x, "epic", cls or "All classes"), []).append(pid)
        elif pid in featured:
            groups.setdefault((x, "sig", FEATURED[featured[pid]]), []).append(pid)
        elif "Signature Quests" in cats:
            name = plain(fm.get("timeline", ""))
            if name.lower() in ("", "signature quest timeline", "signature quests timeline"): name = "Other signature quests"
            groups.setdefault((x, "sig", name), []).append(pid)
        if "Heritage Quests" in cats:
            groups.setdefault((x, "her", "Heritage quests"), []).append(pid)
    for (x, kind, name), pids in sorted(groups.items(), key=lambda kv: (kv[0][0], kv[0][1], kv[0][2].startswith(("Other", "All")), kv[0][2])):
        out.setdefault(x, {}).setdefault(kind, []).append([name, order(pids) if kind in ("sig", "epic") else
                                                          sorted(pids, key=lambda p: pages[p]["fm"]["title"])])
    return out

# "artifact": base64 text chunks + source chunks (claude.ai preview); "github": .gz chunks (GitHub Pages, the default in CI)
TARGET = os.environ.get("EQ2_TARGET", "github" if os.environ.get("GITHUB_ACTIONS") else "artifact")
# "owner/name[/branch]": Edit this page opens GitHub's editor (in CI, the repository being built)
REPO = os.environ.get("EQ2_REPO", os.environ.get("GITHUB_REPOSITORY", ""))
PER_CHUNK = 300                                        # pages per data chunk

def main():
    index_zones()
    site = os.path.join(OUT, "site"); data_dir = os.path.join(site, "data")
    import shutil
    shutil.rmtree(data_dir, ignore_errors=True)
    for sub in ("p", "s", "i"): os.makedirs(os.path.join(data_dir, sub), exist_ok=True)
    nch = max(100, -(-len(pages) // PER_CHUNK)) if TARGET == "github" else 100
    width = len(str(nch - 1))
    ext = ".json.gz" if TARGET == "github" else ".txt"
    chunks_h, chunks_s = [{} for _ in range(nch)], [{} for _ in range(nch)]
    by_type, search, counts = {}, [], {}
    for pid, p in pages.items():
        h, m = build_page(pid, p)
        c = fnv(pid) % nch
        chunks_h[c][pid] = h
        if TARGET != "github" or not REPO: chunks_s[c][pid] = {"src": p["src"], "path": p["path"]}
        ty = pid.split("/")[0]
        by_type.setdefault(ty, {})[pid] = [m["t"], m["k"], m["m"], m["s"], m["lvl"], m["d"], m["z"], m["x"]] + ([1] if m["xe"] else [])
        search.append([pid, m["t"], m["k"], m["z"]] + list(m["a"] or []))
        counts.setdefault(ty, {}); counts[ty][m["x"]] = counts[ty].get(m["x"], 0) + 1
    total = 0
    def put(path, obj):
        raw = gzip.compress(json.dumps(obj, ensure_ascii=False, separators=(",", ":")).encode(), 9)
        if TARGET != "github": raw = base64.b64encode(raw)   # artifacts serve text, not binary: gzip + base64
        open(path + ext, "wb").write(raw)
        return len(raw)
    for c in range(nch):
        total += put(os.path.join(data_dir, "p", str(c).zfill(width)), chunks_h[c])
        if chunks_s[c]: total += put(os.path.join(data_dir, "s", str(c).zfill(width)), chunks_s[c])
    isz = 0
    for ty, d in by_type.items(): isz += put(os.path.join(data_dir, "i", ty), d)
    ssz = put(os.path.join(data_dir, "search"), search)
    colls = [[pid, p["fm"]["title"], str(p["fm"].get("level", "")), plain(p["fm"].get("zone", "")), p["fm"].get("expansion", ""),
              str(p["fm"].get("collection_type", "")), [r[:3] for r in piece_rows(p["fm"]["pieces"])]]
             for pid, p in sorted(pages.items(), key=lambda kv: kv[1]["fm"]["title"].lower())
             if p["fm"]["type"] == "quest" and isinstance(p["fm"].get("pieces"), list)]
    colls = [c for c in colls if c[6]]
    csz = put(os.path.join(data_dir, "collections"), colls)
    lines = {x: {k: [[n, [[q, pages[q]["fm"]["title"], str(pages[q]["fm"].get("level", ""))] for q in l]] for n, l in groups]
                 for k, groups in L.items()} for x, L in questlines().items()}
    zones = {pid: v for pid, v in by_type.get("zones", {}).items()}
    msz = put(os.path.join(data_dir, "meta"), {"chunks": nch, "width": width, "ext": ext, "counts": counts, "lines": lines,
                                               "zones": zones, "collections": len(colls), "repo": REPO, "src": bool(any(chunks_s))})
    total += isz + ssz + msz + csz
    tpl = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "preview_template.html")).read()
    tpl = tpl.replace("/*EXT*/", json.dumps(ext))
    open(os.path.join(site, "index.html"), "w").write(tpl)
    nfiles = sum(len(fs) for _, _, fs in os.walk(site))
    print("pages:", len(pages), "| target:", TARGET, "| files:", nfiles, "| data: %.1f MB (type indexes %.1f, search %.1f, meta %.1f)"
          % (total / 1e6, isz / 1e6, ssz / 1e6, msz / 1e6), "| distinct links to pages not converted yet:", len(missing_links))

main()
