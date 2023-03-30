import os
import qrcode

static_path = os.path.join(os.getcwd(), "app", "QR")


def create_QR(url: str, id: str):
    """
    funcion para guardar el qr en la carpeta QR
    """
    img = qrcode.make(url)
    img.save(os.path.join(static_path, f"{id}.png"))
