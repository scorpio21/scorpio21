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
❤️ <b>PS</b><br>
{barra_stat(stats['hp'])} {stats['hp']}<br>

⚔️ <b>Ataque</b><br>
{barra_stat(stats['attack'])} {stats['attack']}

🛡️ <b>Defensa</b><br>
{barra_stat(stats['defense'])} {stats['defense']}<br>

✨ <b>Ataque Especial</b><br>
{barra_stat(stats['special-attack'])} {stats['special-attack']}<br>

🛡️ <b>Defensa Especial</b><br>
{barra_stat(stats['special-defense'])} {stats['special-defense']}<br>

💨 <b>Velocidad</b><br>
{barra_stat(stats['speed'])} {stats['speed']}
"""

    return bst, nivel_bst, bst_html, stats_md
