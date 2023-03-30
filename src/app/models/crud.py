"""
Create, Read, Update, and Delete to database Sports
crud database Sports
author: Miguel Herize
mail: migherize@gmail.com
"""
from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.models import models_db
from app.schemas import schemas
import app.utils.constants as constants


def create_user(db_conn: Session, player: schemas.SportsSchema) -> models_db.athletes:
    user = models_db.athletes(
        cedula=player.id,
        name=player.name,
        surname=player.surname,
        sports=player.sports,
        category=player.category,
        club=player.club,
        photo=player.photo,
        qr=player.qr,
        tipo=player.tipo,
        version=player.version,
    )

    db_conn.add(user)
    db_conn.commit()

    return user


def get_user(
    db_conn: Session, params_filter: str | int, player_param: str | int, version:str
) -> list:
    search = {params_filter: player_param}
    search["version"] = version
    all_type = db_conn.query(models_db.athletes).filter_by(**search).all()

    if len(all_type) == 0:
        raise HTTPException(status_code=404, detail="Id no encontrado")

    return all_type[0]
