"""8. Escribe un programa que pida un número por teclado y escriba todos sus divisores
separados por comas (y evitando poner una coma al final). Por ejemplo, si el número
introducido es el 14 tu programa debería de mostrar lo siguiente:
Divisores del número 14: 1, 2, 7, 14"""

numero = int(input("Introduce un número: "))
divisores = []
for i in range(1, numero + 1):
    if numero % i == 0:
        divisores.append(i)

print(f"Divisores del número {numero}: {', '.join(str(num) for num in divisores)}")
#print(f"Divisores del número {numero}: {', '.join(map(str, divisores))}")  #hace el map para cambiar el tipo de los numeros a string
