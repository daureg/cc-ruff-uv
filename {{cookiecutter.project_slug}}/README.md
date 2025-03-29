# {{ cookiecutter.project_name }}

{{ cookiecutter.project_short_description }}

## How to contribute

You need [`uv`](https://docs.astral.sh/uv/getting-started/installation/) and [pre-commit](https://pre-commit.com/#install) installed.

After cloning the repository, run the following commands:
```shell
uv sunc -U
pre-commit install
pre-commit run --all-files
make local-tests
git switch -c YOUR_COOL_BRANCH
```
