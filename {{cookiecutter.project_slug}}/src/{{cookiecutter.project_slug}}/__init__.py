"""{{cookiecutter.project_short_description.rstrip('.')}}."""

__version__ = "0.1.0"


def greet(name: str = "World") -> str:
    """Return the user greeting."""
    return f"Hello, {name}!"
