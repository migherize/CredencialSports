import os
import requests
import pandas as pd
from PIL import Image, ImageDraw, ImageFont


def save_credencial(user: dict, fondo: str):
    # Ruta de imagenes
    path_home = os.getcwd()
    os.chdir("../..")
    path_new_home = os.getcwd()
    static_path = os.path.join(path_new_home, "app", "static", fondo)
    save_img = os.path.join(path_new_home, "app", "static", "credenciales")
    perfil = os.path.join(path_new_home, "app", "static", "photo", f"{user['id']}.jpg")
    qr = os.path.join(path_new_home, "app", "static", "QR", f"{user['id']}.jpg")
    # Volvemos a la ruta inicial
    os.chdir(path_home)

    # Abre la imagen
    image = Image.open(static_path)
    width = 1122
    height = 1476
    new_size = (width, height)
    image.resize(new_size)

    # Foto perfil
    foreground_img = Image.open(perfil)
    new_size = (320, 420)  # especifica el nuevo tamaño que deseas
    perfil = foreground_img.resize(new_size)

    # Crea un objeto de dibujo
    draw = ImageDraw.Draw(image)

    # Foto perfil
    foreground_qr = Image.open(qr)
    new_size = (400, 420)  # especifica el nuevo tamaño que deseas
    img_qr = foreground_qr.resize(new_size)

    # Especifica la posición donde se agregará el texto
    pos_nombre = (150, 810)
    pos_apellido = (150, 970)
    pos_Cedula = (150, 1130)
    pos_disciplina = (150, 1290)
    pos_categoria = (150, 1460)

    pos_img = (790, 120)
    pos_qr = (750, 1190)

    # Especifica el texto y la fuente
    nombre = user["name"]
    apellido = user["surname"]
    Cedula = user["id"]
    disciplina = user["sports"]
    categoria = user["category"]

    fuente = ImageFont.truetype("/Library/Fonts/Arial.ttf", size=50)

    # Agrega el texto a la imagen
    draw.text(pos_nombre, nombre, font=fuente, fill=(0, 0, 0))
    draw.text(pos_apellido, apellido, font=fuente, fill=(0, 0, 0))
    draw.text(pos_Cedula, Cedula, font=fuente, fill=(0, 0, 0))
    draw.text(pos_disciplina, disciplina, font=fuente, fill=(0, 0, 0))
    draw.text(pos_categoria, categoria, font=fuente, fill=(0, 0, 0))
    image.paste(perfil, pos_img)
    image.paste(img_qr, pos_qr)
    # Guarda la imagen modificada
    image.save(os.path.join(save_img, f"{Cedula}.png"))


def get_img(id: str, path: str):
    path_home = os.getcwd()
    os.chdir("../..")
    path_new_home = os.getcwd()
    static_path = os.path.join(path_new_home, "app", "static")
    os.chdir(path_home)
    path_img = os.path.join(static_path, path)
    for archivo in os.listdir(path_img):
        ruta_archivo = os.path.join(path_img, archivo)
        if os.path.isfile(ruta_archivo) and id in archivo:
            return archivo
    print("No se encontró la imagen")
    return None


def valid():
    info = os.path.join(os.getcwd(), "data", "user_ingenieria.csv")
    df = pd.read_csv(info)
    bandera = True

    data = df

    duplicados = df.duplicated(subset=["id", "version"])
    for indice, elemento in duplicados.items():
        if elemento:
            print(f"Índice: {indice}, Elemento: {elemento}")
            bandera = False

    data[["name", "surname"]] = df["Nombre"].str.split(expand=True)
    data.drop("Nombre", axis=1, inplace=True)

    data["sports"] = data["sports"].str.upper()
    data["name"] = data["name"].str.upper()
    data["surname"] = data["surname"].str.upper()
    data["category"] = data["category"].str.upper()
    data["club"] = data["club"].str.upper()
    data["tipo"] = data["tipo"].str.upper()

    return bandera, data


def insert_data(bandera, data):
    cabeceras_endpoint = {
        "accept": "application/json",
        "Content-Type": "application/json",
    }
    if bandera:
        for i, j in data.iterrows():
            dict_fila = data.iloc[i].to_dict()
            # print(dict_fila)
            dict_fila["qr"] = dict_fila["id"]
            dict_fila["photo"] = dict_fila["id"]

            response = requests.post(
                "http://127.0.0.1:8000/insert/athletes/",
                headers=cabeceras_endpoint,
                json=dict_fila,
            )
            print(response.status_code)


def save(data):
    for i, j in data.iterrows():
        dict_fila = data.iloc[i].to_dict()
        img_qr = get_img(dict_fila["id"], "QR")
        photo = get_img(dict_fila["id"], "photo")
        dict_fila["qr"] = img_qr
        dict_fila["photo"] = photo
        if dict_fila["tipo"] == "ATLETA":
            fondo = "credencial_atleta.png"
            save_credencial(dict_fila, fondo)

        elif dict_fila["tipo"] == "DELEGADO":
            fondo = "credencial_tecnico.png"
            save_credencial(dict_fila, fondo)


if __name__ == "__main__":
    bandera, data = valid()
    # insert_data(bandera, data)
    save(data)
