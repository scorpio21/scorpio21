# Barras y cálculo de BST


def barra_stat(valor, maximo=255, ancho=10):
    bloques = round((valor / maximo) * ancho)

    if valor < 40:
        color = "🟥"
    elif valor < 70:
        color = "🟧"
    elif valor < 100:
        color = "🟨"
    elif valor < 130:
        color = "🟩"
    else:
        color = "🟦"

    return color * bloques + "⬜" * (ancho - bloques)


def barra_bst(valor, maximo=720, ancho=20):
    bloques = round(valor / maximo * ancho)
    if valor < 40:
        color = "🟥"
    elif valor < 70:
        color = "🟧"
    elif valor < 100:
        color = "🟨"
    elif valor < 130:
        color = "🟩"
    else:
        color = "🟦"

    return color * bloques + "⬜" * (ancho - bloques)


def compute_bst(stats):
    bst = sum(stats.values())

    if bst >= 680:
        nivel_bst = "🌟 Legendario"
    elif bst >= 600:
        nivel_bst = "💎 Pseudolegendario"
    elif bst >= 500:
        nivel_bst = "🔥 Muy fuerte"
    elif bst >= 400:
        nivel_bst = "⚔️ Fuerte"
    elif bst >= 300:
        nivel_bst = "👍 Normal"
    else:
        nivel_bst = "🌱 Básico"

    bst_html = f"""
{barra_bst(bst)}

<b>{bst} puntos</b><br>
{nivel_bst}
"""

    stats_md = f"""
    <table>

    <tr>
    <td>❤️ <b>PS</b></td>
    <td>{barra_stat(stats['hp'])}</td>
    <td><b>{stats['hp']}</b></td>
    </tr>

    <tr>
    <td>⚔️ <b>Ataque</b></td>
    <td>{barra_stat(stats['attack'])}</td>
    <td><b>{stats['attack']}</b></td>
    </tr>

    <tr>
    <td>🛡️ <b>Defensa</b></td>
    <td>{barra_stat(stats['defense'])}</td>
    <td><b>{stats['defense']}</b></td>
    </tr>

    <tr>
    <td>✨ <b>At. Especial</b></td>
    <td>{barra_stat(stats['special-attack'])}</td>
    <td><b>{stats['special-attack']}</b></td>
    </tr>

    <tr>
    <td>🛡️ <b>Def. Especial</b></td>
    <td>{barra_stat(stats['special-defense'])}</td>
    <td><b>{stats['special-defense']}</b></td>
    </tr>

    <tr>
    <td>💨 <b>Velocidad</b></td>
    <td>{barra_stat(stats['speed'])}</td>
    <td><b>{stats['speed']}</b></td>
    </tr>

    </table>
    """
    return bst, nivel_bst, bst_html, stats_md
