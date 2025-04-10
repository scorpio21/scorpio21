import requests
import random
from datetime import datetime

# Obtener Pokémon aleatorio
pokemon_id = random.randint(1, 898)
pokemon_url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}"
species_url = f"https://pokeapi.co/api/v2/pokemon-species/{pokemon_id}"

pokemon_data = requests.get(pokemon_url).json()
species_data = requests.get(species_url).json()

nombre = species_data['names'][5]['name']  # Nombre en español

tipos = pokemon_data['types']

# URL del GIF animado del Pokémon
pokemon_img_url = (
    f"https://projectpokemon.org/images/normal-sprite/{pokemon_data['name'].capitalize()}.gif"
)

# Traducciones de tipos al español
tipos_traducidos = {
    "normal": "Normal",
    "fire": "Fuego",
    "water": "Agua",
    "electric": "Eléctrico",
    "grass": "Planta",
    "ice": "Hielo",
    "fighting": "Lucha",
    "poison": "Veneno",
    "ground": "Tierra",
    "flying": "Volador",
    "psychic": "Psíquico",
    "bug": "Bicho",
    "rock": "Roca",
    "ghost": "Fantasma",
    "dragon": "Dragón",
    "dark": "Siniestro",
    "steel": "Acero",
    "fairy": "Hada"
}

# Traducciones de forma (shape) al español
formas_traducidas = {
    "ball": "Esférica",
    "squiggle": "Serpenteante",
    "fish": "Pez",
    "arms": "Con brazos",
    "blob": "Amorfa",
    "upright": "Bípeda",
    "quadruped": "Cuadrúpeda",
    "wings": "Con alas",
    "tentacles": "Tentáculos",
    "heads": "Con cabezas múltiples",
    "humanoid": "Humanoide",
    "bug-wings": "Con alas de insecto",
    "armor": "Con armadura"
}

# Traducción de tipos al español
tipos_es = ", ".join([tipos_traducidos.get(t["type"]["name"], t["type"]["name"].capitalize()) for t in tipos])

# Traducción de clase (forma)
clase_en = species_data["shape"]["name"]
clase = formas_traducidas.get(clase_en, clase_en.capitalize())

# Frases gamer aleatorias
frases = [
    "¡Demasiado pro para ser verdad!",
    "¡Este Pokémon no necesita masterball!",
    "Lag no cuenta si ganás igual.",
    "AFK pero con estilo.",
    "¡Atrápalos todos... menos los bugs!",
    "Level up sin esfuerzo, como debe ser.",
    "GG EZ."
]
frase_gamer = random.choice(frases)

# Bloque Pokémon del día
pokemon_info_block = f"""<!-- POKEMON_INFO -->
## 🐱‍🔋 Pokémon del día

| Imagen | Nombre | Tipo(s) | Clase |
|:------:|:------:|:-------:|:-----:|
| ![Pokémon del día]({pokemon_img_url}) | **{nombre}** | {tipos_es} | {clase} |
<!-- END_POKEMON_INFO -->"""

# Bloque Frase gamer del día
frase_block = f"""<!-- FRASE_GAMER -->
> 🎮 *{frase_gamer}*
<!-- END_FRASE_GAMER -->"""

# Leer README.md
with open("README.md", "r", encoding="utf-8") as f:
    contenido = f.read()

# Reemplazar bloques
contenido = contenido.split("<!-- POKEMON_INFO -->")[0] + pokemon_info_block + contenido.split("<!-- END_POKEMON_INFO -->")[1].split("<!-- FRASE_GAMER -->")[0] + frase_block + contenido.split("<!-- END_FRASE_GAMER -->")[1]

# Guardar cambios
with open("README.md", "w", encoding="utf-8") as f:
    f.write(contenido)

print("✅ README.md actualizado correctamente.")
