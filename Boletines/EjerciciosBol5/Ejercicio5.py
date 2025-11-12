"""5. Escribe un programa que genere 100 números aleatorios comprendidos entre el 1 y
50 (ambos inclusive) y, posteriormente, obtenga el mayor, el menor y el que mas veces
se repite (y nos diga cuantas veces lo hace)."""
import random
from itertools import count

numeros = [random.randint(1,50) for i in range(100)]
print(numeros)
# Calcular número más repetido
num_mas_repetido = numeros[0]
max_repeticiones = numeros.count(numeros[0])

for n in numeros:
    repeticiones = numeros.count(n)
    if repeticiones > max_repeticiones:
        max_repeticiones = repeticiones
        num_mas_repetido = n
print(f"Num mayor: {max(numeros)}",f"Num menor: {min(numeros)}",
      f"Num más repetido: {num_mas_repetido} con {max_repeticiones} repeticiones",sep="\n")