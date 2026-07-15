import random


def build_pokemon_trivia(nombre):
    return f"""**¿Sabías que...?**  
{nombre} es conocido por su capacidad para {random.choice(['alcanza poderes muy altos', 'desarrollar habilidades que cambian las batallas', 'dominar varias tácticas en combate'])}."""
