import re

def update_readme(pokemon_info_block, frase_info_block, readme_path="README.md"):
    with open(readme_path, "r+", encoding="utf-8") as file:
        contenido = file.read()

        contenido = re.sub(
            r"<!-- POKEMON_INFO -->.*?<!-- END_POKEMON_INFO -->",
            pokemon_info_block,
            contenido,
            flags=re.DOTALL
        )

        contenido = re.sub(
            r"<!-- FRASE_GAMER -->.*?<!-- END_FRASE_GAMER -->",
            frase_info_block,
            contenido,
            flags=re.DOTALL
        )

        file.seek(0)
        file.write(contenido)
        file.truncate()
