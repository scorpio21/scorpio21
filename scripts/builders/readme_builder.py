from builders.pokemon_table import build_pokemon_table
from builders.pokemon_go import build_pokemon_go


def build_pokemon_info_block(
    fecha,
    pokemon_img_url,
    pokemon_shiny_url,
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
    experiencia_nivel_100,
    tipo_crecimiento,
    habitat,
    egg_groups,
    base_happiness,
    capture_rate,
    captura_porcentaje,
    shiny_odds,
    macho,
    hembra,
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
    cadena_evolucion,
    bst_html,
    stats_md,
    curiosidad,
):

    table_html = build_pokemon_table(
        pokemon_img_url=pokemon_img_url,
        shiny_img_url=pokemon_shiny_url,
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
        experience_to_level=experiencia_nivel_100,
        experience_growth=tipo_crecimiento,
        habitat=habitat,
        egg_groups=egg_groups,
        base_happiness=base_happiness,
        capture_rate=capture_rate,
        capture_text=f"{captura_porcentaje}%",
        shiny_odds=shiny_odds,
        male_rate=f"{macho}%" if macho is not None else "Sin género",
        female_rate=f"{hembra}%" if hembra is not None else "Sin género",
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
    )
    print("=========== TABLE_HTML ===========")
    print(table_html)
    print("=========== FIN TABLE_HTML =======")

    datos_interesantes_html = "\n".join(
        f"- {dato}"
        for dato in datos_interesantes
    )

    go_info = build_pokemon_go(nombre)

    return f"""<!-- POKEMON_INFO -->
<!-- Generated: {fecha} -->

<h2 align="center">🐱‍👤 Pokémon del día</h2>

<p align="center">
Descubre cada día un Pokémon diferente con su información completa.
</p>

---

{table_html}

---

## 💡 Curiosidad oficial

> {curiosidad}

---

## 💡 Datos interesantes

{datos_interesantes_html}

---

## 📱 Pokémon GO

{go_info}

---

<p align="center">

⭐ Datos obtenidos de <b>PokéAPI</b><br>
🤖 Generado automáticamente con Python<br>
🗓️ Última actualización: <b>{fecha[:10]}</b>

</p>

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
