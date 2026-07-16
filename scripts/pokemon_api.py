import random
import requests

from pokemon_types import get_pokemon_type_translation


# Función para obtener el Pokémon del día
def get_pokemon_of_the_day():

    url = "https://pokeapi.co/api/v2/pokemon/" + str(random.randint(1, 898))

    response = requests.get(url)
    data = response.json()

    species = requests.get(data["species"]["url"]).json()

    legendario = species["is_legendary"]
    mitico = species["is_mythical"]
    bebe = species["is_baby"]

    forma_regional = "No"

    formas = requests.get(species["varieties"][0]["pokemon"]["url"]).json()

    nombre_forma = formas["name"].lower()

    if any(x in nombre_forma for x in [
        "alola",
        "galar",
        "hisui",
        "paldea"
    ]):
        
        forma_regional = "Sí"
    
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

    # Probabilidad de captura
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

    # Experiencia nivel 100
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

        ability = requests.get(
            habilidad["ability"]["url"]
        ).json()

        descripcion = "Sin descripción"

        # Intentar español
        for entry in ability["effect_entries"]:
            if entry["language"]["name"] == "es":
                descripcion = entry["short_effect"]
                break

        # Si no existe, inglés
        if descripcion == "Sin descripción":
            for entry in ability["effect_entries"]:
                if entry["language"]["name"] == "en":
                    descripcion = entry["short_effect"]
                    break

        nombre_habilidad = (
            ability["name"]
            .replace("-", " ")
            .title()
        )

        for n in ability["names"]:
            if n["language"]["name"] == "es":
                nombre_habilidad = n["name"]
                break

        info = {
            "nombre": nombre_habilidad,
            "descripcion": descripcion
        }

        if habilidad["is_hidden"]:
            habilidad_oculta = info
        else:
            habilidades.append(info)

    # Movimientos reales
    movimientos = []

    disponibles = data["moves"]

    if disponibles:

        for move in random.sample(disponibles, min(4, len(disponibles))):

            move_data = requests.get(move["move"]["url"]).json()

            nombre_movimiento = (
                move_data["name"]
                .replace("-", " ")
                .title()
            )

            for n in move_data["names"]:
                if n["language"]["name"] == "es":
                    nombre_movimiento = n["name"]
                    break

            movimientos.append({
                "nombre": nombre_movimiento,
                "tipo": move_data["type"]["name"]
            })
    # Juegos donde aparece
    juegos = []

    for indice in data["game_indices"]:
        nombre = (
        indice["version"]["name"]
        .replace("-", " ")
        .title()
    )

    juegos.append(nombre)

    # Eliminar duplicados y ordenar
    juegos = sorted(list(set(juegos)))

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
        legendario,
        mitico,
        bebe,
        forma_regional,
        movimientos,
        juegos,
        curiosidad,
    )