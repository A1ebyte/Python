"""12. Realiza un juego en el que debes de acertar un número entre el 1 y el 50 que el
ordenador ha elegido de forma aleatoria. El programa te indicará si has acertado, si te
has pasado o si te has quedado corto. El programa finaliza cuando se acierta o cuando
se superan el número máximo de intentos establecidos en 5."""
import random
intentos=5
adivinar=random.randint(1,50)
adivine=False
print(adivinar)
while intentos > 0 and adivine==False:
    intentos -= 1
    opcion=int(input("Ingrese tu adivinanza: "))
    print("Te pasaste")if adivinar < opcion else print("Te quedaste corto") if adivinar>opcion else None
    if opcion==adivinar:
        adivine=True
print("Adivinaste Felicidades" if adivine else "Mejor suerte la proxima")