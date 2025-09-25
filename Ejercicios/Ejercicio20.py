#20. Escribir un programa que nos pida tres números por teclado en cualquier orden y nos los
#muestre en pantalla ordenados de menor a mayor
numeros=[]
numeros.append(int(input("Ingrese un numero: ")))
numeros.append(int(input("Ingrese un numero: ")))
numeros.append(int(input("Ingrese un numero: ")))
numeros.sort()
print(numeros)