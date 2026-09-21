# Polyglot Topics Lab

A polyglot training and research base for exploring one knowledge model through multiple programming languages, data systems, and scientific-computing workflows.

## Foundation snapshot

The v0.2 foundation currently contains:

- **301** normalized topic records from the original seed list,
- **19** multi-domain categories,
- **105** typed seed relations,
- JSON Schema contracts for topics, relations, and challenges,
- PostgreSQL schema and progressive SQL exercises,
- Python normalization, validation, export, and challenge tooling,
- R exploratory-analysis starters,
- a dependency-light Julia graph module and notebook seed,
- Go and C data-processing examples,
- a minimal static web explorer.

Automatically derived classifications and descriptions are explicitly marked `generated_seed`. They are foundation material for later curation, not claims of editorial verification.

## Language roles

- **R** — exploratory data analysis, statistics, reports.
- **Julia** — scientific computing, graph algorithms, numerical analysis, reactive notebooks.
- **Python** — normalization, validation, generators, later NLP/AI integration.
- **SQL/PostgreSQL** — canonical relational model and data-learning curriculum.
- **Go** — compact services and operational data utilities.
- **C** — parsing, representation, indexing, and systems-level learning.
- **Web/JavaScript** — interactive exploration and visualization.

## Quick checks

```sh
python3 python/validate.py
python3 python/export_views.py
python3 python/generate_challenges.py

(cd go && go run ./cmd/topicstats ../data/generated/topics.tsv)
cc -std=c11 -Wall -Wextra -pedantic c/src/topic_count.c -o topic_count
./topic_count data/generated/topics.tsv
```

Julia and R examples live under `julia/` and `R/`; see [docs/LEARNING_PATHS.md](docs/LEARNING_PATHS.md).

## Data authority

`data/normalized/*.jsonl` and `categories.json` are canonical foundation data. Files under `data/generated/` and `sql/seed.sql` are reproducible views.

See [docs/DATA_MODEL.md](docs/DATA_MODEL.md) and [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md).

## Branches

- `main` — stable integration branch.
- `root-commit` — minimal documented baseline.
- `feat/polyglot-lab-v0.2-foundation` — current foundation work.

## License

Apache License 2.0. See [LICENSE](LICENSE).
