"""
9. Escribir un programa que nos pida elegir entre cuatro destinos turísticos (Francia,
Italia, Chile o Japón) y dependiendo de nuestra respuesta nos diga cual es la capital de
nuestro destino (París, Roma, Santiago de Chile o Tokio)
"""
print("Francia,Italia, Chile o Japón")
pais=input("Elige uno: ").lower()
match pais:
    case "francia":
       print("Paris")
    case "italia":
        print("Roma")
    case "chile":
        print("Santiago")
    case "tokio":
        print("Tokio")
    case _:
        print("opcion no valida")