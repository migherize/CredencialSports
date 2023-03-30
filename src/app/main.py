"""
main Credenciales Enlace Sports
Router General
author: Miguel Herize
mail: migherize@gmail.com
"""
import os
import json
from fastapi import FastAPI, Depends, Body, status, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from jinja2 import Environment, FileSystemLoader
from sqlalchemy.orm import Session
from app.schemas import schemas
from app.models import models_db, database, crud
from app.utils import constants, funcs
from app.models.database import Base, engine

app = FastAPI()
static_path = os.path.join(os.getcwd(), "app", "static")
app.mount("/static", StaticFiles(directory=static_path), name="static")

path_template = os.path.join(os.getcwd(), "app", "templates")
templates = Jinja2Templates(directory=path_template)

env = Environment(loader=FileSystemLoader("templates"))
# Crear tablas
Base.metadata.create_all(bind=engine)


@app.get("/credencial/{id}/{version}")
async def home(id: str, version: str, db_conn: Session = Depends(database.get_db)):
    template = templates.get_template("home.html")
    db_all = crud.get_user(db_conn, "cedula", id, version)
    # img_qr = funcs.get_QR(db_all.cedula)
    img_qr = funcs.get_img(db_all.cedula, "QR")
    photo = funcs.get_img(db_all.cedula, "photo")

    if db_all.tipo == "ATLETA":
        fondo = "credencial_atleta"
    
    elif db_all.tipo == "DELEGADO":
        fondo = "credencial_tecnico"

    user = {
        "name": db_all.name,
        "surname": db_all.surname,
        "id": db_all.cedula,
        "sports": db_all.sports,
        "category": db_all.category,
        "club": db_all.club,
        "photo": photo,
        "tipo": db_all.tipo,
        "img_qr": img_qr,
        "fondo": fondo,
    }
    content = template.render(user=user)
    return HTMLResponse(content=content)


@app.post("/insert/athletes/", status_code=status.HTTP_201_CREATED)
async def insert_athletes(
    input: schemas.SportsSchema = Body(), db_conn: Session = Depends(database.get_db)
) -> dict:
    try:
        db_item = crud.create_user(db_conn, input)
        funcs.create_QR(db_item.cedula, db_item.version, "QR")

        if db_item:
            return {"message": f"{db_item.cedula} Insertado"}

    except Exception as exc:
        raise HTTPException(
            status_code=400,
            detail=json.dumps({"error": str(exc)}),
        ) from exc
