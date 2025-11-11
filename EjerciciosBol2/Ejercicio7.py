"""7. Escribir un programa que pida un número por teclado y nos imprima la tabla de
multiplicar de dicho número del 1 al 10. Por ejemplo, si introducimos el 74 el
resultado será algo así:
74 x 1 = 74
74 x 2 = 148
…
74 x 10 = 740
"""
num=input("Elige el numero: ")
for x in range(1,11):
    print(f"{num} x {x} = {int(num)*x}")