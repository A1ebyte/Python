"""Validar dos palabras de cualquier tamaño separadas por un único espacio en blanco.
Las palabras no pueden contener números y deben de empezar ambas por una letra
mayúscula.
Ejemplo: Hola Mundo
"""

import re
# ^ inicio
# [A-Z] primera letra mayúscula
# [a-zA-Z]+ resto de letras, el + es para decir una o más de estos
# \s un solo espacio
# [A-Z][a-zA-Z]+ segunda palabra, el + es para decir una o más de estos
# $ fin
patron = r"^[A-Z][a-zA-Z]+\s[A-Z][a-zA-Z]+$"

texto = "Hola Mundo"
print(bool(re.match(patron, texto)))
