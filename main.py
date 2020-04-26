from fastapi import FastAPI, Cookie, Response, HTTPException, Depends, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from hashlib import sha256
from starlette.responses import RedirectResponse
import secrets

app = FastAPI ()
app.tokens = []
security = HTTPBasic ()

    
@app.post ("/login")
def create_cookie (user: str, password: str, response: Response, credentials: HTTPBasicCredentials = Depends (security)):
    if_correct_username = secrets.compare_digest (credentials.username, "trudnY")
    if_correct_password = secrets.compare_digest (credentials.password, "PaC13Nt")

    if ((not if_correct_username) and (not if_correct_password)):
        raise HTTPException (status_code = status.HTTP_401_UNAUTHORISED)

    session_token = sha256 (bytes (f"{user}{password}{app.secret.key}", encoding='utf8'))
    app.tokens.append (session_token)

    response = RedirectResponse (url = "/welcome")
    response.set_cookie (key= "session_token", value = session_token)

    return response


@app.get ("/welcome") 
def welcome (*, response: Response, session_token: str = Cookie (None)):
    return {"message": "you are welcome!"}  

    
