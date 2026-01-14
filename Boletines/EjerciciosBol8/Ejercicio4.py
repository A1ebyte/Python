"""Modifica el programa anterior para que sea mas dificil el descifrado haciendo que, de forma
aleatoria, algunas letras cambien de mayúsculas a minúsculas en el cifrado. El mensaje
anterior quedaría entonces así, por ejemplo (tu resultado podría ser diferente ya que la
conversión de mayúsculas es aleatoria:
aanTAañCaaMm OS
"""

import random

def cifrar_mensaje(mensaje):
    cifrado = ""
    inicio, final = 0, len(mensaje) - 1
    while inicio <= final:
        cifrado += mensaje[final].upper() if random.randint(0,1)==1 else mensaje[final].lower()
        if inicio != final:
            char_inicio = mensaje[inicio]
            char_inicio = char_inicio.upper() if random.choice([True, False]) else char_inicio.lower()
            cifrado += char_inicio
        inicio += 1
        final -= 1
    return cifrado

mensaje = "Atacamos mañana"
print("Mensaje original:", mensaje)
print("Mensaje cifrado:", cifrar_mensaje(mensaje))
