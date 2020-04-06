from fastapi import FastAPI
from pydantic import BaseModel
from typing import Dict
from starlette.responses import RedirectResponse 

app = FastAPI()
patients = []


class Patient ():
    def __init__ (self, name, surname):
        self.name = name
        self.surname = surname


@app.get ("/patient/{pk}")
def findPatient (pk: int):
    if (pk >= len (patients)):
        return RedirectResponse (url= 'https://en.wikipedia.org/wiki/List_of_HTTP_status_codes') 
    return {"name": patients [pk].name, "surname": patients [pk].surname }


class My_rq (BaseModel):
    patient : Dict


@app.post ("/patient")
def createPatient (rq: My_rq): 
    my_dict = rq.dict()
    patients.append (Patient (my_dict ["name"], my_dict ["surname"]))
