"""7. Pide al usuario un número y crea un array de enteros de tantas posiciones como indique
ese número. Rellénalo con números aleatorios entre el 10 y el 1000 y finalmente
pregunta al usuario por la posición de la que quiere recuperar el valor. El programa
mostrará el número de la posición indicada si esta existe y un error si tratamos de
recuperar una posición que no existe (menor a 0 o mayor a la longitud del array)
"""
import random
cantidad=int(input("Cuantos hago: "))
lista=[random.randint(10,20) for num in range(cantidad)]
try:
    pos=int(input("Que posición quieres recuperar: "))
    valor=lista[pos]
except:
    valor="Error no existe dicha posición"
print(valor)
