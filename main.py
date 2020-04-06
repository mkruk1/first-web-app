from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict
from starlette.responses import RedirectResponse 



class Patient ():
    def __init__ (self, name, surename):
        self.name = name
        self.surname = surename


app = FastAPI()
patients = []
patients.append (Patient ("ja", "ty"))


@app.get ("/patient/{pk}")
def findPatient (pk: int):
    if (pk >= len (patients)):
        return HTTPException(status_code = 204)
    return {"name": patients [pk].name, "surename": patients [pk].surename }


class My_rq (BaseModel):
    patient : Dict


@app.post ("/patient")
def createPatient (rq: My_rq): 
    my_dict = rq.dict()
    patients.append (Patient (my_dict ["name"], my_dict ["surename"]))
