"""
class pydantic to models athletes
models athletes
author: Miguel Herize
mail: migherize@gmail.com
"""

from pydantic import BaseModel
import app.utils.constants as constants


class SportsSchema(BaseModel):
    id: str
    name: str
    surname: str
    sports: str
    category: str
    club: str
    photo: str

    class Config:
        """
        Ejemplo para el modelo de InputRecollection y para swagger FastApi
        """

        schema_extra = {"example": constants.DICT_EXAMPLE}
