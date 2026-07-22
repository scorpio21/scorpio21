from builders.pokemon_table import build_pokemon_table
from builders.pokemon_go import build_pokemon_go

def build_pokemon_info_block(
    fecha,
    pokemon_img_url,
    pokemon_shiny_url,
    cry_url,
    nombre,
    nombre_japones,
    especie,
    rareza,
    pokedex_num,
    tipos_html,
    debilidades_html,
    resistencias_html,
    inmunidades_html,
    generation,
    anio_generacion,
    juego_debut,
    musica_url,
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
    captura_dificultad,
    captura_barra,
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
    #==========================
    # JUEGOS
    #==========================

    # juegos_html = "<br>".join(f"🎮 {j}" for j in juegos) if juegos else "No disponible"

    #==========================
    # TABLA DE INFORMACIÓN
    #==========================

    table_html = build_pokemon_table(
        pokemon_img_url=pokemon_img_url,
        shiny_img_url=pokemon_shiny_url,
        cry_url=cry_url,
        nombre=nombre,
        nombre_japones=nombre_japones,
        especie=especie,
        rareza=rareza,
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
        experience_to_level=experiencia_nivel_100,
        experience_growth=tipo_crecimiento,
        habitat=habitat,
        egg_groups=egg_groups,
        base_happiness=base_happiness,
        capture_rate=capture_rate,
        capture_text=f"{captura_porcentaje}%",
        captura_barra=captura_barra,
        captura_dificultad=captura_dificultad,
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
    # print("=========== TABLE_HTML ===========")
    # print(table_html)
    # print("=========== FIN TABLE_HTML =======")

    datos_interesantes_html = "<br>".join(
        dato
        for dato in datos_interesantes
    )

    go_info = build_pokemon_go(nombre)

    # print("=========== POKEMON_INFO_BLOCK ===========")
    # print(table_html)
    # print("=========== FIN POKEMON_INFO_BLOCK =======")

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

<table>
<tr>
<td>

> 💬 **{curiosidad}**

</td>
</tr>
</table>

---

## 💡 Datos interesantes

<table>
<tr>
<td>

{datos_interesantes_html}

</td>
</tr>
</table>

---

## 📱 Pokémon GO

{go_info}

---

<p align="center">

⭐ Datos oficiales obtenidos de <b>PokéAPI</b><br>
📊 Aproximadamente el <b>90%</b> del contenido procede de datos oficiales y el <b>10%</b> corresponde a contenido generado automáticamente.<br>
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
