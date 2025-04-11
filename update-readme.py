import requests
from bs4 import BeautifulSoup
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
    clase = data["species"]["name"]

    return nombre, tipos_es, imagen, clase

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
nombre, tipos_es, pokemon_img_url, clase = get_pokemon_of_the_day()

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
pokemon_info_block = f"""<!-- POKEMON_INFO -->

### 🐱‍👤 Pokémon del día

| Imagen | Nombre | Tipo(s) | Clase | Número de Pokédex |
|:------:|:------:|:-------:|:-----:|:-----------------:|
| ![Pokémon del día](https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/103.png) | **Exeggutor** | Planta, Psíquico | Exeggutor | 103 |

**Curiosidad:**  
Exeggutor es conocido por su alta capacidad de usar movimientos psíquicos. Además, su diseño está basado en un árbol tropical de la región de Alola.

---

**Movimientos especiales:**
- **Psíquico**
- **Hoja Afilada**
- **Rayo Solar**

---

**Evolución:**  
- **Exeggutor** → **Exeggutor (Alola)**

---

**Estadísticas base:**
- **HP:** 95
- **Ataque:** 105
- **Defensa:** 85
- **Velocidad:** 45

---

**Habilidad:** Clorofila

---

**Historia del día:**  
"Hoy, Exeggutor se despertó con una extraña sensación. El sol de la mañana lo llenó de energía, y ahora está listo para enfrentar cualquier reto en su camino. ¡Cuidado, entrenadores!"

---

**¿Sabías que...?**  
Exeggutor y Venusaur comparten el tipo Planta, pero mientras Exeggutor es más conocido por su poder psíquico, Venusaur tiene una increíble habilidad para las batallas de largo alcance con su ataque "Látigo Cepa".

---

**Pokémon Go:**
- **CP máximo:** 3556
- **Clase de combate:** 8
- **Evento especial:** Exeggutor puede aparecer más frecuentemente durante el evento "Festival de la primavera".

[Más información en Bulbapedia](https://bulbapedia.bulbagarden.net/wiki/Exeggutor_(Pokémon))

<!-- END_POKEMON_INFO -->
"""

# Bloque de frase gamer en el README
frase_info_block = f"""<!-- FRASE_GAMER -->
## 💬 Frase gamer del día
> "{frase_del_dia}"
<!-- END_FRASE_GAMER -->"""

# Imprimir para verificar el resultado
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
