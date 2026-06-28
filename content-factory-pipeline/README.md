# Forge: the Product Genius content factory

One source library in. Channel-ready, account-personalized assets out. Every
time you add new source material, you get a fresh batch of content without
rewriting anything.

This is the engine behind the web demo in `../content-factory-app`. Same logic,
same prompts, same de-AI guarantees. The web app is the operator's view, this is
the runnable, scriptable version.

## What it does

```
  source files                atom library            per-account drafts
  whitepaper.pdf   --extract-->  9 claims    --adapt-->  blog post
  founder-talk.mp4               7 stats        +        LinkedIn series (x3)
  stream.txt                     5 quotes    channelize  email drip (x4)
                                 4 angles    --qa----->  de-AI cleaned + flagged
```

Four stages, one seam for the model:

1. **Extract** (`extract.py`) turns raw source into a reusable atom library. Run
   once, reused across every account and channel. That reuse is what makes it a
   factory.
2. **Adapt** (`adapt.py`, `prompts.py`) rewrites the atoms for one decision-maker.
   Tone and offer are driven by the account's segment and platform, not chosen by
   hand.
3. **Channelize** turns the adapted angle into a blog post, a LinkedIn series, and
   an email drip, each with its own format rules.
4. **QA / de-AI** (`qa.py`) strips em-dashes and en-dashes, flags banned phrases
   ("delve", "leverage", "seamless", and friends), and checks for numbers that are
   not in the atom library. Nothing ships without passing through it.

## Run it

No install needed. It works offline out of the box.

```bash
python run.py --list                       # show the 10 ICP accounts
python run.py --account thirdlove          # all three channels to stdout
python run.py --account southern --channels blog,email
python run.py --account kohls --out kohls.md
python run.py --all --out-dir examples     # generate all 10 at once
```

## Change the source, change the output

The source is a real input, not a fixed string. Point `--source` at any text
file and the factory extracts fresh atoms from it, so the same account gets
different copy:

```bash
python run.py --account thirdlove --source sample-sources/privacy-essay.txt
python run.py --account thirdlove --source sample-sources/customer-story.txt
```

The privacy essay produces compliance-led copy, the customer story produces
testimonial-led copy, the default whitepaper produces the stats-led copy. Same
ten accounts, new input, new output. That is the whole point of a factory: feed
it new thinking and it keeps producing. The web app exposes the same thing
through preset sources and a paste-your-own box.

## Live model mode

```bash
pip install -r requirements.txt
export ANTHROPIC_API_KEY=sk-...
python run.py --account thirdlove --live
```

`--live` routes the exact prompts in `prompts.py` to a model via
`model.ClaudeClient`. The output still passes through the QA stage, so the style
guarantees hold whether the words came from a model or the offline generator.
Swapping providers (OpenAI, Gemini) is a one-class change in `model.py`.

## Why it is built this way

- **The atom library is the unit of reuse.** New input means re-run extract, and
  every downstream asset updates. You never rewrite the blog and the emails
  separately.
- **Personalization is structural, not cosmetic.** `personas.py` holds a real
  pain, hook, and trigger per account. Segment and platform deterministically set
  tone and offer, so a founder-led Shopify brand and a Kohl's CDO get genuinely
  different content from the same source.
- **The de-AI pass is part of the pipeline, not an afterthought.** That is how the
  factory can promise output that does not read like a default model wrote it.

## Files

```
run.py              CLI
forge/
  sources.py        cached atom library + per-category lift figures
  personas.py       the 10 ICP accounts with research signals
  prompts.py        the prompt templates (extract + per-channel + style rules)
  extract.py        stage 1
  adapt.py          stage 2 + 3 (deterministic offline writers)
  qa.py             stage 4 (de-AI pass)
  model.py          model abstraction (offline generator | Claude client)
  pipeline.py       orchestrator + Markdown renderer
```

## How you would measure it in production

The factory is the supply side. The demand side is tracked the same way Product
Genius tracks its own feed: per-asset, by channel, against revenue. Blog posts on
assisted pipeline and organic traffic, LinkedIn on reply and connection rate by
persona, email on reply rate and meetings booked, never opens. Winning angles get
promoted back into the atom library so the next run starts from what already
worked. The loop is the product.
