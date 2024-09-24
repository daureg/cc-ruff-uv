.PHONY: pyright local-tests clean
pyright:
	pyright --pythonpath $(shell poetry env info -e)

local-tests:
	poetry run pytest -W ignore::DeprecationWarning --cov-report html

clean:
	fd -t f -uu -H pyc -X rm && fd -0 -t d -uu __pycache__ -X rmdir
	rm -rf .ruff_cache/ .mypy_cache/ .pytest_cache/ htmlcov/ .coverage* xunit-reports/ coverage-reports/ dist/
