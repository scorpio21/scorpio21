#print(">>> EJECUTANDO pokemon_table_template.py <<<")

#==========================
# FUNCIONES
#==========================

from color_badges import build_color_badge
from badges import build_cry_badge
#==========================
# FUNCIONES
#=========================

def render_table(
    pokemon_img_url,
    shiny_img_url,
    cry_url,
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
    experience_growth,
    habitat,
    egg_groups,
    base_happiness,
    capture_rate,
    capture_text,
    captura_barra,
    shiny_odds,
    male_rate,
    female_rate,
    habilidades_html,
    objetos_html,
    movimientos_html,
    cadena_evolucion,
    juegos_html,
    bst_html,
    stats_md,
    rareza_iconos,
    rareza_texto,
    rareza_colores,
    legendario,
    mitico,
    bebe,
    forma_regional,
):
    # print(">>> render_table:", repr(stats_md))

    # print(repr(stats_md))

    #==========================
    # TABLA DE INFORMACIÓN
    #==========================
    
    return f"""
<table width="100%">

<tr>
<td colspan="2" align="center">

<table>
<tr>

<td align="center">
<b>Normal</b><br>
<img src="{pokemon_img_url}" width="220">
</td>

<td width="40"></td>

<td align="center">
<b>✨ Shiny</b><br>
<img src="{shiny_img_url}" width="220">
</td>

</tr>
</table>

</td>
</tr>

<tr>
<td colspan="2" align="center">
<a href="https://raw.githubusercontent.com/scorpio21/scorpio21/main/cries/cry.ogg">
<img src="{build_cry_badge(nombre)}" alt="Escuchar grito">
</a>
</td>
</tr>

<tr>
<td colspan="2"><h3>📋 Información General</h3></td>
</tr>

<tr>
<td><b>Nombre</b></td>
<td>{rareza_iconos[rareza]} <b>{nombre}</b></td>
</tr>

<tr>
<td><b>🇯🇵 Nombre japonés</b></td>
<td>{nombre_japones}</td>
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
<td colspan="2"><h3>🧬 Biología</h3></td>
</tr>

<tr>
<td><b>Clase</b></td>
<td>{clase.capitalize()}</td>
</tr>

<tr>
<td><b>⭐ Legendario</b></td>
<td>{"✅ Sí" if legendario else "❌ No"}</td>
</tr>

<tr>
<td><b>🌟 Mítico</b></td>
<td>{"✅ Sí" if mitico else "❌ No"}</td>
</tr>

<tr>
<td><b>👶 Bebé</b></td>
<td>{"✅ Sí" if bebe else "❌ No"}</td>
</tr>

<tr>
<td><b>🌍 Forma regional</b></td>
<td>{forma_regional}</td>
</tr>

<tr>
<td><b>🎨 Color</b></td>
<td>{build_color_badge(color_pokedex)}</td>
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
<td>♂️ {male_rate} &nbsp;&nbsp;&nbsp; ♀️ {female_rate}</td>
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
<td colspan="2"><h3>⚔️ Combate</h3></td>
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
<td><b>🎯 Captura</b></td>
<td>{captura_barra}<br>{capture_text}</td>
</tr>

<tr>
<td><b>🎲 Ratio captura</b></td>
<td>{capture_rate}</td>
</tr>

<tr>
<td><b>✨ Probabilidad Shiny</b></td>
<td>{shiny_odds}</td>
</tr>

<tr>
<td><b>💪 Habilidades</b></td>
<td>{habilidades_html}</td>
</tr>

<tr>
<td><b>📦 Objetos</b></td>
<td>{objetos_html}</td>
</tr>

<tr>
<td><b>🥊 Movimientos</b></td>
<td>{movimientos_html}</td>
</tr>

<tr>
<td><b>🔄 Evolución</b></td>
<td>{cadena_evolucion}</td>
</tr>

<tr>
<td><b>🎮 Juegos</b></td>
<td>{juegos_html}</td>
</tr>

<tr>
<td colspan="2"><h3>📊 Estadísticas</h3></td>
</tr>

<tr>
<td><b>⭐ Experiencia Base</b></td>
<td>{experiencia}</td>
</tr>

<tr>
<td><b>📈 Nivel 100</b></td>
<td>
💠 <b>{f"{experience_to_level:,}".replace(",", ".")} XP</b><br>
<small>Necesaria para alcanzar el nivel 100</small>
</td>
</tr>

<tr>
<td><b>📚 Crecimiento</b></td>
<td>{experience_growth}</td>
</tr>

<tr>
<td><b>🏆 Poder Total (BST)</b></td>
<td>{bst_html}</td>
</tr>

<tr>
<td><b>📊 Estadísticas Base</b></td>
<td style="background:red">{stats_md}</td>
</tr>

</table>
"""
