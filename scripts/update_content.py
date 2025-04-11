import os
import random
import requests
from github import Github
from datetime import datetime

# Obtener el token de la variable de entorno GH_TOKEN
g = Github(os.getenv("GH_TOKEN"))

# Frases graciosas estilo gamer
frases = [
    "¡No campees, enfrentá como gamer!",
    "Ganás experiencia hasta cuando perdés.",
    "Respawneá con más ganas.",
    "¿Lag? Nah, habilidad pura.",
    "Un día sin bugs es un milagro.",
    "Guardá antes de probar algo loco.",
    "Jugá como si fuera tu última vida.",
    "AFK solo si es urgente 😎",
    "Todo gamer sabe: primero looteás, después pensás.",
    "Subí de nivel hasta en la vida real."
]

# Elegir Pokémon aleatorio
pokemon_id = random.randint(1, 649)
pokemon_api_url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}"
response = requests.get(pokemon_api_url)

if response.status_code == 200:
    data = response.json()
    nombre = data["name"].capitalize()
    tipos = ", ".join([t["type"]["name"].capitalize() for t in data["types"] if "type" in t])
    pokemon_img_url = data["sprites"]["front_default"]
    clasificacion = data["species"]["name"].capitalize()
    num_pokedex = data["id"]
else:
    nombre = "Desconocido"
    tipos = "???"
    pokemon_img_url = ""
    clasificacion = "???"
    num_pokedex = "???"

# Descargar GIF del Pokémon
pokemon_gif_url = f"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/{pokemon_id}.gif"
output_path = "output/pokemon.gif"
gif_response = requests.get(pokemon_gif_url)
if gif_response.status_code == 200:
    with open(output_path, "wb") as f:
        f.write(gif_response.content)
else:
    print(f"❌ No se pudo descargar el GIF del Pokémon #{pokemon_id}")

# Elegir una frase aleatoria
frase = random.choice(frases)

# Leer README actual
repo = g.get_repo("scorpio21/scorpio21")
readme_file = repo.get_contents("README.md")
contenido = readme_file.decoded_content.decode("utf-8")

# Si no existen las etiquetas, agregarlas
if "<!-- POKEMON_INFO -->" not in contenido:
    contenido = contenido.split("<!-- END_POKEMON_INFO -->")[0] + "<!-- POKEMON_INFO -->\n<!-- END_POKEMON_INFO -->" + contenido.split("<!-- END_POKEMON_INFO -->")[1]

# Actualizar bloque POKEMON_INFO con la nueva tabla
bloque_pokemon = f"""<!-- POKEMON_INFO -->
| Imagen | Nombre | Tipo(s) | Clase | Número de Pokédex |
|:-:|:-:|:-:|:-:|:-:|
| ![Pokémon del día]({pokemon_gif_url}) | **{nombre}** | {tipos} | {clasificacion} | {num_pokedex} |
<!-- END_POKEMON_INFO -->"""

contenido = contenido.split("<!-- POKEMON_INFO -->")[0] + bloque_pokemon + contenido.split("<!-- END_POKEMON_INFO -->")[1]

# Actualizar la frase gamer
contenido = contenido.split("<!-- FRASE_GAMER -->")[0] + \
    f"<!-- FRASE_GAMER -->\n🕹️ {frase}\n<!-- END_FRASE_GAMER -->" + \
    contenido.split("<!-- END_FRASE_GAMER -->")[1]

# Marcar hora de última actualización
ahora = datetime.now().isoformat()
contenido = "\n".join([ 
    line if not line.strip().startswith("<!-- Última actualización:") else f"<!-- Última actualización: {ahora} -->" 
    for line in contenido.splitlines() 
])

# Subir cambios al repositorio
repo.update_file(
    path="README.md",
    message="🔁 Actualización diaria automática: Pokémon y frase gamer",
    content=contenido,
    sha=readme_file.sha
)

print("¡README actualizado con éxito!")
