from fastapi import FastAPI, Request
from pydantic import BaseModel
from typing import Dict

app = FastAPI()

id_number = -1 

@app.get ("/")
async def showText ():
    return {"message": "this works2"}


class getSth (BaseModel):
    first_key : str
    second_key : str


class myResponse (BaseModel):
    id : int = id_number 
    patient : Dict


@app.post ("/patient", response_model = myResponse)
async def receive_sth (rq: getSth):
    id_number += 1
    return myResponse (patient = {"name": str, "surename": str})


