"""Unit and integration tests for main.py."""

from fastapi.testclient import TestClient # pylint: disable=import-error

from main import app, read_root, read_item

client = TestClient(app)


# Unit tests: call the functions directly, no HTTP involved

def test_read_root_returns_expected_greeting():
    """Root endpoint returns the expected greeting."""
    result = read_root()
    assert result == {"Hello": "World"}


def test_read_root_returns_dict():
    """Root endpoint always returns a dict."""
    result = read_root()
    assert isinstance(result, dict)


def test_read_item_with_query():
    """Item endpoint returns the query param when given."""
    result = read_item(item_id=1, q="teste")
    assert result == {"item_id": 1, "q": "teste"}


def test_read_item_without_query():
    """Item endpoint returns None for q when not given."""
    result = read_item(item_id=5, q=None)
    assert result == {"item_id": 5, "q": None}


def test_read_item_preserves_id():
    """Item endpoint returns the same id it received."""
    result = read_item(item_id=42, q="abc")
    assert result["item_id"] == 42


def test_read_item_returns_dict():
    """Item endpoint always returns a dict."""
    result = read_item(item_id=7, q="xyz")
    assert isinstance(result, dict)


def test_read_item_with_zero_id():
    """Item endpoint accepts an id of zero."""
    result = read_item(item_id=0, q=None)
    assert result["item_id"] == 0


def test_read_item_with_negative_id():
    """Item endpoint accepts a negative id, since there is no validation for it."""
    result = read_item(item_id=-1, q=None)
    assert result["item_id"] == -1


# Integration tests: using TestClient to call the real API over HTTP

def test_integration_root_endpoint():
    """GET / returns 200 with the expected body."""
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hello": "World"}


def test_integration_items_endpoint():
    """GET /items/{item_id} returns 200 with the expected body."""
    response = client.get("/items/5?q=abc")
    assert response.status_code == 200
    assert response.json() == {"item_id": 5, "q": "abc"}
