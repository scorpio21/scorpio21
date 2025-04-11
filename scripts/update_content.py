from github import Github
import os

# Autenticación con el token
g = Github(os.getenv('GH_TOKEN'))  # Obtén el token del entorno

# Obtener el repositorio
repo = g.get_repo("scorpio21/scorpio21")

# Verifica si el repositorio es accesible
print(f"Repositorio accedido: {repo.name}")

try:
    # Acceder al archivo README.md en la raíz
    readme_file = repo.get_contents("README.md")
    print(f"Archivo encontrado: README.md")
    
    # Leer el contenido actual del archivo
    contenido = readme_file.decoded_content.decode("utf-8")
    print("Contenido cargado correctamente.")
    
    # Realizar las modificaciones necesarias aquí (ejemplo: actualización del Pokémon o la frase)
    # Aquí puedes actualizar el contenido como desees, por ejemplo:
    nuevo_contenido = contenido + "\n# Actualización automática del día"

    # Actualizar el archivo README.md con el nuevo contenido
    repo.update_file(
        "README.md",  # Ruta al archivo
        "Actualización del archivo README",  # Mensaje de commit
        nuevo_contenido,  # El contenido actualizado
        readme_file.sha  # El sha actual del archivo
    )
    print("Archivo actualizado correctamente.")
    
except Exception as e:
    print(f"Error al obtener o actualizar el archivo README.md: {str(e)}")
