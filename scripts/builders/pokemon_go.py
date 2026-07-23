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

        pc_max = "No disponible"

        for tabla in soup.select("table.vitals-table"):
            texto = tabla.get_text(" ", strip=True)

            if "Max CP" in texto:
                for fila in tabla.select("tr"):
                    th = fila.find("th")
                    td = fila.find("td")

                    if th and td and "Max CP" in th.text:
                        pc_max = td.get_text(" ", strip=True)
                        break

                break

        return f"""## 📱 Pokémon GO

🏆 <b>PC máximo</b><br>
{pc_max}

<br>

🌐 <a href="{url}">Ver ficha completa</a>
"""

    except Exception:

        return f"""## 🌐 Más información

Puedes consultar información completa y actualizada de **{nombre}** en:

- 🇪🇸 [WikiDex](https://www.wikidex.net/wiki/{nombre})
- 📖 [Pokémon Database](https://pokemondb.net/pokedex/{nombre.lower()})
- 🧬 [Bulbapedia](https://bulbapedia.bulbagarden.net/wiki/{nombre}_(Pokémon))
"""