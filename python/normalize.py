#!/usr/bin/env python3
"""Normalize raw topic labels into stable seed identifiers."""
from __future__ import annotations

import re
import unicodedata


def slugify(value: str) -> str:
    value = (
        value.strip()
        .lower()
        .replace("ä", "ae")
        .replace("ö", "oe")
        .replace("ü", "ue")
        .replace("ß", "ss")
    )
    value = unicodedata.normalize("NFKD", value).encode("ascii", "ignore").decode("ascii")
    return re.sub(r"[^a-z0-9]+", "-", value).strip("-")


def topic_id(label: str) -> str:
    return f"topic.{slugify(label)}"
