#5. Escribir un programa que pida por teclado un número al usuario y diga si es par o impar
numero=input("elige un numero: ")
if numero.isdigit():
    res = "Par" if int(numero) % 2 == 0 else "Impar"
    print(res)
else:
    print("Error valor no valido")