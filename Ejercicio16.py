"""16. Escribir un programa que genere seis números aleatorios entre el 1 y el 49 (simulando una
lotería primitiva). Por el momento no te preocupes de que algunos números puedan salir
repetidos. Ya resolveremos eso más adelante."""
import random
numeros=[]
for i in range(0,6):
    numeros.append(random.randint(1,49))
print("Los números de la lotería son:",numeros)