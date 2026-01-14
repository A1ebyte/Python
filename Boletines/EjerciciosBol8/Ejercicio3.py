"""3. Vamos a realizar un programa de cifrado que haga lo siguiente: mezcle los caractéres
alternando entre las del principio y las del final del mensaje empezando siempre por el final.
Por ejemplo, si nuestro mensaje secreto fuera el siguiente:
12345
El mensaje cifrado sería así:
51432
Un ejemplo con un mensaje de texto real:
Atacamos mañana
Se codificaría así:
aAntaañcaamm os"""

def cifrar_mensaje(mensaje):
    cifrado = ""
    inicio, final = 0, len(mensaje) - 1
    while inicio <= final:
        cifrado += mensaje[final]  # Tomamos del final primero
        if inicio != final:  # Evitar repetir si es el mismo carácter
            cifrado += mensaje[inicio]  # Tomamos del inicio
        inicio += 1
        final -= 1
    return cifrado

mensaje = "Atacamos mañana"
print("Mensaje original:", mensaje)
print("Mensaje cifrado:", cifrar_mensaje(mensaje))
