"""
2. Modifica el programa anterior para que cuando coincidan ambas contraseñas nos
informe del número de intentos inválidos
"""
password=-1
password2=0
cont=0
while password!=password2:
    cont+=1
    password = input("Escribe contraseña\n")
    password2 = input("Confirmar contraseña:\n")
    if password != password2:
        print("Error no coinciden, repite")
print("Todo listo, Intentos: ",cont)