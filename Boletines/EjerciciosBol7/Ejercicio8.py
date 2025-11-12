"""8. Vamos a hacer una implementación del juego del buscaminas y lo primero es preparar el
tablero. Genera un array de dos dimensiones de 5 filas por 5 columnas. El tablero
tendrá 5 minas que se colocaran de forma aleatoria en cinco posiciones del array. Las
minas se representarán con un 1 y las posiciones sin mina con un 0. Al final dibuja el
tablero de esta forma:
0 0 0 0 0
0 0 1 0 0
0 0 1 0 1
0 0 0 0 0
1 1 0 0 0
"""
import random
filas = 5
columnas = 5
minas_total = 5

#tablero = [[0 for _ in range(columnas)] for _ in range(filas)]
tablero = [[0]*columnas for _ in range(filas)]
#print(tablero)

minas_colocadas = 0
while minas_colocadas < minas_total:
    f = random.randint(0, filas - 1)
    c = random.randint(0, columnas - 1)
    if tablero[f][c] == 0:  # solo colocamos mina si no hay ya una
        tablero[f][c] = 1
        minas_colocadas += 1

print("\n".join(" ".join(str(c) for c in arrayFilas) for arrayFilas in tablero))
"""
for fila in tablero:
    print(" ".join(str(c) for c in fila))"""
