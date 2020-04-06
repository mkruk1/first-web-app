from fastapi import FastAPI, Request
from pydantic import BaseModel
from typing import Dict

app = FastAPI()

id_number = 0 

@app.get ("/")
async def showText ():
    return {"message": "this works6"}


class getSth (BaseModel):
    first_key : str
    second_key : str



@app.post ("/patient")
async def receive_sth (rq: getSth):
    id_number += 1
    return {"id" : id_number, "patient" : {"name": getSth.first_key, "surename": getSth.second_key}}


