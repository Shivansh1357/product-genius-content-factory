"""
model.py

A thin model-client abstraction. The pipeline calls generate(prompt, ...) and
does not care whether the text came from a hosted model or the offline
generator. That single seam is the whole production story:

  - No API key set  -> OfflineGenerator runs the deterministic templates in
    adapt.py, so the pipeline works on a plane with no network.
  - ANTHROPIC_API_KEY set + --live -> the same prompts route to Claude.

Swapping providers is a one-class change here, nothing else in the pipeline
moves.
"""

import os


class OfflineGenerator:
    """Deterministic fallback. Delegates to adapt.py's channel writers."""

    name = "offline-deterministic"

    def generate(self, channel, account, lift, atoms):
        from . import adapt
        return adapt.write(channel, account, lift, atoms)


class ClaudeClient:
    """Live mode. Routes the factory prompts to Anthropic's API."""

    name = "claude"

    def __init__(self, model="claude-sonnet-4-6"):
        self.model = model
        try:
            import anthropic  # imported lazily so offline mode needs no install
        except ImportError as exc:
            raise RuntimeError(
                "Live mode needs the anthropic package: pip install anthropic"
            ) from exc
        self.client = anthropic.Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])

    def generate(self, channel, account, lift, atoms):
        from .prompts import build_channel_prompt, EXTRACT_SYSTEM
        system = build_channel_prompt(channel, account, lift)
        user = (
            "Source atom library (JSON-like):\n"
            + "\n".join(f"- {k}: {v}" for k, v in atoms.items())
            + f"\n\nWrite the {channel} asset now."
        )
        msg = self.client.messages.create(
            model=self.model,
            max_tokens=2000,
            system=system,
            messages=[{"role": "user", "content": user}],
        )
        # Returned as raw text; the caller still runs it through qa.clean().
        return {"raw": msg.content[0].text}


def get_client(live: bool):
    if live and os.environ.get("ANTHROPIC_API_KEY"):
        return ClaudeClient()
    return OfflineGenerator()
