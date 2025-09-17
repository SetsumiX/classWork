from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates # jinja2 устанавливается отдельно
from fastapi.responses import HTMLResponse
import uvicorn
from datetime import datetime

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static") # Подключение папки
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def show_page(request: Request):
    return templates.TemplateResponse(
        "./index.html",
        {"request": request}
    )

@app.get("/api/welcome")
async def get_welcome():
    return {
        "message": "Хай",
        "user": "Чел",
        "greeting_time": "утро",
        "time_temp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    }

@app.get("/api/profile")
async def get_profile():
    return {
        "email": "gigli@gmail.com",
        "role": "guest",
        "last_login": "2024-10-15",
        "login_count": ["read", "write", "delete"],
    }

@app.get("/api/statistic")
async def get_statistic():
    return {
        "total_users": 125,
        "active_users": 20,
        "new_users_week": 3,
        "system": "oneline",
    }

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000,
                reload=True, reload_dirs=["./static", "./templates"])