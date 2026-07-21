#------------------------------
# scripts/badges.py
#------------------------------

from urllib.parse import quote
from type_icons import TYPE_ICONS

from config import (
    tipo_badges,
    rareza_iconos,
    rareza_texto,
    rareza_colores,
)
from pokemon_types import obtener_tipo_info
from urllib.parse import quote

#------------------------------
# Gritos
#------------------------------

def build_cry_badge(nombre):
    nombre = quote(nombre)
    return (
        f'https://img.shields.io/badge/'
        f'▶️%20Escuchar%20{nombre}-'
        f'Grito%20Oficial-4CAF50?style=for-the-badge'
    )

# Nombre con icono de rareza
def build_nombre_md(rareza, nombre):
    return f"{rareza_iconos[rareza]} <b>{nombre}</b>"


# Badge de Shields.io (for-the-badge) — se mantiene aunque no se use en README
def build_badge_rareza(nombre, rareza):
    return (
        f'<img src="https://img.shields.io/badge/'
        f'{quote(nombre)}-{quote(rareza_texto[rareza])}-{rareza_colores[rareza]}'
        f'?style=for-the-badge" '
        f'alt="{rareza_texto[rareza]}">'
    )

#------------------------------
# Tipos Html
#------------------------------
TYPE_COLORS = {
    "Normal": "#A8A878",
    "Fuego": "#F08030",
    "Agua": "#6890F0",
    "Eléctrico": "#F8D030",
    "Planta": "#78C850",
    "Hielo": "#98D8D8",
    "Lucha": "#C03028",
    "Veneno": "#A040A0",
    "Tierra": "#E0C068",
    "Volador": "#A890F0",
    "Psíquico": "#F85888",
    "Bicho": "#A8B820",
    "Roca": "#B8A038",
    "Fantasma": "#705898",
    "Dragón": "#7038F8",
    "Siniestro": "#705848",
    "Acero": "#B8B8D0",
    "Hada": "#EE99AC",
    "Astral": "#5A4FFF",
}

def build_tipos_html(tipos_es):
    html = []

    for tipo in tipos_es:
        icono = TYPE_ICONS.get(tipo)
        color = TYPE_COLORS.get(tipo, "#999")

        html.append(f"""
        <div style="
            display:inline-flex;
            align-items:center;
            background:{color};
            color:white;
            padding:4px 10px;
            border-radius:6px;
            font-weight:bold;
            font-size:14px;
            margin-right:6px;
        ">
            <img src="{icono}" width="20" style="margin-right:6px;">
            {tipo}
        </div>
        """)

    return "".join(html)


#------------------------------
# Debilidades, resistencias e inmunidades en HTML
#------------------------------

def build_relations_html(tipos_es):
    debilidades, resistencias, inmunidades = obtener_tipo_info(tipos_es)

    debilidades_html = " ".join(
        f'<img src="{tipo_badges[t]}" alt="{t}">'
        for t in debilidades if t in tipo_badges
    )

    resistencias_html = " ".join(
        f'<img src="{tipo_badges[t]}" alt="{t}">'
        for t in resistencias if t in tipo_badges
    )

    inmunidades_html = " ".join(
        f'<img src="{tipo_badges[t]}" alt="{t}">'
        for t in inmunidades if t in tipo_badges
    )

    return debilidades_html, resistencias_html, inmunidades_html
