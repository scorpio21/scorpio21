import requests
import random
import re
from datetime import datetime

# Tipos de caracteres
type_chart = {
    "Normal": {"weak": ["Lucha"], "resist": [], "immune": ["Fantasma"]},
    "Fuego": {"weak": ["Agua", "Tierra", "Roca"], "resist": ["Fuego", "Planta", "Hielo", "Bicho", "Acero", "Hada"], "immune": []},
    "Agua": {"weak": ["Planta", "Eléctrico"], "resist": ["Fuego", "Agua", "Hielo", "Acero"], "immune": []},
    "Planta": {"weak": ["Fuego", "Hielo", "Veneno", "Volador", "Bicho"], "resist": ["Agua", "Planta", "Tierra", "Eléctrico"], "immune": []},
    "Eléctrico": {"weak": ["Tierra"], "resist": ["Eléctrico", "Volador", "Acero"], "immune": []},
    "Hielo": {"weak": ["Fuego", "Lucha", "Roca", "Acero"], "resist": ["Hielo"], "immune": []},
    "Lucha": {"weak": ["Volador", "Psíquico", "Hada"], "resist": ["Bicho", "Roca", "Siniestro"], "immune": []},
    "Veneno": {"weak": ["Tierra", "Psíquico"], "resist": ["Planta", "Lucha", "Veneno", "Bicho", "Hada"], "immune": []},
    "Tierra": {"weak": ["Agua", "Planta", "Hielo"], "resist": ["Veneno", "Roca"], "immune": ["Eléctrico"]},
    "Volador": {"weak": ["Eléctrico", "Hielo", "Roca"], "resist": ["Planta", "Lucha", "Bicho"], "immune": ["Tierra"]},
    "Psíquico": {"weak": ["Bicho", "Fantasma", "Siniestro"], "resist": ["Lucha", "Psíquico"], "immune": []},
    "Bicho": {"weak": ["Fuego", "Volador", "Roca"], "resist": ["Planta", "Lucha", "Tierra"], "immune": []},
    "Roca": {"weak": ["Agua", "Planta", "Lucha", "Tierra", "Acero"], "resist": ["Normal", "Fuego", "Veneno", "Volador"], "immune": []},
    "Fantasma": {"weak": ["Fantasma", "Siniestro"], "resist": ["Veneno", "Bicho"], "immune": ["Normal", "Lucha"]},
    "Dragón": {"weak": ["Hielo", "Dragón", "Hada"], "resist": ["Fuego", "Agua", "Planta", "Eléctrico"], "immune": []},
    "Siniestro": {"weak": ["Lucha", "Bicho", "Hada"], "resist": ["Fantasma", "Siniestro"], "immune": ["Psíquico"]},
    "Acero": {"weak": ["Fuego", "Lucha", "Tierra"], "resist": ["Normal", "Planta", "Hielo", "Volador", "Psíquico", "Bicho", "Roca", "Dragón", "Acero", "Hada"], "immune": ["Veneno"]},
    "Hada": {"weak": ["Veneno", "Acero"], "resist": ["Lucha", "Bicho", "Siniestro"], "immune": ["Dragón"]}
}
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

# Obtener tipo
def obtener_tipo_info(tipos):
    debilidades = set()
    resistencias = set()
    inmunidades = set()

    for tipo in tipos:
        datos = type_chart.get(tipo, {})
        debilidades.update(datos.get("weak", []))
        resistencias.update(datos.get("resist", []))
        inmunidades.update(datos.get("immune", []))

    return (
        sorted(debilidades),
        sorted(resistencias),
        sorted(inmunidades)
    )
    
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
    species = requests.get(data["species"]["url"]).json()
    
    nombre = data["name"].capitalize()
    tipos = [tipo["type"]["name"] for tipo in data["types"]]
    tipos_es = [get_pokemon_type_translation(tipo) for tipo in tipos]
    imagen = data["sprites"]["other"]["official-artwork"]["front_default"]
    pokedex_num = data["id"]
    clase = data["species"]["name"]

    color_pokedex = species["color"]["name"]

    habitat = species["habitat"]["name"].capitalize() if species["habitat"] else "Desconocido"

    capture_rate = species["capture_rate"]

    base_happiness = species["base_happiness"]

    egg_groups = ", ".join(
    grupo["name"].capitalize()
    for grupo in species["egg_groups"]
)

    stats = {stat["stat"]["name"]: stat["base_stat"] for stat in data["stats"]}

    altura = data["height"] / 10
    peso = data["weight"] / 10
    experiencia = data["base_experience"]

    habilidades = []
    habilidad_oculta = None

    for habilidad in data["abilities"]:
        nombre_habilidad = habilidad["ability"]["name"].replace("-", " ").capitalize()

        if habilidad["is_hidden"]:
            habilidad_oculta = nombre_habilidad
        else:
            habilidades.append(nombre_habilidad)

    return (
        nombre,
        tipos_es,
        imagen,
        pokedex_num,
        clase,
        stats,
        altura,
        peso,
        experiencia,
        habitat,
        color_pokedex,
        capture_rate,
        base_happiness,
        egg_groups,
        habilidades,
        habilidad_oculta
    )
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
# tipos Badges
tipo_badges = {
    "Normal": "https://img.shields.io/badge/Normal-A8A77A?style=flat-square",
    "Fuego": "https://img.shields.io/badge/Fuego-EE8130?style=flat-square",
    "Agua": "https://img.shields.io/badge/Agua-6390F0?style=flat-square",
    "Planta": "https://img.shields.io/badge/Planta-7AC74C?style=flat-square",
    "Eléctrico": "https://img.shields.io/badge/Eléctrico-F7D02C?style=flat-square",
    "Hielo": "https://img.shields.io/badge/Hielo-96D9D6?style=flat-square",
    "Lucha": "https://img.shields.io/badge/Lucha-C22E28?style=flat-square",
    "Veneno": "https://img.shields.io/badge/Veneno-A33EA1?style=flat-square",
    "Tierra": "https://img.shields.io/badge/Tierra-E2BF65?style=flat-square",
    "Volador": "https://img.shields.io/badge/Volador-A98FF3?style=flat-square",
    "Psíquico": "https://img.shields.io/badge/Psíquico-F95587?style=flat-square",
    "Bicho": "https://img.shields.io/badge/Bicho-A6B91A?style=flat-square",
    "Roca": "https://img.shields.io/badge/Roca-B6A136?style=flat-square",
    "Fantasma": "https://img.shields.io/badge/Fantasma-735797?style=flat-square",
    "Dragón": "https://img.shields.io/badge/Dragón-6F35FC?style=flat-square",
    "Siniestro": "https://img.shields.io/badge/Siniestro-705746?style=flat-square",
    "Acero": "https://img.shields.io/badge/Acero-B7B7CE?style=flat-square",
    "Hada": "https://img.shields.io/badge/Hada-D685AD?style=flat-square"
}

# Obtener la cadena de evolución
def get_evolution_chain(pokedex_num):
    try:
        species = requests.get(
            f"https://pokeapi.co/api/v2/pokemon-species/{pokedex_num}"
        ).json()

        evo_data = requests.get(
            species["evolution_chain"]["url"]
        ).json()

        evoluciones = []

        def recorrer(cadena):
            evoluciones.append(cadena["species"]["name"].capitalize())
            for evo in cadena["evolves_to"]:
                recorrer(evo)

        recorrer(evo_data["chain"])

        # Si solo tiene una forma, no evoluciona
        if len(evoluciones) == 1:
            return "No evoluciona"

        # Si hay 4 o menos evoluciones → una sola fila
        # Si hay más → dividir en dos filas
        if len(evoluciones) <= 4:
            filas = [evoluciones]
        else:
            filas = [
                evoluciones[:4],
                evoluciones[4:]
            ]

        html = "<table>"

        for fila in filas:
            html += "<tr>"

            for i, nombre in enumerate(fila):
                imagen = f"https://img.pokemondb.net/artwork/large/{nombre.lower()}.jpg"

                html += f"""
<td align="center">
    <img src="{imagen}" width="70"><br>
    <small><b>{nombre}</b></small>
</td>
"""

                # Flecha entre evoluciones
                if i < len(fila) - 1:
                    html += '<td align="center"><b>➡️</b></td>'

            html += "</tr>"

        html += "</table>"

        return html

    except Exception as e:
        return f"Error obteniendo evolución: {e}"

# Obtener Pokémon del día
(
    nombre,
    tipos_es,
    pokemon_img_url,
    pokedex_num,
    clase,
    stats,
    altura,
    peso,
    experiencia,
    habitat,
    color_pokedex,
    capture_rate,
    base_happiness,
    egg_groups,
    habilidades,
    habilidad_oculta
) = get_pokemon_of_the_day()

colores_pokedex = {
    "black": "⚫ Negro",
    "blue": "🔵 Azul",
    "brown": "🟤 Marrón",
    "gray": "⚪ Gris",
    "green": "🟢 Verde",
    "pink": "🩷 Rosa",
    "purple": "🟣 Morado",
    "red": "🔴 Rojo",
    "white": "⚪ Blanco",
    "yellow": "🟡 Amarillo"
}
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

#Barras
def barra_stat(valor, maximo=255, ancho=10):

    bloques = round((valor / maximo) * ancho)

    if valor < 40:
        color = "🟥"
    elif valor < 70:
        color = "🟧"
    elif valor < 100:
        color = "🟨"
    elif valor < 130:
        color = "🟩"
    else:
        color = "🟦"

    return color * bloques + "⬜" * (ancho - bloques)

# Stats en vertical
stats_md = f"""
❤️ <b>PS</b><br>
{barra_stat(stats['hp'])} {stats['hp']}<br>

⚔️ <b>Ataque</b><br>
{barra_stat(stats['attack'])} {stats['attack']}

🛡️ <b>Defensa</b><br>
{barra_stat(stats['defense'])} {stats['defense']}<br>

✨ <b>Ataque Especial</b><br>
{barra_stat(stats['special-attack'])} {stats['special-attack']}<br>

🛡️ <b>Defensa Especial</b><br>
{barra_stat(stats['special-defense'])} {stats['special-defense']}<br>

💨 <b>Velocidad</b><br>
{barra_stat(stats['speed'])} {stats['speed']}
"""

bst = sum(stats.values())

if bst >= 680:
    nivel_bst = "🌟 Legendario"
elif bst >= 600:
    nivel_bst = "💎 Pseudolegendario"
elif bst >= 500:
    nivel_bst = "🔥 Muy fuerte"
elif bst >= 400:
    nivel_bst = "⚔️ Fuerte"
elif bst >= 300:
    nivel_bst = "👍 Normal"
else:
    nivel_bst = "🌱 Básico"


def barra_bst(valor, maximo=720, ancho=20):
    bloques = round(valor / maximo * ancho)
    return "🟩" * bloques + "⬜" * (ancho - bloques)

bst_html = f"""
{barra_bst(bst)}

<b>{bst} puntos</b><br>
{nivel_bst}
"""

# Tipos Html
tipos_html = " ".join(
    f'<img src="{tipo_badges.get(tipo)}" alt="{tipo}">'
    for tipo in tipos_es
)

debilidades, resistencias, inmunidades = obtener_tipo_info(tipos_es)

debilidades_html = " ".join(
    f'<img src="{tipo_badges[t]}" alt="{t}">'
    for t in debilidades if t in tipo_badges
)

resistencias_html = " ".join(
    f'<img src="{tipo_badges[t]}" alt="{t}">'
    for t in resistencias if t in tipo_badges
)

inmunidades_html = " ".join(
    f'<img src="{tipo_badges[t]}" alt="{t}">'
    for t in inmunidades if t in tipo_badges
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
<tr><td><b>Nº Pokédex</b></td><td>{pokedex_num}</td></tr>
<tr><td><b>Tipo(s)</b></td><td>{tipos_html}</td></tr>
<tr>
<td><b>⚔️ Débil contra</b></td>
<td>{debilidades_html}</td>
</tr>

<tr>
<td><b>🛡️ Resiste</b></td>
<td>{resistencias_html}</td>
</tr>

<tr>
<td><b>✨ Inmune a</b></td>
<td>{inmunidades_html if inmunidades_html else "Ninguna"}</td>
</tr>
<tr><td><b>Clase</b></td><td>{clase.capitalize()}</td></tr>
<tr><td><b>🎨 Color Pokédex</b></td><td>{colores_pokedex[color_pokedex]}</td></tr>
<tr><td><b>📏 Altura</b></td><td>{altura} m</td></tr>
<tr><td><b>⚖️ Peso</b></td><td>{peso} kg</td></tr>
<tr><td><b>⭐ Experiencia</b></td><td>{experiencia}</td></tr>
<tr><td><b>🌍 Hábitat</b></td><td>{habitat}</td></tr>
<tr><td><b>🥚 Grupo huevo</b></td><td>{egg_groups}</td></tr>
<tr><td><b>❤️ Amistad base</b></td><td>{base_happiness}</td></tr>
<tr><td><b>🎯 Ratio captura</b></td><td>{capture_rate}</td></tr>
<tr><td><b>💪 Habilidades</b></td>
<td>{", ".join(habilidades)}</td></tr>
<tr><td><b>✨ Habilidad oculta</b></td>
<td>{habilidad_oculta if habilidad_oculta else "Ninguna"}</td></tr>
<tr><td><b>Movimientos especiales</b></td><td>{', '.join([
random.choice(["Corte Psíquico", "Hoja Afilada", "Puño Fuego"]),
random.choice(["Rayo Solar", "Ataque Psíquico", "Puño Trueno"]),
random.choice(["Puño Trueno", "Puño Fuego"])
])}</td></tr>
<tr><td><b>Evolución</b></td><td>{cadena_evolucion}</td></tr>
<tr><td><b>Estadísticas base</b></td><td>{stats_md}</td></tr>
<tr>
<td><b>🏆 Poder total (BST)</b></td>
<td>{bst_html}</td>
</tr>
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
