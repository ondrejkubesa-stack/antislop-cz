import json
import subprocess
import sys
import unittest
from pathlib import Path

from detector.antislop import scan
from detector.patterns import load_patterns

ROOT = Path(__file__).resolve().parent.parent
FIX = ROOT / "tests/fixtures/scan"
PATS = load_patterns("cs", FIX / "patterns_cs.json")


def run(text, **kw):
    kw.setdefault("lang", "cs")
    return scan(text, patterns=PATS, **kw)


def cli(*args):
    return subprocess.run([sys.executable, "-m", "detector.antislop", *args,
                           "--patterns", str(FIX / "patterns_cs.json")],
                          cwd=ROOT, capture_output=True, text=True)


class ScanTest(unittest.TestCase):
    def test_phrase_hit_has_position(self):
        r = run((FIX / "hit.md").read_text())
        self.assertEqual([(f.rule_id, f.line, f.col) for f in r.findings], [("cs-t-doba", 4, 1)])

    def test_quoted_phrase_not_reported(self):
        r = run("Fráze „Tohle mění pravidla hry.“ je slop.")
        self.assertEqual(r.findings, [])

    def test_code_block_masked(self):
        self.assertEqual(run((FIX / "code.md").read_text()).findings, [])

    def test_profile_filter(self):
        text = "Doufám, že se máte dobře."
        self.assertEqual(run(text, profile="post").findings, [])
        self.assertEqual(len(run(text, profile="email").findings), 1)
        self.assertEqual(len(run(text).findings), 1)

    def test_slovak_note(self):
        r = scan((FIX / "sk.md").read_text(), lang="auto", patterns=PATS)
        self.assertEqual(r.lang, "sk")
        self.assertIsNotNone(r.note)
        self.assertEqual(r.findings, [])

    def test_mixed_cz_en_no_crash(self):
        r = scan((FIX / "mixed.md").read_text(), lang="auto", patterns=PATS)
        self.assertIn(r.lang, ("cs", "en"))

    def test_cli_exit_codes(self):
        self.assertEqual(cli(str(FIX / "clean.md"), "--lang", "cs").returncode, 0)
        self.assertEqual(cli(str(FIX / "hit.md"), "--lang", "cs").returncode, 1)
        self.assertEqual(cli(str(FIX / "nope.md"), "--lang", "cs").returncode, 2)

    def test_json_output_schema(self):
        out = json.loads(cli(str(FIX / "hit.md"), "--lang", "cs", "--json").stdout)
        self.assertEqual(set(out), {"lang", "note", "words", "findings"})
        self.assertEqual(set(out["findings"][0]),
                         {"line", "col", "rule_id", "severity", "category", "match", "replacement"})


if __name__ == "__main__":
    unittest.main()
