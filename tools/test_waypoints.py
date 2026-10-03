"""Run with:  python3 -m unittest discover -s tools -p "test_*.py"   (needs PyYAML, as convert.py does)."""
import os, sys, unittest
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import convert


def md(wikitext, title="T"):
    return convert.convert({"title": title, "wikitext": wikitext, "revid": 1, "timestamp": "2026-01-01T00:00:00Z", "categories": []})[2]


class Coords(unittest.TestCase):
    def test_lenient_numbers(self):
        c = convert.coords
        self.assertEqual(c(["1,544.17", "509.", ".51"]), ["1544.17", "509", "0.51"])
        self.assertEqual(c(["-76,", "12", "-40"]), ["-76", "12", "-40"])
        self.assertEqual(c(["1 2 3 90 0 0"]), ["1", "2", "3"])          # /loc prints x y z heading pitch roll
        self.assertIsNone(c(["1", "2"]))
        self.assertIsNone(c(["a", "b", "c"]))

    def test_template_forms(self):
        self.assertIn("{{waypoint 1544.17, 509, 0.51}}", md("{{loc|1,544.17|509.|.51}}"))
        self.assertIn("{{waypoint 12, 5, -40}}", md("{{loc2|12, 5, -40|uid}}"))


class Prose(unittest.TestCase):
    def test_typed_coordinates_become_chips(self):
        for src in ("(loc 12, 5, -40)", "/way 12 5 -40", "( 12, 5, -40 )", "at 12, 5, -40"):
            self.assertIn("{{waypoint 12, 5, -40}}", convert.prose_waypoints("Find him " + src + " today"), src)

    def test_not_coordinates(self):
        for src in ("worth 40,000,000 coins", "every 25% (75, 50, 25)", "rolls (1, 2, 3, 4)", "see [[Foo (12, 5, -40)]]",
                    "https://example.com/at 12, 5, -40"):
            self.assertNotIn("{{waypoint", convert.prose_waypoints(src), src)

    def test_existing_chip_untouched(self):
        s = "{{waypoint 12, 5, -40}} and (loc 1, 2, 3)"
        self.assertEqual(convert.prose_waypoints(s), "{{waypoint 12, 5, -40}} and {{waypoint 1, 2, 3}}")


if __name__ == "__main__":
    unittest.main()
