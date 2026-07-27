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
### 📊 Estadísticas

🏆 **PC máximo (Nivel 50):** {pokemon["pc_max"]}

⚔️ **Ataque:** {pokemon["base_attack"]}

🛡️ **Defensa:** {pokemon["base_defense"]}

❤️ **Resistencia:** {pokemon["base_stamina"]}

🏷️ **Tipos:** {tipos_html}

---

### ⚡ Ataques rápidos

{fast_moves_html}

---

### 💥 Ataques cargados

{charged_moves_html}
"""