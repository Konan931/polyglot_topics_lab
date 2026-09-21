# Project Brief

## Objective

Build a reusable polyglot knowledge and training dataset from a heterogeneous list of topics.

The same canonical entities should support:

- explanations and discovery,
- category and relation modeling,
- SQL exercises,
- R-based statistics and exploratory analysis,
- Julia-based scientific and graph computing,
- Python-based validation and AI workflows,
- Go and C programming exercises,
- interactive web visualization.

## Design constraints

- One canonical data model, many computational views.
- Raw source terms remain recoverable.
- Topics may belong to multiple categories.
- Relations are typed and reference stable topic IDs.
- Generated metadata is explicitly marked as generated or heuristic.
- Database deployment is a later step, not a prerequisite for local validation.

## Near-term milestone

`v0.2-foundation` establishes schemas, normalized seed data, relational SQL, and first language-specific learning layers.
