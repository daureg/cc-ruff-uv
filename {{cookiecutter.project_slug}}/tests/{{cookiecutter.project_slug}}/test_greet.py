import pytest

from {{cookiecutter.project_slug}} import greet


@pytest.mark.parametrize(
    ("name", "expected"), [("John", "Hello, John!"), ("123", "Hello, 123!")]
)
def test_greet(name: str, expected: str) -> None:
    """Test the greet function."""
    assert greet(name) == expected
