"""Añade una función que sirva para añadir nombres al diccionario. La llamada a la función sería así:
nuevoCliente(clientes, “Felipe”, “Lotas”, 76)
Tu función debería de añadir el nuevo cliente al diccionario con el formato correcto. Si este cliente ya
existe debería de mostrar en consola un mensaje advirtiéndolo y preguntando si se quiere
sobreescribir la edad o no. """

clientes = {
    "Chuletón, José": 35,
    "Tosidad, Rubén": 27,
    "Rupto, Francisco": 44,
    "Cotón, Carmelo": 56
}

def mostrar_clientes(clientes):
    lista = []

#items() devuelve pares clave–valor
    for clave, edad in clientes.items():
        apellidos, nombre = clave.split(", ")
        lista.append((nombre, apellidos, edad))

    lista.sort()  # ordena por nombre

    for nombre, apellidos, edad in lista:
        print(f"{nombre} {apellidos} ({edad})")

def nuevoCliente(clientes, nombre, apellido, edad):
    clave = f"{apellido}, {nombre}"

    if clave in clientes:
        respuesta = input("El cliente ya existe. ¿Sobreescribir edad? (s/n): ")
        if respuesta.lower() == "s":
            clientes[clave] = edad
    else:
        clientes[clave] = edad


nuevoCliente(clientes, "Felipe", "Lotas", 76)
mostrar_clientes(clientes)