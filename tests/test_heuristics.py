import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from detector.antislop import scan
from detector.patterns import Pattern

ROOT = Path(__file__).resolve().parent.parent


def P(pid, severity="rewrite", category="format", kind="heuristic", regex=None, lang=None):
    return Pattern(pid, lang or pid.split("-")[0], category, kind, regex, severity, (),
                   "why", "replacement", "before", "after", "praxe")


def ids(text, pats, lang="cs", profile=None):
    return [f.rule_id for f in scan(text, lang, profile, pats).findings]


def sev(text, pats, lang="cs", profile=None):
    return [f.severity for f in scan(text, lang, profile, pats).findings]


LONG_FLAT = " ".join(["Tohle je věta o deseti slovech, která má stejnou délku."] * 20)


class HeuristicsTest(unittest.TestCase):
    def test_em_dash_hit(self):
        self.assertEqual(ids("Je to rychlé — a levné. Taky – takhle.", [P("x-em-dash", "zero")]),
                         ["x-em-dash", "x-em-dash"])

    def test_spaced_en_dash_is_watch(self):
        self.assertEqual(sev("Je to rychlé — a levné. Taky – takhle.", [P("x-em-dash", "zero")]),
                         ["zero", "watch"])

    def test_footnotes_not_staccato(self):
        pats = [P("x-staccato", category="rhythm")]
        text = "[^1]: Novák, J. 2001.\n[^2]: Dvořák, K. 2003.\n[^3]: Svoboda, L. 2005.\n"
        self.assertEqual(ids(text, pats), [])

    def test_abbreviations_not_staccato(self):
        pats = [P("x-staccato", category="rhythm")]
        text = "Okolo roku 3000 př. n. l. se pilo pivo. Napsal to J. A. Komenský v roce 1631 v Lešně."
        self.assertEqual(ids(text, pats), [])

    def test_number_range_not_dash(self):
        self.assertEqual(ids("Trvá to 5–10 minut, strany 3–4.", [P("x-em-dash", "zero")]), [])

    def test_em_dash_in_code_masked(self):
        self.assertEqual(ids("Příkaz `a — b` a\n```\nx — y\n```\n", [P("x-em-dash", "zero")]), [])

    def test_arrow_hit(self):
        self.assertEqual(len(ids("Vstup → výstup. A -> B. C => D. E ⟶ F.", [P("x-arrow", "zero")])), 4)

    def test_arrow_in_code_masked(self):
        self.assertEqual(ids("Použij `a -> b`.", [P("x-arrow", "zero")]), [])

    def test_emoji_hit_and_email_watch(self):
        pats = [P("x-emoji", "zero", "emoji")]
        self.assertEqual(sev("Hotovo 🚀 díky.", pats), ["zero"])
        self.assertEqual(sev("Hotovo 🚀 díky.", pats, profile="email"), ["watch"])

    def test_no_emoji_in_plain(self):
        self.assertEqual(ids("Cena je 100 Kč, © 2026.", [P("x-emoji", "zero", "emoji")]), [])

    def test_question_fragment_hit(self):
        pats = [P("x-question-fragment", category="construction")]
        self.assertEqual(ids("Pohodlné? Rozhodně. Výsledek? Rychlejší práce.", pats),
                         ["x-question-fragment", "x-question-fragment"])

    def test_proc_protoze_allowed(self):
        pats = [P("x-question-fragment", category="construction")]
        self.assertEqual(ids("Proč? Protože se to vyplatí.", pats), [])

    def test_long_question_not_fragment(self):
        pats = [P("x-question-fragment", category="construction")]
        self.assertEqual(ids("Kolik nás stojí jedna hodina výpadku serveru? Zhruba dvacet tisíc.", pats), [])

    def test_staccato_three(self):
        pats = [P("x-staccato", category="rhythm")]
        self.assertEqual(ids("Je to rychlé. Je to levné. Funguje to hned.", pats), ["x-staccato"])

    def test_staccato_two_ok(self):
        pats = [P("x-staccato", category="rhythm")]
        text = "Je to rychlé. Je to levné. Nasazení do provozu ale zabralo celý týden a dva lidi navíc."
        self.assertEqual(ids(text, pats), [])

    def test_staccato_ignores_bullets(self):
        pats = [P("x-staccato", category="rhythm")]
        self.assertEqual(ids("- Rychlé.\n- Levné.\n- Hned.\n", pats), [])

    def test_bold_lead_bullets(self):
        pats = [P("x-bold-lead-bullets")]
        text = "- **Rychlost:** a\n- **Cena:** b\n- **Podpora:** c\n"
        self.assertEqual(ids(text, pats), ["x-bold-lead-bullets"])
        self.assertEqual(ids("- **Rychlost:** a\n- Cena b\n", pats), [])

    def test_bold_density(self):
        pats = [P("x-bold-density", "watch")]
        dense = " ".join(["Slovo **tučně** a dalších šest slov tady je."] * 20)
        self.assertEqual(ids(dense, pats), ["x-bold-density"])
        self.assertEqual(ids(LONG_FLAT, pats), [])

    def test_title_case_heading(self):
        pats = [P("x-title-case-heading")]
        self.assertEqual(sev("# Jak Napsat Dobrý Text\n", pats, "cs"), ["rewrite"])
        self.assertEqual(sev("# How To Write Good Text\n", pats, "en"), ["watch"])
        self.assertEqual(ids("# Jak napsat dobrý text\n", pats), [])

    def test_title_case_ignores_parenthesized_names(self):
        pats = [P("x-title-case-heading")]
        self.assertEqual(ids("## Instalace (Claude Code)\n", pats), [])
        self.assertEqual(ids("## Install (Claude Code)\n", pats, "en"), [])

    def test_title_case_skips_caps_names_and_links(self):
        pats = [P("x-title-case-heading")]
        for h in ("## V TENTO DEN...", "## Workshop s Martinem Klusoněm",
                  "## Revize Accountů [[@Jan Novák]]", "## Meeting with John Smith"):
            self.assertEqual(ids(h + "\n", pats), [], h)

    def test_rhythm_flat(self):
        pats = [P("x-rhythm-flat", "watch", "rhythm")]
        self.assertEqual(ids(LONG_FLAT, pats), ["x-rhythm-flat"])

    def test_short_text_no_stats(self):
        pats = [P("x-rhythm-flat", "watch", "rhythm")]
        short = " ".join(["Tohle je věta o deseti slovech, která má stejnou délku."] * 12)
        self.assertEqual(ids(short, pats), [])

    def test_vocab_density(self):
        vocab = P("en-v-delve", "watch", "vocabulary", "regex", r"\bdelv(e|es|ing)\b")
        pats = [vocab, P("x-excess-vocab", "watch", "vocabulary")]
        filler = " ".join(["We ship the release on Monday and fix bugs."] * 30)
        self.assertEqual(ids("We delve into it. " + filler, pats, "en"), [])
        many = "We delve. They delve. Delving again. " + filler
        self.assertEqual(ids(many, pats, "en"), ["x-excess-vocab"] * 3)

    def test_unicode_variants_equal(self):
        dash, arrow = [P("x-em-dash", "zero")], [P("x-arrow", "zero")]
        self.assertEqual(len(ids("A — b, c – d.", dash)), len(ids("A – b, c — d.", dash)))
        self.assertEqual(len(ids("A → b.", arrow)), len(ids("A -> b.", arrow)))

    def test_crlf_same_as_lf(self):
        pats = [P("x-staccato", category="rhythm"), P("x-em-dash", "zero")]
        lf = "Je to rychlé. Je to levné. Funguje to hned.\nA — b.\n"
        self.assertEqual(ids(lf, pats), ids(lf.replace("\n", "\r\n"), pats))

    def test_empty_input(self):
        self.assertEqual(ids("", [P("x-em-dash", "zero"), P("x-rhythm-flat", "watch", "rhythm")]), [])
        with tempfile.NamedTemporaryFile("w", suffix=".md", delete=False) as f:
            pass
        r = subprocess.run([sys.executable, "-m", "detector.antislop", f.name, "--lang", "cs",
                            "--patterns", str(ROOT / "tests/fixtures/scan/patterns_cs.json")],
                           cwd=ROOT, capture_output=True, text=True)
        self.assertEqual(r.returncode, 0)


if __name__ == "__main__":
    unittest.main()
