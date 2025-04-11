import random
import requests
from datetime import datetime

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

# Elegir Pokémon y frase aleatoria
pokemon_id = random.randint(1, 649)
pokemon_api_url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}"
response = requests.get(pokemon_api_url)

if response.status_code == 200:
    data = response.json()
    nombre = data["name"].capitalize()
    tipos = ", ".join([t["type"]["name"].capitalize() for t in data["types"] if "type" in t])
    # Usamos el sprite frontal estático (siempre correcto)
    pokemon_img_url = data["sprites"]["front_default"]
else:
    nombre = "Desconocido"
    tipos = "???"
    pokemon_img_url = ""

frase = random.choice(frases)

# Descargar GIF
output_path = "output/pokemon.gif"
gif_response = requests.get(pokemon_gif_url)
if gif_response.status_code == 200:
    with open(output_path, "wb") as f:
        f.write(gif_response.content)
else:
    print(f"❌ No se pudo descargar el GIF del Pokémon #{pokemon_id}")

# Obtener datos del Pokémon desde la API
response = requests.get(pokemon_api_url)
if response.status_code == 200:
    data = response.json()
    nombre = data["name"].capitalize()
    tipos = ", ".join([t["type"]["name"].capitalize() for t in data["types"]])
else:
    nombre = "Desconocido"
    tipos = "???"

# Leer README actual
with open("README.md", "r", encoding="utf-8") as f:
    contenido = f.read()

# Actualizar bloque POKEMON_INFO con tabla bien formateada
bloque_pokemon = f"""<!-- POKEMON_INFO -->
| Imagen | Nombre | Tipo |
|:-:|:-:|:-:|
| ![Pokémon del día](https://raw.githubusercontent.com/scorpio21/scorpio21/main/output/pokemon.gif) | **{nombre}** | {tipos} |
<!-- /POKEMON_INFO -->"""

contenido = contenido.split("<!-- POKEMON_INFO -->")[0] + bloque_pokemon + contenido.split("<!-- /POKEMON_INFO -->")[1]

# Actualizar la frase gamer
contenido = contenido.split("<!-- FRASE_GAMER -->")[0] + \
    f"<!-- FRASE_GAMER -->\n🕹️ {frase}\n<!-- /FRASE_GAMER -->" + \
    contenido.split("<!-- /FRASE_GAMER -->")[1]

# Marcar hora de última actualización
ahora = datetime.now().isoformat()
contenido = "\n".join([
    line if not line.strip().startswith("<!-- Última actualización:") else f"<!-- Última actualización: {ahora} -->"
    for line in contenido.splitlines()
])

# Guardar cambios
with open("README.md", "w", encoding="utf-8") as f:
    f.write(contenido)
