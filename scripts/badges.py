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
                f'<img src="{icono}" width="22" alt="{tipo}" '
                f'style="vertical-align:middle;">'
            )

        if badge:
            html.append(
                f'<img src="{badge}" alt="{tipo}" '
                f'style="vertical-align:middle;">'
            )

    return " ".join(html)

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
