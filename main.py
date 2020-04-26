from fastapi import FastAPI, Cookie, Response, Request, HTTPException, Depends, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from fastapi.templating import Jinja2Templates

from hashlib import sha256
from starlette.responses import RedirectResponse
import secrets

app = FastAPI ()
app.sessions= {}
app.secret_key = "sasdfasfadfasfdhkldfjahsfkjlakdfjahsdlfkjahsflkjashflkahsdfklahsfldkhaslfkhakf"
security = HTTPBasic ()
templates = Jinja2Templates (directory = "templates");


def login_validation (credentials: HTTPBasicCredentials = Depends (security)):
    correct_username = secrets.compare_digest (credentials.username, 'trudnY')
    correct_password = secrets.compare_digest (credentials.password, 'PaC13Nt')

    if not (correct_username and correct_password):
        raise HTTPException (status_code = status.HTTP_401_UNAUTHORIZED, detail = 'Incorrect login or password', headers = {"WWW-Authenticate": "Basic"})

    session_token = sha256 (bytes (f"{credentials.username}{credentials.password}{app.secret_key}", encoding='utf8')).hexdigest ()
    app.sessions [session_token] = credentials.username
    return session_token



@app.get ("/")
def defaultPage ():
    return {"message": "default page"}
    
@app.post ("/login")
def login (response: Response, session_token: str = Depends (login_validation)):
    response = RedirectResponse (url = '/welcome')
    response.status_code =  status.HTTP_302_FOUND
    response.set_cookie (key = "session_token", value = session_token)
    return response

def cookies_validation (session_token: str = Cookie (None)):
    if session_token not in app.sessions:
        session_token = None
    return session_token

@app.get ("/welcome") 
def welcome (response: Response, session_token: str = Depends (cookies_validation)):
    if session_token == None:
        raise HTTPException (status_code = 401)

    return templates.TemplateResponse ("item.html", {"request": request, "user": "trudnY"})


@app.post ("/logout")
def logout (response: Response, session_token: str = Depends (cookies_validation)):
    if session_token is None:
        response.status_code = status.HTTP_401_UNAUTHORIZED
        return {"message": "unauthorised"}
    
    app.sessions.pop (session_token)

    response = RedirectResponse (url = "/")
    response.status_code = status.HTTP_302_FOUND
    return response

