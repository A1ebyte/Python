#7. Escribir un programa que pida un número por teclado al usuario que simule ser el precio de
#un artículo y escriba el resultado de aplicarle el IVA del 21%
numero=input("elige un numero: ")
IVA=0.21
if numero.isdigit():
    numero=int(numero)
    print(f"El numero con IVA es: {numero+(numero*IVA)}")
else:
    print("Error valor no valido")