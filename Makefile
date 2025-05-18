.PHONY: install install_project format test profiling build publish publish_test push

install:
	uv sync --group dev --group test

install_project:
	uv add --dev --editable .
	# pip install -e .

format:
	uv run ruff format .
	uv run ruff check --fix --exit-zero
	uv run pre-commit run --all-files
	uv run mypy .

test:
	uv run pytest --cov=. --cov-report term:skip-covered --cov-report=html .

profiling:
	uv run python -m cProfile -o profile -m pytest -l
	uv run gprof2dot -f pstats profile | dot -Tpng -o profile.png

build:
	uv build

publish: build
	uv publish --index pypi

publish_test: build
	uv publish --index testpypi

push:
	uv run git push --follow-tags origin $(shell git rev-parse --abbrev-ref HEAD)
