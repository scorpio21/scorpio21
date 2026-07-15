import random
from datetime import datetime

from config import (
    colores_pokedex,
    rareza_iconos,
    rareza_texto,
    rareza_colores,
)
from pokemon_api import get_pokemon_of_the_day
from evolution import get_evolution_chain
from rarity import get_rarity
from stats import barra_stat, barra_bst, compute_bst
from badges import (
    build_nombre_md,
    build_badge_rareza,
    build_tipos_html,
    build_relations_html,
)
from quotes import get_gamer_quote
from builders.readme_builder import build_pokemon_info_block, build_frase_info_block
from builders.pokemon_table import build_pokemon_table
from builders.pokemon_story import build_pokemon_story
from builders.pokemon_trivia import build_pokemon_trivia
from builders.pokemon_go import build_pokemon_go
from updater import update_readme

# Obtener Pokémon del día
(
    nombre,
    tipos_es,
    pokemon_img_url,
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
) = get_pokemon_of_the_day()

# obtiene la cadena
cadena_evolucion = get_evolution_chain(pokedex_num)

# Rareza + color
rareza = get_rarity(tipos_es[0], pokedex_num)

# Nombre y badge (se mantiene la variable aunque no se use en README)
nombre_md = build_nombre_md(rareza, nombre)
badge_rareza = build_badge_rareza(nombre, rareza)

# Tipos y relaciones HTML
tipos_html = build_tipos_html(tipos_es)
debilidades_html, resistencias_html, inmunidades_html = build_relations_html(tipos_es)

# Stats y BST
bst, nivel_bst, bst_html, stats_md = compute_bst(stats)

# Frase gamer
frase_del_dia = get_gamer_quote()

# Timestamp
fecha = datetime.utcnow().isoformat()

# Bloque Pokémon (tabla HTML)
pokemon_info_block = build_pokemon_info_block(
    fecha=fecha,
    pokemon_img_url=pokemon_img_url,
    nombre=nombre,
    rareza=rareza,
    pokedex_num=pokedex_num,
    tipos_html=tipos_html,
    debilidades_html=debilidades_html,
    resistencias_html=resistencias_html,
    inmunidades_html=inmunidades_html,
    clase=clase,
    color_pokedex=color_pokedex,
    altura=altura,
    peso=peso,
    experiencia=experiencia,
    habitat=habitat,
    egg_groups=egg_groups,
    base_happiness=base_happiness,
    capture_rate=capture_rate,
    habilidades=habilidades,
    habilidad_oculta=habilidad_oculta,
    cadena_evolucion=cadena_evolucion,
    bst_html=bst_html,
    stats_md=stats_md
)

# Bloque frase gamer
frase_info_block = build_frase_info_block(fecha, frase_del_dia)

# Actualizar README con regex
update_readme(pokemon_info_block, frase_info_block)
