from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict

app = FastAPI ()

@app.get ("/")
def basicFunc ():
    return {"message": "Hello world"}

@app.get ("/welcome")
def welcomeFunc ():
    return {"message": "Welcome world"}
