from fastapi.testclient import TestClient
import pytest

from main import app

client = TestClient (app)

def test_receive_something():
    response = client.post("/patient", json={'name': 'a', 'surename': 'b'})
    assert response.json() == {"id": 0, "patient": {'name': 'a', 'surename': 'b'}}
