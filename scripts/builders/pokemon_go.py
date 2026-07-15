import random


def build_pokemon_go(nombre):
    return f"""**Pokémon Go:**
- **CP máximo:** {random.randint(3000, 4000)}
- **Clase de combate:** 8
- **Evento especial:** {nombre} puede aparecer más frecuentemente durante el evento "Festival de la primavera".

[Más información en Bulbapedia](https://bulbapedia.bulbagarden.net/wiki/{nombre}_(Pokémon))"""
