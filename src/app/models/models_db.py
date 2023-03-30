"""
models to database RecollectionAutomatic
models Recollection Automatic V3
author: Miguel Herize
mail: migherize@gmail.com
"""

from sqlalchemy import Column, Integer, String
from app.models.database import Base


class athletes(Base):
    """
    Tabla de datos de athletes
    """

    __tablename__ = "athletes"
    id = Column(Integer, primary_key=True, autoincrement=True)
    cedula = Column(String(255))
    name = Column(String(255))
    surname = Column(String(255))
    sports = Column(String(255))
    category = Column(String(255))
    club = Column(String(255))
    photo = Column(String(255))
