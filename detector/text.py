"""Text helpers: normalization, masked spans, language guess, sentences."""
import re
import unicodedata
from typing import List, Tuple

Span = Tuple[int, int]

_FENCE = re.compile(r"^```.*?^```[^\n]*$", re.M | re.S)
_INLINE = re.compile(r"`[^`\n]+`")
_QUOTES = re.compile(r"„[^“\n]{1,118}“|“[^”\n]{1,118}”|\"[^\"\n]{1,118}\"")

_SK_CHARS = re.compile(r"[äôĺľŕ]", re.I)
_SK_WORDS = re.compile(r"\b(sa|sú|nie je|ktorý|ktorá|preto|alebo)\b", re.I)
_CS_CHARS = re.compile(r"[ěščřžýáíéůú]", re.I)
_EN_WORDS = re.compile(r"\b(the|and|is|are|we|you|this|that|with|of|to)\b", re.I)

ABBREVIATIONS = ("např.", "tj.", "tzn.", "tzv.", "atd.", "apod.", "resp.", "př.", "sv.", "stol.",
                 "e.g.", "i.e.", "Mr.", "Mrs.", "Dr.", "vs.", "etc.", "č.", "str.", "pp.", "eds.")
_INITIAL = re.compile(r"(?:^|\s)\w\.$")  # single letter + dot: initials, "n. l."
_SENT_SPLIT = re.compile(r"(?<=[.!?…])\s+")
_WORD = re.compile(r"\w+(?:[-']\w+)*", re.U)


def normalize(text: str) -> str:
    text = unicodedata.normalize("NFC", text)
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    return text.replace("\u00a0", " ").replace("\u202f", " ")


def masked_spans(text: str) -> List[Span]:
    spans = [m.span() for m in _FENCE.finditer(text)]

    def inside(pos):
        return any(a <= pos < b for a, b in spans)

    spans += [m.span() for m in _INLINE.finditer(text) if not inside(m.start())]
    spans += [m.span() for m in _QUOTES.finditer(text) if not inside(m.start())]
    return sorted(spans)


def is_masked(pos: int, spans: List[Span]) -> bool:
    return any(a <= pos < b for a, b in spans)


def detect_lang(text: str) -> str:
    sk = len(_SK_CHARS.findall(text)) * 3 + len(_SK_WORDS.findall(text))
    cs = len(_CS_CHARS.findall(text))
    en = len(_EN_WORDS.findall(text))
    if sk >= 3 and sk * 2 >= cs // 4:
        return "sk"
    if cs == 0 or en > cs:
        return "en"
    return "cs"


def words(text: str) -> List[str]:
    return _WORD.findall(text)


def sentences(text: str) -> List[Tuple[int, str]]:
    """Split into (offset, sentence); keeps known abbreviations inside sentences."""
    out: List[Tuple[int, str]] = []
    start = 0
    for m in _SENT_SPLIT.finditer(text):
        chunk = text[start:m.start()]
        if any(chunk.endswith(a) for a in ABBREVIATIONS) or _INITIAL.search(chunk):
            continue
        if chunk.strip():
            out.append((start, chunk))
        start = m.end()
    if text[start:].strip():
        out.append((start, text[start:]))
    return out


def line_col(text: str, pos: int) -> Tuple[int, int]:
    line = text.count("\n", 0, pos) + 1
    col = pos - (text.rfind("\n", 0, pos) + 1) + 1
    return line, col
