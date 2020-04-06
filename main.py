from fastapi import FastAPI
from pydantic import BaseModel
from typing import Dict

app = FastAPI()

id_number = -1


class getSth (BaseModel):
    first_key : Dict


class myResponse ():
    received : Dict
    id_number : int = id_number 


@app.post ("/patient", response_model = myResponse)
async def receive_sth (rq: getSth):
    id_number += 1
    return myResponse (received = rq.dict())

