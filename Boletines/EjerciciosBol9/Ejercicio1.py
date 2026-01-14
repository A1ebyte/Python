"""Crear un programa o una función que reciba un diccionario con los datos de los clientes de una tienda
y su edad y los muestre por consola ordenados por nombre de pila. El diccionario, ya creado en el
código de tu programa, tendrá esta forma
clientes = { "Chuletón, José": 35, "Tosidad, Rubén": 27, "Rupto, Francisco": 44, "Cotón, Carmelo": 56 }
Y la salida por consola así:
Carmelo Cotón (56)
Francisco Rupto (44)
José Chuletón (35)
Rubén Tosidad (27)
"""

def mostrar_clientes(clientes):
    lista = []

#items() devuelve pares clave–valor
    for clave, edad in clientes.items():
        apellidos, nombre = clave.split(", ")
        lista.append((nombre, apellidos, edad))

    lista.sort()  # ordena por nombre

    for nombre, apellidos, edad in lista:
        print(f"{nombre} {apellidos} ({edad})")

clientes = {
    "Chuletón, José": 35,
    "Tosidad, Rubén": 27,
    "Rupto, Francisco": 44,
    "Cotón, Carmelo": 56
}

mostrar_clientes(clientes)
