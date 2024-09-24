# {{ cookiecutter.project_name }}

{{ cookiecutter.project_short_description }}

## How to contribute

You need [poetry](https://python-poetry.org/docs/#installation) and [pre-commit](https://pre-commit.com/#install) installed.

After cloning the repository, run the following commands:
```shell
poetry install --sync --with dev
pre-commit install
pre-commit run --all-files
make local-tests
git switch -c YOUR_COOL_BRANCH
```
