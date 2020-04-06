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
def read_item (pk: int):
    if (pk >= len (patients)):
        return RedirectResponse (url= 'https://en.wikipedia.org/wiki/List_of_HTTP_status_codes') 
    return {"name": patients [pk].name, "surname": patients [pk].surname }
