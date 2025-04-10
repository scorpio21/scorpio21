import random
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

frase = random.choice(frases)
ahora = datetime.now().isoformat()

with open("README.md", "r", encoding="utf-8") as f:
    contenido = f.read()

nuevo_contenido = contenido
nuevo_contenido = nuevo_contenido.split("<!-- FRASE_GAMER -->")[0] + \
    f"<!-- FRASE_GAMER -->\n🕹️ {frase}\n<!-- /FRASE_GAMER -->" + \
    contenido.split("<!-- /FRASE_GAMER -->")[1]

# Reemplaza la línea de última actualización si existe
nuevo_contenido = "\n".join([
    line if not line.strip().startswith("<!-- Última actualización:") else f"<!-- Última actualización: {ahora} -->"
    for line in nuevo_contenido.splitlines()
])

with open("README.md", "w", encoding="utf-8") as f:
    f.write(nuevo_contenido)
