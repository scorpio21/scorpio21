import requests


# Obtener la cadena de evolución
def get_evolution_chain(pokedex_num):
    try:
        species = requests.get(
            f"https://pokeapi.co/api/v2/pokemon-species/{pokedex_num}"
        ).json()

        evo_data = requests.get(
            species["evolution_chain"]["url"]
        ).json()

        evoluciones = []

        def recorrer(cadena):
            evoluciones.append(cadena["species"]["name"].capitalize())
            for evo in cadena["evolves_to"]:
                recorrer(evo)

        recorrer(evo_data["chain"])

        # Si solo tiene una forma, no evoluciona
        if len(evoluciones) == 1:
            return "No evoluciona"

        # Si hay 4 o menos evoluciones → una sola fila
        # Si hay más → dividir en dos filas
        if len(evoluciones) <= 4:
            filas = [evoluciones]
        else:
            filas = [
                evoluciones[:4],
                evoluciones[4:]
            ]

        html = "<table>"

        for fila in filas:
            html += "<tr>"

            for i, nombre in enumerate(fila):
                imagen = f"https://img.pokemondb.net/artwork/large/{nombre.lower()}.jpg"

                html += f"""
<td align="center">
    <img src="{imagen}" width="70"><br>
    <small><b>{nombre}</b></small>
</td>
"""

                # Flecha entre evoluciones
                if i < len(fila) - 1:
                    html += '<td align="center"><b>➡️</b></td>'

            html += "</tr>"

        html += "</table>"

        return html

    except Exception as e:
        return f"Error obteniendo evolución: {e}"
