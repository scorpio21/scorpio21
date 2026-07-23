from pogo_api import get_pokemon_go_data


def build_pokemon_go(nombre):

    pokemon = get_pokemon_go_data(nombre)

    if pokemon is None:
        return "No hay datos de Pokémon GO."

    return f"""
🏆 <b>PC máximo</b><br>
{pokemon["pc_max"]}

<br>

⚔️ <b>Ataque</b><br>
{pokemon["base_attack"]}

<br>

🛡️ <b>Defensa</b><br>
{pokemon["base_defense"]}

<br>

❤️ <b>Resistencia</b><br>
{pokemon["base_stamina"]}

<br>

🏷️ <b>Tipos</b><br>
{", ".join(pokemon["types"])}

<br>

⚡ <b>Ataques rápidos</b><br>
{", ".join(pokemon["fast_moves"])}

<br>

💥 <b>Ataques cargados</b><br>
{", ".join(pokemon["charged_moves"])}
"""