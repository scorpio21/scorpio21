import random

from config import (
    colores_pokedex,
    rareza_texto,
    rareza_colores,
    rareza_iconos,
)


def build_pokemon_table(
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
    experience_to_level,
    habitat,
    egg_groups,
    base_happiness,
    capture_rate,
    capture_text,
    male_rate,
    female_rate,
    habilidades,
    habilidad_oculta,
    cadena_evolucion,
    bst_html,
    stats_md,
):
    habilidades_html = "<br>".join(
        f"🟢 {habilidad}" for habilidad in habilidades
    )

    if habilidad_oculta:
        habilidades_html += f"<br>⭐ {habilidad_oculta} (Oculta)"

    movimientos = ", ".join([
        random.choice(["Corte Psíquico", "Hoja Afilada", "Puño Fuego"]),
        random.choice(["Rayo Solar", "Ataque Psíquico", "Puño Trueno"]),
        random.choice(["Puño Trueno", "Puño Fuego"])
    ])

    return f"""
<table>

<tr>
<td><b>Imagen</b></td>
<td>
<img src="{pokemon_img_url}" width="250"><br>
<b>Normal</b>
</td>
</tr>

<tr>
<td><b>✨ Sprite Shiny</b></td>
<td>
<img src="{shiny_img_url}" width="250"><br>
<b>Shiny</b>
</td>
</tr>

<tr>
<td><b>Nombre</b></td>
<td>{rareza_iconos[rareza]} <b>{nombre}</b></td>
</tr>

<tr>
<td><b>Rareza</b></td>
<td>
<img src="https://img.shields.io/badge/{rareza_texto[rareza]}-{rareza_colores[rareza]}?style=flat-square">
</td>
</tr>

<tr>
<td><b>Nº Pokédex</b></td>
<td>#{pokedex_num}</td>
</tr>

<tr>
<td><b>🧬 Generación</b></td>
<td>{generation}</td>
</tr>

<tr>
<td><b>Tipo(s)</b></td>
<td>{tipos_html}</td>
</tr>

<tr>
<td><b>⚔️ Débil contra</b></td>
<td>{debilidades_html}</td>
</tr>

<tr>
<td><b>🛡️ Resiste</b></td>
<td>{resistencias_html}</td>
</tr>

<tr>
<td><b>✨ Inmune a</b></td>
<td>{inmunidades_html if inmunidades_html else "Ninguna"}</td>
</tr>

<tr>
<td><b>Clase</b></td>
<td>{clase.capitalize()}</td>
</tr>

<tr>
<td><b>🎨 Color Pokédex</b></td>
<td>{colores_pokedex[color_pokedex]}</td>
</tr>

<tr>
<td><b>📏 Altura</b></td>
<td>{altura} m</td>
</tr>

<tr>
<td><b>⚖️ Peso</b></td>
<td>{peso} kg</td>
</tr>

<tr>
<td><b>♂️ / ♀️</b></td>
<td>♂️ {male_rate} &nbsp;&nbsp; ♀️ {female_rate}</td>
</tr>

<tr>
<td><b>⭐ Experiencia Base</b></td>
<td>{experiencia}</td>
</tr>

<tr>
<td><b>📈 Para subir de nivel</b></td>
<td>{experience_to_level}</td>
</tr>

<tr>
<td><b>🌍 Hábitat</b></td>
<td>{habitat}</td>
</tr>

<tr>
<td><b>🥚 Grupo huevo</b></td>
<td>{egg_groups}</td>
</tr>

<tr>
<td><b>❤️ Amistad base</b></td>
<td>{base_happiness}</td>
</tr>

<tr>
<td><b>🎯 Probabilidad captura</b></td>
<td>{capture_text}</td>
</tr>

<tr>
<td><b>🎲 Ratio captura</b></td>
<td>{capture_rate}</td>
</tr>

<tr>
<td><b>💪 Habilidades</b></td>
<td>{habilidades_html}</td>
</tr>

<tr>
<td><b>🥊 Movimientos especiales</b></td>
<td>{movimientos}</td>
</tr>

<tr>
<td><b>🔄 Evolución</b></td>
<td>{cadena_evolucion}</td>
</tr>

<tr>
<td><b>🏆 Poder Total (BST)</b></td>
<td>{bst_html}</td>
</tr>

<tr>
<td><b>📊 Estadísticas Base</b></td>
<td>{stats_md}</td>
</tr>

</table>
"""