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

    stat_names = {
        "hp": "❤️ PS",
        "attack": "⚔️ Ataque",
        "defense": "🛡️ Defensa",
        "special-attack": "✨ At. Especial",
        "special-defense": "🛡️ Def. Especial",
        "speed": "💨 Velocidad",
    }

    mejor = max(stats.items(), key=lambda x: x[1])
    peor = min(stats.items(), key=lambda x: x[1])

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
    stats_md = f"""❤️ PS {stats['hp']}<br>
    {barra_stat(stats['hp'])}<br>
    ⚔️ Ataque {stats['attack']}<br>
    {barra_stat(stats['attack'])}<br>
    🛡️ Defensa {stats['defense']}<br>
    {barra_stat(stats['defense'])}<br>
    ✨ At. Especial {stats['special-attack']}<br>
    {barra_stat(stats['special-attack'])}<br>
    🛡️ Def. Especial {stats['special-defense']}<br>
    {barra_stat(stats['special-defense'])}<br>
    💨 Velocidad {stats['speed']}<br>
    {barra_stat(stats['speed'])}
    <hr>

🏆 <b>Total Base:</b> {bst}<br>
🥇 <b>Mejor atributo:</b> {stat_names[mejor[0]]} ({mejor[1]})<br>
🥉 <b>Atributo más bajo:</b> {stat_names[peor[0]]} ({peor[1]})"""
    
    return bst, nivel_bst, bst_html, stats_md
