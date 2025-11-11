#Listas se pueden modificar, las tuplas no
lista1=[]
lista2=list()
lista3=[1,2,3,4,5,5]
lista4=["eva","adam","moha"]
lista5=[1,"2",3,"4",False,5,"Perez",[1,2,3],4.56]
lista6=[0,54,4,5111,2,124,8,21454,24,54]


lista5=lista1+lista2
print(lista5)

lista5.extend(lista3)
print(lista5+lista4)

lista5.append(10)
listaCopy= lista5.copy()
print(lista5)
lista3.insert(1,333)
print(lista3)
ele=lista5.pop()
lista5.remove(1)
lista3.sort(reverse=True)
print(lista2)
print(lista5)


if 5 in lista1:
    print("si")
    print("Aparece",lista1.count(5),"veces")
    print("Aparece", lista1.index(5), "veces") #tira error si no esta en la lista
else:
    print("no")

partes = ["tres 0", "un 1", "un 2", "un 5", "dos 8"]
print(partes[-1])  #imprime el ultimo valor

text001="Hola Mundo Cruel"
lista7=list(text001)
print(lista7)
text002=str(lista7)
print(text002)
print("-".join(lista7))

numeros = [1, 0, 1, 1, 0, 1]
resultado = ''.join(str(n) for n in numeros)
print(resultado)  # '101101'
#tuplas y conjuntos en github de kerin