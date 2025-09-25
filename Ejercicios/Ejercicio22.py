#22. Escribir un programa que genere un número primo aleatorio entre el 10.000.000 y el 50.000.000
import random

numprimo=0
primo=False
while not primo:
    numprimo=random.randint(10000000,50000000)
    for x in range(2, int(numprimo ** .5) + 1):
        if numprimo % x == 0:
            primo = False
            break
    primo = True
print(f"{numprimo}")