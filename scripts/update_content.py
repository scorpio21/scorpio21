import requests
import random
import base64
from github import Github
import os

# ------------------ Configuración ------------------
REPO_NAME = "scorpio21/scorpio21"
README_PATH = "README.md"

# ------------------ Pokémon del día ------------------
def obtener_pokemon_aleatorio():
    pokemon_id = random.randint(1, 898)  # Primera 8 generaciones
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}"
    respuesta = requests.get(url)
    if respuesta.status_code != 200:
        print(f"❌ No se pudo obtener el Pokémon #{pokemon_id}")
        return None
    datos = respuesta.json()
    
    nombre = datos["name"].capitalize()
    tipo = ", ".join([t["type"]["name"].capitalize() for t in datos["types"]])
    altura = datos["height"] / 10  # Altura en metros
    peso = datos["weight"] / 10  # Peso en kg
    habilidades = ", ".join([h["ability"]["name"].capitalize() for h in datos["abilities"]])
    imagen_url = datos["sprites"]["versions"]["generation-v"]["black-white"]["animated"]["front_default"]
    if not imagen_url:
        imagen_url = datos["sprites"]["front_default"]
    if not imagen_url:
        print(f"❌ No se pudo obtener imagen para {nombre}")
        return None
    
    return {
        "nombre": nombre,
        "tipo": tipo,
        "altura": altura,
        "peso": peso,
        "habilidades": habilidades,
        "imagen": imagen_url
    }

# ------------------ Frase gamer del día ------------------
FRASES_GAMERS = [
    "¡Necesito más maná!",
    "¡Lag, no vale!",
    "¡Git gud!",
    "¿Guardar partida? Eso es para cobardes.",
    "Press F to pay respects.",
    "¿Estás ganando, hijo?",
    "¡Eso fue un crítico!",
    "El joystick está mal, no soy yo.",
]

def obtener_frase_gamer():
    return random.choice(FRASES_GAMERS)

# ------------------ Actualizar README.md ------------------
def actualizar_readme(pokemon, frase, token):
    g = Github(token)
    repo = g.get_repo(REPO_NAME)
    readme_file = repo.get_contents(README_PATH)
    contenido = readme_file.decoded_content.decode("utf-8")

    bloque_pokemon = f"""<!-- POKEMON_INFO -->
<table>
  <tr>
    <td><img src="{pokemon['imagen']}" alt="{pokemon['nombre']}" /></td>
    <td>
      <b>Pokémon del día:</b><br>
      🆔 Número: {pokemon['nombre']}<br>
      🧬 Tipo(s): {pokemon['tipo']}<br>
      📏 Altura: {pokemon['altura']} m<br>
      ⚖️ Peso: {pokemon['peso']} kg<br>
      🧠 Habilidades: {pokemon['habilidades']}<br>
    </td>
  </tr>
</table>
<!-- POKEMON_INFO_END -->"""

    bloque_frase = f"""<!-- FRASE_GAMER -->
🎮 Frase gamer del día: <i>{frase}</i>
<!-- FRASE_GAMER_END -->"""

    # Reemplazar bloques
    contenido_nuevo = contenido
    if "<!-- POKEMON_INFO -->" in contenido and "<!-- POKEMON_INFO_END -->" in contenido:
        contenido_nuevo = contenido_nuevo.split("<!-- POKEMON_INFO -->")[0] + bloque_pokemon + contenido_nuevo.split("<!-- POKEMON_INFO_END -->")[1]
    if "<!-- FRASE_GAMER -->" in contenido and "<!-- FRASE_GAMER_END -->" in contenido:
        contenido_nuevo = contenido_nuevo.split("<!-- FRASE_GAMER -->")[0] + bloque_frase + contenido_nuevo.split("<!-- FRASE_GAMER_END -->")[1]

    if contenido_nuevo != contenido:
        repo.update_file(
            path=README_PATH,
            message="🔁 Actualización diaria automática: Pokémon y frase gamer",
            content=contenido_nuevo,
            sha=readme_file.sha
        )
        print("✅ README.md actualizado correctamente.")
    else:
        print("ℹ️ No hubo cambios en el README.md.")

# ------------------ Ejecución principal ------------------
if __name__ == "__main__":
    token = os.getenv("GH_TOKEN")
    if not token:
        print("❌ GH_TOKEN no está definido en las variables de entorno.")
        exit(1)

    pokemon = obtener_pokemon_aleatorio()
    if not pokemon:
        exit(1)

    frase = obtener_frase_gamer()
    actualizar_readme(pokemon, frase, token)
