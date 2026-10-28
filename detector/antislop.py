"""Antislop detector: finds slop patterns in Czech and English text.

Usage: python3 -m detector.antislop [FILE|-] [--lang auto|cs|en] [--profile P] [--json]
Exit: 0 = no zero/rewrite findings, 1 = some found, 2 = input error.
"""
import argparse
import json
import re
import sys
from dataclasses import asdict, dataclass, field
from pathlib import Path
from typing import List, Optional

from detector import text as T
from detector.patterns import PROFILES, REGEX_FLAGS, Pattern, PatternError, load_patterns, localized


@dataclass
class Finding:
    line: int
    col: int
    rule_id: str
    severity: str
    category: str
    match: str
    replacement: str


@dataclass
class ScanResult:
    lang: str
    note: Optional[str]
    words: int
    findings: List[Finding] = field(default_factory=list)


def _applies(p: Pattern, profile: Optional[str]) -> bool:
    return not p.profiles or profile is None or profile in p.profiles


def scan(text: str, lang: str = "auto", profile: Optional[str] = None,
         patterns: Optional[List[Pattern]] = None) -> ScanResult:
    text = T.normalize(text)
    detected = T.detect_lang(text) if lang == "auto" else lang
    note = "SK: kontrola českým modulem" if detected == "sk" else None
    rules_lang = "cs" if detected == "sk" else detected
    pats = patterns if patterns is not None else load_patterns(rules_lang)
    pats = [localized(p, rules_lang) for p in pats]
    masked = T.masked_spans(text)
    result = ScanResult(detected, note, len(T.words(text)))

    for p in pats:
        if not _applies(p, profile):
            continue
        if p.kind == "regex":
            if p.category == "vocabulary":
                continue  # reported only as density by x-excess-vocab
            for m in re.finditer(p.regex, text, REGEX_FLAGS):
                if T.is_masked(m.start(), masked):
                    continue
                line, col = T.line_col(text, m.start())
                result.findings.append(Finding(line, col, p.id, p.severity, p.category,
                                               m.group(0), p.replacement))
        else:
            from detector.heuristics import REGISTRY, ScanContext
            fn = REGISTRY.get(p.id)
            if fn:
                ctx = ScanContext(rules_lang, profile, result.words, masked, p, tuple(pats))
                result.findings.extend(fn(text, ctx))
    result.findings.sort(key=lambda f: (f.line, f.col, f.rule_id))
    return result


def _print_text(r: ScanResult) -> None:
    head = f"antislop: lang={r.lang}, words={r.words}, findings={len(r.findings)}"
    print(head + (f" ({r.note})" if r.note else ""))
    for f in r.findings:
        print(f'{f.line}:{f.col} [{f.severity}] {f.rule_id}: "{f.match}" → nahraď: {f.replacement}')


def main(argv: Optional[List[str]] = None) -> int:
    ap = argparse.ArgumentParser(prog="antislop", description=__doc__.splitlines()[0])
    ap.add_argument("file", nargs="?", default="-")
    ap.add_argument("--lang", default="auto", choices=("auto", "cs", "en"))
    ap.add_argument("--profile", choices=PROFILES)
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--patterns", help="explicit pattern file (testing)")
    a = ap.parse_args(argv)
    try:
        src = sys.stdin.read() if a.file == "-" else Path(a.file).read_text(encoding="utf-8")
        pats = load_patterns(a.lang, Path(a.patterns)) if a.patterns else None
        r = scan(src, a.lang, a.profile, pats)
    except (OSError, UnicodeDecodeError, PatternError) as e:
        print(f"antislop: {e}", file=sys.stderr)
        return 2
    if a.json:
        print(json.dumps(asdict(r), ensure_ascii=False, indent=1))
    else:
        _print_text(r)
    return 1 if any(f.severity in ("zero", "rewrite") for f in r.findings) else 0


if __name__ == "__main__":
    sys.exit(main())
