Purpose
- This repository is a collection of algorithm implementations (by topic) and accompanying tests. The goal is small, focused algorithmic functions and in-place implementations suitable for interview practice.

Repository layout (big picture)
- `algorithms/`: source packages organized by topic (e.g., `sorting`, `search`, `graphs`, `trees`, `ml`).
- `tests/algorithms/`: pytest test modules mirroring `algorithms/` structure.
- `pyproject.toml`: project metadata and dev dependencies (uses Poetry).

Key patterns and conventions (do not invent new ones without discussion)
- Package imports: modules are imported as `from algorithms.<topic>.<module> import <symbol>` (tests use this pattern).
- In-place mutation: many functions sort or modify lists in place (e.g., `quick_sort(a, 0, len(a)-1)`); follow existing signatures.
- Index-based APIs: several algorithms accept explicit start/end indices rather than slicing. Example:
  - `binary_search(a, 0, len(a), target)` (note the `high` parameter usage)
  - `quick_sort(a, 0, len(a)-1)` (uses inclusive `high` index)
- Keep functions small and deterministic — aim for the same call signatures and behavior as nearby modules when adding new code.

Testing & developer workflow
- Python: >=3.8 (see `pyproject.toml`). Dev dependencies include `pytest`.
- Recommended local workflow using Poetry:
  - `poetry install`
  - `poetry shell` (optional)
  - `poetry run pytest -q`
- Alternative (without Poetry): create a venv, `pip install -e .`, then run `pytest` from repo root.
- Tests mirror module structure. When adding a new module `algorithms/foo/bar.py`, add tests in `tests/algorithms/foo/test_bar.py` or similar.

Examples to follow
- Sorting (in-place): `algorithms/sorting/quicksort.py` → `quick_sort(a, 0, len(a)-1)`; tests: `tests/algorithms/sorting/quicksort_test.py`.
- Search (index-based): `algorithms/search/binary_search.py` → `binary_search(a, 0, len(a), target)`; tests: `tests/algorithms/search/binary_search_test.py`.

Code additions & PR guidance
- Keep changes small and focused — prefer implementing one algorithm per PR with matching tests.
- Add tests that mirror the project's style (pytest, function tests asserting expected outputs and in-place mutations).
- If changing public call signatures, update all tests and add a short note in the PR description.

Dependencies & integration points
- Minimal external dependencies; prefer stdlib. If you must add a dependency, update `pyproject.toml` via `poetry add --dev <pkg>` or consult the maintainer.

What to look for when editing
- Match existing function signatures (especially index parameter conventions).
- Preserve in-place behavior where current tests assume it.
- Use the package import path (`algorithms.*`) rather than relative paths in tests and top-level scripts.

Where to inspect for examples
- `pyproject.toml` — dependency and tooling guidance.
- `algorithms/sorting/quicksort.py` and `tests/algorithms/sorting/quicksort_test.py` — canonical in-place example.
- `algorithms/search/binary_search.py` and `tests/algorithms/search/binary_search_test.py` — canonical index-parameter example.

If anything in these notes is unclear or incomplete, tell me which area to expand (testing, packaging, API examples, or conventions).
