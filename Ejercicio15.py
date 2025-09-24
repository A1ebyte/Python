"""15. Modificar el programa del punto anterior para que si el primer número que metemos es
mayor que el segundo funcione correctamente. Es decir, si metemos en primer lugar el 50 y
en segundo el 10 nos debería de generar un número aleatorio entre el 10 y el 50 (y no entre el
50 y el 10 que no tiene mucha lógica…)"""
import random
num1=input("Elige un numero: ")
num2=input("Elige otro numero: ")
if not(num1.isdigit() and num2.isdigit()):
    print("Algún numero ingresado no es valido")
    exit()
num1=int(num1)
num2=int(num2)
if num1>num2:
    print(random.randint(num2,num1))
else:
    print(random.randint(num1,num2))