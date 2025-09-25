#6. Escribir un programa que pida por teclado un número al usuario y diga si es divisible por 3 o no
numero=input("elige un numero: ")
if numero.isdigit():
    res = "Divisible por 3" if int(numero) % 2 == 0 else "No divisible por 3"
    print(res)
else:
    print("Error valor no valido")