from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates # jinja2 устанавливается отдельно
from fastapi.responses import HTMLResponse
import uvicorn

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static") # Подключение папки
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def show_page(request: Request):
    data = {
        "message": "Greeting!",
        "user": "Mate"
    }
    return templates.TemplateResponse(
        "./index.html",
        {
            "request": request,
            "data": data
        }
    )

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000,
                reload=True, reload_dirs=["./static", "./templates"])