# Branching Model

## `main`

Stable integration branch. It currently contains only the repository's initial commit until reviewed foundation work is merged.

## `root-commit`

A deliberately minimal baseline branch built directly from the repository's initial commit. It records the project purpose, documentation conventions, and contribution/security basics without introducing the implementation foundation.

## `feat/polyglot-lab-v0.2-foundation`

Active foundation branch. It builds on the baseline and introduces schemas, normalized data, SQL learning material, and language-specific tooling.

Foundation changes are reviewed through a draft pull request before reaching `main`.
