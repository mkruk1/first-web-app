from fastapi import FastAPI
from typing import Dict
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
async def root ():
    return {"method": "Hello World during the coronavirus pandemic!"}
