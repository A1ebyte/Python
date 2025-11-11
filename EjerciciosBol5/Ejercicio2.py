"""2. Hacer un programa en que nos permita calcular todos los divisores comunes a dos
números"""
num1 = int(input("Introduce el primer número: "))
num2 = int(input("Introduce el segundo número: "))

divisores1 = {i for i in range(1, min(num1, num2) + 1) if num1 % i == 0}
divisores2 = {i for i in range(1, min(num1, num2) + 1) if num2 % i == 0}

divisores_comunes = divisores1 & divisores2  # intersección de conjuntos

print("Divisores comunes:", sorted(divisores_comunes))

"""
num1 = int(input("Introduce el primer número: "))
num2 = int(input("Introduce el segundo número: "))

divisores_comunes = []

for i in range(1, min(num1, num2) + 1):
    if num1 % i == 0 and num2 % i == 0:
        divisores_comunes.append(i)

print("Divisores comunes:", divisores_comunes)
"""