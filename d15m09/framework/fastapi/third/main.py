from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates # jinja2 устанавливается отдельно
from fastapi.responses import HTMLResponse
import uvicorn

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static") # Подключение папк
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def show_page(request: Request):
    return templates.TemplateResponse("./index.html", {"request": request})

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000,
                reload=True, reload_dirs=["./static", "./templates"])