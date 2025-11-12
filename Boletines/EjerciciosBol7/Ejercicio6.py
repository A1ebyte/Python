"""6. Modifica el ejercicio anterior para que, nos muestre en que posición del array se
encuentran el máximo y el mínimo. Si están repetidos y aparecen en mas de una
posición debería de indicarlas todas"""
import random
cantidad=int(input("Cuantos hago: "))
lista=[random.randint(10,20) for num in range(cantidad)]
maximo=max(lista)
maxPos=[str(n) for n, valor in enumerate(lista) if valor==max(lista)]
minimo=min(lista)
minPos=[n for n in range(cantidad) if lista[n]==min(lista)]
print(f"Lista: {lista}")
print(f"Máximo: {maximo}, posiciones: {", ".join(maxPos)}")
print(f"Mínimo: {minimo}, posiciones: {minPos}")
print(f"Promedio: {round(sum(lista)/len(lista),2)}")