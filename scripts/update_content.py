import os
import random
import requests
from datetime import datetime
from PIL import Image
from io import BytesIO
import re

# 🎮 Frases gamer
FRASES = [
    "El que pausa pierde, ¡siempre fue así!",
    "Subí de nivel solo para perder con estilo.",
    "Tu teclado no tiene suficiente RGB para ganarme.",
    "GG, pero era warm-up.",
    "¡Lag, lo juro!",
    "¿Quién necesita dormir cuando hay raids?",
    "Tu build es tan mala que hasta el jefe se ríe.",
    "No perdí, estaba recolectando datos.",
    "Camper nivel: tienda de campaña.",
    "Apuntar es opcional si usás escopeta."
]

# 📅 Pokémon del día (basado en fecha)
def get_pokemon_del_dia():
    dia_del_ano = datetime.utcnow().timetuple().tm_yday
    pokemon_id = (dia_del_ano % 898) + 1
    return pokemon_id

def get_pokemon_info(pokemon_id):
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}"
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception("No se pudo obtener el Pokémon.")
    data = response.json()
    nombre = data["name"].capitalize()
    imagen_url = data["sprites"]["other"]["official-artwork"]["front_default"]
    return nombre, imagen_url

# 🖼️ Descargar imagen
def descargar_imagen(url, nombre_archivo):
    response = requests.get(url)
    if response.status_code == 200:
        with open(nombre_archivo, "wb") as f:
            f.write(response.content)

# 🖌️ Crear SVG con la imagen descargada
def generar_svg_pokemon(nombre, nombre_archivo_imagen, archivo_salida_svg):
    svg_content = f'''<svg xmlns="http://www.w3.org/2000/svg" width="300" height="300">
  <style>
    .nombre {{
      font: bold 18px sans-serif;
      fill: #333;
    }}
  </style>
  <image href="{nombre_archivo_imagen}" height="200" width="200" x="50" y="20"/>
  <text x="50%" y="260" text-anchor="middle" class="nombre">Pokémon del día: {nombre}</text>
</svg>'''
    with open(archivo_salida_svg, "w", encoding="utf-8") as f:
        f.write(svg_content)

# 📜 Generar frase aleatoria
def generar_frase():
    return random.choice(FRASES)

# ✏️ Reemplazar bloque en el README.md
def actualizar_readme_con_frase(frase):
    with open("README.md", "r", encoding="utf-8") as f:
        contenido = f.read()

    nuevo_contenido = re.sub(
        r'<!-- FRASE_GAMER -->.*?<!-- /FRASE_GAMER -->',
        f'<!-- FRASE_GAMER -->\n🎯 {frase}\n<!-- /FRASE_GAMER -->',
        contenido,
        flags=re.DOTALL
    )

    with open("README.md", "w", encoding="utf-8") as f:
        f.write(nuevo_contenido)

# 🧠 Ejecución principal
def main():
    pokemon_id = get_pokemon_del_dia()
    nombre_pokemon, url_imagen = get_pokemon_info(pokemon_id)

    output_dir = "output"
    os.makedirs(output_dir, exist_ok=True)

    imagen_path = os.path.join(output_dir, "pokemon.png")
    descargar_imagen(url_imagen, imagen_path)

    svg_path = "pokemon-del-dia.svg"
    generar_svg_pokemon(nombre_pokemon, imagen_path, svg_path)

    frase = generar_frase()
    actualizar_readme_con_frase(frase)

    print("✅ Pokémon y frase del día actualizados correctamente.")

if __name__ == "__main__":
    main()
