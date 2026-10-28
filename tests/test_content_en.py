import re
import unittest
from pathlib import Path

from detector.antislop import scan
from detector.patterns import REGEX_FLAGS, load_patterns

FIX = Path(__file__).resolve().parent / "fixtures"


def missed(path, lang, profile=None):
    text = path.read_text()
    hit = {f.line for f in scan(text, lang, profile).findings}
    return [(i, l) for i, l in enumerate(text.split("\n"), 1) if l.strip() and i not in hit]


class ContentEnTest(unittest.TestCase):
    def test_en_fixture_hits(self):
        self.assertEqual(missed(FIX / "en/email-slop.md", "en", "email"), [])
        self.assertEqual(missed(FIX / "en/linkedin-slop.md", "en", "post"), [])
        self.assertEqual(missed(FIX / "en/feedback-slop.md", "en", "feedback"), [])

    def test_clean_en_zero_findings(self):
        r = scan((FIX / "en/clean.md").read_text(), "en", "offer")
        self.assertEqual([f for f in r.findings if f.severity in ("zero", "rewrite")], [])
        self.assertGreaterEqual(r.words, 250)

    def test_every_en_pattern_has_fixture_hit(self):
        for p in load_patterns("en"):
            if p.kind != "regex":
                continue
            with self.subTest(p.id):
                self.assertRegex(p.example_before, re.compile(p.regex, REGEX_FLAGS))
                self.assertNotRegex(p.example_after, re.compile(p.regex, REGEX_FLAGS))

    def test_calques_both_directions(self):
        self.assertEqual(missed(FIX / "en/calques.md", "en"), [])
        self.assertEqual(missed(FIX / "cs/calques.md", "cs"), [])
        cats = {f.category for f in scan((FIX / "cs/calques.md").read_text(), "cs").findings}
        self.assertEqual(cats, {"calque"})

    def test_vocab_single_use_silent(self):
        text = (FIX / "en/clean.md").read_text().replace("The extension costs", "We delve into it. The extension costs")
        self.assertEqual([f for f in scan(text, "en").findings if f.rule_id == "x-excess-vocab"], [])


if __name__ == "__main__":
    unittest.main()
