"""
extract.py

Stage 1 of the factory. Turns raw source files into the atom library that every
downstream stage reads. This is what makes the source a real input: change the
source, the atoms change, and so does the output.

- No source given        -> the cached whitepaper atoms in sources.py.
- A source file or text   -> the heuristic extractor below (offline).
- live=True               -> route the raw text through the Extract prompt
                             (prompts.EXTRACT_SYSTEM) on a hosted model.

The heuristic extractor is intentionally simple so the demo needs no model. It
produces the same 8 atom keys the writers expect, so adapt.py does not care
where the atoms came from.
"""

import re
from .sources import ATOMS, SOURCE_MANIFEST


def extract(raw_text: str = None, source_path: str = None, live: bool = False) -> dict:
    if source_path:
        with open(source_path, "r", encoding="utf-8") as f:
            raw_text = f.read()
    if live and raw_text:
        # Production path: send raw_text + prompts.EXTRACT_SYSTEM to a model and
        # parse the JSON it returns. The demo uses the heuristic instead.
        raise NotImplementedError(
            "Live extraction routes through model.ClaudeClient in production."
        )
    if raw_text:
        return extract_from_text(raw_text)
    return ATOMS


def extract_from_text(text: str) -> dict:
    """Heuristic extraction. Genuinely text-driven: new input, new atoms."""
    t = re.sub(r"\s+", " ", text or "").strip()
    if len(t) < 40:
        return dict(ATOMS)
    sents = re.findall(r"[^.!?]+[.!?]+", t) or [t]
    sents = [s.strip() for s in sents]

    def find(pattern, min_len=0):
        rx = re.compile(pattern, re.I)
        for s in sents:
            if rx.search(s) and len(s) >= min_len:
                return s
        return ""

    def lower(s):
        return s[0].lower() + s[1:] if s else s

    def phrase(s, fallback):
        return re.sub(r"[.!?]+$", "", lower(s)) if s else fallback

    longest = max(sents, key=len) if sents else ""
    short = [s for s in sents if 20 < len(s) < 95]

    A = {
        # stat keeps its original case: it is always injected after a colon,
        # so a leading proper noun (e.g. "Club Furniture") must survive.
        "headline_stat": (re.sub(r"[.!?]+$", "", find(r"\d+\s*(%|percent|x\b)|\$\s?\d"))
                          or ATOMS["headline_stat"]),
        "betsey_story": (find(r"\b(we|our|they|after|customer|merchant)\b", 70) or longest
                         or ATOMS["betsey_story"]),
        "mechanism": phrase(find(r"\b(learn|model|adapt|AI|system|engine|feed|algorithm)\b"),
                            ATOMS["mechanism"]),
        "no_data": phrase(find(r"\b(without|no |any size|small|privacy|cookie|data|budget|GDPR|CCPA)\b"),
                          ATOMS["no_data"]),
        "few_interactions": phrase(find(r"\b(minute|hour|day|week|interaction|install|fast|quick|right away)\b"),
                                   ATOMS["few_interactions"]),
        "darpa": phrase(find(r"\b(research|founded|built|team|PhD|patent|backed|DARPA|trusted|years)\b"),
                        ATOMS["darpa"]),
        "conservative": phrase(find(r"\b(test|measure|average|study|result|proof|confirmed)\b"),
                               ATOMS["conservative"]),
        "speed_line": phrase(short[-1] if short else "", ATOMS["speed_line"]),
    }
    return A


def manifest() -> dict:
    return SOURCE_MANIFEST
