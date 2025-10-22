lista=[20,45,55,29,20,24,14,45,20]
#lista=[15,2,7,4,3,6]
listaEditable=[]+lista
numerosRepetidos=[]
for x in listaEditable:
    if listaEditable.count(x)>1 and x not in numerosRepetidos:
        numerosRepetidos.append(x)
if len(numerosRepetidos)>0:
    print("Elementos repetidos:")
    for x in numerosRepetidos:
        print(f"El numero {x} aparece {lista.count(x)} veces")
else:
    print("No hay elementos repetidos")