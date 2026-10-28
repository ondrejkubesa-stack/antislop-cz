"""Structural heuristics. Each takes (text, ScanContext) and returns findings.

A heuristic runs only when a pattern with its id is loaded, so data can switch it off.
"""
import re
import statistics
import unicodedata
from dataclasses import dataclass
from typing import Callable, Dict, List, Optional, Tuple

from detector import text as T
from detector.patterns import REGEX_FLAGS, Pattern

MIN_WORDS_STATS = 150


@dataclass
class ScanContext:
    lang: str
    profile: Optional[str]
    words: int
    masked: List[T.Span]
    pattern: Pattern
    patterns: Tuple[Pattern, ...] = ()


def _finding(text, pos, match, ctx, severity=None, replacement=None):
    from detector.antislop import Finding
    line, col = T.line_col(text, pos)
    p = ctx.pattern
    return Finding(line, col, p.id, severity or p.severity, p.category, match,
                   replacement or p.replacement)


def _regex_hits(rx, text, ctx, **kw):
    return [_finding(text, m.start(), m.group(0).strip(), ctx, **kw)
            for m in rx.finditer(text) if not T.is_masked(m.start(), ctx.masked)]


_EM_DASH = re.compile(r"—")
_SPACED_EN_DASH = re.compile(r"(?<=\s)–(?=\s)")
_ARROW = re.compile(r"[→⟶➜➔➝⇒]|->|=>")


def em_dash(text, ctx):
    # spaced en dash is correct Czech typography (and British usage): only a warning
    return _regex_hits(_EM_DASH, text, ctx) + _regex_hits(_SPACED_EN_DASH, text, ctx, severity="watch")


_TABLE_LINE = re.compile(r"^\s*\|.*$", re.M)
_LINE_START_ARROW = re.compile(r"^\s*(?:[-*+]\s+)?$")


def arrow(text, ctx):
    """Arrows in prose are rewrite; arrows used as bullets are zero; tables are skipped."""
    tables = [m.span() for m in _TABLE_LINE.finditer(text)]
    hits = []
    for m in _ARROW.finditer(text):
        if T.is_masked(m.start(), ctx.masked) or T.is_masked(m.start(), tables):
            continue
        line_start = text.rfind("\n", 0, m.start()) + 1
        bullet = bool(_LINE_START_ARROW.match(text[line_start:m.start()]))
        hits.append(_finding(text, m.start(), m.group(0), ctx, severity="zero" if bullet else None))
    return hits


def _is_emoji(ch):
    cp = ord(ch)
    return unicodedata.category(ch) == "So" and (cp >= 0x1F000 or 0x2600 <= cp <= 0x27BF)


def emoji(text, ctx):
    sev = "watch" if ctx.profile == "email" else None
    return [_finding(text, i, ch, ctx, severity=sev) for i, ch in enumerate(text)
            if _is_emoji(ch) and not T.is_masked(i, ctx.masked)]


_STRUCT_LINE = re.compile(r"^\s*(#|[-*+]\s|\d+[.)]\s|>|\||\[\^)")
_ALLOWED_ANSWER = re.compile(r"^(protože|because|páč|neboť)\b", re.I)
_INTERROGATIVE = re.compile(r"^(kdo|co|kdy|kde|kam|odkud|jak|jaký|jaká|jaké|kolik|který|která|které|čí|proč|"
                            r"who|what|when|where|which|whose|how|why|is|are|do|does|did|can|will)\b", re.I)


def _prose_paragraphs(text):
    """(offset, paragraph) for prose paragraphs; headings, lists, tables and code are skipped."""
    out, pos = [], 0
    for block in re.split(r"(\n\s*\n)", text):
        lines = [l for l in block.split("\n") if l.strip()]
        if lines and not any(_STRUCT_LINE.match(l) for l in lines) and not block.lstrip().startswith("```"):
            out.append((pos, block))
        pos += len(block)
    return out


def question_fragment(text, ctx):
    hits = []
    for off, para in _prose_paragraphs(text):
        sents = T.sentences(para)
        for (o1, q), (o2, a) in zip(sents, sents[1:]):
            # rhetorical teaser ("Výsledek? …") is 1-2 words and not a real question word
            if q.rstrip().endswith("?") and len(T.words(q)) <= 2 and len(T.words(a)) <= 5 \
                    and not _INTERROGATIVE.match(q.strip()) \
                    and not _ALLOWED_ANSWER.match(a.strip()) and not a.rstrip().endswith("?"):
                pos = off + o1
                if not T.is_masked(pos, ctx.masked):
                    hits.append(_finding(text, pos, f"{q.strip()} {a.strip()}", ctx))
    return hits


def staccato(text, ctx):
    hits = []
    for off, para in _prose_paragraphs(text):
        run = []
        for o, s in T.sentences(para) + [(None, "")]:
            n = len(T.words(s))
            if o is not None and 0 < n <= 7:
                run.append((o, s))
                continue
            if len(run) >= 3:
                pos = off + run[0][0]
                hits.append(_finding(text, pos, " ".join(x[1].strip() for x in run), ctx))
            run = []
    return hits


_BOLD_LEAD = re.compile(r"^\s*([-*+]|\d+[.)])\s+\*\*[^*\n]+\*\*", re.M)
_BOLD = re.compile(r"\*\*[^*\n]+\*\*|__[^_\n]+__")


def bold_lead_bullets(text, ctx):
    ms = [m for m in _BOLD_LEAD.finditer(text) if not T.is_masked(m.start(), ctx.masked)]
    if len(ms) < 3:
        return []
    msg = f"{len(ms)} bullets open with bold" if ctx.lang == "en" else f"{len(ms)} odrážek začíná tučně"
    return [_finding(text, ms[0].start(), msg, ctx)]


def bold_density(text, ctx):
    if ctx.words < MIN_WORDS_STATS:
        return []
    ms = [m for m in _BOLD.finditer(text) if not T.is_masked(m.start(), ctx.masked)]
    if len(ms) * 80 <= ctx.words:
        return []
    msg = (f"{len(ms)} bold spans in {ctx.words} words" if ctx.lang == "en"
           else f"{len(ms)} tučných úseků na {ctx.words} slov")
    return [_finding(text, ms[0].start(), msg, ctx)]


_HEADING = re.compile(r"^#{1,6}\s+(.+)$", re.M)


def title_case_heading(text, ctx):
    sev = "watch" if ctx.lang == "en" else "rewrite"
    hits = []
    for m in _HEADING.finditer(text):
        # skip the first word, parentheses and wiki links (names); ALL CAPS is not title case;
        # require 3+ capitalized longer words so a heading with a person's name passes
        head = re.sub(r"\([^)]*\)|\[\[[^\]]*\]\]", "", m.group(1))
        if T.is_masked(m.start(), ctx.masked) or head.upper() == head:
            continue
        ws = [w for w in T.words(head)[1:] if w[0].isalpha() and len(w) > 3]
        caps = sum(1 for w in ws if w[0].isupper())
        if caps >= 3 and caps / len(ws) >= 0.75:
            hits.append(_finding(text, m.start(1), m.group(1).strip(), ctx, severity=sev))
    return hits


def rhythm_flat(text, ctx):
    if ctx.words < MIN_WORDS_STATS:
        return []
    lens = [len(T.words(s)) for _, para in _prose_paragraphs(text) for _, s in T.sentences(para)]
    lens = [n for n in lens if n]
    if len(lens) < 5:
        return []
    cv = statistics.pstdev(lens) / statistics.mean(lens)
    if cv >= 0.35 or max(lens) > 25:
        return []
    msg = (f"sentence length variation {cv:.2f}, longest sentence {max(lens)} words" if ctx.lang == "en"
           else f"rozptyl délky vět {cv:.2f}, nejdelší věta {max(lens)} slov")
    return [_finding(text, 0, msg, ctx)]


def excess_vocab(text, ctx):
    if ctx.words < MIN_WORDS_STATS:
        return []
    hits = []
    for p in ctx.patterns:
        if p.category == "vocabulary" and p.kind == "regex":
            for m in re.finditer(p.regex, text, REGEX_FLAGS):
                if not T.is_masked(m.start(), ctx.masked):
                    hits.append(_finding(text, m.start(), m.group(0), ctx, replacement=p.replacement))
    if len(hits) < 2 or len(hits) * 1000 <= 3 * ctx.words:
        return []
    return hits


REGISTRY: Dict[str, Callable[[str, ScanContext], list]] = {
    "x-em-dash": em_dash,
    "x-arrow": arrow,
    "x-emoji": emoji,
    "x-question-fragment": question_fragment,
    "x-staccato": staccato,
    "x-bold-lead-bullets": bold_lead_bullets,
    "x-bold-density": bold_density,
    "x-title-case-heading": title_case_heading,
    "x-rhythm-flat": rhythm_flat,
    "x-excess-vocab": excess_vocab,
}
