import random

texto=input("Introduce una cadena: ")
nuevoTexto=""
listaTexto=list(texto)
for x in range(0,len(texto)):
    letra=random.choice(listaTexto)
    nuevoTexto+=letra
    listaTexto.remove(letra)
print(f"Resultado: {nuevoTexto}")