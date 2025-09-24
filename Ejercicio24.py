#24. Modifica el programa anterior para que sea el usuario quién introduzca dos números y se nos
#muestre los primos que hay entre ambos
menor=int(input("Escribe el numero menor: "))
mayor=int(input("Escribe el numero mayor: "))
for num in range(menor,mayor):
    primo = True
    for numero in range(2, int(num ** .5) + 1):
        if num % numero == 0:
            primo = False
            break
    if primo:
        print(num, end=" ")