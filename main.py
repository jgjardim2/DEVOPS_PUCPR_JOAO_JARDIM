"""FastAPI app with a root endpoint and an item lookup endpoint."""

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    """Return a greeting message."""
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    """Return the item id and an optional query."""
    return {"item_id": item_id, "q": q}