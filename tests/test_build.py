import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from detector import build

ROOT = Path(__file__).resolve().parent.parent


class BuildTest(unittest.TestCase):
    def test_build_deterministic(self):
        for lang in ("cs", "en"):
            self.assertEqual(build.render_portable(lang), build.render_portable(lang))
            self.assertEqual(build.render_rules(lang), build.render_rules(lang))

    def test_check_detects_stale(self):
        with tempfile.TemporaryDirectory() as d:
            tmp = Path(d) / "repo"
            shutil.copytree(ROOT, tmp, ignore=shutil.ignore_patterns(".git", ".superpowers", "input", "monitor"))
            run = lambda *a: subprocess.run([sys.executable, "-m", "detector.build", *a], cwd=tmp,
                                            capture_output=True, text=True).returncode
            self.assertEqual(run(), 0)
            self.assertEqual(run("--check"), 0)
            p = tmp / "patterns/cs.json"
            p.write_text(p.read_text().replace("Vata na začátku.", "Vata na začátku textu.", 1))
            self.assertEqual(run("--check"), 1)

    def test_portable_under_limit(self):
        for lang in ("cs", "en"):
            self.assertLess(len(build.render_portable(lang)), 60000)

    def test_portable_has_no_generated_markers(self):
        for lang in ("cs", "en"):
            self.assertNotIn("<!-- generated", build.render_portable(lang))


if __name__ == "__main__":
    unittest.main()
