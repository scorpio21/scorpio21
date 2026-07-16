from builders.pokemon_table import build_pokemon_table
from builders.pokemon_story import build_pokemon_story
from builders.pokemon_trivia import build_pokemon_trivia
from builders.pokemon_go import build_pokemon_go


def build_pokemon_info_block(
    fecha,
    pokemon_img_url,
    shiny_img_url,
    nombre,
    rareza,
    pokedex_num,
    tipos_html,
    debilidades_html,
    resistencias_html,
    inmunidades_html,
    generation,
    clase,
    color_pokedex,
    altura,
    peso,
    experiencia,
    experiencia_nivel,
    habitat,
    egg_groups,
    gender_rate,
    base_happiness,
    capture_rate,
    capture_percent,
    habilidades,
    habilidad_oculta,
    cadena_evolucion,
    bst_html,
    stats_md,
):
    table_html = build_pokemon_table(
        pokemon_img_url=pokemon_img_url,
        shiny_img_url=shiny_img_url,
        nombre=nombre,
        rareza=rareza,
        pokedex_num=pokedex_num,
        tipos_html=tipos_html,
        debilidades_html=debilidades_html,
        resistencias_html=resistencias_html,
        inmunidades_html=inmunidades_html,
        generation=generation,
        clase=clase,
        color_pokedex=color_pokedex,
        altura=altura,
        peso=peso,
        experiencia=experiencia,
        experiencia_nivel=experiencia_nivel,
        habitat=habitat,
        egg_groups=egg_groups,
        gender_rate=gender_rate,
        base_happiness=base_happiness,
        capture_rate=capture_rate,
        capture_percent=capture_percent,
        habilidades=habilidades,
        habilidad_oculta=habilidad_oculta,
        cadena_evolucion=cadena_evolucion,
        bst_html=bst_html,
        stats_md=stats_md,
    )

    story = build_pokemon_story(nombre)
    trivia = build_pokemon_trivia(nombre)
    go_info = build_pokemon_go(nombre)

    return f"""<!-- POKEMON_INFO -->
<!-- Generated: {fecha} -->

<h2 align="center">🐱‍👤 Pokémon del día</h2>

<p align="center">
Descubre cada día un Pokémon diferente con sus estadísticas, evolución y curiosidades.
</p>

---

{table_html}

---

## 📖 Historia

{story}

---

## 🧠 ¿Sabías que...?

{trivia}

---

## 📱 Pokémon GO

{go_info}

<!-- END_POKEMON_INFO -->
"""


def build_frase_info_block(fecha, frase_del_dia):
    return f"""<!-- FRASE_GAMER -->
<!-- Generated: {fecha} -->

---

## 💬 Frase Gamer del día

> *"{frase_del_dia}"*

<!-- END_FRASE_GAMER -->
"""