"""Una dirección IP pública de clase C. Cuatro bytes en formato decimal separados por un
punto. Los dos primeros tienen que ser siempre 192.168.
Ejemplo: 192.168.30.30
"""
import re

# ^ inicio
# 192\.168\. red fija
# (\.[0-9]{1,3}){2} resto de bytes byte
# \. punto
# $ fin
patron = r"^192\.168(\.[0-9]{1,3}){2}$"

ip = "192.168.30.30"
print(bool(re.match(patron, ip)))
