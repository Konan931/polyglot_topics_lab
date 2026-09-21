#!/usr/bin/env python3
"""Regenerate sql/seed.sql from canonical foundation data."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "normalized"
OUT = ROOT / "sql" / "seed.sql"


def load_jsonl(path: Path) -> list[dict]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def quote(value: object) -> str:
    return str(value).replace("'", "''")


def main() -> None:
    topics = load_jsonl(DATA / "topics.jsonl")
    relations = load_jsonl(DATA / "relations.jsonl")
    categories = json.loads((DATA / "categories.json").read_text(encoding="utf-8"))
    lines = ["-- Generated from data/normalized/*. This is a reproducible seed view.", "begin;"]

    for category in categories:
        lines.append(
            "insert into categories (id, label, description) values "
            f"('{quote(category['id'])}', '{quote(category['label'])}', '{quote(category['description'])}') "
            "on conflict (id) do nothing;"
        )

    for topic in topics:
        lines.append(
            "insert into topics (id, canonical_name, entity_type, difficulty, summary_short, metadata_status) values "
            f"('{quote(topic['id'])}', '{quote(topic['canonical_name'])}', '{quote(topic['entity_type'])}', "
            f"{topic['difficulty']}, '{quote(topic['summary_short'])}', '{quote(topic['metadata_status'])}') "
            "on conflict (id) do nothing;"
        )
        for index, category_id in enumerate(topic["categories"]):
            lines.append(
                "insert into topic_categories (topic_id, category_id, is_primary, weight) values "
                f"('{quote(topic['id'])}', '{quote(category_id)}', "
                f"{'true' if index == 0 else 'false'}, {1.0 if index == 0 else 0.75}) "
                "on conflict (topic_id, category_id) do nothing;"
            )

    for relation in relations:
        lines.append(
            "insert into relations (id, source_id, target_id, relation_type, weight, metadata_status) values "
            f"('{quote(relation['id'])}', '{quote(relation['source_id'])}', '{quote(relation['target_id'])}', "
            f"'{quote(relation['relation_type'])}', {relation['weight']}, '{quote(relation['metadata_status'])}') "
            "on conflict (id) do nothing;"
        )

    lines.append("commit;")
    OUT.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"wrote {OUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
