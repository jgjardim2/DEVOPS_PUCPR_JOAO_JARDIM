"""Unit tests for the FastAPI endpoints in main.py."""

from main import read_root, read_item


def test_read_root():
    """Ensure the root endpoint returns the expected greeting."""
    result = read_root()
    assert result == {"Hello": "World"}


def test_read_item_with_query():
    """Ensure read_item returns the query parameter when provided."""
    result = read_item(item_id=1, q="teste")
    assert result == {"item_id": 1, "q": "teste"}


def test_read_item_without_query():
    """Ensure read_item returns None for q when not provided."""
    result = read_item(item_id=5, q=None)
    assert result == {"item_id": 5, "q": None}


def test_read_item_id_type():
    """Ensure the item_id is returned unchanged in the response."""
    result = read_item(item_id=42, q="abc")
    assert result["item_id"] == 42


def test_read_item_returns_dict():
    """Ensure read_item always returns a dictionary."""
    result = read_item(item_id=7, q="xyz")
    assert isinstance(result, dict)