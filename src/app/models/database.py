"""
Database athletes
database, connection, session with sqlalchemy to athletes
author: Miguel Herize
mail: migherize@gmail.com
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import app.utils.constants as constants

"""
# connection to DB (orm = SQLAlchemy)
eng = (
    constants.DB
    + "://"
    + constants.USERDB
    + ":"
    + constants.PASSWORDDB
    + "@"
    + constants.NAME_SERVICEDB
    + ":"
    + constants.PORT
    + "/"
    + constants.NAMEDB
)
engine = create_engine(eng)
"""
SQLALCHEMY_DATABASE_URL = "sqlite:///./example.db"
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def get_db():
    """
    conexion database
    """
    database = SessionLocal()
    try:
        yield database
    finally:
        database.close()
