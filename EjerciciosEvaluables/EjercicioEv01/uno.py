import random

dados=input("Cuantos dados quieres tirar: ")
tiradas=0
terminar=False
while not dados.isdigit():
    dados=input("Escribe un numero/valor valido: ")
while not terminar:
    totalDados=[]
    tiradas+=1
    for x in range(0,int(dados)):
        totalDados.append(str(random.randint(1, 6)))  #si aqui no lo convierto en str al hacer el join da errores raros
    terminar=True if totalDados.count(totalDados[0])==int(dados) else False
    print(" - ".join(totalDados))
print(f"He tenido que lanzar los dados: {tiradas} veces para que todos sean iguales")
