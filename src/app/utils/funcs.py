import os
import qrcode
from app.utils import constants

static_path = os.path.join(os.getcwd(), "app", "static", "QR")


def create_QR(id: str):
    """
    funcion para guardar el qr en la carpeta QR
    """
    img = qrcode.make(constants.host + id)
    img.save(os.path.join(static_path, f"{id}.png"))


def get_QR(id: str):
    for archivo in os.listdir(static_path):
        ruta_archivo = os.path.join(static_path, archivo)
        if os.path.isfile(ruta_archivo) and id in archivo:
            print("Se encontró la imagen:", ruta_archivo)
            return archivo
    print("No se encontró la imagen")
    return None
