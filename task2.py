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


