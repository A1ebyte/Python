"""Una clave con el siguiente formato XX00-xxX-00 donde las X deben de ser letras
mayúsculas, las x letras minúsculas y los 0 dígitos.
Ejemplo: AB12-xyZ-75
"""
import re

# ^ inicio
# [A-Z]{2} dos letras mayúsculas
# [0-9]{2} dos dígitos
# - guion directamente o escaparlo con \-
# [a-z]{2} dos letras minúsculas
# [A-Z] una letra mayúscula
# - guion
# [0-9]{2} dos dígitos
# $ fin
patron = r"^[A-Z]{2}[0-9]{2}\-[a-z]{2}[A-Z]-[0-9]{2}$"

clave = "AB12-xyZ-75"
print(bool(re.match(patron, clave)))
