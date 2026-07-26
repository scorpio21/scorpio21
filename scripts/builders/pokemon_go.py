from pogo_api import get_pokemon_go_data
from shields.badges import (
    build_tipos_html,
    build_moves_html,
)

def build_pokemon_go(nombre):

    pokemon = get_pokemon_go_data(nombre)
    
    if not pokemon:
        return "⚠️ Información de Pokémon GO no disponible."

    tipos_html = build_tipos_html(
        pokemon.get("types", [])
    )

    fast_moves_html = build_moves_html(
        pokemon.get("fast_moves", [])
    )

    charged_moves_html = build_moves_html(
        pokemon.get("charged_moves", [])
    )

    return f"""
<table width="100%">
<tr>
<th align="left">📊 Estadísticas</th>
<th align="left">⚔️ Combate</th>
</tr>

<tr>

<td valign="top">

🏆 <b>PC máximo (Nivel 50)</b><br>
{pokemon["pc_max"]}

<br><br>

⚔️ <b>Ataque</b><br>
{pokemon["base_attack"]}

<br><br>

🛡️ <b>Defensa</b><br>
{pokemon["base_defense"]}

<br><br>

❤️ <b>Resistencia</b><br>
{pokemon["base_stamina"]}

<br><br>

🏷️ <b>Tipos</b><br>
{tipos_html}

</td>

</tr>
</table>

### ⚡ Ataques rápidos

{fast_moves_html}

<br>

### 💥 Ataques cargados

{charged_moves_html}
"""