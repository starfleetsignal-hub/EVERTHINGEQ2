"""Run with:  python3 -m unittest discover -s tools -p "test_*.py"   (needs PyYAML, as convert.py does)."""
import os, sys, unittest
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import convert, wikifix


def md(title, wikitext):
    return convert.convert({"title": title, "wikitext": wikitext, "revid": 1, "timestamp": "2026-01-01T00:00:00Z", "categories": []})[2]


class Converter(unittest.TestCase):
    def test_pipe_template_in_link(self):
        out = md("T", "[[The Tower of the Drafling{{!}}Drafling Tower]] and [[Foo {{!}} Bar]]")
        self.assertIn("[[The Tower of the Drafling|Drafling Tower]]", out)
        self.assertIn("[[Foo|Bar]]", out)
        self.assertNotIn("{{", out)

    def test_pipe_template_in_template_argument(self):
        self.assertIn("[[Sunscar Coyote (Familiar)|Sunscar Coyote]]", md("T", "{{DTLine|Zonename = Sunscar Coyote (Familiar){{!}}Sunscar Coyote|Minlevel = 1}}"))

    def test_pagename_in_link_and_image(self):
        out = md("A Faro' Nuk hyas", "* [[{{PAGENAME}} (Silent City)]]\n[[File:{{PAGENAME}}.jpg|thumb]]")
        self.assertIn("[[A Faro' Nuk hyas (Silent City)]]", out)
        self.assertIn("images/A_Faro%27_Nuk_hyas.jpg", out.replace("'", "%27"))
        self.assertNotIn("PAGENAME", out)

    def test_unclosed_link_does_not_swallow_the_page(self):
        out = md("T", "Go to [[Sathir's Span]. Then\n\n==Rewards==\n*At least {{Coin|0|36|79|48}}\n*{{Faction|Riliss|+500}}")
        self.assertIn("36g 79s 48c", out)
        self.assertIn("+500 faction with **Riliss**", out)
        self.assertNotIn("{{", out)

    def test_coin_with_nested_info_is_dropped(self):
        out = md("T", "==Rewards==\n*{{Coin|||||{{info|how much?}}}}\n*{{Coin|15|50|||25000}}")
        self.assertNotIn("info", out)
        self.assertIn("15p 50g 25000 status", out)


class Leftovers(unittest.TestCase):
    """What build_preview does to pages that were converted before the fixes above."""
    def test_inline(self):
        f = wikifix.fix_inline
        self.assertEqual(f("[[A{{!}}B]]"), "[[A|B]]")
        self.assertEqual(f("[[{{PAGENAME}} (Sinking Sands)]]", "A Faro' Nuk hyas"), "[[A Faro' Nuk hyas (Sinking Sands)]]")
        self.assertEqual(f("![](images/{{PAGENAME}}.jpg)", "Barbcoat (TBoCH Good)"), "![](images/Barbcoat_%28TBoCH_Good%29.jpg)")
        self.assertEqual(f("At least {{Coin|0|36|79|48}}"), "At least 36g 79s 48c")
        self.assertEqual(f("{{coin|2500|20 | 99|500000}}"), "2500p 20g 99s 500000c")
        self.assertEqual(f("{{Coin|||||{{info|how much?}}}}"), "")
        self.assertEqual(f("{{Loc|386, -15, -79}}"), "{{waypoint 386, -15, -79}}")
        self.assertEqual(f("{{Faction|Riliss|+500}}"), "+500 faction with **Riliss**")
        self.assertEqual(f("plain {{waypoint 1, 2, 3}} text"), "plain {{waypoint 1, 2, 3}} text")

    def test_block_drops_info_only_items(self):
        self.assertEqual(wikifix.fix_block("x\n- {{info|how much?}} status\n- keep\n"), "x\n- keep\n")

    def test_coin_pipes_stay_in_one_cell(self):
        row = wikifix.protect_coin_pipes("a | {{coin|1|2 | 3}} | b")
        self.assertEqual(row.count("|"), 2)


if __name__ == "__main__":
    unittest.main()
