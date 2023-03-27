"""
main Credenciales Enlace Sports
Router General
author: Miguel Herize
mail: migherize@gmail.com
"""
import os
from fastapi import FastAPI
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from typing import Union


app = FastAPI()
"""(
    title="My API",
    description="API description",
    version="1.0.0",
    openapi_url="/api/v1/openapi.json",
    docs_url="/docs",
    redoc_url="/redoc",
    servers=[{"url": "https://credencial-lo-sports.onrender.com"}],
)
"""
static_path = os.path.join(os.getcwd(), "app", "static")
print("static_path", static_path)
app.mount("/static", StaticFiles(directory=static_path), name="static")


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/credencial", response_class=HTMLResponse)
def credencial():
    return FileResponse("app/index.html")


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
