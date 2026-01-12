""" Validar un número de teléfono con prefijo internacional (empieza por el signo + seguido
de dos dígitos, luego un espacio y a continuación un número de teléfono.
Ejemplo +34 912233444
"""

import re

# ^ inicio
# \+ símbolo + o solo hacer [+]
# [0-9]{2} dos dígitos de país
# (espacio) espacio obligatorio o se puede usar \s
# [0-9]{9} número de teléfono
# $ fin
patron1 = r"^[+][0-9]{2} [0-9]{9}$"
patron2 = r"^\+[0-9]{2}\s[0-9]{9}$"

telefono = "+34 912233444"
print("patron1:",bool(re.match(patron1, telefono)))
print("patron2:",bool(re.match(patron2, telefono)))

