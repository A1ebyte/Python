"""18. Escribe un programa que genere números aleatorios entre el 1 y el 1000 sin parar y que sólo
se detenga cuando salga el 666. Los números que ha tenido que generar tu programa hasta
aparecer el 666 son los que restan para el apocalipsis. Tu programa debería de indicarlo con
un mensaje tétrico (¡Faltan 236 días para que se acabe)"""
import random

numero=0
diasApok=0
while numero!=666:
    numero=random.randint(1,1000)
    diasApok=diasApok+1
    print(numero)
print(f"¡Faltan {diasApok} días para que se el APOCALIPSIS!")