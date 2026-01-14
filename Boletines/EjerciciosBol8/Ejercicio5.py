"""5. Realiza ahora el programa que haga el descifrado del mensaje. Como es imposible saber que
letras eran mayúsculas y cuales minúsculas en el mensaje original tu mensaje descifrado
debería de aparecer con todas las letras en mayúsculas
"""

def descifrar_mensaje(cifrado):
    longitud = len(cifrado)
    mensajeDecifrando = [""] * longitud  # Lista para reconstruir el mensaje
    inicio, final = 0, longitud - 1
    indice = 0  # índice del cifrado

    while inicio <= final:
        # El primer carácter es el final del original
        mensajeDecifrando[final] = cifrado[indice].upper()
        indice += 1

        # Si no es el mismo, el siguiente carácter es el inicio del original
        if inicio != final:
            mensajeDecifrando[inicio] = cifrado[indice].upper()
            indice += 1

        inicio += 1
        final -= 1

    return "".join(mensajeDecifrando)

mensaje_cifrado = "AaNtAañcAAMM OS"
mensaje_descifrado = descifrar_mensaje(mensaje_cifrado)

print("Mensaje cifrado:  ", mensaje_cifrado)
print("Mensaje descifrado:", mensaje_descifrado)

