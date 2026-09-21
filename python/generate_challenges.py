#!/usr/bin/env python3
"""Generate deterministic starter challenges from canonical topics."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TOPICS = ROOT / "data" / "normalized" / "topics.jsonl"
OUT = ROOT / "data" / "generated" / "challenges.jsonl"


def main() -> None:
    topics = [json.loads(line) for line in TOPICS.read_text(encoding="utf-8").splitlines() if line.strip()]
    challenges = []
    for index, topic in enumerate(topics[:24], 1):
        challenges.append({
            "id": f"challenge.lookup.{index:03d}",
            "kind": "lookup",
            "difficulty": min(topic["difficulty"], 5),
            "prompt": f"Identify the topic described as: {topic['summary_short']}",
            "targets": [topic["id"]],
            "expected": topic["canonical_name"],
            "metadata_status": "generated_seed",
        })
    OUT.write_text("\n".join(json.dumps(row, ensure_ascii=False) for row in challenges) + "\n", encoding="utf-8")
    print(f"wrote {len(challenges)} challenges to {OUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
