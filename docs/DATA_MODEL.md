# Data Model

The canonical source is JSONL under `data/normalized/`. Generated TSV and SQL files are reproducible views for languages and tools that benefit from simpler interchange formats.

## Topic identity

Topic IDs are stable ASCII slugs prefixed with `topic.`. Display labels remain UTF-8 and may change independently only after references and migrations are considered.

## Categories

Topics may belong to multiple categories. Array order currently records the generated seed's primary category first; PostgreSQL represents this explicitly with `topic_categories.is_primary`.

## Relations

Relations are directed, typed edges between topic IDs. `generated_seed` relations are hypotheses for curation, not authoritative semantic claims.

## Curation states

- `generated_seed` — automatically or heuristically derived foundation data.
- `curated` — intentionally edited by a human or reviewed workflow.
- `reviewed` — checked against the project's later evidence and quality criteria.

## Canonical versus generated

Canonical foundation data:

- `data/normalized/topics.jsonl`
- `data/normalized/relations.jsonl`
- `data/normalized/categories.json`

Generated views:

- `data/generated/topics.tsv`
- `data/generated/relations.tsv`
- `data/generated/challenges.jsonl`
- `sql/seed.sql`
