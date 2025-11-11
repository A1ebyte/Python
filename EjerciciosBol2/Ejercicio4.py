"""Escribir un programa que nos pida por teclado dos calificaciones numéricas de un
alumno y nos muestre la media aritmética resultante redondeada sin decimales. Las
notas introducidas deben de estar entre 0 y 10 y admiten decimales. Caso de que una
entrada sea errónea debería de advertirnos de ello y no hacer el cálculo
"""
try:
    nota1=float(input("Ingrese la 1era nota: "))
    nota2=float(input("Ingrese la 2da nota: "))
    if not 0<=nota1<=10 or not 0<=nota2<=10:
        raise Exception
except:
    print("Uno de los valores no es valido")
print(round(nota1+nota2))