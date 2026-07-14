import requests
import random
import re
from datetime import datetime

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

# Obtener Pokémon del día
nombre, tipos_es, pokemon_img_url, pokedex_num, clase, stats = get_pokemon_of_the_day()

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

# Stats en vertical con <br>
stats_md = (
    f"HP: {stats['hp']}<br>"
    f"Atq: {stats['attack']}<br>"
    f"Def: {stats['defense']}<br>"
    f"Vel: {stats['speed']}"
)

# Timestamp para forzar cambios
fecha = datetime.utcnow().isoformat()

# Bloque Pokémon
pokemon_info_block = f"""<!-- POKEMON_INFO -->
<!-- Generated: {fecha} -->
### 🐱‍👤 Pokémon del día

| Imagen | Nombre | Tipo(s) | Clase | Nº Pokédex | Movimientos especiales | Evolución | Estadísticas base |
|:------:|:------:|:-------:|:-----:|:----------:|:----------------------:|:---------:|:------------------:|
| ![Pokémon del día]({pokemon_img_url}) | **{nombre}** | {', '.join(tipos_es)} | {clase.capitalize()} | {pokedex_num} | {', '.join([
random.choice(["Corte Psíquico", "Hoja Afilada", "Puño Fuego"]),
random.choice(["Rayo Solar", "Ataque Psíquico", "Puño Trueno"]),
random.choice(["Puño Trueno", "Puño Fuego"])
])} | {nombre} → {nombre} (Alola) | {stats_md} |

**Curiosidad:**  
{nombre} es conocido por su habilidad para {random.choice(["usar ataques poderosos", "alcanzar altas velocidades", "dominar la batalla", "resistir ataques"]).lower()}.

---

**Habilidad:** {random.choice(["Clorofila", "Ojo Compuesto", "Impunidad"])} 

---

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
