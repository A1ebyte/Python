"""
1. Escribir un programa que pida una contraseña por teclado (dos veces) y si no
coinciden nos lo vuelva a pedir hasta que lo hagan
"""
password=-1
password2=0
while password!=password2:
    password = input("Escribe contraseña\n")
    password2 = input("Confirmar contraseña:\n")
    if password != password2:
        print("Error no coinciden, repite")
print("Todo listo")