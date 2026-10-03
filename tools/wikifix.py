"""Wiki-template leftovers shared by convert.py (fixes them at the source) and build_preview.py (fixes pages that
were converted before the converter handled them, so the site is right without rewriting 400k Markdown files).

Handled: {{!}} (a pipe), {{PAGENAME}} and its variants, {{info|...}} notes, {{Coin|p|g|s|c|status}}, {{Loc|x|y|z}},
{{Faction|name|amount}} and the {{NPC}}/{{POI}}/{{Zone}}... link templates.
"""
import html, re, urllib.parse

PIPE = re.compile(r"\{\{\s*!\s*\}\}")
PAGENAME = re.compile(r"\{\{\s*(?:BASE|FULL|SUB|ROOT)?PAGENAME(?:E)?\s*\}\}", re.I)
INFO = re.compile(r"\{\{\s*info\s*(?:\|[^{}]*)?\}\}", re.I)
COIN = re.compile(r"\{\{\s*coin\s*\|((?:[^{}]|\{\{[^{}]*\}\})*)\}\}", re.I)
LOC = re.compile(r"\{\{\s*loc2?\s*\|\s*(-?[\d.]+)\s*[,|]\s*(-?[\d.]+)\s*[,|]\s*(-?[\d.]+)\s*\}\}", re.I)
COIN_IN_ROW = re.compile(r"\{\{\s*coin\s*\|[^{}]*\}\}", re.I)
FACTION = re.compile(r"\{\{\s*r?faction\s*\|([^{}|]*)(?:\|([^{}|]*))?[^{}]*\}\}", re.I)
LINKER = re.compile(r"\{\{\s*(?:npc|npcl|poi|zone|monster|named|item|equip|quest|instance|collection|recipe|spell)\s*\|([^{}|\[\]]+)(?:\|([^{}|\[\]]*))?\}\}", re.I)
# a list item that holds only an {{info}} note (old converter output: "- {{info|how much?}} status")
INFO_ITEM = re.compile(r"(?m)^[ \t]*(?:[-*]|\d+\.)[ \t]*(?:\{\{\s*info\b[^{}]*\}\}[ \t]*(?:status)?[ \t]*)$\n?", re.I)
LEFT = re.compile(r"\{\{\s*(?:!\s*\}\}|(?:(?:BASE|FULL|SUB|ROOT)?PAGENAME|info|coin|loc2?|r?faction|npcl?|poi|zone|monster|named|item|equip|quest|instance|collection|recipe|spell)\b)", re.I)


def coin_text(args):
    """'15|50|||25000' -> '15p 50g 25000 status'. Empty when no amount is given (e.g. an {{info}} placeholder)."""
    pos = [a.strip() for a in INFO.sub("", args).split("|")]
    pos += [""] * (5 - len(pos))
    bits = ["%s%s" % (v, u) for v, u in zip(pos[:4], "pgsc") if v and v != "0"]
    if pos[4]: bits.append("%s status" % pos[4])
    if not bits and not any(pos): return ""
    return " ".join(bits) or "0c"


def has_leftovers(s):
    return bool(LEFT.search(s))


def fix_inline(s, title=""):
    """Replace leftover templates in one (already HTML-escaped) inline fragment; title is the raw page title. {{!}} becomes '|' (so [[A{{!}}B]] is a piped link)."""
    if "{{" not in s or not LEFT.search(s): return s
    s = PIPE.sub("|", s)
    # a picture path must survive the Markdown image syntax, and a title can hold parentheses
    s = re.sub(r"(images/)" + PAGENAME.pattern, lambda m: m.group(1) + urllib.parse.quote(title.replace(" ", "_"), safe=""), s, flags=re.I)
    s = PAGENAME.sub(lambda m: html.escape(title, quote=False), s)
    s = COIN.sub(lambda m: coin_text(m.group(1)), s)
    s = LOC.sub(lambda m: "{{waypoint %s, %s, %s}}" % m.groups(), s)
    s = FACTION.sub(lambda m: "%s faction with **%s**" % ((m.group(2) or "+100").strip(), m.group(1).strip()), s)
    s = LINKER.sub(lambda m: "[[%s|%s]]" % (m.group(1).strip(), m.group(2).strip()) if (m.group(2) or "").strip() else "[[%s]]" % m.group(1).strip(), s)
    return INFO.sub("", s)


def fix_block(md):
    """Drop list items that only carry an {{info}} note (needs whole lines, so it runs on the body, not on fragments)."""
    return INFO_ITEM.sub("", md) if "{{" in md and re.search(r"\{\{\s*info", md, re.I) else md


def protect_coin_pipes(row):
    """The pipes inside {{Coin|a|b|c}} in a table row are not cell separators; hide them (as \\x05) while the row is split."""
    return COIN_IN_ROW.sub(lambda m: m.group(0).replace("|", "\x05"), row) if "{{" in row else row
