import requests
import time
# fichero pogo_api.py
from translation.pokemon_types import get_pokemon_type_translation

def get_json(url):

    for intento in range(3):

        try:
            respuesta = requests.get(url, timeout=20)
            respuesta.raise_for_status()
            return respuesta.json()

        except Exception as e:

            print(f"⚠️ Error descargando {url}")
            print(f"Intento {intento + 1}/3")

            if intento < 2:
                time.sleep(2)

    raise Exception(f"No se pudo descargar {url}")


# ------------------------------
# Cargar estadísticas de Pokémon pogo_api.py
# ------------------------------
def load_stats():

    url = "https://pogoapi.net/api/v1/pokemon_stats.json"

    return get_json(url)
#------------------------------
# Cargar movimientos de Pokémon
#------------------------------
def load_moves():

    url = "https://pogoapi.net/api/v1/current_pokemon_moves.json"

    return get_json(url)
#------------------------------
# Cargar tipos de Pokémon
#------------------------------
def load_types():

    url = "https://pogoapi.net/api/v1/pokemon_types.json"

    return get_json(url)
#------------------------------
# Cargar ataques rápidos
#------------------------------
def load_fast_moves():

    url = "https://pogoapi.net/api/v1/fast_moves.json"

    return get_json(url)

#------------------------------
# Cargar ataques cargados
#------------------------------
def load_charged_moves():

    url = "https://pogoapi.net/api/v1/charged_moves.json"

    return get_json(url)

#------------------------------
# Cargar multiplicadores de PC
#------------------------------
def load_cp_multiplier():

    url = "https://pogoapi.net/api/v1/cp_multiplier.json"

    return get_json(url)
#------------------------------
# Buscar tipo de movimiento
#------------------------------
def buscar_movimiento(nombre_movimiento, movimientos):

    for move in movimientos:

        if move["name"] == nombre_movimiento:
            return move

#------------------------------
# Obtener datos de Pokémon GO
#------------------------------
def get_pokemon_go_data(nombre):

    stats = load_stats()
    moves = load_moves()
    types = load_types()
    fast_move_types = load_fast_moves()
    charged_move_types = load_charged_moves()
    nombre = nombre.lower()
    cp_multiplier = load_cp_multiplier()

    pokemon_moves = None

    cpm = None

    for cp in cp_multiplier:
        if cp["level"] == 50:
            cpm = cp["multiplier"]
            break

    for tipo in types:

        if (
            tipo["pokemon_name"].lower() == nombre
            and tipo["form"] == "Normal"
        ):
            pokemon_types = tipo
            break

    if "pokemon_types" not in locals():
       
        pokemon_types = {
            "type": []
        }
    for move in moves:

        if (
            move["pokemon_name"].lower() == nombre
            and move["form"] == "Normal"
        ):
            pokemon_moves = move
            break

    if pokemon_moves is None:
        
        pokemon_moves = {
            "fast_moves": [],
            "charged_moves": []
        }
    
    for pokemon in stats:

        if (
            pokemon["pokemon_name"].lower() == nombre
            and pokemon["form"] == "Normal"
        ):

            return {
        "pokemon_name": pokemon["pokemon_name"],
        "base_attack": pokemon["base_attack"],
        "base_defense": pokemon["base_defense"],
        "base_stamina": pokemon["base_stamina"],
        "fast_moves": [
            {
                "nombre": move["name"],
                "tipo": move["type"],
                "power": move["power"],
                "energy": move["energy_delta"],
                "duration": move["duration"]
            }
            for m in pokemon_moves.get("fast_moves", [])
            for move in [buscar_movimiento(m, fast_move_types)]
            if move
        ],

        "charged_moves": [
            {
                "nombre": move["name"],
                "tipo": move["type"],
                "power": move["power"],
                "energy": abs(move["energy_delta"]),
                "duration": move["duration"]
            }
            for m in pokemon_moves.get("charged_moves", [])
            for move in [buscar_movimiento(m, charged_move_types)]
            if move
        ],

        "types": [
           get_pokemon_type_translation(t.lower())
           for t in pokemon_types["type"]
        ],

                "pc_max": (
                    pokemon["base_attack"]
                    + pokemon["base_defense"]
                    + pokemon["base_stamina"]
                )
            }
    return None
