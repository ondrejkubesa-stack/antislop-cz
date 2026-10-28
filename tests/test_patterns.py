import json
import tempfile
import unittest
from pathlib import Path

from detector.patterns import Pattern, PatternError, load_patterns

FIX = Path(__file__).resolve().parent / "fixtures"


def bad_case(name):
    cases = json.loads((FIX / "patterns_bad.json").read_text())
    tmp = tempfile.NamedTemporaryFile("w", suffix=".json", delete=False)
    json.dump(cases[name], tmp, ensure_ascii=False)
    tmp.close()
    return Path(tmp.name)


class PatternsTest(unittest.TestCase):
    def test_load_valid(self):
        pats = load_patterns("cs", FIX / "patterns_valid.json")
        self.assertEqual(len(pats), 2)
        self.assertIsInstance(pats[0], Pattern)
        self.assertEqual(pats[0].profiles, ())

    def test_missing_replacement_raises(self):
        with self.assertRaisesRegex(PatternError, "cs-test-doba"):
            load_patterns("cs", bad_case("missing_replacement"))

    def test_bad_regex_raises(self):
        with self.assertRaisesRegex(PatternError, "cs-test-doba"):
            load_patterns("cs", bad_case("bad_regex"))

    def test_duplicate_id_raises(self):
        with self.assertRaisesRegex(PatternError, "cs-test-doba"):
            load_patterns("cs", bad_case("duplicate_id"))

    def test_unknown_severity_raises(self):
        with self.assertRaisesRegex(PatternError, "cs-test-doba"):
            load_patterns("cs", bad_case("unknown_severity"))


if __name__ == "__main__":
    unittest.main()
