from PIL import Image, ImageDraw, ImageFont
import os


def save(user: dict, fondo: str):
    # Ruta de imagenes
    os.chdir("../")
    path_new_home = os.getcwd()
    static_path = os.path.join(path_new_home, "static", fondo)
    save_img = os.path.join(path_new_home, "static", "credenciales")
    perfil = os.path.join(path_new_home, "static", "photo", f"{user['id']}.jpg")
    qr = os.path.join(path_new_home, "static", "QR", f"{user['id']}.jpg")

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
    image.save(os.path.join(save_img, f"{Cedula}_{user['version']}.png"))


user = {
    "id": "28440356",
    "sports": "KIKIMBOL",
    "category": "FEMENINO",
    "tipo": "ATLETA",
    "version": 0,
    "name": "ROXANA ",
    "surname": "SULBARAN",
    "qr": "25.832.303",
    "photo": "25.832.303",
}

fondo = "credencial_atleta.png"
save(user, fondo)
