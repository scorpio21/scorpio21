# print(">>> EJECUTANDO builders/pokemon_table.py <<<")

#==========================
# FUNCIONES
#=========================

from config import (
    rareza_texto,
    rareza_colores,
    rareza_iconos,
)

from color_badges import COLOR_BADGES
from move_colors import MOVE_COLORS
from urllib.parse import quote
from builders.pokemon_table_template import render_table
from item_icons import ITEM_ICON_URL
from experience_growth_badges import EXPERIENCE_GROWTH_BADGES

#==========================
# FUNCIONES
#=========================

def barra_porcentaje(texto):
    try:
        valor = float(texto.replace("%", "").strip())
    except Exception:
        valor = 0

    bloques = round(valor / 10)
    return "🟩" * bloques + "⬜" * (10 - bloques)


def build_pokemon_table(
    pokemon_img_url,
    shiny_img_url,
    cry_url,
    nombre,
    nombre_japones,
    rareza,
    pokedex_num,
    tipos_html,
    debilidades_html,
    resistencias_html,
    inmunidades_html,
    generation,
    juego_debut,
    musica_url,
    clase,
    color_pokedex,
    altura,
    peso,
    experiencia,
    experience_to_level,
    experience_growth,
    habitat,
    egg_groups,
    base_happiness,
    capture_rate,
    capture_text,
    shiny_odds,
    male_rate,
    female_rate,
    habilidades,
    habilidad_oculta,
    legendario,
    mitico,
    bebe,
    forma_regional,
    movimientos,
    objetos,
    juegos,
    cadena_evolucion,
    bst_html,
    stats_md,
):

    # ==========================
    # HABILIDADES
    # ==========================

    habilidades_html = ""

    for h in habilidades:
        habilidades_html += (
            f"🟢 ⚡ <b>{h['nombre']}</b><br>"
            f"<small>{h['descripcion']}</small><br><br>"
        )

    if habilidad_oculta:
        habilidades_html += (
            f"⭐ ✨ <b>{habilidad_oculta['nombre']}</b> (Oculta)<br>"
            f"<small>{habilidad_oculta['descripcion']}</small>"
        )

    # ==========================
    # MOVIMIENTOS
    # ==========================

    movimientos_html = " ".join(
        f'<img src="https://img.shields.io/badge/'
        f'{quote(m["nombre"])}-'
        f'{MOVE_COLORS.get(m["tipo"], "777777")}'
        f'?style=flat-square">'
        for m in movimientos
    )

    # ==========================
    # OBJETOS
    # ==========================
    objetos_unicos = []

    for obj in objetos:
        if obj not in objetos_unicos:
            objetos_unicos.append(obj)

    if objetos_unicos:

        objetos_html = "<br>".join(

            f'<img src="{ITEM_ICON_URL.format(o["id"])}" width="28" height="28"> '
            f'<b>{o["nombre"]}</b> '
            f'({o["probabilidad"]}%)'

            for o in objetos_unicos
        )

    else:

        objetos_html = "No puede llevar objetos."

    captura_barra = barra_porcentaje(capture_text)

    juegos_html = "<br>".join(
        f"🎮 {juego}"
        for juego in juegos
    )

    badge = EXPERIENCE_GROWTH_BADGES.get(
        experience_growth,
        (experience_growth, "lightgrey")
    )

    experience_growth_html = (
        f'<img src="https://img.shields.io/badge/'
        f'{quote(badge[0])}-{badge[1]}?style=flat-square">'
    )
    
    region = generation.split("(")[1].replace(")", "")
    
    # print(">>> stats_md =", repr(stats_md))

    #==========================
    # TABLA DE INFORMACIÓN
    #==========================
    
    return render_table(
        pokemon_img_url=pokemon_img_url,
        shiny_img_url=shiny_img_url,
        cry_url=cry_url,
        nombre=nombre,
        nombre_japones=nombre_japones,
        rareza=rareza,
        pokedex_num=pokedex_num,
        tipos_html=tipos_html,
        debilidades_html=debilidades_html,
        resistencias_html=resistencias_html,
        inmunidades_html=inmunidades_html,
        generation=generation,
        juego_debut=juego_debut,
        musica_url=musica_url,
        region=region,
        clase=clase,
        color_pokedex=color_pokedex,
        altura=altura,
        peso=peso,
        experiencia=experiencia,
        experience_to_level=experience_to_level,
        experience_growth=experience_growth_html,
        habitat=habitat,
        egg_groups=egg_groups,
        base_happiness=base_happiness,
        capture_rate=capture_rate,
        capture_text=capture_text,
        captura_barra=captura_barra,
        shiny_odds=shiny_odds,
        male_rate=male_rate,
        female_rate=female_rate,
        habilidades_html=habilidades_html,
        objetos_html=objetos_html,
        movimientos_html=movimientos_html,
        cadena_evolucion=cadena_evolucion,
        juegos_html=juegos_html,
        bst_html=bst_html,
        stats_md=stats_md,
        rareza_iconos=rareza_iconos,
        rareza_texto=rareza_texto,
        rareza_colores=rareza_colores,
        legendario=legendario,
        mitico=mitico,
        bebe=bebe,
        forma_regional=forma_regional,
    )