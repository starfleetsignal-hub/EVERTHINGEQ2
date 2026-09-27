#!/usr/bin/env python3
"""Convert downloaded EQ2 wiki pages (raw/*.json) into Markdown files (content/<type>s/<slug>.md).

Markdown conventions for the site (kept simple so editors can write them by hand):
  [[Page title]] / [[Page title|link text]]   link to another page on the site
  {{waypoint x, y, z}}                        green chip that copies "/waypoint x, y, z"
  YAML front matter holds the infobox fields and the CC BY-SA source attribution.
"""
import glob, html, json, os, re, sys, collections
import yaml

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(HERE, ".."))
RAW = os.path.join(ROOT, "raw")
CONTENT = os.environ.get("EQ2_CONTENT", os.path.join(ROOT, "content"))
WIKI = "https://eq2.fandom.com/wiki/"

unknown_templates = collections.Counter()

# ---------------------------------------------------------------- helpers

def slugify(title):
    s = title.lower().replace("&", " and ").replace("'", "").replace("’", "")
    s = re.sub(r"[^a-z0-9]+", "-", s).strip("-")
    return s or "page"

def norm_title(t):
    t = html.unescape(t).replace("_", " ").strip().lstrip(":")
    t = re.sub(r"\s+", " ", t)
    return t[:1].upper() + t[1:] if t else t

def wiki_url(title):
    return WIKI + title.replace(" ", "_").replace("?", "%3F")

def find_close(s, i, open_, close):
    """s[i:] starts with open_; return index just past the matching close, honouring nesting of {{ }} and [[ ]]."""
    depth, j = 0, i
    while j < len(s):
        if s.startswith("{{", j) or s.startswith("[[", j):
            depth += 1; j += 2; continue
        if s.startswith("}}", j) or s.startswith("]]", j):
            depth -= 1; j += 2
            if depth == 0: return j
            continue
        j += 1
    return -1

def split_params(inner):
    """Split template/link inner text on top-level '|'."""
    parts, depth, cur, j = [], 0, [], 0
    while j < len(inner):
        two = inner[j:j + 2]
        if two in ("{{", "[["): depth += 1; cur.append(two); j += 2; continue
        if two in ("}}", "]]"): depth -= 1; cur.append(two); j += 2; continue
        if inner[j] == "|" and depth == 0:
            parts.append("".join(cur)); cur = []; j += 1; continue
        cur.append(inner[j]); j += 1
    parts.append("".join(cur))
    return parts

def template_args(parts):
    pos, named, n = {}, {}, 1
    for p in parts:
        m = re.match(r"\s*([A-Za-z_][\w ]*?)\s*=(.*)$", p, re.S)
        if m: named[m.group(1).strip().lower()] = m.group(2).strip()
        else: pos[n] = p.strip(); n += 1
    return pos, named

def first_nonempty(*vals):
    for v in vals:
        if v and v.strip(): return v.strip()
    return ""

# ---------------------------------------------------------------- per-page converter

HOLIDAYS = {"year of darkpaw": "Year of Darkpaw", "moonlight": "Moonlight Enchantments", "scorched sky": "Scorched Sky Celebration",
            "chronoportal phenomenon": "Chronoportal Phenomenon", "chronoportal phenomenon merchants": "Chronoportal Phenomenon",
            "nights of the dead": "Nights of the Dead", "frostfell": "Frostfell", "erollisiday": "Erollisi Day",
            "brew day": "Brew Day", "bristlebane": "Bristlebane Day", "heroesfestival": "Heroes' Festival",
            "oceansfullfestival": "Oceansfull Festival", "tinkerfest": "Tinkerfest", "moonlight enchantments": "Moonlight Enchantments"}
DROP = {"info", "wikify", "steps", "rewards", "created with census", "created_with_census", "zam", "ogaming",
        "epicweapquestbottom", "dab", "toc", "clear", "clr", "stub", "tocright", "-", "sic", "timeline", "capok",
        "factok", "factcheck", "test", "soeforums", "censusicon", "backtick", "obsolete", "eq2u", "zonerename", "rename",
        "copytext", "bug", "articles for deletion", "eq2questlist", "tentonhammer", "eq2traders", "link2lootdb", "update",
        "disambig", "hidediv", "hideclose", "claimeditem", "rtoc", "spelltypes", "masterharvesttop", "masterharvestbottom",
        "masterharvestt5", "sharedt8avatarloot", "for", "see also", "island", "czone", "accesszone", "droppeditem", "mspell",
        "malefemale", "need", "eq2map", "eq2flames"}
LINKERS = {"npc", "poi", "zone", "monster", "named", "item", "equip", "quest", "instance", "collection", "recipe",
           "spell", "faction page", "npcl"}
INFOBOXES = {"questinformation": "quest", "npcinformation": "npc", "zonebox": "zone", "zoneinformation": "zone",
             "izoneinformation": "instance", "tlinformation": "timeline", "lnlinformation": "lore",
             "monsterinformation": "monster", "namedinformation": "named", "poiinformation": "poi",
             "houseinformation": "house", "islandinformation": "island", "deityinformation": "lore",
             "iteminformation": "item", "equipinformation": "item", "adorninformation2": "item", "adorninformation": "item",
             "ammoinformation": "item", "recipebook": "item", "spellinformation2": "spell", "spellinformation": "spell",
             "achievement": "achievement", "tswritinformation": "quest", "cquestinformation": "quest",
             "osquestinformation": "quest", "nodeinformation": "poi", "aa2information": "page", "disambig": "disambiguation",
             "harvestinformation": "item", "bookinformation": "item", "titleinformation": "page",
             "factioninformation": "page", "prestigeinformation": "page"}
ITEM_KIND = {"equipinformation": "Equipment", "adorninformation2": "Adornment", "adorninformation": "Adornment",
             "ammoinformation": "Ammo", "recipebook": "Recipe book",
             "harvestinformation": "Harvestable", "bookinformation": "Book"}

class Page:
    def __init__(self, rec):
        self.rec = rec
        self.title = rec["title"]
        self.fm = {}            # front matter
        self.categories = list(rec.get("categories", []))
        self.images = []
        self.store = {}         # placeholder -> markdown
        self.kind = None
        self.box = None
        self.extra_md = ""      # sections built from infobox fields, appended to the body

    # placeholders keep converted links/templates away from the block parser
    def ph(self, md, block=False):
        k = ("\x02B%d\x03" if block else "\x02I%d\x03") % len(self.store)
        self.store[k] = md
        return k

    def unph(self, s, in_table=False):
        for _ in range(8):
            if "\x02" not in s: break
            s = re.sub(r"\x02[IB]\d+\x03", lambda m: self.store[m.group(0)].replace("|", "\\|") if in_table else self.store[m.group(0)], s)
        return s

    # ---------------- inline expansion (templates + links) -> text with placeholders
    def expand(self, s):
        out, i = [], 0
        while i < len(s):
            if s.startswith("{{", i) or s.startswith("[[", i):
                j = find_close(s, i, s[i:i+2], None)
                if j < 0: out.append(s[i:]); break
                inner = s[i + 2:j - 2]
                if s.startswith("{{", i):
                    out.append(self.template(inner))
                    i = j
                else:
                    m = re.match(r"[a-z]+", s[j:])       # link trail: [[gnoll]]s
                    trail = m.group(0) if m else ""
                    out.append(self.link(inner, trail))
                    i = j + len(trail)
                continue
            m = re.match(r"\[(https?://[^\s\]]+)(?:\s+([^\]]*))?\]", s[i:])
            if m:
                out.append(self.ph("[%s](%s)" % (self.inline(m.group(2) or m.group(1)), m.group(1))))
                i += m.end(); continue
            out.append(s[i]); i += 1
        return "".join(out)

    def inline(self, s):
        """Fully convert a fragment to finished inline Markdown."""
        s = self.expand(s)
        s = quotes(s)
        s = re.sub(r"\s*\n\s*", " ", s).strip()
        return self.unph(s)

    def wlink(self, target, text=None):
        target = norm_title(target)
        if not target: return text or ""
        if text is None or text.strip() == "" or text == target:
            return self.ph("[[%s]]" % target)
        return self.ph("[[%s|%s]]" % (target, text))

    def link(self, inner, trail=""):
        parts = split_params(inner)
        target = parts[0].strip()
        low = target.lower().lstrip(":")
        if re.match(r"(file|image):", low):
            opts = [p.strip() for p in parts[1:]]
            caption = ""
            for o in opts:
                if o and not re.match(r"^(thumb|thumbnail|frame|frameless|border|left|right|center|none|upright.*|\d+(x\d+)?px|x\d+px|link=.*|alt=.*)$", o, re.I):
                    caption = o
            name = norm_title(target.split(":", 1)[1])
            self.images.append(name)
            cap = plain(self.inline(caption)) if caption else ""
            return self.ph("![%s](images/%s)" % (cap, name.replace(" ", "_").replace("(", "%28").replace(")", "%29")))
        if low.startswith("category:") and not target.startswith(":"):
            self.categories.append(norm_title(target.split(":", 1)[1]))
            return ""
        if re.match(r"^[a-z]{2,3}(-[a-z]+)?:", target):   # interlanguage link, e.g. [[fr:...]]
            return ""
        if low.startswith("category:"):                     # [[:Category:X|text]] -> text only
            return self.inline(parts[1] if len(parts) > 1 else target.split(":", 2)[-1]) + trail
        if re.match(r"(user|user talk|talk|template|project|eq2i|everquest 2 wiki|special|help|w|wikipedia):", low):
            return self.inline(parts[1] if len(parts) > 1 else target.split(":", 1)[1]) + trail
        text = self.inline(parts[1]) if len(parts) > 1 and parts[1].strip() else None
        if trail: text = (text if text is not None else norm_title(target) if target[:1].isupper() else target) + trail
        return self.wlink(target, text)

    def template(self, inner):
        parts = split_params(inner)
        name = re.sub(r"\s+", " ", parts[0].replace("_", " ")).strip()
        key = name.lower()
        pos, named = template_args(parts[1:])
        P = lambda n: pos.get(n, "")

        if key in ("loc", "loc2", "masterloc"):
            nums = [P(1), P(2), P(3)] if P(2) or P(3) else re.split(r"[\s,]+", P(1))
            nums = [n.strip() for n in nums if n.strip()]
            if len(nums) == 3 and all(re.match(r"^-?\d+(\.\d+)?$", n) for n in nums):
                return self.ph("{{waypoint %s}}" % ", ".join(nums))
            return " ".join(nums)
        if key in LINKERS:
            if not P(1): return ""
            return self.wlink(self.inline(P(1)), self.inline(P(2)) if P(2) else None)
        if key in ("subclasslink", "class", "race", "deity", "classlink"):
            return self.wlink(P(1)) if P(1) else ""
        if key in ("raritycolor", "elementalcolor"):
            return self.inline(P(1))
        if key == "effect":
            return self.ph("**%s**" % self.inline(P(1))) if P(1) else ""
        if key == "rfaction":
            return self.ph("%s faction with **%s**" % (P(2) or "+100", self.inline(P(1))))
        if key == "questreward":
            return self.wlink(P(1), self.inline(P(3)) if P(3) else None)
        if key == "timedquest":
            return self.ph("*Timed quest: %s%s.*" % (self.inline(P(1)), (", " + self.inline(P(2))) if P(2) else ""))
        if key == "armorset":
            body = self.body(P(2))
            return "\n" + self.ph("**%s armor set**\n\n%s" % (self.inline(P(1)), body), block=True) + "\n"
        if key in ("a", "an"):
            return self.wlink("%s %s" % (key, P(1)), P(1)) + P(2)
        if key == "zonesb":
            return self.wlink("%s (%s)" % (P(1), P(2)), "%s [%s]" % (P(1), P(2)))
        if key == "itemsb":
            return self.wlink("%s (%s)" % (P(1), P(2)), "%s [%s]" % (P(1), P(2)))
        if key == "coin":
            bits = [f"{v}{u}" for v, u in ((P(1), "p"), (P(2), "g"), (P(3), "s"), (P(4), "c")) if v and v != "0"]
            st = named.get("5") or P(5)
            if st: bits.append(f"{st} status")
            return self.ph(" ".join(bits) or "0c")
        if key == "status":
            return self.ph(f"{P(1)} status")
        if key == "faction":
            amt = P(2) or "+100"
            return self.ph("%s faction with **%s**" % (amt, self.inline(P(1))))
        if key == "!": return "|"
        if key == "pagename": return self.title
        if key in ("repeatquest", "repeatable"):
            lim = named.get("limit") or P(1)
            self.fm["repeatable"] = int(lim) if lim.isdigit() else True
            return "This quest is repeatable" + (f" up to {lim} times." if lim else ".")
        if key in ("removed from game", "rfg", "removed"):
            self.fm["removed_from_game"] = self.inline(P(1)) if P(1) else True
            return ""
        if key in HOLIDAYS:
            self.fm.setdefault("events", []).append(HOLIDAYS[key]); return ""
        if key.endswith(" timeline") or key in DROP:
            return ""
        if key == "quote":
            body = self.body(P(1))
            q = "\n".join(("> " + l) if l else ">" for l in body.split("\n"))
            if P(2): q += "\n>\n> — " + self.inline(P(2))
            return "\n" + self.ph(q, block=True) + "\n"
        if key in INFOBOXES:
            return ""   # handled by extract_infobox
        if key in ("smalltable", "prettytable", "wikitable"):
            return "{|"
        if key in ("dialog", "dialogue") or key.startswith(":"):
            return ""
        if key == "citem":
            return self.wlink(named.get("item", P(1)))
        if key == "fromcrate":
            return "From " + self.wlink(P(1), self.inline(P(2)) if P(2) else None)
        if key == "itemfromquest":
            return "Quest: " + self.wlink(P(1), self.inline(P(2)) if P(2) else None)
        if key == "cquestreward":
            return "Collection reward: " + self.wlink(P(1))
        if key == "frompattern":
            return "Made from " + self.wlink(P(1), self.inline(P(2)) if P(2) else None)
        if key == "crafteditem":
            return "Crafted by %s (level %s)%s" % (self.wlink(P(1)), P(2), (" from " + self.wlink(P(3))) if P(3) else "")
        if key == "vendoritem":
            return "Sold by %s%s%s" % (self.wlink(P(2)) if P(2) else "a merchant", (" (" + P(1) + ")") if P(1) else "",
                                        (" in " + self.wlink(P(3))) if P(3) else "")
        if key == "equipmenteffect":
            return self.ph("**%s**" % self.inline(P(1))) if P(1) else ""
        if key == "spelleffectsline2":
            vals = [pos.get(i, "") for i in range(2, 10)]
            vals = [v for v in vals if v]
            return self.ph("%s: %s (Apprentice to Grandmaster)" % (P(1), " / ".join(vals))) if vals else ""
        if key == "obtainrecipe":
            src = P(1)
            if src.lower() == "drop": return "This recipe book drops from creatures (level %s)." % P(2) if P(2) else "This recipe book drops from creatures."
            return "Sold by tradeskill recipe merchants (%s)." % src if src else "Sold by tradeskill recipe merchants."
        if key == "droppedcrate":
            who = self.wlink(P(1), self.inline(P(2)) if P(2) else None) if P(1) else ""
            return "Dropped by %s%s" % (who or "a creature", (" in " + self.wlink(P(3))) if P(3) else "")
        if key == "plundered":
            loc = [P(i) for i in (2, 3, 4)]
            chip = self.template("loc|%s|%s|%s" % tuple(loc)) if all(re.fullmatch(r"-?[\d.]+", v or "") for v in loc) else ""
            return "Found in plundered chests in %s%s" % (self.wlink(P(1)), (" " + chip) if chip else "")
        if key == "missioncrate":
            return "From " + self.wlink(P(1))
        if key == "dtline":
            z, lv = named.get("zonename", ""), named.get("levelrange", "")
            return self.wlink(z) + (" (level %s)" % lv if lv else "") if z else ""
        if key in ("lootdb", "droppreview"):
            return ""
        if key == "tradeskillrecipemerchants":
            return "Recipe books like this are sold by tradeskill merchants in the major cities."
        if key in ("adornitem", "tinkeritem"):
            skill = "Adorning" if key == "adornitem" else "Tinkering"
            return "Made with %s (skill %s) from %s." % (skill, P(1), self.wlink(P(2))) if P(2) else "Made with %s (skill %s)." % (skill, P(1))
        if key == "hquestreward":
            return "Heritage quest reward: " + self.wlink(P(1), self.inline(P(3)) if P(3) else None)
        if key == "achievementreward":
            return "Achievement reward: " + self.wlink(P(1))
        if key in ("lonloot", "lon"):
            return "Legends of Norrath loot card"
        if key in ("spelleffectstop", "spelleffectsbottom2", "spelleffectsbottom", "aaeffectsbottom", "sfadorntabletop2", "adorntablebottom") \
                or key.startswith("aaeffectstop") or (key.startswith("all") and key.endswith("cats")):
            return ""
        if key.startswith("aaeffectsline"):
            vals = [v for v in (pos.get(i, "") for i in range(2, 30)) if v]
            return self.ph("%s: %s" % (P(1), " / ".join(vals))) if vals else ""
        if key == "citemlist":
            items = [named.get("item%d" % i, "") for i in range(1, 60)]
            return "\n" + self.ph("\n".join("- " + self.unph(self.wlink(v)) for v in items if v.strip()), block=True) + "\n"
        if key == "marketplaceitem":
            return "Marketplace" + (" (%s Daybreak Cash)" % P(1) if P(1) else "")
        if key == "sharedspawn":
            return self.ph("Shares its spawn point with " + ", ".join(self.inline(v) for v in pos.values() if v) + ".")
        if key == "charmpet":
            return self.ph("Can be charmed by %s." % (", ".join(v + "s" for v in pos.values() if v) or "charm classes"))
        unknown_templates[key] += 1
        return ""

    # ---------------- infobox -> front matter
    def extract_infobox(self, w):
        out, i = [], 0
        while i < len(w):
            if w.startswith("{{", i):
                j = find_close(w, i, "{{", None)
                if j < 0: break
                parts = split_params(w[i + 2:j - 2])
                key = parts[0].strip().lower().replace("_", " ")
                if key in INFOBOXES and self.kind is None:
                    self.kind = INFOBOXES[key]; self.box = key
                    pos, named = template_args(parts[1:])
                    self.infobox(self.kind, named)
                    out.append(w[i:i]); i = j
                    continue
                out.append(w[i:j]); i = j
                continue
            out.append(w[i]); i += 1
        return "".join(out)

    def val(self, v):
        return self.inline(v) if v else ""

    def pagelink(self, v):
        """A field that normally names a page: wrap bare names in a link."""
        v = (v or "").strip()
        if not v: return ""
        if "[[" in v or "{{" in v: return self.inline(v)
        return self.unph(self.wlink(v))

    def listval(self, v):
        items = []
        for line in re.split(r"\n|<br\s*/?>", v or "", flags=re.I):
            line = line.strip().lstrip("*#").strip()
            if line: items.append(self.inline(line))
        return items

    def located(self, a):
        loc = self.val(a.get("location"))
        mr = [x for x in re.split(r"[\s,]+", (a.get("mapref") or "").strip()) if x]
        if len(mr) == 3 and all(re.match(r"^-?\d+(\.\d+)?$", x) for x in mr):
            loc = (loc + " " if loc else "") + "{{waypoint %s}}" % ", ".join(mr)
        return loc.strip()

    def image(self, a, key="iname"):
        v = (a.get(key) or "").strip()
        if v and v != "*":
            self.images.append(norm_title(v))
            return "images/" + norm_title(v).replace(" ", "_")
        return ""

    COLLECTION_TYPES = {"n": "Shiny", "normal": "Shiny", "p": "Pages", "page": "Pages", "c": "Corpse", "h": "Hidden",
                        "a": "Aerial", "ht": "Hidden tradeskill", "hp": "Hidden purple", "meta": "Collection items",
                        "click": "Clickable", "yod": "Year of Discovery"}

    def collection(self, a, put):
        """CQuestInformation: collection zone, type, pieces (front matter, for the tracker) and rewards (body)."""
        zones = re.findall(r"\{\{\s*czone\s*\|\s*([^}|]+)", a.get("czones") or "", re.I)
        zones = [z.strip() for z in zones if z.strip()] or [(a.get("czone") or "").strip()]
        put("zone", ", ".join(self.pagelink(z) for z in zones if z))
        t = re.sub(r"\s+", " ", (a.get("type") or "").strip())
        if t and re.match(r"^[\w ,]+$", t):
            put("collection_type", self.COLLECTION_TYPES.get(t.lower(), t[:1].upper() + t[1:].lower()))
        pieces = []
        for line in (a.get("members") or "").split("\n"):
            line = line.strip().lstrip("*#").strip()
            if not line or line.lower().startswith("{{allmembers"): continue
            piece, icon = {}, re.search(r"\{\{\s*censusicon\s*\|\s*(\d+)\s*\}\}", line, re.I)
            line = re.sub(r"\{\{\s*censusicon\s*\|[^}]*\}\}", "", line, flags=re.I).strip()
            m = re.match(r"\[\[([^\]|]+)(?:\|([^\]]*))?\]\]", line) or re.match(r"'''(.+?)'''", line)
            if m and m.re.pattern.startswith(r"\[\["):
                target, name = norm_title(m.group(1)), plain(self.inline(m.group(2) or m.group(1)))
            elif m:
                target, name = "", plain(self.inline(m.group(1)))
            else:
                target, name, m = "", plain(self.inline(re.split(r"\s+-\s+|:\s", line)[0])), None
            if not name: continue
            piece["name"] = name
            if target and target != norm_title(name): piece["page"] = target
            if icon: piece["icon"] = "images/Item_%s.png" % icon.group(1)
            rest = line[m.end():] if m else line[len(re.split(r"\s+-\s+|:\s", line)[0]):]
            rest = re.sub(r"^[\s\-–:,.]+", "", rest.replace("'''", "").replace("''", "")).strip()
            if rest: piece["note"] = self.inline(rest)
            pieces.append(piece)
        if pieces: self.fm["pieces"] = pieces
        rewards = (a.get("rewards") or "").strip()
        if rewards:
            self.extra_md = "## Rewards\n\n" + self.body(rewards).strip()

    def infobox(self, kind, a):
        fm = self.fm
        def put(k, v):
            if isinstance(v, str) and not re.search(r"[\w\[]", v): return
            if v not in ("", None, [], {}, False): fm[k] = v
        yes = lambda k: (a.get(k) or "").strip().lower() in ("y", "yes", "1", "true")
        def levels():
            lo, hi = (a.get("levellow") or "").strip(), (a.get("level") or "").strip()
            return f"{lo}-{hi}" if lo and hi and lo != hi else hi or lo
        def diff():
            d, m = self.val(a.get("diff")), (a.get("levelmod") or "").strip()
            return (d + (" " + m if m else "")).strip()
        if kind == "quest" and self.box in ("questinformation", "osquestinformation", "cquestinformation"):
            put("level", self.val(a.get("level")))
            put("difficulty", self.val(a.get("diff")))
            put("zone", self.pagelink(a.get("szone")))
            tl = (a.get("timeline") or "").strip()
            put("timeline", self.pagelink(tl if not tl or "[[" in tl or tl.endswith("Timeline") else tl + " Timeline"))
            put("journal_category", self.val(a.get("jcat")))
            put("city_faction", self.val(a.get("faction")))
            put("starts", self.val(a.get("start")))
            put("prerequisite", self.pagelink(a.get("prereq")))
            put("next_quest", self.pagelink(a.get("next")))
            put("in_game_name", self.val(a.get("altname")))
            put("added_in", self.val(a.get("patch")))
            if (a.get("aaexp") or "").strip(): fm["achievement_xp"] = True
            if self.box == "cquestinformation": self.collection(a, put)
        elif kind == "npc":
            put("subtitle", self.val(a.get("idesc")))
            put("purpose", self.val(a.get("purpose")))
            put("race", self.val(a.get("race")))
            put("class", self.val(a.get("class")))
            put("zone", self.pagelink(a.get("zone")))
            put("faction", self.val(a.get("faction")))
            loc = self.val(a.get("location"))
            mr = [x for x in re.split(r"[\s,]+", (a.get("mapref") or "").strip()) if x]
            if len(mr) == 3 and all(re.match(r"^-?\d+(\.\d+)?$", x) for x in mr):
                loc = (loc + " " if loc else "") + "{{waypoint %s}}" % ", ".join(mr)
            put("location", loc.strip())
            put("added_in", self.val(a.get("patch")))
            if (a.get("iname") or "").strip():
                put("image", "images/" + norm_title(a["iname"]).replace(" ", "_")); self.images.append(norm_title(a["iname"]))
        elif kind == "zone":
            put("release", self.pagelink(a.get("introduced")))
            put("levels", self.val(a.get("levelrange")))
            put("access", self.val(a.get("instance")))
            put("adjacent_zones", self.listval((a.get("azones") or "").replace("]], [[", "]]\n[[")))
            put("timelines", self.listval((a.get("timelines") or "").replace("]], [[", "]]\n[[")))
            put("dungeons", self.listval(a.get("adungeons")))
            put("instances", self.listval(a.get("ainstances")))
            put("harvest_tier", self.val(a.get("harvestnodetier")))
            if (a.get("image") or "").strip():
                put("image", "images/" + norm_title(a["image"]).replace(" ", "_")); self.images.append(norm_title(a["image"]))
            put("image_caption", self.val(a.get("caption")))
        elif kind in ("monster", "named"):
            put("in_game_name", self.val(a.get("altname")))
            put("subtitle", self.val(a.get("idesc")))
            put("race", self.val(a.get("race")))
            put("class", self.val(a.get("class")))
            put("level", levels())
            put("difficulty", diff())
            put("group", self.val(a.get("group")))
            put("zone", self.pagelink(a.get("zone")))
            put("location", self.located(a))
            if yes("agro"): fm["aggressive"] = True
            if yes("social"): fm["social"] = True
            put("health", self.val(a.get("hp")))
            put("primary_damage", self.val(a.get("primedmg")))
            put("specials", self.val(a.get("specials") or a.get("special")))
            put("respawn", self.val(a.get("respawn")))
            put("placeholder", self.val(a.get("ph")))
            put("drops", self.listval(a.get("drops")))
            put("related_quests", self.listval(a.get("rquests")))
            if yes("aaxp"): fm["achievement_xp"] = True
            put("added_in", self.val(a.get("patch")))
            put("image", self.image(a))
        elif kind == "poi":
            put("zone", ", ".join(x for x in (self.pagelink(a.get(k)) for k in ("zone", "zone2", "zone3")) if x))
            put("location", self.located(a))
            put("discovery_xp", self.val(a.get("discovery")))
            put("achievement", self.val(a.get("achievement")))
            put("added_in", self.val(a.get("patch")))
            put("image", self.image(a))
            put("image_caption", self.val(a.get("idesc")))
        elif kind == "instance":
            put("release", self.pagelink(a.get("introduced")))
            put("levels", self.val(a.get("levelrange")))
            put("access", self.val(a.get("instance")))
            put("difficulty", self.val(a.get("zdiff")))
            put("entered_from", self.pagelink(a.get("azone") or a.get("pzone")))
            put("entrance", self.val(a.get("entrance")))
            put("players", "-".join(x for x in ((a.get("pmin") or "").strip(), (a.get("pmax") or "").strip()) if x))
            put("access_quest", self.pagelink(a.get("aquest")))
            put("related_quest", self.pagelink(a.get("rquest") or a.get("rquests")))
            put("success_lockout", self.val(a.get("slock")))
            put("failure_lockout", self.val(a.get("flock")))
            put("image", self.image(a))
            put("image_caption", self.val(a.get("idesc")))
        elif kind == "house":
            put("city", self.pagelink(a.get("city")))
            put("zone", self.pagelink(a.get("zone")))
            put("street", self.val(a.get("street")))
            put("location", self.located(a))
            put("price", self.val(a.get("price")))
            put("upkeep", self.val(a.get("upkeep")))
            put("rooms", self.val(a.get("rooms")))
            put("item_slots", self.val(a.get("vslots")))
            put("guild_level", self.val(a.get("gl")))
        elif kind == "item":
            put("item_kind", ITEM_KIND.get(self.box, "") or self.val(a.get("type")))
            put("item_subtype", self.val(a.get("subtype")))
            n = (a.get("iconnum") or "").strip()
            if re.fullmatch(r"\d+", n):
                fm["icon"] = "images/Item_%s.png" % n; self.images.append("Item %s.png" % n)
            put("tier", self.val(a.get("icat") or a.get("rarity")).strip("- ").title())
            put("level", self.val(a.get("level")).strip("- "))
            put("item_level", self.val(a.get("itemlevel")))
            put("slot", self.val(a.get("slot") or a.get("slotcolor")))
            put("classes", self.val(a.get("classes") or a.get("class")))
            put("flags", self.val(a.get("flags")))
            put("description", self.val(a.get("desc")))
            stats = {}
            for k in ("str", "sta", "agi", "wis", "int", "health", "power", "maxhealth", "mit", "crit", "critbonus", "potency",
                      "resolve", "fervor", "accuracy", "strike", "abmod", "aspeed", "dps", "multi", "flurry", "dblcast",
                      "wdmg", "cbovercap", "vselemental", "vsarcane", "vsnoxious", "mitinc", "damage", "dmg", "delay",
                      "drating", "range", "dtype", "wtype", "satiation", "duration", "charges", "casting", "recast"):
                v = self.val(a.get(k))
                if v and v not in ("-",): stats[k] = v
            put("stats", stats)
            # effectlist holds only the effect names; effectdesc holds the full text, so prefer it
            ek = next((k for k in ("effects", "effectdesc", "effectlist") if (a.get(k) or "").strip()), None)
            eff = a[ek] if ek else ""
            names = re.findall(r"\{\{\s*equipment\s*_?effect\s*\|\s*([^|}]+)", a.get("effectlist") or "", re.I) \
                if ek != "effectlist" else []
            put("effect_name", self.val(a.get("effectname")) or ", ".join(dict.fromkeys(n.strip() for n in names)))
            put("effects", self.body(eff) if eff else "")
            put("contains", self.body(a["contains"]) if (a.get("contains") or "").strip() else "")
            put("recipes", self.body(a["recipes"]) if (a.get("recipes") or "").strip() else "")
            put("creates", self.val(a.get("creates")))
            put("obtained_from", self.val(a.get("obtain")))
            put("used_in_quest", self.pagelink(a.get("rquest")))
            put("starts_quest", self.pagelink(a.get("squest")))
            put("item_link", (a.get("itemlink") or "").strip())
            put("image", self.image(a))
        elif kind == "spell":
            put("class", self.pagelink(a.get("class")))
            put("spell_type", self.val(a.get("type")))
            put("category", self.val(a.get("category")))
            n = (a.get("iconnum") or "").strip()
            if re.fullmatch(r"\d+", n):
                fm["icon"] = "images/Spell_%s.png" % n; self.images.append("Spell %s.png" % n)
            lv = [(a.get("l%d" % i) or "").strip() for i in range(1, 16)]
            put("levels", ", ".join(v for v in lv if v) or self.val(a.get("level")))
            for k, lab in (("target", "target"), ("power", "power_cost"), ("health", "health_cost"), ("conc", "concentration"),
                           ("cast", "cast_time"), ("recast", "recast"), ("duration", "duration"), ("range", "range"),
                           ("radius", "radius"), ("maxae", "max_targets"), ("mastery", "mastery")):
                put(lab, self.val(a.get(k)))
            put("description", self.val(a.get("desc")))
            put("effects", self.body(a["effects"]) if (a.get("effects") or "").strip() else "")
        elif kind == "achievement":
            put("in_game_name", self.val(a.get("name")))
            put("description", self.val(a.get("desc")))
            put("category", self.val(a.get("cat")))
            put("subcategory", self.val(a.get("subcat")))
            put("points", self.val(a.get("points")))
            put("requirements", self.listval((a.get("col1") or "") + "\n" + (a.get("col2") or "")))
            put("quota", self.val(a.get("quota")))
            put("rewards", self.listval(a.get("reward")))
            if (a.get("hidden") or "").strip(): fm["hidden"] = True
        elif kind == "quest" and self.box == "tswritinformation":
            put("tradeskill_class", self.pagelink(a.get("class")))
            put("level", self.val(a.get("level")))
            put("difficulty", self.val(a.get("diff")))
            put("writ_type", self.val(a.get("writtype")))
            put("description", self.val(a.get("desc")))
            put("timer", self.val(a.get("timer")))
        elif kind == "disambiguation":
            pass
        elif kind == "timeline":
            put("zone", self.pagelink(a.get("szone")))
            lo, hi = (a.get("levellow") or "").strip(), (a.get("levelhigh") or "").strip()
            put("levels", f"{lo}-{hi}" if lo and hi else lo or hi)
            put("difficulty", self.val(a.get("diff")))
            put("previous_timeline", self.pagelink(a.get("prev")))
            put("next_timeline", self.pagelink(a.get("next")))
            put("side_timelines", self.listval(a.get("sidetimeline")))
        else:
            for k, v in a.items():
                if k not in ("uid",) and v.strip(): put(k, self.val(v))

    # ---------------- block conversion
    def body(self, w):
        """Convert a chunk of wikitext (no infobox) to Markdown blocks."""
        s = self.expand(w)
        lines = s.split("\n")
        blocks, para, i = [], [], 0
        list_lines = []

        def flush_para():
            if para:
                blocks.append(self.unph(quotes("\n".join(l.strip() for l in para))))
                para.clear()
        def flush_list():
            if list_lines:
                blocks.append(self.render_list(list_lines)); list_lines.clear()

        while i < len(lines):
            line = lines[i]
            st = line.strip()
            if st.startswith("{|"):
                flush_para(); flush_list()
                j = i + 1; depth = 1
                while j < len(lines) and depth:
                    t = lines[j].strip()
                    if t.startswith("{|"): depth += 1
                    if t.startswith("|}"): depth -= 1
                    j += 1
                blocks.append(self.render_table(lines[i + 1:j - 1] if j - 1 > i else []))
                i = j; continue
            if st.startswith("|}"):
                i += 1; continue
            m = re.match(r"^(={1,6})\s*(.+?)\s*\1\s*$", st)
            if m:
                flush_para(); flush_list()
                lvl = max(2, len(m.group(1)))
                blocks.append("#" * lvl + " " + self.unph(quotes(m.group(2))))
                i += 1; continue
            if re.match(r"^\x02B\d+\x03$", st):
                flush_para(); flush_list(); blocks.append(self.unph(st)); i += 1; continue
            if st in ("\x01DETAILS_END",) or st.startswith("\x01DETAILS "):
                flush_para(); flush_list()
                blocks.append("</details>" if st == "\x01DETAILS_END" else
                              "<details><summary>%s</summary>" % self.unph(quotes(st[len("\x01DETAILS "):])))
                i += 1; continue
            if re.match(r"^[*#;]", st) or (re.match(r"^:", st) and list_lines):
                flush_para(); list_lines.append(st); i += 1; continue
            if st.startswith(":"):
                flush_list(); para.append(st.lstrip(":").strip()); i += 1; continue
            if st == "----":
                flush_para(); flush_list(); blocks.append("---"); i += 1; continue
            if not st:
                flush_para(); flush_list(); i += 1; continue
            flush_list(); para.append(st); i += 1
        flush_para(); flush_list()
        out = "\n\n".join(b for b in blocks if b.strip())
        return re.sub(r"\n{3,}", "\n\n", out).strip()

    def render_list(self, lines):
        out = []
        for l in lines:
            m = re.match(r"^([*#:;]+)\s*(.*)$", l)
            prefix, text = m.group(1), m.group(2)
            text = self.unph(quotes(text))
            if prefix.endswith(";"):
                text = "**%s**" % text.split(":", 1)[0].strip() + (": " + text.split(":", 1)[1].strip() if ":" in text else "")
            indent = ""
            for ch in prefix[:-1]:
                indent += "   " if ch == "#" else "  "
            last = prefix[-1]
            marker = "1. " if last == "#" else "- "
            if not text: continue
            out.append(indent + marker + text)
        return "\n".join(out)

    def render_table(self, rows_src):
        rows, cur, header_row = [], None, []
        caption = ""
        def cell_text(c):
            # strip "attr=... |" prefix when present
            if "|" in c:
                a, b = c.split("|", 1)
                if "=" in a or not a.strip(): c = b
            return c.strip()
        for raw in rows_src:
            t = raw.strip()
            if t.startswith("|-"):
                if cur is not None: rows.append(cur)
                cur = []; continue
            if t.startswith("|+"):
                caption = t[2:].strip(); continue
            if cur is None: cur = []
            if t.startswith("!"):
                for c in re.split(r"!!|\|\|", t[1:]): cur.append(("h", cell_text(c)))
            elif t.startswith("|"):
                for c in t[1:].split("||"): cur.append(("d", cell_text(c)))
            elif cur:
                k, v = cur[-1]; cur[-1] = (k, (v + "<br>" + t) if v else t)
            elif t:
                cur.append(("d", t))
        if cur: rows.append(cur)
        rows = [r for r in rows if r]
        if not rows: return ""
        conv = lambda v: re.sub(r"\s*\n\s*", " ", self.unph(quotes(v), in_table=True)).strip()
        if len(rows) == 1 and len(rows[0]) == 1:           # layout box (e.g. a floated image)
            return self.unph(quotes(rows[0][0][1].replace("<br>", "\n")))
        if all(k == "h" for k, _ in rows[0]): head, data = rows[0], rows[1:]
        else: head, data = [("h", "")] * max(len(r) for r in rows), rows
        n = max(len(head), max((len(r) for r in data), default=0))
        hdr = [conv(v) for _, v in head] + [""] * (n - len(head))
        lines = ["| " + " | ".join(hdr) + " |", "|" + "---|" * n]
        for r in data:
            cells = [conv(v) for _, v in r] + [""] * (n - len(r))
            lines.append("| " + " | ".join(cells) + " |")
        return ("**%s**\n\n" % conv(caption) if caption else "") + "\n".join(lines)

# ---------------------------------------------------------------- preprocessing

def plain(s):
    """Inline Markdown -> plain text (for image alt text)."""
    s = re.sub(r"\[\[([^\]|]*)\|([^\]]*)\]\]", r"\2", s)
    s = re.sub(r"\[\[([^\]]*)\]\]", r"\1", s)
    s = re.sub(r"\{\{waypoint ([^}]*)\}\}", r"\1", s)
    return s.replace("*", "").replace("[", "(").replace("]", ")").strip()

def quotes(s):
    s = s.replace("'''''", "\x04***\x04").replace("'''", "\x04**\x04").replace("''", "\x04*\x04")
    s = s.replace("\x04", "")
    return re.sub(r"(?<=\S)[ \t]+(\*{1,3})(?=[\s.,;:!?)]|$)", r"\1 ", s).rstrip(" ") if "*" in s else s

def preprocess(w):
    w = re.sub(r"<!--.*?(-->|$)", "", w, flags=re.S)
    w = re.sub(r"<nowiki>(.*?)</nowiki>", lambda m: html.escape(m.group(1)).replace("[", "&#91;").replace("{", "&#123;").replace("'", "&#39;"), w, flags=re.S)
    w = re.sub(r"</?(noinclude|includeonly|onlyinclude)>", "", w)
    w = re.sub(r"<ref[^>]*/>", "", w)
    w = re.sub(r"<ref[^>]*>.*?</ref>", "", w, flags=re.S)
    # collapsible dialog boxes -> <details>
    w = re.sub(r'<div class="NavFrame[^"]*"[^>]*>\s*<div class="NavHead"[^>]*>(.*?)</div>\s*<div class="NavContent"[^>]*>(.*?)</div>\s*</div>',
               lambda m: "\n\x01DETAILS %s\n\n%s\n\n\x01DETAILS_END\n" % (m.group(1).replace("&nbsp;", " ").strip(), m.group(2)), w, flags=re.S)
    w = re.sub(r"<br\s*/?>", "<br>", w, flags=re.I)
    w = re.sub(r"</?(center|u|big|small|span|div|font|p)\b[^>]*>", "", w, flags=re.I)
    w = re.sub(r"__\w+__", "", w)
    w = w.replace("&nbsp;", " ")
    return w

# ---------------------------------------------------------------- main

EXPANSIONS = ["Shattered Lands", "Desert of Flames", "Kingdom of Sky", "Echoes of Faydwer", "Rise of Kunark",
              "The Shadow Odyssey", "Sentinel's Fate", "Destiny of Velious", "Age of Discovery", "Chains of Eternity",
              "Tears of Veeshan", "Altar of Malice", "Terrors of Thalumbra", "Kunark Ascending", "Planes of Prophecy",
              "Chaos Descending", "Blood of Luclin", "Reign of Shadows", "Visions of Vetrovia", "Renewal of Ro",
              "Ballads of Zimara", "Scars of Destruction", "Rage of Cthurath"]

def expansion(categories):
    typed = re.compile(r"^(%s) (Zones|Quests|NPCs|Monsters|Named Monsters|POIs)$" % "|".join(re.escape(e) for e in EXPANSIONS))
    for c in categories:
        m = typed.match(c)
        if m: return m.group(1)
    for c in categories:
        if c in EXPANSIONS: return c
    return ""

TYPE_DIRS = {"item": "items", "spell": "spells", "achievement": "achievements", "disambiguation": "pages",
             "island": "zones", "monster": "monsters", "named": "named", "poi": "pois", "instance": "zones", "house": "housing",
             "quest": "quests", "npc": "npcs", "zone": "zones", "timeline": "timelines", "lore": "lore", "page": "pages"}

def classify(p):
    if p.kind: return p.kind
    if p.title.endswith(" Timeline"): return "timeline"
    cats = " ".join(p.categories).lower()
    if " quests" in cats: return "quest"
    return "page"

def drop_empty_sections(md):
    """Remove headings whose section has no text before the next heading of the same or higher level."""
    lines, changed = md.split("\n"), True
    while changed:
        changed, out = False, []
        heads = [(i, len(m.group(1))) for i, l in enumerate(lines) for m in [re.match(r"^(#{2,6}) ", l)] if m]
        drop = set()
        for n, (i, lvl) in enumerate(heads):
            end = heads[n + 1][0] if n + 1 < len(heads) else len(lines)
            has_text = any(l.strip() for l in lines[i + 1:end])
            sub = n + 1 < len(heads) and heads[n + 1][1] > lvl
            if not has_text and not sub: drop.add(i)
        if drop:
            lines = [l for i, l in enumerate(lines) if i not in drop]; changed = True
    return re.sub(r"\n{3,}", "\n\n", "\n".join(lines)).strip()

def convert(rec):
    p = Page(rec)
    w = preprocess(rec["wikitext"])
    w = p.extract_infobox(w)
    body = p.body(w)
    if p.extra_md: body = (body.rstrip() + "\n\n" + p.extra_md).strip()
    kind = classify(p)
    body = drop_empty_sections(body)
    fm = {"title": p.title, "type": kind}
    x = expansion(list(rec.get("categories", [])) + p.categories)
    if x: fm["expansion"] = x
    fm.update(p.fm)
    if rec.get("redirects"): fm["aliases"] = rec["redirects"]
    cats = [c for c in dict.fromkeys(p.categories) if not re.search(r"redlinks|Articles|Stubs?$|Pages with|Hidden", c)]
    if cats: fm["categories"] = cats
    fm["source"] = {"title": p.title, "url": wiki_url(p.title),
                    "history": wiki_url(p.title) + "?action=history",
                    "revision": rec["revid"], "revised": rec["timestamp"],
                    "license": "CC BY-SA 3.0"}
    front = yaml.safe_dump(fm, sort_keys=False, allow_unicode=True, width=1000)
    return kind, p, "---\n" + front + "---\n\n" + body + "\n"

def main(only=None):
    """Convert every raw page, or only the raw/*.json files named in `only` (keeps images-needed.json as is)."""
    files = sorted(glob.glob(os.path.join(RAW, "*.json"))) if not only else [f if os.path.exists(f) else os.path.join(RAW, f) for f in only]
    counts, images, slugs, failed = collections.Counter(), set(), {}, []
    for f in files:
        rec = json.load(open(f))
        if rec["wikitext"].lstrip().upper().startswith("#REDIRECT"): continue
        try:
            kind, p, md = convert(rec)
        except Exception as e:                    # one odd page must not stop a 400k-page run
            failed.append((rec["title"], repr(e)[:120])); continue
        d = os.path.join(CONTENT, TYPE_DIRS[kind]); os.makedirs(d, exist_ok=True)
        slug = slugify(rec["title"])
        if (kind, slug) in slugs and slugs[(kind, slug)] != rec["title"]:
            slug += "-" + str(rec["pageid"])
        slugs[(kind, slug)] = rec["title"]
        with open(os.path.join(d, slug + ".md"), "w") as fh: fh.write(md)
        counts[kind] += 1; images.update(p.images)
    if not only: json.dump(sorted(images), open(os.path.join(ROOT, "images-needed.json"), "w"), indent=1)
    print("converted:", dict(counts), "| images referenced:", len(images))
    if failed: print("failed:", len(failed), failed[:10])
    if unknown_templates: print("unhandled templates (dropped):", unknown_templates.most_common(30))

if __name__ == "__main__":
    main(sys.argv[1:] or None)
