import pandas as pd
import os
import requests

info = os.path.join(os.getcwd(), "data", "user_ingenieria.csv")
df = pd.read_csv(info)
bandera = True
cabeceras_endpoint = {"accept": "application/json", "Content-Type": "application/json"}

data = df

duplicados = df.duplicated(subset=["id", "version"])
for indice, elemento in duplicados.items():
    if elemento:
        print(f"Índice: {indice}, Elemento: {elemento}")
        bandera = False

print(data.columns)
print(data)
data[["name", "surname"]] = df["Nombre"].str.split(expand=True)
data.drop("Nombre", axis=1, inplace=True)

data["sports"] = data["sports"].str.upper()
data["name"] = data["name"].str.upper()
data["surname"] = data["surname"].str.upper()
data["category"] = data["category"].str.upper()
data["club"] = data["club"].str.upper()
data["tipo"] = data["tipo"].str.upper()

if bandera:
    for i, j in data.iterrows():
        dict_fila = df.iloc[i].to_dict()
        # print(dict_fila)
        dict_fila["qr"] = dict_fila["id"]
        dict_fila["photo"] = dict_fila["id"]

        response = requests.post(
            "http://127.0.0.1:8000/insert/athletes/",
            headers=cabeceras_endpoint,
            json=dict_fila,
        )
        print(response.status_code)
