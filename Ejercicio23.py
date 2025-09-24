#23. Escribir un programa que te escriba todos los números primos que hay entre el 1 y el 100
for num in range(1,101):
    primo = True
    for numero in range(2, int(num ** .5) + 1):
        if num % numero == 0:
            primo = False
            break
    if primo:
        print(num, end=" ")