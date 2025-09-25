#21. Escribir un programa que pida por teclado un número al usuario y calcule si es primo o no
numero=int(input("Ingrese un numero: "))
primo=True
for num in range(2, int(numero ** .5) + 1):
    if numero % num == 0:
        primo = False
        break
print(f"Primo: {primo}")