from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

def test_create_item():
    payload = {"name": "Laptop", "price": 999.99}
    response = client.post("/items/", json=payload)
    assert response.status_code == 201
    assert response.json() == {"name": "Laptop", "price": 999.99}

def test_create_item_invalid_data():
    # Verify FastAPI returns 422 when required fields are missing or wrong type
    response = client.post("/items/", json={"name": "Laptop"})
    assert response.status_code == 422
