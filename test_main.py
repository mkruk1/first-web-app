from starlette.testclient import TestClient
from main import app

client = TestClient (app)

def test_read_main ():
    response = client.get("/")
    assert response.status_code == 200


def test_wrong_patient ():
    response = client.get ("/patient/3")
    assert response.status_code == 200


def test_add_patient ():
    client.post ("/patient/3", json = {"name": "andrew", "surename": "duda"})
    response = client.get ("/patient/3");
    assert response == {"name": "andrew", "surename": "duda"}

