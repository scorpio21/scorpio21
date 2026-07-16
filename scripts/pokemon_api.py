import random
import requests

from pokemon_types import get_pokemon_type_translation


# Función para obtener el Pokémon del día
def get_pokemon_of_the_day():

    url = "https://pokeapi.co/api/v2/pokemon/" + str(random.randint(1, 898))

    response = requests.get(url)
    data = response.json()

    species = requests.get(data["species"]["url"]).json()

    # Curiosidad oficial
    curiosidad = "No disponible"

    for texto in species["flavor_text_entries"]:
        if texto["language"]["name"] == "es":
            curiosidad = (
                texto["flavor_text"]
                .replace("\n", " ")
                .replace("\f", " ")
            )
            break

    if curiosidad == "No disponible":
        for texto in species["flavor_text_entries"]:
            if texto["language"]["name"] == "en":
                curiosidad = (
                    texto["flavor_text"]
                    .replace("\n", " ")
                    .replace("\f", " ")
                )
                break

    nombre = data["name"].capitalize()

    tipos = [tipo["type"]["name"] for tipo in data["types"]]
    tipos_es = [get_pokemon_type_translation(tipo) for tipo in tipos]

    # Imágenes
    imagen = data["sprites"]["other"]["official-artwork"]["front_default"]
    imagen_shiny = data["sprites"]["other"]["official-artwork"]["front_shiny"]

    pokedex_num = data["id"]
    clase = data["species"]["name"]

    color_pokedex = species["color"]["name"]

    # Generación
    generaciones = {
        "generation-i": "I (Kanto)",
        "generation-ii": "II (Johto)",
        "generation-iii": "III (Hoenn)",
        "generation-iv": "IV (Sinnoh)",
        "generation-v": "V (Teselia)",
        "generation-vi": "VI (Kalos)",
        "generation-vii": "VII (Alola)",
        "generation-viii": "VIII (Galar)",
        "generation-ix": "IX (Paldea)"
    }

    generation = generaciones.get(
        species["generation"]["name"],
        species["generation"]["name"]
    )

    habitat = (
        species["habitat"]["name"].capitalize()
        if species["habitat"]
        else "Desconocido"
    )

    capture_rate = species["capture_rate"]

    # Probabilidad de captura (%)
    captura_porcentaje = round((capture_rate / 255) * 100, 1)

    base_happiness = species["base_happiness"]

    egg_groups = ", ".join(
        grupo["name"].capitalize()
        for grupo in species["egg_groups"]
    )

    stats = {
        stat["stat"]["name"]: stat["base_stat"]
        for stat in data["stats"]
    }

    altura = data["height"] / 10
    peso = data["weight"] / 10

    experiencia = data["base_experience"]

    # Experiencia necesaria para nivel 100
    growth = requests.get(species["growth_rate"]["url"]).json()
    experiencia_nivel_100 = growth["levels"][-1]["experience"]

    # Sexo
    gender_rate = species["gender_rate"]

    if gender_rate == -1:
        macho = None
        hembra = None
    else:
        hembra = round((gender_rate / 8) * 100, 1)
        macho = round(100 - hembra, 1)

    # Probabilidad shiny
    shiny_odds = "1 entre 4096"

    # Habilidades
    habilidades = []
    habilidad_oculta = None

    for habilidad in data["abilities"]:

        nombre_habilidad = (
            habilidad["ability"]["name"]
            .replace("-", " ")
            .capitalize()
        )

        if habilidad["is_hidden"]:
            habilidad_oculta = "✨ " + nombre_habilidad
        else:
            habilidades.append("⚡ " + nombre_habilidad)

    return (
        nombre,
        tipos_es,
        imagen,
        imagen_shiny,
        pokedex_num,
        clase,
        stats,
        altura,
        peso,
        experiencia,
        experiencia_nivel_100,
        habitat,
        color_pokedex,
        generation,
        capture_rate,
        captura_porcentaje,
        shiny_odds,
        macho,
        hembra,
        base_happiness,
        egg_groups,
        habilidades,
        habilidad_oculta,
        curiosidad,
    )
