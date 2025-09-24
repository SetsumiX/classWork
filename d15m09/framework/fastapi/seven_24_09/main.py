import secrets
from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
import uvicorn
from database import Database

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

db = Database()

active_session = {}

def get_cur_user(request: Request):
    """Получение текущего вользователя
        :parse request: Данные запроса
        :return: int user_id
    """
    session_token = request.cookies.get("session_token")
    if not session_token: return None
    user_id = active_session.get(session_token)
    return user_id

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    user_id = get_cur_user(request)
    if user_id is None:
        return RedirectResponse(url="/login")
    todos = db.get_user_id(user_id)
    return templates.TemplateResponse("index.html",
                                      {"request": request, "todos": todos})

@app.get("/login", response_class=HTMLResponse)
async def login_page(request: Request):
    if get_cur_user(request): return RedirectResponse(url="/")
    return templates.TemplateResponse("login.html", {"request": request})

@app.post("/login")
async def login_post(request: Request, username: str = Form(...), password: str = Form(...)):
    user_id = db.authenticate_user(username, password)
    if user_id:
        session_token = secrets.token_hex(16)
        print(f"Токен аккаунта({username}) - {session_token}")
        active_session[session_token] = user_id
        response = RedirectResponse("/", status_code=303)
        response.set_cookie(key="session_token", httponly=True, max_age=3600)
        return response
    else:
        return templates.TemplateResponse("login.html", {"request": request, "error": "Неверное имя пользователя или пароль"})

if __name__ == "__main__":
    uvicorn.run("main:app",
                host="127.0.0.1", port=5555,
                reload=True, reload_dirs=["./static", "./templates"])