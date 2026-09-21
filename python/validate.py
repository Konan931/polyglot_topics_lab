#!/usr/bin/env python3
"""Run dependency-free integrity checks over the foundation dataset."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TOPICS = ROOT / "data" / "normalized" / "topics.jsonl"
RELATIONS = ROOT / "data" / "normalized" / "relations.jsonl"
CATEGORIES = ROOT / "data" / "normalized" / "categories.json"


def load_jsonl(path: Path) -> list[dict]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def validate() -> dict[str, int]:
    topics = load_jsonl(TOPICS)
    relations = load_jsonl(RELATIONS)
    categories = json.loads(CATEGORIES.read_text(encoding="utf-8"))

    topic_ids = [row["id"] for row in topics]
    if len(topic_ids) != len(set(topic_ids)):
        raise ValueError("duplicate topic IDs")

    category_ids = {row["id"] for row in categories}
    for topic in topics:
        unknown = set(topic["categories"]) - category_ids
        if unknown:
            raise ValueError(f"unknown categories for {topic['id']}: {sorted(unknown)}")

    topic_set = set(topic_ids)
    for relation in relations:
        if relation["source_id"] not in topic_set or relation["target_id"] not in topic_set:
            raise ValueError(f"dangling relation: {relation['id']}")
        if relation["source_id"] == relation["target_id"]:
            raise ValueError(f"self relation: {relation['id']}")

    return {"topics": len(topics), "categories": len(categories), "relations": len(relations)}


if __name__ == "__main__":
    print("validation ok:", validate())
