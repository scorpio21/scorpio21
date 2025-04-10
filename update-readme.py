import requests
import random
import re

README_PATH = "README.md"

TIPOS_ES = {
    "normal": "Normal", "fighting": "Lucha", "flying": "Volador", "poison": "Veneno",
    "ground": "Tierra", "rock": "Roca", "bug": "Bicho", "ghost": "Fantasma", "steel": "Acero",
    "fire": "Fuego", "water": "Agua", "grass": "Planta", "electric": "Eléctrico", "psychic": "Psíquico",
    "ice": "Hielo", "dragon": "Dragón", "dark": "Siniestro", "fairy": "Hada"
}

FRASES_GAMER = [
    "¡No campees tanto que te salen raíces! 🎮",
    "La vida es como Dark Souls: difícil, pero gratificante. 🗡️",
    "¿Eres pro o solo tu conexión es buena? ⚡",
    "El lag es el verdadero jefe final. 🕹️",
    "Subí de nivel en procrastinación. 💤"
]

def obtener_pokemon_aleatorio():
    id_aleatorio = random.randint(1, 898)
    url = f"https://pokeapi.co/api/v2/pokemon/{id_aleatorio}"
    data = requests.get(url).json()
    nombre = data["name"].capitalize()
    tipos = [t["type"]["name"] for t in data["types"]]
    tipos_es = ", ".join(TIPOS_ES.get(t, t) for t in tipos)
    imagen = data["sprites"]["other"]["official-artwork"]["front_default"]
    clase = "Legendario" if data.get("base_experience", 0) > 250 else "Normal"
    return nombre, tipos_es, clase, imagen

def actualizar_readme(nombre, tipos_es, clase, imagen, frase):
    with open(README_PATH, "r", encoding="utf-8") as f:
        contenido = f.read()

    bloque_pokemon = f"""<!-- POKEMON_INFO -->
## 🐱‍👤 Pokémon del día

| Imagen | Nombre | Tipo(s) | Clase |
|:------:|:------:|:-------:|:-----:|
| ![Pokémon del día]({imagen}) | **{nombre}** | {tipos_es} | {clase} |
<!-- END_POKEMON_INFO -->"""

    bloque_frase = f"""<!-- FRASE_GAMER -->
🎮 **Frase gamer del día**: _{frase}_
<!-- END_FRASE_GAMER -->"""

    contenido = re.sub(r"<!-- POKEMON_INFO -->.*?<!-- END_POKEMON_INFO -->", bloque_pokemon, contenido, flags=re.DOTALL)
    contenido = re.sub(r"<!-- FRASE_GAMER -->.*?<!-- END_FRASE_GAMER -->", bloque_frase, contenido, flags=re.DOTALL)

    with open(README_PATH, "w", encoding="utf-8") as f:
        f.write(contenido)

if __name__ == "__main__":
    nombre, tipos_es, clase, imagen = obtener_pokemon_aleatorio()
    frase = random.choice(FRASES_GAMER)
    actualizar_readme(nombre, tipos_es, clase, imagen, frase)
