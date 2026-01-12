"""Un IBAN bancario de España. Las dos letras iniciales siempre tienen que ser ES
Ejemplo: ES61 1234 3456 42 0456323532"""
import re

# ^  inicio
# ES letras fijas ES
# [0-9]{2} dígitos de control
# ( [0-9]{4}){2} dos grupos de 4 dígitos
# (espacio)
# [0-9]{2} últimos 2 digitos Iban
# [0-9]{10} numero de cuenta
# $ fin
patron = r"^ES[0-9]{2}( [0-9]{4}){2} [0-9]{2} [0-9]{10}$"

iban = "ES61 1234 3456 42 0456323532"
print(bool(re.match(patron, iban)))
