"""
main Credenciales Enlace Sports
Router General
author: Miguel Herize
mail: migherize@gmail.com
"""
import os
from fastapi import FastAPI, Request
from sqlalchemy import create_engine, text
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from jinja2 import Environment, FileSystemLoader

app = FastAPI()
static_path = os.path.join(os.getcwd(), "app", "static")
app.mount("/static", StaticFiles(directory=static_path), name="static")

path_template = os.path.join(os.getcwd(), "app", "templates")
templates = Jinja2Templates(directory=path_template)

env = Environment(loader=FileSystemLoader("templates"))


@app.get("/credencial/{id}")
async def home():
    template = templates.get_template("home.html")
    user = {
        "id": "Miguel",
        "name": "Herize",
        "surname": "25.832.303",
        "sports": "Ajedrez",
        "category": "Individual",
        "club": "INGENIERIA",
        "photo": "25832303.jpg",
    }
    content = template.render(user=user)
    return HTMLResponse(content=content)
