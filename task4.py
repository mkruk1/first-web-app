from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict
from starlette.responses import RedirectResponse 


app = FastAPI()
class Patient (BaseModel):
    name: str
    surename: str


@app.get ("/")
def justBasicStuff ():
    raise HTTPException (status_code = 203)


patients_list = []

@app.get ("/patient/{pk}")
def findPatient (pk: int):
    if (pk >= len (patients_list)):
        raise HTTPException(status_code = 204)    

    return patients_list [pk]



@app.post ("/patient", response_model = Patient)
def createPatient (patient: Patient): 
    patients_list.append (patient.dict ())
    return patient
