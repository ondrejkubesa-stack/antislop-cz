import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILL = ROOT / "skills/antislop/SKILL.md"


class SkillTest(unittest.TestCase):
    def test_skill_frontmatter(self):
        text = SKILL.read_text()
        m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
        self.assertIsNotNone(m)
        front = m.group(1)
        self.assertRegex(front, r"(?m)^name: antislop$")
        desc = re.search(r"(?ms)^description: (.*?)(?=^\w+:|\Z)", front).group(1)
        self.assertLess(len(desc), 1024)
        for ref in ("rules/principy.md", "rules/postup.md", "rules/procedure-en.md", "detector.antislop"):
            self.assertIn(ref, text)
        for path in re.findall(r"`(rules/[\w/.-]+\.md)`", text):
            self.assertTrue((ROOT / path).exists(), path)


if __name__ == "__main__":
    unittest.main()
