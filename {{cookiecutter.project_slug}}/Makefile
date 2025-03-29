.PHONY: pyright local-tests clean mypy ruff
pyright:
	pyright --pythonpath .venv/bin/python3

local-tests:
	uv run --no-sync pytest -W ignore::DeprecationWarning --cov-report html

clean:
	fd -t f -uu -H pyc -X rm && fd -0 -t d -uu __pycache__ -X rmdir
	rm -rf .ruff_cache/ .mypy_cache/ .pytest_cache/ htmlcov/ .coverage* xunit-reports/ coverage-reports/ dist/

mypy:
	uv run --no-sync mypy src/ tests/

ruff:
	git ls-files '*.py' | xargs uv run --no-sync --with ruff ruff check --output-format concise

lint: mypy pyright ruff
