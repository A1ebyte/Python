"""Escribe un programa que pida al usuario una contraseña y compruebe que cumple las
siguientes condiciones:
a. Debe tener al menos 8 caracteres y no más de 20.
b. Debe tener al menos una letra mayúscula y una minúscula.
c. Debe de tener al menos un número
c. Debe tener un símbolo de entre los siguientes: _, -, !, ?, *
Si la contraseña no es válida, se pide de nuevo, y así sucesivamente hasta que sea correcta.
Una vez que es correcta se pide al usuario que la introduzca de nuevo, si coincide se informa
al usuario y se termina el proceso. Si no coincide se vuelve a empezar el proceso."""

import re  # Para usar expresiones regulares

def es_contraseña_valida(contrasena):
    if len(contrasena) < 8 or len(contrasena) > 20:
        return False
    if not re.search(r"[A-Z]", contrasena):  # Al menos una mayúscula
        return False
    if not re.search(r"[a-z]", contrasena):  # Al menos una minúscula
        return False
    if not re.search(r"[0-9]", contrasena):  # Al menos un número
        return False
    if not re.search(r"[_\-!?\*]", contrasena):  # Al menos un símbolo permitido
        return False
    return True

while True:
    contraseña = input("Introduce tu contraseña: ")
    if es_contraseña_valida(contraseña):
        repetir = input("Vuelve a introducir tu contraseña: ")
        if contraseña == repetir:
            print("¡Contraseña válida y confirmada!")
            break
        else:
            print("Las contraseñas no coinciden. Intenta de nuevo.")
    else:
        print("Contraseña inválida. Debe cumplir todos los requisitos.")
