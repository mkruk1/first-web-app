from fastapi import FastAPI, Request
from pydantic import BaseModel
from typing import Dict

app = FastAPI()

id_number = 0 

@app.get ("/")
async def showText ():
    return {"message": "this works7"}


class GiveMeSomethingRq (BaseModel):
    name : str
    surename : str 

class GiveMeSomethingResp (BaseModel):
    id : int
    patient : Dict

@app.post ("/patient", )
def receive_something (rq: GiveMeSomethingRq):
    global id_number 
    id_number += 1
    return {"id" : id_number, "patient" : rq.dict()}





