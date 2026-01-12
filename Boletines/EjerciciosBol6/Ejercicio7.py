"""Validar una tarjeta de crédito: cuatro grupos de cuatro números cada uno separados por
un espacio. A continuación un espacio y la fecha de caducidad en formato MM/YY. El
mes tiene que ser válido (entre 01 y 12)
Ejemplo: 1234 5678 9012 3456 03/25"""

import re

# ^ inicio
# [0-9]{4} primer bloque de 4 números
# ([0-9]{4}){3} tres bloques más con espacio
# espacio \s
# (0[1-9]|1[0-2]) mes válido 01 a 12
# / separador
# [0-9]{2} año
# $ fin
patron1 = r"^[0-9]{4}(\s[0-9]{4}){3}\s(0[1-9]|1[0-2])/[0-9]{2}$"
patron2 = r"^[0-9]{4} [0-9]{4} [0-9]{4} [0-9]{4} (0[1-9]|1[0-2])/[0-9]{2}$"
patron3 = r"^([0-9]{4} ){4}(0[1-9]|1[0-2])/[0-9]{2}$"

tarjeta = "1234 5678 9012 3456 03/25"
print(bool(re.match(patron1, tarjeta)))
print(bool(re.match(patron2, tarjeta)))
print(bool(re.match(patron3, tarjeta)))
