import secrets
from fastapi.exceptions import HTTPException
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
    todos = db.get_user_todos(user_id)
    return templates.TemplateResponse("index.html",
                                      {"request": request, "todos": todos})

@app.get("/api/todos", response_class=HTMLResponse)
async def get_todos(request: Request):
    user_id = get_cur_user(request)
    if user_id is None:
        raise HTTPException(status_code=401, detail="Не авторизирован")
    return {"todos": db.get_user_todos(user_id)}

@app.post("/api/todos")
async def add_todos(todo: dict, request: Request):
    user_id = get_cur_user(request)
    if user_id is None:
        raise HTTPException(status_code=401, detail="Не авторизирован")
    if db.add_todo(user_id, todo["task"]):
        return {"message": "Задача добавлена"}
    else:
        raise HTTPException(status_code=500, detail="Ошибка добавления задачи")

@app.delete("/api/todos/{todo_id}")
async def del_todo(todo_id: int, request: Request):
    user_id = get_cur_user(request)
    if user_id is None:
        raise HTTPException(status_code=401, detail="Не авторизирован")
    if db.del_todo(user_id, todo_id):
        return {"message": "Задача удалена успешно"}
    else:
        raise HTTPException(status_code=404, detail="Задача не найдена")

@app.put("/api/todos/{todo_id}/toggle")
async def put_todo(todo_id: int, request: Request):
    user_id = get_cur_user(request)
    if user_id is None:
        raise HTTPException(status_code=401, detail="Не авторизирован")
    if db.toggle_todo(user_id, todo_id):
        return {"message": "Статус задачи изменён"}
    else:
        raise HTTPException(status_code=404, detail="Задача не найдена")

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
        response.set_cookie(key="session_token",value=session_token, httponly=True, max_age=3600)
        return response
    else:
        return templates.TemplateResponse("login.html", {"request": request, "error": "Неверное имя пользователя или пароль"})

@app.post("/registration")
async def regist_post(request: Request, username: str = Form(...), password: str = Form(...)):
    user_id = db.create_user(username, password)

    if user_id:
        session_token = secrets.token_hex(16)
        print(session_token)
        active_session[session_token] = user_id
        response = RedirectResponse(url="/login")
        response.set_cookie(key="session_token", value=session_token, httponly=True, max_age=3600)
        return response
    else:
        return templates.TemplateResponse(
            "login.html",
            {"request": request,
             "error": "Пользователь уже существует с таким именем"}
        )

@app.get("/login")
async def logout():
    response = RedirectResponse(url="/login")
    response.delete_cookie("session_token")
    return response

if __name__ == "__main__":
    uvicorn.run("main:app",
                host="127.0.0.1", port=8000,
                reload=True, reload_dirs=["./static", "./templates"])