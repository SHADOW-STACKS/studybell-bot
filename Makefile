.PHONY: help install check fix lint format typecheck test clean

help:
	@echo "Project Commands"
	@echo ""
	@echo "Setup:"
	@echo "  make install       - Install dependencies with uv"
	@echo ""
	@echo "Code Quality:"
	@echo "  make check         - Run all checks (lint + format + types + tests)"
	@echo "  make fix           - Auto-fix lint and format issues"
	@echo "  make lint          - Run linter (ruff check)"
	@echo "  make format        - Check formatting (ruff format --check)"
	@echo "  make typecheck     - Run type checker (mypy)"
	@echo "  make test          - Run tests"
	@echo "  make clean         - Remove caches"

install:
	uv sync --locked --all-extras

check: lint format typecheck test

fix:
	uv run ruff check --fix .
	uv run ruff format .

lint:
	uv run ruff check .

format:
	uv run ruff format --check .

# mypy and pytest exit non-zero on an empty tree; same guard as in ci.yml.
typecheck:
	@if [ -n "$$(find app -name '*.py' 2>/dev/null | head -n 1)" ]; then \
		uv run mypy .; \
	else echo "typecheck: no Python files in app/, skipped"; fi

test:
	@if [ -n "$$(find tests -name '*.py' 2>/dev/null | head -n 1)" ]; then \
		uv run pytest tests/ -v; \
	else echo "test: no Python files in tests/, skipped"; fi

clean:
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type d -name .pytest_cache -exec rm -rf {} +
	find . -type d -name .mypy_cache -exec rm -rf {} +
	find . -type d -name .ruff_cache -exec rm -rf {} +
