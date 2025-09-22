from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
import uvicorn

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

todos = []

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "todos": todos})

@app.get("/todos")
async def add_todos():
    return {"todos": todos}

@app.post("/todos")
async def add_todo(todo_id: dict):
    todos.append({"id": len(todos)+1, "task": todo_id["task"]})
    return {"message": "Задача добавлена"}

@app.delete("/todos/{todo_id}")
async def delete(todo_id: int):
    global todos
    todos = [t for t in todos if t["id"] != todo_id]

if __name__ == "__main__":
    uvicorn.run("main:app",
                host="127.0.0.1", port=8000,
                reload=True, reload_dirs=["./static", "./templates"])