import random
import requests

from pokemon_types import get_pokemon_type_translation


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
