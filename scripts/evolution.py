import requests
from item_translations import ITEM_TRANSLATIONS
from pokemon_types import get_pokemon_type_translation
from badges import build_tipos_html

# Obtener la cadena de evolución
def get_evolution_chain(pokedex_num):
    try:
        species = requests.get(
            f"https://pokeapi.co/api/v2/pokemon-species/{pokedex_num}"
        ).json()

        evo_data = requests.get(
            species["evolution_chain"]["url"]
        ).json()

        html = """
<table align="center">
<tr>
"""

        def recorrer(cadena):
            nombre = cadena["species"]["name"].capitalize()

            pokemon = requests.get(
                f"https://pokeapi.co/api/v2/pokemon/{cadena['species']['name']}"
            ).json()
            
            numero = pokemon["id"]

            tipos_es = [
                get_pokemon_type_translation(t["type"]["name"])
                for t in pokemon["types"]
            ]

            tipos_html = build_tipos_html(tipos_es)
            tipos_html = tipos_html.replace(
                'width="22"',
                'width="18"'
            )

            imagen = (
                f"https://img.pokemondb.net/artwork/large/"
                f"{nombre.lower()}.jpg"
            )
           
            html_part = f"""
<td align="center" valign="top">

<div style="
display:flex;
flex-direction:column;
align-items:center;
">

<div style="
width:78px;
height:78px;
border-radius:50%;
overflow:hidden;
background:#98C2D1;
border:2px solid #492A49;
display:flex;
align-items:center;
justify-content:center;
">
    <img src="{imagen}" style="width:62px; height:auto;">
</div>

<div style="
margin-top:8px;
font-size:12px;
color:#9aa6b2;
">
</div>

<div style="
margin-top:6px;
padding:6px 10px;
background:#EAF4F7;
border-radius:8px;
min-width:95px;
">

<b style="font-size:15px;color:#000;">
{nombre}
</b>

<br>

<small style="
color:#555;
font-weight:bold;
">
#{numero:04d}
</small>

<br><br>

{tipos_html}

</div>

</div>


</td>
"""

            for evo in cadena["evolves_to"]:

                detalle = evo["evolution_details"][0] if evo["evolution_details"] else {}

                texto = ""

                if detalle.get("min_level"):
                    texto = f"Nivel {detalle['min_level']}"

                elif detalle.get("item"):

                    item = detalle["item"]["name"]

                    texto = ITEM_TRANSLATIONS.get(
                        item,
                        item.replace("-", " ").title()
                )

                elif detalle.get("trigger", {}).get("name") == "trade":
                    texto = "Intercambio"

                elif detalle.get("min_happiness"):
                    texto = "Amistad"

                elif detalle.get("known_move"):
                    texto = (
                        "Aprende "
                        + detalle["known_move"]["name"]
                        .replace("-", " ")
                        .title()
                    )

                elif detalle.get("held_item"):
                    texto = (
                        "Con "
                        + detalle["held_item"]["name"]
                        .replace("-", " ")
                        .title()
                    )

                elif detalle.get("time_of_day"):
                    texto = detalle["time_of_day"].capitalize()

                elif detalle.get("needs_overworld_rain"):
                    texto = "Lluvia"

                elif detalle.get("turn_upside_down"):
                    texto = "Consola boca abajo"

                elif detalle.get("min_affection"):
                    texto = "Afecto"

                elif detalle.get("min_beauty"):
                    texto = "Belleza"

                elif detalle.get("party_species"):
                    texto = (
                        "Con "
                        + detalle["party_species"]["name"]
                        .capitalize()
                    )

                elif detalle.get("party_type"):
                    texto = (
                        "Tipo "
                        + detalle["party_type"]["name"]
                        .capitalize()
                    )

                elif detalle.get("relative_physical_stats") == 1:
                    texto = "Ataque > Defensa"

                elif detalle.get("relative_physical_stats") == -1:
                    texto = "Ataque < Defensa"

                elif detalle.get("relative_physical_stats") == 0:
                    texto = "Ataque = Defensa"

                elif nombre == "Meltan":
                    texto = "400 Caramelos (Pokémon GO)"

                elif detalle.get("trade_species"):
                    texto = (
                        "Intercambiar por "
                        + detalle["trade_species"]["name"]
                        .capitalize()
                    )

                elif detalle.get("trigger", {}).get("name") == "use-item":
                    texto = "Usar objeto"

                else:
                    texto = "Evoluciona"

                html_part += f"""
<td align="center" valign="middle" style="width:auto; padding:10px;">

<div style="
font-size:14px;
font-weight:bold;
color:#FFD54F;
margin-bottom:10px;
">

{texto}

</div>

<div style="
font-size:32px;
font-weight:bold;
">

➜

</div>

</td>
"""

                html_part += recorrer(evo)

            return html_part

        html += recorrer(evo_data["chain"])
        html += """
</tr>
</table>
"""

        return html

    except Exception as e:
        return f"Error obteniendo evolución: {e}"
        