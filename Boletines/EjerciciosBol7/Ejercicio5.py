"""5. Pide al usuario un número y crea un array de enteros de tantas posiciones como indique
ese número. Rellenalo con números aleatorios entre el 10 y el 1000 y finalmente
muestra cual es el máximo, cual el mínimo y la media aritmética con dos decimales."""
import random
cantidad=int(input("Cuantos hago: "))
lista=[random.randint(10,1000) for num in range(cantidad)]
print(lista)
print(max(lista))
print(min(lista))
print(round(sum(lista)/len(lista),2))