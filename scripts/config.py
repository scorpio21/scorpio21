# Diccionarios y constantes de configuración

# Tipos de caracteres
type_chart = {
    "Normal": {"weak": ["Lucha"], "resist": [], "immune": ["Fantasma"]},
    "Fuego": {"weak": ["Agua", "Tierra", "Roca"], "resist": ["Fuego", "Planta", "Hielo", "Bicho", "Acero", "Hada"], "immune": []},
    "Agua": {"weak": ["Planta", "Eléctrico"], "resist": ["Fuego", "Agua", "Hielo", "Acero"], "immune": []},
    "Planta": {"weak": ["Fuego", "Hielo", "Veneno", "Volador", "Bicho"], "resist": ["Agua", "Planta", "Tierra", "Eléctrico"], "immune": []},
    "Eléctrico": {"weak": ["Tierra"], "resist": ["Eléctrico", "Volador", "Acero"], "immune": []},
    "Hielo": {"weak": ["Fuego", "Lucha", "Roca", "Acero"], "resist": ["Hielo"], "immune": []},
    "Lucha": {"weak": ["Volador", "Psíquico", "Hada"], "resist": ["Bicho", "Roca", "Siniestro"], "immune": []},
    "Veneno": {"weak": ["Tierra", "Psíquico"], "resist": ["Planta", "Lucha", "Veneno", "Bicho", "Hada"], "immune": []},
    "Tierra": {"weak": ["Agua", "Planta", "Hielo"], "resist": ["Veneno", "Roca"], "immune": ["Eléctrico"]},
    "Volador": {"weak": ["Eléctrico", "Hielo", "Roca"], "resist": ["Planta", "Lucha", "Bicho"], "immune": ["Tierra"]},
    "Psíquico": {"weak": ["Bicho", "Fantasma", "Siniestro"], "resist": ["Lucha", "Psíquico"], "immune": []},
    "Bicho": {"weak": ["Fuego", "Volador", "Roca"], "resist": ["Planta", "Lucha", "Tierra"], "immune": []},
    "Roca": {"weak": ["Agua", "Planta", "Lucha", "Tierra", "Acero"], "resist": ["Normal", "Fuego", "Veneno", "Volador"], "immune": []},
    "Fantasma": {"weak": ["Fantasma", "Siniestro"], "resist": ["Veneno", "Bicho"], "immune": ["Normal", "Lucha"]},
    "Dragón": {"weak": ["Hielo", "Dragón", "Hada"], "resist": ["Fuego", "Agua", "Planta", "Eléctrico"], "immune": []},
    "Siniestro": {"weak": ["Lucha", "Bicho", "Hada"], "resist": ["Fantasma", "Siniestro"], "immune": ["Psíquico"]},
    "Acero": {"weak": ["Fuego", "Lucha", "Tierra"], "resist": ["Normal", "Planta", "Hielo", "Volador", "Psíquico", "Bicho", "Roca", "Dragón", "Acero", "Hada"], "immune": ["Veneno"]},
    "Hada": {"weak": ["Veneno", "Acero"], "resist": ["Lucha", "Bicho", "Siniestro"], "immune": ["Dragón"]}
}

# Lista de legendarios/míticos
legendarios = [
    144, 145, 146, 150, 151, 243, 244, 245, 249, 250, 251,
    377, 378, 379, 380, 381, 382, 383, 384, 385,
    480, 481, 482, 483, 484, 485, 486, 487, 488, 489, 490,
    638, 639, 640, 641, 642, 643, 644, 645, 646, 647, 648, 649,
    716, 717, 718, 719, 720, 721,
    785, 786, 787, 788, 789, 790, 791, 792, 800, 801, 802,
    888, 889, 890
]

# Colores según rareza (neón falso compatible con GitHub)
neon_rarity_colors = {
    "comun": "#00ff7f",
    "no_comun": "#1e90ff",
    "raro": "#ff1493",
    "legendario": "#ffd700"
}

# Badges de tipos
tipo_badges = {
    "Normal": "https://img.shields.io/badge/Normal-A8A77A?style=flat-square",
    "Fuego": "https://img.shields.io/badge/Fuego-EE8130?style=flat-square",
    "Agua": "https://img.shields.io/badge/Agua-6390F0?style=flat-square",
    "Planta": "https://img.shields.io/badge/Planta-7AC74C?style=flat-square",
    "Eléctrico": "https://img.shields.io/badge/Eléctrico-F7D02C?style=flat-square",
    "Hielo": "https://img.shields.io/badge/Hielo-96D9D6?style=flat-square",
    "Lucha": "https://img.shields.io/badge/Lucha-C22E28?style=flat-square",
    "Veneno": "https://img.shields.io/badge/Veneno-A33EA1?style=flat-square",
    "Tierra": "https://img.shields.io/badge/Tierra-E2BF65?style=flat-square",
    "Volador": "https://img.shields.io/badge/Volador-A98FF3?style=flat-square",
    "Psíquico": "https://img.shields.io/badge/Psíquico-F95587?style=flat-square",
    "Bicho": "https://img.shields.io/badge/Bicho-A6B91A?style=flat-square",
    "Roca": "https://img.shields.io/badge/Roca-B6A136?style=flat-square",
    "Fantasma": "https://img.shields.io/badge/Fantasma-735797?style=flat-square",
    "Dragón": "https://img.shields.io/badge/Dragón-6F35FC?style=flat-square",
    "Siniestro": "https://img.shields.io/badge/Siniestro-705746?style=flat-square",
    "Acero": "https://img.shields.io/badge/Acero-B7B7CE?style=flat-square",
    "Hada": "https://img.shields.io/badge/Hada-D685AD?style=flat-square"
}

# Iconos según rareza
rareza_iconos = {
    "comun": "🟢",
    "no_comun": "🔵",
    "raro": "🟣",
    "legendario": "🟡✨"
}

# Colores para Shields.io
rareza_colores = {
    "comun": "brightgreen",
    "no_comun": "blue",
    "raro": "purple",
    "legendario": "gold"
}

# Texto de la rareza
rareza_texto = {
    "comun": "Común",
    "no_comun": "No común",
    "raro": "Raro",
    "legendario": "Legendario"
}

