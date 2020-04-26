from fastapi import FastAPI, Cookie, Response, HTTPException, Depends
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from hashlib import sha256
from starlette.responses import RedirectResponse
import secrets

app = FastAPI ()
app.tokens = []
security = HTTPBasic ()

    
@app.post ("/login")
def create_cookie (user: str, password: str, response: Response, credentials: HTTPBasicCredentials = Depends (security)):
    username = secrets.compare_digest (credentials.username, "trudnY")
    password = secrets.compare_digest (credentials.password, "PaC13Nt")

    if not (username and password):
        raise HTTPException (status_code = 401)

    session_token = sha256 (bytes (f"{user}{password}{app.secret.key}", encoding='utf8'))
    app.tokens.append (session_token)

    response.set_cookie (key= "session_token", value = session_token)
    response = RedirectResponse (url = "/welcome")

    return RedirectResponse (url = "/welcome")


@app.get ("/welcome") 
def welcome (*, response: Response, session_token: str = Cookie (None)):
    return {"message": "you are welcome!"}  

    
