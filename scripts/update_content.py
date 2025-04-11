import os
from github import Github
import random
import requests
from bs4 import BeautifulSoup

# Usamos el token de GitHub
token = os.getenv("GH_TOKEN")  # Asegúrate de que el token esté en los secretos de GitHub Actions
g = Github(token)

# Obtener el repositorio
repo = g.get_repo("scorpio21/scorpio21")
print(f"Repositorio: {repo.name}")  # Verificar el nombre del repositorio

try:
    # Intentar obtener el archivo README.md
    readme_file = repo.get_contents("README.md")
    print(f"Archivo encontrado: {readme_file.name}")
    contenido = readme_file.decoded_content.decode("utf-8")
    print("Contenido del archivo cargado correctamente.")
except Exception as e:
    print(f"Error al obtener el archivo README.md: {str(e)}")
    exit(1)  # Terminar el script si no se puede obtener el archivo

# Aquí deberías seguir con el código para obtener el Pokémon del día y la frase gamer

# Obtener el Pokémon del día (ejemplo)
pokemon_id = random.randint(1, 898)  # Número aleatorio para el Pokémon (puedes ajustar el rango)
pokemon_url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}"

try:
    response = requests.get(pokemon_url)
    response.raise_for_status()
    pokemon_data = response.json()

    # Obtener los detalles del Pokémon
    pokemon_name = pokemon_data["name"].capitalize()
    pokemon_types = [type_data["type"]["name"] for type_data in pokemon_data["types"]]
    pokemon_types_str = ", ".join(pokemon_types)
    pokemon_image_url = pokemon_data["sprites"]["other"]["official-artwork"]["front_default"]

    # Descargar el GIF del Pokémon
    gif_response = requests.get(pokemon_image_url)
    if gif_response.status_code != 200:
        print(f"❌ No se pudo descargar el GIF del Pokémon #{pokemon_id}")
        pokemon_image_url = ""  # Asigna una imagen vacía si no se puede descargar
except Exception as e:
    print(f"Error al obtener el Pokémon: {str(e)}")
    pokemon_image_url = ""

# Aquí puedes actualizar la frase gamer (esto es solo un ejemplo)
frase_gamer = "¡Atrévete a ser el mejor!"

# Reemplazar el contenido en el README.md
contenido = contenido.replace("<!-- POKEMON_INFO -->", f"""
| Imagen | Nombre | Tipo(s) |
|--------|--------|---------|
| ![Pokémon]( {pokemon_image_url} ) | {pokemon_name} | {pokemon_types_str} |
""")

contenido = contenido.replace("<!-- FRASE_GAMER -->", f"**Frase gamer del día:** {frase_gamer}")

# Subir el archivo actualizado al repositorio
try:
    repo.update_file(
        path="README.md",
        message="🔁 Actualización diaria automática: Pokémon y frase gamer",
        content=contenido,
        sha=readme_file.sha
    )
    print("README.md actualizado correctamente")
except Exception as e:
    print(f"Error al actualizar el archivo README.md: {str(e)}")
    exit(1)  # Terminar el script si no se puede actualizar el archivo
