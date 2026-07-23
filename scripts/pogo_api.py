import requests

from translation.pokemon_types import get_pokemon_type_translation
# ------------------------------
# Cargar estadísticas de Pokémon
# ------------------------------
def load_stats():

    url = "https://pogoapi.net/api/v1/pokemon_stats.json"

    return requests.get(url, timeout=20).json()

def load_moves():

    url = "https://pogoapi.net/api/v1/current_pokemon_moves.json"

    return requests.get(url, timeout=20).json()

def load_types():

    url = "https://pogoapi.net/api/v1/pokemon_types.json"

    return requests.get(url, timeout=20).json()

def load_cp_multiplier():

    url = "https://pogoapi.net/api/v1/cp_multiplier.json"

    return requests.get(url, timeout=20).json()

def get_pokemon_go_data(nombre):

    stats = load_stats()
    moves = load_moves()
    types = load_types()
    nombre = nombre.lower()
    cp_multiplier = load_cp_multiplier()

    pokemon_moves = None

    for tipo in types:

        if (
            tipo["pokemon_name"].lower() == nombre
            and tipo["form"] == "Normal"
        ):
            pokemon_types = tipo
            break

    for move in moves:

        if (
            move["pokemon_name"].lower() == nombre
            and move["form"] == "Normal"
        ):
            pokemon_moves = move
            break

    for pokemon in stats:

        if (
            pokemon["pokemon_name"].lower() == nombre
            and pokemon["form"] == "Normal"
        ):

            cp_max = None

    for cp in cp_multiplier:
        if cp["level"] == 50:
           cp_max = cp["multiplier"]
           break

    return {
        "pokemon_name": pokemon["pokemon_name"],
        "base_attack": pokemon["base_attack"],
        "base_defense": pokemon["base_defense"],
        "base_stamina": pokemon["base_stamina"],
        "fast_moves": pokemon_moves["fast_moves"],
        "charged_moves": pokemon_moves["charged_moves"],
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