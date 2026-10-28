"""Regressions from the Codex review (docs/internal oponentura, 2026-10-28)."""
import json
import unittest
from pathlib import Path

from detector import build
from detector.antislop import scan

ROOT = Path(__file__).resolve().parent.parent


def found(text, lang="cs", profile=None, sev=("zero", "rewrite")):
    return [f.rule_id for f in scan(text, lang, profile).findings if f.severity in sev]


class ReviewRegressions(unittest.TestCase):
    def test_as02_factual_contrast_not_zero(self):
        self.assertEqual(found("Otázkou není platnost smlouvy, ale okamžik jejího zániku.", sev=("zero",)), [])
        self.assertEqual(found("Nejde o daň z příjmu. Jde o DPH.", sev=("zero",)), [])

    def test_as03_legal_pairs_not_rewrite(self):
        self.assertEqual(found("Smlouvu podepsal nejen jednatel, ale i prokurista."), [])
        self.assertEqual(found("Není to daňový náklad, ale účetní položka."), [])

    def test_as04_factual_qa_not_fragment(self):
        self.assertEqual(found("Kdo návrh schválil? Představenstvo společnosti."), [])
        self.assertIn("x-question-fragment", found("Výsledek? Rychlejší práce."))

    def test_as05_arrow_in_table_ignored_and_not_zero(self):
        self.assertEqual(found("| Stav | Přechod |\n|---|---|\n| A | A → B |\n"), [])
        self.assertEqual(found("Model převádí stav A → stav B.", sev=("zero",)), [])

    def test_as08_history_and_science_not_flagged(self):
        self.assertEqual(found("Revoluce v roce 1848 zasáhla české země."), [])
        self.assertEqual(found("Vitamin K hraje zásadní roli při srážení krve."), [])
        self.assertEqual(found("Data říkají, že rozdíl není významný."), [])

    def test_as09_native_czech_not_calque(self):
        self.assertEqual(found("V konečném důsledku rozhodne soud.", sev=("zero", "rewrite", "watch")), [])
        self.assertEqual(found("Pomůžeme vám v rámci možností.", sev=("zero", "rewrite", "watch")), [])

    def test_as10_valid_english_not_calque(self):
        for t in ("It is necessary to note that the theorem assumes continuity.",
                  "I am sending you the signed contract.", "Concretely, we need two servers."):
            self.assertEqual(found(t, "en", sev=("zero", "rewrite", "watch")), [], t)

    def test_as06_en_portable_has_no_czech_in_common_block(self):
        text = build.render_portable("en")
        for cz in ("Je to rychlé", "Dlouhá pomlčka", "Nahraď číslem", "odrážek"):
            self.assertNotIn(cz, text)

    def test_as06_en_finding_messages_in_english(self):
        r = scan("- **A:** x\n- **B:** y\n- **C:** z\n", "en")
        self.assertTrue(r.findings)
        self.assertNotIn("odrážek", r.findings[0].match)

    def test_as12_vocab_examples_grammatical(self):
        for f in ("en", "cs"):
            for p in json.loads((ROOT / f"patterns/{f}.json").read_text()):
                if p["category"] == "vocabulary":
                    self.assertNotRegex(p["example_before"], r"^(This is a|Je to) \w+ (step|krok)\.$", p["id"])

    def test_as15_new_gaps_detected(self):
        self.assertIn("en-unsupported-authority", found("Studies show that remote teams are happier.", "en"))
        self.assertIn("cs-nepodlozena-autorita", found("Výzkumy ukazují, že lidé čtou méně."))
        self.assertIn("en-participle-tail", found("Sales rose 5 %, highlighting the strength of the brand.", "en"))
        self.assertIn("en-in-conclusion", found("In conclusion, the plan works.", "en"))


if __name__ == "__main__":
    unittest.main()
