import requests
from bs4 import BeautifulSoup


def build_pokemon_go(nombre):

    url = f"https://pokemondb.net/pokedex/{nombre.lower()}"

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    try:
        r = requests.get(url, headers=headers, timeout=10)

        if r.status_code != 200:
            raise Exception()

        soup = BeautifulSoup(r.text, "html.parser")

        return f"""Página encontrada ✅

🌐 {url}
"""

    except Exception:

        return f"""## 🌐 Más información

Puedes consultar información completa y actualizada de **{nombre}** en:

- 🇪🇸 [WikiDex](https://www.wikidex.net/wiki/{nombre})
- 📖 [Pokémon Database](https://pokemondb.net/pokedex/{nombre.lower()})
- 🧬 [Bulbapedia](https://bulbapedia.bulbagarden.net/wiki/{nombre}_(Pokémon))
"""
