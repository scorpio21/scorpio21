GAME_MUSIC = {

    "I (Kanto)": (
        "Pokémon Rojo / Azul",
        "https://www.youtube.com/results?search_query=Pokemon+Red+Blue+Wild+Pokemon+Theme"
    ),

    "II (Johto)": (
        "Pokémon Oro / Plata",
        "https://www.youtube.com/results?search_query=Pokemon+Gold+Silver+Wild+Pokemon+Theme"
    ),

    "III (Hoenn)": (
        "Pokémon Rubí / Zafiro",
        "https://www.youtube.com/results?search_query=Pokemon+Ruby+Sapphire+Wild+Pokemon+Theme"
    ),

    "IV (Sinnoh)": (
        "Pokémon Diamante / Perla",
        "https://www.youtube.com/results?search_query=Pokemon+Diamond+Pearl+Wild+Pokemon+Theme"
    ),

    "V (Teselia)": (
        "Pokémon Negro / Blanco",
        "https://www.youtube.com/results?search_query=Pokemon+Black+White+Wild+Pokemon+Theme"
    ),

    "VI (Kalos)": (
        "Pokémon X / Y",
        "https://www.youtube.com/results?search_query=Pokemon+X+Y+Wild+Pokemon+Theme"
    ),

    "VII (Alola)": (
        "Pokémon Sol / Luna",
        "https://www.youtube.com/results?search_query=Pokemon+Sun+Moon+Wild+Pokemon+Theme"
    ),

    "VIII (Galar)": (
        "Pokémon Espada / Escudo",
        "https://www.youtube.com/results?search_query=Pokemon+Sword+Shield+Wild+Pokemon+Theme"
    ),

    "IX (Paldea)": (
        "Pokémon Escarlata / Púrpura",
        "https://www.youtube.com/results?search_query=Pokemon+Scarlet+Violet+Wild+Pokemon+Theme"
    ),

}

def get_game_music(generation):
    return GAME_MUSIC.get(
        generation,
        ("Desconocido", "#")
    )