import random

from config import colores_pokedex, rareza_texto, rareza_colores


def build_pokemon_info_block(
    fecha,
    pokemon_img_url,
    nombre,
    rareza,
    pokedex_num,
    tipos_html,
    debilidades_html,
    resistencias_html,
    inmunidades_html,
    clase,
    color_pokedex,
    altura,
    peso,
    experiencia,
    habitat,
    egg_groups,
    base_happiness,
    capture_rate,
    habilidades,
    habilidad_oculta,
    cadena_evolucion,
    bst_html,
    stats_md
):
    pokemon_info_block = f"""<!-- POKEMON_INFO -->
<!-- Generated: {fecha} -->
### 🐱‍👤 Pokémon del día

<table>
<tr><td><b>Imagen</b></td><td><img src="{pokemon_img_url}" alt="{nombre}" /></td></tr>
<tr><td><b>Nombre</b></td><td>{rareza_iconos[rareza]} <b>{nombre}</b></td></tr>

<tr><td><b>Rareza</b></td><td>
<img src="https://img.shields.io/badge/{rareza_texto[rareza]}-{rareza_colores[rareza]}?style=flat-square">
</td></tr>
<tr><td><b>Nº Pokédex</b></td><td>{pokedex_num}</td></tr>
<tr><td><b>Tipo(s)</b></td><td>{tipos_html}</td></tr>
<tr>
<td><b>⚔️ Débil contra</b></td>
<td>{debilidades_html}</td>
</tr>

<tr>
<td><b>🛡️ Resiste</b></td>
<td>{resistencias_html}</td>
</tr>

<tr>
<td><b>✨ Inmune a</b></td>
<td>{inmunidades_html if inmunidades_html else "Ninguna"}</td>
</tr>
<tr><td><b>Clase</b></td><td>{clase.capitalize()}</td></tr>
<tr><td><b>🎨 Color Pokédex</b></td><td>{colores_pokedex[color_pokedex]}</td></tr>
<tr><td><b>📏 Altura</b></td><td>{altura} m</td></tr>
<tr><td><b>⚖️ Peso</b></td><td>{peso} kg</td></tr>
<tr><td><b>⭐ Experiencia</b></td><td>{experiencia}</td></tr>
<tr><td><b>🌍 Hábitat</b></td><td>{habitat}</td></tr>
<tr><td><b>🥚 Grupo huevo</b></td><td>{egg_groups}</td></tr>
<tr><td><b>❤️ Amistad base</b></td><td>{base_happiness}</td></tr>
<tr><td><b>🎯 Ratio captura</b></td><td>{capture_rate}</td></tr>
<tr><td><b>💪 Habilidades</b></td>
<td>{", ".join(habilidades)}</td></tr>
<tr><td><b>✨ Habilidad oculta</b></td>
<td>{habilidad_oculta if habilidad_oculta else "Ninguna"}</td></tr>
<tr><td><b>Movimientos especiales</b></td><td>{', '.join([
random.choice(["Corte Psíquico", "Hoja Afilada", "Puño Fuego"]),
random.choice(["Rayo Solar", "Ataque Psíquico", "Puño Trueno"]),
random.choice(["Puño Trueno", "Puño Fuego"])
])}</td></tr>
<tr><td><b>Evolución</b></td><td>{cadena_evolucion}</td></tr>
<tr>
<td><b>🏆 Poder total (BST)</b></td>
<td>{bst_html}</td>
</tr>
<tr><td><b>Estadísticas base</b></td><td>{stats_md}</td></tr>
<tr>
</table>

<br>

**Historia del día:**  
"Hoy, {nombre} decidió {random.choice(['tomar un descanso', 'explorar un nuevo terreno', 'enfrentar su mayor desafío'])}. ¡Prepárate para ver qué sucede!"

---

**¿Sabías que...?**  
{nombre} es conocido por su capacidad para {random.choice(['alcanza poderes muy altos', 'desarrollar habilidades que cambian las batallas', 'dominar varias tácticas en combate'])}.

---

**Pokémon Go:**
- **CP máximo:** {random.randint(3000, 4000)}
- **Clase de combate:** 8
- **Evento especial:** {nombre} puede aparecer más frecuentemente durante el evento "Festival de la primavera".

[Más información en Bulbapedia](https://bulbapedia.bulbagarden.net/wiki/{nombre}_(Pokémon))

<!-- END_POKEMON_INFO -->
"""
    return pokemon_info_block


def build_frase_info_block(fecha, frase_del_dia):
    frase_info_block = f"""<!-- FRASE_GAMER -->
<!-- Generated: {fecha} -->
### 💬 Frase 🎮 del día
> "{frase_del_dia}"
<!-- END_FRASE_GAMER -->
"""
    return frase_info_block
