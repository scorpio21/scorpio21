import random
import requests
import os
import shutil


from translation.pokemon_types import get_pokemon_type_translation
from experience_growth import EXPERIENCE_GROWTH
from translation.item_translations import ITEM_TRANSLATIONS
from music.game_music import get_game_music
from shields.color_badges import build_color_badge
from translation.habitat_translations import HABITAT_TRANSLATIONS
from translation.game_translations import GAME_TRANSLATIONS

# Función para obtener el Pokémon del día
def get_pokemon_of_the_day():

    url = "https://pokeapi.co/api/v2/pokemon/" + str(random.randint(1, 898))

    response = requests.get(url)
    data = response.json()

    species = requests.get(data["species"]["url"]).json()
    
    # Clase del Pokémon
    clase = "Desconocida"

    for genero in species["genera"]:
        if genero["language"]["name"] == "es":
            clase = genero["genus"].replace("Pokémon ", "")
            break

    if clase == "Desconocida":
        for genero in species["genera"]:
            if genero["language"]["name"] == "en":
                clase = genero["genus"]
                break

    # Nombre japonés
    nombre_japones = "Desconocido"

    for n in species["names"]:
        if n["language"]["name"] == "ja":
            nombre_japones = n["name"]
            break

    legendario = species["is_legendary"]
    mitico = species["is_mythical"]
    bebe = species["is_baby"]

    forma_regional = "No"

    formas = requests.get(species["varieties"][0]["pokemon"]["url"]).json()
    nombre_forma = formas["name"].lower()

    if "alola" in nombre_forma:
        forma_regional = "Alola"
    elif "galar" in nombre_forma:
        forma_regional = "Galar"
    elif "hisui" in nombre_forma:
        forma_regional = "Hisui"
    elif "paldea" in nombre_forma:
        forma_regional = "Paldea"
    
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

    especie = species["name"].replace("-", " ").title()

    tipos = [tipo["type"]["name"] for tipo in data["types"]]
    tipos_es = [get_pokemon_type_translation(tipo) for tipo in tipos]

    # Imágenes
    imagen = data["sprites"]["other"]["official-artwork"]["front_default"]
    imagen_shiny = data["sprites"]["other"]["official-artwork"]["front_shiny"]
    
    # Sonido del Pokémon
    cry_url = data["cries"]["latest"]
    
    if cry_url is None:
        cry_url = data["cries"]["legacy"]

    pokedex_num = data["id"]

    color_pokedex = build_color_badge(species["color"]["name"])

    # Generación
    generaciones = {
        "generation-i": ("I (Kanto)", 1996),
        "generation-ii": ("II (Johto)", 1999),
        "generation-iii": ("III (Hoenn)", 2002),
        "generation-iv": ("IV (Sinnoh)", 2006),
        "generation-v": ("V (Teselia)", 2010),
        "generation-vi": ("VI (Kalos)", 2013),
        "generation-vii": ("VII (Alola)", 2016),
        "generation-viii": ("VIII (Galar)", 2019),
        "generation-ix": ("IX (Paldea)", 2022),
    }

    generation, anio_generacion = generaciones.get(
        species["generation"]["name"],
        (species["generation"]["name"], "Desconocido")
    )

    juego_debut, musica_url = get_game_music(generation)

    if species["habitat"]:
        habitat = HABITAT_TRANSLATIONS.get(
            species["habitat"]["name"],
            species["habitat"]["name"].replace("-", " ").title()
        )
    else:
        habitat = "❓ Desconocido"

    capture_rate = species["capture_rate"]

    # Probabilidad de captura
    captura_porcentaje = round((capture_rate / 255) * 100, 1)

    if capture_rate >= 200:
        captura_dificultad = ("Muy fácil", "brightgreen")
    elif capture_rate >= 120:
        captura_dificultad = ("Fácil", "green")
    elif capture_rate >= 60:
        captura_dificultad = ("Normal", "yellow")
    elif capture_rate >= 20:
        captura_dificultad = ("Difícil", "orange")
    else:
        captura_dificultad = ("Muy difícil", "red")

    base_happiness = species["base_happiness"]
    
    print([g["name"] for g in species["egg_groups"]])

    egg_groups = []

    for grupo in species["egg_groups"]:

        grupo_data = requests.get(grupo["url"]).json()

        nombre_grupo = grupo["name"].capitalize()

        for n in grupo_data["names"]:
            if n["language"]["name"] == "es":
                nombre_grupo = n["name"]
                break

        egg_groups.append(nombre_grupo)

    egg_groups = ", ".join(egg_groups)

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

    tipo_crecimiento = EXPERIENCE_GROWTH.get(
        growth["name"],
        growth["name"].capitalize()
    )

    # ID de la tasa de crecimiento
    growth_rate_id = growth["name"]

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

    #==========================
    # DATOS INTERESANTES
    datos_interesantes = [
        f"🧬 Introducido en la generación {generation}.",
        f"🎨 Su color en la Pokédex es {color_pokedex}.",
        f"📏 Mide {altura} m.",
        f"⚖️ Pesa {peso} kg.",
        f"🥚 Pertenece al grupo huevo {egg_groups}.",
        f"❤️ Amistad base: {base_happiness}.",
        f"🎯 Ratio de captura: {capture_rate}.",
        f"📈 Crecimiento: {tipo_crecimiento}.",
    ]

    random.shuffle(datos_interesantes)
    datos_interesantes = datos_interesantes[:3]

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
    # ==========================
    # Objetos que puede llevar 
    # ==========================

    objetos = []

    for item in data["held_items"]:
        
        nombre_objeto = item["item"]["name"]

        nombre_objeto = ITEM_TRANSLATIONS.get(
            nombre_objeto,
            nombre_objeto.replace("-", " ").title()
        )

        for version in item["version_details"]:

            objetos.append({
                "id": item["item"]["name"],
                "nombre": nombre_objeto,
                "probabilidad": version["rarity"]
            })
            
    # Juegos donde aparece
    juegos = []

    
    for entrada in species["flavor_text_entries"]:

        if entrada["language"]["name"] != "es":
            continue
    
        clave = entrada["version"]["name"]

        print(clave)  # <-- para ver qué nombres llegan

        nombre_juego = GAME_TRANSLATIONS.get(
            clave.replace("-", " ").title(),
            clave.replace("-", " ").title()
        )

        if nombre_juego not in juegos:
            juegos.append(nombre_juego)

        # Si no hay juegos en las entradas de la Pokédex,
        # usar el juego de debut
        if not juegos:
            juegos = [juego_debut]

        # Ordenar alfabéticamente
        juegos.sort()

    #==========================
    # Retornar todos los datos
    #==========================
    
    print("🎮 game_indices:", data["game_indices"])
    print("🎮 juegos traducidos:", juegos)

    return (
        nombre,
        nombre_japones,
        especie,
        tipos_es,
        imagen,
        imagen_shiny,
        cry_url,
        pokedex_num,
        clase,
        stats,
        altura,
        peso,
        experiencia,
        experiencia_nivel_100,
        tipo_crecimiento,
        habitat,
        color_pokedex,
        generation,
        anio_generacion,
        juego_debut,
        musica_url,
        capture_rate,
        captura_porcentaje,
        captura_dificultad,
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
        objetos,
        juegos,
        datos_interesantes,
        curiosidad,
    )