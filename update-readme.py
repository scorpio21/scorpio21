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
pokemon_number = random.randint(1, 649)  # Hasta generación 5 con animaciones
pokemon_url = f"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/animated/{pokemon_number}.gif"

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

# Actualizar la frase
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
