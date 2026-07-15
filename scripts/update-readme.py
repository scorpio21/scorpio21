import datetime

from pokemon_api import get_pokemon_of_the_day
from evolution import get_evolution_chain
from rarity import get_rarity
from stats import compute_bst
from badges import (
    build_tipos_html,
    build_relations_html,
)
from quotes import get_gamer_quote
from builders.readme_builder import (
    build_pokemon_info_block,
    build_frase_info_block,
)
from updater import update_readme

# Obtener Pokémon y calcular variables
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
    habilidad_oculta,
) = get_pokemon_of_the_day()

cadena_evolucion = get_evolution_chain(pokedex_num)
rareza = get_rarity(tipos_es[0], pokedex_num)

tipos_html = build_tipos_html(tipos_es)
debilidades_html, resistencias_html, inmunidades_html = build_relations_html(tipos_es)
bst, nivel_bst, bst_html, stats_md = compute_bst(stats)

frase_del_dia = get_gamer_quote()
fecha = datetime.datetime.utcnow().isoformat()

pokemon_info_block = build_pokemon_info_block(
    fecha, pokemon_img_url, nombre, rareza, pokedex_num, tipos_html, debilidades_html,
    resistencias_html, inmunidades_html, clase, color_pokedex, altura, peso, experiencia,
    habitat, egg_groups, base_happiness, capture_rate, habilidades, habilidad_oculta,
    cadena_evolucion, bst_html, stats_md
)

frase_info_block = build_frase_info_block(fecha, frase_del_dia)
update_readme(pokemon_info_block, frase_info_block)
