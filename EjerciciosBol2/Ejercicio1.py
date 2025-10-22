"""1. Escribir un programa que nos pida tres palabras por teclado en cualquier orden y nos
las muestre en pantalla ordenadas alfabeticamente en orden ascendente"""
lista=[]
for x in range(0,3):
    lista.append(input("Escribe una palabra"))
lista.sort()
print(", ".join(lista))