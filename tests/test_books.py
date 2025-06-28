from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_add_book():
    res = client.post("/books", json={"title": "Test Book", "author": "Tester"})
    assert res.status_code == 200

def test_list_books():
    res = client.get("/books")
    assert res.status_code == 200
    assert "books" in res.json()