"""17. Escribir un programa que nos permita generar una quiniela. Para ello nos debe generar
quince números aleatorios entre el 1 y el 3. Recuerda que los resultados válidos son 1 X o 2,
así que si te sale un 3 lo que tienes que imprimir en pantalla es una X"""
import random
for i in range(0,15):
    res=random.randint(1,3)
    res= res if res!=3 else "X"
    print(f"{f"0{i+1}" if i+1 < 10 else i+1}. {res}")