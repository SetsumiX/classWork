from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates # jinja2 устанавливается отдельно
import uvicorn

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static") # Подключение папки

templates = Jinja2Templates(directory="templates")

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/page")
def show_page(request: Request):
    return templates.TemplateResponse("./index.html", {"request": request})

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000, reload=True, reload_dirs=["./static", "./templates"])