"""
sources.py

The Extract stage turns raw source material (a whitepaper, a founder talk,
a stream-of-consciousness recording) into a reusable library of "atoms":
claims, stats, quotes, and narrative angles. Atoms are extracted once and
reused across every account and every channel, which is what makes this a
factory rather than a one-off copy job.

In production, extract.py calls a model to produce this structure from the
raw text. The dictionary below is the cached result of that call against the
Product Genius technical whitepaper, so the pipeline runs offline.
"""

# Per-category revenue-per-session lift, from the whitepaper test-results table.
CATEGORY_LIFT = {
    "Apparel": 34,
    "Jewelry": 33,
    "Specialty Foods": 26,
    "Furnishings": 25,
    "Specialty Retail": 25,
}

ATOMS = {
    "headline_stat": (
        "a 36 percent average lift in revenue per session across 25 brands "
        "and millions of sessions"
    ),
    "mechanism": (
        "an AI feed that adapts to each shopper as they scroll, learning from "
        "the live session instead of waiting for a trend to become "
        "statistically significant"
    ),
    "betsey_story": (
        "On a fast-moving fashion brand the lift would hold for a week and "
        "then vanish within hours, on its own, because shopper interest, "
        "competitor pricing, and new drops had moved faster than our "
        "statistics could confirm. The fix was to act before the data was "
        "conclusive."
    ),
    "speed_line": "you have to move faster than the speed of statistics",
    "no_data": (
        "It learns from the live visit, so it needs no third-party data and no "
        "long training period, and it works on stores doing as few as ten "
        "thousand sessions a month"
    ),
    "few_interactions": (
        "it picks up a useful signal in under a dozen interactions per shopper"
    ),
    "darpa": (
        "the learning system came out of roughly 35 million dollars of "
        "DARPA-funded research"
    ),
    "conservative": (
        "we averaged the lift across every day of the test, not just the "
        "strong days at the end, so the number is conservative"
    ),
}

# Metadata about the source, surfaced in the UI and logs.
SOURCE_MANIFEST = {
    "title": "Product Genius Technical Whitepaper + Founder Talk",
    "inputs": [
        "whitepaper.pdf",
        "founder-talk.mp4 (transcribed)",
        "stream-of-consciousness.txt",
    ],
    "atoms_extracted": {
        "claims": 9,
        "stats": 7,
        "quotes": 5,
        "angles": 4,
    },
}
