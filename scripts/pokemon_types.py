from config import type_chart

# Traducción de tipos
def get_pokemon_type_translation(tipo):
    traducciones = {
        "fire": "Fuego", "water": "Agua", "grass": "Planta", "electric": "Eléctrico",
        "bug": "Bicho", "poison": "Veneno", "ghost": "Fantasma", "steel": "Acero",
        "psychic": "Psíquico", "normal": "Normal", "flying": "Volador", "fighting": "Lucha",
        "rock": "Roca", "fairy": "Hada", "ice": "Hielo", "dragon": "Dragón",
        "dark": "Siniestro", "ground": "Tierra", "shadow": "Sombra"
    }
    return traducciones.get(tipo, tipo)


# Obtener tipo
def obtener_tipo_info(tipos):
    debilidades = set()
    resistencias = set()
    inmunidades = set()

    for tipo in tipos:
        datos = type_chart.get(tipo, {})
        debilidades.update(datos.get("weak", []))
        resistencias.update(datos.get("resist", []))
        inmunidades.update(datos.get("immune", []))

    return (
        sorted(debilidades),
        sorted(resistencias),
        sorted(inmunidades)
    )
