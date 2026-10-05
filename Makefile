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
	uv sync --all-extras

check: lint format typecheck test

fix:
	uv run ruff check --fix .
	uv run ruff format .

lint:
	uv run ruff check .

format:
	uv run ruff format --check .

typecheck:
	uv run mypy .

test:
	uv run pytest tests/ -v

clean:
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type d -name .pytest_cache -exec rm -rf {} +
	find . -type d -name .mypy_cache -exec rm -rf {} +
	find . -type d -name .ruff_cache -exec rm -rf {} +
