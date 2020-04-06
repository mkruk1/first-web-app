from fastapi.testclient import TestClient
import pytest

def test_receive_something():
    with TestClient (app) as client:
        response = client.post("/patient", json = {"name": "michal", "surename": "kruk"})
        assert response.json() == {"id": 0, "patient": {"name": "michal", "surename": "kruk"}}
