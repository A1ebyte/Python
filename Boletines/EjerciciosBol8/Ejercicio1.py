"""
Realiza un programa que dada una matriz almacenada en un array te calcule su transpuesta
y la almacene en otro diferente. Tu programa debería, ademas, dibujar en consola las
matrices de la siguiente forma:
| 1 2 |             | 1 3 |
| 3 4 |             | 2 4 |
"""

matriz = [[1, 0, 1], [3, 3, 4]]
transpuesta = []

for i in range(len(matriz[0])):
    arrayNuevo=[]
    for j in range(len(matriz)):
        arrayNuevo.append(matriz[j][i])
    transpuesta.append(arrayNuevo)

[print(numero) for numero in matriz]
print("*"*40)
[print(numero) for numero in transpuesta]
