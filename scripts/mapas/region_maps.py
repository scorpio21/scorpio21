REGION_MAPS = {
    "I (Kanto)": "https://archives.bulbagarden.net/media/upload/4/44/Kanto_Map.png",
    "II (Johto)": "https://archives.bulbagarden.net/media/upload/6/64/Johto_Map.png",
    "III (Hoenn)": "https://archives.bulbagarden.net/media/upload/8/85/Hoenn_ORAS_Map.png",
    "IV (Sinnoh)": "https://archives.bulbagarden.net/media/upload/6/6f/Sinnoh_BDSP_Map.png",
    "V (Teselia)": "https://archives.bulbagarden.net/media/upload/2/23/Unova_B2W2_Map.png",
    "VI (Kalos)": "https://archives.bulbagarden.net/media/upload/8/88/Kalos_Map.png",
    "VII (Alola)": "https://archives.bulbagarden.net/media/upload/6/69/Alola_USUM_Map.png",
    "VIII (Galar)": "https://archives.bulbagarden.net/media/upload/6/68/Galar_Map.png",
    "IX (Paldea)": "https://archives.bulbagarden.net/media/upload/9/90/Paldea_Map.png",
}

def get_region_map(generation):
    return REGION_MAPS.get(generation, "")