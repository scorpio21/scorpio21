import requests
import random
import re

def obtener_pokemon_aleatorio():
    pokemon_id = random.randint(1, 898)
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}"
    respuesta = requests.get(url)
    datos = respuesta.json()

    nombre = datos["name"].capitalize()
    tipos = [t["type"]["name"].capitalize() for t in datos["types"]]
    tipos_es = ", ".join([traducir_tipo(t) for t in tipos])
    clase = obtener_clase_pokemon(pokemon_id)

    sprite_url = datos["sprites"]["versions"]["generation-v"]["black-white"]["animated"]["front_default"]
    if sprite_url is None:
        sprite_url = datos["sprites"]["front_default"]

    return nombre, tipos_es, clase, sprite_url

def traducir_tipo(tipo):
    traducciones = {
        "Normal": "Normal", "Fire": "Fuego", "Water": "Agua", "Electric": "Eléctrico",
        "Grass": "Planta", "Ice": "Hielo", "Fighting": "Lucha", "Poison": "Veneno",
        "Ground": "Tierra", "Flying": "Volador", "Psychic": "Psíquico", "Bug": "Bicho",
        "Rock": "Roca", "Ghost": "Fantasma", "Dragon": "Dragón", "Dark": "Siniestro",
        "Steel": "Acero", "Fairy": "Hada"
    }
    return traducciones.get(tipo, tipo)

def obtener_clase_pokemon(pokemon_id):
    url = f"https://pokeapi.co/api/v2/pokemon-species/{pokemon_id}"
    respuesta = requests.get(url)
    datos = respuesta.json()
    for entry in datos["genera"]:
        if entry["language"]["name"] == "es":
            return entry["genus"]
    return "Desconocida"

def obtener_frase_gamer():
    frases = [
        "¡No campees tanto, que pareces una tienda de campaña!",
        "AFK pero en espíritu sigo presente.",
        "Nivel bajo, pero moral alta.",
        "Ese lag fue emocional.",
        "Game over, pero con estilo.",
        "¡Recargando... pero mi vida también!",
        "No soy noob, estoy en fase de aprendizaje."
    ]
    return random.choice(frases)

# Obtener datos del Pokémon
nombre, tipos_es, clase, imagen_url = obtener_pokemon_aleatorio()
frase_gamer = obtener_frase_gamer()

# Leer README
with open("README.md", "r", encoding="utf-8") as f:
    contenido = f.read()

# Bloque del Pokémon del día
pokemon_info_block = f"""<!-- POKEMON_INFO -->
## 🐱‍👤 Pokémon del día

| Imagen | Nombre | Tipo(s) | Clase |
|:------:|:------:|:-------:|:-----:|
| ![Pokémon del día]({imagen_url}) | **{nombre}** | {tipos_es} | {clase} |
<!-- END_POKEMON_INFO -->"""

# Bloque de la frase gamer del día
frase_gamer_block = f"""<!-- FRASE_GAMER -->
## 🎮 Frase gamer del día

🗯️ *{frase_gamer}*
<!-- END_FRASE_GAMER -->"""

# Reemplazo en el contenido
contenido = re.sub(r"<!-- POKEMON_INFO -->.*<!-- END_POKEMON_INFO -->", pokemon_info_block, contenido, flags=re.DOTALL)
contenido = re.sub(r"<!-- FRASE_GAMER -->.*<!-- END_FRASE_GAMER -->", frase_gamer_block, contenido, flags=re.DOTALL)

# Guardar README actualizado
with open("README.md", "w", encoding="utf-8") as f:
    f.write(contenido)
