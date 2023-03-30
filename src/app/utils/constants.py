"""
constants to Credencial Sports
File for the entire service to configure and constants
author: Miguel Herize
mail: migherize@gmail.com
"""
import os
from dotenv import load_dotenv

# Cargar .env
load_dotenv()
PATH_HOME = os.getcwd()

# Leer variables de entorno
DB = os.getenv("DB")
USERDB = os.getenv("userDB")
PASSWORDDB = os.getenv("passwordDB")
NAME_SERVICEDB = os.getenv("name_serviceDB")
NAMEDB = os.getenv("nameBD")
PORT = os.getenv("port")

host = "http://127.0.0.1:8000/credencial/"
DICT_EXAMPLE = {
    "id": "12.345.678",
    "name": "Peter",
    "surname": "Parker",
    "sports": "Futbol",
    "category": "Adulto",
    "club": "Avengers",
    "photo": "grupo_futbol.jpg",
}
