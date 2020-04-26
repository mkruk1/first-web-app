from starlette.testclient import TestClient
from main import app

client = TestClient (app)

def test_read_main ():
    response = client.get("/")
    assert response.status_code == 203


def test_wrong_url ():
    reponse = client.get ("/lol/")
    assert reponse.status_code == 404


def test_wrong_patient ():
    response = client.get ("/patient/3")
    assert response.status_code == 204


def test_add_patient ():
    response = client.post ("/patient", json = {"name": "andrew", "surename": "duda"})
    assert response.status_code == 200
    response = client.get ("/patient/0");
    assert response.status_code == 200
    assert response.json () == {"name": "andrew", "surename": "duda"}


