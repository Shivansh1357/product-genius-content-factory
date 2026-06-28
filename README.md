# Product Genius — Growth Marketing Engineer assessment

This repo is my submission for the Product Genius Growth Marketing Engineer challenge. It completes both tasks: the strategic design of an AI demand generation engine, and a working AI content factory built around it.

**▶ Live demo: https://content-factory-app-liart.vercel.app**

Open it, pick an account (start with ThirdLove), and click **Forge content**. Swap the source or paste your own, and the blog post, LinkedIn series, and email drip all regenerate, personalized to that buyer. No install, no key, nothing to host.

## The short version

Product Genius is a Shopify-native AI personalization feed that lifts revenue per session by roughly 20–36%. The buyer is whoever owns the conversion number. Five of the ten target accounts run on Shopify, which turns out to be the single most important fact for how to prioritize them: platform decides the speed of the deal, the size of the offer, and whether the motion is self-serve or sales-assisted.

The whole packet, including the generated marketing copy and the code comments, is written without em-dashes and the usual machine tells. The content factory enforces that with an automated cleanup stage (see `content-factory-pipeline/forge/qa.py`).

## What's in here

| Path | What it is |
| --- | --- |
| [`content-factory-app/`](content-factory-app/) | **The working product.** A single self-contained `index.html`. This is what's deployed at the link above. |
| [`content-factory-pipeline/`](content-factory-pipeline/) | The same engine as runnable Python, with a CLI, a built-in de-AI pass, and a one-class seam to swap in a live model. |
| [`sample-outputs/`](sample-outputs/) | Hand-polished reference outputs for two contrasting accounts (ThirdLove and Southern Baked Pie) so you can read the quality bar without running anything. |
| `0 - Start Here.docx` | The submission overview. |
| `Task 1 - Demand Generation Engine.docx` | The strategic system design: targeting, segmentation, channels, signals, personalization, the end-to-end workflow, and how it learns. |
| `Task 2 - AI Content Factory.docx` | The write-up of the content factory: how it works, why the personalization is real, how to measure it, and what to add next. |
| `Loom Walkthrough Script.docx` | A timed, section-by-section script for the video walkthrough. |

## Run the pipeline locally

No install needed — it works offline out of the box.

```bash
cd content-factory-pipeline
python run.py --list                      # show the 10 ICP accounts
python run.py --account thirdlove         # all three channels to stdout
python run.py --account thirdlove --source sample-sources/privacy-essay.txt
python run.py --all --out-dir examples    # generate all 10 at once
```

See [`content-factory-pipeline/README.md`](content-factory-pipeline/README.md) for the full engineering write-up.

## How to read it in five minutes

1. Open the [live demo](https://content-factory-app-liart.vercel.app), select ThirdLove, and click **Forge content**. That is Task 2 in motion.
2. Skim `Task 1` for the segmentation table. The Shopify vs. enterprise split is the core idea.
3. For the engineering, open `content-factory-pipeline/README.md` and run the one-line command above.
