"""14. Escribir un programa que nos pida dos números por teclado y genere un número aleatorio
comprendido entre ambos. Por el momento no te preocupes de que el primer número
siempre debería de ser menor que el segundo, simplemente no los metas en un orden
incorrecto."""
import random
num1=input("Elige tu numero mayor: ")
num2=input("Elige tu numero menor: ")
if not(num1.isdigit() and num2.isdigit()):
    print("Algún numero ingresado no es valido")
    exit()
num1=int(num1)
num2=int(num2)
print(random.randint(num1, num2))