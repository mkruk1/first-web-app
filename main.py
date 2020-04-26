from fastapi import FastAPI, Cookie, Response, Request, HTTPException, Depends, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

from hashlib import sha256
from starlette.responses import RedirectResponse
import secrets

app = FastAPI ()
app.sessions= {}
security = HTTPBasic ()


def login_validation (credentials: HTTPBasicCredentials = Depends (security)):
    correct_username = secrets.compare_digest (credentials.username, 'trudnY')
    correct_password = secrets.compare_digest (credentials.password, 'PaC13Nt')

    if not (correct_username and correct_password):
        raise HTTPException (status_code = status.HTTP_401_UNAUTHORIZED, detail = 'Incorrect login or password', headers = {"WWW-Authenticate": "Basic"})

    session_token = sha256 (bytes (f"{credentials.username}{credentials.password}{app.secret_key}", endcoding='utf8')).hexdigest ()
    app.sessions [session_token] = credentials.username
    return session_token


    
@app.post ("/login")
def login (response: Response, session_token: str, credentials = Depends (login_validation)):
    response = RedirectResponse (url = '/welcome')
    return response

def cookies_validation (session_token: str = Cookie (None)):
    if session_token not in app.sessions:
        session_token = None
    return session_token

@app.get ("/welcome") 
def welcome (request: Request, response: Response, session_token: str = Depends (cookies_validation)):
    if session_token == None:
        raise HTTPException (status_code = 401)
    
    return JSONResponse (status_code = 302, content = jsonable_encode ({"message": "hello"}))

    
