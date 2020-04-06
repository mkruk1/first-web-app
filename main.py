from fastapi import FastAPI
#from typing import Dict
#from pydantic import BaseModel
app = FastAPI()

@app.get("/")
async def root ():
    return {"method": "Hello World during the coronavirus pandemic!"}


"""
class HelloResp (BaseModel):
    msg: str

@app.get("/get", response_model = HelloResp)
async def getMethod (name: str):
    return HelloResp (msg=f "Hello {name}")

class GiveMeSomethingRq (BaseModel):
    first_key: str

class GiveMeSomethingRespo (BaseModel):
    received: Dict
    constant_data: str = "python jest super"

@app.post("/dej/mi/cos", reponse_model = GiveMeSomethingResp)
def receive_something (rq: GiveMeSomethingRq):
    return GiveMeSomethingResp (received = rq.dict())
"""
