# 3. Escribir un programa donde se muestren los 5 primeros números múltiplos de uno dado por el usuario
# (se introducirá por teclado)
numero=input("elige un numero: ")
if numero.isdigit():
    for x in range(1, 6):
        print(numero * x)
else:
    print("Error valor no valido")