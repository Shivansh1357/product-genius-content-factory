"""Forge: the Product Genius content factory.

One source library in, channel-ready and personalized assets out.
"""
from .pipeline import run, render_markdown
from .personas import ACCOUNTS

__all__ = ["run", "render_markdown", "ACCOUNTS"]
__version__ = "0.1.0"
