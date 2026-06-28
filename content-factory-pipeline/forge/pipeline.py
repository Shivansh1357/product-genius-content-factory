"""
pipeline.py

The orchestrator. Wires the four stages together:

    Extract  ->  Adapt + Channelize  ->  QA / de-AI

and renders the result to Markdown. Every text asset, regardless of whether it
came from the offline generator or a live model, passes through qa.clean(), so
the no-em-dash and no-banned-word guarantees hold for the whole system.
"""

from . import extract, qa
from .model import get_client
from .sources import CATEGORY_LIFT
from .personas import get


def run(account_id: str, channels=("blog", "linkedin", "email"), live=False, source=None) -> dict:
    account = get(account_id)
    atoms = extract.extract(source_path=source, live=live)
    client = get_client(live)
    lift = CATEGORY_LIFT[account.lift_category]

    assets = {}
    all_flags = {}
    for channel in channels:
        asset = client.generate(channel, account, lift, atoms)
        asset, flags = _qa_asset(asset)
        assets[channel] = asset
        if flags:
            all_flags[channel] = flags

    return {
        "account": account,
        "engine": client.name,
        "lift": lift,
        "assets": assets,
        "flags": all_flags,
        "source": source or "cached whitepaper atoms",
    }


def _qa_asset(asset: dict) -> tuple:
    """Run the de-AI pass over whichever text fields an asset carries."""
    flags = []

    def scrub(text):
        cleaned, f = qa.clean(text)
        flags.extend(f)
        return cleaned

    if asset["type"] == "blog":
        asset["title"] = scrub(asset["title"])
        asset["paragraphs"] = [scrub(p) for p in asset["paragraphs"]]
    elif asset["type"] == "linkedin":
        for post in asset["posts"]:
            post["text"] = scrub(post["text"])
    elif asset["type"] == "email":
        for mail in asset["emails"]:
            mail["subject"] = scrub(mail["subject"])
            mail["body"] = scrub(mail["body"])
    return asset, flags


# ---------------------------------------------------------------- rendering

def render_markdown(result: dict) -> str:
    a = result["account"]
    out = []
    out.append(f"# Forge output: {a.name}")
    out.append(
        f"_Target: {a.persona_name}, {a.persona_title}. Segment: {a.segment}. "
        f"Platform: {a.platform}. Engine: {result['engine']}. "
        f"Source: {result['source']}. Category lift used: {result['lift']}%._\n"
    )

    if "blog" in result["assets"]:
        b = result["assets"]["blog"]
        out.append("## Blog post\n")
        out.append(f"### {b['title']}\n")
        out.extend(p + "\n" for p in b["paragraphs"])

    if "linkedin" in result["assets"]:
        out.append("## LinkedIn series\n")
        for i, post in enumerate(result["assets"]["linkedin"]["posts"], 1):
            out.append(f"**Post {i} ({post['voice']})**\n")
            out.append(post["text"] + "\n")

    if "email" in result["assets"]:
        out.append("## Email drip\n")
        for mail in result["assets"]["email"]["emails"]:
            out.append(f"**{mail['day']} | Subject: {mail['subject']}**\n")
            out.append(mail["body"] + "\n")

    if result["flags"]:
        out.append("## QA flags\n")
        for ch, flags in result["flags"].items():
            out.append(f"- {ch}: {', '.join(flags)}")
    else:
        out.append("_QA: clean. No em-dashes, no banned phrases, no unsupported numbers._")

    return "\n".join(out)
