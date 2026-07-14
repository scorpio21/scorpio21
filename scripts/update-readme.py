import requests
import random
import re
from datetime import datetime

# Lista de legendarios/míticos
legendarios = [
    144,145,146,150,151,243,244,245,249,250,251,
    377,378,379,380,381,382,383,384,385,
    480,481,482,483,484,485,486,487,488,489,490,
    638,639,640,641,642,643,644,645,646,647,648,649,
    716,717,718,719,720,721,
    785,786,787,788,789,790,791,792,800,801,802,
    888,889,890
]

# Colores según rareza (neón falso compatible con GitHub)
neon_rarity_colors = {
    "comun": "#00ff7f",
    "no_comun": "#1e90ff",
    "raro": "#ff1493",
    "legendario": "#ffd700"
}

# Función para determinar rareza
def get_rarity(tipo_principal, pokedex_num):
    if pokedex_num in legendarios:
        return "legendario"
    if tipo_principal in ["Psíquico", "Fantasma", "Acero", "Dragón", "Siniestro", "Hada"]:
        return "raro"
    if tipo_principal in ["Planta", "Agua", "Fuego", "Eléctrico", "Veneno", "Lucha", "Roca", "Tierra", "Hielo"]:
        return "no_comun"
    return "comun"

# Función para obtener el Pokémon del día
def get_pokemon_of_the_day():
    url = "https://pokeapi.co/api/v2/pokemon/" + str(random.randint(1, 898))
    response = requests.get(url)
    data = response.json()
    
    nombre = data["name"].capitalize()
    tipos = [tipo["type"]["name"] for tipo in data["types"]]
    tipos_es = [get_pokemon_type_translation(tipo) for tipo in tipos]
    imagen = data["sprites"]["front_default"]
    pokedex_num = data["id"]
    clase = data["species"]["name"]
    
    stats = {stat["stat"]["name"]: stat["base_stat"] for stat in data["stats"]}
    
    return nombre, tipos_es, imagen, pokedex_num, clase, stats

# Traducción de tipos
def get_pokemon_type_translation(tipo):
    traducciones = {
        "fire": "Fuego", "water": "Agua", "grass": "Planta", "electric": "Eléctrico",
        "bug": "Bicho", "poison": "Veneno", "ghost": "Fantasma", "steel": "Acero",
        "psychic": "Psíquico", "normal": "Normal", "flying": "Volador", "fighting": "Lucha",
        "rock": "Roca", "fairy": "Hada", "ice": "Hielo", "dragon": "Dragón",
        "dark": "Siniestro", "ground": "Tierra", "shadow": "Sombra"
    }
    return traducciones.get(tipo, tipo)
    
# Obtener la cadena de evolución
def get_evolution_chain(pokedex_num):
    try:
        # Obtener la especie
        species_url = f"https://pokeapi.co/api/v2/pokemon-species/{pokedex_num}"
        species = requests.get(species_url).json()

        # URL de la cadena evolutiva
        evo_url = species["evolution_chain"]["url"]

        # Descargar la cadena
        evo_data = requests.get(evo_url).json()

        nombres = []

        def recorrer(cadena):
            nombres.append(cadena["species"]["name"].capitalize())
            for evo in cadena["evolves_to"]:
                recorrer(evo)

        recorrer(evo_data["chain"])

        if len(nombres) == 1:
            return "No evoluciona"

        return " → ".join(nombres)

    except Exception:
        return "Desconocida"

# Obtener Pokémon del día
nombre, tipos_es, pokemon_img_url, pokedex_num, clase, stats = get_pokemon_of_the_day()

# obtiene la cadena
cadena_evolucion = get_evolution_chain(pokedex_num)

# Rareza + color
rareza = get_rarity(tipos_es[0], pokedex_num)

# Iconos según rareza
rareza_iconos = {
    "comun": "🟢",
    "no_comun": "🔵",
    "raro": "🟣",
    "legendario": "🟡✨"
}

# Colores para Shields.io
rareza_colores = {
    "comun": "brightgreen",
    "no_comun": "blue",
    "raro": "purple",
    "legendario": "gold"
}

# Texto de la rareza
rareza_texto = {
    "comun": "Común",
    "no_comun": "No común",
    "raro": "Raro",
    "legendario": "Legendario"
}

# Nombre
nombre_md = f"{rareza_iconos[rareza]} <b>{nombre}</b>"

# Badge de Shields.io
from urllib.parse import quote

badge_rareza = (
    f'<img src="https://img.shields.io/badge/'
    f'{quote(nombre)}-{quote(rareza_texto[rareza])}-{rareza_colores[rareza]}'
    f'?style=for-the-badge" '
    f'alt="{rareza_texto[rareza]}">'
)

# Frase gamer
def get_gamer_quote():
    frases = [
        "¡Nunca subestimes el poder de un jugador con café!",
        "Solo hay una regla: ¡Ganar es lo único que importa!",
        "El verdadero juego comienza cuando apagas la consola.",
        "En cada partida, hay un nuevo desafío esperando ser conquistado.",
        "Si no estás ganando, ¡estás aprendiendo!",
        "Jugar es una forma de vida, ¡y siempre es un buen momento para empezar!",
        "Gamer de día, héroe de noche.",
        "La vida es como un videojuego: ¡haz tu movimiento!"
    ]
    return random.choice(frases)

frase_del_dia = get_gamer_quote()

# Stats en vertical
stats_md = (
    f"HP: {stats['hp']}<br>"
    f"Atq: {stats['attack']}<br>"
    f"Def: {stats['defense']}<br>"
    f"Vel: {stats['speed']}"
)

# Timestamp
fecha = datetime.utcnow().isoformat()

# Bloque Pokémon (tabla HTML)
pokemon_info_block = f"""<!-- POKEMON_INFO -->
<!-- Generated: {fecha} -->
### 🐱‍👤 Pokémon del día

<table>
<tr><td><b>Imagen</b></td><td><img src="{pokemon_img_url}" alt="{nombre}" /></td></tr>
<tr><td><b>Nombre</b></td><td>{rareza_iconos[rareza]} <b>{nombre}</b></td></tr>

<tr><td><b>Rareza</b></td><td>
<img src="https://img.shields.io/badge/{rareza_texto[rareza]}-{rareza_colores[rareza]}?style=flat-square">
</td></tr>
<tr><td><b>Tipo(s)</b></td><td>{', '.join(tipos_es)}</td></tr>
<tr><td><b>Clase</b></td><td>{clase.capitalize()}</td></tr>
<tr><td><b>Nº Pokédex</b></td><td>{pokedex_num}</td></tr>
<tr><td><b>Movimientos especiales</b></td><td>{', '.join([
random.choice(["Corte Psíquico", "Hoja Afilada", "Puño Fuego"]),
random.choice(["Rayo Solar", "Ataque Psíquico", "Puño Trueno"]),
random.choice(["Puño Trueno", "Puño Fuego"])
])}</td></tr>
<tr><td><b>Evolución</b></td><td>{cadena_evolucion}</td></tr>
<tr><td><b>Estadísticas base</b></td><td>{stats_md}</td></tr>
</table>

<br>

**Historia del día:**  
"Hoy, {nombre} decidió {random.choice(['tomar un descanso', 'explorar un nuevo terreno', 'enfrentar su mayor desafío'])}. ¡Prepárate para ver qué sucede!"

---

**¿Sabías que...?**  
{nombre} es conocido por su capacidad para {random.choice(['alcanza poderes muy altos', 'desarrollar habilidades que cambian las batallas', 'dominar varias tácticas en combate'])}.

---

**Pokémon Go:**
- **CP máximo:** {random.randint(3000, 4000)}
- **Clase de combate:** 8
- **Evento especial:** {nombre} puede aparecer más frecuentemente durante el evento "Festival de la primavera".

[Más información en Bulbapedia](https://bulbapedia.bulbagarden.net/wiki/{nombre}_(Pokémon))

<!-- END_POKEMON_INFO -->
"""

# Bloque frase gamer
frase_info_block = f"""<!-- FRASE_GAMER -->
<!-- Generated: {fecha} -->
### 💬 Frase 🎮 del día
> "{frase_del_dia}"
<!-- END_FRASE_GAMER -->
"""

# Actualizar README con regex
with open("README.md", "r+", encoding="utf-8") as file:
    contenido = file.read()

    contenido = re.sub(
        r"<!-- POKEMON_INFO -->.*?<!-- END_POKEMON_INFO -->",
        pokemon_info_block,
        contenido,
        flags=re.DOTALL
    )

    contenido = re.sub(
        r"<!-- FRASE_GAMER -->.*?<!-- END_FRASE_GAMER -->",
        frase_info_block,
        contenido,
        flags=re.DOTALL
    )

    file.seek(0)
    file.write(contenido)
    file.truncate()
