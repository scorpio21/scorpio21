import requests
import random

# Función para obtener el Pokémon del día
def get_pokemon_of_the_day():
    url = "https://pokeapi.co/api/v2/pokemon/" + str(random.randint(1, 898))  # Hay 898 Pokémon conocidos
    response = requests.get(url)
    data = response.json()
    
    nombre = data["name"].capitalize()
    tipos = [tipo["type"]["name"] for tipo in data["types"]]
    tipos_es = [get_pokemon_type_translation(tipo) for tipo in tipos]  # Traducción de los tipos al español
    imagen = data["sprites"]["front_default"]
    pokedex_num = data["id"]  # Número del Pokémon en la Pokédex
    clase = data["species"]["name"]
    
    # Estadísticas base
    stats = {stat["stat"]["name"]: stat["base_stat"] for stat in data["stats"]}
    
    return nombre, tipos_es, imagen, pokedex_num, clase, stats

# Función para traducir tipos de Pokémon al español
def get_pokemon_type_translation(tipo):
    traducciones = {
        "fire": "Fuego",
        "water": "Agua",
        "grass": "Planta",
        "electric": "Eléctrico",
        "bug": "Bicho",
        "poison": "Veneno",
        "ghost": "Fantasma",
        "steel": "Acero",
        "psychic": "Psíquico",
        "normal": "Normal",
        "flying": "Volador",
        "fighting": "Lucha",
        "rock": "Roca",
        "fairy": "Hada",
        "ice": "Hielo",
        "dragon": "Dragón",
        "dark": "Siniestro",
        "ground": "Tierra",
        "shadow": "Sombra"
    }
    return traducciones.get(tipo, tipo)  # Si no encuentra la traducción, devuelve el nombre del tipo tal cual

# Obtener el Pokémon del día
nombre, tipos_es, pokemon_img_url, pokedex_num, clase, stats = get_pokemon_of_the_day()

# Función para obtener la frase gamer del día
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

# Obtener la frase gamer del día
frase_del_dia = get_gamer_quote()


# Bloque de información de Pokémon en el README
stats_md = f"HP: {stats['hp']}<br>Atq: {stats['attack']}<br>Def: {stats['defense']}<br>Vel: {stats['speed']}"
pokemon_info_block = f"""<!-- POKEMON_INFO -->
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

# Bloque de frase gamer en el README
frase_info_block = f"""<!-- FRASE_GAMER -->

### 💬 Frase 🎮 del día
> "{frase_del_dia}"
<!-- END_FRASE_GAMER -->"""

# Verificar los bloques antes de escribirlos
print(pokemon_info_block)
print(frase_info_block)

# Abre el archivo README.md para hacer las actualizaciones
with open("README.md", "r+", encoding="utf-8") as file:
    contenido = file.read()

    # Reemplazar o agregar el bloque del Pokémon y la frase del día
    if "<!-- POKEMON_INFO -->" in contenido:
        contenido = contenido.split("<!-- POKEMON_INFO -->")[0] + pokemon_info_block + contenido.split("<!-- END_POKEMON_INFO -->")[1]
    else:
        contenido = contenido.replace("<!-- POKEMON_INFO -->", pokemon_info_block)
    
    if "<!-- FRASE_GAMER -->" in contenido:
        contenido = contenido.split("<!-- FRASE_GAMER -->")[0] + frase_info_block + contenido.split("<!-- END_FRASE_GAMER -->")[1]
    else:
        contenido = contenido.replace("<!-- FRASE_GAMER -->", frase_info_block)

    # Volver a escribir el archivo con las actualizaciones
    file.seek(0)
    file.write(contenido)
    file.truncate()
