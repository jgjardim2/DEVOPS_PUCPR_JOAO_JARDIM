from main import read_root, read_item


def test_read_root():
    result = read_root()
    assert result == {"Hello": "World"}


def test_read_item_with_query():
    result = read_item(item_id=1, q="teste")
    assert result == {"item_id": 1, "q": "teste"}


def test_read_item_without_query():
    result = read_item(item_id=5, q=None)
    assert result == {"item_id": 5, "q": None}


def test_read_item_id_type():
    result = read_item(item_id=42, q="abc")
    assert result["item_id"] == 42


def test_read_item_returns_dict():
    result = read_item(item_id=7, q="xyz")
    assert isinstance(result, dict)