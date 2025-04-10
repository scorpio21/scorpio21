import random
import requests
from datetime import datetime

# Lista de frases
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
pokemon_number = random.randint(1, 649)  # Hasta generación 5 con animaciones

# Obtener datos del Pokémon desde la PokéAPI
pokemon_data = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon_number}").json()
pokemon_name = pokemon_data['name'].capitalize()
pokemon_types = [t['type']['name'].capitalize() for t in pokemon_data['types']]
pokemon_types_str = ', '.join(pokemon_types)

# URL del GIF animado del Pokémon
pokemon_url = f"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/showdown/{pokemon_number}.gif"

# Descargar GIF
output_path = "output/pokemon.gif"
response = requests.get(pokemon_url)
if response.status_code == 200:
    with open(output_path, "wb") as f:
        f.write(response.content)
else:
    print(f"No se pudo descargar el GIF del Pokémon #{pokemon_number}")

# Actualizar README
with open("README.md", "r", encoding="utf-8") as f:
    contenido = f.read()

# Actualizar la sección del Pokémon
pokemon_section = f"""
### 🐱‍👤 Pokémon del día

![Pokémon del día](https://raw.githubusercontent.com/scorpio21/scorpio21/main/output/pokemon.gif)

**Nombre:** {pokemon_name}  
**Tipo(s):** {pokemon_types_str}
"""
contenido = contenido.split("<!-- POKEMON_INFO -->")[0] + \
    f"<!-- POKEMON_INFO -->\n{pokemon_section}\n<!-- /POKEMON_INFO -->" + \
    contenido.split("<!-- /POKEMON_INFO -->")[1]

# Actualizar la frase gamer
contenido = contenido.split("<!-- FRASE_GAMER -->")[0] + \
    f"<!-- FRASE_GAMER -->\n🕹️ {frase}\n<!-- /FRASE_GAMER -->" + \
    contenido.split("<!-- /FRASE_GAMER -->")[1]

# Actualizar la marca de tiempo
ahora = datetime.now().isoformat()
contenido = "\n".join([
    line if not line.strip().startswith("<!-- Última actualización:") else f"<!-- Última actualización: {ahora} -->"
    for line in contenido.splitlines()
])

# Escribir cambios
with open("README.md", "w", encoding="utf-8") as f:
    f.write(contenido)
