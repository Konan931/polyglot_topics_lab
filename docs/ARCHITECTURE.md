# Architecture

Polyglot Topics Lab separates four concerns.

## 1. Source layer

Immutable or minimally transformed source material, including the original topic list.

## 2. Canonical knowledge layer

Normalized entities, aliases, categories, typed relations, descriptions, provenance, and learning metadata.

## 3. Computational views

- R: statistics and exploratory analysis.
- Julia: graph algorithms, numerical/scientific workflows, visualization, Pluto notebooks.
- Python: normalization, validation, generators, NLP/AI adapters.
- SQL/PostgreSQL: integrity, querying, joins, recursive traversal, later vector search.
- Go: operational utilities and compact services.
- C: systems-level parsing and representation.
- Web: interactive explorer and learning interface.

## 4. Generated artifacts

CSV, JSONL, SQL seeds, reports, challenges, notebooks, and visualization-ready exports.

Generated files are views of the canonical model, not competing sources of truth.
