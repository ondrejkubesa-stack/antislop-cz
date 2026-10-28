import tempfile
import unittest
from pathlib import Path

from detector.calibrate import calibrate


class CalibrateTest(unittest.TestCase):
    def test_calibrate_counts(self):
        with tempfile.TemporaryDirectory() as d:
            a = Path(d) / "a.md"
            b = Path(d) / "b.md"
            a.write_text("Je to rychlé — a levné. " + "slovo " * 98)
            b.write_text("Faktura odejde zítra. " + "slovo " * 97)
            r = calibrate([a, b], "cs")
            self.assertEqual(r["words"], 203)
            self.assertAlmostEqual(r["per_1000"]["zero"], 1000 / 203, places=3)
            self.assertEqual(r["by_rule"]["x-em-dash"], 1)


if __name__ == "__main__":
    unittest.main()
