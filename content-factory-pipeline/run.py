#!/usr/bin/env python3
"""
run.py: command-line entry point for the Forge content factory.

Examples:
    python run.py --account thirdlove
    python run.py --account southern --channels blog,email
    python run.py --account kohls --out kohls.md
    python run.py --list
    python run.py --all --out-dir examples

By default it runs offline (the deterministic generator), so no API key is
needed. Pass --live with ANTHROPIC_API_KEY set to route the same prompts to
a model.
"""

import argparse
import os
import sys

from forge import pipeline
from forge.personas import ACCOUNTS


def main():
    p = argparse.ArgumentParser(description="Forge: Product Genius content factory")
    p.add_argument("--account", help="account id (see --list)")
    p.add_argument("--channels", default="blog,linkedin,email",
                   help="comma list of: blog, linkedin, email")
    p.add_argument("--source",
                   help="path to a source text file to extract atoms from "
                        "(default: the cached whitepaper atoms). Try the files in sample-sources/")
    p.add_argument("--live", action="store_true",
                   help="use a hosted model (needs ANTHROPIC_API_KEY)")
    p.add_argument("--out", help="write Markdown to this file instead of stdout")
    p.add_argument("--out-dir", help="with --all, write one file per account here")
    p.add_argument("--all", action="store_true", help="run every account")
    p.add_argument("--list", action="store_true", help="list known accounts")
    args = p.parse_args()

    if args.list:
        print("Known accounts:\n")
        for acc in ACCOUNTS.values():
            print(f"  {acc.id:<12} {acc.name:<22} {acc.segment:<12} "
                  f"{'Shopify' if acc.shopify else acc.platform}")
        return

    channels = tuple(c.strip() for c in args.channels.split(",") if c.strip())

    if args.all:
        out_dir = args.out_dir or "examples"
        os.makedirs(out_dir, exist_ok=True)
        for acc in ACCOUNTS:
            result = pipeline.run(acc, channels=channels, live=args.live, source=args.source)
            md = pipeline.render_markdown(result)
            path = os.path.join(out_dir, f"{acc}.md")
            with open(path, "w") as f:
                f.write(md)
            flag = " (flags!)" if result["flags"] else ""
            print(f"wrote {path}{flag}")
        return

    if not args.account:
        p.error("give --account ID, or --all, or --list")

    result = pipeline.run(args.account, channels=channels, live=args.live, source=args.source)
    md = pipeline.render_markdown(result)

    if args.out:
        with open(args.out, "w") as f:
            f.write(md)
        print(f"wrote {args.out}")
    else:
        print(md)

    if result["flags"]:
        print("\n[!] QA flags raised, see the QA section above", file=sys.stderr)


if __name__ == "__main__":
    main()
