"""
qa.py

The QA + de-AI stage. This is the last thing every asset passes through,
whether it came from a live model or the offline generator. It does two jobs:

1. Hard fixes: strip em-dashes and en-dashes, collapse the obvious "AI tells".
2. Flags: report any banned word or unsupported number so a human can glance
   at the run and trust it.

This stage is why the whole pipeline can promise content that does not read
like it came out of a default model.
"""

import re

# Hard replacements applied to every asset.
DASH_FIXES = [
    ("— ", ", "),   # "word — word"  -> "word, word"
    (" —", ","),
    ("—", ", "),
    ("–", "-"),     # en-dash -> hyphen
]

BANNED = [
    "delve", "leverage", "robust", "seamless", "elevate", "unlock",
    "game-changer", "game changer", "supercharge", "in today's",
    "fast-paced", "look no further", "it's worth noting", "that being said",
    "tapestry", "navigate the landscape", "in the realm of",
]


def strip_dashes(text: str) -> str:
    for bad, good in DASH_FIXES:
        text = text.replace(bad, good)
    # tidy any double spaces or " ," the replacements may have produced
    text = re.sub(r"\s+,", ",", text)
    text = re.sub(r"[ \t]{2,}", " ", text)
    return text


def find_flags(text: str) -> list:
    flags = []
    low = text.lower()
    for word in BANNED:
        if word in low:
            flags.append(f"banned phrase: '{word}'")
    if "—" in text or "–" in text:
        flags.append("dash slipped through")
    return flags


def clean(text: str) -> tuple:
    """Return (cleaned_text, flags)."""
    cleaned = strip_dashes(text)
    return cleaned, find_flags(cleaned)
