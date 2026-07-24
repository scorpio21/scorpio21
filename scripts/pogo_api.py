import requests

# fichero pogo_api.py

from translation.pokemon_types import get_pokemon_type_translation
# ------------------------------
# Cargar estadísticas de Pokémon pogo_api.py
# ------------------------------
def load_stats():

    url = "https://pogoapi.net/api/v1/pokemon_stats.json"

    return requests.get(url, timeout=20).json()
#------------------------------
# Cargar movimientos de Pokémon
#------------------------------
def load_moves():

    url = "https://pogoapi.net/api/v1/current_pokemon_moves.json"

    return requests.get(url, timeout=20).json()
#------------------------------
# Cargar tipos de Pokémon
#------------------------------
def load_types():

    url = "https://pogoapi.net/api/v1/pokemon_types.json"

    return requests.get(url, timeout=20).json()
#------------------------------
# Cargar ataques rápidos
#------------------------------
def load_fast_moves():

    url = "https://pogoapi.net/api/v1/fast_moves.json"

    return requests.get(url, timeout=20).json()

#------------------------------
# Cargar ataques cargados
#------------------------------
def load_charged_moves():

    url = "https://pogoapi.net/api/v1/charged_moves.json"

    return requests.get(url, timeout=20).json()

#------------------------------
# Cargar multiplicadores de PC
#------------------------------
def load_cp_multiplier():

    url = "https://pogoapi.net/api/v1/cp_multiplier.json"

    return requests.get(url, timeout=20).json()
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

    # print(cp_multiplier)

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
        print(f"⚠️ No se encontraron tipos para {nombre}")
        pokemon_types = {
            "type": []
        }
    print(f"🔍 Buscando movimientos para: {nombre}")

    for move in moves:

        if nombre in move["pokemon_name"].lower():
            print(move["pokemon_name"], "-", move["form"])

        if (
            move["pokemon_name"].lower() == nombre
            and move["form"] == "Normal"
        ):
            pokemon_moves = move
            break

    if pokemon_moves is None:
        print(f"⚠️ No se encontraron movimientos para {nombre}")
        pokemon_moves = {
            "fast_moves": [],
            "charged_moves": []
        }
    
    for pokemon in stats:

        if (
            pokemon["pokemon_name"].lower() == nombre
            and pokemon["form"] == "Normal"
        ):
            # print("CPM:", cpm)

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


if __name__ == "__main__":

    pokemon = get_pokemon_go_data("Pikachu")

    print("PC máximo:", pokemon["pc_max"])
    print("Tipos:", pokemon["types"])
    print(pokemon["fast_moves"])
    print(pokemon["charged_moves"])
    
    print("\n=== FAST MOVE ===")

    fast = load_fast_moves()
    
    for m in fast:
        if m["name"] == "Poison Jab":
            print(m)
            break

    print("\n=== CHARGED MOVE ===")

    charged = load_charged_moves()

    for m in charged:
        if m["name"] == "Sludge Wave":
            print(m)
            break
