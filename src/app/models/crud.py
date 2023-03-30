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


def create_user(db_conn: Session, spider: schemas.SportsSchema) -> models_db.athletes:
    user = models_db.athletes(
        cedula=spider.id,
        name=spider.name,
        surname=spider.surname,
        sports=spider.sports,
        category=spider.category,
        club=spider.club,
        photo=spider.photo,
    )

    db_conn.add(user)
    db_conn.commit()

    return user


def get_user(
    db_conn: Session, params_filter: str | int, spider_param: str | int
) -> list:
    search = {params_filter: spider_param}
    all_type = db_conn.query(models_db.athletes).filter_by(**search).all()

    if len(all_type) == 0:
        raise HTTPException(status_code=404, detail="Id no encontrado")

    return all_type[0]
