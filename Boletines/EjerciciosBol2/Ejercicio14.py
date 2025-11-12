"""14. Modifica el programa anterior para que al final del programa te pida si quieres volver
a jugar y en caso afirmativo comience una nueva partida
"""
import random
jugar=True
while jugar:
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
    volverJugar=input("Quieres jugar de nuevo? Si/No")
    while volverJugar not in ["Si", "No"]:
        print("Opcion no valida")
        volverJugar = input("Quieres jugar de nuevo? Si/No")
    jugar=True if volverJugar=="Si" else False