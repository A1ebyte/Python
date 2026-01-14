"""
7. EJERCICIO CON FORMATO DE EXAMEN
Un número es Armstrong cuando la suma de cada uno de los números que lo componen
elevado al número de dígitos de dicho número de dicho número da como resultado el propio
número.
Realiza un programa que, dado un número introducido por teclado, averigüe si es un número
Armstrong o Narcisista.
Ejemplo de un número de 3 dígitos: 153 ya que 13+53+33 = 1+125+27 = 153.
Todos los números de una cifra son narcisistas. De tres cifras tienes, además del anterior, el
370, el 371 y el 407 y de mas de tres cifras puedes probar con el 1634. No existen números
narcisistas de dos cifras.
Ejemplo de funcionamiento:
Introduce un número: 371
El número 371 es narcisista
No hace falta comprobaciones acerca de la entrada que siempre será un número entero.
"""

def es_armstrong(numero):
    digitos = [int(num) for num in str(numero)]
    elevarA = len(digitos)
    #suma = sum(num ** elevarA for num in digitos)
    suma = 0
    for num in digitos:
        suma += num ** elevarA
    return suma == numero

num = int(input("Introduce un número: "))
if es_armstrong(num):
    print(f"El número {num} es narcisista")
else:
    print(f"El número {num} no es narcisista")
