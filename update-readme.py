import requests
import random
import re

README_PATH = "README.md"

# Diccionario de tipos traducidos
tipos_traducidos = {
    "normal": "Normal", "fire": "Fuego", "water": "Agua", "electric": "Eléctrico",
    "grass": "Planta", "ice": "Hielo", "fighting": "Lucha", "poison": "Veneno",
    "ground": "Tierra", "flying": "Volador", "psychic": "Psíquico", "bug": "Bicho",
    "rock": "Roca", "ghost": "Fantasma", "dragon": "Dragón", "dark": "Siniestro",
    "steel": "Acero", "fairy": "Hada"
}

# Lista de frases gamer graciosas
frases_gamer = [
    "🌟 ¡Hoy es un buen día para farmear!", 
    "🎮 ¿Guardar partida? ¡Siempre!", 
    "👾 ¡Press F para respetar!", 
    "💥 ¡Critico super efectivo!", 
    "🧠 Sin manco no hay leyenda.", 
    "🔋 Recargando energía… AFK un ratito."
]

# Obtener un Pokémon aleatorio
poke_id = random.randint(1, 898)
pokemon = requests.get(f"https://pokeapi.co/api/v2/pokemon/{poke_id}").json()
species = requests.get(pokemon["species"]["url"]).json()

nombre = next(n["name"] for n in species["names"] if n["language"]["name"] == "es")
clase = next(t["genus"] for t in species["genera"] if t["language"]["name"] == "es")
tipos_en = [t["type"]["name"] for t in pokemon["types"]]
tipos_es = ", ".join(tipos_traducidos.get(t, t.title()) for t in tipos_en)

pokemon_img_url = f"https://projectpokemon.org/images/normal-sprite/{pokemon['name'].capitalize()}.gif"

# Crear bloque Pokémon
pokemon_info_block = f"""<!-- POKEMON_INFO -->
## 🐱‍👤 Pokémon del día

| Imagen | Nombre | Tipo(s) | Clase |
|:------:|:------:|:-------:|:-----:|
| ![Pokémon del día]({pokemon_img_url}) | **{nombre}** | {tipos_es} | {clase} |
<!-- END_POKEMON_INFO -->"""

# Frase gamer del día
frase = random.choice(frases_gamer)
frase_gamer_block = f"""<!-- FRASE_GAMER -->
🎮 **Frase gamer del día:**  
> {frase}
<!-- END_FRASE_GAMER -->"""

# Leer el README
with open(README_PATH, "r", encoding="utf-8") as f:
    contenido = f.read()

# Reemplazar bloques
contenido = re.sub(
    r"<!-- POKEMON_INFO -->.*?<!-- END_POKEMON_INFO -->",
    pokemon_info_block,
    contenido,
    flags=re.DOTALL,
)

contenido = re.sub(
    r"<!-- FRASE_GAMER -->.*?<!-- END_FRASE_GAMER -->",
    frase_gamer_block,
    contenido,
    flags=re.DOTALL,
)

# Guardar README actualizado
with open(README_PATH, "w", encoding="utf-8") as f:
    f.write(contenido)
