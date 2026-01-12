"""Validar un número de teléfono móvil (debe de empezar por 6, 7 u 8)
Ejemplo: 655776655
"""

import re

# ^ inicio
# [6-8] empieza por 6, 7 u 8
# [0-9]{8} ocho dígitos más
# $ fin
patron = r"^[6-8][0-9]{8}$"

movil = "655776655"
print(bool(re.match(patron, movil)))
