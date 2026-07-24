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
<table>

<tr>
<td><b>🏆 PC máximo</b></td>
<td>{pokemon["pc_max"]}</td>
</tr>

<tr>
<td><b>⚔️ Ataque</b></td>
<td>{pokemon["base_attack"]}</td>
</tr>

<tr>
<td><b>🛡️ Defensa</b></td>
<td>{pokemon["base_defense"]}</td>
</tr>

<tr>
<td><b>❤️ Resistencia</b></td>
<td>{pokemon["base_stamina"]}</td>
</tr>

<tr>
<td><b>🏷️ Tipos</b></td>
<td>{tipos_html}</td>
</tr>

<tr>
<td><b>⚡ Ataques rápidos</b></td>
<td>{fast_moves_html}</td>
</tr>

<tr>
<td><b>💥 Ataques cargados</b></td>
<td>{charged_moves_html}</td>
</tr>

</table>
"""