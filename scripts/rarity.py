from config import legendarios


# Función para determinar rareza
def get_rarity(tipo_principal, pokedex_num):
    if pokedex_num in legendarios:
        return "legendario"
    if tipo_principal in ["Psíquico", "Fantasma", "Acero", "Dragón", "Siniestro", "Hada"]:
        return "raro"
    if tipo_principal in ["Planta", "Agua", "Fuego", "Eléctrico", "Veneno", "Lucha", "Roca", "Tierra", "Hielo"]:
        return "no_comun"
    return "comun"
