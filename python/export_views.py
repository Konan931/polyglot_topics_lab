#!/usr/bin/env python3
"""Export canonical JSONL into TSV views used by low-dependency examples."""
from __future__ import annotations

import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"


def load_jsonl(path: Path) -> list[dict]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def main() -> None:
    topics = load_jsonl(DATA / "normalized" / "topics.jsonl")
    relations = load_jsonl(DATA / "normalized" / "relations.jsonl")
    out = DATA / "generated"
    out.mkdir(exist_ok=True)

    with (out / "topics.tsv").open("w", encoding="utf-8", newline="") as handle:
        writer = csv.writer(handle, delimiter="\t", lineterminator="\n")
        writer.writerow(["id", "canonical_name", "entity_type", "categories", "difficulty", "summary_short", "metadata_status"])
        for row in topics:
            writer.writerow([row["id"], row["canonical_name"], row["entity_type"], "|".join(row["categories"]), row["difficulty"], row["summary_short"], row["metadata_status"]])

    with (out / "relations.tsv").open("w", encoding="utf-8", newline="") as handle:
        writer = csv.writer(handle, delimiter="\t", lineterminator="\n")
        writer.writerow(["id", "source_id", "target_id", "relation_type", "weight", "metadata_status"])
        for row in relations:
            writer.writerow([row["id"], row["source_id"], row["target_id"], row["relation_type"], row["weight"], row["metadata_status"]])


if __name__ == "__main__":
    main()
