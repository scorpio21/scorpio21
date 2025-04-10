import random
import requests
from datetime import datetime

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

# Elegir frase y Pokémon aleatorio
frase = random.choice(frases)
pokemon_number = random.randint(1, 649)

# Descargar imagen GIF
gif_url = f"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/animated/{pokemon_number}.gif"
response = requests.get(gif_url)
if response.status_code == 200:
    with open("output/pokemon.gif", "wb") as f:
        f.write(response.content)

# Obtener nombre y tipo desde la API
pokeapi_url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_number}"
poke_response = requests.get(pokeapi_url)
if poke_response.status_code == 200:
    data = poke_response.json()
    nombre = data["name"].capitalize()
    tipos = ", ".join(t["type"]["name"].capitalize() for t in data["types"])
else:
    nombre = "Desconocido"
    tipos = "Desconocido"

# Crear tabla Markdown
tabla_markdown = f"""<!-- POKEMON_INFO -->
| ![Pokémon del día](https://raw.githubusercontent.com/scorpio21/scorpio21/main/output/pokemon.gif) | **{nombre}** | {tipos} |
|:-:|:-:|:-:|
<!-- /POKEMON_INFO -->"""

# Leer README
with open("README.md", "r", encoding="utf-8") as f:
    contenido = f.read()

# Reemplazar la tabla Pokémon
if "<!-- POKEMON_INFO -->" in contenido and "<!-- /POKEMON_INFO -->" in contenido:
    antes = contenido.split("<!-- POKEMON_INFO -->")[0]
    despues = contenido.split("<!-- /POKEMON_INFO -->")[1]
    contenido = antes + tabla_markdown + despues
else:
    print("No se encontraron las marcas <!-- POKEMON_INFO --> en el README.")

# Reemplazar frase gamer
contenido = contenido.split("<!-- FRASE_GAMER -->")[0] + \
    f"<!-- FRASE_GAMER -->\n🕹️ {frase}\n<!-- /FRASE_GAMER -->" + \
    contenido.split("<!-- /FRASE_GAMER -->")[1]

# Timestamp
ahora = datetime.now().isoformat()
contenido = "\n".join([
    line if not line.strip().startswith("<!-- Última actualización:") else f"<!-- Última actualización: {ahora} -->"
    for line in contenido.splitlines()
])

# Guardar README actualizado
with open("README.md", "w", encoding="utf-8") as f:
    f.write(contenido)
