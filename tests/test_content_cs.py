import re
import unittest
from pathlib import Path

from detector.antislop import scan
from detector.patterns import REGEX_FLAGS, load_patterns

FIX = Path(__file__).resolve().parent / "fixtures"


def lines_without_findings(path, lang):
    text = path.read_text()
    hit = {f.line for f in scan(text, lang).findings}
    return [(i, l) for i, l in enumerate(text.split("\n"), 1) if l.strip() and i not in hit]


class ContentCsTest(unittest.TestCase):
    def test_linkedin_phrases_coverage(self):
        self.assertEqual(lines_without_findings(FIX / "cs/linkedin-slop.md", "cs"), [])
        self.assertEqual(lines_without_findings(FIX / "en/contrast.md", "en"), [])

    def test_clean_cs_zero_findings(self):
        r = scan((FIX / "cs/clean.md").read_text(), "cs")
        bad = [f for f in r.findings if f.severity in ("zero", "rewrite")]
        self.assertEqual(bad, [])
        self.assertGreaterEqual(r.words, 250)

    def test_every_cs_pattern_has_fixture_hit(self):
        for p in load_patterns("cs"):
            if p.kind != "regex":
                continue
            with self.subTest(p.id):
                self.assertRegex(p.example_before, re.compile(p.regex, REGEX_FLAGS))
                self.assertNotRegex(p.example_after, re.compile(p.regex, REGEX_FLAGS))


if __name__ == "__main__":
    unittest.main()
