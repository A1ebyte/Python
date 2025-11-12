import random

dados=input("Cuantos dados quieres tirar: ")
porcentajes=[0,0,0,0,0,0]
tiradas=0
terminar=False
while not dados.isdigit():
    dados=input("Escribe un numero/valor valido: ")
while not terminar:
    totalDados=[]
    tiradas+=1
    for x in range(0,int(dados)):
        if random.randint(1, 3)>1:
            valor=6
        else:
            valor=random.randint(1, 6)
        porcentajes[valor-1]+=1
        totalDados.append(str(valor))
        terminar = True if totalDados.count(totalDados[0]) == int(dados) else False
    """for x in range(0,len(totalDados)):
        if totalDados[x]!=totalDados[(x+1 if x<len(totalDados)-1 else 0)]:
            terminar=False
            break
        else:
            terminar=True"""
    print(" - ".join(totalDados))
for x in range(0,len(porcentajes)):
    print(f"El numero {x+1} ha salido el {round((porcentajes[x]/(tiradas*int(dados))*100),2)}")
print(f"He tenido que lanzar los dados: {tiradas} veces para que todos sean iguales")