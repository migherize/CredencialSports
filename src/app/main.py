"""
main Credenciales Enlace Sports
Router General
author: Miguel Herize
mail: migherize@gmail.com
"""

from fastapi import FastAPI
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


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
