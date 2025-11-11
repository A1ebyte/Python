"""13. Modifica el programa anterior para que el programa te de todos los intentos que
necesites pero que cuando aciertes te informe de cuantas veces has fallado antes de
lograrlo
"""
import random
intentos=0
adivinar=random.randint(1,50)
adivine=False
print(adivinar)
while not adivine:
    intentos += 1
    opcion=int(input("Ingrese tu adivinanza: "))
    print("Te pasaste")if adivinar < opcion else print("Te quedaste corto") if adivinar>opcion else None
    if opcion==adivinar:
        adivine=True
print(f"Adivinaste Felicidades y has tardado: {intentos} intentos")