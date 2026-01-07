# algorithms

Small collection of algorithm implementations (by topic) with matching pytest suites. Designed for interview practice: implementations are small, index-based, and often mutate in-place.

CI status

[![CI](https://github.com/jadielam/algorithms/actions/workflows/ci.yml/badge.svg)](https://github.com/jadielam/algorithms/actions/workflows/ci.yml)


## Quickstart — run tests

### Using Poetry (preferred)

```bash
poetry install
poetry run pytest -q
```

### Using an explicit virtualenv (manual)

```bash
python -m venv .venv
source .venv/bin/activate   # macOS / Linux
.venv\Scripts\Activate.ps1  # Windows PowerShell
python -m pip install -e .
python -m pip install pytest
pytest -q
```

## Pre-commit (optional)

Install and enable locally so tests run before each commit:

```bash
poetry run pip install pre-commit
poetry run pre-commit install

# or global
pip install pre-commit
pre-commit install
```

## Repository layout

- `algorithms/` — source packages (e.g., `sorting`, `graphs`, `trees`, `string`, `ml`).
- `tests/algorithms/` — pytest modules mirroring `algorithms/`.
- `pyproject.toml` — project metadata and dev dependencies (Poetry).

## Key conventions

- Package imports: use `from algorithms.<topic>.<module> import <symbol>` in tests and examples.
- Many APIs are index-based or mutate in-place (e.g., `quick_sort(a, 0, len(a)-1)`).

## More guidance

- See `.github/copilot-instructions.md` for development conventions and examples.

