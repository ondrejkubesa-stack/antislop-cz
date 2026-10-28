"""Measure findings per 1000 words on a corpus of human-written texts.

Usage: python3 -m detector.calibrate --lang cs FILE...
"""
import argparse
import json
import sys
from collections import Counter
from pathlib import Path
from typing import Dict, List

from detector.antislop import scan


def calibrate(paths: List[Path], lang: str) -> Dict:
    words = 0
    sev: Counter = Counter()
    rules: Counter = Counter()
    for p in paths:
        r = scan(Path(p).read_text(encoding="utf-8"), lang)
        words += r.words
        for f in r.findings:
            sev[f.severity] += 1
            rules[f.rule_id] += 1
    per = {s: (sev[s] * 1000 / words if words else 0.0) for s in ("zero", "rewrite", "watch")}
    return {"files": len(paths), "words": words, "per_1000": per, "by_rule": dict(rules.most_common())}


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(prog="antislop-calibrate")
    ap.add_argument("--lang", required=True, choices=("cs", "en"))
    ap.add_argument("files", nargs="+")
    a = ap.parse_args(argv)
    print(json.dumps(calibrate([Path(f) for f in a.files], a.lang), ensure_ascii=False, indent=1))
    return 0


if __name__ == "__main__":
    sys.exit(main())
