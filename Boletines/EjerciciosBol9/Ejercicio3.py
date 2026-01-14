"""Por último, crea ahora una función que sume un año a la edad de un cliente. La llamada sería así:
cumpleCliente(clientes, “José”, “Chuletón”)
Si el cliente existe debería de sumar un año a su edad. Si no existe debería de informar de ello por
consola y no hacer nada
"""

clientes = {
    "Chuletón, José": 35,
    "Tosidad, Rubén": 27,
    "Rupto, Francisco": 44,
    "Cotón, Carmelo": 56
}

def cumpleCliente(clientes, nombre, apellido):
    clave = f"{apellido}, {nombre}"

    if clave in clientes:
        clientes[clave] += 1
        print(f"{nombre} ha cumplido años. Nueva edad: {clientes[clave]}")
    else:
        print("El cliente no existe.")

def mostrar_clientes(clientes):
    lista = []

#items() devuelve pares clave–valor
    for clave, edad in clientes.items():
        apellidos, nombre = clave.split(", ")
        lista.append((nombre, apellidos, edad))

    lista.sort()  # ordena por nombre

    for nombre, apellidos, edad in lista:
        print(f"{nombre} {apellidos} ({edad})")

mostrar_clientes(clientes)
cumpleCliente(clientes, "José", "Chuletón")
mostrar_clientes(clientes)
