"""Schema and loader for antislop patterns (patterns/*.json)."""
import json
import re
from dataclasses import dataclass
from pathlib import Path
from typing import List, Optional, Tuple

ROOT = Path(__file__).resolve().parent.parent
PATTERN_DIR = ROOT / "patterns"

LANGS = ("cs", "en")
CATEGORIES = ("phrase", "construction", "punctuation", "emoji", "format",
              "calque", "rhythm", "vocabulary")
SEVERITIES = ("zero", "rewrite", "watch")
PROFILES = ("post", "email", "offer", "feedback")
KINDS = ("regex", "heuristic")
REGEX_FLAGS = re.I | re.U

_ID = re.compile(r"^(cs|en|x)-[a-z0-9-]+$")
_TEXT_FIELDS = ("why", "replacement", "example_before", "example_after", "source")


class PatternError(ValueError):
    pass


@dataclass(frozen=True)
class Pattern:
    id: str
    lang: str
    category: str
    kind: str
    regex: Optional[str]
    severity: str
    profiles: Tuple[str, ...]
    why: str
    replacement: str
    example_before: str
    example_after: str
    source: str
    en: Optional[dict] = None  # English why/replacement/examples for "x-" patterns


def localized(p: "Pattern", lang: str) -> "Pattern":
    """Return the pattern with English texts when lang is en and a translation exists."""
    if lang != "en" or not p.en:
        return p
    from dataclasses import replace
    return replace(p, **{k: v for k, v in p.en.items() if k in _TEXT_FIELDS[:4]})


def _validate(raw: dict) -> Pattern:
    pid = raw.get("id", "?")

    def fail(msg):
        raise PatternError(f"{pid}: {msg}")

    if not _ID.match(pid):
        fail("id must match (cs|en|x)-[a-z0-9-]+")
    if raw.get("lang") not in LANGS + ("x",) or raw["lang"] != pid.split("-")[0]:
        fail("lang must match the id prefix")
    if raw.get("category") not in CATEGORIES:
        fail(f"unknown category {raw.get('category')!r}")
    if raw.get("kind") not in KINDS:
        fail(f"unknown kind {raw.get('kind')!r}")
    if raw.get("severity") not in SEVERITIES:
        fail(f"unknown severity {raw.get('severity')!r}")
    profiles = tuple(raw.get("profiles") or ())
    for p in profiles:
        if p not in PROFILES:
            fail(f"unknown profile {p!r}")
    for f in _TEXT_FIELDS:
        if not str(raw.get(f) or "").strip():
            fail(f"missing {f}")
    for k in (raw.get("en") or {}):
        if k not in _TEXT_FIELDS[:4]:
            fail(f"unknown en field {k!r}")
    if raw["kind"] == "regex":
        if not raw.get("regex"):
            fail("regex pattern without regex")
        try:
            re.compile(raw["regex"], REGEX_FLAGS)
        except re.error as e:
            fail(f"bad regex: {e}")
    return Pattern(pid, raw["lang"], raw["category"], raw["kind"], raw.get("regex"),
                   raw["severity"], profiles, raw["why"], raw["replacement"],
                   raw["example_before"], raw["example_after"], raw["source"], raw.get("en"))


def _read(path: Path) -> list:
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as e:
        raise PatternError(f"{path.name}: invalid JSON: {e}")
    if not isinstance(data, list):
        raise PatternError(f"{path.name}: expected a list of patterns")
    return data


def load_patterns(lang: str, path: Optional[Path] = None) -> List[Pattern]:
    """Load patterns for `lang` (common + language file), or from one explicit file."""
    if path is not None:
        files = [Path(path)]
    else:
        files = [PATTERN_DIR / "common.json", PATTERN_DIR / f"{lang}.json"]
    out: List[Pattern] = []
    seen = set()
    for f in files:
        if not f.exists():
            continue
        for raw in _read(f):
            p = _validate(raw)
            if p.id in seen:
                raise PatternError(f"{p.id}: duplicate id")
            seen.add(p.id)
            out.append(p)
    return out
