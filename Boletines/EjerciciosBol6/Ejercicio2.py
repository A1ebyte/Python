"""2. Validar un número de teléfono
Ejemplo: 91345566"""

import re

# ^ inicio
# [0-9]{8} exactamente 8 dígitos
# $ fin
patron = r"^[0-9]{8}$"

telefono = "91345566"
print(bool(re.match(patron, telefono)))
