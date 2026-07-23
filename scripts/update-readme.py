import datetime

from pokemon_api import get_pokemon_of_the_day
from evolution import get_evolution_chain
from rarity import get_rarity
from stats import compute_bst
from shields.badges import (
    build_tipos_html,
    build_relations_html,
)
from quotes import get_gamer_quote
from builders.readme_builder import (
    build_pokemon_info_block,
    build_frase_info_block,
)
from updater import update_readme
from download_cry import download_cry

# Obtener Pokémon
(
    nombre,
    nombre_japones,
    especie,
    tipos_es,
    pokemon_img_url,
    pokemon_shiny_url,
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
    captura_barra,
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
) = get_pokemon_of_the_day()

download_cry(cry_url)

# Datos adicionales
# cadena_evolucion = get_evolution_chain(pokedex_num)
cadena_evolucion = get_evolution_chain(pokedex_num)
rareza = get_rarity(tipos_es[0], pokedex_num)

tipos_html = build_tipos_html(tipos_es)
debilidades_html, resistencias_html, inmunidades_html = build_relations_html(tipos_es)

bst, nivel_bst, bst_html, stats_md = compute_bst(stats)

# Obtener frase del día
frase_del_dia = get_gamer_quote()

# Actualizar README
fecha = datetime.datetime.now(datetime.timezone.utc).isoformat()


# Construir bloque README
pokemon_info_block = build_pokemon_info_block(
    fecha=fecha,
    pokemon_img_url=pokemon_img_url,
    pokemon_shiny_url=pokemon_shiny_url,
    nombre=nombre,
    nombre_japones=nombre_japones,
    especie=especie,
    rareza=rareza,
    cry_url=cry_url,
    pokedex_num=pokedex_num,
    tipos_html=tipos_html,
    debilidades_html=debilidades_html,
    resistencias_html=resistencias_html,
    inmunidades_html=inmunidades_html,
    generation=generation,
    anio_generacion=anio_generacion,
    juego_debut=juego_debut,
    musica_url=musica_url,
    clase=clase,
    color_pokedex=color_pokedex,
    altura=altura,
    peso=peso,
    experiencia=experiencia,
    experiencia_nivel_100=experiencia_nivel_100,
    tipo_crecimiento=tipo_crecimiento,
    habitat=habitat,
    egg_groups=egg_groups,
    base_happiness=base_happiness,
    capture_rate=capture_rate,
    captura_porcentaje=captura_porcentaje,
    captura_dificultad=captura_dificultad,
    captura_barra=f"{captura_porcentaje}%",
    shiny_odds=shiny_odds,
    macho=macho,
    hembra=hembra,
    habilidades=habilidades,
    habilidad_oculta=habilidad_oculta,
    legendario=legendario,
    mitico=mitico,
    bebe=bebe,
    forma_regional=forma_regional,
    movimientos=movimientos,
    objetos=objetos,
    juegos=juegos,
    cadena_evolucion=cadena_evolucion,
    bst_html=bst_html,
    stats_md=stats_md,
    datos_interesantes=datos_interesantes,
    curiosidad=curiosidad,
)

# Frase del día
frase_info_block = build_frase_info_block(
    fecha,
    frase_del_dia
)

# Actualizar README
update_readme(
    pokemon_info_block,
    frase_info_block
)
