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
    # Agregar más información (Clase y número de Pokédex)
    pokemon_clase = data["species"]["name"].capitalize()
    numero_pokedex = data["id"]
    pokemon_img_url = data["sprites"]["front_default"]
else:
    nombre = "Desconocido"
    tipos = "???"
    pokemon_clase = "???"
    numero_pokedex = "???"
    pokemon_img_url = ""

frase = random.choice(frases)

# Descargar GIF
pokemon_gif_url = "https://raw.githubusercontent.com/scorpio21/scorpio21/main/output/pokemon.gif"
output_path = "output/pokemon.gif"
gif_response = requests.get(pokemon_gif_url)
if gif_response.status_code == 200:
    with open(output_path, "wb") as f:
        f.write(gif_response.content)
else:
    print(f"❌ No se pudo descargar el GIF del Pokémon #{pokemon_id}")

# Leer README actual
with open("README.md", "r", encoding="utf-8") as f:
    contenido = f.read()

# Si no existen las etiquetas, agregarlas
if "<!-- POKEMON_INFO -->" not in contenido:
    contenido = contenido.split("<!-- END_POKEMON_INFO -->")[0] + "<!-- POKEMON_INFO -->\n<!-- END_POKEMON_INFO -->" + contenido.split("<!-- END_POKEMON_INFO -->")[1]

# Actualizar bloque POKEMON_INFO con tabla bien formateada
bloque_pokemon = f"""<!-- POKEMON_INFO -->
| Imagen | Nombre | Tipo(s) | Clase | Número de Pokédex |
|:-:|:-:|:-:|:-:|:-:|
| ![Pokémon del día]({pokemon_gif_url}) | **{nombre}** | {tipos} | {pokemon_clase} | {numero_pokedex} |
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

# Guardar cambios
with open("README.md", "w", encoding="utf-8") as f:
    f.write(contenido)
