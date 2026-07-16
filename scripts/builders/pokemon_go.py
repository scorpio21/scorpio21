import random


def build_pokemon_go(nombre):
    return f"""## 🌐 Más información

Puedes consultar información completa y actualizada de **{nombre}** en:

- 🇪🇸 [WikiDex](https://www.wikidex.net/wiki/{nombre})
- 📖 [Pokémon Database](https://pokemondb.net/pokedex/{nombre.lower()})
- 🧬 [Bulbapedia](https://bulbapedia.bulbagarden.net/wiki/{nombre}_(Pokémon))
"""
