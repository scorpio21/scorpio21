import os
import requests


def download_cry(cry_url):
    if not cry_url:
        return

    os.makedirs("cries", exist_ok=True)

    response = requests.get(cry_url, timeout=30)

    if response.status_code == 200:
        with open("cries/cry.ogg", "wb") as f:
            f.write(response.content)

        print("Cry descargado correctamente.")
    else:
        print("No se pudo descargar el cry.")