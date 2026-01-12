"""Un número de 4 cifras mínimo y 8 cifras máximo
Ejemplo: 12345"""
import re

# ^ inicio
# [0-9]{4,8} entre 4 y 8 dígitos
# $ fin
patron = r"^[0-9]{4,8}$"
numero = "12345"
print(bool(re.match(patron, numero)))
