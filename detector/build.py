"""Generate pattern lists in rules/*.md and the portable files from patterns/*.json.

Usage: python3 -m detector.build [--check]   (--check exits 1 if a generated file is stale)
"""
import argparse
import re
import sys
from pathlib import Path
from typing import Dict, List

from detector.patterns import ROOT, Pattern, load_patterns, localized

RULES = ROOT / "rules"
PORTABLE = ROOT / "portable"

HEADINGS = {
    "cs": {"zero": "Nulová tolerance", "phrase": "Obraty", "construction": "Konstrukce",
           "calque": "Kalky", "vocabulary": "Slova, která vadí v hustotě",
           "punctuation": "Interpunkce", "emoji": "Emoji", "format": "Formátování",
           "rhythm": "Rytmus", "replace": "Náhrada", "example": "Lépe"},
    "en": {"zero": "Zero tolerance", "phrase": "Phrases", "construction": "Constructions",
           "calque": "Calques", "vocabulary": "Words that hurt in density",
           "punctuation": "Punctuation", "emoji": "Emoji", "format": "Formatting",
           "rhythm": "Rhythm", "replace": "Replace", "example": "Better"},
}
ORDER = ("construction", "phrase", "calque", "vocabulary", "punctuation", "emoji", "format", "rhythm")
_MARKER = re.compile(r"(<!-- generated:([\w-]+) -->\n).*?(<!-- /generated -->)", re.S)


def _item(p: Pattern, h: Dict[str, str], lang: str) -> str:
    q = ("„", "“") if lang == "cs" else ("“", "”")
    sev = "" if p.severity == "rewrite" else f" `{p.severity}`"
    return (f"- {q[0]}{p.example_before}{q[1]}{sev}: {p.why} {h['replace']}: {p.replacement} "
            f"{h['example']}: {q[0]}{p.example_after}{q[1]}")


def _section(pats: List[Pattern], lang: str, categories) -> str:
    h = HEADINGS[lang]
    out = []
    for cat in ORDER:
        if cat not in categories:
            continue
        items = [p for p in pats if p.category == cat]
        if not items:
            continue
        out.append(f"### {h[cat]}\n")
        out += [_item(p, h, lang) for p in sorted(items, key=lambda p: (p.severity != "zero", p.id))]
        out.append("")
    return "\n".join(out).rstrip() + "\n"


def _lang_patterns(lang: str) -> List[Pattern]:
    return [p for p in load_patterns(lang) if p.lang == lang]


def render_rules(lang: str) -> str:
    """Phrase/construction/vocabulary list for rules/<lang>.md (calques live in kalky.md)."""
    cats = [c for c in ORDER if c != "calque"]
    return _section(_lang_patterns(lang), lang, cats)


def render_calques(lang: str) -> str:
    return _section(_lang_patterns(lang), lang, ["calque"])


def render_common(lang: str) -> str:
    pats = [localized(p, lang) for p in load_patterns(lang) if p.lang == "x"]
    return _section(pats, lang, ORDER)


def _strip_markers(text: str) -> str:
    return re.sub(r"<!-- /?generated[^>]*-->\n?", "", text)


def _read(name: str) -> str:
    return (RULES / name).read_text(encoding="utf-8").strip() + "\n"


def render_portable(lang: str) -> str:
    if lang == "cs":
        parts = ["# Antislop (čeština)\n\nVlož tento soubor do instrukcí projektu (ChatGPT, claude.ai) "
                 "a požádej o kontrolu textu. Zdroj: plugin antislop, licence MIT.\n",
                 _read("principy.md"), _read("postup.md"),
                 "## Strukturní a interpunkční vzory\n\n" + render_common(lang),
                 _strip_markers(_fill(_read("cs.md"))), _strip_markers(_fill(_read("kalky.md")))]
        for prof in ("post", "email", "offer", "feedback"):
            parts.append(_read(f"profily/{prof}.md"))
    else:
        parts = ["# Antislop (English)\n\nPaste this file into your project instructions (ChatGPT, claude.ai) "
                 "and ask for a review of your text. Source: antislop plugin, MIT licence.\n",
                 _read("principles-en.md"), _read("procedure-en.md"),
                 "## Structure and punctuation patterns\n\n" + render_common(lang),
                 _strip_markers(_fill(_read("en.md"))),
                 "## Calques from Czech\n\n" + render_calques("en")]
    text = "\n".join(p.rstrip() + "\n" for p in parts)
    text = re.sub(r"^(#+) ", r"#\1 ", text, flags=re.M)
    return text.replace("## Antislop (", "# Antislop (", 1)


GENERATORS = {
    "patterns-cs": lambda: render_rules("cs"),
    "patterns-en": lambda: render_rules("en"),
    "calques-cs": lambda: render_calques("cs"),
    "calques-en": lambda: render_calques("en"),
}


def _fill(text: str) -> str:
    return _MARKER.sub(lambda m: m.group(1) + GENERATORS[m.group(2)]() + m.group(3), text)


def targets() -> Dict[Path, str]:
    out = {}
    for name in ("cs.md", "en.md", "kalky.md"):
        out[RULES / name] = _fill((RULES / name).read_text(encoding="utf-8"))
    out[PORTABLE / "antislop-cs.md"] = render_portable("cs")
    out[PORTABLE / "antislop-en.md"] = render_portable("en")
    return out


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(prog="antislop-build")
    ap.add_argument("--check", action="store_true")
    a = ap.parse_args(argv)
    stale = []
    for path, content in targets().items():
        current = path.read_text(encoding="utf-8") if path.exists() else None
        if current == content:
            continue
        if a.check:
            stale.append(path.relative_to(ROOT))
        else:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(content, encoding="utf-8")
            print(f"wrote {path.relative_to(ROOT)}")
    if stale:
        print("stale: " + ", ".join(map(str, stale)), file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
