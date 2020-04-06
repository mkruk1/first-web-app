from fastapi.testclient import TestClient
import pytest

from main import app

client = TestClient (app)

def test_receive_something():
    response = client.post("/patient", json={'name': 'a', 'surename': 'b'})
    print ("aSDFfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff") 
    print (type(response))
