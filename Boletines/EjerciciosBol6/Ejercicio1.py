"""
Validar un código postal de Madrid. Cinco números, los dos primeros siempre son el 28
Ejemplo: 28032
"""
import re

cp = "28032"

# ^28 empieza por 28
# [0-9]{3} tres dígitos numéricos
# $ fin de la cadena
patron = r"^28[0-9]{3}$"

# Valida código postal de Madrid
print(bool(re.match(patron, cp)))
