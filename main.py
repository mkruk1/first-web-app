from fastapi import FastAPI
from typing import Dict
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
async def root ():
    return {"method": "Hello World during the coronavirus pandemic!"}

@app.get ("/method")
async def getMethod ():
    return {"method": "GET"}

@app.post ("/method")
async def postMethod ():
    return {"method": "POST"}


@app.put ("/method")
async def putMethod ():
    return {"method": "PUT"}


@app.delete ("/method")
async def deleteMethod ():
    return {"method": "DELETE"}


"""
class HelloResp (BaseModel):
    msg: str

@app.get("/method/", response_model = HelloResp)
async def getMethod (name: str):
    return HelloResp (msg="Hello {name}")

class GiveMeSomethingRq (BaseModel):
    first_key: str

class GiveMeSomethingResp (BaseModel):
    received: Dict
    constant_data: str = "python jest super"

@app.post("/post/", response_model = GiveMeSomethingResp)
def receive_something (rq: GiveMeSomethingRq):
    return GiveMeSomethingResp (received = rq.dict())
    """
