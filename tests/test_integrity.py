from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "python"))

from normalize import topic_id
from validate import validate


def test_slug_generation() -> None:
    assert topic_id("Käthe Kollwitz") == "topic.kaethe-kollwitz"
    assert topic_id("Baldur's Gate 3") == "topic.baldur-s-gate-3"


def test_dataset_integrity() -> None:
    result = validate()
    assert result["topics"] == 301
    assert result["categories"] == 19
    assert result["relations"] == 105
