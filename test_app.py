from fastapi.testclient import TestClient
from app import app  # pas eventueel aan naar je bestandsnaam

client = TestClient(app)

def test_home():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == "Hello jongens en meisjes"

def test_novi():
    response = client.get("/novi")
    assert response.status_code == 200
    assert response.json() == {"message": "Hoi Novi"}

def test_get_cars():
    response = client.get("/cars")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert len(response.json()) == 2

def test_get_car_success():
    response = client.get("/cars/Honda")
    assert response.status_code == 200
    data = response.json()
    assert data["brand"] == "Honda"
    assert "type" in data
    assert "price" in data

def test_get_car_not_found():
    response = client.get("/cars/BMW")
    assert response.status_code == 200  # of 404 als je dat wilt maken
    assert response.json() == {"error": "Car not found"}