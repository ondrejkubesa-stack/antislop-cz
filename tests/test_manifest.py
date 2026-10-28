import json
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


class ManifestTest(unittest.TestCase):
    def test_manifest_valid(self):
        plugin = json.loads((ROOT / ".claude-plugin/plugin.json").read_text())
        market = json.loads((ROOT / ".claude-plugin/marketplace.json").read_text())
        self.assertEqual(plugin["name"], "antislop-cz")
        self.assertRegex(plugin["version"], r"^\d+\.\d+\.\d+$")
        self.assertEqual(market["plugins"][0]["name"], "antislop-cz")


if __name__ == "__main__":
    unittest.main()
