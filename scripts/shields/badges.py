#------------------------------
# scripts/badges.py
#------------------------------
from config import pokemon_type_colors
from urllib.parse import quote
from type_icons import TYPE_ICONS

from config import (
    tipo_badges,
    rareza_iconos,
    rareza_texto,
    rareza_colores,
)
from translation.pokemon_types import obtener_tipo_info
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

def build_tipos_html(tipos_es):
    html = []

    for tipo in tipos_es:
        icono = TYPE_ICONS.get(tipo)
        badge = tipo_badges.get(tipo)

        if icono:
            html.append(
                f'<img src="{icono}" width="23" alt="{tipo}" '
                f'style="vertical-align:middle;">&nbsp;'
            )

        if badge:
            html.append(
                f'<img src="{badge}" alt="{tipo}" '
                f'style="vertical-align:middle;"><br>'
            )

    return "".join(html)

#------------------------------
# Debilidades, resistencias e inmunidades en HTML
#------------------------------

def build_relations_html(tipos_es):
    debilidades, resistencias, inmunidades = obtener_tipo_info(tipos_es)

    return (
        build_tipos_html(debilidades),
        build_tipos_html(resistencias),
        build_tipos_html(inmunidades),
    )

def build_moves_html(moves):

    html = []

    for move in moves:

        color = pokemon_type_colors.get(
            move["tipo"].lower(),
            "lightgrey"
        )

        badge = (
            f"https://img.shields.io/badge/"
            f"{move['nombre'].replace(' ', '%20')}-"
            f"{color}?style=flat-square"
        )

        html.append(f'<img src="{badge}">')

    return "<br>".join(html)
