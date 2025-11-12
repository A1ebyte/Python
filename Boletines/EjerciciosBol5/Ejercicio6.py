"""6. Escribe un programa que nos permita contar el número de veces que se repite cada
cifra en un número. Por ejemplo, el número 885210003 tiene tres 0, un 1, un 2, un 5 y
dos 8."""
numero=885210003
numeroSet=set(str(numero))
for x in sorted(numeroSet):
    print("El numero",numero,"tiene",str(numero).count(x),x)