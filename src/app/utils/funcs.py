import os
import qrcode
from app.utils import constants

static_path = os.path.join(os.getcwd(), "app", "static")


def create_QR(id: str, version:str, path: str):
    path_QR = os.path.join(static_path, path)
    """
    funcion para guardar el qr en la carpeta QR
    """
    img = qrcode.make(constants.host + id + "/" + version)
    img.save(os.path.join(path_QR, f"{id}.jpg"))


def get_img(id: str, path: str):
    path_img = os.path.join(static_path, path)
    for archivo in os.listdir(path_img):
        ruta_archivo = os.path.join(path_img, archivo)
        if os.path.isfile(ruta_archivo) and id in archivo:
            print("Se encontró la imagen:", ruta_archivo)
            return archivo
    print("No se encontró la imagen")
    return None
